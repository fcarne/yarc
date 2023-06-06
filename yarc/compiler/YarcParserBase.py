from typing import Any

from antlr3 import Parser, Token
from antlr3.exceptions import MissingTokenException
from antlr3.recognizers import RecognizerSharedState
from antlr3.streams import CharStream

from yarc.compiler.handlers.formatters.error_formatter import ErrorType
from yarc.compiler.handlers.handler import Handler
from yarc.compiler.handlers.handler_factory import HandlerFactory


class YarcParserBase(Parser):
    def __init__(
        self,
        input: CharStream,
        state: RecognizerSharedState | None = None,
        *args: Any,
        **kwargs: Any,
    ):
        super().__init__(input, state, *args, **kwargs)

        self.__handler: Handler

    @property
    def handler(self) -> Handler:
        return self.__handler

    def set_handler(self, lib: str, handler_kwargs: dict[str, Any]) -> None:
        if not hasattr(self, "__handler"):
            self.__handler = HandlerFactory.get_handler(
                parser=self, lib=lib, handler_kwargs=handler_kwargs
            )

    def displayRecognitionError(self, e):
        from yarc.compiler.token_mapping import TOKEN_TYPE_TO_TEXT
        from yarc.compiler.YarcLexer import DEDENT, EOF, INDENT, NEWLINE, tokenNamesMap

        tk: Token = self.input.LT(1)
        msg = None
        if isinstance(e, MissingTokenException) and e.expecting == INDENT:
            error_type = ErrorType.INDENTATION_ERROR

            i = -1
            anchor: Token = self.input.LT(i)
            while anchor.type != NEWLINE:
                i -= 1
                anchor = self.input.LT(i)

            msg = f"expected an indented block after statement on line {anchor.line}"
        elif tk.type == INDENT:
            error_type = ErrorType.INDENTATION_ERROR
        elif tk.type == DEDENT or (
            isinstance(e, MissingTokenException) and e.expecting == EOF
        ):
            error_type = ErrorType.INDENTATION_ERROR
            msg = "unindent does not match any outer indentation level"
        elif isinstance(e, MissingTokenException):
            error_type = ErrorType.SYNTAX_ERROR
            token_text = TOKEN_TYPE_TO_TEXT.get(e.expecting, tokenNamesMap[e.expecting])
            msg = f"expected '{token_text}'"
        else:
            error_type = ErrorType.SYNTAX_ERROR

        self.handler.handle_error(type=error_type, msg=msg, tk=tk)
