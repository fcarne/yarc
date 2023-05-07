from yarc.dsl.v3.handler.simbol_stack import SymbolStack


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
