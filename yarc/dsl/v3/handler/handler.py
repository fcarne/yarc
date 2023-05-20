from typing import Any, NamedTuple, Union

import abc
import random
import string
import time

from antlr3 import Parser, Token

from yarc.dsl.v3.handler.error_formatter import ErrorFormatter
from yarc.dsl.v3.handler.simbol_stack import SymbolStack

# from yarc.dsl.v3.YarcLexer import FRAMES


class Attribute(NamedTuple):
    name: str
    value: Any
    st: str


class Parameter(NamedTuple):
    name: str
    value: Any


class Handler(abc.ABC):
    BEHAVIOR = "behavior"

    def __init__(self, parser: Parser):
        random.seed(42)
        self.parser = parser

        self.default_settings = {
            "root_path": ".",
            "seed": int(time.time() * 1000),
            "num_scenes": 1,
            "fps": 24,
            "stage_meters_per_unit": 1,
            "stage_up_axis": "y",
            # "output_dir": "./output",
            "resolution": [512, 512],
        }
        self._map_settings()

        self.symbol_stack = SymbolStack()

        self.error_formatter = ErrorFormatter(parser.input)
        self.error_list: dict[str, str] = {}
        self.warning_list: dict[str, str] = {}

    def _map_settings(self) -> None:
        self.settings = {
            key: f'"{value}"' if isinstance(value, str) else str(value)
            for key, value in self.default_settings.items()
        }
        self.default_changed = {key: False for key in self.default_settings}

    def is_special_setting(self, setting: str) -> bool:
        return setting in self.default_settings

    def add_setting(self, setting: str, value: Any) -> None:
        self.settings[setting] = str(value)
        if setting in self.default_changed:
            self.default_changed[setting] = True

    def special_setting_to_str(self, setting: str, value: Any) -> str:
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
        settings_str = "{\n"
        for key, value in self.settings.items():
            settings_str += " " * indent + f"'{key}': {value},\n"
        settings_str += " " * (indent - 2) + "}\n\n"

        default_to_str = [
            self.special_setting_to_str(key, value)
            for key, value in self.settings.items()
            if not self.default_changed.get(key, True)
        ]

        settings_str += "\n".join(
            default for default in default_to_str if default is not None
        )

        return settings_str

    def push_stack(self) -> None:
        self.symbol_stack.push()

    def pop_stack(self) -> None:
        vars = self.symbol_stack.pop()
        [var for var in vars._symbols if not var.used]
        # TODO: add Warning for unused variables

    def define(self, vars: list[str]) -> None:
        for var in vars:
            self.symbol_stack.define(var, Any)

    def lookup(self, var: str) -> None:
        if self.symbol_stack.lookup(var) is None:
            # TODO: add undeclared error
            pass

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

    def check_writer_params(self, writer_params: list[Parameter]) -> None:
        raise NotImplementedError

    def check_target(self, filter) -> None:
        raise NotImplementedError

    def is_frame(self, type: Token) -> bool:
        return "frame" in type.text

    def get_random_uid(self) -> str:
        suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"prim_{suffix}"

    def expand_string(self, s: Union[Token, str]) -> str:
        if isinstance(s, Token):
            s = s.text

        if s[1:3] in ["*/", "*\\"]:
            return s[-1] + self.settings["root_path"][1:-1] + s[2:]
        else:
            return s

    def parse_setting_id(self, setting_id: Token) -> str:
        setting = setting_id.text

        if setting not in self.settings:
            # TODO: error/warning
            pass

        return setting.lstrip("$")

    def handle_error(self, tk: Token, hdr: str, msg: str) -> None:
        if tk is None:
            tk = self.input.LT(-1)

        position = f"[{tk.line},{tk.charPositionInLine + 1}]"
        token_text = f"'{tk.text}'"
        error_msg = f"Error at {position}: on token {token_text}"
        error_msg += "\n" + hdr + "\n**********\n" + msg

        self.error_list[hdr] = self.error_formatter.format(tk, msg)
