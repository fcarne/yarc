from typing import Optional

from antlr3 import ANTLRFileStream, CommonTokenStream

from yarc.parser.YarcLexer import YarcLexer
from yarc.parser.YarcParser import YarcParser


class Yarc:
    def __init__(self, input_path: str, lib: Optional[str] = None, **kwargs):
        input_file = ANTLRFileStream(input_path)
        lexer = YarcLexer(input_file)
        stream = CommonTokenStream(lexer)
        self.parser = YarcParser(stream)

        self.lib = lib
        self.handler_args = kwargs

    def parse(self) -> str:
        if self.lib is not None:
            self.parser.set_handler(self.lib, self.handler_args)

        return self.parser.scenario(handler_kwargs=self.handler_args)

    @property
    def errors(self) -> dict[str, str]:
        return self.parser.handler.error_dict

    @property
    def warnings(self) -> dict[str, str]:
        return self.parser.handler.warning_dict
