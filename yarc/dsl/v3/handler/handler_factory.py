from pathlib import Path

import stringtemplate3

from yarc.dsl.v3 import YarcParser
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

    def get_handler(lib, parser: YarcParser, **kwargs) -> type[Handler]:
        handler, template_path = HandlerFactory.supported_libraries.get(
            lib, "Replicator"
        )

        with open(template_path) as template:
            parser.templateLib = stringtemplate3.StringTemplateGroup(file=template)

        return handler(**kwargs)
