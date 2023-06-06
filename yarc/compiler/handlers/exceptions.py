from typing import Any, Optional

from yarc.compiler.handlers.formatters.error_formatter import ErrorType


class YARCException(Exception):
    def __init__(
        self, error_type: ErrorType, msg: Optional[str] = None, **kwargs: Any
    ) -> None:
        self.error_type = error_type
        self.message = (
            msg if msg is not None else error_type.default_msg.format(*kwargs.values())
        )

        super().__init__(f"{self.error_type.type}: {self.message}")
