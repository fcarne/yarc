from typing import Any, NamedTuple, Optional, Union

import abc
import random
import string
import time

from antlr3 import Parser, Token

from yarc.dsl.v3.handler.error_formatter import ErrorFormatter, ErrorType
from yarc.dsl.v3.handler.simbol_stack import SymbolStack
from yarc.dsl.v3.handler.warning_formatter import WarningFormatter, WarningType


class Attribute(NamedTuple):
    name: str
    value: Any
    st: str


class Parameter(NamedTuple):
    name: str
    value: Any


class Handler(abc.ABC):
    BEHAVIOR = "behavior"

    def __init__(self, parser: Parser, warnings: bool = False):
        random.seed(42)
        self.parser = parser

        self.default_settings = {
            "root_path": ".",
            "seed": int(time.time() * 1000),
            "num_scenes": 1,
            "fps": 24,
            "stage_meters_per_unit": 1,
            "stage_up_axis": "y",
            # "output_dir": "*/output",
            "resolution": [512, 512],
        }
        self.settings: dict[str, str] = {}

        self.symbol_stack = SymbolStack()
        self.should_lookup = True
        self.forward_references: list[tuple(str, Token)] = []

        self.error_dict: dict[str, str] = {}
        self.error_formatter = ErrorFormatter(parser.input)

        self.warning_dict: dict[str, str] = {}
        self.warning_formatter = WarningFormatter()
        self.show_warnings = warnings

    def _rewrite_defaults(self, settings: dict[str, Any]) -> None:
        return {
            key: f'"{value}"' if isinstance(value, str) else str(value)
            for key, value in settings.items()
        }

    def is_special_setting(self, setting: Token) -> bool:
        return setting.text in self.default_settings

    def add_setting(self, setting: Token, value: Any) -> None:
        setting_text = setting.text

        if self.show_warnings and setting_text in self.settings:
            self.handle_warning(
                WarningType.DUPLICATED_SETTING, setting, setting=setting_text
            )

        self.settings[setting_text] = str(value)

    def special_setting_to_str(self, setting: Token | str, value: Any) -> str:
        setting = setting.text if isinstance(setting, Token) else str(setting)
        match setting:
            case "stage_up_axis":
                return f"rep.settings.set_stage_up_axis({value})"
            case "stage_meters_per_unit":
                return f"rep.settings.set_stage_meters_per_unit({value})"
            case "seed":
                return f"rep.set_global_seed({value})"
            case "fps":
                return f"# I don't remember how to do it XD"
            case _:
                return None

    def settings_to_str(self, indent: int = 2) -> str:
        default_not_changed = {
            k: v for k, v in self.default_settings.items() if k not in self.settings
        }
        settings = self._rewrite_defaults(default_not_changed) | self.settings

        settings_str = "{\n"
        for key, value in settings.items():
            settings_str += " " * indent + f"'{key}': {value},\n"
        settings_str += "}\n\n"

        default_not_changed_rewrite = [
            rewrited
            for k, v in default_not_changed.items()
            if (rewrited := self.special_setting_to_str(k, v)) is not None
        ]
        settings_str += "\n".join(default_not_changed_rewrite)

        return settings_str

    def push_stack(self) -> None:
        self.symbol_stack.push()

    def pop_stack(self) -> None:
        vars = self.symbol_stack.pop()

        if self.show_warnings:
            unused_vars = [var for var in vars.symbols if not var.used]
            for var in unused_vars:
                self.handle_warning(WarningType.UNUSED_VARIABLE, var=var.name)

    def define(self, vars: list[str]) -> None:
        for var in vars:
            self.symbol_stack.define(var, Any)

    def lookup(self, var: str, tk: Optional[Token] = None) -> None:
        if tk is None:
            tk: Token = self.parser.input.LT(-1)

        if self.should_lookup:
            if self.symbol_stack.lookup(var) is None:
                self.handle_error(tk=tk, hdr=ErrorType.NAME_ERROR, name=var)
        else:
            self.forward_references.append((var, tk))

    def disable_lookup(self) -> None:
        self.should_lookup = False

    def enable_lookup(self) -> None:
        self.should_lookup = True
        for var, tk in self.forward_references:
            self.lookup(var=var, tk=tk)

        self.forward_references.clear()

    def parse_snippet(self, snippet: Token) -> str:
        raise NotImplementedError

    def get_params(
        self, token: Token, attrs: list[Attribute], warnings: bool = False, **kwargs
    ) -> list[Attribute]:
        raise NotImplementedError

    def get_attrs(self, token: Token, attrs: list[Attribute]) -> list[str]:
        raise NotImplementedError

    def get_behaviors(self, attrs: list[Attribute]) -> list[str]:
        raise NotImplementedError

    def map(self, *tokens: list[Union[Token, str]]) -> str:
        raise NotImplementedError

    def check_writer(self, writer: Token, params: list[Parameter]) -> None:
        raise NotImplementedError

    def check_target(self, tk: Token) -> None:
        raise NotImplementedError

    def is_frame(self, type: Token) -> bool:
        return "frame" in type.text

    def get_random_uid(self) -> str:
        suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"prim_{suffix}"

    def expand_string(self, s: Union[Token, str]) -> str:
        if isinstance(s, Token):
            s = s.text

        root_path = (
            self.settings["root_path"][1:-1]
            if "root_path" in self.settings
            else self.default_settings["root_path"]
        )
        if s[1:3] in ["*/", "*\\"]:
            return s[-1] + root_path + s[2:]
        else:
            return s

    def parse_setting_id(self, setting_id: Token) -> str:
        setting = setting_id.text.lstrip("$")

        if setting not in self.settings and setting not in self.default_settings:
            self.handle_error(
                tk=setting_id, hdr=ErrorType.SETTING_ERROR, setting=setting
            )

        return setting.lstrip("$")

    def handle_error(
        self, tk: Token, hdr: ErrorType | str, msg: Optional[str] = None, **kwargs
    ) -> None:
        show_anchors = True
        if tk is None:
            tk = self.input.LT(-1)

        if hdr == ErrorType.INDENTATION_ERROR:
            show_anchors = False

        if msg is None:
            msg = hdr.default_msg.format(*kwargs.values())

        hdr = hdr.type
        hdr += f" at line {tk.line}"

        self.error_dict[hdr] = self.error_formatter.format(
            tk, msg, show_anchors=show_anchors
        )

    def handle_warning(
        self, type: WarningType, tk: Optional[Token] = None, **kwargs
    ) -> None:
        hdr = type.value

        if tk is not None:
            hdr += f" at line {tk.line}"

        self.warning_dict[hdr] = self.warning_formatter.get_warning_message(
            type, **kwargs
        )
