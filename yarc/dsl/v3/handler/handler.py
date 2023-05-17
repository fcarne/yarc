from typing import Any, NamedTuple, Optional, Union

import abc
import random
import string
import time

from antlr3 import Parser, Token

from yarc.dsl.v3.handler.error_handler import ErrorHandler
from yarc.dsl.v3.handler.simbol_stack import SymbolStack


class Attribute(NamedTuple):
    name: str
    value: Any
    st: str


class Parameter(NamedTuple):
    name: str
    value: Any


class Handler(abc.ABC):
    operators = {
        "+": ["__add__", "__concat__"],
        "-": "__sub__",
        "*": "__mul__",
        "/": "__truediv__",
        "//": "__floordiv__",
        "%": "__mod__",
        "**": "__pow__",
        "pos": "__pos__",
        "neg": "__neg__",
        "&": "__and__",
        "|": "__or__",
        "^": "__xor__",
        "~": ["__invert__", "__inv__"],
        "<": "__lt__",
        "<=": "__le__",
        "==": "__eq__",
        "!=": "__ne__",
        ">=": "__ge__",
        ">": "__gt__",
        "<<": "__lshift__",
        ">>": "__rshift__",
        "and": "__bool__",
        "or": "__bool__",
        "not": "__not__",
        "in": "__contains__",
    }

    in_place_operators = {
        "+=": ["__iadd__", "__iconcat__"],
        "-=": "__isub__",
        "*=": "__imul__",
        "/=": "__idiv__",
        "//=": "__ifloordiv__",
        "%=": "__imod__",
        "**=": "__ipow__",
        "&=": "__iand__",
        "|=": "__ior__",
        "^=": "__ixor__",
        "<<=": "__ilshift__",
        ">>=": "__irshift__",
    }

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

        self.__symbol_stack = SymbolStack()

        self.error_handler = ErrorHandler(parser.input)
        self.error_list: list[str] = []
        self.warning_list: list[str] = []

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

    @property
    def symbol_stack(self) -> SymbolStack:
        return self.__symbol_stack

    def parse_snippet(self, snippet: Token) -> str:
        return snippet.text

    def get_attrs(self, directive: str, attrs: Optional[list[Attribute]]) -> list[str]:
        if attrs is None:
            return []
        return [attr.st for attr in attrs if attr.name != "behavior"]

    def get_behaviors(self, attrs: list[Attribute]) -> list[str]:
        if attrs is None:
            return []
        return [attr.st for attr in attrs if attr.name == "behavior"]

    def get_params(
        self, directive: str, attrs: list[Attribute], extra_param: Optional[Any] = None
    ) -> list[Attribute]:
        if attrs is None:
            return []
        return [Attribute("extra_param", extra_param, "")]

    def map(self, *tokens: list[Union[Token, str]]) -> str:
        tokens = [
            token.text if isinstance(token, Token) else str(token) for token in tokens
        ]
        return "_".join(tokens)

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

    def handle_error(self, tk: Token, hdr: str, msg: str) -> None:
        if tk is None:
            tk = self.input.LT(-1)

        position = f"[{tk.line},{tk.charPositionInLine + 1}]"
        token_text = f"'{tk.text}'"
        error_msg = f"Error at {position}: on token {token_text}"
        error_msg += "\n" + hdr + "\n**********\n" + msg

        self.error_list.append(self.error_handler.format_error(tk, error_msg))

    def check_writer_params(self, writer_params: list[Attribute]) -> None:
        pass

    def parse_setting_id(self, setting_id: Union[str, Token]) -> str:
        setting_id = setting_id.text if isinstance(setting_id, Token) else setting_id
        return setting_id.lstrip("$")

    def check_declared() -> None:
        pass
