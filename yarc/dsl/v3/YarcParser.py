# $ANTLR 3.5.3 YarcParser.g 2023-05-19 01:44:09

import sys

import stringtemplate3
from antlr3 import (
    BaseRecognizer,
    EarlyExitException,
    FailedPredicateException,
    NoViableAltException,
    ParserRuleReturnScope,
    RecognitionException,
    RecognizerSharedState,
    Token,
)

from yarc.dsl.v3.handler.handler import Attribute, Handler, Parameter
from yarc.dsl.v3.handler.handler_factory import HandlerFactory

if __name__ is not None and "." in __name__:
    from .YarcParserBase import YarcParserBase
else:
    from YarcParserBase import YarcParserBase


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF = -1
AND = 4
ASSIGN = 5
AT = 6
AUG_ASSIGN = 7
AXIS = 8
BIN_DIGIT = 9
BIT_AND = 10
BIT_NOT = 11
BIT_OR = 12
CAMERA = 13
COLON = 14
COMBINE = 15
COMMA = 16
COMMENT = 17
CREATE = 18
DEDENT = 19
DIGIT = 20
DISTRIBUTION = 21
DIV = 22
DOT = 23
EDIT = 24
ELLIPSIS = 25
ELSE = 26
EQUALS = 27
EVERY = 28
EXPONENT = 29
EXPONENT_FLOAT = 30
FALSE = 31
FETCH = 32
FLOAT_NUMBER = 33
FOR = 34
FRACTION = 35
FRAMES = 36
FROM = 37
GET = 38
GROUP = 39
GT = 40
GT_EQ = 41
HEX_DIGIT = 42
ID = 43
IDIV = 44
ID_CONTINUE = 45
ID_START = 46
IF = 47
IN = 48
INDENT = 49
INSTANTIATE = 50
INTEGER = 51
INT_PART = 52
IS = 53
LBRACE = 54
LBRACK = 55
LEN = 56
LETTER = 57
LIGHT = 58
LIMIT = 59
LINE_JOINING = 60
LOOK_AT = 61
LPAREN = 62
LSHIFT = 63
LT = 64
LT_EQ = 65
MATCH = 66
MATERIAL = 67
MATERIAL_ = 68
MINUS = 69
MOD = 70
MOVE_TO_CAM = 71
MUL = 72
NESTED_CODE = 73
NEWLINE = 74
NONE = 75
NON_ZERO_DIGIT = 76
NOT = 77
NOT_EQ = 78
OCT_DIGIT = 79
ON = 80
OPEN = 81
OR = 82
ORDER = 83
PHYSICS = 84
PIVOT = 85
PLUS = 86
POINT_FLOAT = 87
POWER = 88
RANGE = 89
RBRACE = 90
RBRACK = 91
RECURSIVE = 92
ROTATE = 93
ROT_AROUND = 94
RPAREN = 95
RSHIFT = 96
SCALE = 97
SCATTER = 98
SCENARIO = 99
SEMANTICS = 100
SEMI = 101
SETTINGS = 102
SETTING_ID = 103
SHAPE = 104
SHORT_STRING = 105
SIZE = 106
SKIP_ = 107
SNIPPET = 108
SPACES = 109
STAGE = 110
STEP = 111
STEREO = 112
STRING = 113
STRING_ESCAPE_SEQ = 114
TIME = 115
TIMELINE = 116
TO = 117
TRANSLATE = 118
TRUE = 119
UNDERSCORE = 120
UNKNOWN = 121
UP_AXIS = 122
VISIBLE = 123
WRITERS = 124
XOR = 125

# token names
tokenNamesMap = {
    0: "<invalid>",
    1: "<EOR>",
    2: "<DOWN>",
    3: "<UP>",
    -1: "EOF",
    4: "AND",
    5: "ASSIGN",
    6: "AT",
    7: "AUG_ASSIGN",
    8: "AXIS",
    9: "BIN_DIGIT",
    10: "BIT_AND",
    11: "BIT_NOT",
    12: "BIT_OR",
    13: "CAMERA",
    14: "COLON",
    15: "COMBINE",
    16: "COMMA",
    17: "COMMENT",
    18: "CREATE",
    19: "DEDENT",
    20: "DIGIT",
    21: "DISTRIBUTION",
    22: "DIV",
    23: "DOT",
    24: "EDIT",
    25: "ELLIPSIS",
    26: "ELSE",
    27: "EQUALS",
    28: "EVERY",
    29: "EXPONENT",
    30: "EXPONENT_FLOAT",
    31: "FALSE",
    32: "FETCH",
    33: "FLOAT_NUMBER",
    34: "FOR",
    35: "FRACTION",
    36: "FRAMES",
    37: "FROM",
    38: "GET",
    39: "GROUP",
    40: "GT",
    41: "GT_EQ",
    42: "HEX_DIGIT",
    43: "ID",
    44: "IDIV",
    45: "ID_CONTINUE",
    46: "ID_START",
    47: "IF",
    48: "IN",
    49: "INDENT",
    50: "INSTANTIATE",
    51: "INTEGER",
    52: "INT_PART",
    53: "IS",
    54: "LBRACE",
    55: "LBRACK",
    56: "LEN",
    57: "LETTER",
    58: "LIGHT",
    59: "LIMIT",
    60: "LINE_JOINING",
    61: "LOOK_AT",
    62: "LPAREN",
    63: "LSHIFT",
    64: "LT",
    65: "LT_EQ",
    66: "MATCH",
    67: "MATERIAL",
    68: "MATERIAL_",
    69: "MINUS",
    70: "MOD",
    71: "MOVE_TO_CAM",
    72: "MUL",
    73: "NESTED_CODE",
    74: "NEWLINE",
    75: "NONE",
    76: "NON_ZERO_DIGIT",
    77: "NOT",
    78: "NOT_EQ",
    79: "OCT_DIGIT",
    80: "ON",
    81: "OPEN",
    82: "OR",
    83: "ORDER",
    84: "PHYSICS",
    85: "PIVOT",
    86: "PLUS",
    87: "POINT_FLOAT",
    88: "POWER",
    89: "RANGE",
    90: "RBRACE",
    91: "RBRACK",
    92: "RECURSIVE",
    93: "ROTATE",
    94: "ROT_AROUND",
    95: "RPAREN",
    96: "RSHIFT",
    97: "SCALE",
    98: "SCATTER",
    99: "SCENARIO",
    100: "SEMANTICS",
    101: "SEMI",
    102: "SETTINGS",
    103: "SETTING_ID",
    104: "SHAPE",
    105: "SHORT_STRING",
    106: "SIZE",
    107: "SKIP_",
    108: "SNIPPET",
    109: "SPACES",
    110: "STAGE",
    111: "STEP",
    112: "STEREO",
    113: "STRING",
    114: "STRING_ESCAPE_SEQ",
    115: "TIME",
    116: "TIMELINE",
    117: "TO",
    118: "TRANSLATE",
    119: "TRUE",
    120: "UNDERSCORE",
    121: "UNKNOWN",
    122: "UP_AXIS",
    123: "VISIBLE",
    124: "WRITERS",
    125: "XOR",
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>",
    "<EOR>",
    "<DOWN>",
    "<UP>",
    "AND",
    "ASSIGN",
    "AT",
    "AUG_ASSIGN",
    "AXIS",
    "BIN_DIGIT",
    "BIT_AND",
    "BIT_NOT",
    "BIT_OR",
    "CAMERA",
    "COLON",
    "COMBINE",
    "COMMA",
    "COMMENT",
    "CREATE",
    "DEDENT",
    "DIGIT",
    "DISTRIBUTION",
    "DIV",
    "DOT",
    "EDIT",
    "ELLIPSIS",
    "ELSE",
    "EQUALS",
    "EVERY",
    "EXPONENT",
    "EXPONENT_FLOAT",
    "FALSE",
    "FETCH",
    "FLOAT_NUMBER",
    "FOR",
    "FRACTION",
    "FRAMES",
    "FROM",
    "GET",
    "GROUP",
    "GT",
    "GT_EQ",
    "HEX_DIGIT",
    "ID",
    "IDIV",
    "ID_CONTINUE",
    "ID_START",
    "IF",
    "IN",
    "INDENT",
    "INSTANTIATE",
    "INTEGER",
    "INT_PART",
    "IS",
    "LBRACE",
    "LBRACK",
    "LEN",
    "LETTER",
    "LIGHT",
    "LIMIT",
    "LINE_JOINING",
    "LOOK_AT",
    "LPAREN",
    "LSHIFT",
    "LT",
    "LT_EQ",
    "MATCH",
    "MATERIAL",
    "MATERIAL_",
    "MINUS",
    "MOD",
    "MOVE_TO_CAM",
    "MUL",
    "NESTED_CODE",
    "NEWLINE",
    "NONE",
    "NON_ZERO_DIGIT",
    "NOT",
    "NOT_EQ",
    "OCT_DIGIT",
    "ON",
    "OPEN",
    "OR",
    "ORDER",
    "PHYSICS",
    "PIVOT",
    "PLUS",
    "POINT_FLOAT",
    "POWER",
    "RANGE",
    "RBRACE",
    "RBRACK",
    "RECURSIVE",
    "ROTATE",
    "ROT_AROUND",
    "RPAREN",
    "RSHIFT",
    "SCALE",
    "SCATTER",
    "SCENARIO",
    "SEMANTICS",
    "SEMI",
    "SETTINGS",
    "SETTING_ID",
    "SHAPE",
    "SHORT_STRING",
    "SIZE",
    "SKIP_",
    "SNIPPET",
    "SPACES",
    "STAGE",
    "STEP",
    "STEREO",
    "STRING",
    "STRING_ESCAPE_SEQ",
    "TIME",
    "TIMELINE",
    "TO",
    "TRANSLATE",
    "TRUE",
    "UNDERSCORE",
    "UNKNOWN",
    "UP_AXIS",
    "VISIBLE",
    "WRITERS",
    "XOR",
]


