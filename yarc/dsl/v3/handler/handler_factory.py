from typing import Any, Optional

from pathlib import Path

import stringtemplate3
from antlr3 import Parser

from yarc.dsl.v3.handler.error_formatter import ErrorType
from yarc.dsl.v3.handler.handler import Handler
from yarc.dsl.v3.handler.replicator_handler import OmniReplicatorHandler


class HandlerFactory:
    TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"

    supported_libraries: dict[str, tuple[type[Handler], Path]] = {
        "Replicator": (
            OmniReplicatorHandler,
            TEMPLATE_DIR / "replicator.stg",
        )
    }

    @staticmethod
    def is_library_supported(lib):
        return lib in HandlerFactory.supported_libraries

    @staticmethod
    def get_handler(
        lib, parser: Parser, handler_kwargs: Optional[dict[str, Any]] = None
    ) -> type[Handler]:
        if HandlerFactory.is_library_supported(lib) is False:
            raise ValueError(
                f"{ErrorType.LIB_ERROR}: {ErrorType.LIB_ERROR.default_msg.format(lib)} "
            )

        handler, template_path = HandlerFactory.supported_libraries[lib]
        with open(template_path) as template:
            parser.templateLib = stringtemplate3.StringTemplateGroup(file=template)

        if handler_kwargs is None:
            handler_kwargs = {}

        return handler(parser, **handler_kwargs)
