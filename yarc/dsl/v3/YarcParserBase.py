from antlr3 import Parser

from yarc.dsl.v3.handler.handler import Handler


class YarcParserBase(Parser):
    def __init__(self, input, state=None, *args, **kwargs):
        super().__init__(input, state, *args, **kwargs)

        self.__handler = None

    @property
    def handler(self) -> type[Handler]:
        return self.__handler

    @handler.setter
    def handler(self, handler) -> None:
        if self.__handler is None:
            self.__handler = handler

    def displayRecognitionError(self, e):
        hdr = " * " + self.getErrorHeader(e)
        msg = " - " + self.getErrorMessage(e)
        tk = self.input.LT(1)

        self.handler.handle_error(tk, hdr, msg)
