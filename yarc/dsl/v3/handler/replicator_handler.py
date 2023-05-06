import importlib

from yarc.dsl.v3.handler.guard_method_calls import guard_method_calls
from yarc.dsl.v3.handler.handler import Handler


# TODO: check if Omni Replicator  is in path
@guard_method_calls(importlib.util.find_spec("omni.replicator.core") is not None)
class OmniReplicatorHandler(Handler):
    ...
