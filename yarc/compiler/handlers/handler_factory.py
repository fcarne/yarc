from typing import Any, Optional

from pathlib import Path

import stringtemplate3
from antlr3 import Parser

from yarc.compiler.handlers.exceptions import YARCException
from yarc.compiler.handlers.formatters.error_formatter import ErrorType
from yarc.compiler.handlers.handler import Handler
from yarc.compiler.handlers.replicator_handler import OmniReplicatorHandler
from yarc.templates import TEMPLATES_DIR


class HandlerFactory:
    supported_libraries: dict[str, tuple[type[Handler], Path]] = {
        "Replicator": (
            OmniReplicatorHandler,
            TEMPLATES_DIR / "replicator.stg",
        )
    }

    @staticmethod
    def is_library_supported(lib):
        return lib in HandlerFactory.supported_libraries

    @staticmethod
    def get_handler(
        parser: Parser, lib: str, handler_kwargs: Optional[dict[str, Any]] = None
    ) -> Handler:
        if HandlerFactory.is_library_supported(lib) is False:
            raise YARCException(error_type=ErrorType.LIB_ERROR, lib=lib)

        handler, template_path = HandlerFactory.supported_libraries[lib]
        with open(template_path) as template:
            parser.templateLib = stringtemplate3.StringTemplateGroup(file=template)

        if handler_kwargs is None:
            handler_kwargs = {}

        return handler(parser, **handler_kwargs)
