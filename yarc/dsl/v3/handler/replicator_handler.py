import importlib

from yarc.dsl.v3.handler.handler import Handler


def import_guard() -> bool:
    try:
        spec = importlib.util.find_spec("omni.replicator.core")
        return spec is not None
    except (ImportError, ModuleNotFoundError):
        return False


class OmniReplicatorHandler(Handler):
    ...
