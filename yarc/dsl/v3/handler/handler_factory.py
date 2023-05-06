import os
from pathlib import Path

from yarc.dsl.v3.handler.handler import Handler
from yarc.dsl.v3.handler.replicator_handler import OmniReplicatorHandler


class HandlerFactory:
    TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"

    supported_libraries: dict[str, tuple[type[Handler], Path]] = {
        "Replicator": (
            OmniReplicatorHandler,
            os.path.join(TEMPLATE_DIR, "replicator.stg"),
        )
    }

    def is_library_supported(self, lib):
        return lib in self.supported_libraries

    def get_handler(self, lib, **kwargs) -> tuple[Handler, str]:
        (handler, template_path) = self.supported_libraries.get(lib, "Replicator")
        return (handler(**kwargs), str(template_path))
