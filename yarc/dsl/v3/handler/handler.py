from typing import Any, NamedTuple, Optional, Union

import random
import string

from antlr3 import Token

from yarc.dsl.v3.handler.simbol_stack import SymbolStack


class Attribute(NamedTuple):
    name: str
    value: float
    st: str


class Handler:
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

    def __init__(self):
        random.seed(42)

        self.__comments = []
        self.__snippets = []

        self.__symbol_stack = SymbolStack()

    def add_comment(self, comment: str) -> None:
        self.__comments.append(comment.lstrip("# ").strip())

    def add_snippet(self, snippet: str) -> None:
        self.__snippets.append(snippet.lstrip("{{").rstrip("}}").strip())

    @property
    def comments(self) -> list[str]:
        return self.__comments

    @property
    def snippets(self) -> list[str]:
        return self.__snippets

    @property
    def symbol_stack(self) -> SymbolStack:
        return self.__symbol_stack

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
