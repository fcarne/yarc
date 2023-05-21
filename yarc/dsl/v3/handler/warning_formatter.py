import difflib
from enum import Enum


class WarningType(Enum):
    UNUSED_VARIABLE = "unused_variable"
    UNKNOWN_PARAM = "unknown_parameter"
    UNSUPPORTED_GET_TARGET = "unsupported_get_target"


class WarningFormatter:
    def get_warning_message(self, type: WarningType, **kwargs) -> str:
        match type:
            case WarningType.UNUSED_VARIABLE:
                return f"variable '{kwargs['var']}' declared but never used. ╭( ๐_๐)╮"
            case WarningType.UNKNOWN_PARAM:
                return f"unknown parameter '{kwargs['param']}' for '{kwargs['command']}'. {self.closest_suggestion(kwargs['param'], kwargs['accepted_params'])}(⊙_☉)"
            case WarningType.UNSUPPORTED_GET_TARGET:
                return f"unsupported target '{kwargs['target']}'. {self.closest_suggestion(kwargs['target'], kwargs['supported_targets'])}(´つヮ⊂)"
            case _:
                return f"(ノ-_-)ノ ミ ┴┴"

    def closest_suggestion(self, name: str, accepted: set[str]) -> str:
        closest_match = difflib.get_close_matches(name, accepted)
        if closest_match:
            suggestion = closest_match[0]
            return f"Did you mean '{suggestion}'? "
        else:
            return ""

    # def format(self, msg: str, line: Optional[int] = None) -> str:
    #     warning = f"Warning"
    #     if line:
    #         warning += f" at line {line}"
    #     warning += f": {msg}"
    #     return warning
