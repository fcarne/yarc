from antlr3 import Parser, Token
from antlr3.exceptions import MissingTokenException

from yarc.parser.handlers.formatters.error_formatter import ErrorType
from yarc.parser.handlers.handler import Handler


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
        from yarc.parser.token_mapping import TOKEN_TYPE_TO_TEXT
        from yarc.parser.YarcLexer import DEDENT, EOF, INDENT, NEWLINE, tokenNamesMap

        tk = self.input.LT(1)

        e_msg = self.getErrorMessage(e)
        msg = None
        if isinstance(e, MissingTokenException) and e.expecting == INDENT:
            hdr = ErrorType.INDENTATION_ERROR

            i = -1
            anchor: Token = self.input.LT(i)
            while anchor.type != NEWLINE:
                i -= 1
                anchor = self.input.LT(i)

            msg = f"expected an indented block after statement on line {anchor.line}"
        elif tk.type == INDENT:
            hdr = ErrorType.INDENTATION_ERROR
        elif tk.type == DEDENT or (
            isinstance(e, MissingTokenException) and e.expecting == EOF
        ):
            hdr = ErrorType.INDENTATION_ERROR
            msg = "unindent does not match any outer indentation level"
        elif isinstance(e, MissingTokenException):
            hdr = ErrorType.SYNTAX_ERROR
            token_text = TOKEN_TYPE_TO_TEXT.get(e.expecting, tokenNamesMap[e.expecting])
            msg = f"expected '{token_text}'"
        else:
            hdr = ErrorType.SYNTAX_ERROR

        self.handler.handle_error(tk, hdr, msg)
