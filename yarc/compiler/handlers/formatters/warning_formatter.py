from typing import Any, Optional

import difflib
from enum import Enum


class WarningType(Enum):
    UNUSED_VARIABLE = "UnusedVariable"
    UNKNOWN_PARAMETER = "UnknownParamter"
    UNSUPPORTED_GET_TARGET = "UnsupportedTarget"
    DUPLICATED_SETTING = "DuplicatedSetting"
    OVERWRITTEN_ATTRIBUTE = "OverwrittenAttributes"
    MISSING_WRITER_PARAMETER = "MissingWriterParameter"


class WarningFormatter:
    def get_warning_message(self, type: WarningType, **kwargs: Any) -> str:
        match type:
            case WarningType.UNUSED_VARIABLE:
                return f"variable '{kwargs['var']}' declared but never used"
            case WarningType.UNKNOWN_PARAMETER:
                suggestion = self.closest_suggestion(
                    kwargs["param"], kwargs["accepted_params"]
                )
                return f"unknown parameter '{kwargs['param']}' for '{kwargs['command']}'{ ' . ' + suggestion if suggestion else ''}"
            case WarningType.UNSUPPORTED_GET_TARGET:
                suggestion = self.closest_suggestion(
                    kwargs["target"], kwargs["supported_targets"]
                )
                return f"unsupported target '{kwargs['target']}'{ ' . ' + suggestion if suggestion else ''}"
            case WarningType.DUPLICATED_SETTING:
                return f"'{kwargs['setting']}' has already been set"
            case WarningType.OVERWRITTEN_ATTRIBUTE:
                return f"'{kwargs['others']}' overrided by {kwargs['last']}"
            case WarningType.MISSING_WRITER_PARAMETER:
                return f"missing parameter '{kwargs['param']}' for writer '{kwargs['writer']}'{'. Defaulted to {} '.format(kwargs['default']) if 'default' in kwargs else ''}"

    def closest_suggestion(self, name: str, accepted: set[str]) -> Optional[str]:
        closest_match = difflib.get_close_matches(name, accepted)
        if closest_match:
            suggestion = closest_match[0]
            return f"Did you mean '{suggestion}'?"
        else:
            return None
