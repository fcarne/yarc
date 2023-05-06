from pathlib import Path

import stringtemplate3

from yarc.dsl.v3 import YarcParser
from yarc.dsl.v3.handler.handler import Handler
from yarc.dsl.v3.handler.replicator_handler import OmniReplicatorHandler


class HandlerFactory:
    TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"

    supported_libraries: dict[str, tuple[type[Handler], Path]] = {
        "Replicator": (
            OmniReplicatorHandler,
            TEMPLATE_DIR / "replicator.stg",
        )
    }

    def is_library_supported(self, lib):
        return lib in self.supported_libraries

    def get_handler(self, lib, parser: YarcParser, **kwargs) -> type[Handler]:
        handler, template_path = self.supported_libraries.get(lib, "Replicator")
        parser.templateLib = stringtemplate3.StringTemplateGroup(
            file=str(template_path)
        )

        return handler(**kwargs)