class YarcParser(YarcParserBase):
    grammarFileName = "YarcParser.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)

        self.delegates = []

        self.templateLib = stringtemplate3.StringTemplateGroup(
            "YarcParserTemplates", lexer="angle-bracket"
        )

    def setTemplateLib(self, templateLib):
        self.templateLib = templateLib

    def getTemplateLib(self):
        return self.templateLib

    class scenario_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "scenario"
    # YarcParser.g:20:1: scenario : ( NEWLINE )* declaration (before+= code_snippet | NEWLINE )* ( settings )? stage ( writers )? after+= ( code_snippet )* -> scenario(name=$declaration.scenario_namebefore_snippets=$beforesettings=$settings.ststage=$stage.stwriters=$writers.stafter_snippets=$after);
    def scenario(
        self,
    ):
        retval = self.scenario_return()
        retval.start = self.input.LT(1)

        after = None
        list_after = None
        list_before = None
        declaration1 = None
        settings2 = None
        stage3 = None
        writers4 = None
        before = None
        try:
            try:
                # YarcParser.g:20:10: ( ( NEWLINE )* declaration (before+= code_snippet | NEWLINE )* ( settings )? stage ( writers )? after+= ( code_snippet )* -> scenario(name=$declaration.scenario_namebefore_snippets=$beforesettings=$settings.ststage=$stage.stwriters=$writers.stafter_snippets=$after))
                # YarcParser.g:20:12: ( NEWLINE )* declaration (before+= code_snippet | NEWLINE )* ( settings )? stage ( writers )? after+= ( code_snippet )*
                pass
                # YarcParser.g:20:12: ( NEWLINE )*
                while True:  # loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if LA1_0 == NEWLINE:
                        alt1 = 1

                    if alt1 == 1:
                        # YarcParser.g:20:12: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario59
                        )

                    else:
                        break  # loop1

                self._state.following.append(self.FOLLOW_declaration_in_scenario62)
                declaration1 = self.declaration()

                self._state.following.pop()

                # YarcParser.g:20:33: (before+= code_snippet | NEWLINE )*
                while True:  # loop2
                    alt2 = 3
                    LA2_0 = self.input.LA(1)

                    if LA2_0 == SNIPPET:
                        alt2 = 1
                    elif LA2_0 == NEWLINE:
                        alt2 = 2

                    if alt2 == 1:
                        # YarcParser.g:20:34: before+= code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_scenario67
                        )
                        before = self.code_snippet()

                        self._state.following.pop()
                        if list_before is None:
                            list_before = []
                        list_before.append(before.st)

                    elif alt2 == 2:
                        # YarcParser.g:20:57: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario71
                        )

                    else:
                        break  # loop2

                # YarcParser.g:20:67: ( settings )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if LA3_0 == SETTINGS:
                    alt3 = 1
                if alt3 == 1:
                    # YarcParser.g:20:67: settings
                    self._state.following.append(self.FOLLOW_settings_in_scenario75)
                    settings2 = self.settings()

                    self._state.following.pop()

                self._state.following.append(self.FOLLOW_stage_in_scenario78)
                stage3 = self.stage()

                self._state.following.pop()

                # YarcParser.g:20:83: ( writers )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == WRITERS:
                    alt4 = 1
                if alt4 == 1:
                    # YarcParser.g:20:83: writers
                    self._state.following.append(self.FOLLOW_writers_in_scenario80)
                    writers4 = self.writers()

                    self._state.following.pop()

                # YarcParser.g:20:99: ( code_snippet )*
                while True:  # loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if LA5_0 == SNIPPET:
                        alt5 = 1

                    if alt5 == 1:
                        # YarcParser.g:20:100: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_scenario86
                        )
                        after = self.code_snippet()

                        self._state.following.pop()
                        if list_after is None:
                            list_after = []
                        list_after.append(after.st)

                    else:
                        break  # loop5

                # TEMPLATE REWRITE
                # 21:3: -> scenario(name=$declaration.scenario_namebefore_snippets=$beforesettings=$settings.ststage=$stage.stwriters=$writers.stafter_snippets=$after)
                retval.st = self.templateLib.getInstanceOf(
                    "scenario",
                    attributes={
                        "name": (
                            (declaration1 is not None)
                            and [declaration1.scenario_name]
                            or [None]
                        )[0],
                        "before_snippets": list_before,
                        "settings": (
                            (settings2 is not None) and [settings2.st] or [None]
                        )[0],
                        "stage": ((stage3 is not None) and [stage3.st] or [None])[0],
                        "writers": ((writers4 is not None) and [writers4.st] or [None])[
                            0
                        ],
                        "after_snippets": list_after,
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "scenario"

    class code_snippet_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "code_snippet"
    # YarcParser.g:28:1: code_snippet : SNIPPET -> snippet(code=code);
    def code_snippet(
        self,
    ):
        retval = self.code_snippet_return()
        retval.start = self.input.LT(1)

        SNIPPET5 = None

        try:
            try:
                # YarcParser.g:28:14: ( SNIPPET -> snippet(code=code))
                # YarcParser.g:28:17: SNIPPET
                SNIPPET5 = self.match(
                    self.input, SNIPPET, self.FOLLOW_SNIPPET_in_code_snippet209
                )

                # action start
                code = self.handler.parse_snippet(SNIPPET5)
                # action end

                # TEMPLATE REWRITE
                # 28:69: -> snippet(code=code)
                retval.st = self.templateLib.getInstanceOf(
                    "snippet", attributes={"code": code}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "code_snippet"

    class declaration_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.scenario_name = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "declaration"
    # YarcParser.g:30:1: declaration returns [scenario_name] : SCENARIO ID ( COLON name )? NEWLINE ;
    def declaration(
        self,
    ):
        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        ID6 = None
        name7 = None

        try:
            try:
                # YarcParser.g:30:37: ( SCENARIO ID ( COLON name )? NEWLINE )
                # YarcParser.g:30:39: SCENARIO ID ( COLON name )? NEWLINE
                self.match(self.input, SCENARIO, self.FOLLOW_SCENARIO_in_declaration232)

                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_declaration234)

                # YarcParser.g:30:51: ( COLON name )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if LA6_0 == COLON:
                    alt6 = 1
                if alt6 == 1:
                    # YarcParser.g:30:52: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration237)

                    self._state.following.append(self.FOLLOW_name_in_declaration239)
                    name7 = self.name()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_declaration243)

                # action start
                retval.scenario_name = ID6.text
                # action end

                # action start
                self.handler = HandlerFactory.get_handler(
                    (
                        (name7 is not None)
                        and [self.input.toString(name7.start, name7.stop)]
                        or [None]
                    )[0],
                    self,
                )
                # action end

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "declaration"

    class settings_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "settings"
    # YarcParser.g:34:1: settings : SETTINGS COLON NEWLINE INDENT stmts_+= ( setting | code_snippet )+ DEDENT -> settings(settings=self.handler.settings_to_str()stmts=$stmts_);
    def settings(
        self,
    ):
        retval = self.settings_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:34:13: ( SETTINGS COLON NEWLINE INDENT stmts_+= ( setting | code_snippet )+ DEDENT -> settings(settings=self.handler.settings_to_str()stmts=$stmts_))
                # YarcParser.g:34:15: SETTINGS COLON NEWLINE INDENT stmts_+= ( setting | code_snippet )+ DEDENT
                self.match(self.input, SETTINGS, self.FOLLOW_SETTINGS_in_settings266)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_settings268)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_settings270)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_settings272)

                # YarcParser.g:34:53: ( setting | code_snippet )+
                cnt7 = 0
                while True:  # loop7
                    alt7 = 3
                    LA7_0 = self.input.LA(1)

                    if LA7_0 == ID:
                        alt7 = 1
                    elif LA7_0 == SNIPPET:
                        alt7 = 2

                    if alt7 == 1:
                        # YarcParser.g:34:54: setting
                        self._state.following.append(self.FOLLOW_setting_in_settings277)
                        stmts_ = self.setting()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt7 == 2:
                        # YarcParser.g:34:64: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_settings281
                        )
                        stmts_ = self.code_snippet()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt7 >= 1:
                            break  # loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_settings285)

                # TEMPLATE REWRITE
                # 34:86: -> settings(settings=self.handler.settings_to_str()stmts=$stmts_)
                retval.st = self.templateLib.getInstanceOf(
                    "settings",
                    attributes={
                        "settings": self.handler.settings_to_str(),
                        "stmts": list_stmts_,
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "settings"

    class setting_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "setting"
    # YarcParser.g:35:1: setting : ID ASSIGN test NEWLINE ({...}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}| -> setting(setting=$ID.textvalue=$test.st)) ;
    def setting(
        self,
    ):
        retval = self.setting_return()
        retval.start = self.input.LT(1)

        ID8 = None
        test9 = None

        try:
            try:
                # YarcParser.g:35:16: ( ID ASSIGN test NEWLINE ({...}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}| -> setting(setting=$ID.textvalue=$test.st)) )
                # YarcParser.g:35:18: ID ASSIGN test NEWLINE ({...}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}| -> setting(setting=$ID.textvalue=$test.st))
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_setting313)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_setting315)

                self._state.following.append(self.FOLLOW_test_in_setting317)
                test9 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_setting319)

                # YarcParser.g:35:41: ({...}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}| -> setting(setting=$ID.textvalue=$test.st))
                alt8 = 2
                LA8 = self.input.LA(1)
                if LA8 in {DEDENT}:
                    self.input.LA(2)

                    if self.handler.is_special_setting(ID8.text):
                        alt8 = 1
                    elif True:
                        alt8 = 2
                    else:
                        nvae = NoViableAltException("", 8, 1, self.input)

                        raise nvae

                elif LA8 in {ID}:
                    self.input.LA(2)

                    if self.handler.is_special_setting(ID8.text):
                        alt8 = 1
                    elif True:
                        alt8 = 2
                    else:
                        nvae = NoViableAltException("", 8, 2, self.input)

                        raise nvae

                elif LA8 in {SNIPPET}:
                    self.input.LA(2)

                    if self.handler.is_special_setting(ID8.text):
                        alt8 = 1
                    elif True:
                        alt8 = 2
                    else:
                        nvae = NoViableAltException("", 8, 3, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # YarcParser.g:35:43: {...}?
                    if not (self.handler.is_special_setting(ID8.text)):
                        raise FailedPredicateException(
                            self.input,
                            "setting",
                            "self.handler.is_special_setting($ID.text)",
                        )

                    # TEMPLATE REWRITE
                    # 35:88: -> {self.handler.special_setting_to_str($ID.text, $test.st)}
                    retval.st = self.handler.special_setting_to_str(
                        ID8.text, ((test9 is not None) and [test9.st] or [None])[0]
                    )

                elif alt8 == 2:
                    # YarcParser.g:36:43:
                    pass
                    # TEMPLATE REWRITE
                    # 36:43: -> setting(setting=$ID.textvalue=$test.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "setting",
                        attributes={
                            "setting": ID8.text,
                            "value": ((test9 is not None) and [test9.st] or [None])[0],
                        },
                    )

                # action start
                self.handler.add_setting(
                    setting=ID8.text,
                    value=((test9 is not None) and [test9.st] or [None])[0],
                )
                # action end

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "setting"

    class writers_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "writers"
    # YarcParser.g:39:1: writers : WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | code_snippet | writer )+ DEDENT -> writers(stmts=$stmts_);
    def writers(
        self,
    ):
        retval = self.writers_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:39:13: ( WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | code_snippet | writer )+ DEDENT -> writers(stmts=$stmts_))
                # YarcParser.g:39:15: WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | code_snippet | writer )+ DEDENT
                self.match(self.input, WRITERS, self.FOLLOW_WRITERS_in_writers441)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writers443)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writers445)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writers447)

                # YarcParser.g:39:52: ( expr_stmt | code_snippet | writer )+
                cnt9 = 0
                while True:  # loop9
                    alt9 = 4
                    LA9 = self.input.LA(1)
                    if LA9 in {ID}:
                        LA9_2 = self.input.LA(2)

                        if LA9_2 == COLON:
                            alt9 = 3
                        elif LA9_2 in {ASSIGN, AUG_ASSIGN, COMMA}:
                            alt9 = 1

                    elif LA9 in {UNDERSCORE}:
                        alt9 = 1
                    elif LA9 in {SNIPPET}:
                        alt9 = 2

                    if alt9 == 1:
                        # YarcParser.g:39:53: expr_stmt
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers452
                        )
                        stmts_ = self.expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt9 == 2:
                        # YarcParser.g:39:65: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_writers456
                        )
                        stmts_ = self.code_snippet()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt9 == 3:
                        # YarcParser.g:39:80: writer
                        self._state.following.append(self.FOLLOW_writer_in_writers460)
                        stmts_ = self.writer()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt9 >= 1:
                            break  # loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writers464)

                # TEMPLATE REWRITE
                # 39:96: -> writers(stmts=$stmts_)
                retval.st = self.templateLib.getInstanceOf(
                    "writers", attributes={"stmts": list_stmts_}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "writers"

    class writer_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "writer"
    # YarcParser.g:40:1: writer : ID COLON NEWLINE INDENT ( writer_param )+ DEDENT -> writer(writer_id=$ID.textparams=params);
    def writer(
        self,
    ):
        retval = self.writer_return()
        retval.start = self.input.LT(1)

        ID11 = None
        writer_param10 = None

        params = []
        try:
            try:
                # YarcParser.g:41:3: ( ID COLON NEWLINE INDENT ( writer_param )+ DEDENT -> writer(writer_id=$ID.textparams=params))
                # YarcParser.g:41:5: ID COLON NEWLINE INDENT ( writer_param )+ DEDENT
                ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_writer494)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writer496)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer498)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writer500)

                # YarcParser.g:41:29: ( writer_param )+
                cnt10 = 0
                while True:  # loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if LA10_0 == ID:
                        alt10 = 1

                    if alt10 == 1:
                        # YarcParser.g:41:30: writer_param
                        self._state.following.append(
                            self.FOLLOW_writer_param_in_writer503
                        )
                        writer_param10 = self.writer_param()

                        self._state.following.pop()

                        # action start
                        params.append(
                            (
                                (writer_param10 is not None)
                                and [writer_param10.param]
                                or [None]
                            )[0]
                        )
                        # action end

                    else:
                        if cnt10 >= 1:
                            break  # loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writer509)

                # action start
                self.handler.check_writer_params(params)
                # action end

                # TEMPLATE REWRITE
                # 42:3: -> writer(writer_id=$ID.textparams=params)
                retval.st = self.templateLib.getInstanceOf(
                    "writer", attributes={"writer_id": ID11.text, "params": params}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "writer"

    class writer_param_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.param = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "writer_param"
    # YarcParser.g:43:1: writer_param returns [param] : ID ASSIGN test NEWLINE ;
    def writer_param(
        self,
    ):
        retval = self.writer_param_return()
        retval.start = self.input.LT(1)

        ID12 = None
        test13 = None

        try:
            try:
                # YarcParser.g:43:29: ( ID ASSIGN test NEWLINE )
                # YarcParser.g:43:31: ID ASSIGN test NEWLINE
                ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_writer_param538)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_writer_param540)

                self._state.following.append(self.FOLLOW_test_in_writer_param542)
                test13 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer_param544)

                # action start
                retval.param = Parameter(
                    ID12.text, ((test13 is not None) and [test13.st] or [None])[0]
                )
                # action end

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "writer_param"

    class stage_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "stage"
    # YarcParser.g:45:1: stage : STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st};
    def stage(
        self,
    ):
        retval = self.stage_return()
        retval.start = self.input.LT(1)

        stmts14 = None

        try:
            try:
                # YarcParser.g:45:13: ( STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st})
                # YarcParser.g:45:15: STAGE COLON NEWLINE INDENT stmts DEDENT
                self.match(self.input, STAGE, self.FOLLOW_STAGE_in_stage560)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_stage562)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stage564)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stage566)

                self._state.following.append(self.FOLLOW_stmts_in_stage568)
                stmts14 = self.stmts()

                self._state.following.pop()

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stage570)

                # TEMPLATE REWRITE
                # 45:55: -> {$stmts.st}
                retval.st = ((stmts14 is not None) and [stmts14.st] or [None])[0]

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stage"

    class stmts_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "stmts"
    # YarcParser.g:46:1: stmts :stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt )+ -> stage(stmts=$stmts_);
    def stmts(
        self,
    ):
        retval = self.stmts_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:46:16: (stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt )+ -> stage(stmts=$stmts_))
                # YarcParser.g:46:18: stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt )+
                pass
                # YarcParser.g:46:26: ( open_stmt )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if LA11_0 == OPEN:
                    alt11 = 1
                if alt11 == 1:
                    # YarcParser.g:46:27: open_stmt
                    self._state.following.append(self.FOLLOW_open_stmt_in_stmts593)
                    stmts_ = self.open_stmt()

                    self._state.following.pop()
                    if list_stmts_ is None:
                        list_stmts_ = []
                    list_stmts_.append(stmts_.st)

                # YarcParser.g:46:47: ( aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt )+
                cnt12 = 0
                while True:  # loop12
                    alt12 = 5
                    LA12 = self.input.LA(1)
                    if LA12 in {CREATE, GET, GROUP, ID, INSTANTIATE, UNDERSCORE}:
                        alt12 = 1
                    elif LA12 in {SNIPPET}:
                        alt12 = 2
                    elif LA12 in {EDIT}:
                        alt12 = 3
                    elif LA12 in {EVERY}:
                        alt12 = 4

                    if alt12 == 1:
                        # YarcParser.g:46:48: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts600
                        )
                        stmts_ = self.aug_expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt12 == 2:
                        # YarcParser.g:46:64: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_stmts604
                        )
                        stmts_ = self.code_snippet()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt12 == 3:
                        # YarcParser.g:46:79: edit_stmt
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts608)
                        stmts_ = self.edit_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt12 == 4:
                        # YarcParser.g:46:91: behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_behavior_stmt_in_stmts612
                        )
                        stmts_ = self.behavior_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt12 >= 1:
                            break  # loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1

                # TEMPLATE REWRITE
                # 46:107: -> stage(stmts=$stmts_)
                retval.st = self.templateLib.getInstanceOf(
                    "stage", attributes={"stmts": list_stmts_}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stmts"

    class open_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "open_stmt"
    # YarcParser.g:50:1: open_stmt : OPEN test NEWLINE -> open_stmt(path=$test.st);
    def open_stmt(
        self,
    ):
        retval = self.open_stmt_return()
        retval.start = self.input.LT(1)

        test15 = None

        try:
            try:
                # YarcParser.g:50:11: ( OPEN test NEWLINE -> open_stmt(path=$test.st))
                # YarcParser.g:50:13: OPEN test NEWLINE
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_open_stmt635)

                self._state.following.append(self.FOLLOW_test_in_open_stmt637)
                test15 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_open_stmt639)

                # TEMPLATE REWRITE
                # 50:31: -> open_stmt(path=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "open_stmt",
                    attributes={
                        "path": ((test15 is not None) and [test15.st] or [None])[0]
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "open_stmt"

    class edit_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "edit_stmt"
    # YarcParser.g:51:1: edit_stmt : EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs($EDIT, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))) ;
    def edit_stmt(
        self,
    ):
        retval = self.edit_stmt_return()
        retval.start = self.input.LT(1)

        EDIT16 = None
        list_params = None
        list_values = None
        id = None
        edit_block17 = None
        params = None
        values = None
        try:
            try:
                # YarcParser.g:51:11: ( EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs($EDIT, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))) )
                # YarcParser.g:51:13: EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs($EDIT, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                EDIT16 = self.match(self.input, EDIT, self.FOLLOW_EDIT_in_edit_stmt655)

                # YarcParser.g:51:18: ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs($EDIT, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if LA14_0 == TIMELINE:
                    alt14 = 1
                elif LA14_0 in {ID, UNDERSCORE}:
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # YarcParser.g:51:19: TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt658
                    )

                    self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_stmt660)

                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_stmt662)

                    self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_stmt664)

                    # YarcParser.g:51:49: (params+= name values+= test NEWLINE )+
                    cnt13 = 0
                    while True:  # loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if LA13_0 in {ID, UNDERSCORE}:
                            alt13 = 1

                        if alt13 == 1:
                            # YarcParser.g:51:50: params+= name values+= test NEWLINE
                            self._state.following.append(
                                self.FOLLOW_name_in_edit_stmt669
                            )
                            params = self.name()

                            self._state.following.pop()
                            if list_params is None:
                                list_params = []
                            list_params.append(params.st)

                            self._state.following.append(
                                self.FOLLOW_test_in_edit_stmt673
                            )
                            values = self.test()

                            self._state.following.pop()
                            if list_values is None:
                                list_values = []
                            list_values.append(values.st)

                            self.match(
                                self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_stmt675
                            )

                        else:
                            if cnt13 >= 1:
                                break  # loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1

                    self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_stmt679)

                    # TEMPLATE REWRITE
                    # 51:93: -> edit_timeline(params=$paramsvalues=$values)
                    retval.st = self.templateLib.getInstanceOf(
                        "edit_timeline",
                        attributes={"params": list_params, "values": list_values},
                    )

                elif alt14 == 2:
                    # YarcParser.g:52:20: id= name edit_block[$id.st]
                    self._state.following.append(self.FOLLOW_name_in_edit_stmt717)
                    id = self.name()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_edit_block_in_edit_stmt719)
                    edit_block17 = self.edit_block(
                        ((id is not None) and [id.st] or [None])[0]
                    )

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 52:47: -> edit_stmt(id=$id.ststmts=self.handler.get_attrs($EDIT, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "edit_stmt",
                        attributes={
                            "id": ((id is not None) and [id.st] or [None])[0],
                            "stmts": self.handler.get_attrs(
                                EDIT16,
                                (
                                    (edit_block17 is not None)
                                    and [edit_block17.attrs]
                                    or [None]
                                )[0],
                            ),
                            "behaviors": self.handler.get_behaviors(
                                (
                                    (edit_block17 is not None)
                                    and [edit_block17.attrs]
                                    or [None]
                                )[0]
                            ),
                        },
                    )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "edit_stmt"

    class create_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "create_expr"
    # YarcParser.g:55:1: create_expr[id] : CREATE (count= test )? (prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| (prim= STEREO CAMERA |prim= CAMERA ) (attrs= edit_block[$id] | NEWLINE ) -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))|prim= FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params($FROM, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($FROM, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params($MATERIAL, $attrs.attrs, warnings=True, count=count.st))) ;
    def create_expr(self, id):
        retval = self.create_expr_return()
        retval.start = self.input.LT(1)

        prim = None
        MATERIAL18 = None
        count = None
        attrs = None
        file = None

        try:
            try:
                # YarcParser.g:55:16: ( CREATE (count= test )? (prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| (prim= STEREO CAMERA |prim= CAMERA ) (attrs= edit_block[$id] | NEWLINE ) -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))|prim= FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params($FROM, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($FROM, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params($MATERIAL, $attrs.attrs, warnings=True, count=count.st))) )
                # YarcParser.g:56:3: CREATE (count= test )? (prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| (prim= STEREO CAMERA |prim= CAMERA ) (attrs= edit_block[$id] | NEWLINE ) -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))|prim= FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params($FROM, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($FROM, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params($MATERIAL, $attrs.attrs, warnings=True, count=count.st)))
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr768)

                # YarcParser.g:56:15: (count= test )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if LA15_0 in {
                    BIT_NOT,
                    COMBINE,
                    DISTRIBUTION,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LEN,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NOT,
                    PLUS,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                }:
                    alt15 = 1
                if alt15 == 1:
                    # YarcParser.g:56:15: count= test
                    self._state.following.append(self.FOLLOW_test_in_create_expr772)
                    count = self.test()

                    self._state.following.pop()

                # YarcParser.g:56:22: (prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| (prim= STEREO CAMERA |prim= CAMERA ) (attrs= edit_block[$id] | NEWLINE ) -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))|prim= FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params($FROM, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($FROM, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params($MATERIAL, $attrs.attrs, warnings=True, count=count.st)))
                alt22 = 4
                LA22 = self.input.LA(1)
                if LA22 in {LIGHT, SHAPE}:
                    alt22 = 1
                elif LA22 in {CAMERA, STEREO}:
                    alt22 = 2
                elif LA22 in {FROM}:
                    alt22 = 3
                elif LA22 in {MATERIAL}:
                    alt22 = 4
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # YarcParser.g:57:5: prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE )
                    pass
                    # YarcParser.g:57:10: ( SHAPE | LIGHT )
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if LA16_0 == SHAPE:
                        alt16 = 1
                    elif LA16_0 == LIGHT:
                        alt16 = 2
                    else:
                        nvae = NoViableAltException("", 16, 0, self.input)

                        raise nvae

                    if alt16 == 1:
                        # YarcParser.g:57:11: SHAPE
                        prim = self.match(
                            self.input, SHAPE, self.FOLLOW_SHAPE_in_create_expr784
                        )

                    elif alt16 == 2:
                        # YarcParser.g:57:19: LIGHT
                        prim = self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr788
                        )

                    # YarcParser.g:57:26: (attrs= edit_block[$id] | NEWLINE )
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if LA17_0 == COLON:
                        alt17 = 1
                    elif LA17_0 == NEWLINE:
                        alt17 = 2
                    else:
                        nvae = NoViableAltException("", 17, 0, self.input)

                        raise nvae

                    if alt17 == 1:
                        # YarcParser.g:57:27: attrs= edit_block[$id]
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr794
                        )
                        attrs = self.edit_block(id)

                        self._state.following.pop()

                    elif alt17 == 2:
                        # YarcParser.g:57:51: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr799
                        )

                    # TEMPLATE REWRITE
                    # 58:7: -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "create_prim",
                        attributes={
                            "id": id,
                            "prim": self.handler.map(prim),
                            "params": self.handler.get_params(
                                prim,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                count=((count is not None) and [count.st] or [None])[0],
                            ),
                            "stmts": self.handler.get_attrs(
                                prim,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                            ),
                            "behaviors": self.handler.get_behaviors(
                                ((attrs is not None) and [attrs.attrs] or [None])[0]
                            ),
                        },
                    )

                elif alt22 == 2:
                    # YarcParser.g:63:7: (prim= STEREO CAMERA |prim= CAMERA ) (attrs= edit_block[$id] | NEWLINE )
                    pass
                    # YarcParser.g:63:7: (prim= STEREO CAMERA |prim= CAMERA )
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if LA18_0 == STEREO:
                        alt18 = 1
                    elif LA18_0 == CAMERA:
                        alt18 = 2
                    else:
                        nvae = NoViableAltException("", 18, 0, self.input)

                        raise nvae

                    if alt18 == 1:
                        # YarcParser.g:63:8: prim= STEREO CAMERA
                        prim = self.match(
                            self.input, STEREO, self.FOLLOW_STEREO_in_create_expr935
                        )

                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr937
                        )

                    elif alt18 == 2:
                        # YarcParser.g:63:29: prim= CAMERA
                        prim = self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr943
                        )

                    # YarcParser.g:63:42: (attrs= edit_block[$id] | NEWLINE )
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if LA19_0 == COLON:
                        alt19 = 1
                    elif LA19_0 == NEWLINE:
                        alt19 = 2
                    else:
                        nvae = NoViableAltException("", 19, 0, self.input)

                        raise nvae

                    if alt19 == 1:
                        # YarcParser.g:63:43: attrs= edit_block[$id]
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr949
                        )
                        attrs = self.edit_block(id)

                        self._state.following.pop()

                    elif alt19 == 2:
                        # YarcParser.g:63:67: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr954
                        )

                    # TEMPLATE REWRITE
                    # 64:7: -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "create_camera",
                        attributes={
                            "id": id,
                            "prim": self.handler.map(prim),
                            "params": self.handler.get_params(
                                prim,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                count=((count is not None) and [count.st] or [None])[0],
                            ),
                            "stmts": self.handler.get_attrs(
                                prim,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                            ),
                            "behaviors": self.handler.get_behaviors(
                                ((attrs is not None) and [attrs.attrs] or [None])[0]
                            ),
                        },
                    )

                elif alt22 == 3:
                    # YarcParser.g:69:7: prim= FROM file= test (attrs= edit_block[$id] | NEWLINE )
                    prim = self.match(
                        self.input, FROM, self.FOLLOW_FROM_in_create_expr1089
                    )

                    self._state.following.append(self.FOLLOW_test_in_create_expr1093)
                    file = self.test()

                    self._state.following.pop()

                    # YarcParser.g:69:27: (attrs= edit_block[$id] | NEWLINE )
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if LA20_0 == COLON:
                        alt20 = 1
                    elif LA20_0 == NEWLINE:
                        alt20 = 2
                    else:
                        nvae = NoViableAltException("", 20, 0, self.input)

                        raise nvae

                    if alt20 == 1:
                        # YarcParser.g:69:28: attrs= edit_block[$id]
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr1098
                        )
                        attrs = self.edit_block(id)

                        self._state.following.pop()

                    elif alt20 == 2:
                        # YarcParser.g:69:52: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr1103
                        )

                    # TEMPLATE REWRITE
                    # 70:7: -> create_from(id=$idfile=$file.stparams=self.handler.get_params($FROM, $attrs.attrs, count=$count.st)stmts=self.handler.get_attrs($FROM, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "create_from",
                        attributes={
                            "id": id,
                            "file": ((file is not None) and [file.st] or [None])[0],
                            "params": self.handler.get_params(
                                prim,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                count=((count is not None) and [count.st] or [None])[0],
                            ),
                            "stmts": self.handler.get_attrs(
                                prim,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                            ),
                            "behaviors": self.handler.get_behaviors(
                                ((attrs is not None) and [attrs.attrs] or [None])[0]
                            ),
                        },
                    )

                elif alt22 == 4:
                    # YarcParser.g:75:7: MATERIAL (attrs= simple_block | NEWLINE )
                    MATERIAL18 = self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr1234
                    )

                    # YarcParser.g:75:16: (attrs= simple_block | NEWLINE )
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if LA21_0 == COLON:
                        alt21 = 1
                    elif LA21_0 == NEWLINE:
                        alt21 = 2
                    else:
                        nvae = NoViableAltException("", 21, 0, self.input)

                        raise nvae

                    if alt21 == 1:
                        # YarcParser.g:75:17: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_create_expr1239
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt21 == 2:
                        # YarcParser.g:75:38: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr1243
                        )

                    # TEMPLATE REWRITE
                    # 76:7: -> create_material(id=$idparams=self.handler.get_params($MATERIAL, $attrs.attrs, warnings=True, count=count.st))
                    retval.st = self.templateLib.getInstanceOf(
                        "create_material",
                        attributes={
                            "id": id,
                            "params": self.handler.get_params(
                                MATERIAL18,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                warnings=True,
                                count=count.st,
                            ),
                        },
                    )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "create_expr"

    class instantiate_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "instantiate_expr"
    # YarcParser.g:81:1: instantiate_expr[id] : INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE ) -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params($INSTANTIATE, $edit_block.attrs, size=$count.st)stmts=self.handler.get_attrs($INSTANTIATE, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs));
    def instantiate_expr(self, id):
        retval = self.instantiate_expr_return()
        retval.start = self.input.LT(1)

        count = None
        INSTANTIATE19 = None
        file = None
        edit_block20 = None

        try:
            try:
                # YarcParser.g:81:22: ( INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE ) -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params($INSTANTIATE, $edit_block.attrs, size=$count.st)stmts=self.handler.get_attrs($INSTANTIATE, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                # YarcParser.g:81:24: INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE )
                INSTANTIATE19 = self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr1305,
                )

                # YarcParser.g:81:42: ( test )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if LA23_0 in {
                    BIT_NOT,
                    COMBINE,
                    DISTRIBUTION,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LEN,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NOT,
                    PLUS,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                }:
                    alt23 = 1
                if alt23 == 1:
                    # YarcParser.g:81:43: test
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr1310
                    )
                    count = self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr1314)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr1318)
                file = self.test()

                self._state.following.pop()

                # YarcParser.g:81:65: ( edit_block[$id] | NEWLINE )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if LA24_0 == COLON:
                    alt24 = 1
                elif LA24_0 == NEWLINE:
                    alt24 = 2
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # YarcParser.g:81:66: edit_block[$id]
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr1321
                    )
                    edit_block20 = self.edit_block(id)

                    self._state.following.pop()

                elif alt24 == 2:
                    # YarcParser.g:81:84: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instantiate_expr1326
                    )

                # TEMPLATE REWRITE
                # 82:3: -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params($INSTANTIATE, $edit_block.attrs, size=$count.st)stmts=self.handler.get_attrs($INSTANTIATE, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                retval.st = self.templateLib.getInstanceOf(
                    "instantiate_expr",
                    attributes={
                        "id": id,
                        "file": ((file is not None) and [file.st] or [None])[0],
                        "params": self.handler.get_params(
                            INSTANTIATE19,
                            (
                                (edit_block20 is not None)
                                and [edit_block20.attrs]
                                or [None]
                            )[0],
                            size=count.st,
                        ),
                        "stmts": self.handler.get_attrs(
                            INSTANTIATE19,
                            (
                                (edit_block20 is not None)
                                and [edit_block20.attrs]
                                or [None]
                            )[0],
                        ),
                        "behaviors": self.handler.get_behaviors(
                            (
                                (edit_block20 is not None)
                                and [edit_block20.attrs]
                                or [None]
                            )[0]
                        ),
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "instantiate_expr"

    class group_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "group_expr"
    # YarcParser.g:87:1: group_expr[id] : GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE ) -> group_expr(id=$idnames=$namesparams=self.handler.get_params($GROUP, $edit_block.attrs)stmts=self.handler.get_attrs($GROUP, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs));
    def group_expr(self, id):
        retval = self.group_expr_return()
        retval.start = self.input.LT(1)

        GROUP21 = None
        list_names = None
        edit_block22 = None
        names = None
        try:
            try:
                # YarcParser.g:87:22: ( GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE ) -> group_expr(id=$idnames=$namesparams=self.handler.get_params($GROUP, $edit_block.attrs)stmts=self.handler.get_attrs($GROUP, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                # YarcParser.g:87:24: GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE )
                GROUP21 = self.match(
                    self.input, GROUP, self.FOLLOW_GROUP_in_group_expr1465
                )

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr1467)

                self._state.following.append(self.FOLLOW_name_in_group_expr1471)
                names = self.name()

                self._state.following.pop()
                if list_names is None:
                    list_names = []
                list_names.append(names.st)

                # YarcParser.g:87:49: ( COMMA names+= name )*
                while True:  # loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if LA25_0 == COMMA:
                        alt25 = 1

                    if alt25 == 1:
                        # YarcParser.g:87:50: COMMA names+= name
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_group_expr1474
                        )

                        self._state.following.append(self.FOLLOW_name_in_group_expr1478)
                        names = self.name()

                        self._state.following.pop()
                        if list_names is None:
                            list_names = []
                        list_names.append(names.st)

                    else:
                        break  # loop25

                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_group_expr1482)

                # YarcParser.g:87:77: ( edit_block[$id] | NEWLINE )
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if LA26_0 == COLON:
                    alt26 = 1
                elif LA26_0 == NEWLINE:
                    alt26 = 2
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # YarcParser.g:87:78: edit_block[$id]
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr1485
                    )
                    edit_block22 = self.edit_block(id)

                    self._state.following.pop()

                elif alt26 == 2:
                    # YarcParser.g:87:96: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_group_expr1490
                    )

                # TEMPLATE REWRITE
                # 88:3: -> group_expr(id=$idnames=$namesparams=self.handler.get_params($GROUP, $edit_block.attrs)stmts=self.handler.get_attrs($GROUP, $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                retval.st = self.templateLib.getInstanceOf(
                    "group_expr",
                    attributes={
                        "id": id,
                        "names": list_names,
                        "params": self.handler.get_params(
                            GROUP21,
                            (
                                (edit_block22 is not None)
                                and [edit_block22.attrs]
                                or [None]
                            )[0],
                        ),
                        "stmts": self.handler.get_attrs(
                            GROUP21,
                            (
                                (edit_block22 is not None)
                                and [edit_block22.attrs]
                                or [None]
                            )[0],
                        ),
                        "behaviors": self.handler.get_behaviors(
                            (
                                (edit_block22 is not None)
                                and [edit_block22.attrs]
                                or [None]
                            )[0]
                        ),
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "group_expr"

    class get_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "get_expr"
    # YarcParser.g:93:1: get_expr[id] : GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE ) -> get_expr(id=$idfilter=self.handler.map($filter)path=$path.stparams=self.handler.get_params($GET, $simple_block.attrs, warnings=True));
    def get_expr(self, id):
        retval = self.get_expr_return()
        retval.start = self.input.LT(1)

        filter = None
        GET23 = None
        path = None
        simple_block24 = None

        try:
            try:
                # YarcParser.g:93:22: ( GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE ) -> get_expr(id=$idfilter=self.handler.map($filter)path=$path.stparams=self.handler.get_params($GET, $simple_block.attrs, warnings=True)))
                # YarcParser.g:93:24: GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE )
                GET23 = self.match(self.input, GET, self.FOLLOW_GET_in_get_expr1604)

                # YarcParser.g:93:28: (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )?
                alt28 = 2
                LA28 = self.input.LA(1)
                if LA28 in {CAMERA, LIGHT, MATERIAL}:
                    alt28 = 1
                elif LA28 in {ID}:
                    LA28_2 = self.input.LA(2)

                    if LA28_2 == AT:
                        alt28 = 1
                elif LA28 in {UNDERSCORE}:
                    LA28_3 = self.input.LA(2)

                    if LA28_3 == AT:
                        alt28 = 1
                if alt28 == 1:
                    # YarcParser.g:93:29: filter= ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # YarcParser.g:93:36: ( CAMERA | LIGHT | MATERIAL | name )
                    alt27 = 4
                    LA27 = self.input.LA(1)
                    if LA27 in {CAMERA}:
                        alt27 = 1
                    elif LA27 in {LIGHT}:
                        alt27 = 2
                    elif LA27 in {MATERIAL}:
                        alt27 = 3
                    elif LA27 in {ID, UNDERSCORE}:
                        alt27 = 4
                    else:
                        nvae = NoViableAltException("", 27, 0, self.input)

                        raise nvae

                    if alt27 == 1:
                        # YarcParser.g:93:37: CAMERA
                        filter = self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr1610
                        )

                    elif alt27 == 2:
                        # YarcParser.g:93:46: LIGHT
                        filter = self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr1614
                        )

                    elif alt27 == 3:
                        # YarcParser.g:93:54: MATERIAL
                        filter = self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr1618
                        )

                    elif alt27 == 4:
                        # YarcParser.g:93:65: name
                        self._state.following.append(self.FOLLOW_name_in_get_expr1622)
                        filter = self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr1625)

                self._state.following.append(self.FOLLOW_test_in_get_expr1631)
                path = self.test()

                self._state.following.pop()

                # YarcParser.g:93:86: ( simple_block | NEWLINE )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if LA29_0 == COLON:
                    alt29 = 1
                elif LA29_0 == NEWLINE:
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # YarcParser.g:93:87: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr1634
                    )
                    simple_block24 = self.simple_block()

                    self._state.following.pop()

                elif alt29 == 2:
                    # YarcParser.g:93:102: NEWLINE
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr1638)

                # action start
                self.handler.check_target(filter)
                # action end

                # TEMPLATE REWRITE
                # 94:3: -> get_expr(id=$idfilter=self.handler.map($filter)path=$path.stparams=self.handler.get_params($GET, $simple_block.attrs, warnings=True))
                retval.st = self.templateLib.getInstanceOf(
                    "get_expr",
                    attributes={
                        "id": id,
                        "filter": self.handler.map(filter),
                        "path": ((path is not None) and [path.st] or [None])[0],
                        "params": self.handler.get_params(
                            GET23,
                            (
                                (simple_block24 is not None)
                                and [simple_block24.attrs]
                                or [None]
                            )[0],
                            warnings=True,
                        ),
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "get_expr"

    class edit_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.attrs = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "edit_block"
    # YarcParser.g:99:1: edit_block[id] returns [attrs] : COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT ;
    def edit_block(self, id):
        retval = self.edit_block_return()
        retval.start = self.input.LT(1)

        stmt_ = None

        retval.attrs = []
        try:
            try:
                # YarcParser.g:101:3: ( COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT )
                # YarcParser.g:101:5: COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block1732)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block1734)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block1736)

                # YarcParser.g:101:26: (stmt_= ( attr | inner_behavior_stmt[$id] ) )+
                cnt31 = 0
                while True:  # loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if LA31_0 in {
                        EVERY,
                        ID,
                        LOOK_AT,
                        MATERIAL_,
                        MOVE_TO_CAM,
                        PHYSICS,
                        PIVOT,
                        ROTATE,
                        ROT_AROUND,
                        SCALE,
                        SCATTER,
                        SEMANTICS,
                        SIZE,
                        TRANSLATE,
                        UNDERSCORE,
                        UP_AXIS,
                        VISIBLE,
                    }:
                        alt31 = 1

                    if alt31 == 1:
                        # YarcParser.g:101:27: stmt_= ( attr | inner_behavior_stmt[$id] )
                        pass
                        # YarcParser.g:101:33: ( attr | inner_behavior_stmt[$id] )
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if LA30_0 in {
                            ID,
                            LOOK_AT,
                            MATERIAL_,
                            MOVE_TO_CAM,
                            PHYSICS,
                            PIVOT,
                            ROTATE,
                            ROT_AROUND,
                            SCALE,
                            SCATTER,
                            SEMANTICS,
                            SIZE,
                            TRANSLATE,
                            UNDERSCORE,
                            UP_AXIS,
                            VISIBLE,
                        }:
                            alt30 = 1
                        elif LA30_0 == EVERY:
                            alt30 = 2
                        else:
                            nvae = NoViableAltException("", 30, 0, self.input)

                            raise nvae

                        if alt30 == 1:
                            # YarcParser.g:101:34: attr
                            self._state.following.append(
                                self.FOLLOW_attr_in_edit_block1742
                            )
                            stmt_ = self.attr()

                            self._state.following.pop()

                        elif alt30 == 2:
                            # YarcParser.g:101:41: inner_behavior_stmt[$id]
                            self._state.following.append(
                                self.FOLLOW_inner_behavior_stmt_in_edit_block1746
                            )
                            stmt_ = self.inner_behavior_stmt(id)

                            self._state.following.pop()

                        # action start
                        retval.attrs.append(stmt_.attr)
                        # action end

                    else:
                        if cnt31 >= 1:
                            break  # loop31

                        eee = EarlyExitException(31, self.input)
                        raise eee

                    cnt31 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_block1754)

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "edit_block"

    class simple_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.attrs = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "simple_block"
    # YarcParser.g:102:1: simple_block returns [attrs] : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        retval = self.simple_block_return()
        retval.start = self.input.LT(1)

        simple_attr25 = None

        retval.attrs = []
        try:
            try:
                # YarcParser.g:104:3: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # YarcParser.g:104:5: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block1773)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block1775)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block1777)

                # YarcParser.g:104:26: ( simple_attr )+
                cnt32 = 0
                while True:  # loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if LA32_0 in {ID, UNDERSCORE}:
                        alt32 = 1

                    if alt32 == 1:
                        # YarcParser.g:104:27: simple_attr
                        self._state.following.append(
                            self.FOLLOW_simple_attr_in_simple_block1780
                        )
                        simple_attr25 = self.simple_attr()

                        self._state.following.pop()

                        # action start
                        retval.attrs.append(
                            (
                                (simple_attr25 is not None)
                                and [simple_attr25.attr]
                                or [None]
                            )[0]
                        )
                        # action end

                    else:
                        if cnt32 >= 1:
                            break  # loop32

                        eee = EarlyExitException(32, self.input)
                        raise eee

                    cnt32 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_simple_block1786)

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "simple_block"

    class attr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.attr = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "attr"
    # YarcParser.g:106:1: attr returns [attr] : a= ( core_attr | simple_attr | compound_attr ) -> {$a.st};
    def attr(
        self,
    ):
        retval = self.attr_return()
        retval.start = self.input.LT(1)

        a = None

        try:
            try:
                # YarcParser.g:106:21: (a= ( core_attr | simple_attr | compound_attr ) -> {$a.st})
                # YarcParser.g:106:23: a= ( core_attr | simple_attr | compound_attr )
                pass
                # YarcParser.g:106:25: ( core_attr | simple_attr | compound_attr )
                alt33 = 3
                LA33 = self.input.LA(1)
                if LA33 in {
                    LOOK_AT,
                    MATERIAL_,
                    PIVOT,
                    ROTATE,
                    SCALE,
                    SEMANTICS,
                    SIZE,
                    TRANSLATE,
                    UP_AXIS,
                    VISIBLE,
                }:
                    alt33 = 1
                elif LA33 in {ID, UNDERSCORE}:
                    alt33 = 2
                elif LA33 in {MOVE_TO_CAM, PHYSICS, ROT_AROUND, SCATTER}:
                    alt33 = 3
                else:
                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # YarcParser.g:106:26: core_attr
                    self._state.following.append(self.FOLLOW_core_attr_in_attr1801)
                    a = self.core_attr()

                    self._state.following.pop()

                elif alt33 == 2:
                    # YarcParser.g:106:38: simple_attr
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr1805)
                    a = self.simple_attr()

                    self._state.following.pop()

                elif alt33 == 3:
                    # YarcParser.g:106:52: compound_attr
                    self._state.following.append(self.FOLLOW_compound_attr_in_attr1809)
                    a = self.compound_attr()

                    self._state.following.pop()

                # action start
                retval.attr = a.attr
                # action end

                # TEMPLATE REWRITE
                # 106:83: -> {$a.st}
                retval.st = a.st

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "attr"

    class simple_attr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.attr = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "simple_attr"
    # YarcParser.g:107:1: simple_attr returns [attr] : name_= name ( COLON type= name )? value= test NEWLINE -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st);
    def simple_attr(
        self,
    ):
        retval = self.simple_attr_return()
        retval.start = self.input.LT(1)

        name_ = None
        type = None
        value = None

        try:
            try:
                # YarcParser.g:109:3: (name_= name ( COLON type= name )? value= test NEWLINE -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st))
                # YarcParser.g:109:5: name_= name ( COLON type= name )? value= test NEWLINE
                self._state.following.append(self.FOLLOW_name_in_simple_attr1839)
                name_ = self.name()

                self._state.following.pop()

                # YarcParser.g:109:16: ( COLON type= name )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if LA34_0 == COLON:
                    alt34 = 1
                if alt34 == 1:
                    # YarcParser.g:109:17: COLON type= name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr1842)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr1846)
                    type = self.name()

                    self._state.following.pop()

                self._state.following.append(self.FOLLOW_test_in_simple_attr1852)
                value = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_attr1854)

                # TEMPLATE REWRITE
                # 110:3: -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st)
                retval.st = self.templateLib.getInstanceOf(
                    "simple_attr",
                    attributes={
                        "name": ((name_ is not None) and [name_.st] or [None])[0],
                        "type": ((type is not None) and [type.st] or [None])[0],
                        "value": ((value is not None) and [value.st] or [None])[0],
                    },
                )

                retval.stop = self.input.LT(-1)

                # action start
                retval.attr = Attribute(
                    ((name_ is not None) and [name_.st] or [None])[0],
                    ((value is not None) and [value.st] or [None])[0],
                    retval.st,
                )
                # action end

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "simple_attr"

    class compound_attr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.attr = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "compound_attr"
    # YarcParser.g:112:1: compound_attr returns [attr] : (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE ) -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))) ;
    def compound_attr(
        self,
    ):
        retval = self.compound_attr_return()
        retval.start = self.input.LT(1)

        name_ = None
        surface = None
        attrs = None
        center = None
        camera = None

        try:
            try:
                # YarcParser.g:114:3: ( (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE ) -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))) )
                # YarcParser.g:114:5: (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE ) -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True)))
                pass
                # YarcParser.g:114:5: (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs, warnings=True))|name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE ) -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True)))
                alt39 = 4
                LA39 = self.input.LA(1)
                if LA39 in {SCATTER}:
                    alt39 = 1
                elif LA39 in {ROT_AROUND}:
                    alt39 = 2
                elif LA39 in {PHYSICS}:
                    alt39 = 3
                elif LA39 in {MOVE_TO_CAM}:
                    alt39 = 4
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # YarcParser.g:114:7: name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr1901
                    )

                    self.match(self.input, ON, self.FOLLOW_ON_in_compound_attr1903)

                    self._state.following.append(self.FOLLOW_name_in_compound_attr1907)
                    surface = self.name()

                    self._state.following.pop()

                    # YarcParser.g:114:37: (attrs= simple_block | NEWLINE )
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if LA35_0 == COLON:
                        alt35 = 1
                    elif LA35_0 == NEWLINE:
                        alt35 = 2
                    else:
                        nvae = NoViableAltException("", 35, 0, self.input)

                        raise nvae

                    if alt35 == 1:
                        # YarcParser.g:114:38: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr1912
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt35 == 2:
                        # YarcParser.g:114:59: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr1916,
                        )

                    # TEMPLATE REWRITE
                    # 115:7: -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))
                    retval.st = self.templateLib.getInstanceOf(
                        "scatter_expr",
                        attributes={
                            "scatter_type": self.handler.map(name_),
                            "surface": (
                                (surface is not None) and [surface.st] or [None]
                            )[0],
                            "params": self.handler.get_params(
                                name_,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                warnings=True,
                            ),
                        },
                    )

                elif alt39 == 2:
                    # YarcParser.g:118:7: name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input,
                        ROT_AROUND,
                        self.FOLLOW_ROT_AROUND_in_compound_attr2000,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr2004)
                    center = self.name()

                    self._state.following.pop()

                    # YarcParser.g:118:36: (attrs= simple_block | NEWLINE )
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if LA36_0 == COLON:
                        alt36 = 1
                    elif LA36_0 == NEWLINE:
                        alt36 = 2
                    else:
                        nvae = NoViableAltException("", 36, 0, self.input)

                        raise nvae

                    if alt36 == 1:
                        # YarcParser.g:118:37: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr2009
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt36 == 2:
                        # YarcParser.g:118:58: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr2013,
                        )

                    # TEMPLATE REWRITE
                    # 119:7: -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))
                    retval.st = self.templateLib.getInstanceOf(
                        "rot_around_expr",
                        attributes={
                            "center": ((center is not None) and [center.st] or [None])[
                                0
                            ],
                            "params": self.handler.get_params(
                                name_,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                warnings=True,
                            ),
                        },
                    )

                elif alt39 == 3:
                    # YarcParser.g:121:7: name_= PHYSICS (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input, PHYSICS, self.FOLLOW_PHYSICS_in_compound_attr2070
                    )

                    # YarcParser.g:121:21: (attrs= simple_block | NEWLINE )
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if LA37_0 == COLON:
                        alt37 = 1
                    elif LA37_0 == NEWLINE:
                        alt37 = 2
                    else:
                        nvae = NoViableAltException("", 37, 0, self.input)

                        raise nvae

                    if alt37 == 1:
                        # YarcParser.g:121:22: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr2075
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt37 == 2:
                        # YarcParser.g:121:43: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr2079,
                        )

                    # TEMPLATE REWRITE
                    # 122:7: -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs, warnings=True))
                    retval.st = self.templateLib.getInstanceOf(
                        "physics_expr",
                        attributes={
                            "physics_attr": self.handler.map(name_),
                            "params": self.handler.get_params(
                                name_,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                warnings=True,
                            ),
                        },
                    )

                elif alt39 == 4:
                    # YarcParser.g:124:7: name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input,
                        MOVE_TO_CAM,
                        self.FOLLOW_MOVE_TO_CAM_in_compound_attr2132,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr2136)
                    camera = self.name()

                    self._state.following.pop()

                    # YarcParser.g:124:37: (attrs= simple_block | NEWLINE )
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if LA38_0 == COLON:
                        alt38 = 1
                    elif LA38_0 == NEWLINE:
                        alt38 = 2
                    else:
                        nvae = NoViableAltException("", 38, 0, self.input)

                        raise nvae

                    if alt38 == 1:
                        # YarcParser.g:124:38: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr2141
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt38 == 2:
                        # YarcParser.g:124:59: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr2145,
                        )

                    # TEMPLATE REWRITE
                    # 125:7: -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs, warnings=True))
                    retval.st = self.templateLib.getInstanceOf(
                        "move_to_camera_expr",
                        attributes={
                            "camera": ((camera is not None) and [camera.st] or [None])[
                                0
                            ],
                            "params": self.handler.get_params(
                                name_,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                warnings=True,
                            ),
                        },
                    )

                retval.stop = self.input.LT(-1)

                # action start
                retval.attr = Attribute(self.handler.map(name_), "", retval.st)
                # action end

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "compound_attr"

    class core_attr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.attr = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "core_attr"
    # YarcParser.g:129:1: core_attr returns [attr] : ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| PIVOT value= test -> pivot_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)| MATERIAL_ value= test -> material_expr(value=$value.st)) NEWLINE ;
    def core_attr(
        self,
    ):
        retval = self.core_attr_return()
        retval.start = self.input.LT(1)

        axis = None
        TRANSLATE26 = None
        ROTATE27 = None
        SCALE28 = None
        LOOK_AT29 = None
        UP_AXIS30 = None
        SIZE31 = None
        PIVOT32 = None
        SEMANTICS33 = None
        VISIBLE34 = None
        MATERIAL_35 = None
        value = None

        try:
            try:
                # YarcParser.g:131:3: ( ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| PIVOT value= test -> pivot_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)| MATERIAL_ value= test -> material_expr(value=$value.st)) NEWLINE )
                # YarcParser.g:131:5: ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| PIVOT value= test -> pivot_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)| MATERIAL_ value= test -> material_expr(value=$value.st)) NEWLINE
                pass
                # YarcParser.g:131:5: ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| PIVOT value= test -> pivot_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)| MATERIAL_ value= test -> material_expr(value=$value.st))
                alt42 = 10
                LA42 = self.input.LA(1)
                if LA42 in {TRANSLATE}:
                    alt42 = 1
                elif LA42 in {ROTATE}:
                    alt42 = 2
                elif LA42 in {SCALE}:
                    alt42 = 3
                elif LA42 in {LOOK_AT}:
                    alt42 = 4
                elif LA42 in {UP_AXIS}:
                    alt42 = 5
                elif LA42 in {SIZE}:
                    alt42 = 6
                elif LA42 in {PIVOT}:
                    alt42 = 7
                elif LA42 in {SEMANTICS}:
                    alt42 = 8
                elif LA42 in {VISIBLE}:
                    alt42 = 9
                elif LA42 in {MATERIAL_}:
                    alt42 = 10
                else:
                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae

                if alt42 == 1:
                    # YarcParser.g:131:7: TRANSLATE (axis= AXIS )? TO value= test
                    TRANSLATE26 = self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr2223
                    )

                    # YarcParser.g:131:21: (axis= AXIS )?
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if LA40_0 == AXIS:
                        alt40 = 1
                    if alt40 == 1:
                        # YarcParser.g:131:21: axis= AXIS
                        axis = self.match(
                            self.input, AXIS, self.FOLLOW_AXIS_in_core_attr2227
                        )

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr2230)

                    self._state.following.append(self.FOLLOW_test_in_core_attr2234)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(TRANSLATE26, axis)
                    # action end

                    # TEMPLATE REWRITE
                    # 131:87: -> translate_expr(type=namevalue=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "translate_expr",
                        attributes={
                            "type": name,
                            "value": ((value is not None) and [value.st] or [None])[0],
                        },
                    )

                elif alt42 == 2:
                    # YarcParser.g:132:7: ROTATE (axis= AXIS )? value= test
                    ROTATE27 = self.match(
                        self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr2258
                    )

                    # YarcParser.g:132:18: (axis= AXIS )?
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if LA41_0 == AXIS:
                        alt41 = 1
                    if alt41 == 1:
                        # YarcParser.g:132:18: axis= AXIS
                        axis = self.match(
                            self.input, AXIS, self.FOLLOW_AXIS_in_core_attr2262
                        )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2267)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(ROTATE27, axis)
                    # action end

                    # TEMPLATE REWRITE
                    # 132:78: -> rotate_expr(type=namevalue=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "rotate_expr",
                        attributes={
                            "type": name,
                            "value": ((value is not None) and [value.st] or [None])[0],
                        },
                    )

                elif alt42 == 3:
                    # YarcParser.g:133:7: SCALE value= test
                    SCALE28 = self.match(
                        self.input, SCALE, self.FOLLOW_SCALE_in_core_attr2291
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2295)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SCALE28)
                    # action end

                    # TEMPLATE REWRITE
                    # 133:58: -> scale_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "scale_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt42 == 4:
                    # YarcParser.g:134:7: LOOK_AT value= test
                    LOOK_AT29 = self.match(
                        self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr2314
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2318)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(LOOK_AT29)
                    # action end

                    # TEMPLATE REWRITE
                    # 134:62: -> look_at_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "look_at_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt42 == 5:
                    # YarcParser.g:135:7: UP_AXIS value= test
                    UP_AXIS30 = self.match(
                        self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr2337
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2341)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(UP_AXIS30)
                    # action end

                    # TEMPLATE REWRITE
                    # 135:62: -> look_at_up_axis_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "look_at_up_axis_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt42 == 6:
                    # YarcParser.g:136:7: SIZE value= test
                    SIZE31 = self.match(
                        self.input, SIZE, self.FOLLOW_SIZE_in_core_attr2360
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2364)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SIZE31)
                    # action end

                    # TEMPLATE REWRITE
                    # 136:56: -> size_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "size_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt42 == 7:
                    # YarcParser.g:137:7: PIVOT value= test
                    PIVOT32 = self.match(
                        self.input, PIVOT, self.FOLLOW_PIVOT_in_core_attr2383
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2387)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(PIVOT32)
                    # action end

                    # TEMPLATE REWRITE
                    # 137:58: -> pivot_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "pivot_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt42 == 8:
                    # YarcParser.g:138:7: SEMANTICS value= test
                    SEMANTICS33 = self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr2406
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2410)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SEMANTICS33)
                    # action end

                    # TEMPLATE REWRITE
                    # 138:66: -> semantics_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "semantics_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt42 == 9:
                    # YarcParser.g:139:7: VISIBLE value= test
                    VISIBLE34 = self.match(
                        self.input, VISIBLE, self.FOLLOW_VISIBLE_in_core_attr2429
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2433)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(VISIBLE34)
                    # action end

                    # TEMPLATE REWRITE
                    # 139:62: -> visible_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "visible_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt42 == 10:
                    # YarcParser.g:140:7: MATERIAL_ value= test
                    MATERIAL_35 = self.match(
                        self.input, MATERIAL_, self.FOLLOW_MATERIAL__in_core_attr2452
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2456)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(MATERIAL_35)
                    # action end

                    # TEMPLATE REWRITE
                    # 140:66: -> material_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "material_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_core_attr2473)

                retval.stop = self.input.LT(-1)

                # action start
                retval.attr = Attribute(
                    name, ((value is not None) and [value.st] or [None])[0], retval.st
                )
                # action end

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "core_attr"

    class inner_behavior_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.attr = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "inner_behavior_stmt"
    # YarcParser.g:143:1: inner_behavior_stmt[id] returns [attr] : behavior_expr inner_behavior_block -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st);
    def inner_behavior_stmt(self, id):
        retval = self.inner_behavior_stmt_return()
        retval.start = self.input.LT(1)

        behavior_expr36 = None
        inner_behavior_block37 = None

        try:
            try:
                # YarcParser.g:145:3: ( behavior_expr inner_behavior_block -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st))
                # YarcParser.g:145:5: behavior_expr inner_behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_inner_behavior_stmt2496
                )
                behavior_expr36 = self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_inner_behavior_block_in_inner_behavior_stmt2498
                )
                inner_behavior_block37 = self.inner_behavior_block()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 145:40: -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st)
                retval.st = self.templateLib.getInstanceOf(
                    "inner_behavior_stmt",
                    attributes={
                        "behavior": (
                            (behavior_expr36 is not None)
                            and [behavior_expr36.st]
                            or [None]
                        )[0],
                        "id": id,
                        "block": (
                            (inner_behavior_block37 is not None)
                            and [inner_behavior_block37.st]
                            or [None]
                        )[0],
                    },
                )

                retval.stop = self.input.LT(-1)

                # action start
                retval.attr = Attribute(Handler.BEHAVIOR, "", retval.st)
                # action end

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "inner_behavior_stmt"

    class inner_behavior_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "inner_behavior_block"
    # YarcParser.g:146:1: inner_behavior_block : COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT -> behavior_block(stmts=$stmts_);
    def inner_behavior_block(
        self,
    ):
        retval = self.inner_behavior_block_return()
        retval.start = self.input.LT(1)

        list_stmts_ = None
        stmts_ = None
        try:
            try:
                # YarcParser.g:146:22: ( COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT -> behavior_block(stmts=$stmts_))
                # YarcParser.g:146:24: COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block2524
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block2526
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block2528
                )

                # YarcParser.g:146:51: (stmts_+= attr )+
                cnt43 = 0
                while True:  # loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if LA43_0 in {
                        ID,
                        LOOK_AT,
                        MATERIAL_,
                        MOVE_TO_CAM,
                        PHYSICS,
                        PIVOT,
                        ROTATE,
                        ROT_AROUND,
                        SCALE,
                        SCATTER,
                        SEMANTICS,
                        SIZE,
                        TRANSLATE,
                        UNDERSCORE,
                        UP_AXIS,
                        VISIBLE,
                    }:
                        alt43 = 1

                    if alt43 == 1:
                        # YarcParser.g:146:51: stmts_+= attr
                        self._state.following.append(
                            self.FOLLOW_attr_in_inner_behavior_block2532
                        )
                        stmts_ = self.attr()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt43 >= 1:
                            break  # loop43

                        eee = EarlyExitException(43, self.input)
                        raise eee

                    cnt43 += 1

                self.match(
                    self.input, DEDENT, self.FOLLOW_DEDENT_in_inner_behavior_block2535
                )

                # TEMPLATE REWRITE
                # 146:66: -> behavior_block(stmts=$stmts_)
                retval.st = self.templateLib.getInstanceOf(
                    "behavior_block", attributes={"stmts": list_stmts_}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "inner_behavior_block"

    class behavior_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "behavior_stmt"
    # YarcParser.g:149:1: behavior_stmt : behavior_expr behavior_block -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st);
    def behavior_stmt(
        self,
    ):
        retval = self.behavior_stmt_return()
        retval.start = self.input.LT(1)

        behavior_expr38 = None
        behavior_block39 = None

        try:
            try:
                # YarcParser.g:149:16: ( behavior_expr behavior_block -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st))
                # YarcParser.g:149:18: behavior_expr behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_behavior_stmt2555
                )
                behavior_expr38 = self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_behavior_block_in_behavior_stmt2557
                )
                behavior_block39 = self.behavior_block()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 149:47: -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st)
                retval.st = self.templateLib.getInstanceOf(
                    "behavior_stmt",
                    attributes={
                        "behavior": (
                            (behavior_expr38 is not None)
                            and [behavior_expr38.st]
                            or [None]
                        )[0],
                        "block": (
                            (behavior_block39 is not None)
                            and [behavior_block39.st]
                            or [None]
                        )[0],
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "behavior_stmt"

    class behavior_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "behavior_expr"
    # YarcParser.g:150:1: behavior_expr : EVERY (interval= test )? type= ( FRAMES | TIME ) -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type));
    def behavior_expr(
        self,
    ):
        retval = self.behavior_expr_return()
        retval.start = self.input.LT(1)

        type = None
        interval = None

        try:
            try:
                # YarcParser.g:150:16: ( EVERY (interval= test )? type= ( FRAMES | TIME ) -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type)))
                # YarcParser.g:150:18: EVERY (interval= test )? type= ( FRAMES | TIME )
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr2579)

                # YarcParser.g:150:32: (interval= test )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if LA44_0 in {
                    BIT_NOT,
                    COMBINE,
                    DISTRIBUTION,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LEN,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NOT,
                    PLUS,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                }:
                    alt44 = 1
                if alt44 == 1:
                    # YarcParser.g:150:32: interval= test
                    self._state.following.append(self.FOLLOW_test_in_behavior_expr2583)
                    interval = self.test()

                    self._state.following.pop()

                # YarcParser.g:150:44: ( FRAMES | TIME )
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 == FRAMES:
                    alt45 = 1
                elif LA45_0 == TIME:
                    alt45 = 2
                else:
                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae

                if alt45 == 1:
                    # YarcParser.g:150:45: FRAMES
                    type = self.match(
                        self.input, FRAMES, self.FOLLOW_FRAMES_in_behavior_expr2589
                    )

                elif alt45 == 2:
                    # YarcParser.g:150:54: TIME
                    type = self.match(
                        self.input, TIME, self.FOLLOW_TIME_in_behavior_expr2593
                    )

                # TEMPLATE REWRITE
                # 150:60: -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type))
                retval.st = self.templateLib.getInstanceOf(
                    "behavior_expr",
                    attributes={
                        "interval": (
                            (interval is not None) and [interval.st] or [None]
                        )[0],
                        "is_frame": self.handler.is_frame(type),
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "behavior_expr"

    class behavior_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "behavior_block"
    # YarcParser.g:151:1: behavior_block : COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt )+ DEDENT -> behavior_block(stmts=$stmts_);
    def behavior_block(
        self,
    ):
        retval = self.behavior_block_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:151:16: ( COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt )+ DEDENT -> behavior_block(stmts=$stmts_))
                # YarcParser.g:151:18: COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block2615)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block2617
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block2619)

                # YarcParser.g:151:47: ( aug_expr_stmt | code_snippet | edit_stmt )+
                cnt46 = 0
                while True:  # loop46
                    alt46 = 4
                    LA46 = self.input.LA(1)
                    if LA46 in {CREATE, GET, GROUP, ID, INSTANTIATE, UNDERSCORE}:
                        alt46 = 1
                    elif LA46 in {SNIPPET}:
                        alt46 = 2
                    elif LA46 in {EDIT}:
                        alt46 = 3

                    if alt46 == 1:
                        # YarcParser.g:151:48: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block2624
                        )
                        stmts_ = self.aug_expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt46 == 2:
                        # YarcParser.g:151:64: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_behavior_block2628
                        )
                        stmts_ = self.code_snippet()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt46 == 3:
                        # YarcParser.g:151:79: edit_stmt
                        self._state.following.append(
                            self.FOLLOW_edit_stmt_in_behavior_block2632
                        )
                        stmts_ = self.edit_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt46 >= 1:
                            break  # loop46

                        eee = EarlyExitException(46, self.input)
                        raise eee

                    cnt46 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_behavior_block2636)

                # TEMPLATE REWRITE
                # 151:98: -> behavior_block(stmts=$stmts_)
                retval.st = self.templateLib.getInstanceOf(
                    "behavior_block", attributes={"stmts": list_stmts_}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "behavior_block"

    class expr_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "expr_stmt"
    # YarcParser.g:154:1: expr_stmt : assignable= namelist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st);
    def expr_stmt(
        self,
    ):
        retval = self.expr_stmt_return()
        retval.start = self.input.LT(1)

        op = None
        value = None
        assignable = None

        try:
            try:
                # YarcParser.g:154:11: (assignable= namelist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st))
                # YarcParser.g:154:13: assignable= namelist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_namelist_in_expr_stmt2657)
                assignable = self.namelist()

                self._state.following.pop()

                # action start
                self.handler.define(
                    ((assignable is not None) and [assignable.names] or [None])[0]
                )
                # action end

                # YarcParser.g:154:77: ( AUG_ASSIGN | ASSIGN )
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if LA47_0 == AUG_ASSIGN:
                    alt47 = 1
                elif LA47_0 == ASSIGN:
                    alt47 = 2
                else:
                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae

                if alt47 == 1:
                    # YarcParser.g:154:78: AUG_ASSIGN
                    op = self.match(
                        self.input, AUG_ASSIGN, self.FOLLOW_AUG_ASSIGN_in_expr_stmt2664
                    )

                elif alt47 == 2:
                    # YarcParser.g:154:91: ASSIGN
                    op = self.match(
                        self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr_stmt2668
                    )

                # YarcParser.g:154:105: ( testlist | fetch_expr )
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if LA48_0 in {
                    BIT_NOT,
                    COMBINE,
                    DISTRIBUTION,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LEN,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NOT,
                    PLUS,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                }:
                    alt48 = 1
                elif LA48_0 == FETCH:
                    alt48 = 2
                else:
                    nvae = NoViableAltException("", 48, 0, self.input)

                    raise nvae

                if alt48 == 1:
                    # YarcParser.g:154:106: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt2674)
                    value = self.testlist()

                    self._state.following.pop()

                elif alt48 == 2:
                    # YarcParser.g:154:117: fetch_expr
                    self._state.following.append(
                        self.FOLLOW_fetch_expr_in_expr_stmt2678
                    )
                    value = self.fetch_expr()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expr_stmt2681)

                # TEMPLATE REWRITE
                # 155:3: -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st)
                retval.st = self.templateLib.getInstanceOf(
                    "expr_stmt",
                    attributes={
                        "assignable": (
                            (assignable is not None) and [assignable.st] or [None]
                        )[0],
                        "op": op.text,
                        "value": value.st,
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "expr_stmt"

    class aug_expr_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "aug_expr_stmt"
    # YarcParser.g:157:1: aug_expr_stmt : ( (id= namelist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) ) | model_expr[id] -> {$model_expr.st});
    def aug_expr_stmt(
        self,
    ):
        retval = self.aug_expr_stmt_return()
        retval.start = self.input.LT(1)

        op = None
        value = None
        id = None
        model_expr40 = None

        try:
            try:
                # YarcParser.g:157:14: ( (id= namelist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) ) | model_expr[id] -> {$model_expr.st})
                alt53 = 2
                LA53_0 = self.input.LA(1)

                if LA53_0 in {ID, UNDERSCORE}:
                    alt53 = 1
                elif LA53_0 in {CREATE, GET, GROUP, INSTANTIATE}:
                    alt53 = 2
                else:
                    nvae = NoViableAltException("", 53, 0, self.input)

                    raise nvae

                if alt53 == 1:
                    # YarcParser.g:157:16: (id= namelist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) )
                    pass
                    # YarcParser.g:157:16: (id= namelist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) )
                    # YarcParser.g:158:5: id= namelist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) )
                    self._state.following.append(
                        self.FOLLOW_namelist_in_aug_expr_stmt2719
                    )
                    id = self.namelist()

                    self._state.following.pop()

                    # action start
                    self.handler.define(((id is not None) and [id.names] or [None])[0])
                    # action end

                    # YarcParser.g:158:50: (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) )
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if LA52_0 == AUG_ASSIGN:
                        alt52 = 1
                    elif LA52_0 == ASSIGN:
                        alt52 = 2
                    else:
                        nvae = NoViableAltException("", 52, 0, self.input)

                        raise nvae

                    if alt52 == 1:
                        # YarcParser.g:159:7: op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE
                        op = self.match(
                            self.input,
                            AUG_ASSIGN,
                            self.FOLLOW_AUG_ASSIGN_in_aug_expr_stmt2733,
                        )

                        # YarcParser.g:159:27: ( testlist | fetch_expr )
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if LA49_0 in {
                            BIT_NOT,
                            COMBINE,
                            DISTRIBUTION,
                            FALSE,
                            FLOAT_NUMBER,
                            ID,
                            INTEGER,
                            LBRACE,
                            LBRACK,
                            LEN,
                            LPAREN,
                            LT,
                            MINUS,
                            NONE,
                            NOT,
                            PLUS,
                            SETTING_ID,
                            STRING,
                            TRUE,
                            UNDERSCORE,
                        }:
                            alt49 = 1
                        elif LA49_0 == FETCH:
                            alt49 = 2
                        else:
                            nvae = NoViableAltException("", 49, 0, self.input)

                            raise nvae

                        if alt49 == 1:
                            # YarcParser.g:159:28: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt2738
                            )
                            value = self.testlist()

                            self._state.following.pop()

                        elif alt49 == 2:
                            # YarcParser.g:159:39: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt2742
                            )
                            value = self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_aug_expr_stmt2745,
                        )

                        # TEMPLATE REWRITE
                        # 159:59: -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "expr_stmt",
                            attributes={
                                "assignable": ((id is not None) and [id.st] or [None])[
                                    0
                                ],
                                "op": op.text,
                                "value": value.st,
                            },
                        )

                    elif alt52 == 2:
                        # YarcParser.g:160:9: op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st})
                        op = self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt2777
                        )

                        # YarcParser.g:160:19: (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st})
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if LA51_0 in {
                            BIT_NOT,
                            COMBINE,
                            DISTRIBUTION,
                            FALSE,
                            FETCH,
                            FLOAT_NUMBER,
                            ID,
                            INTEGER,
                            LBRACE,
                            LBRACK,
                            LEN,
                            LPAREN,
                            LT,
                            MINUS,
                            NONE,
                            NOT,
                            PLUS,
                            SETTING_ID,
                            STRING,
                            TRUE,
                            UNDERSCORE,
                        }:
                            alt51 = 1
                        elif LA51_0 in {CREATE, GET, GROUP, INSTANTIATE}:
                            alt51 = 2
                        else:
                            nvae = NoViableAltException("", 51, 0, self.input)

                            raise nvae

                        if alt51 == 1:
                            # YarcParser.g:161:9: value= ( testlist | fetch_expr ) NEWLINE
                            pass
                            # YarcParser.g:161:15: ( testlist | fetch_expr )
                            alt50 = 2
                            LA50_0 = self.input.LA(1)

                            if LA50_0 in {
                                BIT_NOT,
                                COMBINE,
                                DISTRIBUTION,
                                FALSE,
                                FLOAT_NUMBER,
                                ID,
                                INTEGER,
                                LBRACE,
                                LBRACK,
                                LEN,
                                LPAREN,
                                LT,
                                MINUS,
                                NONE,
                                NOT,
                                PLUS,
                                SETTING_ID,
                                STRING,
                                TRUE,
                                UNDERSCORE,
                            }:
                                alt50 = 1
                            elif LA50_0 == FETCH:
                                alt50 = 2
                            else:
                                nvae = NoViableAltException("", 50, 0, self.input)

                                raise nvae

                            if alt50 == 1:
                                # YarcParser.g:161:16: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt2792
                                )
                                value = self.testlist()

                                self._state.following.pop()

                            elif alt50 == 2:
                                # YarcParser.g:161:27: fetch_expr
                                self._state.following.append(
                                    self.FOLLOW_fetch_expr_in_aug_expr_stmt2796
                                )
                                value = self.fetch_expr()

                                self._state.following.pop()

                            self.match(
                                self.input,
                                NEWLINE,
                                self.FOLLOW_NEWLINE_in_aug_expr_stmt2799,
                            )

                            # TEMPLATE REWRITE
                            # 161:47: -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)
                            retval.st = self.templateLib.getInstanceOf(
                                "expr_stmt",
                                attributes={
                                    "assignable": (
                                        (id is not None) and [id.st] or [None]
                                    )[0],
                                    "op": op.text,
                                    "value": value.st,
                                },
                            )

                        elif alt51 == 2:
                            # YarcParser.g:162:11: value= ( model_expr[$id.st] )
                            pass
                            # YarcParser.g:162:17: ( model_expr[$id.st] )
                            # YarcParser.g:162:18: model_expr[$id.st]
                            self._state.following.append(
                                self.FOLLOW_model_expr_in_aug_expr_stmt2834
                            )
                            value = self.model_expr(
                                ((id is not None) and [id.st] or [None])[0]
                            )

                            self._state.following.pop()

                            # TEMPLATE REWRITE
                            # 162:38: -> {$value.st}
                            retval.st = value.st

                elif alt53 == 2:
                    # YarcParser.g:166:5: model_expr[id]
                    pass
                    # action start
                    id = self.handler.get_random_uid()
                    # action end

                    self._state.following.append(
                        self.FOLLOW_model_expr_in_aug_expr_stmt2868
                    )
                    model_expr40 = self.model_expr(id)

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 166:57: -> {$model_expr.st}
                    retval.st = (
                        (model_expr40 is not None) and [model_expr40.st] or [None]
                    )[0]

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "aug_expr_stmt"

    class model_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "model_expr"
    # YarcParser.g:169:1: model_expr[id] : expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] ) -> {expr_.st};
    def model_expr(self, id):
        retval = self.model_expr_return()
        retval.start = self.input.LT(1)

        expr_ = None

        try:
            try:
                # YarcParser.g:169:15: (expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] ) -> {expr_.st})
                # YarcParser.g:169:17: expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] )
                pass
                # YarcParser.g:169:23: ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] )
                alt54 = 4
                LA54 = self.input.LA(1)
                if LA54 in {CREATE}:
                    alt54 = 1
                elif LA54 in {INSTANTIATE}:
                    alt54 = 2
                elif LA54 in {GET}:
                    alt54 = 3
                elif LA54 in {GROUP}:
                    alt54 = 4
                else:
                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae

                if alt54 == 1:
                    # YarcParser.g:169:24: create_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_model_expr2885
                    )
                    expr_ = self.create_expr(id)

                    self._state.following.pop()

                elif alt54 == 2:
                    # YarcParser.g:169:43: instantiate_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_model_expr2890
                    )
                    expr_ = self.instantiate_expr(id)

                    self._state.following.pop()

                elif alt54 == 3:
                    # YarcParser.g:169:67: get_expr[$id]
                    self._state.following.append(self.FOLLOW_get_expr_in_model_expr2895)
                    expr_ = self.get_expr(id)

                    self._state.following.pop()

                elif alt54 == 4:
                    # YarcParser.g:169:83: group_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_group_expr_in_model_expr2900
                    )
                    expr_ = self.group_expr(id)

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 169:100: -> {expr_.st}
                retval.st = expr_.st

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "model_expr"

    class fetch_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "fetch_expr"
    # YarcParser.g:171:1: fetch_expr : FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )? -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE);
    def fetch_expr(
        self,
    ):
        retval = self.fetch_expr_return()
        retval.start = self.input.LT(1)

        RECURSIVE41 = None
        ext = None
        path = None
        filter = None
        limit = None

        try:
            try:
                # YarcParser.g:171:12: ( FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )? -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE))
                # YarcParser.g:171:14: FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )?
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr2914)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr2918)
                ext = self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr2920)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr2924)
                path = self.test()

                self._state.following.pop()

                # YarcParser.g:171:44: ( MATCH filter= test )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if LA55_0 == MATCH:
                    alt55 = 1
                if alt55 == 1:
                    # YarcParser.g:171:45: MATCH filter= test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr2927)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr2931)
                    filter = self.test()

                    self._state.following.pop()

                # YarcParser.g:171:65: ( LIMIT limit= test )?
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if LA56_0 == LIMIT:
                    alt56 = 1
                if alt56 == 1:
                    # YarcParser.g:171:66: LIMIT limit= test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr2936)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr2940)
                    limit = self.test()

                    self._state.following.pop()

                # YarcParser.g:171:85: ( RECURSIVE )?
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if LA57_0 == RECURSIVE:
                    alt57 = 1
                if alt57 == 1:
                    # YarcParser.g:171:85: RECURSIVE
                    RECURSIVE41 = self.match(
                        self.input, RECURSIVE, self.FOLLOW_RECURSIVE_in_fetch_expr2944
                    )

                # TEMPLATE REWRITE
                # 172:3: -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE)
                retval.st = self.templateLib.getInstanceOf(
                    "fetch_expr",
                    attributes={
                        "ext": ((ext is not None) and [ext.st] or [None])[0],
                        "path": ((path is not None) and [path.st] or [None])[0],
                        "filter": ((filter is not None) and [filter.st] or [None])[0],
                        "limit": ((limit is not None) and [limit.st] or [None])[0],
                        "recursive": RECURSIVE41,
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "fetch_expr"

    class test_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "test"
    # YarcParser.g:175:1: test : expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st);
    def test(
        self,
    ):
        retval = self.test_return()
        retval.start = self.input.LT(1)

        expr_ = None
        cond = None
        else_expr = None

        try:
            try:
                # YarcParser.g:175:13: (expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st))
                # YarcParser.g:175:15: expr_= or_test ( IF cond= or_test ELSE else_expr= test )?
                self._state.following.append(self.FOLLOW_or_test_in_test2995)
                expr_ = self.or_test()

                self._state.following.pop()

                # YarcParser.g:175:29: ( IF cond= or_test ELSE else_expr= test )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if LA58_0 == IF:
                    alt58 = 1
                if alt58 == 1:
                    # YarcParser.g:175:30: IF cond= or_test ELSE else_expr= test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test2998)

                    self._state.following.append(self.FOLLOW_or_test_in_test3002)
                    cond = self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test3004)

                    self._state.following.append(self.FOLLOW_test_in_test3008)
                    else_expr = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 176:13: -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st)
                retval.st = self.templateLib.getInstanceOf(
                    "test",
                    attributes={
                        "expr": ((expr_ is not None) and [expr_.st] or [None])[0],
                        "cond": ((cond is not None) and [cond.st] or [None])[0],
                        "else_expr": (
                            (else_expr is not None) and [else_expr.st] or [None]
                        )[0],
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "test"

    class test_nocond_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "test_nocond"
    # YarcParser.g:177:1: test_nocond : or_test -> test(expr=$or_test.st);
    def test_nocond(
        self,
    ):
        retval = self.test_nocond_return()
        retval.start = self.input.LT(1)

        or_test42 = None

        try:
            try:
                # YarcParser.g:177:13: ( or_test -> test(expr=$or_test.st))
                # YarcParser.g:177:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond3050)
                or_test42 = self.or_test()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 177:23: -> test(expr=$or_test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "test",
                    attributes={
                        "expr": ((or_test42 is not None) and [or_test42.st] or [None])[
                            0
                        ]
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "test_nocond"

    class or_test_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "or_test"
    # YarcParser.g:178:1: or_test :exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs);
    def or_test(
        self,
    ):
        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:178:13: (exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs))
                # YarcParser.g:178:15: exprs+= and_test ( OR exprs+= and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test3072)
                exprs = self.and_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:178:31: ( OR exprs+= and_test )*
                while True:  # loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if LA59_0 == OR:
                        alt59 = 1

                    if alt59 == 1:
                        # YarcParser.g:178:32: OR exprs+= and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test3075)

                        self._state.following.append(
                            self.FOLLOW_and_test_in_or_test3079
                        )
                        exprs = self.and_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop59

                # TEMPLATE REWRITE
                # 178:53: -> or_test(exprs=$exprs)
                retval.st = self.templateLib.getInstanceOf(
                    "or_test", attributes={"exprs": list_exprs}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "or_test"

    class and_test_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "and_test"
    # YarcParser.g:179:1: and_test :exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs);
    def and_test(
        self,
    ):
        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:179:13: (exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs))
                # YarcParser.g:179:15: exprs+= not_test ( AND exprs+= not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test3102)
                exprs = self.not_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:179:31: ( AND exprs+= not_test )*
                while True:  # loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if LA60_0 == AND:
                        alt60 = 1

                    if alt60 == 1:
                        # YarcParser.g:179:32: AND exprs+= not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test3105)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test3109
                        )
                        exprs = self.not_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop60

                # TEMPLATE REWRITE
                # 179:54: -> and_test(exprs=$exprs)
                retval.st = self.templateLib.getInstanceOf(
                    "and_test", attributes={"exprs": list_exprs}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "and_test"

    class not_test_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "not_test"
    # YarcParser.g:180:1: not_test : ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st});
    def not_test(
        self,
    ):
        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        expr_ = None
        comparison43 = None

        try:
            try:
                # YarcParser.g:180:13: ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st})
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if LA61_0 == NOT:
                    alt61 = 1
                elif LA61_0 in {
                    BIT_NOT,
                    COMBINE,
                    DISTRIBUTION,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LEN,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    PLUS,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                }:
                    alt61 = 2
                else:
                    nvae = NoViableAltException("", 61, 0, self.input)

                    raise nvae

                if alt61 == 1:
                    # YarcParser.g:180:15: NOT expr_= not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test3130)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test3134)
                    expr_ = self.not_test()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 180:35: -> not_test(expr=$expr_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "not_test",
                        attributes={
                            "expr": ((expr_ is not None) and [expr_.st] or [None])[0]
                        },
                    )

                elif alt61 == 2:
                    # YarcParser.g:181:15: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test3160)
                    comparison43 = self.comparison()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 181:26: -> {$comparison.st}
                    retval.st = (
                        (comparison43 is not None) and [comparison43.st] or [None]
                    )[0]

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "not_test"

    class comparison_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "comparison"
    # YarcParser.g:182:1: comparison :exprs+= expr (ops+= comp_op exprs+= expr )* -> comparison(exprs=$exprsops=$ops);
    def comparison(
        self,
    ):
        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        list_ops = None
        exprs = None
        ops = None
        try:
            try:
                # YarcParser.g:182:13: (exprs+= expr (ops+= comp_op exprs+= expr )* -> comparison(exprs=$exprsops=$ops))
                # YarcParser.g:182:15: exprs+= expr (ops+= comp_op exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison3174)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:182:27: (ops+= comp_op exprs+= expr )*
                while True:  # loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if LA62_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt62 = 1

                    if alt62 == 1:
                        # YarcParser.g:182:28: ops+= comp_op exprs+= expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison3179
                        )
                        ops = self.comp_op()

                        self._state.following.pop()
                        if list_ops is None:
                            list_ops = []
                        list_ops.append(ops.st)

                        self._state.following.append(self.FOLLOW_expr_in_comparison3183)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop62

                # TEMPLATE REWRITE
                # 182:55: -> comparison(exprs=$exprsops=$ops)
                retval.st = self.templateLib.getInstanceOf(
                    "comparison", attributes={"exprs": list_exprs, "ops": list_ops}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "comparison"

    class comp_op_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "comp_op"
    # YarcParser.g:183:1: comp_op : op= ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT ) -> {$op};
    def comp_op(
        self,
    ):
        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        op = None

        try:
            try:
                # YarcParser.g:183:13: (op= ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT ) -> {$op})
                # YarcParser.g:183:15: op= ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                pass
                # YarcParser.g:183:18: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                alt63 = 10
                LA63 = self.input.LA(1)
                if LA63 in {LT}:
                    alt63 = 1
                elif LA63 in {GT}:
                    alt63 = 2
                elif LA63 in {EQUALS}:
                    alt63 = 3
                elif LA63 in {GT_EQ}:
                    alt63 = 4
                elif LA63 in {LT_EQ}:
                    alt63 = 5
                elif LA63 in {NOT_EQ}:
                    alt63 = 6
                elif LA63 in {IN}:
                    alt63 = 7
                elif LA63 in {NOT}:
                    alt63 = 8
                elif LA63 in {IS}:
                    LA63_9 = self.input.LA(2)

                    if LA63_9 == NOT:
                        alt63 = 10
                    elif LA63_9 in {
                        BIT_NOT,
                        COMBINE,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LEN,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt63 = 9
                    else:
                        nvae = NoViableAltException("", 63, 9, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 63, 0, self.input)

                    raise nvae

                if alt63 == 1:
                    # YarcParser.g:183:19: LT
                    op = self.match(self.input, LT, self.FOLLOW_LT_in_comp_op3213)

                elif alt63 == 2:
                    # YarcParser.g:183:24: GT
                    op = self.match(self.input, GT, self.FOLLOW_GT_in_comp_op3217)

                elif alt63 == 3:
                    # YarcParser.g:183:29: EQUALS
                    op = self.match(
                        self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op3221
                    )

                elif alt63 == 4:
                    # YarcParser.g:183:38: GT_EQ
                    op = self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op3225)

                elif alt63 == 5:
                    # YarcParser.g:183:46: LT_EQ
                    op = self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op3229)

                elif alt63 == 6:
                    # YarcParser.g:183:54: NOT_EQ
                    op = self.match(
                        self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op3233
                    )

                elif alt63 == 7:
                    # YarcParser.g:183:63: IN
                    op = self.match(self.input, IN, self.FOLLOW_IN_in_comp_op3237)

                elif alt63 == 8:
                    # YarcParser.g:183:68: NOT IN
                    op = self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op3241)

                    op = self.match(self.input, IN, self.FOLLOW_IN_in_comp_op3243)

                elif alt63 == 9:
                    # YarcParser.g:183:77: IS
                    op = self.match(self.input, IS, self.FOLLOW_IS_in_comp_op3247)

                elif alt63 == 10:
                    # YarcParser.g:183:82: IS NOT
                    op = self.match(self.input, IS, self.FOLLOW_IS_in_comp_op3251)

                    op = self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op3253)

                # TEMPLATE REWRITE
                # 183:90: -> {$op}
                retval.st = op

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "comp_op"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "expr"
    # YarcParser.g:184:1: expr :exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs);
    def expr(
        self,
    ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:184:13: (exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs))
                # YarcParser.g:184:15: exprs+= xor_expr ( BIT_OR exprs+= xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr3274)
                exprs = self.xor_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:184:31: ( BIT_OR exprs+= xor_expr )*
                while True:  # loop64
                    alt64 = 2
                    LA64_0 = self.input.LA(1)

                    if LA64_0 == BIT_OR:
                        alt64 = 1

                    if alt64 == 1:
                        # YarcParser.g:184:32: BIT_OR exprs+= xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr3277)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr3281)
                        exprs = self.xor_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop64

                # TEMPLATE REWRITE
                # 184:57: -> expr(exprs=$exprs)
                retval.st = self.templateLib.getInstanceOf(
                    "expr", attributes={"exprs": list_exprs}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "expr"

    class xor_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "xor_expr"
    # YarcParser.g:185:1: xor_expr :exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs);
    def xor_expr(
        self,
    ):
        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:185:13: (exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs))
                # YarcParser.g:185:15: exprs+= and_expr ( XOR exprs+= and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr3304)
                exprs = self.and_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:185:31: ( XOR exprs+= and_expr )*
                while True:  # loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if LA65_0 == XOR:
                        alt65 = 1

                    if alt65 == 1:
                        # YarcParser.g:185:32: XOR exprs+= and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr3307)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr3311
                        )
                        exprs = self.and_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop65

                # TEMPLATE REWRITE
                # 185:54: -> xor_expr(exprs=$exprs)
                retval.st = self.templateLib.getInstanceOf(
                    "xor_expr", attributes={"exprs": list_exprs}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "xor_expr"

    class and_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "and_expr"
    # YarcParser.g:186:1: and_expr :exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs);
    def and_expr(
        self,
    ):
        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:186:13: (exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs))
                # YarcParser.g:186:15: exprs+= shift_expr ( BIT_AND exprs+= shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr3334)
                exprs = self.shift_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:186:33: ( BIT_AND exprs+= shift_expr )*
                while True:  # loop66
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if LA66_0 == BIT_AND:
                        alt66 = 1

                    if alt66 == 1:
                        # YarcParser.g:186:34: BIT_AND exprs+= shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr3337
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr3341
                        )
                        exprs = self.shift_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop66

                # TEMPLATE REWRITE
                # 186:62: -> and_expr(exprs=$exprs)
                retval.st = self.templateLib.getInstanceOf(
                    "and_expr", attributes={"exprs": list_exprs}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "and_expr"

    class shift_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "shift_expr"
    # YarcParser.g:187:1: shift_expr :exprs+= arith_expr (ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsops=$ops);
    def shift_expr(
        self,
    ):
        retval = self.shift_expr_return()
        retval.start = self.input.LT(1)

        ops = None
        list_ops = None
        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:187:13: (exprs+= arith_expr (ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsops=$ops))
                # YarcParser.g:187:15: exprs+= arith_expr (ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr3362)
                exprs = self.arith_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:187:33: (ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                while True:  # loop68
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if LA68_0 in {LSHIFT, RSHIFT}:
                        alt68 = 1

                    if alt68 == 1:
                        # YarcParser.g:187:34: ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr
                        pass
                        # YarcParser.g:187:39: ( LSHIFT | RSHIFT )
                        alt67 = 2
                        LA67_0 = self.input.LA(1)

                        if LA67_0 == LSHIFT:
                            alt67 = 1
                        elif LA67_0 == RSHIFT:
                            alt67 = 2
                        else:
                            nvae = NoViableAltException("", 67, 0, self.input)

                            raise nvae

                        if alt67 == 1:
                            # YarcParser.g:187:40: LSHIFT
                            ops = self.match(
                                self.input, LSHIFT, self.FOLLOW_LSHIFT_in_shift_expr3368
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt67 == 2:
                            # YarcParser.g:187:49: RSHIFT
                            ops = self.match(
                                self.input, RSHIFT, self.FOLLOW_RSHIFT_in_shift_expr3372
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr3377
                        )
                        exprs = self.arith_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop68

                # TEMPLATE REWRITE
                # 187:77: -> shift_expr(exprs=$exprsops=$ops)
                retval.st = self.templateLib.getInstanceOf(
                    "shift_expr", attributes={"exprs": list_exprs, "ops": list_ops}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "shift_expr"

    class arith_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "arith_expr"
    # YarcParser.g:188:1: arith_expr :terms+= term (ops+= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsops=$ops);
    def arith_expr(
        self,
    ):
        retval = self.arith_expr_return()
        retval.start = self.input.LT(1)

        ops = None
        list_ops = None
        list_terms = None
        terms = None
        try:
            try:
                # YarcParser.g:188:13: (terms+= term (ops+= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsops=$ops))
                # YarcParser.g:188:15: terms+= term (ops+= ( PLUS | MINUS ) terms+= term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr3403)
                terms = self.term()

                self._state.following.pop()
                if list_terms is None:
                    list_terms = []
                list_terms.append(terms.st)

                # YarcParser.g:188:27: (ops+= ( PLUS | MINUS ) terms+= term )*
                while True:  # loop70
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if LA70_0 in {MINUS, PLUS}:
                        alt70 = 1

                    if alt70 == 1:
                        # YarcParser.g:188:28: ops+= ( PLUS | MINUS ) terms+= term
                        pass
                        # YarcParser.g:188:33: ( PLUS | MINUS )
                        alt69 = 2
                        LA69_0 = self.input.LA(1)

                        if LA69_0 == PLUS:
                            alt69 = 1
                        elif LA69_0 == MINUS:
                            alt69 = 2
                        else:
                            nvae = NoViableAltException("", 69, 0, self.input)

                            raise nvae

                        if alt69 == 1:
                            # YarcParser.g:188:34: PLUS
                            ops = self.match(
                                self.input, PLUS, self.FOLLOW_PLUS_in_arith_expr3409
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt69 == 2:
                            # YarcParser.g:188:41: MINUS
                            ops = self.match(
                                self.input, MINUS, self.FOLLOW_MINUS_in_arith_expr3413
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        self._state.following.append(self.FOLLOW_term_in_arith_expr3418)
                        terms = self.term()

                        self._state.following.pop()
                        if list_terms is None:
                            list_terms = []
                        list_terms.append(terms.st)

                    else:
                        break  # loop70

                # TEMPLATE REWRITE
                # 188:62: -> arith_expr(terms=$termsops=$ops)
                retval.st = self.templateLib.getInstanceOf(
                    "arith_expr", attributes={"terms": list_terms, "ops": list_ops}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "arith_expr"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "term"
    # YarcParser.g:189:1: term :factors+= factor (ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsops=$ops);
    def term(
        self,
    ):
        retval = self.term_return()
        retval.start = self.input.LT(1)

        ops = None
        list_ops = None
        list_factors = None
        factors = None
        try:
            try:
                # YarcParser.g:189:13: (factors+= factor (ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsops=$ops))
                # YarcParser.g:189:15: factors+= factor (ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                self._state.following.append(self.FOLLOW_factor_in_term3450)
                factors = self.factor()

                self._state.following.pop()
                if list_factors is None:
                    list_factors = []
                list_factors.append(factors.st)

                # YarcParser.g:189:31: (ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                while True:  # loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if LA72_0 in {DIV, IDIV, MOD, MUL}:
                        alt72 = 1

                    if alt72 == 1:
                        # YarcParser.g:189:32: ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor
                        pass
                        # YarcParser.g:189:37: ( MUL | DIV | MOD | IDIV )
                        alt71 = 4
                        LA71 = self.input.LA(1)
                        if LA71 in {MUL}:
                            alt71 = 1
                        elif LA71 in {DIV}:
                            alt71 = 2
                        elif LA71 in {MOD}:
                            alt71 = 3
                        elif LA71 in {IDIV}:
                            alt71 = 4
                        else:
                            nvae = NoViableAltException("", 71, 0, self.input)

                            raise nvae

                        if alt71 == 1:
                            # YarcParser.g:189:38: MUL
                            ops = self.match(
                                self.input, MUL, self.FOLLOW_MUL_in_term3456
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt71 == 2:
                            # YarcParser.g:189:44: DIV
                            ops = self.match(
                                self.input, DIV, self.FOLLOW_DIV_in_term3460
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt71 == 3:
                            # YarcParser.g:189:50: MOD
                            ops = self.match(
                                self.input, MOD, self.FOLLOW_MOD_in_term3464
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt71 == 4:
                            # YarcParser.g:189:56: IDIV
                            ops = self.match(
                                self.input, IDIV, self.FOLLOW_IDIV_in_term3468
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        self._state.following.append(self.FOLLOW_factor_in_term3473)
                        factors = self.factor()

                        self._state.following.pop()
                        if list_factors is None:
                            list_factors = []
                        list_factors.append(factors.st)

                    else:
                        break  # loop72

                # TEMPLATE REWRITE
                # 189:80: -> term(factors=$factorsops=$ops)
                retval.st = self.templateLib.getInstanceOf(
                    "term", attributes={"factors": list_factors, "ops": list_ops}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "term"

    class factor_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "factor"
    # YarcParser.g:190:1: factor : (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st});
    def factor(
        self,
    ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)

        prefix = None
        factor_ = None
        power44 = None

        try:
            try:
                # YarcParser.g:190:13: (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st})
                alt74 = 2
                LA74_0 = self.input.LA(1)

                if LA74_0 in {BIT_NOT, MINUS, PLUS}:
                    alt74 = 1
                elif LA74_0 in {
                    COMBINE,
                    DISTRIBUTION,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LEN,
                    LPAREN,
                    LT,
                    NONE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                }:
                    alt74 = 2
                else:
                    nvae = NoViableAltException("", 74, 0, self.input)

                    raise nvae

                if alt74 == 1:
                    # YarcParser.g:190:15: prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor
                    pass
                    # YarcParser.g:190:22: ( PLUS | MINUS | BIT_NOT )
                    alt73 = 3
                    LA73 = self.input.LA(1)
                    if LA73 in {PLUS}:
                        alt73 = 1
                    elif LA73 in {MINUS}:
                        alt73 = 2
                    elif LA73 in {BIT_NOT}:
                        alt73 = 3
                    else:
                        nvae = NoViableAltException("", 73, 0, self.input)

                        raise nvae

                    if alt73 == 1:
                        # YarcParser.g:190:23: PLUS
                        prefix = self.match(
                            self.input, PLUS, self.FOLLOW_PLUS_in_factor3504
                        )

                    elif alt73 == 2:
                        # YarcParser.g:190:30: MINUS
                        prefix = self.match(
                            self.input, MINUS, self.FOLLOW_MINUS_in_factor3508
                        )

                    elif alt73 == 3:
                        # YarcParser.g:190:38: BIT_NOT
                        prefix = self.match(
                            self.input, BIT_NOT, self.FOLLOW_BIT_NOT_in_factor3512
                        )

                    self._state.following.append(self.FOLLOW_factor_in_factor3517)
                    factor_ = self.factor()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 190:62: -> prefix_factor(factor=$factor_.stprefix=$prefix)
                    retval.st = self.templateLib.getInstanceOf(
                        "prefix_factor",
                        attributes={
                            "factor": (
                                (factor_ is not None) and [factor_.st] or [None]
                            )[0],
                            "prefix": prefix,
                        },
                    )

                elif alt74 == 2:
                    # YarcParser.g:191:15: power
                    self._state.following.append(self.FOLLOW_power_in_factor3547)
                    power44 = self.power()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 191:21: -> {$power.st}
                    retval.st = ((power44 is not None) and [power44.st] or [None])[0]

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "factor"

    class power_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "power"
    # YarcParser.g:192:1: power : atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st);
    def power(
        self,
    ):
        retval = self.power_return()
        retval.start = self.input.LT(1)

        atom_expr45 = None
        factor46 = None

        try:
            try:
                # YarcParser.g:192:13: ( atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st))
                # YarcParser.g:192:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power3564)
                atom_expr45 = self.atom_expr()

                self._state.following.pop()

                # YarcParser.g:192:25: ( POWER factor )?
                alt75 = 2
                LA75_0 = self.input.LA(1)

                if LA75_0 == POWER:
                    alt75 = 1
                if alt75 == 1:
                    # YarcParser.g:192:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power3567)

                    self._state.following.append(self.FOLLOW_factor_in_power3569)
                    factor46 = self.factor()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 192:41: -> power(atom=$atom_expr.stfactor=$factor.st)
                retval.st = self.templateLib.getInstanceOf(
                    "power",
                    attributes={
                        "atom": (
                            (atom_expr45 is not None) and [atom_expr45.st] or [None]
                        )[0],
                        "factor": ((factor46 is not None) and [factor46.st] or [None])[
                            0
                        ],
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "power"

    class atom_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "atom_expr"
    # YarcParser.g:193:1: atom_expr : atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers);
    def atom_expr(
        self,
    ):
        retval = self.atom_expr_return()
        retval.start = self.input.LT(1)

        list_trailers = None
        atom47 = None
        trailers = None
        try:
            try:
                # YarcParser.g:193:13: ( atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers))
                # YarcParser.g:193:15: atom (trailers+= trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr3594)
                atom47 = self.atom()

                self._state.following.pop()

                # YarcParser.g:193:20: (trailers+= trailer )*
                while True:  # loop76
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if LA76_0 in {DOT, LBRACK}:
                        alt76 = 1

                    if alt76 == 1:
                        # YarcParser.g:193:21: trailers+= trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr3599
                        )
                        trailers = self.trailer()

                        self._state.following.pop()
                        if list_trailers is None:
                            list_trailers = []
                        list_trailers.append(trailers.st)

                    else:
                        break  # loop76

                # TEMPLATE REWRITE
                # 193:41: -> atom_expr(atom=$atom.sttrailers=$trailers)
                retval.st = self.templateLib.getInstanceOf(
                    "atom_expr",
                    attributes={
                        "atom": ((atom47 is not None) and [atom47.st] or [None])[0],
                        "trailers": list_trailers,
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "atom_expr"

    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "atom"
    # YarcParser.g:194:1: atom : ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=setting)| distribution -> {$distribution.st}| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {self.handler.expand_string($STRING)}| NONE -> null(| TRUE -> true(| FALSE -> false() ;
    def atom(
        self,
    ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)

        SETTING_ID52 = None
        INTEGER54 = None
        FLOAT_NUMBER55 = None
        STRING56 = None
        test_ = None
        testlist_comp48 = None
        vector_comp49 = None
        dict_or_set_maker50 = None
        name51 = None
        distribution53 = None

        try:
            try:
                # YarcParser.g:194:5: ( ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=setting)| distribution -> {$distribution.st}| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {self.handler.expand_string($STRING)}| NONE -> null(| TRUE -> true(| FALSE -> false() )
                # YarcParser.g:195:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=setting)| distribution -> {$distribution.st}| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {self.handler.expand_string($STRING)}| NONE -> null(| TRUE -> true(| FALSE -> false()
                pass
                # YarcParser.g:195:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=setting)| distribution -> {$distribution.st}| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {self.handler.expand_string($STRING)}| NONE -> null(| TRUE -> true(| FALSE -> false()
                alt80 = 14
                LA80 = self.input.LA(1)
                if LA80 in {LPAREN}:
                    alt80 = 1
                elif LA80 in {LBRACK}:
                    alt80 = 2
                elif LA80 in {LT}:
                    alt80 = 3
                elif LA80 in {LBRACE}:
                    alt80 = 4
                elif LA80 in {LEN}:
                    alt80 = 5
                elif LA80 in {ID, UNDERSCORE}:
                    alt80 = 6
                elif LA80 in {SETTING_ID}:
                    alt80 = 7
                elif LA80 in {COMBINE, DISTRIBUTION}:
                    alt80 = 8
                elif LA80 in {INTEGER}:
                    alt80 = 9
                elif LA80 in {FLOAT_NUMBER}:
                    alt80 = 10
                elif LA80 in {STRING}:
                    alt80 = 11
                elif LA80 in {NONE}:
                    alt80 = 12
                elif LA80 in {TRUE}:
                    alt80 = 13
                elif LA80 in {FALSE}:
                    alt80 = 14
                else:
                    nvae = NoViableAltException("", 80, 0, self.input)

                    raise nvae

                if alt80 == 1:
                    # YarcParser.g:195:4: LPAREN test_= test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom3624)

                    self._state.following.append(self.FOLLOW_test_in_atom3628)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom3630)

                    # TEMPLATE REWRITE
                    # 195:29: -> parenthesized_expr(expr=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "parenthesized_expr",
                        attributes={
                            "expr": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt80 == 2:
                    # YarcParser.g:196:5: LBRACK ( testlist_comp )? RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom3645)

                    # YarcParser.g:196:12: ( testlist_comp )?
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if LA77_0 in {
                        BIT_NOT,
                        COMBINE,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LEN,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NOT,
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt77 = 1
                    if alt77 == 1:
                        # YarcParser.g:196:12: testlist_comp
                        self._state.following.append(
                            self.FOLLOW_testlist_comp_in_atom3647
                        )
                        testlist_comp48 = self.testlist_comp()

                        self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom3650)

                    # TEMPLATE REWRITE
                    # 196:34: -> list(list_comp=$testlist_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list",
                        attributes={
                            "list_comp": (
                                (testlist_comp48 is not None)
                                and [testlist_comp48.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt80 == 3:
                    # YarcParser.g:197:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom3665)

                    # YarcParser.g:197:8: ( vector_comp )?
                    alt78 = 2
                    LA78_0 = self.input.LA(1)

                    if LA78_0 in {
                        BIT_NOT,
                        COMBINE,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LEN,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt78 = 1
                    if alt78 == 1:
                        # YarcParser.g:197:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom3667
                        )
                        vector_comp49 = self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom3670)

                    # TEMPLATE REWRITE
                    # 197:24: -> vector(values=$vector_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "vector",
                        attributes={
                            "values": (
                                (vector_comp49 is not None)
                                and [vector_comp49.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt80 == 4:
                    # YarcParser.g:198:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom3685)

                    # YarcParser.g:198:12: ( dict_or_set_maker )?
                    alt79 = 2
                    LA79_0 = self.input.LA(1)

                    if LA79_0 in {
                        BIT_NOT,
                        COMBINE,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LEN,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NOT,
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt79 = 1
                    if alt79 == 1:
                        # YarcParser.g:198:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom3687
                        )
                        dict_or_set_maker50 = self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom3690)

                    # TEMPLATE REWRITE
                    # 198:38: -> dict(dict_comp=$dict_or_set_maker.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dict",
                        attributes={
                            "dict_comp": (
                                (dict_or_set_maker50 is not None)
                                and [dict_or_set_maker50.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt80 == 5:
                    # YarcParser.g:199:5: LEN LPAREN test_= test RPAREN
                    self.match(self.input, LEN, self.FOLLOW_LEN_in_atom3705)

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom3707)

                    self._state.following.append(self.FOLLOW_test_in_atom3711)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom3713)

                    # TEMPLATE REWRITE
                    # 199:34: -> len(value=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "len",
                        attributes={
                            "value": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt80 == 6:
                    # YarcParser.g:200:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom3728)
                    name51 = self.name()

                    self._state.following.pop()

                    # action start
                    self.handler.lookup(
                        ((name51 is not None) and [name51.st] or [None])[0]
                    )
                    # action end

                    # TEMPLATE REWRITE
                    # 200:42: -> {$name.st}
                    retval.st = ((name51 is not None) and [name51.st] or [None])[0]

                elif alt80 == 7:
                    # YarcParser.g:201:5: SETTING_ID
                    SETTING_ID52 = self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom3740
                    )

                    # action start
                    setting = self.handler.parse_setting_id(SETTING_ID52)
                    # action end

                    # TEMPLATE REWRITE
                    # 201:70: -> setting_id(id=setting)
                    retval.st = self.templateLib.getInstanceOf(
                        "setting_id", attributes={"id": setting}
                    )

                elif alt80 == 8:
                    # YarcParser.g:202:5: distribution
                    self._state.following.append(self.FOLLOW_distribution_in_atom3757)
                    distribution53 = self.distribution()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 202:18: -> {$distribution.st}
                    retval.st = (
                        (distribution53 is not None) and [distribution53.st] or [None]
                    )[0]

                elif alt80 == 9:
                    # YarcParser.g:203:5: INTEGER
                    INTEGER54 = self.match(
                        self.input, INTEGER, self.FOLLOW_INTEGER_in_atom3767
                    )

                    # TEMPLATE REWRITE
                    # 203:13: -> {$INTEGER.text}
                    retval.st = INTEGER54.text

                elif alt80 == 10:
                    # YarcParser.g:204:5: FLOAT_NUMBER
                    FLOAT_NUMBER55 = self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom3777
                    )

                    # TEMPLATE REWRITE
                    # 204:18: -> {$FLOAT_NUMBER.text}
                    retval.st = FLOAT_NUMBER55.text

                elif alt80 == 11:
                    # YarcParser.g:205:5: STRING
                    STRING56 = self.match(
                        self.input, STRING, self.FOLLOW_STRING_in_atom3787
                    )

                    # TEMPLATE REWRITE
                    # 205:12: -> {self.handler.expand_string($STRING)}
                    retval.st = self.handler.expand_string(STRING56)

                elif alt80 == 12:
                    # YarcParser.g:206:5: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom3797)

                    # TEMPLATE REWRITE
                    # 206:10: -> null(
                    retval.st = self.templateLib.getInstanceOf("null")

                elif alt80 == 13:
                    # YarcParser.g:207:5: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom3809)

                    # TEMPLATE REWRITE
                    # 207:10: -> true(
                    retval.st = self.templateLib.getInstanceOf("true")

                elif alt80 == 14:
                    # YarcParser.g:208:5: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom3821)

                    # TEMPLATE REWRITE
                    # 208:11: -> false(
                    retval.st = self.templateLib.getInstanceOf("false")

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "atom"

    class name_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "name"
    # YarcParser.g:212:1: name : ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text});
    def name(
        self,
    ):
        retval = self.name_return()
        retval.start = self.input.LT(1)

        ID57 = None
        UNDERSCORE58 = None

        try:
            try:
                # YarcParser.g:212:5: ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text})
                alt81 = 2
                LA81_0 = self.input.LA(1)

                if LA81_0 == ID:
                    alt81 = 1
                elif LA81_0 == UNDERSCORE:
                    alt81 = 2
                else:
                    nvae = NoViableAltException("", 81, 0, self.input)

                    raise nvae

                if alt81 == 1:
                    # YarcParser.g:213:3: ID
                    ID57 = self.match(self.input, ID, self.FOLLOW_ID_in_name3841)

                    # TEMPLATE REWRITE
                    # 213:6: -> {$ID.text}
                    retval.st = ID57.text

                elif alt81 == 2:
                    # YarcParser.g:214:5: UNDERSCORE
                    UNDERSCORE58 = self.match(
                        self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_name3851
                    )

                    # TEMPLATE REWRITE
                    # 214:16: -> {$UNDERSCORE.text}
                    retval.st = UNDERSCORE58.text

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "name"

    class distribution_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "distribution"
    # YarcParser.g:217:1: distribution : ( DISTRIBUTION LPAREN args= arglist RPAREN -> distribution(name=self.handler.map($DISTRIBUTION)arglist=$args.st)| COMBINE LPAREN args= arglist RPAREN -> combined_distribution(distrs=$args.st));
    def distribution(
        self,
    ):
        retval = self.distribution_return()
        retval.start = self.input.LT(1)

        DISTRIBUTION59 = None
        args = None

        try:
            try:
                # YarcParser.g:217:14: ( DISTRIBUTION LPAREN args= arglist RPAREN -> distribution(name=self.handler.map($DISTRIBUTION)arglist=$args.st)| COMBINE LPAREN args= arglist RPAREN -> combined_distribution(distrs=$args.st))
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if LA82_0 == DISTRIBUTION:
                    alt82 = 1
                elif LA82_0 == COMBINE:
                    alt82 = 2
                else:
                    nvae = NoViableAltException("", 82, 0, self.input)

                    raise nvae

                if alt82 == 1:
                    # YarcParser.g:217:16: DISTRIBUTION LPAREN args= arglist RPAREN
                    DISTRIBUTION59 = self.match(
                        self.input,
                        DISTRIBUTION,
                        self.FOLLOW_DISTRIBUTION_in_distribution3864,
                    )

                    self.match(
                        self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution3866
                    )

                    self._state.following.append(
                        self.FOLLOW_arglist_in_distribution3870
                    )
                    args = self.arglist()

                    self._state.following.pop()

                    self.match(
                        self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution3872
                    )

                    # TEMPLATE REWRITE
                    # 217:56: -> distribution(name=self.handler.map($DISTRIBUTION)arglist=$args.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "distribution",
                        attributes={
                            "name": self.handler.map(DISTRIBUTION59),
                            "arglist": ((args is not None) and [args.st] or [None])[0],
                        },
                    )

                elif alt82 == 2:
                    # YarcParser.g:218:18: COMBINE LPAREN args= arglist RPAREN
                    self.match(
                        self.input, COMBINE, self.FOLLOW_COMBINE_in_distribution3905
                    )

                    self.match(
                        self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution3907
                    )

                    self._state.following.append(
                        self.FOLLOW_arglist_in_distribution3911
                    )
                    args = self.arglist()

                    self._state.following.pop()

                    self.match(
                        self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution3913
                    )

                    # TEMPLATE REWRITE
                    # 218:53: -> combined_distribution(distrs=$args.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "combined_distribution",
                        attributes={
                            "distrs": ((args is not None) and [args.st] or [None])[0]
                        },
                    )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "distribution"

    class testlist_comp_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "testlist_comp"
    # YarcParser.g:220:1: testlist_comp :exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) ;
    def testlist_comp(
        self,
    ):
        retval = self.testlist_comp_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        to = None
        step = None
        comp_for60 = None
        exprs = None
        try:
            try:
                # YarcParser.g:220:15: (exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) )
                # YarcParser.g:220:18: exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                self._state.following.append(self.FOLLOW_test_in_testlist_comp3934)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:220:30: ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                alt85 = 3
                LA85 = self.input.LA(1)
                if LA85 in {FOR}:
                    alt85 = 1
                elif LA85 in {COMMA, RBRACK}:
                    alt85 = 2
                elif LA85 in {RANGE}:
                    alt85 = 3
                else:
                    nvae = NoViableAltException("", 85, 0, self.input)

                    raise nvae

                if alt85 == 1:
                    # YarcParser.g:220:32: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp3938
                    )
                    comp_for60 = self.comp_for()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 220:41: -> list_comp(expr=$exprs[0]for=$comp_for.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list_comp",
                        attributes={
                            "expr": list_exprs[0],
                            "for": (
                                (comp_for60 is not None) and [comp_for60.st] or [None]
                            )[0],
                        },
                    )

                elif alt85 == 2:
                    # YarcParser.g:221:32: ( COMMA exprs+= test )*
                    pass
                    # YarcParser.g:221:32: ( COMMA exprs+= test )*
                    while True:  # loop83
                        alt83 = 2
                        LA83_0 = self.input.LA(1)

                        if LA83_0 == COMMA:
                            alt83 = 1

                        if alt83 == 1:
                            # YarcParser.g:221:33: COMMA exprs+= test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp3986,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp3990
                            )
                            exprs = self.test()

                            self._state.following.pop()
                            if list_exprs is None:
                                list_exprs = []
                            list_exprs.append(exprs.st)

                        else:
                            break  # loop83

                    # TEMPLATE REWRITE
                    # 221:53: -> test_list(exprs=$exprs)
                    retval.st = self.templateLib.getInstanceOf(
                        "test_list", attributes={"exprs": list_exprs}
                    )

                elif alt85 == 3:
                    # YarcParser.g:222:32: RANGE to= test ( STEP step= test )?
                    self.match(
                        self.input, RANGE, self.FOLLOW_RANGE_in_testlist_comp4034
                    )

                    self._state.following.append(self.FOLLOW_test_in_testlist_comp4038)
                    to = self.test()

                    self._state.following.pop()

                    # YarcParser.g:222:46: ( STEP step= test )?
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if LA84_0 == STEP:
                        alt84 = 1
                    if alt84 == 1:
                        # YarcParser.g:222:47: STEP step= test
                        self.match(
                            self.input, STEP, self.FOLLOW_STEP_in_testlist_comp4041
                        )

                        self._state.following.append(
                            self.FOLLOW_test_in_testlist_comp4045
                        )
                        step = self.test()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 222:64: -> range(from=$exprs[0]to=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "range",
                        attributes={
                            "from": list_exprs[0],
                            "to": ((to is not None) and [to.st] or [None])[0],
                            "step": ((step is not None) and [step.st] or [None])[0],
                        },
                    )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "testlist_comp"

    class vector_comp_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "vector_comp"
    # YarcParser.g:225:1: vector_comp : x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st);
    def vector_comp(
        self,
    ):
        retval = self.vector_comp_return()
        retval.start = self.input.LT(1)

        x = None
        y = None
        z = None

        try:
            try:
                # YarcParser.g:225:15: (x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st))
                # YarcParser.g:225:17: x= expr COMMA y= expr COMMA z= expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp4109)
                x = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp4111)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp4115)
                y = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp4117)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp4121)
                z = self.expr()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 225:50: -> vector_comp(x=$x.sty=$y.stz=$z.st)
                retval.st = self.templateLib.getInstanceOf(
                    "vector_comp",
                    attributes={
                        "x": ((x is not None) and [x.st] or [None])[0],
                        "y": ((y is not None) and [y.st] or [None])[0],
                        "z": ((z is not None) and [z.st] or [None])[0],
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vector_comp"

    class trailer_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "trailer"
    # YarcParser.g:226:1: trailer : ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st));
    def trailer(
        self,
    ):
        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        subscriptlist61 = None
        name62 = None

        try:
            try:
                # YarcParser.g:226:15: ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st))
                alt86 = 2
                LA86_0 = self.input.LA(1)

                if LA86_0 == LBRACK:
                    alt86 = 1
                elif LA86_0 == DOT:
                    alt86 = 2
                else:
                    nvae = NoViableAltException("", 86, 0, self.input)

                    raise nvae

                if alt86 == 1:
                    # YarcParser.g:226:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer4153)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer4155
                    )
                    subscriptlist61 = self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer4157)

                    # TEMPLATE REWRITE
                    # 226:45: -> index(index=$subscriptlist.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "index",
                        attributes={
                            "index": (
                                (subscriptlist61 is not None)
                                and [subscriptlist61.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt86 == 2:
                    # YarcParser.g:227:17: DOT name
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer4185)

                    self._state.following.append(self.FOLLOW_name_in_trailer4187)
                    name62 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 227:26: -> dot_attr(attr=$name.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dot_attr",
                        attributes={
                            "attr": ((name62 is not None) and [name62.st] or [None])[0]
                        },
                    )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "trailer"

    class arglist_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "arglist"
    # YarcParser.g:228:1: arglist :args+= argument ( COMMA args+= argument )* -> arg_list(args=$args);
    def arglist(
        self,
    ):
        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        list_args = None
        args = None
        try:
            try:
                # YarcParser.g:228:15: (args+= argument ( COMMA args+= argument )* -> arg_list(args=$args))
                # YarcParser.g:228:17: args+= argument ( COMMA args+= argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist4211)
                args = self.argument()

                self._state.following.pop()
                if list_args is None:
                    list_args = []
                list_args.append(args.st)

                # YarcParser.g:228:32: ( COMMA args+= argument )*
                while True:  # loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if LA87_0 == COMMA:
                        alt87 = 1

                    if alt87 == 1:
                        # YarcParser.g:228:33: COMMA args+= argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist4214)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist4218
                        )
                        args = self.argument()

                        self._state.following.pop()
                        if list_args is None:
                            list_args = []
                        list_args.append(args.st)

                    else:
                        break  # loop87

                # TEMPLATE REWRITE
                # 228:56: -> arg_list(args=$args)
                retval.st = self.templateLib.getInstanceOf(
                    "arg_list", attributes={"args": list_args}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "arglist"

    class argument_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "argument"
    # YarcParser.g:229:1: argument : kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st);
    def argument(
        self,
    ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)

        kw_or_arg = None
        arg = None

        try:
            try:
                # YarcParser.g:229:15: (kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st))
                # YarcParser.g:229:17: kw_or_arg= test ( ASSIGN arg= test )?
                self._state.following.append(self.FOLLOW_test_in_argument4243)
                kw_or_arg = self.test()

                self._state.following.pop()

                # YarcParser.g:229:32: ( ASSIGN arg= test )?
                alt88 = 2
                LA88_0 = self.input.LA(1)

                if LA88_0 == ASSIGN:
                    alt88 = 1
                if alt88 == 1:
                    # YarcParser.g:229:33: ASSIGN arg= test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument4246)

                    self._state.following.append(self.FOLLOW_test_in_argument4250)
                    arg = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 229:51: -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st)
                retval.st = self.templateLib.getInstanceOf(
                    "arg",
                    attributes={
                        "kw_or_arg": (
                            (kw_or_arg is not None) and [kw_or_arg.st] or [None]
                        )[0],
                        "arg": ((arg is not None) and [arg.st] or [None])[0],
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "argument"

    class subscriptlist_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "subscriptlist"
    # YarcParser.g:230:1: subscriptlist :subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs);
    def subscriptlist(
        self,
    ):
        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        list_subs = None
        subs = None
        try:
            try:
                # YarcParser.g:230:15: (subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs))
                # YarcParser.g:230:17: subs+= subscript_ ( COMMA subs+= subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist4275
                )
                subs = self.subscript_()

                self._state.following.pop()
                if list_subs is None:
                    list_subs = []
                list_subs.append(subs.st)

                # YarcParser.g:230:34: ( COMMA subs+= subscript_ )*
                while True:  # loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if LA89_0 == COMMA:
                        alt89 = 1

                    if alt89 == 1:
                        # YarcParser.g:230:35: COMMA subs+= subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist4278
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist4282
                        )
                        subs = self.subscript_()

                        self._state.following.pop()
                        if list_subs is None:
                            list_subs = []
                        list_subs.append(subs.st)

                    else:
                        break  # loop89

                # TEMPLATE REWRITE
                # 230:60: -> subscript_list(subs=$subs)
                retval.st = self.templateLib.getInstanceOf(
                    "subscript_list", attributes={"subs": list_subs}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "subscriptlist"

    class subscript__return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "subscript_"
    # YarcParser.g:231:1: subscript_ : (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st));
    def subscript_(
        self,
    ):
        retval = self.subscript__return()
        retval.start = self.input.LT(1)

        to = None
        step = None
        COLON63 = None
        COLON64 = None
        from_ = None

        try:
            try:
                # YarcParser.g:231:15: (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st))
                alt95 = 2
                LA95_0 = self.input.LA(1)

                if LA95_0 in {
                    BIT_NOT,
                    COMBINE,
                    DISTRIBUTION,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LEN,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NOT,
                    PLUS,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                }:
                    alt95 = 1
                elif LA95_0 == COLON:
                    alt95 = 2
                else:
                    nvae = NoViableAltException("", 95, 0, self.input)

                    raise nvae

                if alt95 == 1:
                    # YarcParser.g:231:17: from_= test ( COLON to= ( test )? step= ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_4305)
                    from_ = self.test()

                    self._state.following.pop()

                    # YarcParser.g:231:28: ( COLON to= ( test )? step= ( sliceop )? )?
                    alt92 = 2
                    LA92_0 = self.input.LA(1)

                    if LA92_0 == COLON:
                        alt92 = 1
                    if alt92 == 1:
                        # YarcParser.g:231:29: COLON to= ( test )? step= ( sliceop )?
                        COLON63 = self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_4308
                        )

                        # YarcParser.g:231:38: ( test )?
                        alt90 = 2
                        LA90_0 = self.input.LA(1)

                        if LA90_0 in {
                            BIT_NOT,
                            COMBINE,
                            DISTRIBUTION,
                            FALSE,
                            FLOAT_NUMBER,
                            ID,
                            INTEGER,
                            LBRACE,
                            LBRACK,
                            LEN,
                            LPAREN,
                            LT,
                            MINUS,
                            NONE,
                            NOT,
                            PLUS,
                            SETTING_ID,
                            STRING,
                            TRUE,
                            UNDERSCORE,
                        }:
                            alt90 = 1
                        if alt90 == 1:
                            # YarcParser.g:231:39: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_4313
                            )
                            to = self.test()

                            self._state.following.pop()

                        # YarcParser.g:231:51: ( sliceop )?
                        alt91 = 2
                        LA91_0 = self.input.LA(1)

                        if LA91_0 == COLON:
                            alt91 = 1
                        if alt91 == 1:
                            # YarcParser.g:231:52: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_4320
                            )
                            step = self.sliceop()

                            self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 231:64: -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={
                            "from": ((from_ is not None) and [from_.st] or [None])[0],
                            "colon": COLON63,
                            "to": to.st,
                            "step": step.st,
                        },
                    )

                elif alt95 == 2:
                    # YarcParser.g:232:17: COLON to= ( test )? step= ( sliceop )?
                    COLON64 = self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_subscript_4366
                    )

                    # YarcParser.g:232:26: ( test )?
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if LA93_0 in {
                        BIT_NOT,
                        COMBINE,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LEN,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NOT,
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt93 = 1
                    if alt93 == 1:
                        # YarcParser.g:232:27: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_4371)
                        to = self.test()

                        self._state.following.pop()

                    # YarcParser.g:232:39: ( sliceop )?
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if LA94_0 == COLON:
                        alt94 = 1
                    if alt94 == 1:
                        # YarcParser.g:232:40: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_4378
                        )
                        step = self.sliceop()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 232:51: -> subscript(colon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={"colon": COLON64, "to": to.st, "step": step.st},
                    )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "subscript_"

    class sliceop_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "sliceop"
    # YarcParser.g:233:1: sliceop : COLON ( test )? -> subscipt_step(step=$test.st);
    def sliceop(
        self,
    ):
        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        test65 = None

        try:
            try:
                # YarcParser.g:233:15: ( COLON ( test )? -> subscipt_step(step=$test.st))
                # YarcParser.g:233:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop4413)

                # YarcParser.g:233:23: ( test )?
                alt96 = 2
                LA96_0 = self.input.LA(1)

                if LA96_0 in {
                    BIT_NOT,
                    COMBINE,
                    DISTRIBUTION,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LEN,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NOT,
                    PLUS,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                }:
                    alt96 = 1
                if alt96 == 1:
                    # YarcParser.g:233:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop4415)
                    test65 = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 233:29: -> subscipt_step(step=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "subscipt_step",
                    attributes={
                        "step": ((test65 is not None) and [test65.st] or [None])[0]
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "sliceop"

    class namelist_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.names = None
            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "namelist"
    # YarcParser.g:235:1: namelist returns [names] :names_+= name ( COMMA names_+= name )* -> test_list(exprs=$names_);
    def namelist(
        self,
    ):
        retval = self.namelist_return()
        retval.start = self.input.LT(1)

        list_names_ = None
        names_ = None
        try:
            try:
                # YarcParser.g:235:25: (names_+= name ( COMMA names_+= name )* -> test_list(exprs=$names_))
                # YarcParser.g:235:27: names_+= name ( COMMA names_+= name )*
                self._state.following.append(self.FOLLOW_name_in_namelist4438)
                names_ = self.name()

                self._state.following.pop()
                if list_names_ is None:
                    list_names_ = []
                list_names_.append(names_.st)

                # YarcParser.g:235:40: ( COMMA names_+= name )*
                while True:  # loop97
                    alt97 = 2
                    LA97_0 = self.input.LA(1)

                    if LA97_0 == COMMA:
                        alt97 = 1

                    if alt97 == 1:
                        # YarcParser.g:235:41: COMMA names_+= name
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_namelist4441)

                        self._state.following.append(self.FOLLOW_name_in_namelist4445)
                        names_ = self.name()

                        self._state.following.pop()
                        if list_names_ is None:
                            list_names_ = []
                        list_names_.append(names_.st)

                    else:
                        break  # loop97

                # action start
                retval.names = list_names_
                # action end

                # TEMPLATE REWRITE
                # 235:81: -> test_list(exprs=$names_)
                retval.st = self.templateLib.getInstanceOf(
                    "test_list", attributes={"exprs": list_names_}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "namelist"

    class testlist_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "testlist"
    # YarcParser.g:236:1: testlist :exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs);
    def testlist(
        self,
    ):
        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:236:10: (exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs))
                # YarcParser.g:236:12: exprs+= test ( COMMA exprs+= test )*
                self._state.following.append(self.FOLLOW_test_in_testlist4467)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:236:24: ( COMMA exprs+= test )*
                while True:  # loop98
                    alt98 = 2
                    LA98_0 = self.input.LA(1)

                    if LA98_0 == COMMA:
                        alt98 = 1

                    if alt98 == 1:
                        # YarcParser.g:236:25: COMMA exprs+= test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist4470)

                        self._state.following.append(self.FOLLOW_test_in_testlist4474)
                        exprs = self.test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop98

                # TEMPLATE REWRITE
                # 236:45: -> test_list(exprs=$exprs)
                retval.st = self.templateLib.getInstanceOf(
                    "test_list", attributes={"exprs": list_exprs}
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "testlist"

    class dict_or_set_maker_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "dict_or_set_maker"
    # YarcParser.g:237:1: dict_or_set_maker :exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs)) ;
    def dict_or_set_maker(
        self,
    ):
        retval = self.dict_or_set_maker_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        list_values = None
        for_ = None
        exprs = None
        values = None
        try:
            try:
                # YarcParser.g:237:18: (exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs)) )
                # YarcParser.g:238:3: exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs))
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker4495)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:238:15: ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs))
                alt103 = 2
                LA103_0 = self.input.LA(1)

                if LA103_0 == COLON:
                    alt103 = 1
                elif LA103_0 in {COMMA, FOR, RBRACE}:
                    alt103 = 2
                else:
                    nvae = NoViableAltException("", 103, 0, self.input)

                    raise nvae

                if alt103 == 1:
                    # YarcParser.g:238:17: COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker4499
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker4503
                    )
                    values = self.test()

                    self._state.following.pop()
                    if list_values is None:
                        list_values = []
                    list_values.append(values.st)

                    # YarcParser.g:238:36: (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* )
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if LA100_0 == FOR:
                        alt100 = 1
                    elif LA100_0 in {COMMA, RBRACE}:
                        alt100 = 2
                    else:
                        nvae = NoViableAltException("", 100, 0, self.input)

                        raise nvae

                    if alt100 == 1:
                        # YarcParser.g:238:37: for_= comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker4508
                        )
                        for_ = self.comp_for()

                        self._state.following.pop()

                        # TEMPLATE REWRITE
                        # 238:51: -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "dict_comp",
                            attributes={
                                "key": list_exprs[0],
                                "value": list_values[0],
                                "for": ((for_ is not None) and [for_.st] or [None])[0],
                            },
                        )

                    elif alt100 == 2:
                        # YarcParser.g:239:38: ( COMMA exprs+= test COLON values+= test )*
                        pass
                        # YarcParser.g:239:38: ( COMMA exprs+= test COLON values+= test )*
                        while True:  # loop99
                            alt99 = 2
                            LA99_0 = self.input.LA(1)

                            if LA99_0 == COMMA:
                                alt99 = 1

                            if alt99 == 1:
                                # YarcParser.g:239:39: COMMA exprs+= test COLON values+= test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker4567,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker4571
                                )
                                exprs = self.test()

                                self._state.following.pop()
                                if list_exprs is None:
                                    list_exprs = []
                                list_exprs.append(exprs.st)

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker4573,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker4577
                                )
                                values = self.test()

                                self._state.following.pop()
                                if list_values is None:
                                    list_values = []
                                list_values.append(values.st)

                            else:
                                break  # loop99

                    # TEMPLATE REWRITE
                    # 239:79: -> key_value_list(keys=$exprsvalues=$values)
                    retval.st = self.templateLib.getInstanceOf(
                        "key_value_list",
                        attributes={"keys": list_exprs, "values": list_values},
                    )

                elif alt103 == 2:
                    # YarcParser.g:240:17: (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* )
                    pass
                    # YarcParser.g:240:17: (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* )
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if LA102_0 == FOR:
                        alt102 = 1
                    elif LA102_0 in {COMMA, RBRACE}:
                        alt102 = 2
                    else:
                        nvae = NoViableAltException("", 102, 0, self.input)

                        raise nvae

                    if alt102 == 1:
                        # YarcParser.g:240:18: for_= comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker4615
                        )
                        for_ = self.comp_for()

                        self._state.following.pop()

                        # TEMPLATE REWRITE
                        # 240:32: -> list_comp(expr=$exprs[0]for=$for_.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "list_comp",
                            attributes={
                                "expr": list_exprs[0],
                                "for": ((for_ is not None) and [for_.st] or [None])[0],
                            },
                        )

                    elif alt102 == 2:
                        # YarcParser.g:241:19: ( COMMA exprs+= test )*
                        pass
                        # YarcParser.g:241:19: ( COMMA exprs+= test )*
                        while True:  # loop101
                            alt101 = 2
                            LA101_0 = self.input.LA(1)

                            if LA101_0 == COMMA:
                                alt101 = 1

                            if alt101 == 1:
                                # YarcParser.g:241:20: COMMA exprs+= test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker4653,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker4657
                                )
                                exprs = self.test()

                                self._state.following.pop()
                                if list_exprs is None:
                                    list_exprs = []
                                list_exprs.append(exprs.st)

                            else:
                                break  # loop101

                    # TEMPLATE REWRITE
                    # 241:42: -> test_list(exprs=$exprs)
                    retval.st = self.templateLib.getInstanceOf(
                        "test_list", attributes={"exprs": list_exprs}
                    )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "dict_or_set_maker"

    class comp_iter_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "comp_iter"
    # YarcParser.g:245:1: comp_iter : comp= ( comp_for | comp_if ) -> {$comp.st};
    def comp_iter(
        self,
    ):
        retval = self.comp_iter_return()
        retval.start = self.input.LT(1)

        comp = None

        try:
            try:
                # YarcParser.g:245:11: (comp= ( comp_for | comp_if ) -> {$comp.st})
                # YarcParser.g:245:13: comp= ( comp_for | comp_if )
                pass
                # YarcParser.g:245:18: ( comp_for | comp_if )
                alt104 = 2
                LA104_0 = self.input.LA(1)

                if LA104_0 == FOR:
                    alt104 = 1
                elif LA104_0 == IF:
                    alt104 = 2
                else:
                    nvae = NoViableAltException("", 104, 0, self.input)

                    raise nvae

                if alt104 == 1:
                    # YarcParser.g:245:19: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter4698)
                    comp = self.comp_for()

                    self._state.following.pop()

                elif alt104 == 2:
                    # YarcParser.g:245:30: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter4702)
                    comp = self.comp_if()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 245:39: -> {$comp.st}
                retval.st = comp.st

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "comp_iter"

    class comp_for_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "comp_for"
    # YarcParser.g:246:1: comp_for : FOR namelist IN or_test ( comp_iter )? -> comp_for(exprs=$namelist.stseq=$or_test.stcomp_iter=$comp_iter.st);
    def comp_for(
        self,
    ):
        retval = self.comp_for_return()
        retval.start = self.input.LT(1)

        namelist66 = None
        or_test67 = None
        comp_iter68 = None

        try:
            try:
                # YarcParser.g:246:11: ( FOR namelist IN or_test ( comp_iter )? -> comp_for(exprs=$namelist.stseq=$or_test.stcomp_iter=$comp_iter.st))
                # YarcParser.g:246:13: FOR namelist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for4715)

                self._state.following.append(self.FOLLOW_namelist_in_comp_for4717)
                namelist66 = self.namelist()

                self._state.following.pop()

                # action start
                self.handler.define(
                    ((namelist66 is not None) and [namelist66.names] or [None])[0]
                )
                # action end

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for4721)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for4723)
                or_test67 = self.or_test()

                self._state.following.pop()

                # YarcParser.g:246:76: ( comp_iter )?
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if LA105_0 in {FOR, IF}:
                    alt105 = 1
                if alt105 == 1:
                    # YarcParser.g:246:76: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for4725)
                    comp_iter68 = self.comp_iter()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 246:87: -> comp_for(exprs=$namelist.stseq=$or_test.stcomp_iter=$comp_iter.st)
                retval.st = self.templateLib.getInstanceOf(
                    "comp_for",
                    attributes={
                        "exprs": (
                            (namelist66 is not None) and [namelist66.st] or [None]
                        )[0],
                        "seq": ((or_test67 is not None) and [or_test67.st] or [None])[
                            0
                        ],
                        "comp_iter": (
                            (comp_iter68 is not None) and [comp_iter68.st] or [None]
                        )[0],
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "comp_for"

    class comp_if_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "comp_if"
    # YarcParser.g:247:1: comp_if : IF test_nocond ( comp_iter )? -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st);
    def comp_if(
        self,
    ):
        retval = self.comp_if_return()
        retval.start = self.input.LT(1)

        test_nocond69 = None
        comp_iter70 = None

        try:
            try:
                # YarcParser.g:247:11: ( IF test_nocond ( comp_iter )? -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st))
                # YarcParser.g:247:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if4754)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if4756)
                test_nocond69 = self.test_nocond()

                self._state.following.pop()

                # YarcParser.g:247:28: ( comp_iter )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if LA106_0 in {FOR, IF}:
                    alt106 = 1
                if alt106 == 1:
                    # YarcParser.g:247:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if4758)
                    comp_iter70 = self.comp_iter()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 247:39: -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st)
                retval.st = self.templateLib.getInstanceOf(
                    "comp_if",
                    attributes={
                        "cond": (
                            (test_nocond69 is not None) and [test_nocond69.st] or [None]
                        )[0],
                        "comp_iter": (
                            (comp_iter70 is not None) and [comp_iter70.st] or [None]
                        )[0],
                    },
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "comp_if"

    FOLLOW_NEWLINE_in_scenario59 = frozenset([74, 99])
    FOLLOW_declaration_in_scenario62 = frozenset([74, 102, 108, 110])
    FOLLOW_code_snippet_in_scenario67 = frozenset([74, 102, 108, 110])
    FOLLOW_NEWLINE_in_scenario71 = frozenset([74, 102, 108, 110])
    FOLLOW_settings_in_scenario75 = frozenset([110])
    FOLLOW_stage_in_scenario78 = frozenset([1, 108, 124])
    FOLLOW_writers_in_scenario80 = frozenset([1, 108])
    FOLLOW_code_snippet_in_scenario86 = frozenset([1, 108])
    FOLLOW_SNIPPET_in_code_snippet209 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration232 = frozenset([43])
    FOLLOW_ID_in_declaration234 = frozenset([14, 74])
    FOLLOW_COLON_in_declaration237 = frozenset([43, 120])
    FOLLOW_name_in_declaration239 = frozenset([74])
    FOLLOW_NEWLINE_in_declaration243 = frozenset([1])
    FOLLOW_SETTINGS_in_settings266 = frozenset([14])
    FOLLOW_COLON_in_settings268 = frozenset([74])
    FOLLOW_NEWLINE_in_settings270 = frozenset([49])
    FOLLOW_INDENT_in_settings272 = frozenset([43, 108])
    FOLLOW_setting_in_settings277 = frozenset([19, 43, 108])
    FOLLOW_code_snippet_in_settings281 = frozenset([19, 43, 108])
    FOLLOW_DEDENT_in_settings285 = frozenset([1])
    FOLLOW_ID_in_setting313 = frozenset([5])
    FOLLOW_ASSIGN_in_setting315 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_setting317 = frozenset([74])
    FOLLOW_NEWLINE_in_setting319 = frozenset([1])
    FOLLOW_WRITERS_in_writers441 = frozenset([14])
    FOLLOW_COLON_in_writers443 = frozenset([74])
    FOLLOW_NEWLINE_in_writers445 = frozenset([49])
    FOLLOW_INDENT_in_writers447 = frozenset([43, 108, 120])
    FOLLOW_expr_stmt_in_writers452 = frozenset([19, 43, 108, 120])
    FOLLOW_code_snippet_in_writers456 = frozenset([19, 43, 108, 120])
    FOLLOW_writer_in_writers460 = frozenset([19, 43, 108, 120])
    FOLLOW_DEDENT_in_writers464 = frozenset([1])
    FOLLOW_ID_in_writer494 = frozenset([14])
    FOLLOW_COLON_in_writer496 = frozenset([74])
    FOLLOW_NEWLINE_in_writer498 = frozenset([49])
    FOLLOW_INDENT_in_writer500 = frozenset([43])
    FOLLOW_writer_param_in_writer503 = frozenset([19, 43])
    FOLLOW_DEDENT_in_writer509 = frozenset([1])
    FOLLOW_ID_in_writer_param538 = frozenset([5])
    FOLLOW_ASSIGN_in_writer_param540 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_writer_param542 = frozenset([74])
    FOLLOW_NEWLINE_in_writer_param544 = frozenset([1])
    FOLLOW_STAGE_in_stage560 = frozenset([14])
    FOLLOW_COLON_in_stage562 = frozenset([74])
    FOLLOW_NEWLINE_in_stage564 = frozenset([49])
    FOLLOW_INDENT_in_stage566 = frozenset([18, 24, 28, 38, 39, 43, 50, 81, 108, 120])
    FOLLOW_stmts_in_stage568 = frozenset([19])
    FOLLOW_DEDENT_in_stage570 = frozenset([1])
    FOLLOW_open_stmt_in_stmts593 = frozenset([18, 24, 28, 38, 39, 43, 50, 108, 120])
    FOLLOW_aug_expr_stmt_in_stmts600 = frozenset(
        [1, 18, 24, 28, 38, 39, 43, 50, 108, 120]
    )
    FOLLOW_code_snippet_in_stmts604 = frozenset(
        [1, 18, 24, 28, 38, 39, 43, 50, 108, 120]
    )
    FOLLOW_edit_stmt_in_stmts608 = frozenset([1, 18, 24, 28, 38, 39, 43, 50, 108, 120])
    FOLLOW_behavior_stmt_in_stmts612 = frozenset(
        [1, 18, 24, 28, 38, 39, 43, 50, 108, 120]
    )
    FOLLOW_OPEN_in_open_stmt635 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_open_stmt637 = frozenset([74])
    FOLLOW_NEWLINE_in_open_stmt639 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt655 = frozenset([43, 116, 120])
    FOLLOW_TIMELINE_in_edit_stmt658 = frozenset([14])
    FOLLOW_COLON_in_edit_stmt660 = frozenset([74])
    FOLLOW_NEWLINE_in_edit_stmt662 = frozenset([49])
    FOLLOW_INDENT_in_edit_stmt664 = frozenset([43, 120])
    FOLLOW_name_in_edit_stmt669 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_edit_stmt673 = frozenset([74])
    FOLLOW_NEWLINE_in_edit_stmt675 = frozenset([19, 43, 120])
    FOLLOW_DEDENT_in_edit_stmt679 = frozenset([1])
    FOLLOW_name_in_edit_stmt717 = frozenset([14])
    FOLLOW_edit_block_in_edit_stmt719 = frozenset([1])
    FOLLOW_CREATE_in_create_expr768 = frozenset(
        [
            11,
            13,
            15,
            21,
            31,
            33,
            37,
            43,
            51,
            54,
            55,
            56,
            58,
            62,
            64,
            67,
            69,
            75,
            77,
            86,
            103,
            104,
            112,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_create_expr772 = frozenset([13, 37, 58, 67, 104, 112])
    FOLLOW_SHAPE_in_create_expr784 = frozenset([14, 74])
    FOLLOW_LIGHT_in_create_expr788 = frozenset([14, 74])
    FOLLOW_edit_block_in_create_expr794 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr799 = frozenset([1])
    FOLLOW_STEREO_in_create_expr935 = frozenset([13])
    FOLLOW_CAMERA_in_create_expr937 = frozenset([14, 74])
    FOLLOW_CAMERA_in_create_expr943 = frozenset([14, 74])
    FOLLOW_edit_block_in_create_expr949 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr954 = frozenset([1])
    FOLLOW_FROM_in_create_expr1089 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_create_expr1093 = frozenset([14, 74])
    FOLLOW_edit_block_in_create_expr1098 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr1103 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr1234 = frozenset([14, 74])
    FOLLOW_simple_block_in_create_expr1239 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr1243 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr1305 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            37,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_instantiate_expr1310 = frozenset([37])
    FOLLOW_FROM_in_instantiate_expr1314 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_instantiate_expr1318 = frozenset([14, 74])
    FOLLOW_edit_block_in_instantiate_expr1321 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr1326 = frozenset([1])
    FOLLOW_GROUP_in_group_expr1465 = frozenset([55])
    FOLLOW_LBRACK_in_group_expr1467 = frozenset([43, 120])
    FOLLOW_name_in_group_expr1471 = frozenset([16, 91])
    FOLLOW_COMMA_in_group_expr1474 = frozenset([43, 120])
    FOLLOW_name_in_group_expr1478 = frozenset([16, 91])
    FOLLOW_RBRACK_in_group_expr1482 = frozenset([14, 74])
    FOLLOW_edit_block_in_group_expr1485 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr1490 = frozenset([1])
    FOLLOW_GET_in_get_expr1604 = frozenset(
        [
            11,
            13,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            58,
            62,
            64,
            67,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_CAMERA_in_get_expr1610 = frozenset([6])
    FOLLOW_LIGHT_in_get_expr1614 = frozenset([6])
    FOLLOW_MATERIAL_in_get_expr1618 = frozenset([6])
    FOLLOW_name_in_get_expr1622 = frozenset([6])
    FOLLOW_AT_in_get_expr1625 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_get_expr1631 = frozenset([14, 74])
    FOLLOW_simple_block_in_get_expr1634 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr1638 = frozenset([1])
    FOLLOW_COLON_in_edit_block1732 = frozenset([74])
    FOLLOW_NEWLINE_in_edit_block1734 = frozenset([49])
    FOLLOW_INDENT_in_edit_block1736 = frozenset(
        [28, 43, 61, 68, 71, 84, 85, 93, 94, 97, 98, 100, 106, 118, 120, 122, 123]
    )
    FOLLOW_attr_in_edit_block1742 = frozenset(
        [19, 28, 43, 61, 68, 71, 84, 85, 93, 94, 97, 98, 100, 106, 118, 120, 122, 123]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block1746 = frozenset(
        [19, 28, 43, 61, 68, 71, 84, 85, 93, 94, 97, 98, 100, 106, 118, 120, 122, 123]
    )
    FOLLOW_DEDENT_in_edit_block1754 = frozenset([1])
    FOLLOW_COLON_in_simple_block1773 = frozenset([74])
    FOLLOW_NEWLINE_in_simple_block1775 = frozenset([49])
    FOLLOW_INDENT_in_simple_block1777 = frozenset([43, 120])
    FOLLOW_simple_attr_in_simple_block1780 = frozenset([19, 43, 120])
    FOLLOW_DEDENT_in_simple_block1786 = frozenset([1])
    FOLLOW_core_attr_in_attr1801 = frozenset([1])
    FOLLOW_simple_attr_in_attr1805 = frozenset([1])
    FOLLOW_compound_attr_in_attr1809 = frozenset([1])
    FOLLOW_name_in_simple_attr1839 = frozenset(
        [
            11,
            14,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_COLON_in_simple_attr1842 = frozenset([43, 120])
    FOLLOW_name_in_simple_attr1846 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_simple_attr1852 = frozenset([74])
    FOLLOW_NEWLINE_in_simple_attr1854 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr1901 = frozenset([80])
    FOLLOW_ON_in_compound_attr1903 = frozenset([43, 120])
    FOLLOW_name_in_compound_attr1907 = frozenset([14, 74])
    FOLLOW_simple_block_in_compound_attr1912 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr1916 = frozenset([1])
    FOLLOW_ROT_AROUND_in_compound_attr2000 = frozenset([43, 120])
    FOLLOW_name_in_compound_attr2004 = frozenset([14, 74])
    FOLLOW_simple_block_in_compound_attr2009 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr2013 = frozenset([1])
    FOLLOW_PHYSICS_in_compound_attr2070 = frozenset([14, 74])
    FOLLOW_simple_block_in_compound_attr2075 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr2079 = frozenset([1])
    FOLLOW_MOVE_TO_CAM_in_compound_attr2132 = frozenset([43, 120])
    FOLLOW_name_in_compound_attr2136 = frozenset([14, 74])
    FOLLOW_simple_block_in_compound_attr2141 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr2145 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr2223 = frozenset([8, 117])
    FOLLOW_AXIS_in_core_attr2227 = frozenset([117])
    FOLLOW_TO_in_core_attr2230 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2234 = frozenset([74])
    FOLLOW_ROTATE_in_core_attr2258 = frozenset(
        [
            8,
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_AXIS_in_core_attr2262 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2267 = frozenset([74])
    FOLLOW_SCALE_in_core_attr2291 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2295 = frozenset([74])
    FOLLOW_LOOK_AT_in_core_attr2314 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2318 = frozenset([74])
    FOLLOW_UP_AXIS_in_core_attr2337 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2341 = frozenset([74])
    FOLLOW_SIZE_in_core_attr2360 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2364 = frozenset([74])
    FOLLOW_PIVOT_in_core_attr2383 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2387 = frozenset([74])
    FOLLOW_SEMANTICS_in_core_attr2406 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2410 = frozenset([74])
    FOLLOW_VISIBLE_in_core_attr2429 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2433 = frozenset([74])
    FOLLOW_MATERIAL__in_core_attr2452 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_core_attr2456 = frozenset([74])
    FOLLOW_NEWLINE_in_core_attr2473 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt2496 = frozenset([14])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt2498 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block2524 = frozenset([74])
    FOLLOW_NEWLINE_in_inner_behavior_block2526 = frozenset([49])
    FOLLOW_INDENT_in_inner_behavior_block2528 = frozenset(
        [43, 61, 68, 71, 84, 85, 93, 94, 97, 98, 100, 106, 118, 120, 122, 123]
    )
    FOLLOW_attr_in_inner_behavior_block2532 = frozenset(
        [19, 43, 61, 68, 71, 84, 85, 93, 94, 97, 98, 100, 106, 118, 120, 122, 123]
    )
    FOLLOW_DEDENT_in_inner_behavior_block2535 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt2555 = frozenset([14])
    FOLLOW_behavior_block_in_behavior_stmt2557 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr2579 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            36,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            115,
            119,
            120,
        ]
    )
    FOLLOW_test_in_behavior_expr2583 = frozenset([36, 115])
    FOLLOW_FRAMES_in_behavior_expr2589 = frozenset([1])
    FOLLOW_TIME_in_behavior_expr2593 = frozenset([1])
    FOLLOW_COLON_in_behavior_block2615 = frozenset([74])
    FOLLOW_NEWLINE_in_behavior_block2617 = frozenset([49])
    FOLLOW_INDENT_in_behavior_block2619 = frozenset([18, 24, 38, 39, 43, 50, 108, 120])
    FOLLOW_aug_expr_stmt_in_behavior_block2624 = frozenset(
        [18, 19, 24, 38, 39, 43, 50, 108, 120]
    )
    FOLLOW_code_snippet_in_behavior_block2628 = frozenset(
        [18, 19, 24, 38, 39, 43, 50, 108, 120]
    )
    FOLLOW_edit_stmt_in_behavior_block2632 = frozenset(
        [18, 19, 24, 38, 39, 43, 50, 108, 120]
    )
    FOLLOW_DEDENT_in_behavior_block2636 = frozenset([1])
    FOLLOW_namelist_in_expr_stmt2657 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_expr_stmt2664 = frozenset(
        [
            11,
            15,
            21,
            31,
            32,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_ASSIGN_in_expr_stmt2668 = frozenset(
        [
            11,
            15,
            21,
            31,
            32,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_testlist_in_expr_stmt2674 = frozenset([74])
    FOLLOW_fetch_expr_in_expr_stmt2678 = frozenset([74])
    FOLLOW_NEWLINE_in_expr_stmt2681 = frozenset([1])
    FOLLOW_namelist_in_aug_expr_stmt2719 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_aug_expr_stmt2733 = frozenset(
        [
            11,
            15,
            21,
            31,
            32,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt2738 = frozenset([74])
    FOLLOW_fetch_expr_in_aug_expr_stmt2742 = frozenset([74])
    FOLLOW_NEWLINE_in_aug_expr_stmt2745 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt2777 = frozenset(
        [
            11,
            15,
            18,
            21,
            31,
            32,
            33,
            38,
            39,
            43,
            50,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt2792 = frozenset([74])
    FOLLOW_fetch_expr_in_aug_expr_stmt2796 = frozenset([74])
    FOLLOW_NEWLINE_in_aug_expr_stmt2799 = frozenset([1])
    FOLLOW_model_expr_in_aug_expr_stmt2834 = frozenset([1])
    FOLLOW_model_expr_in_aug_expr_stmt2868 = frozenset([1])
    FOLLOW_create_expr_in_model_expr2885 = frozenset([1])
    FOLLOW_instantiate_expr_in_model_expr2890 = frozenset([1])
    FOLLOW_get_expr_in_model_expr2895 = frozenset([1])
    FOLLOW_group_expr_in_model_expr2900 = frozenset([1])
    FOLLOW_FETCH_in_fetch_expr2914 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_fetch_expr2918 = frozenset([37])
    FOLLOW_FROM_in_fetch_expr2920 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_fetch_expr2924 = frozenset([1, 59, 66, 92])
    FOLLOW_MATCH_in_fetch_expr2927 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_fetch_expr2931 = frozenset([1, 59, 92])
    FOLLOW_LIMIT_in_fetch_expr2936 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_fetch_expr2940 = frozenset([1, 92])
    FOLLOW_RECURSIVE_in_fetch_expr2944 = frozenset([1])
    FOLLOW_or_test_in_test2995 = frozenset([1, 47])
    FOLLOW_IF_in_test2998 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_or_test_in_test3002 = frozenset([26])
    FOLLOW_ELSE_in_test3004 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_test3008 = frozenset([1])
    FOLLOW_or_test_in_test_nocond3050 = frozenset([1])
    FOLLOW_and_test_in_or_test3072 = frozenset([1, 82])
    FOLLOW_OR_in_or_test3075 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_and_test_in_or_test3079 = frozenset([1, 82])
    FOLLOW_not_test_in_and_test3102 = frozenset([1, 4])
    FOLLOW_AND_in_and_test3105 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_not_test_in_and_test3109 = frozenset([1, 4])
    FOLLOW_NOT_in_not_test3130 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_not_test_in_not_test3134 = frozenset([1])
    FOLLOW_comparison_in_not_test3160 = frozenset([1])
    FOLLOW_expr_in_comparison3174 = frozenset([1, 27, 40, 41, 48, 53, 64, 65, 77, 78])
    FOLLOW_comp_op_in_comparison3179 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_expr_in_comparison3183 = frozenset([1, 27, 40, 41, 48, 53, 64, 65, 77, 78])
    FOLLOW_LT_in_comp_op3213 = frozenset([1])
    FOLLOW_GT_in_comp_op3217 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op3221 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op3225 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op3229 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op3233 = frozenset([1])
    FOLLOW_IN_in_comp_op3237 = frozenset([1])
    FOLLOW_NOT_in_comp_op3241 = frozenset([48])
    FOLLOW_IN_in_comp_op3243 = frozenset([1])
    FOLLOW_IS_in_comp_op3247 = frozenset([1])
    FOLLOW_IS_in_comp_op3251 = frozenset([77])
    FOLLOW_NOT_in_comp_op3253 = frozenset([1])
    FOLLOW_xor_expr_in_expr3274 = frozenset([1, 12])
    FOLLOW_BIT_OR_in_expr3277 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_xor_expr_in_expr3281 = frozenset([1, 12])
    FOLLOW_and_expr_in_xor_expr3304 = frozenset([1, 125])
    FOLLOW_XOR_in_xor_expr3307 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_and_expr_in_xor_expr3311 = frozenset([1, 125])
    FOLLOW_shift_expr_in_and_expr3334 = frozenset([1, 10])
    FOLLOW_BIT_AND_in_and_expr3337 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_shift_expr_in_and_expr3341 = frozenset([1, 10])
    FOLLOW_arith_expr_in_shift_expr3362 = frozenset([1, 63, 96])
    FOLLOW_LSHIFT_in_shift_expr3368 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_RSHIFT_in_shift_expr3372 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_arith_expr_in_shift_expr3377 = frozenset([1, 63, 96])
    FOLLOW_term_in_arith_expr3403 = frozenset([1, 69, 86])
    FOLLOW_PLUS_in_arith_expr3409 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_MINUS_in_arith_expr3413 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_term_in_arith_expr3418 = frozenset([1, 69, 86])
    FOLLOW_factor_in_term3450 = frozenset([1, 22, 44, 70, 72])
    FOLLOW_MUL_in_term3456 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_DIV_in_term3460 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_MOD_in_term3464 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_IDIV_in_term3468 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_factor_in_term3473 = frozenset([1, 22, 44, 70, 72])
    FOLLOW_PLUS_in_factor3504 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_MINUS_in_factor3508 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_BIT_NOT_in_factor3512 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_factor_in_factor3517 = frozenset([1])
    FOLLOW_power_in_factor3547 = frozenset([1])
    FOLLOW_atom_expr_in_power3564 = frozenset([1, 88])
    FOLLOW_POWER_in_power3567 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_factor_in_power3569 = frozenset([1])
    FOLLOW_atom_in_atom_expr3594 = frozenset([1, 23, 55])
    FOLLOW_trailer_in_atom_expr3599 = frozenset([1, 23, 55])
    FOLLOW_LPAREN_in_atom3624 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_atom3628 = frozenset([95])
    FOLLOW_RPAREN_in_atom3630 = frozenset([1])
    FOLLOW_LBRACK_in_atom3645 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            91,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_testlist_comp_in_atom3647 = frozenset([91])
    FOLLOW_RBRACK_in_atom3650 = frozenset([1])
    FOLLOW_LT_in_atom3665 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            40,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_vector_comp_in_atom3667 = frozenset([40])
    FOLLOW_GT_in_atom3670 = frozenset([1])
    FOLLOW_LBRACE_in_atom3685 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            90,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_dict_or_set_maker_in_atom3687 = frozenset([90])
    FOLLOW_RBRACE_in_atom3690 = frozenset([1])
    FOLLOW_LEN_in_atom3705 = frozenset([62])
    FOLLOW_LPAREN_in_atom3707 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_atom3711 = frozenset([95])
    FOLLOW_RPAREN_in_atom3713 = frozenset([1])
    FOLLOW_name_in_atom3728 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom3740 = frozenset([1])
    FOLLOW_distribution_in_atom3757 = frozenset([1])
    FOLLOW_INTEGER_in_atom3767 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom3777 = frozenset([1])
    FOLLOW_STRING_in_atom3787 = frozenset([1])
    FOLLOW_NONE_in_atom3797 = frozenset([1])
    FOLLOW_TRUE_in_atom3809 = frozenset([1])
    FOLLOW_FALSE_in_atom3821 = frozenset([1])
    FOLLOW_ID_in_name3841 = frozenset([1])
    FOLLOW_UNDERSCORE_in_name3851 = frozenset([1])
    FOLLOW_DISTRIBUTION_in_distribution3864 = frozenset([62])
    FOLLOW_LPAREN_in_distribution3866 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_arglist_in_distribution3870 = frozenset([95])
    FOLLOW_RPAREN_in_distribution3872 = frozenset([1])
    FOLLOW_COMBINE_in_distribution3905 = frozenset([62])
    FOLLOW_LPAREN_in_distribution3907 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_arglist_in_distribution3911 = frozenset([95])
    FOLLOW_RPAREN_in_distribution3913 = frozenset([1])
    FOLLOW_test_in_testlist_comp3934 = frozenset([1, 16, 34, 89])
    FOLLOW_comp_for_in_testlist_comp3938 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp3986 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_testlist_comp3990 = frozenset([1, 16])
    FOLLOW_RANGE_in_testlist_comp4034 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_testlist_comp4038 = frozenset([1, 111])
    FOLLOW_STEP_in_testlist_comp4041 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_testlist_comp4045 = frozenset([1])
    FOLLOW_expr_in_vector_comp4109 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp4111 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_expr_in_vector_comp4115 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp4117 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 69, 75, 86, 103, 113, 119, 120]
    )
    FOLLOW_expr_in_vector_comp4121 = frozenset([1])
    FOLLOW_LBRACK_in_trailer4153 = frozenset(
        [
            11,
            14,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_subscriptlist_in_trailer4155 = frozenset([91])
    FOLLOW_RBRACK_in_trailer4157 = frozenset([1])
    FOLLOW_DOT_in_trailer4185 = frozenset([43, 120])
    FOLLOW_name_in_trailer4187 = frozenset([1])
    FOLLOW_argument_in_arglist4211 = frozenset([1, 16])
    FOLLOW_COMMA_in_arglist4214 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_argument_in_arglist4218 = frozenset([1, 16])
    FOLLOW_test_in_argument4243 = frozenset([1, 5])
    FOLLOW_ASSIGN_in_argument4246 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_argument4250 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist4275 = frozenset([1, 16])
    FOLLOW_COMMA_in_subscriptlist4278 = frozenset(
        [
            11,
            14,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_subscript__in_subscriptlist4282 = frozenset([1, 16])
    FOLLOW_test_in_subscript_4305 = frozenset([1, 14])
    FOLLOW_COLON_in_subscript_4308 = frozenset(
        [
            1,
            11,
            14,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_subscript_4313 = frozenset([1, 14])
    FOLLOW_sliceop_in_subscript_4320 = frozenset([1])
    FOLLOW_COLON_in_subscript_4366 = frozenset(
        [
            1,
            11,
            14,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_subscript_4371 = frozenset([1, 14])
    FOLLOW_sliceop_in_subscript_4378 = frozenset([1])
    FOLLOW_COLON_in_sliceop4413 = frozenset(
        [
            1,
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_sliceop4415 = frozenset([1])
    FOLLOW_name_in_namelist4438 = frozenset([1, 16])
    FOLLOW_COMMA_in_namelist4441 = frozenset([43, 120])
    FOLLOW_name_in_namelist4445 = frozenset([1, 16])
    FOLLOW_test_in_testlist4467 = frozenset([1, 16])
    FOLLOW_COMMA_in_testlist4470 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_testlist4474 = frozenset([1, 16])
    FOLLOW_test_in_dict_or_set_maker4495 = frozenset([1, 14, 16, 34])
    FOLLOW_COLON_in_dict_or_set_maker4499 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker4503 = frozenset([1, 16, 34])
    FOLLOW_comp_for_in_dict_or_set_maker4508 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker4567 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker4571 = frozenset([14])
    FOLLOW_COLON_in_dict_or_set_maker4573 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker4577 = frozenset([1, 16])
    FOLLOW_comp_for_in_dict_or_set_maker4615 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker4653 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker4657 = frozenset([1, 16])
    FOLLOW_comp_for_in_comp_iter4698 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter4702 = frozenset([1])
    FOLLOW_FOR_in_comp_for4715 = frozenset([43, 120])
    FOLLOW_namelist_in_comp_for4717 = frozenset([48])
    FOLLOW_IN_in_comp_for4721 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_or_test_in_comp_for4723 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_for4725 = frozenset([1])
    FOLLOW_IF_in_comp_if4754 = frozenset(
        [
            11,
            15,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            62,
            64,
            69,
            75,
            77,
            86,
            103,
            113,
            119,
            120,
        ]
    )
    FOLLOW_test_nocond_in_comp_if4756 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_if4758 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
