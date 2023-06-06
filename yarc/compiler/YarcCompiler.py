from typing import Any, Optional

from pathlib import Path

from antlr3 import ANTLRFileStream, CommonTokenStream

from yarc.compiler.YarcLexer import YarcLexer
from yarc.compiler.YarcParser import YarcParser


class YarcCompiler:
    def __init__(self, input: str | Path, lib: Optional[str] = None, **kwargs: Any):
        if isinstance(input, Path):
            input = input.absolute()

        input_file = ANTLRFileStream(input)
        lexer = YarcLexer(input_file)
        stream = CommonTokenStream(lexer)
        self.parser = YarcParser(stream)

        self.lib = lib
        self.handler_args = kwargs

    def compile(self) -> str:
        if self.lib is not None:
            self.parser.set_handler(self.lib, self.handler_args)

        return str(self.parser.scenario(handler_kwargs=self.handler_args)).strip()

    @property
    def errors(self) -> dict[str, str]:
        return self.parser.handler.error_dict

    @property
    def warnings(self) -> dict[str, str]:
        return self.parser.handler.warning_dict
