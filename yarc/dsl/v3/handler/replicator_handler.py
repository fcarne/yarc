import importlib

from yarc.dsl.v3.handler.guard_method_calls import guard_method_calls
from yarc.dsl.v3.handler.handler import Handler


def import_guard() -> bool:
    try:
        spec = importlib.util.find_spec("omni.replicator.core")
        return spec is not None
    except (ImportError, ModuleNotFoundError):
        return False


# TODO: check if Omni Replicator  is in path
@guard_method_calls(import_guard())
class OmniReplicatorHandler(Handler):
    ...
