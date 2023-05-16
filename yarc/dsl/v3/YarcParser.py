# $ANTLR 3.5.3 YarcParser.g 2023-05-16 20:35:46

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

from yarc.dsl.v3.handler.handler import Attribute, Parameter
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
MINUS = 68
MOD = 69
MOVE_TO_CAM = 70
MUL = 71
NESTED_CODE = 72
NEWLINE = 73
NONE = 74
NON_ZERO_DIGIT = 75
NOT = 76
NOT_EQ = 77
OCT_DIGIT = 78
ON = 79
OPEN = 80
OR = 81
ORDER = 82
PHYSICS = 83
PLUS = 84
POINT_FLOAT = 85
POWER = 86
RANGE = 87
RBRACE = 88
RBRACK = 89
RECURSIVE = 90
ROTATE = 91
ROT_AROUND = 92
RPAREN = 93
RSHIFT = 94
SCALE = 95
SCATTER = 96
SCENARIO = 97
SEMANTICS = 98
SEMI = 99
SETTINGS = 100
SETTING_ID = 101
SHAPE = 102
SHORT_STRING = 103
SIZE = 104
SKIP_ = 105
SNIPPET = 106
SPACES = 107
STAGE = 108
STEP = 109
STEREO = 110
STRING = 111
STRING_ESCAPE_SEQ = 112
TIME = 113
TIMELINE = 114
TO = 115
TRANSLATE = 116
TRUE = 117
UNDERSCORE = 118
UNKNOWN = 119
UP_AXIS = 120
VISIBLE = 121
WRITERS = 122
XOR = 123

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
    68: "MINUS",
    69: "MOD",
    70: "MOVE_TO_CAM",
    71: "MUL",
    72: "NESTED_CODE",
    73: "NEWLINE",
    74: "NONE",
    75: "NON_ZERO_DIGIT",
    76: "NOT",
    77: "NOT_EQ",
    78: "OCT_DIGIT",
    79: "ON",
    80: "OPEN",
    81: "OR",
    82: "ORDER",
    83: "PHYSICS",
    84: "PLUS",
    85: "POINT_FLOAT",
    86: "POWER",
    87: "RANGE",
    88: "RBRACE",
    89: "RBRACK",
    90: "RECURSIVE",
    91: "ROTATE",
    92: "ROT_AROUND",
    93: "RPAREN",
    94: "RSHIFT",
    95: "SCALE",
    96: "SCATTER",
    97: "SCENARIO",
    98: "SEMANTICS",
    99: "SEMI",
    100: "SETTINGS",
    101: "SETTING_ID",
    102: "SHAPE",
    103: "SHORT_STRING",
    104: "SIZE",
    105: "SKIP_",
    106: "SNIPPET",
    107: "SPACES",
    108: "STAGE",
    109: "STEP",
    110: "STEREO",
    111: "STRING",
    112: "STRING_ESCAPE_SEQ",
    113: "TIME",
    114: "TIMELINE",
    115: "TO",
    116: "TRANSLATE",
    117: "TRUE",
    118: "UNDERSCORE",
    119: "UNKNOWN",
    120: "UP_AXIS",
    121: "VISIBLE",
    122: "WRITERS",
    123: "XOR",
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
    # YarcParser.g:20:1: scenario : (before+= code_snippet | NEWLINE )* declaration (before+= code_snippet | NEWLINE )* ( settings )? stage ( writers )? after+= ( code_snippet )* -> scenario(name=$declaration.scenario_namebefore_snippets=$beforesettings=$settings.ststage=$stage.stwriters=$writers.stafter_snippets=$after);
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
                # YarcParser.g:20:10: ( (before+= code_snippet | NEWLINE )* declaration (before+= code_snippet | NEWLINE )* ( settings )? stage ( writers )? after+= ( code_snippet )* -> scenario(name=$declaration.scenario_namebefore_snippets=$beforesettings=$settings.ststage=$stage.stwriters=$writers.stafter_snippets=$after))
                # YarcParser.g:20:12: (before+= code_snippet | NEWLINE )* declaration (before+= code_snippet | NEWLINE )* ( settings )? stage ( writers )? after+= ( code_snippet )*
                pass
                # YarcParser.g:20:12: (before+= code_snippet | NEWLINE )*
                while True:  # loop1
                    alt1 = 3
                    LA1_0 = self.input.LA(1)

                    if LA1_0 == SNIPPET:
                        alt1 = 1
                    elif LA1_0 == NEWLINE:
                        alt1 = 2

                    if alt1 == 1:
                        # YarcParser.g:20:13: before+= code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_scenario62
                        )
                        before = self.code_snippet()

                        self._state.following.pop()
                        if list_before is None:
                            list_before = []
                        list_before.append(before.st)

                    elif alt1 == 2:
                        # YarcParser.g:20:36: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario66
                        )

                    else:
                        break  # loop1

                self._state.following.append(self.FOLLOW_declaration_in_scenario70)
                declaration1 = self.declaration()

                self._state.following.pop()

                # YarcParser.g:20:58: (before+= code_snippet | NEWLINE )*
                while True:  # loop2
                    alt2 = 3
                    LA2_0 = self.input.LA(1)

                    if LA2_0 == SNIPPET:
                        alt2 = 1
                    elif LA2_0 == NEWLINE:
                        alt2 = 2

                    if alt2 == 1:
                        # YarcParser.g:20:59: before+= code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_scenario75
                        )
                        before = self.code_snippet()

                        self._state.following.pop()
                        if list_before is None:
                            list_before = []
                        list_before.append(before.st)

                    elif alt2 == 2:
                        # YarcParser.g:20:82: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario79
                        )

                    else:
                        break  # loop2

                # YarcParser.g:20:92: ( settings )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if LA3_0 == SETTINGS:
                    alt3 = 1
                if alt3 == 1:
                    # YarcParser.g:20:92: settings
                    self._state.following.append(self.FOLLOW_settings_in_scenario83)
                    settings2 = self.settings()

                    self._state.following.pop()

                self._state.following.append(self.FOLLOW_stage_in_scenario86)
                stage3 = self.stage()

                self._state.following.pop()

                # YarcParser.g:20:108: ( writers )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == WRITERS:
                    alt4 = 1
                if alt4 == 1:
                    # YarcParser.g:20:108: writers
                    self._state.following.append(self.FOLLOW_writers_in_scenario88)
                    writers4 = self.writers()

                    self._state.following.pop()

                # YarcParser.g:20:124: ( code_snippet )*
                while True:  # loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if LA5_0 == SNIPPET:
                        alt5 = 1

                    if alt5 == 1:
                        # YarcParser.g:20:125: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_scenario94
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
                    self.input, SNIPPET, self.FOLLOW_SNIPPET_in_code_snippet217
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
                self.match(self.input, SCENARIO, self.FOLLOW_SCENARIO_in_declaration240)

                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_declaration242)

                # YarcParser.g:30:51: ( COLON name )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if LA6_0 == COLON:
                    alt6 = 1
                if alt6 == 1:
                    # YarcParser.g:30:52: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration245)

                    self._state.following.append(self.FOLLOW_name_in_declaration247)
                    name7 = self.name()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_declaration251)

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
                self.match(self.input, SETTINGS, self.FOLLOW_SETTINGS_in_settings274)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_settings276)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_settings278)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_settings280)

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
                        self._state.following.append(self.FOLLOW_setting_in_settings285)
                        stmts_ = self.setting()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt7 == 2:
                        # YarcParser.g:34:64: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_settings289
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

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_settings293)

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
    # YarcParser.g:35:1: stage : STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st};
    def stage(
        self,
    ):
        retval = self.stage_return()
        retval.start = self.input.LT(1)

        stmts8 = None

        try:
            try:
                # YarcParser.g:35:13: ( STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st})
                # YarcParser.g:35:15: STAGE COLON NEWLINE INDENT stmts DEDENT
                self.match(self.input, STAGE, self.FOLLOW_STAGE_in_stage320)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_stage322)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stage324)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stage326)

                self._state.following.append(self.FOLLOW_stmts_in_stage328)
                stmts8 = self.stmts()

                self._state.following.pop()

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stage330)

                # TEMPLATE REWRITE
                # 35:55: -> {$stmts.st}
                retval.st = ((stmts8 is not None) and [stmts8.st] or [None])[0]

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stage"

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
    # YarcParser.g:36:1: writers : WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | code_snippet | writer )+ DEDENT -> writers(stmts=$stmts_);
    def writers(
        self,
    ):
        retval = self.writers_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:36:13: ( WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | code_snippet | writer )+ DEDENT -> writers(stmts=$stmts_))
                # YarcParser.g:36:15: WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | code_snippet | writer )+ DEDENT
                self.match(self.input, WRITERS, self.FOLLOW_WRITERS_in_writers345)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writers347)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writers349)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writers351)

                # YarcParser.g:36:52: ( expr_stmt | code_snippet | writer )+
                cnt8 = 0
                while True:  # loop8
                    alt8 = 4
                    LA8 = self.input.LA(1)
                    if LA8 in {
                        BIT_NOT,
                        COMBINE,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
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
                        alt8 = 1
                    elif LA8 in {ID}:
                        LA8_3 = self.input.LA(2)

                        if LA8_3 == COLON:
                            alt8 = 3
                        elif LA8_3 in {
                            AND,
                            ASSIGN,
                            AUG_ASSIGN,
                            BIT_AND,
                            BIT_OR,
                            COMMA,
                            DIV,
                            DOT,
                            EQUALS,
                            GT,
                            GT_EQ,
                            IDIV,
                            IF,
                            IN,
                            IS,
                            LBRACK,
                            LSHIFT,
                            LT,
                            LT_EQ,
                            MINUS,
                            MOD,
                            MUL,
                            NOT,
                            NOT_EQ,
                            OR,
                            PLUS,
                            POWER,
                            RSHIFT,
                            XOR,
                        }:
                            alt8 = 1

                    elif LA8 in {SNIPPET}:
                        alt8 = 2

                    if alt8 == 1:
                        # YarcParser.g:36:53: expr_stmt
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers356
                        )
                        stmts_ = self.expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt8 == 2:
                        # YarcParser.g:36:65: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_writers360
                        )
                        stmts_ = self.code_snippet()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt8 == 3:
                        # YarcParser.g:36:80: writer
                        self._state.following.append(self.FOLLOW_writer_in_writers364)
                        stmts_ = self.writer()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt8 >= 1:
                            break  # loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writers368)

                # TEMPLATE REWRITE
                # 36:96: -> writers(stmts=$stmts_)
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
    # YarcParser.g:38:1: setting : ID ASSIGN test NEWLINE ({...}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}| -> setting(setting=$ID.textvalue=$test.st)) ;
    def setting(
        self,
    ):
        retval = self.setting_return()
        retval.start = self.input.LT(1)

        ID9 = None
        test10 = None

        try:
            try:
                # YarcParser.g:38:16: ( ID ASSIGN test NEWLINE ({...}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}| -> setting(setting=$ID.textvalue=$test.st)) )
                # YarcParser.g:38:18: ID ASSIGN test NEWLINE ({...}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}| -> setting(setting=$ID.textvalue=$test.st))
                ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_setting392)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_setting394)

                self._state.following.append(self.FOLLOW_test_in_setting396)
                test10 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_setting398)

                # YarcParser.g:38:41: ({...}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}| -> setting(setting=$ID.textvalue=$test.st))
                alt9 = 2
                LA9 = self.input.LA(1)
                if LA9 in {DEDENT}:
                    self.input.LA(2)

                    if self.handler.is_special_setting(ID9.text):
                        alt9 = 1
                    elif True:
                        alt9 = 2
                    else:
                        nvae = NoViableAltException("", 9, 1, self.input)

                        raise nvae

                elif LA9 in {ID}:
                    self.input.LA(2)

                    if self.handler.is_special_setting(ID9.text):
                        alt9 = 1
                    elif True:
                        alt9 = 2
                    else:
                        nvae = NoViableAltException("", 9, 2, self.input)

                        raise nvae

                elif LA9 in {SNIPPET}:
                    self.input.LA(2)

                    if self.handler.is_special_setting(ID9.text):
                        alt9 = 1
                    elif True:
                        alt9 = 2
                    else:
                        nvae = NoViableAltException("", 9, 3, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # YarcParser.g:38:43: {...}?
                    if not (self.handler.is_special_setting(ID9.text)):
                        raise FailedPredicateException(
                            self.input,
                            "setting",
                            "self.handler.is_special_setting($ID.text)",
                        )

                    # TEMPLATE REWRITE
                    # 38:88: -> {self.handler.special_setting_to_str($ID.text, $test.st)}
                    retval.st = self.handler.special_setting_to_str(
                        ID9.text, ((test10 is not None) and [test10.st] or [None])[0]
                    )

                elif alt9 == 2:
                    # YarcParser.g:39:43:
                    pass
                    # TEMPLATE REWRITE
                    # 39:43: -> setting(setting=$ID.textvalue=$test.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "setting",
                        attributes={
                            "setting": ID9.text,
                            "value": ((test10 is not None) and [test10.st] or [None])[
                                0
                            ],
                        },
                    )

                # action start
                self.handler.add_setting(
                    setting=ID9.text,
                    value=((test10 is not None) and [test10.st] or [None])[0],
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
    # YarcParser.g:41:1: stmts :stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt )+ -> stage(stmts=$stmts_);
    def stmts(
        self,
    ):
        retval = self.stmts_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:41:16: (stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt )+ -> stage(stmts=$stmts_))
                # YarcParser.g:41:18: stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt )+
                pass
                # YarcParser.g:41:26: ( open_stmt )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if LA10_0 == OPEN:
                    alt10 = 1
                if alt10 == 1:
                    # YarcParser.g:41:27: open_stmt
                    self._state.following.append(self.FOLLOW_open_stmt_in_stmts527)
                    stmts_ = self.open_stmt()

                    self._state.following.pop()
                    if list_stmts_ is None:
                        list_stmts_ = []
                    list_stmts_.append(stmts_.st)

                # YarcParser.g:41:47: ( aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt )+
                cnt11 = 0
                while True:  # loop11
                    alt11 = 5
                    LA11 = self.input.LA(1)
                    if LA11 in {
                        BIT_NOT,
                        COMBINE,
                        CREATE,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
                        GET,
                        GROUP,
                        ID,
                        INSTANTIATE,
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
                        alt11 = 1
                    elif LA11 in {SNIPPET}:
                        alt11 = 2
                    elif LA11 in {EDIT}:
                        alt11 = 3
                    elif LA11 in {EVERY}:
                        alt11 = 4

                    if alt11 == 1:
                        # YarcParser.g:41:48: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts534
                        )
                        stmts_ = self.aug_expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt11 == 2:
                        # YarcParser.g:41:64: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_stmts538
                        )
                        stmts_ = self.code_snippet()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt11 == 3:
                        # YarcParser.g:41:79: edit_stmt
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts542)
                        stmts_ = self.edit_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt11 == 4:
                        # YarcParser.g:41:91: behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_behavior_stmt_in_stmts546
                        )
                        stmts_ = self.behavior_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt11 >= 1:
                            break  # loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1

                # TEMPLATE REWRITE
                # 41:107: -> stage(stmts=$stmts_)
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
    # YarcParser.g:42:1: writer : ID COLON NEWLINE INDENT ( writer_param )+ DEDENT -> writer(writer_id=$ID.textparams=params);
    def writer(
        self,
    ):
        retval = self.writer_return()
        retval.start = self.input.LT(1)

        ID12 = None
        writer_param11 = None

        params = []
        try:
            try:
                # YarcParser.g:43:3: ( ID COLON NEWLINE INDENT ( writer_param )+ DEDENT -> writer(writer_id=$ID.textparams=params))
                # YarcParser.g:43:5: ID COLON NEWLINE INDENT ( writer_param )+ DEDENT
                ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_writer578)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writer580)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer582)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writer584)

                # YarcParser.g:43:29: ( writer_param )+
                cnt12 = 0
                while True:  # loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if LA12_0 == ID:
                        alt12 = 1

                    if alt12 == 1:
                        # YarcParser.g:43:30: writer_param
                        self._state.following.append(
                            self.FOLLOW_writer_param_in_writer587
                        )
                        writer_param11 = self.writer_param()

                        self._state.following.pop()

                        # action start
                        params.append(
                            (
                                (writer_param11 is not None)
                                and [writer_param11.param]
                                or [None]
                            )[0]
                        )
                        # action end

                    else:
                        if cnt12 >= 1:
                            break  # loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writer593)

                # action start
                self.handler.check_writer_params(params)
                # action end

                # TEMPLATE REWRITE
                # 44:3: -> writer(writer_id=$ID.textparams=params)
                retval.st = self.templateLib.getInstanceOf(
                    "writer", attributes={"writer_id": ID12.text, "params": params}
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
    # YarcParser.g:45:1: writer_param returns [param] : ID ASSIGN test NEWLINE ;
    def writer_param(
        self,
    ):
        retval = self.writer_param_return()
        retval.start = self.input.LT(1)

        ID13 = None
        test14 = None

        try:
            try:
                # YarcParser.g:45:29: ( ID ASSIGN test NEWLINE )
                # YarcParser.g:45:31: ID ASSIGN test NEWLINE
                ID13 = self.match(self.input, ID, self.FOLLOW_ID_in_writer_param622)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_writer_param624)

                self._state.following.append(self.FOLLOW_test_in_writer_param626)
                test14 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer_param628)

                # action start
                retval.param = Parameter(
                    ID13.text, ((test14 is not None) and [test14.st] or [None])[0]
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
    # YarcParser.g:49:1: open_stmt : OPEN test NEWLINE -> open_stmt(path=$test.st);
    def open_stmt(
        self,
    ):
        retval = self.open_stmt_return()
        retval.start = self.input.LT(1)

        test15 = None

        try:
            try:
                # YarcParser.g:49:11: ( OPEN test NEWLINE -> open_stmt(path=$test.st))
                # YarcParser.g:49:13: OPEN test NEWLINE
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_open_stmt642)

                self._state.following.append(self.FOLLOW_test_in_open_stmt644)
                test15 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_open_stmt646)

                # TEMPLATE REWRITE
                # 49:31: -> open_stmt(path=$test.st)
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
    # YarcParser.g:50:1: edit_stmt : EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))) ;
    def edit_stmt(
        self,
    ):
        retval = self.edit_stmt_return()
        retval.start = self.input.LT(1)

        list_params = None
        list_values = None
        id = None
        edit_block16 = None
        params = None
        values = None
        try:
            try:
                # YarcParser.g:50:11: ( EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))) )
                # YarcParser.g:50:13: EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                self.match(self.input, EDIT, self.FOLLOW_EDIT_in_edit_stmt662)

                # YarcParser.g:50:18: ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
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
                    # YarcParser.g:50:19: TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt665
                    )

                    self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_stmt667)

                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_stmt669)

                    self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_stmt671)

                    # YarcParser.g:50:49: (params+= name values+= test NEWLINE )+
                    cnt13 = 0
                    while True:  # loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if LA13_0 in {ID, UNDERSCORE}:
                            alt13 = 1

                        if alt13 == 1:
                            # YarcParser.g:50:50: params+= name values+= test NEWLINE
                            self._state.following.append(
                                self.FOLLOW_name_in_edit_stmt676
                            )
                            params = self.name()

                            self._state.following.pop()
                            if list_params is None:
                                list_params = []
                            list_params.append(params.st)

                            self._state.following.append(
                                self.FOLLOW_test_in_edit_stmt680
                            )
                            values = self.test()

                            self._state.following.pop()
                            if list_values is None:
                                list_values = []
                            list_values.append(values.st)

                            self.match(
                                self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_stmt682
                            )

                        else:
                            if cnt13 >= 1:
                                break  # loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1

                    self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_stmt686)

                    # TEMPLATE REWRITE
                    # 50:93: -> edit_timeline(params=$paramsvalues=$values)
                    retval.st = self.templateLib.getInstanceOf(
                        "edit_timeline",
                        attributes={"params": list_params, "values": list_values},
                    )

                elif alt14 == 2:
                    # YarcParser.g:51:20: id= name edit_block[$id.st]
                    self._state.following.append(self.FOLLOW_name_in_edit_stmt724)
                    id = self.name()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_edit_block_in_edit_stmt726)
                    edit_block16 = self.edit_block(
                        ((id is not None) and [id.st] or [None])[0]
                    )

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 51:47: -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "edit_stmt",
                        attributes={
                            "id": ((id is not None) and [id.st] or [None])[0],
                            "stmts": self.handler.get_attrs(
                                "edit",
                                (
                                    (edit_block16 is not None)
                                    and [edit_block16.attrs]
                                    or [None]
                                )[0],
                            ),
                            "behaviors": self.handler.get_behaviors(
                                (
                                    (edit_block16 is not None)
                                    and [edit_block16.attrs]
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
    # YarcParser.g:54:1: create_expr[id] : CREATE (count= test )? (prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))|prim= ( ( STEREO )? CAMERA ) (attrs= edit_block[$id] | NEWLINE ) -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st))) ;
    def create_expr(self, id):
        retval = self.create_expr_return()
        retval.start = self.input.LT(1)

        prim = None
        count = None
        attrs = None
        file = None

        try:
            try:
                # YarcParser.g:54:16: ( CREATE (count= test )? (prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))|prim= ( ( STEREO )? CAMERA ) (attrs= edit_block[$id] | NEWLINE ) -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st))) )
                # YarcParser.g:55:3: CREATE (count= test )? (prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))|prim= ( ( STEREO )? CAMERA ) (attrs= edit_block[$id] | NEWLINE ) -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st)))
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr775)

                # YarcParser.g:55:15: (count= test )?
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
                    # YarcParser.g:55:15: count= test
                    self._state.following.append(self.FOLLOW_test_in_create_expr779)
                    count = self.test()

                    self._state.following.pop()

                # YarcParser.g:55:22: (prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))|prim= ( ( STEREO )? CAMERA ) (attrs= edit_block[$id] | NEWLINE ) -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st)))
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
                    # YarcParser.g:56:5: prim= ( SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE )
                    pass
                    # YarcParser.g:56:10: ( SHAPE | LIGHT )
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
                        # YarcParser.g:56:11: SHAPE
                        prim = self.match(
                            self.input, SHAPE, self.FOLLOW_SHAPE_in_create_expr791
                        )

                    elif alt16 == 2:
                        # YarcParser.g:56:19: LIGHT
                        prim = self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr795
                        )

                    # YarcParser.g:56:26: (attrs= edit_block[$id] | NEWLINE )
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
                        # YarcParser.g:56:27: attrs= edit_block[$id]
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr801
                        )
                        attrs = self.edit_block(id)

                        self._state.following.pop()

                    elif alt17 == 2:
                        # YarcParser.g:56:51: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr806
                        )

                    # TEMPLATE REWRITE
                    # 57:7: -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "create_prim",
                        attributes={
                            "id": id,
                            "prim": self.handler.map(prim),
                            "params": self.handler.get_params(
                                prim,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                ((count is not None) and [count.st] or [None])[0],
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
                    # YarcParser.g:62:7: prim= ( ( STEREO )? CAMERA ) (attrs= edit_block[$id] | NEWLINE )
                    pass
                    # YarcParser.g:62:12: ( ( STEREO )? CAMERA )
                    # YarcParser.g:62:13: ( STEREO )? CAMERA
                    # YarcParser.g:62:13: ( STEREO )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if LA18_0 == STEREO:
                        alt18 = 1
                    if alt18 == 1:
                        # YarcParser.g:62:13: STEREO
                        prim = self.match(
                            self.input, STEREO, self.FOLLOW_STEREO_in_create_expr942
                        )

                    prim = self.match(
                        self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr945
                    )

                    # YarcParser.g:62:29: (attrs= edit_block[$id] | NEWLINE )
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
                        # YarcParser.g:62:30: attrs= edit_block[$id]
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr951
                        )
                        attrs = self.edit_block(id)

                        self._state.following.pop()

                    elif alt19 == 2:
                        # YarcParser.g:62:54: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr956
                        )

                    # TEMPLATE REWRITE
                    # 63:7: -> create_camera(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "create_camera",
                        attributes={
                            "id": id,
                            "prim": self.handler.map(prim),
                            "params": self.handler.get_params(
                                prim,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                ((count is not None) and [count.st] or [None])[0],
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
                    # YarcParser.g:68:7: FROM file= test (attrs= edit_block[$id] | NEWLINE )
                    self.match(self.input, FROM, self.FOLLOW_FROM_in_create_expr1089)

                    self._state.following.append(self.FOLLOW_test_in_create_expr1093)
                    file = self.test()

                    self._state.following.pop()

                    # YarcParser.g:68:22: (attrs= edit_block[$id] | NEWLINE )
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
                        # YarcParser.g:68:23: attrs= edit_block[$id]
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr1098
                        )
                        attrs = self.edit_block(id)

                        self._state.following.pop()

                    elif alt20 == 2:
                        # YarcParser.g:68:47: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr1103
                        )

                    # TEMPLATE REWRITE
                    # 69:7: -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "create_from",
                        attributes={
                            "id": id,
                            "file": ((file is not None) and [file.st] or [None])[0],
                            "params": self.handler.get_params(
                                "from_file",
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                ((count is not None) and [count.st] or [None])[0],
                            ),
                            "stmts": self.handler.get_attrs(
                                "from_file",
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                            ),
                            "behaviors": self.handler.get_behaviors(
                                ((attrs is not None) and [attrs.attrs] or [None])[0]
                            ),
                        },
                    )

                elif alt22 == 4:
                    # YarcParser.g:74:7: MATERIAL (attrs= simple_block | NEWLINE )
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr1234
                    )

                    # YarcParser.g:74:16: (attrs= simple_block | NEWLINE )
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
                        # YarcParser.g:74:17: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_create_expr1239
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt21 == 2:
                        # YarcParser.g:74:38: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr1243
                        )

                    # TEMPLATE REWRITE
                    # 75:7: -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st))
                    retval.st = self.templateLib.getInstanceOf(
                        "create_material",
                        attributes={
                            "id": id,
                            "params": self.handler.get_params(
                                "material",
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                                ((count is not None) and [count.st] or [None])[0],
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
    # YarcParser.g:80:1: instantiate_expr[id] : INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE ) -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params(\"instantiate\", $edit_block.attrs, $count.st)stmts=self.handler.get_attrs(\"instantiate\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs));
    def instantiate_expr(self, id):
        retval = self.instantiate_expr_return()
        retval.start = self.input.LT(1)

        count = None
        file = None
        edit_block17 = None

        try:
            try:
                # YarcParser.g:80:22: ( INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE ) -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params(\"instantiate\", $edit_block.attrs, $count.st)stmts=self.handler.get_attrs(\"instantiate\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                # YarcParser.g:80:24: INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE )
                self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr1305,
                )

                # YarcParser.g:80:42: ( test )?
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
                    # YarcParser.g:80:43: test
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr1310
                    )
                    count = self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr1314)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr1318)
                file = self.test()

                self._state.following.pop()

                # YarcParser.g:80:65: ( edit_block[$id] | NEWLINE )
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
                    # YarcParser.g:80:66: edit_block[$id]
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr1321
                    )
                    edit_block17 = self.edit_block(id)

                    self._state.following.pop()

                elif alt24 == 2:
                    # YarcParser.g:80:84: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instantiate_expr1326
                    )

                # TEMPLATE REWRITE
                # 81:3: -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params(\"instantiate\", $edit_block.attrs, $count.st)stmts=self.handler.get_attrs(\"instantiate\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                retval.st = self.templateLib.getInstanceOf(
                    "instantiate_expr",
                    attributes={
                        "id": id,
                        "file": ((file is not None) and [file.st] or [None])[0],
                        "params": self.handler.get_params(
                            "instantiate",
                            (
                                (edit_block17 is not None)
                                and [edit_block17.attrs]
                                or [None]
                            )[0],
                            count.st,
                        ),
                        "stmts": self.handler.get_attrs(
                            "instantiate",
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
    # YarcParser.g:86:1: group_expr[id] : GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE ) -> group_expr(id=$idnames=$namesparams=self.handler.get_params(\"group\", $edit_block.attrs)stmts=self.handler.get_attrs(\"group\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs));
    def group_expr(self, id):
        retval = self.group_expr_return()
        retval.start = self.input.LT(1)

        list_names = None
        edit_block18 = None
        names = None
        try:
            try:
                # YarcParser.g:86:22: ( GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE ) -> group_expr(id=$idnames=$namesparams=self.handler.get_params(\"group\", $edit_block.attrs)stmts=self.handler.get_attrs(\"group\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                # YarcParser.g:86:24: GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE )
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_expr1465)

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr1467)

                self._state.following.append(self.FOLLOW_name_in_group_expr1471)
                names = self.name()

                self._state.following.pop()
                if list_names is None:
                    list_names = []
                list_names.append(names.st)

                # YarcParser.g:86:49: ( COMMA names+= name )*
                while True:  # loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if LA25_0 == COMMA:
                        alt25 = 1

                    if alt25 == 1:
                        # YarcParser.g:86:50: COMMA names+= name
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

                # YarcParser.g:86:77: ( edit_block[$id] | NEWLINE )
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
                    # YarcParser.g:86:78: edit_block[$id]
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr1485
                    )
                    edit_block18 = self.edit_block(id)

                    self._state.following.pop()

                elif alt26 == 2:
                    # YarcParser.g:86:96: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_group_expr1490
                    )

                # TEMPLATE REWRITE
                # 87:3: -> group_expr(id=$idnames=$namesparams=self.handler.get_params(\"group\", $edit_block.attrs)stmts=self.handler.get_attrs(\"group\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                retval.st = self.templateLib.getInstanceOf(
                    "group_expr",
                    attributes={
                        "id": id,
                        "names": list_names,
                        "params": self.handler.get_params(
                            "group",
                            (
                                (edit_block18 is not None)
                                and [edit_block18.attrs]
                                or [None]
                            )[0],
                        ),
                        "stmts": self.handler.get_attrs(
                            "group",
                            (
                                (edit_block18 is not None)
                                and [edit_block18.attrs]
                                or [None]
                            )[0],
                        ),
                        "behaviors": self.handler.get_behaviors(
                            (
                                (edit_block18 is not None)
                                and [edit_block18.attrs]
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
    # YarcParser.g:92:1: get_expr[id] : GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE ) -> get_expr(id=$idfilter=$filter.stpath=$path.stparams=self.handler.get_params(\"get\", $simple_block.attrs));
    def get_expr(self, id):
        retval = self.get_expr_return()
        retval.start = self.input.LT(1)

        filter = None
        path = None
        simple_block19 = None

        try:
            try:
                # YarcParser.g:92:22: ( GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE ) -> get_expr(id=$idfilter=$filter.stpath=$path.stparams=self.handler.get_params(\"get\", $simple_block.attrs)))
                # YarcParser.g:92:24: GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE )
                self.match(self.input, GET, self.FOLLOW_GET_in_get_expr1604)

                # YarcParser.g:92:28: (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )?
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
                    # YarcParser.g:92:29: filter= ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # YarcParser.g:92:36: ( CAMERA | LIGHT | MATERIAL | name )
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
                        # YarcParser.g:92:37: CAMERA
                        filter = self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr1610
                        )

                    elif alt27 == 2:
                        # YarcParser.g:92:46: LIGHT
                        filter = self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr1614
                        )

                    elif alt27 == 3:
                        # YarcParser.g:92:54: MATERIAL
                        filter = self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr1618
                        )

                    elif alt27 == 4:
                        # YarcParser.g:92:65: name
                        self._state.following.append(self.FOLLOW_name_in_get_expr1622)
                        filter = self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr1625)

                self._state.following.append(self.FOLLOW_test_in_get_expr1631)
                path = self.test()

                self._state.following.pop()

                # YarcParser.g:92:86: ( simple_block | NEWLINE )
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
                    # YarcParser.g:92:87: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr1634
                    )
                    simple_block19 = self.simple_block()

                    self._state.following.pop()

                elif alt29 == 2:
                    # YarcParser.g:92:102: NEWLINE
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr1638)

                # TEMPLATE REWRITE
                # 93:3: -> get_expr(id=$idfilter=$filter.stpath=$path.stparams=self.handler.get_params(\"get\", $simple_block.attrs))
                retval.st = self.templateLib.getInstanceOf(
                    "get_expr",
                    attributes={
                        "id": id,
                        "filter": filter.st,
                        "path": ((path is not None) and [path.st] or [None])[0],
                        "params": self.handler.get_params(
                            "get",
                            (
                                (simple_block19 is not None)
                                and [simple_block19.attrs]
                                or [None]
                            )[0],
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
    # YarcParser.g:98:1: edit_block[id] returns [attrs] : COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT ;
    def edit_block(self, id):
        retval = self.edit_block_return()
        retval.start = self.input.LT(1)

        stmt_ = None

        retval.attrs = []
        try:
            try:
                # YarcParser.g:100:3: ( COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT )
                # YarcParser.g:100:5: COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block1730)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block1732)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block1734)

                # YarcParser.g:100:26: (stmt_= ( attr | inner_behavior_stmt[$id] ) )+
                cnt31 = 0
                while True:  # loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if LA31_0 in {
                        EVERY,
                        ID,
                        LOOK_AT,
                        MATERIAL,
                        MOVE_TO_CAM,
                        PHYSICS,
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
                        # YarcParser.g:100:27: stmt_= ( attr | inner_behavior_stmt[$id] )
                        pass
                        # YarcParser.g:100:33: ( attr | inner_behavior_stmt[$id] )
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if LA30_0 in {
                            ID,
                            LOOK_AT,
                            MATERIAL,
                            MOVE_TO_CAM,
                            PHYSICS,
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
                            # YarcParser.g:100:34: attr
                            self._state.following.append(
                                self.FOLLOW_attr_in_edit_block1740
                            )
                            stmt_ = self.attr()

                            self._state.following.pop()

                        elif alt30 == 2:
                            # YarcParser.g:100:41: inner_behavior_stmt[$id]
                            self._state.following.append(
                                self.FOLLOW_inner_behavior_stmt_in_edit_block1744
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

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_block1752)

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
    # YarcParser.g:101:1: simple_block returns [attrs] : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        retval = self.simple_block_return()
        retval.start = self.input.LT(1)

        simple_attr20 = None

        retval.attrs = []
        try:
            try:
                # YarcParser.g:103:3: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # YarcParser.g:103:5: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block1771)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block1773)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block1775)

                # YarcParser.g:103:26: ( simple_attr )+
                cnt32 = 0
                while True:  # loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if LA32_0 in {ID, UNDERSCORE}:
                        alt32 = 1

                    if alt32 == 1:
                        # YarcParser.g:103:27: simple_attr
                        self._state.following.append(
                            self.FOLLOW_simple_attr_in_simple_block1778
                        )
                        simple_attr20 = self.simple_attr()

                        self._state.following.pop()

                        # action start
                        retval.attrs.append(
                            (
                                (simple_attr20 is not None)
                                and [simple_attr20.attr]
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

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_simple_block1784)

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
    # YarcParser.g:105:1: attr returns [attr] : a= ( core_attr | simple_attr | compound_attr ) -> {$a.st};
    def attr(
        self,
    ):
        retval = self.attr_return()
        retval.start = self.input.LT(1)

        a = None

        try:
            try:
                # YarcParser.g:105:21: (a= ( core_attr | simple_attr | compound_attr ) -> {$a.st})
                # YarcParser.g:105:23: a= ( core_attr | simple_attr | compound_attr )
                pass
                # YarcParser.g:105:25: ( core_attr | simple_attr | compound_attr )
                alt33 = 3
                LA33 = self.input.LA(1)
                if LA33 in {
                    LOOK_AT,
                    MATERIAL,
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
                    # YarcParser.g:105:26: core_attr
                    self._state.following.append(self.FOLLOW_core_attr_in_attr1799)
                    a = self.core_attr()

                    self._state.following.pop()

                elif alt33 == 2:
                    # YarcParser.g:105:38: simple_attr
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr1803)
                    a = self.simple_attr()

                    self._state.following.pop()

                elif alt33 == 3:
                    # YarcParser.g:105:52: compound_attr
                    self._state.following.append(self.FOLLOW_compound_attr_in_attr1807)
                    a = self.compound_attr()

                    self._state.following.pop()

                # action start
                retval.attr = a.attr
                # action end

                # TEMPLATE REWRITE
                # 105:83: -> {$a.st}
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
    # YarcParser.g:106:1: simple_attr returns [attr] : name_= name ( COLON type= name )? value= test NEWLINE -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st);
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
                # YarcParser.g:108:3: (name_= name ( COLON type= name )? value= test NEWLINE -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st))
                # YarcParser.g:108:5: name_= name ( COLON type= name )? value= test NEWLINE
                self._state.following.append(self.FOLLOW_name_in_simple_attr1837)
                name_ = self.name()

                self._state.following.pop()

                # YarcParser.g:108:16: ( COLON type= name )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if LA34_0 == COLON:
                    alt34 = 1
                if alt34 == 1:
                    # YarcParser.g:108:17: COLON type= name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr1840)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr1844)
                    type = self.name()

                    self._state.following.pop()

                self._state.following.append(self.FOLLOW_test_in_simple_attr1850)
                value = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_attr1852)

                # TEMPLATE REWRITE
                # 109:3: -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st)
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
    # YarcParser.g:111:1: compound_attr returns [attr] : (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs))|name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE ) -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs))) ;
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
                # YarcParser.g:113:3: ( (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs))|name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE ) -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs))) )
                # YarcParser.g:113:5: (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs))|name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE ) -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs)))
                pass
                # YarcParser.g:113:5: (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs))|name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE ) -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs)))
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
                    # YarcParser.g:113:7: name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr1899
                    )

                    self.match(self.input, ON, self.FOLLOW_ON_in_compound_attr1901)

                    self._state.following.append(self.FOLLOW_name_in_compound_attr1905)
                    surface = self.name()

                    self._state.following.pop()

                    # YarcParser.g:113:37: (attrs= simple_block | NEWLINE )
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
                        # YarcParser.g:113:38: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr1910
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt35 == 2:
                        # YarcParser.g:113:59: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr1914,
                        )

                    # TEMPLATE REWRITE
                    # 114:7: -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))
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
                            ),
                        },
                    )

                elif alt39 == 2:
                    # YarcParser.g:117:7: name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input,
                        ROT_AROUND,
                        self.FOLLOW_ROT_AROUND_in_compound_attr1998,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr2002)
                    center = self.name()

                    self._state.following.pop()

                    # YarcParser.g:117:36: (attrs= simple_block | NEWLINE )
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
                        # YarcParser.g:117:37: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr2007
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt36 == 2:
                        # YarcParser.g:117:58: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr2011,
                        )

                    # TEMPLATE REWRITE
                    # 118:7: -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "rot_around_expr",
                        attributes={
                            "center": ((center is not None) and [center.st] or [None])[
                                0
                            ],
                            "params": self.handler.get_params(
                                name_,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                            ),
                        },
                    )

                elif alt39 == 3:
                    # YarcParser.g:120:7: name_= PHYSICS (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input, PHYSICS, self.FOLLOW_PHYSICS_in_compound_attr2068
                    )

                    # YarcParser.g:120:21: (attrs= simple_block | NEWLINE )
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
                        # YarcParser.g:120:22: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr2073
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt37 == 2:
                        # YarcParser.g:120:43: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr2077,
                        )

                    # TEMPLATE REWRITE
                    # 121:7: -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "physics_expr",
                        attributes={
                            "physics_attr": self.handler.map(name_),
                            "params": self.handler.get_params(
                                name_,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                            ),
                        },
                    )

                elif alt39 == 4:
                    # YarcParser.g:123:7: name_= MOVE_TO_CAM camera= name (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input,
                        MOVE_TO_CAM,
                        self.FOLLOW_MOVE_TO_CAM_in_compound_attr2130,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr2134)
                    camera = self.name()

                    self._state.following.pop()

                    # YarcParser.g:123:37: (attrs= simple_block | NEWLINE )
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
                        # YarcParser.g:123:38: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr2139
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt38 == 2:
                        # YarcParser.g:123:59: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr2143,
                        )

                    # TEMPLATE REWRITE
                    # 124:7: -> move_to_camera_expr(camera=$camera.stparams=self.handler.get_params($name_, $attrs.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "move_to_camera_expr",
                        attributes={
                            "camera": ((camera is not None) and [camera.st] or [None])[
                                0
                            ],
                            "params": self.handler.get_params(
                                name_,
                                ((attrs is not None) and [attrs.attrs] or [None])[0],
                            ),
                        },
                    )

                retval.stop = self.input.LT(-1)

                # action start
                retval.attr = Attribute(name_.text, "", retval.st)
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
    # YarcParser.g:128:1: core_attr returns [attr] : ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test ( ORDER )? -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)| MATERIAL value= test -> material_expr(value=$value.st)) NEWLINE ;
    def core_attr(
        self,
    ):
        retval = self.core_attr_return()
        retval.start = self.input.LT(1)

        axis = None
        TRANSLATE21 = None
        ROTATE22 = None
        SCALE23 = None
        LOOK_AT24 = None
        UP_AXIS25 = None
        SIZE26 = None
        SEMANTICS27 = None
        VISIBLE28 = None
        MATERIAL29 = None
        value = None

        try:
            try:
                # YarcParser.g:130:3: ( ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test ( ORDER )? -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)| MATERIAL value= test -> material_expr(value=$value.st)) NEWLINE )
                # YarcParser.g:130:5: ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test ( ORDER )? -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)| MATERIAL value= test -> material_expr(value=$value.st)) NEWLINE
                pass
                # YarcParser.g:130:5: ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test ( ORDER )? -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)| MATERIAL value= test -> material_expr(value=$value.st))
                alt43 = 9
                LA43 = self.input.LA(1)
                if LA43 in {TRANSLATE}:
                    alt43 = 1
                elif LA43 in {ROTATE}:
                    alt43 = 2
                elif LA43 in {SCALE}:
                    alt43 = 3
                elif LA43 in {LOOK_AT}:
                    alt43 = 4
                elif LA43 in {UP_AXIS}:
                    alt43 = 5
                elif LA43 in {SIZE}:
                    alt43 = 6
                elif LA43 in {SEMANTICS}:
                    alt43 = 7
                elif LA43 in {VISIBLE}:
                    alt43 = 8
                elif LA43 in {MATERIAL}:
                    alt43 = 9
                else:
                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # YarcParser.g:130:7: TRANSLATE (axis= AXIS )? TO value= test
                    TRANSLATE21 = self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr2221
                    )

                    # YarcParser.g:130:21: (axis= AXIS )?
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if LA40_0 == AXIS:
                        alt40 = 1
                    if alt40 == 1:
                        # YarcParser.g:130:21: axis= AXIS
                        axis = self.match(
                            self.input, AXIS, self.FOLLOW_AXIS_in_core_attr2225
                        )

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr2228)

                    self._state.following.append(self.FOLLOW_test_in_core_attr2232)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(TRANSLATE21, axis)
                    # action end

                    # TEMPLATE REWRITE
                    # 130:87: -> translate_expr(type=namevalue=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "translate_expr",
                        attributes={
                            "type": name,
                            "value": ((value is not None) and [value.st] or [None])[0],
                        },
                    )

                elif alt43 == 2:
                    # YarcParser.g:131:7: ROTATE (axis= AXIS )? value= test ( ORDER )?
                    ROTATE22 = self.match(
                        self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr2256
                    )

                    # YarcParser.g:131:18: (axis= AXIS )?
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if LA41_0 == AXIS:
                        alt41 = 1
                    if alt41 == 1:
                        # YarcParser.g:131:18: axis= AXIS
                        axis = self.match(
                            self.input, AXIS, self.FOLLOW_AXIS_in_core_attr2260
                        )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2265)
                    value = self.test()

                    self._state.following.pop()

                    # YarcParser.g:131:36: ( ORDER )?
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if LA42_0 == ORDER:
                        alt42 = 1
                    if alt42 == 1:
                        # YarcParser.g:131:36: ORDER
                        self.match(
                            self.input, ORDER, self.FOLLOW_ORDER_in_core_attr2267
                        )

                    # action start
                    name = self.handler.map(ROTATE22, axis)
                    # action end

                    # TEMPLATE REWRITE
                    # 131:85: -> rotate_expr(type=namevalue=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "rotate_expr",
                        attributes={
                            "type": name,
                            "value": ((value is not None) and [value.st] or [None])[0],
                        },
                    )

                elif alt43 == 3:
                    # YarcParser.g:132:7: SCALE value= test
                    SCALE23 = self.match(
                        self.input, SCALE, self.FOLLOW_SCALE_in_core_attr2292
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2296)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SCALE23)
                    # action end

                    # TEMPLATE REWRITE
                    # 132:58: -> scale_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "scale_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt43 == 4:
                    # YarcParser.g:133:7: LOOK_AT value= test
                    LOOK_AT24 = self.match(
                        self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr2315
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2319)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(LOOK_AT24)
                    # action end

                    # TEMPLATE REWRITE
                    # 133:62: -> look_at_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "look_at_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt43 == 5:
                    # YarcParser.g:134:7: UP_AXIS value= test
                    UP_AXIS25 = self.match(
                        self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr2338
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2342)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(UP_AXIS25)
                    # action end

                    # TEMPLATE REWRITE
                    # 134:62: -> look_at_up_axis_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "look_at_up_axis_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt43 == 6:
                    # YarcParser.g:135:7: SIZE value= test
                    SIZE26 = self.match(
                        self.input, SIZE, self.FOLLOW_SIZE_in_core_attr2361
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2365)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SIZE26)
                    # action end

                    # TEMPLATE REWRITE
                    # 135:56: -> size_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "size_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt43 == 7:
                    # YarcParser.g:136:7: SEMANTICS value= test
                    SEMANTICS27 = self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr2384
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2388)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SEMANTICS27)
                    # action end

                    # TEMPLATE REWRITE
                    # 136:66: -> semantics_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "semantics_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt43 == 8:
                    # YarcParser.g:137:7: VISIBLE value= test
                    VISIBLE28 = self.match(
                        self.input, VISIBLE, self.FOLLOW_VISIBLE_in_core_attr2407
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2411)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(VISIBLE28)
                    # action end

                    # TEMPLATE REWRITE
                    # 137:62: -> visible_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "visible_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt43 == 9:
                    # YarcParser.g:138:7: MATERIAL value= test
                    MATERIAL29 = self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_core_attr2430
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr2434)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(MATERIAL29)
                    # action end

                    # TEMPLATE REWRITE
                    # 138:64: -> material_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "material_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_core_attr2451)

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
    # YarcParser.g:141:1: inner_behavior_stmt[id] returns [attr] : behavior_expr inner_behavior_block -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st);
    def inner_behavior_stmt(self, id):
        retval = self.inner_behavior_stmt_return()
        retval.start = self.input.LT(1)

        behavior_expr30 = None
        inner_behavior_block31 = None

        try:
            try:
                # YarcParser.g:143:3: ( behavior_expr inner_behavior_block -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st))
                # YarcParser.g:143:5: behavior_expr inner_behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_inner_behavior_stmt2474
                )
                behavior_expr30 = self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_inner_behavior_block_in_inner_behavior_stmt2476
                )
                inner_behavior_block31 = self.inner_behavior_block()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 143:40: -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st)
                retval.st = self.templateLib.getInstanceOf(
                    "inner_behavior_stmt",
                    attributes={
                        "behavior": (
                            (behavior_expr30 is not None)
                            and [behavior_expr30.st]
                            or [None]
                        )[0],
                        "id": id,
                        "block": (
                            (inner_behavior_block31 is not None)
                            and [inner_behavior_block31.st]
                            or [None]
                        )[0],
                    },
                )

                retval.stop = self.input.LT(-1)

                # action start
                retval.attr = Attribute("behavior", "", retval.st)
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
    # YarcParser.g:144:1: inner_behavior_block : COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT -> behavior_block(stmts=$stmts_);
    def inner_behavior_block(
        self,
    ):
        retval = self.inner_behavior_block_return()
        retval.start = self.input.LT(1)

        list_stmts_ = None
        stmts_ = None
        try:
            try:
                # YarcParser.g:144:22: ( COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT -> behavior_block(stmts=$stmts_))
                # YarcParser.g:144:24: COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block2502
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block2504
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block2506
                )

                # YarcParser.g:144:51: (stmts_+= attr )+
                cnt44 = 0
                while True:  # loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if LA44_0 in {
                        ID,
                        LOOK_AT,
                        MATERIAL,
                        MOVE_TO_CAM,
                        PHYSICS,
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
                        alt44 = 1

                    if alt44 == 1:
                        # YarcParser.g:144:51: stmts_+= attr
                        self._state.following.append(
                            self.FOLLOW_attr_in_inner_behavior_block2510
                        )
                        stmts_ = self.attr()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt44 >= 1:
                            break  # loop44

                        eee = EarlyExitException(44, self.input)
                        raise eee

                    cnt44 += 1

                self.match(
                    self.input, DEDENT, self.FOLLOW_DEDENT_in_inner_behavior_block2513
                )

                # TEMPLATE REWRITE
                # 144:66: -> behavior_block(stmts=$stmts_)
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
    # YarcParser.g:147:1: behavior_stmt : behavior_expr behavior_block -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st);
    def behavior_stmt(
        self,
    ):
        retval = self.behavior_stmt_return()
        retval.start = self.input.LT(1)

        behavior_expr32 = None
        behavior_block33 = None

        try:
            try:
                # YarcParser.g:147:16: ( behavior_expr behavior_block -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st))
                # YarcParser.g:147:18: behavior_expr behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_behavior_stmt2533
                )
                behavior_expr32 = self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_behavior_block_in_behavior_stmt2535
                )
                behavior_block33 = self.behavior_block()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 147:47: -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st)
                retval.st = self.templateLib.getInstanceOf(
                    "behavior_stmt",
                    attributes={
                        "behavior": (
                            (behavior_expr32 is not None)
                            and [behavior_expr32.st]
                            or [None]
                        )[0],
                        "block": (
                            (behavior_block33 is not None)
                            and [behavior_block33.st]
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
    # YarcParser.g:148:1: behavior_expr : EVERY (interval= test )? type= ( FRAMES | TIME ) -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type));
    def behavior_expr(
        self,
    ):
        retval = self.behavior_expr_return()
        retval.start = self.input.LT(1)

        type = None
        interval = None

        try:
            try:
                # YarcParser.g:148:16: ( EVERY (interval= test )? type= ( FRAMES | TIME ) -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type)))
                # YarcParser.g:148:18: EVERY (interval= test )? type= ( FRAMES | TIME )
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr2557)

                # YarcParser.g:148:32: (interval= test )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 in {
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
                    alt45 = 1
                if alt45 == 1:
                    # YarcParser.g:148:32: interval= test
                    self._state.following.append(self.FOLLOW_test_in_behavior_expr2561)
                    interval = self.test()

                    self._state.following.pop()

                # YarcParser.g:148:44: ( FRAMES | TIME )
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 == FRAMES:
                    alt46 = 1
                elif LA46_0 == TIME:
                    alt46 = 2
                else:
                    nvae = NoViableAltException("", 46, 0, self.input)

                    raise nvae

                if alt46 == 1:
                    # YarcParser.g:148:45: FRAMES
                    type = self.match(
                        self.input, FRAMES, self.FOLLOW_FRAMES_in_behavior_expr2567
                    )

                elif alt46 == 2:
                    # YarcParser.g:148:54: TIME
                    type = self.match(
                        self.input, TIME, self.FOLLOW_TIME_in_behavior_expr2571
                    )

                # TEMPLATE REWRITE
                # 148:60: -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type))
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
    # YarcParser.g:149:1: behavior_block : COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt )+ DEDENT -> behavior_block(stmts=$stmts_);
    def behavior_block(
        self,
    ):
        retval = self.behavior_block_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:149:16: ( COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt )+ DEDENT -> behavior_block(stmts=$stmts_))
                # YarcParser.g:149:18: COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | code_snippet | edit_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block2593)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block2595
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block2597)

                # YarcParser.g:149:47: ( aug_expr_stmt | code_snippet | edit_stmt )+
                cnt47 = 0
                while True:  # loop47
                    alt47 = 4
                    LA47 = self.input.LA(1)
                    if LA47 in {
                        BIT_NOT,
                        COMBINE,
                        CREATE,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
                        GET,
                        GROUP,
                        ID,
                        INSTANTIATE,
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
                        alt47 = 1
                    elif LA47 in {SNIPPET}:
                        alt47 = 2
                    elif LA47 in {EDIT}:
                        alt47 = 3

                    if alt47 == 1:
                        # YarcParser.g:149:48: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block2602
                        )
                        stmts_ = self.aug_expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt47 == 2:
                        # YarcParser.g:149:64: code_snippet
                        self._state.following.append(
                            self.FOLLOW_code_snippet_in_behavior_block2606
                        )
                        stmts_ = self.code_snippet()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt47 == 3:
                        # YarcParser.g:149:79: edit_stmt
                        self._state.following.append(
                            self.FOLLOW_edit_stmt_in_behavior_block2610
                        )
                        stmts_ = self.edit_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt47 >= 1:
                            break  # loop47

                        eee = EarlyExitException(47, self.input)
                        raise eee

                    cnt47 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_behavior_block2614)

                # TEMPLATE REWRITE
                # 149:98: -> behavior_block(stmts=$stmts_)
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
    # YarcParser.g:152:1: expr_stmt : assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st);
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
                # YarcParser.g:152:11: (assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st))
                # YarcParser.g:152:13: assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt2635)
                assignable = self.testlist()

                self._state.following.pop()

                # YarcParser.g:152:36: ( AUG_ASSIGN | ASSIGN )
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if LA48_0 == AUG_ASSIGN:
                    alt48 = 1
                elif LA48_0 == ASSIGN:
                    alt48 = 2
                else:
                    nvae = NoViableAltException("", 48, 0, self.input)

                    raise nvae

                if alt48 == 1:
                    # YarcParser.g:152:37: AUG_ASSIGN
                    op = self.match(
                        self.input, AUG_ASSIGN, self.FOLLOW_AUG_ASSIGN_in_expr_stmt2640
                    )

                elif alt48 == 2:
                    # YarcParser.g:152:50: ASSIGN
                    op = self.match(
                        self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr_stmt2644
                    )

                # YarcParser.g:152:64: ( testlist | fetch_expr )
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
                    # YarcParser.g:152:65: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt2650)
                    value = self.testlist()

                    self._state.following.pop()

                elif alt49 == 2:
                    # YarcParser.g:152:76: fetch_expr
                    self._state.following.append(
                        self.FOLLOW_fetch_expr_in_expr_stmt2654
                    )
                    value = self.fetch_expr()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expr_stmt2657)

                # TEMPLATE REWRITE
                # 153:3: -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st)
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
    # YarcParser.g:155:1: aug_expr_stmt : ( (id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) ) | model_expr[id] -> {$model_expr.st});
    def aug_expr_stmt(
        self,
    ):
        retval = self.aug_expr_stmt_return()
        retval.start = self.input.LT(1)

        op = None
        value = None
        id = None
        model_expr34 = None

        try:
            try:
                # YarcParser.g:155:14: ( (id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) ) | model_expr[id] -> {$model_expr.st})
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if LA54_0 in {
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
                    alt54 = 1
                elif LA54_0 in {CREATE, GET, GROUP, INSTANTIATE}:
                    alt54 = 2
                else:
                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae

                if alt54 == 1:
                    # YarcParser.g:155:16: (id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) )
                    pass
                    # YarcParser.g:155:16: (id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) )
                    # YarcParser.g:156:5: id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) )
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt2695
                    )
                    id = self.testlist()

                    self._state.following.pop()

                    # YarcParser.g:156:17: (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) )
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if LA53_0 == AUG_ASSIGN:
                        alt53 = 1
                    elif LA53_0 == ASSIGN:
                        alt53 = 2
                    else:
                        nvae = NoViableAltException("", 53, 0, self.input)

                        raise nvae

                    if alt53 == 1:
                        # YarcParser.g:157:7: op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE
                        op = self.match(
                            self.input,
                            AUG_ASSIGN,
                            self.FOLLOW_AUG_ASSIGN_in_aug_expr_stmt2707,
                        )

                        # YarcParser.g:157:27: ( testlist | fetch_expr )
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
                            # YarcParser.g:157:28: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt2712
                            )
                            value = self.testlist()

                            self._state.following.pop()

                        elif alt50 == 2:
                            # YarcParser.g:157:39: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt2716
                            )
                            value = self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_aug_expr_stmt2719,
                        )

                        # TEMPLATE REWRITE
                        # 157:59: -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)
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

                    elif alt53 == 2:
                        # YarcParser.g:158:9: op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st})
                        op = self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt2751
                        )

                        # YarcParser.g:158:19: (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st})
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if LA52_0 in {
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
                            alt52 = 1
                        elif LA52_0 in {CREATE, GET, GROUP, INSTANTIATE}:
                            alt52 = 2
                        else:
                            nvae = NoViableAltException("", 52, 0, self.input)

                            raise nvae

                        if alt52 == 1:
                            # YarcParser.g:159:9: value= ( testlist | fetch_expr ) NEWLINE
                            pass
                            # YarcParser.g:159:15: ( testlist | fetch_expr )
                            alt51 = 2
                            LA51_0 = self.input.LA(1)

                            if LA51_0 in {
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
                                alt51 = 1
                            elif LA51_0 == FETCH:
                                alt51 = 2
                            else:
                                nvae = NoViableAltException("", 51, 0, self.input)

                                raise nvae

                            if alt51 == 1:
                                # YarcParser.g:159:16: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt2766
                                )
                                value = self.testlist()

                                self._state.following.pop()

                            elif alt51 == 2:
                                # YarcParser.g:159:27: fetch_expr
                                self._state.following.append(
                                    self.FOLLOW_fetch_expr_in_aug_expr_stmt2770
                                )
                                value = self.fetch_expr()

                                self._state.following.pop()

                            self.match(
                                self.input,
                                NEWLINE,
                                self.FOLLOW_NEWLINE_in_aug_expr_stmt2773,
                            )

                            # TEMPLATE REWRITE
                            # 159:47: -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)
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

                        elif alt52 == 2:
                            # YarcParser.g:160:11: value= ( model_expr[$id.st] )
                            pass
                            # YarcParser.g:160:17: ( model_expr[$id.st] )
                            # YarcParser.g:160:18: model_expr[$id.st]
                            self._state.following.append(
                                self.FOLLOW_model_expr_in_aug_expr_stmt2808
                            )
                            value = self.model_expr(
                                ((id is not None) and [id.st] or [None])[0]
                            )

                            self._state.following.pop()

                            # TEMPLATE REWRITE
                            # 160:38: -> {$value.st}
                            retval.st = value.st

                elif alt54 == 2:
                    # YarcParser.g:164:5: model_expr[id]
                    pass
                    # action start
                    id = self.handler.get_random_uid()
                    # action end

                    self._state.following.append(
                        self.FOLLOW_model_expr_in_aug_expr_stmt2842
                    )
                    model_expr34 = self.model_expr(id)

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 164:57: -> {$model_expr.st}
                    retval.st = (
                        (model_expr34 is not None) and [model_expr34.st] or [None]
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
    # YarcParser.g:167:1: model_expr[id] : expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] ) -> {expr_.st};
    def model_expr(self, id):
        retval = self.model_expr_return()
        retval.start = self.input.LT(1)

        expr_ = None

        try:
            try:
                # YarcParser.g:167:15: (expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] ) -> {expr_.st})
                # YarcParser.g:167:17: expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] )
                pass
                # YarcParser.g:167:23: ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] )
                alt55 = 4
                LA55 = self.input.LA(1)
                if LA55 in {CREATE}:
                    alt55 = 1
                elif LA55 in {INSTANTIATE}:
                    alt55 = 2
                elif LA55 in {GET}:
                    alt55 = 3
                elif LA55 in {GROUP}:
                    alt55 = 4
                else:
                    nvae = NoViableAltException("", 55, 0, self.input)

                    raise nvae

                if alt55 == 1:
                    # YarcParser.g:167:24: create_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_model_expr2859
                    )
                    expr_ = self.create_expr(id)

                    self._state.following.pop()

                elif alt55 == 2:
                    # YarcParser.g:167:43: instantiate_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_model_expr2864
                    )
                    expr_ = self.instantiate_expr(id)

                    self._state.following.pop()

                elif alt55 == 3:
                    # YarcParser.g:167:67: get_expr[$id]
                    self._state.following.append(self.FOLLOW_get_expr_in_model_expr2869)
                    expr_ = self.get_expr(id)

                    self._state.following.pop()

                elif alt55 == 4:
                    # YarcParser.g:167:83: group_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_group_expr_in_model_expr2874
                    )
                    expr_ = self.group_expr(id)

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 167:100: -> {expr_.st}
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
    # YarcParser.g:169:1: fetch_expr : FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )? -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE);
    def fetch_expr(
        self,
    ):
        retval = self.fetch_expr_return()
        retval.start = self.input.LT(1)

        RECURSIVE35 = None
        ext = None
        path = None
        filter = None
        limit = None

        try:
            try:
                # YarcParser.g:169:12: ( FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )? -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE))
                # YarcParser.g:169:14: FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )?
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr2888)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr2892)
                ext = self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr2894)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr2898)
                path = self.test()

                self._state.following.pop()

                # YarcParser.g:169:44: ( MATCH filter= test )?
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if LA56_0 == MATCH:
                    alt56 = 1
                if alt56 == 1:
                    # YarcParser.g:169:45: MATCH filter= test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr2901)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr2905)
                    filter = self.test()

                    self._state.following.pop()

                # YarcParser.g:169:65: ( LIMIT limit= test )?
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if LA57_0 == LIMIT:
                    alt57 = 1
                if alt57 == 1:
                    # YarcParser.g:169:66: LIMIT limit= test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr2910)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr2914)
                    limit = self.test()

                    self._state.following.pop()

                # YarcParser.g:169:85: ( RECURSIVE )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if LA58_0 == RECURSIVE:
                    alt58 = 1
                if alt58 == 1:
                    # YarcParser.g:169:85: RECURSIVE
                    RECURSIVE35 = self.match(
                        self.input, RECURSIVE, self.FOLLOW_RECURSIVE_in_fetch_expr2918
                    )

                # TEMPLATE REWRITE
                # 170:3: -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE)
                retval.st = self.templateLib.getInstanceOf(
                    "fetch_expr",
                    attributes={
                        "ext": ((ext is not None) and [ext.st] or [None])[0],
                        "path": ((path is not None) and [path.st] or [None])[0],
                        "filter": ((filter is not None) and [filter.st] or [None])[0],
                        "limit": ((limit is not None) and [limit.st] or [None])[0],
                        "recursive": RECURSIVE35,
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
    # YarcParser.g:173:1: test : expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st);
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
                # YarcParser.g:173:13: (expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st))
                # YarcParser.g:173:15: expr_= or_test ( IF cond= or_test ELSE else_expr= test )?
                self._state.following.append(self.FOLLOW_or_test_in_test2969)
                expr_ = self.or_test()

                self._state.following.pop()

                # YarcParser.g:173:29: ( IF cond= or_test ELSE else_expr= test )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if LA59_0 == IF:
                    alt59 = 1
                if alt59 == 1:
                    # YarcParser.g:173:30: IF cond= or_test ELSE else_expr= test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test2972)

                    self._state.following.append(self.FOLLOW_or_test_in_test2976)
                    cond = self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test2978)

                    self._state.following.append(self.FOLLOW_test_in_test2982)
                    else_expr = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 174:13: -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st)
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
    # YarcParser.g:175:1: test_nocond : or_test -> test(expr=$or_test.st);
    def test_nocond(
        self,
    ):
        retval = self.test_nocond_return()
        retval.start = self.input.LT(1)

        or_test36 = None

        try:
            try:
                # YarcParser.g:175:13: ( or_test -> test(expr=$or_test.st))
                # YarcParser.g:175:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond3024)
                or_test36 = self.or_test()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 175:23: -> test(expr=$or_test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "test",
                    attributes={
                        "expr": ((or_test36 is not None) and [or_test36.st] or [None])[
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
    # YarcParser.g:176:1: or_test :exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs);
    def or_test(
        self,
    ):
        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:176:13: (exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs))
                # YarcParser.g:176:15: exprs+= and_test ( OR exprs+= and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test3046)
                exprs = self.and_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:176:31: ( OR exprs+= and_test )*
                while True:  # loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if LA60_0 == OR:
                        alt60 = 1

                    if alt60 == 1:
                        # YarcParser.g:176:32: OR exprs+= and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test3049)

                        self._state.following.append(
                            self.FOLLOW_and_test_in_or_test3053
                        )
                        exprs = self.and_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop60

                # TEMPLATE REWRITE
                # 176:53: -> or_test(exprs=$exprs)
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
    # YarcParser.g:177:1: and_test :exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs);
    def and_test(
        self,
    ):
        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:177:13: (exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs))
                # YarcParser.g:177:15: exprs+= not_test ( AND exprs+= not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test3076)
                exprs = self.not_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:177:31: ( AND exprs+= not_test )*
                while True:  # loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if LA61_0 == AND:
                        alt61 = 1

                    if alt61 == 1:
                        # YarcParser.g:177:32: AND exprs+= not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test3079)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test3083
                        )
                        exprs = self.not_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop61

                # TEMPLATE REWRITE
                # 177:54: -> and_test(exprs=$exprs)
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
    # YarcParser.g:178:1: not_test : ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st});
    def not_test(
        self,
    ):
        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        expr_ = None
        comparison37 = None

        try:
            try:
                # YarcParser.g:178:13: ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st})
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if LA62_0 == NOT:
                    alt62 = 1
                elif LA62_0 in {
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
                    alt62 = 2
                else:
                    nvae = NoViableAltException("", 62, 0, self.input)

                    raise nvae

                if alt62 == 1:
                    # YarcParser.g:178:15: NOT expr_= not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test3104)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test3108)
                    expr_ = self.not_test()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 178:35: -> not_test(expr=$expr_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "not_test",
                        attributes={
                            "expr": ((expr_ is not None) and [expr_.st] or [None])[0]
                        },
                    )

                elif alt62 == 2:
                    # YarcParser.g:179:15: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test3134)
                    comparison37 = self.comparison()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 179:26: -> {$comparison.st}
                    retval.st = (
                        (comparison37 is not None) and [comparison37.st] or [None]
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
    # YarcParser.g:180:1: comparison :exprs+= expr (ops+= comp_op exprs+= expr )* -> comparison(exprs=$exprsops=$ops);
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
                # YarcParser.g:180:13: (exprs+= expr (ops+= comp_op exprs+= expr )* -> comparison(exprs=$exprsops=$ops))
                # YarcParser.g:180:15: exprs+= expr (ops+= comp_op exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison3148)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:180:27: (ops+= comp_op exprs+= expr )*
                while True:  # loop63
                    alt63 = 2
                    LA63_0 = self.input.LA(1)

                    if LA63_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt63 = 1

                    if alt63 == 1:
                        # YarcParser.g:180:28: ops+= comp_op exprs+= expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison3153
                        )
                        ops = self.comp_op()

                        self._state.following.pop()
                        if list_ops is None:
                            list_ops = []
                        list_ops.append(ops.st)

                        self._state.following.append(self.FOLLOW_expr_in_comparison3157)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop63

                # TEMPLATE REWRITE
                # 180:55: -> comparison(exprs=$exprsops=$ops)
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
    # YarcParser.g:181:1: comp_op : op= ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT ) -> {$op};
    def comp_op(
        self,
    ):
        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        op = None

        try:
            try:
                # YarcParser.g:181:13: (op= ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT ) -> {$op})
                # YarcParser.g:181:15: op= ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                pass
                # YarcParser.g:181:18: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                alt64 = 10
                LA64 = self.input.LA(1)
                if LA64 in {LT}:
                    alt64 = 1
                elif LA64 in {GT}:
                    alt64 = 2
                elif LA64 in {EQUALS}:
                    alt64 = 3
                elif LA64 in {GT_EQ}:
                    alt64 = 4
                elif LA64 in {LT_EQ}:
                    alt64 = 5
                elif LA64 in {NOT_EQ}:
                    alt64 = 6
                elif LA64 in {IN}:
                    alt64 = 7
                elif LA64 in {NOT}:
                    alt64 = 8
                elif LA64 in {IS}:
                    LA64_9 = self.input.LA(2)

                    if LA64_9 == NOT:
                        alt64 = 10
                    elif LA64_9 in {
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
                        alt64 = 9
                    else:
                        nvae = NoViableAltException("", 64, 9, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 64, 0, self.input)

                    raise nvae

                if alt64 == 1:
                    # YarcParser.g:181:19: LT
                    op = self.match(self.input, LT, self.FOLLOW_LT_in_comp_op3187)

                elif alt64 == 2:
                    # YarcParser.g:181:24: GT
                    op = self.match(self.input, GT, self.FOLLOW_GT_in_comp_op3191)

                elif alt64 == 3:
                    # YarcParser.g:181:29: EQUALS
                    op = self.match(
                        self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op3195
                    )

                elif alt64 == 4:
                    # YarcParser.g:181:38: GT_EQ
                    op = self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op3199)

                elif alt64 == 5:
                    # YarcParser.g:181:46: LT_EQ
                    op = self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op3203)

                elif alt64 == 6:
                    # YarcParser.g:181:54: NOT_EQ
                    op = self.match(
                        self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op3207
                    )

                elif alt64 == 7:
                    # YarcParser.g:181:63: IN
                    op = self.match(self.input, IN, self.FOLLOW_IN_in_comp_op3211)

                elif alt64 == 8:
                    # YarcParser.g:181:68: NOT IN
                    op = self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op3215)

                    op = self.match(self.input, IN, self.FOLLOW_IN_in_comp_op3217)

                elif alt64 == 9:
                    # YarcParser.g:181:77: IS
                    op = self.match(self.input, IS, self.FOLLOW_IS_in_comp_op3221)

                elif alt64 == 10:
                    # YarcParser.g:181:82: IS NOT
                    op = self.match(self.input, IS, self.FOLLOW_IS_in_comp_op3225)

                    op = self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op3227)

                # TEMPLATE REWRITE
                # 181:90: -> {$op}
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
    # YarcParser.g:182:1: expr :exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs);
    def expr(
        self,
    ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:182:13: (exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs))
                # YarcParser.g:182:15: exprs+= xor_expr ( BIT_OR exprs+= xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr3248)
                exprs = self.xor_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:182:31: ( BIT_OR exprs+= xor_expr )*
                while True:  # loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if LA65_0 == BIT_OR:
                        alt65 = 1

                    if alt65 == 1:
                        # YarcParser.g:182:32: BIT_OR exprs+= xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr3251)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr3255)
                        exprs = self.xor_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop65

                # TEMPLATE REWRITE
                # 182:57: -> expr(exprs=$exprs)
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
    # YarcParser.g:183:1: xor_expr :exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs);
    def xor_expr(
        self,
    ):
        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:183:13: (exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs))
                # YarcParser.g:183:15: exprs+= and_expr ( XOR exprs+= and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr3278)
                exprs = self.and_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:183:31: ( XOR exprs+= and_expr )*
                while True:  # loop66
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if LA66_0 == XOR:
                        alt66 = 1

                    if alt66 == 1:
                        # YarcParser.g:183:32: XOR exprs+= and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr3281)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr3285
                        )
                        exprs = self.and_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop66

                # TEMPLATE REWRITE
                # 183:54: -> xor_expr(exprs=$exprs)
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
    # YarcParser.g:184:1: and_expr :exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs);
    def and_expr(
        self,
    ):
        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:184:13: (exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs))
                # YarcParser.g:184:15: exprs+= shift_expr ( BIT_AND exprs+= shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr3308)
                exprs = self.shift_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:184:33: ( BIT_AND exprs+= shift_expr )*
                while True:  # loop67
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if LA67_0 == BIT_AND:
                        alt67 = 1

                    if alt67 == 1:
                        # YarcParser.g:184:34: BIT_AND exprs+= shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr3311
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr3315
                        )
                        exprs = self.shift_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop67

                # TEMPLATE REWRITE
                # 184:62: -> and_expr(exprs=$exprs)
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
    # YarcParser.g:185:1: shift_expr :exprs+= arith_expr (ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsops=$ops);
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
                # YarcParser.g:185:13: (exprs+= arith_expr (ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsops=$ops))
                # YarcParser.g:185:15: exprs+= arith_expr (ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr3336)
                exprs = self.arith_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:185:33: (ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                while True:  # loop69
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if LA69_0 in {LSHIFT, RSHIFT}:
                        alt69 = 1

                    if alt69 == 1:
                        # YarcParser.g:185:34: ops+= ( LSHIFT | RSHIFT ) exprs+= arith_expr
                        pass
                        # YarcParser.g:185:39: ( LSHIFT | RSHIFT )
                        alt68 = 2
                        LA68_0 = self.input.LA(1)

                        if LA68_0 == LSHIFT:
                            alt68 = 1
                        elif LA68_0 == RSHIFT:
                            alt68 = 2
                        else:
                            nvae = NoViableAltException("", 68, 0, self.input)

                            raise nvae

                        if alt68 == 1:
                            # YarcParser.g:185:40: LSHIFT
                            ops = self.match(
                                self.input, LSHIFT, self.FOLLOW_LSHIFT_in_shift_expr3342
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt68 == 2:
                            # YarcParser.g:185:49: RSHIFT
                            ops = self.match(
                                self.input, RSHIFT, self.FOLLOW_RSHIFT_in_shift_expr3346
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr3351
                        )
                        exprs = self.arith_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop69

                # TEMPLATE REWRITE
                # 185:77: -> shift_expr(exprs=$exprsops=$ops)
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
    # YarcParser.g:186:1: arith_expr :terms+= term (ops+= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsops=$ops);
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
                # YarcParser.g:186:13: (terms+= term (ops+= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsops=$ops))
                # YarcParser.g:186:15: terms+= term (ops+= ( PLUS | MINUS ) terms+= term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr3377)
                terms = self.term()

                self._state.following.pop()
                if list_terms is None:
                    list_terms = []
                list_terms.append(terms.st)

                # YarcParser.g:186:27: (ops+= ( PLUS | MINUS ) terms+= term )*
                while True:  # loop71
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if LA71_0 in {MINUS, PLUS}:
                        alt71 = 1

                    if alt71 == 1:
                        # YarcParser.g:186:28: ops+= ( PLUS | MINUS ) terms+= term
                        pass
                        # YarcParser.g:186:33: ( PLUS | MINUS )
                        alt70 = 2
                        LA70_0 = self.input.LA(1)

                        if LA70_0 == PLUS:
                            alt70 = 1
                        elif LA70_0 == MINUS:
                            alt70 = 2
                        else:
                            nvae = NoViableAltException("", 70, 0, self.input)

                            raise nvae

                        if alt70 == 1:
                            # YarcParser.g:186:34: PLUS
                            ops = self.match(
                                self.input, PLUS, self.FOLLOW_PLUS_in_arith_expr3383
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt70 == 2:
                            # YarcParser.g:186:41: MINUS
                            ops = self.match(
                                self.input, MINUS, self.FOLLOW_MINUS_in_arith_expr3387
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        self._state.following.append(self.FOLLOW_term_in_arith_expr3392)
                        terms = self.term()

                        self._state.following.pop()
                        if list_terms is None:
                            list_terms = []
                        list_terms.append(terms.st)

                    else:
                        break  # loop71

                # TEMPLATE REWRITE
                # 186:62: -> arith_expr(terms=$termsops=$ops)
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
    # YarcParser.g:187:1: term :factors+= factor (ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsops=$ops);
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
                # YarcParser.g:187:13: (factors+= factor (ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsops=$ops))
                # YarcParser.g:187:15: factors+= factor (ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                self._state.following.append(self.FOLLOW_factor_in_term3424)
                factors = self.factor()

                self._state.following.pop()
                if list_factors is None:
                    list_factors = []
                list_factors.append(factors.st)

                # YarcParser.g:187:31: (ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                while True:  # loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if LA73_0 in {DIV, IDIV, MOD, MUL}:
                        alt73 = 1

                    if alt73 == 1:
                        # YarcParser.g:187:32: ops+= ( MUL | DIV | MOD | IDIV ) factors+= factor
                        pass
                        # YarcParser.g:187:37: ( MUL | DIV | MOD | IDIV )
                        alt72 = 4
                        LA72 = self.input.LA(1)
                        if LA72 in {MUL}:
                            alt72 = 1
                        elif LA72 in {DIV}:
                            alt72 = 2
                        elif LA72 in {MOD}:
                            alt72 = 3
                        elif LA72 in {IDIV}:
                            alt72 = 4
                        else:
                            nvae = NoViableAltException("", 72, 0, self.input)

                            raise nvae

                        if alt72 == 1:
                            # YarcParser.g:187:38: MUL
                            ops = self.match(
                                self.input, MUL, self.FOLLOW_MUL_in_term3430
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt72 == 2:
                            # YarcParser.g:187:44: DIV
                            ops = self.match(
                                self.input, DIV, self.FOLLOW_DIV_in_term3434
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt72 == 3:
                            # YarcParser.g:187:50: MOD
                            ops = self.match(
                                self.input, MOD, self.FOLLOW_MOD_in_term3438
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        elif alt72 == 4:
                            # YarcParser.g:187:56: IDIV
                            ops = self.match(
                                self.input, IDIV, self.FOLLOW_IDIV_in_term3442
                            )
                            if list_ops is None:
                                list_ops = []
                            list_ops.append(ops)

                        self._state.following.append(self.FOLLOW_factor_in_term3447)
                        factors = self.factor()

                        self._state.following.pop()
                        if list_factors is None:
                            list_factors = []
                        list_factors.append(factors.st)

                    else:
                        break  # loop73

                # TEMPLATE REWRITE
                # 187:80: -> term(factors=$factorsops=$ops)
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
    # YarcParser.g:188:1: factor : (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st});
    def factor(
        self,
    ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)

        prefix = None
        factor_ = None
        power38 = None

        try:
            try:
                # YarcParser.g:188:13: (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st})
                alt75 = 2
                LA75_0 = self.input.LA(1)

                if LA75_0 in {BIT_NOT, MINUS, PLUS}:
                    alt75 = 1
                elif LA75_0 in {
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
                    alt75 = 2
                else:
                    nvae = NoViableAltException("", 75, 0, self.input)

                    raise nvae

                if alt75 == 1:
                    # YarcParser.g:188:15: prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor
                    pass
                    # YarcParser.g:188:22: ( PLUS | MINUS | BIT_NOT )
                    alt74 = 3
                    LA74 = self.input.LA(1)
                    if LA74 in {PLUS}:
                        alt74 = 1
                    elif LA74 in {MINUS}:
                        alt74 = 2
                    elif LA74 in {BIT_NOT}:
                        alt74 = 3
                    else:
                        nvae = NoViableAltException("", 74, 0, self.input)

                        raise nvae

                    if alt74 == 1:
                        # YarcParser.g:188:23: PLUS
                        prefix = self.match(
                            self.input, PLUS, self.FOLLOW_PLUS_in_factor3478
                        )

                    elif alt74 == 2:
                        # YarcParser.g:188:30: MINUS
                        prefix = self.match(
                            self.input, MINUS, self.FOLLOW_MINUS_in_factor3482
                        )

                    elif alt74 == 3:
                        # YarcParser.g:188:38: BIT_NOT
                        prefix = self.match(
                            self.input, BIT_NOT, self.FOLLOW_BIT_NOT_in_factor3486
                        )

                    self._state.following.append(self.FOLLOW_factor_in_factor3491)
                    factor_ = self.factor()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 188:62: -> prefix_factor(factor=$factor_.stprefix=$prefix)
                    retval.st = self.templateLib.getInstanceOf(
                        "prefix_factor",
                        attributes={
                            "factor": (
                                (factor_ is not None) and [factor_.st] or [None]
                            )[0],
                            "prefix": prefix,
                        },
                    )

                elif alt75 == 2:
                    # YarcParser.g:189:15: power
                    self._state.following.append(self.FOLLOW_power_in_factor3521)
                    power38 = self.power()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 189:21: -> {$power.st}
                    retval.st = ((power38 is not None) and [power38.st] or [None])[0]

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
    # YarcParser.g:190:1: power : atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st);
    def power(
        self,
    ):
        retval = self.power_return()
        retval.start = self.input.LT(1)

        atom_expr39 = None
        factor40 = None

        try:
            try:
                # YarcParser.g:190:13: ( atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st))
                # YarcParser.g:190:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power3538)
                atom_expr39 = self.atom_expr()

                self._state.following.pop()

                # YarcParser.g:190:25: ( POWER factor )?
                alt76 = 2
                LA76_0 = self.input.LA(1)

                if LA76_0 == POWER:
                    alt76 = 1
                if alt76 == 1:
                    # YarcParser.g:190:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power3541)

                    self._state.following.append(self.FOLLOW_factor_in_power3543)
                    factor40 = self.factor()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 190:41: -> power(atom=$atom_expr.stfactor=$factor.st)
                retval.st = self.templateLib.getInstanceOf(
                    "power",
                    attributes={
                        "atom": (
                            (atom_expr39 is not None) and [atom_expr39.st] or [None]
                        )[0],
                        "factor": ((factor40 is not None) and [factor40.st] or [None])[
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
    # YarcParser.g:191:1: atom_expr : atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers);
    def atom_expr(
        self,
    ):
        retval = self.atom_expr_return()
        retval.start = self.input.LT(1)

        list_trailers = None
        atom41 = None
        trailers = None
        try:
            try:
                # YarcParser.g:191:13: ( atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers))
                # YarcParser.g:191:15: atom (trailers+= trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr3568)
                atom41 = self.atom()

                self._state.following.pop()

                # YarcParser.g:191:20: (trailers+= trailer )*
                while True:  # loop77
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if LA77_0 in {DOT, LBRACK}:
                        alt77 = 1

                    if alt77 == 1:
                        # YarcParser.g:191:21: trailers+= trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr3573
                        )
                        trailers = self.trailer()

                        self._state.following.pop()
                        if list_trailers is None:
                            list_trailers = []
                        list_trailers.append(trailers.st)

                    else:
                        break  # loop77

                # TEMPLATE REWRITE
                # 191:41: -> atom_expr(atom=$atom.sttrailers=$trailers)
                retval.st = self.templateLib.getInstanceOf(
                    "atom_expr",
                    attributes={
                        "atom": ((atom41 is not None) and [atom41.st] or [None])[0],
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
    # YarcParser.g:192:1: atom : ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| distribution -> {$distribution.st}| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {self.handler.expand_string($STRING)}| NONE -> null(| TRUE -> true(| FALSE -> false() ;
    def atom(
        self,
    ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)

        SETTING_ID46 = None
        INTEGER48 = None
        FLOAT_NUMBER49 = None
        STRING50 = None
        test_ = None
        testlist_comp42 = None
        vector_comp43 = None
        dict_or_set_maker44 = None
        name45 = None
        distribution47 = None

        try:
            try:
                # YarcParser.g:192:5: ( ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| distribution -> {$distribution.st}| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {self.handler.expand_string($STRING)}| NONE -> null(| TRUE -> true(| FALSE -> false() )
                # YarcParser.g:193:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| distribution -> {$distribution.st}| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {self.handler.expand_string($STRING)}| NONE -> null(| TRUE -> true(| FALSE -> false()
                pass
                # YarcParser.g:193:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| distribution -> {$distribution.st}| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {self.handler.expand_string($STRING)}| NONE -> null(| TRUE -> true(| FALSE -> false()
                alt81 = 14
                LA81 = self.input.LA(1)
                if LA81 in {LPAREN}:
                    alt81 = 1
                elif LA81 in {LBRACK}:
                    alt81 = 2
                elif LA81 in {LT}:
                    alt81 = 3
                elif LA81 in {LBRACE}:
                    alt81 = 4
                elif LA81 in {LEN}:
                    alt81 = 5
                elif LA81 in {ID, UNDERSCORE}:
                    alt81 = 6
                elif LA81 in {SETTING_ID}:
                    alt81 = 7
                elif LA81 in {COMBINE, DISTRIBUTION}:
                    alt81 = 8
                elif LA81 in {INTEGER}:
                    alt81 = 9
                elif LA81 in {FLOAT_NUMBER}:
                    alt81 = 10
                elif LA81 in {STRING}:
                    alt81 = 11
                elif LA81 in {NONE}:
                    alt81 = 12
                elif LA81 in {TRUE}:
                    alt81 = 13
                elif LA81 in {FALSE}:
                    alt81 = 14
                else:
                    nvae = NoViableAltException("", 81, 0, self.input)

                    raise nvae

                if alt81 == 1:
                    # YarcParser.g:193:4: LPAREN test_= test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom3598)

                    self._state.following.append(self.FOLLOW_test_in_atom3602)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom3604)

                    # TEMPLATE REWRITE
                    # 193:29: -> parenthesized_expr(expr=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "parenthesized_expr",
                        attributes={
                            "expr": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt81 == 2:
                    # YarcParser.g:194:5: LBRACK ( testlist_comp )? RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom3619)

                    # YarcParser.g:194:12: ( testlist_comp )?
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
                        NOT,
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt78 = 1
                    if alt78 == 1:
                        # YarcParser.g:194:12: testlist_comp
                        self._state.following.append(
                            self.FOLLOW_testlist_comp_in_atom3621
                        )
                        testlist_comp42 = self.testlist_comp()

                        self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom3624)

                    # TEMPLATE REWRITE
                    # 194:34: -> list(list_comp=$testlist_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list",
                        attributes={
                            "list_comp": (
                                (testlist_comp42 is not None)
                                and [testlist_comp42.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt81 == 3:
                    # YarcParser.g:195:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom3639)

                    # YarcParser.g:195:8: ( vector_comp )?
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
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt79 = 1
                    if alt79 == 1:
                        # YarcParser.g:195:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom3641
                        )
                        vector_comp43 = self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom3644)

                    # TEMPLATE REWRITE
                    # 195:24: -> vector(values=$vector_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "vector",
                        attributes={
                            "values": (
                                (vector_comp43 is not None)
                                and [vector_comp43.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt81 == 4:
                    # YarcParser.g:196:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom3659)

                    # YarcParser.g:196:12: ( dict_or_set_maker )?
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if LA80_0 in {
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
                        alt80 = 1
                    if alt80 == 1:
                        # YarcParser.g:196:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom3661
                        )
                        dict_or_set_maker44 = self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom3664)

                    # TEMPLATE REWRITE
                    # 196:38: -> dict(dict_comp=$dict_or_set_maker.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dict",
                        attributes={
                            "dict_comp": (
                                (dict_or_set_maker44 is not None)
                                and [dict_or_set_maker44.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt81 == 5:
                    # YarcParser.g:197:5: LEN LPAREN test_= test RPAREN
                    self.match(self.input, LEN, self.FOLLOW_LEN_in_atom3679)

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom3681)

                    self._state.following.append(self.FOLLOW_test_in_atom3685)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom3687)

                    # TEMPLATE REWRITE
                    # 197:34: -> len(value=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "len",
                        attributes={
                            "value": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt81 == 6:
                    # YarcParser.g:198:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom3702)
                    name45 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 198:10: -> {$name.st}
                    retval.st = ((name45 is not None) and [name45.st] or [None])[0]

                elif alt81 == 7:
                    # YarcParser.g:199:5: SETTING_ID
                    SETTING_ID46 = self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom3712
                    )

                    # TEMPLATE REWRITE
                    # 199:16: -> setting_id(id=$SETTING_ID.text)
                    retval.st = self.templateLib.getInstanceOf(
                        "setting_id", attributes={"id": SETTING_ID46.text}
                    )

                elif alt81 == 8:
                    # YarcParser.g:200:5: distribution
                    self._state.following.append(self.FOLLOW_distribution_in_atom3728)
                    distribution47 = self.distribution()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 200:18: -> {$distribution.st}
                    retval.st = (
                        (distribution47 is not None) and [distribution47.st] or [None]
                    )[0]

                elif alt81 == 9:
                    # YarcParser.g:201:5: INTEGER
                    INTEGER48 = self.match(
                        self.input, INTEGER, self.FOLLOW_INTEGER_in_atom3738
                    )

                    # TEMPLATE REWRITE
                    # 201:13: -> {$INTEGER.text}
                    retval.st = INTEGER48.text

                elif alt81 == 10:
                    # YarcParser.g:202:5: FLOAT_NUMBER
                    FLOAT_NUMBER49 = self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom3748
                    )

                    # TEMPLATE REWRITE
                    # 202:18: -> {$FLOAT_NUMBER.text}
                    retval.st = FLOAT_NUMBER49.text

                elif alt81 == 11:
                    # YarcParser.g:203:5: STRING
                    STRING50 = self.match(
                        self.input, STRING, self.FOLLOW_STRING_in_atom3758
                    )

                    # TEMPLATE REWRITE
                    # 203:12: -> {self.handler.expand_string($STRING)}
                    retval.st = self.handler.expand_string(STRING50)

                elif alt81 == 12:
                    # YarcParser.g:204:5: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom3769)

                    # TEMPLATE REWRITE
                    # 204:10: -> null(
                    retval.st = self.templateLib.getInstanceOf("null")

                elif alt81 == 13:
                    # YarcParser.g:205:5: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom3781)

                    # TEMPLATE REWRITE
                    # 205:10: -> true(
                    retval.st = self.templateLib.getInstanceOf("true")

                elif alt81 == 14:
                    # YarcParser.g:206:5: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom3793)

                    # TEMPLATE REWRITE
                    # 206:11: -> false(
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
    # YarcParser.g:210:1: name : ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text});
    def name(
        self,
    ):
        retval = self.name_return()
        retval.start = self.input.LT(1)

        ID51 = None
        UNDERSCORE52 = None

        try:
            try:
                # YarcParser.g:210:5: ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text})
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if LA82_0 == ID:
                    alt82 = 1
                elif LA82_0 == UNDERSCORE:
                    alt82 = 2
                else:
                    nvae = NoViableAltException("", 82, 0, self.input)

                    raise nvae

                if alt82 == 1:
                    # YarcParser.g:211:3: ID
                    ID51 = self.match(self.input, ID, self.FOLLOW_ID_in_name3813)

                    # TEMPLATE REWRITE
                    # 211:6: -> {$ID.text}
                    retval.st = ID51.text

                elif alt82 == 2:
                    # YarcParser.g:212:5: UNDERSCORE
                    UNDERSCORE52 = self.match(
                        self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_name3823
                    )

                    # TEMPLATE REWRITE
                    # 212:16: -> {$UNDERSCORE.text}
                    retval.st = UNDERSCORE52.text

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
    # YarcParser.g:223:1: distribution : ( DISTRIBUTION LPAREN args= arglist RPAREN -> distribution(name=self.handler.map($DISTRIBUTION)arglist=$args.st)| COMBINE LPAREN args= arglist RPAREN -> combined_distribution(distrs=$args.st));
    def distribution(
        self,
    ):
        retval = self.distribution_return()
        retval.start = self.input.LT(1)

        DISTRIBUTION53 = None
        args = None

        try:
            try:
                # YarcParser.g:223:14: ( DISTRIBUTION LPAREN args= arglist RPAREN -> distribution(name=self.handler.map($DISTRIBUTION)arglist=$args.st)| COMBINE LPAREN args= arglist RPAREN -> combined_distribution(distrs=$args.st))
                alt83 = 2
                LA83_0 = self.input.LA(1)

                if LA83_0 == DISTRIBUTION:
                    alt83 = 1
                elif LA83_0 == COMBINE:
                    alt83 = 2
                else:
                    nvae = NoViableAltException("", 83, 0, self.input)

                    raise nvae

                if alt83 == 1:
                    # YarcParser.g:223:16: DISTRIBUTION LPAREN args= arglist RPAREN
                    DISTRIBUTION53 = self.match(
                        self.input,
                        DISTRIBUTION,
                        self.FOLLOW_DISTRIBUTION_in_distribution3840,
                    )

                    self.match(
                        self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution3842
                    )

                    self._state.following.append(
                        self.FOLLOW_arglist_in_distribution3846
                    )
                    args = self.arglist()

                    self._state.following.pop()

                    self.match(
                        self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution3848
                    )

                    # TEMPLATE REWRITE
                    # 223:56: -> distribution(name=self.handler.map($DISTRIBUTION)arglist=$args.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "distribution",
                        attributes={
                            "name": self.handler.map(DISTRIBUTION53),
                            "arglist": ((args is not None) and [args.st] or [None])[0],
                        },
                    )

                elif alt83 == 2:
                    # YarcParser.g:224:18: COMBINE LPAREN args= arglist RPAREN
                    self.match(
                        self.input, COMBINE, self.FOLLOW_COMBINE_in_distribution3881
                    )

                    self.match(
                        self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution3883
                    )

                    self._state.following.append(
                        self.FOLLOW_arglist_in_distribution3887
                    )
                    args = self.arglist()

                    self._state.following.pop()

                    self.match(
                        self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution3889
                    )

                    # TEMPLATE REWRITE
                    # 224:53: -> combined_distribution(distrs=$args.st)
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
    # YarcParser.g:226:1: testlist_comp :exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) ;
    def testlist_comp(
        self,
    ):
        retval = self.testlist_comp_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        to = None
        step = None
        comp_for54 = None
        exprs = None
        try:
            try:
                # YarcParser.g:226:15: (exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) )
                # YarcParser.g:226:18: exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                self._state.following.append(self.FOLLOW_test_in_testlist_comp3910)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:226:30: ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                alt86 = 3
                LA86 = self.input.LA(1)
                if LA86 in {FOR}:
                    alt86 = 1
                elif LA86 in {COMMA, RBRACK}:
                    alt86 = 2
                elif LA86 in {RANGE}:
                    alt86 = 3
                else:
                    nvae = NoViableAltException("", 86, 0, self.input)

                    raise nvae

                if alt86 == 1:
                    # YarcParser.g:226:32: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp3914
                    )
                    comp_for54 = self.comp_for()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 226:41: -> list_comp(expr=$exprs[0]for=$comp_for.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list_comp",
                        attributes={
                            "expr": list_exprs[0],
                            "for": (
                                (comp_for54 is not None) and [comp_for54.st] or [None]
                            )[0],
                        },
                    )

                elif alt86 == 2:
                    # YarcParser.g:227:32: ( COMMA exprs+= test )*
                    pass
                    # YarcParser.g:227:32: ( COMMA exprs+= test )*
                    while True:  # loop84
                        alt84 = 2
                        LA84_0 = self.input.LA(1)

                        if LA84_0 == COMMA:
                            alt84 = 1

                        if alt84 == 1:
                            # YarcParser.g:227:33: COMMA exprs+= test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp3962,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp3966
                            )
                            exprs = self.test()

                            self._state.following.pop()
                            if list_exprs is None:
                                list_exprs = []
                            list_exprs.append(exprs.st)

                        else:
                            break  # loop84

                    # TEMPLATE REWRITE
                    # 227:53: -> test_list(exprs=$exprs)
                    retval.st = self.templateLib.getInstanceOf(
                        "test_list", attributes={"exprs": list_exprs}
                    )

                elif alt86 == 3:
                    # YarcParser.g:228:32: RANGE to= test ( STEP step= test )?
                    self.match(
                        self.input, RANGE, self.FOLLOW_RANGE_in_testlist_comp4010
                    )

                    self._state.following.append(self.FOLLOW_test_in_testlist_comp4014)
                    to = self.test()

                    self._state.following.pop()

                    # YarcParser.g:228:46: ( STEP step= test )?
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if LA85_0 == STEP:
                        alt85 = 1
                    if alt85 == 1:
                        # YarcParser.g:228:47: STEP step= test
                        self.match(
                            self.input, STEP, self.FOLLOW_STEP_in_testlist_comp4017
                        )

                        self._state.following.append(
                            self.FOLLOW_test_in_testlist_comp4021
                        )
                        step = self.test()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 228:64: -> range(from=$exprs[0]to=$to.ststep=$step.st)
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
    # YarcParser.g:231:1: vector_comp : x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st);
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
                # YarcParser.g:231:15: (x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st))
                # YarcParser.g:231:17: x= expr COMMA y= expr COMMA z= expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp4085)
                x = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp4087)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp4091)
                y = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp4093)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp4097)
                z = self.expr()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 231:50: -> vector_comp(x=$x.sty=$y.stz=$z.st)
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
    # YarcParser.g:233:1: trailer : ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st));
    def trailer(
        self,
    ):
        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        subscriptlist55 = None
        name56 = None

        try:
            try:
                # YarcParser.g:233:15: ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st))
                alt87 = 2
                LA87_0 = self.input.LA(1)

                if LA87_0 == LBRACK:
                    alt87 = 1
                elif LA87_0 == DOT:
                    alt87 = 2
                else:
                    nvae = NoViableAltException("", 87, 0, self.input)

                    raise nvae

                if alt87 == 1:
                    # YarcParser.g:233:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer4131)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer4133
                    )
                    subscriptlist55 = self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer4135)

                    # TEMPLATE REWRITE
                    # 233:45: -> index(index=$subscriptlist.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "index",
                        attributes={
                            "index": (
                                (subscriptlist55 is not None)
                                and [subscriptlist55.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt87 == 2:
                    # YarcParser.g:234:17: DOT name
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer4163)

                    self._state.following.append(self.FOLLOW_name_in_trailer4165)
                    name56 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 234:26: -> dot_attr(attr=$name.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dot_attr",
                        attributes={
                            "attr": ((name56 is not None) and [name56.st] or [None])[0]
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
    # YarcParser.g:235:1: arglist :args+= argument ( COMMA args+= argument )* -> arg_list(args=$args);
    def arglist(
        self,
    ):
        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        list_args = None
        args = None
        try:
            try:
                # YarcParser.g:235:15: (args+= argument ( COMMA args+= argument )* -> arg_list(args=$args))
                # YarcParser.g:235:17: args+= argument ( COMMA args+= argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist4189)
                args = self.argument()

                self._state.following.pop()
                if list_args is None:
                    list_args = []
                list_args.append(args.st)

                # YarcParser.g:235:32: ( COMMA args+= argument )*
                while True:  # loop88
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if LA88_0 == COMMA:
                        alt88 = 1

                    if alt88 == 1:
                        # YarcParser.g:235:33: COMMA args+= argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist4192)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist4196
                        )
                        args = self.argument()

                        self._state.following.pop()
                        if list_args is None:
                            list_args = []
                        list_args.append(args.st)

                    else:
                        break  # loop88

                # TEMPLATE REWRITE
                # 235:56: -> arg_list(args=$args)
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
    # YarcParser.g:236:1: argument : kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st);
    def argument(
        self,
    ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)

        kw_or_arg = None
        arg = None

        try:
            try:
                # YarcParser.g:236:15: (kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st))
                # YarcParser.g:236:17: kw_or_arg= test ( ASSIGN arg= test )?
                self._state.following.append(self.FOLLOW_test_in_argument4221)
                kw_or_arg = self.test()

                self._state.following.pop()

                # YarcParser.g:236:32: ( ASSIGN arg= test )?
                alt89 = 2
                LA89_0 = self.input.LA(1)

                if LA89_0 == ASSIGN:
                    alt89 = 1
                if alt89 == 1:
                    # YarcParser.g:236:33: ASSIGN arg= test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument4224)

                    self._state.following.append(self.FOLLOW_test_in_argument4228)
                    arg = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 236:51: -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st)
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
    # YarcParser.g:237:1: subscriptlist :subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs);
    def subscriptlist(
        self,
    ):
        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        list_subs = None
        subs = None
        try:
            try:
                # YarcParser.g:237:15: (subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs))
                # YarcParser.g:237:17: subs+= subscript_ ( COMMA subs+= subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist4253
                )
                subs = self.subscript_()

                self._state.following.pop()
                if list_subs is None:
                    list_subs = []
                list_subs.append(subs.st)

                # YarcParser.g:237:34: ( COMMA subs+= subscript_ )*
                while True:  # loop90
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if LA90_0 == COMMA:
                        alt90 = 1

                    if alt90 == 1:
                        # YarcParser.g:237:35: COMMA subs+= subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist4256
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist4260
                        )
                        subs = self.subscript_()

                        self._state.following.pop()
                        if list_subs is None:
                            list_subs = []
                        list_subs.append(subs.st)

                    else:
                        break  # loop90

                # TEMPLATE REWRITE
                # 237:60: -> subscript_list(subs=$subs)
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
    # YarcParser.g:238:1: subscript_ : (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st));
    def subscript_(
        self,
    ):
        retval = self.subscript__return()
        retval.start = self.input.LT(1)

        to = None
        step = None
        COLON57 = None
        COLON58 = None
        from_ = None

        try:
            try:
                # YarcParser.g:238:15: (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st))
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
                elif LA96_0 == COLON:
                    alt96 = 2
                else:
                    nvae = NoViableAltException("", 96, 0, self.input)

                    raise nvae

                if alt96 == 1:
                    # YarcParser.g:238:17: from_= test ( COLON to= ( test )? step= ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_4283)
                    from_ = self.test()

                    self._state.following.pop()

                    # YarcParser.g:238:28: ( COLON to= ( test )? step= ( sliceop )? )?
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if LA93_0 == COLON:
                        alt93 = 1
                    if alt93 == 1:
                        # YarcParser.g:238:29: COLON to= ( test )? step= ( sliceop )?
                        COLON57 = self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_4286
                        )

                        # YarcParser.g:238:38: ( test )?
                        alt91 = 2
                        LA91_0 = self.input.LA(1)

                        if LA91_0 in {
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
                            alt91 = 1
                        if alt91 == 1:
                            # YarcParser.g:238:39: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_4291
                            )
                            to = self.test()

                            self._state.following.pop()

                        # YarcParser.g:238:51: ( sliceop )?
                        alt92 = 2
                        LA92_0 = self.input.LA(1)

                        if LA92_0 == COLON:
                            alt92 = 1
                        if alt92 == 1:
                            # YarcParser.g:238:52: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_4298
                            )
                            step = self.sliceop()

                            self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 238:64: -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={
                            "from": ((from_ is not None) and [from_.st] or [None])[0],
                            "colon": COLON57,
                            "to": to.st,
                            "step": step.st,
                        },
                    )

                elif alt96 == 2:
                    # YarcParser.g:239:17: COLON to= ( test )? step= ( sliceop )?
                    COLON58 = self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_subscript_4344
                    )

                    # YarcParser.g:239:26: ( test )?
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if LA94_0 in {
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
                        alt94 = 1
                    if alt94 == 1:
                        # YarcParser.g:239:27: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_4349)
                        to = self.test()

                        self._state.following.pop()

                    # YarcParser.g:239:39: ( sliceop )?
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if LA95_0 == COLON:
                        alt95 = 1
                    if alt95 == 1:
                        # YarcParser.g:239:40: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_4356
                        )
                        step = self.sliceop()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 239:51: -> subscript(colon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={"colon": COLON58, "to": to.st, "step": step.st},
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
    # YarcParser.g:240:1: sliceop : COLON ( test )? -> subscipt_step(step=$test.st);
    def sliceop(
        self,
    ):
        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        test59 = None

        try:
            try:
                # YarcParser.g:240:15: ( COLON ( test )? -> subscipt_step(step=$test.st))
                # YarcParser.g:240:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop4391)

                # YarcParser.g:240:23: ( test )?
                alt97 = 2
                LA97_0 = self.input.LA(1)

                if LA97_0 in {
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
                    alt97 = 1
                if alt97 == 1:
                    # YarcParser.g:240:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop4393)
                    test59 = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 240:29: -> subscipt_step(step=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "subscipt_step",
                    attributes={
                        "step": ((test59 is not None) and [test59.st] or [None])[0]
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

    class exprlist_return(ParserRuleReturnScope):
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

    # $ANTLR start "exprlist"
    # YarcParser.g:242:1: exprlist :exprs+= expr ( COMMA exprs+= expr )* -> test_list(exprs=$exprs);
    def exprlist(
        self,
    ):
        retval = self.exprlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:242:10: (exprs+= expr ( COMMA exprs+= expr )* -> test_list(exprs=$exprs))
                # YarcParser.g:242:12: exprs+= expr ( COMMA exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_exprlist4413)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:242:24: ( COMMA exprs+= expr )*
                while True:  # loop98
                    alt98 = 2
                    LA98_0 = self.input.LA(1)

                    if LA98_0 == COMMA:
                        alt98 = 1

                    if alt98 == 1:
                        # YarcParser.g:242:25: COMMA exprs+= expr
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist4416)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist4420)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop98

                # TEMPLATE REWRITE
                # 242:45: -> test_list(exprs=$exprs)
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

    # $ANTLR end "exprlist"

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
    # YarcParser.g:243:1: testlist :exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs);
    def testlist(
        self,
    ):
        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:243:10: (exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs))
                # YarcParser.g:243:12: exprs+= test ( COMMA exprs+= test )*
                self._state.following.append(self.FOLLOW_test_in_testlist4440)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:243:24: ( COMMA exprs+= test )*
                while True:  # loop99
                    alt99 = 2
                    LA99_0 = self.input.LA(1)

                    if LA99_0 == COMMA:
                        alt99 = 1

                    if alt99 == 1:
                        # YarcParser.g:243:25: COMMA exprs+= test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist4443)

                        self._state.following.append(self.FOLLOW_test_in_testlist4447)
                        exprs = self.test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop99

                # TEMPLATE REWRITE
                # 243:45: -> test_list(exprs=$exprs)
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
    # YarcParser.g:244:1: dict_or_set_maker :exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs)) ;
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
                # YarcParser.g:244:18: (exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs)) )
                # YarcParser.g:245:3: exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs))
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker4468)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:245:15: ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs))
                alt104 = 2
                LA104_0 = self.input.LA(1)

                if LA104_0 == COLON:
                    alt104 = 1
                elif LA104_0 in {COMMA, FOR, RBRACE}:
                    alt104 = 2
                else:
                    nvae = NoViableAltException("", 104, 0, self.input)

                    raise nvae

                if alt104 == 1:
                    # YarcParser.g:245:17: COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker4472
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker4476
                    )
                    values = self.test()

                    self._state.following.pop()
                    if list_values is None:
                        list_values = []
                    list_values.append(values.st)

                    # YarcParser.g:245:36: (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* )
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if LA101_0 == FOR:
                        alt101 = 1
                    elif LA101_0 in {COMMA, RBRACE}:
                        alt101 = 2
                    else:
                        nvae = NoViableAltException("", 101, 0, self.input)

                        raise nvae

                    if alt101 == 1:
                        # YarcParser.g:245:37: for_= comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker4481
                        )
                        for_ = self.comp_for()

                        self._state.following.pop()

                        # TEMPLATE REWRITE
                        # 245:51: -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "dict_comp",
                            attributes={
                                "key": list_exprs[0],
                                "value": list_values[0],
                                "for": ((for_ is not None) and [for_.st] or [None])[0],
                            },
                        )

                    elif alt101 == 2:
                        # YarcParser.g:246:38: ( COMMA exprs+= test COLON values+= test )*
                        pass
                        # YarcParser.g:246:38: ( COMMA exprs+= test COLON values+= test )*
                        while True:  # loop100
                            alt100 = 2
                            LA100_0 = self.input.LA(1)

                            if LA100_0 == COMMA:
                                alt100 = 1

                            if alt100 == 1:
                                # YarcParser.g:246:39: COMMA exprs+= test COLON values+= test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker4540,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker4544
                                )
                                exprs = self.test()

                                self._state.following.pop()
                                if list_exprs is None:
                                    list_exprs = []
                                list_exprs.append(exprs.st)

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker4546,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker4550
                                )
                                values = self.test()

                                self._state.following.pop()
                                if list_values is None:
                                    list_values = []
                                list_values.append(values.st)

                            else:
                                break  # loop100

                    # TEMPLATE REWRITE
                    # 246:79: -> key_value_list(keys=$exprsvalues=$values)
                    retval.st = self.templateLib.getInstanceOf(
                        "key_value_list",
                        attributes={"keys": list_exprs, "values": list_values},
                    )

                elif alt104 == 2:
                    # YarcParser.g:247:17: (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* )
                    pass
                    # YarcParser.g:247:17: (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* )
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if LA103_0 == FOR:
                        alt103 = 1
                    elif LA103_0 in {COMMA, RBRACE}:
                        alt103 = 2
                    else:
                        nvae = NoViableAltException("", 103, 0, self.input)

                        raise nvae

                    if alt103 == 1:
                        # YarcParser.g:247:18: for_= comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker4588
                        )
                        for_ = self.comp_for()

                        self._state.following.pop()

                        # TEMPLATE REWRITE
                        # 247:32: -> list_comp(expr=$exprs[0]for=$for_.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "list_comp",
                            attributes={
                                "expr": list_exprs[0],
                                "for": ((for_ is not None) and [for_.st] or [None])[0],
                            },
                        )

                    elif alt103 == 2:
                        # YarcParser.g:248:19: ( COMMA exprs+= test )*
                        pass
                        # YarcParser.g:248:19: ( COMMA exprs+= test )*
                        while True:  # loop102
                            alt102 = 2
                            LA102_0 = self.input.LA(1)

                            if LA102_0 == COMMA:
                                alt102 = 1

                            if alt102 == 1:
                                # YarcParser.g:248:20: COMMA exprs+= test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker4626,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker4630
                                )
                                exprs = self.test()

                                self._state.following.pop()
                                if list_exprs is None:
                                    list_exprs = []
                                list_exprs.append(exprs.st)

                            else:
                                break  # loop102

                    # TEMPLATE REWRITE
                    # 248:42: -> test_list(exprs=$exprs)
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
    # YarcParser.g:252:1: comp_iter : comp= ( comp_for | comp_if ) -> {$comp.st};
    def comp_iter(
        self,
    ):
        retval = self.comp_iter_return()
        retval.start = self.input.LT(1)

        comp = None

        try:
            try:
                # YarcParser.g:252:11: (comp= ( comp_for | comp_if ) -> {$comp.st})
                # YarcParser.g:252:13: comp= ( comp_for | comp_if )
                pass
                # YarcParser.g:252:18: ( comp_for | comp_if )
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if LA105_0 == FOR:
                    alt105 = 1
                elif LA105_0 == IF:
                    alt105 = 2
                else:
                    nvae = NoViableAltException("", 105, 0, self.input)

                    raise nvae

                if alt105 == 1:
                    # YarcParser.g:252:19: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter4671)
                    comp = self.comp_for()

                    self._state.following.pop()

                elif alt105 == 2:
                    # YarcParser.g:252:30: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter4675)
                    comp = self.comp_if()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 252:39: -> {$comp.st}
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
    # YarcParser.g:253:1: comp_for : FOR exprlist IN or_test ( comp_iter )? -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st);
    def comp_for(
        self,
    ):
        retval = self.comp_for_return()
        retval.start = self.input.LT(1)

        exprlist60 = None
        or_test61 = None
        comp_iter62 = None

        try:
            try:
                # YarcParser.g:253:11: ( FOR exprlist IN or_test ( comp_iter )? -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st))
                # YarcParser.g:253:13: FOR exprlist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for4688)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for4690)
                exprlist60 = self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for4692)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for4694)
                or_test61 = self.or_test()

                self._state.following.pop()

                # YarcParser.g:253:37: ( comp_iter )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if LA106_0 in {FOR, IF}:
                    alt106 = 1
                if alt106 == 1:
                    # YarcParser.g:253:37: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for4696)
                    comp_iter62 = self.comp_iter()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 253:48: -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st)
                retval.st = self.templateLib.getInstanceOf(
                    "comp_for",
                    attributes={
                        "exprs": (
                            (exprlist60 is not None) and [exprlist60.st] or [None]
                        )[0],
                        "seq": ((or_test61 is not None) and [or_test61.st] or [None])[
                            0
                        ],
                        "comp_iter": (
                            (comp_iter62 is not None) and [comp_iter62.st] or [None]
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
    # YarcParser.g:254:1: comp_if : IF test_nocond ( comp_iter )? -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st);
    def comp_if(
        self,
    ):
        retval = self.comp_if_return()
        retval.start = self.input.LT(1)

        test_nocond63 = None
        comp_iter64 = None

        try:
            try:
                # YarcParser.g:254:11: ( IF test_nocond ( comp_iter )? -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st))
                # YarcParser.g:254:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if4725)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if4727)
                test_nocond63 = self.test_nocond()

                self._state.following.pop()

                # YarcParser.g:254:28: ( comp_iter )?
                alt107 = 2
                LA107_0 = self.input.LA(1)

                if LA107_0 in {FOR, IF}:
                    alt107 = 1
                if alt107 == 1:
                    # YarcParser.g:254:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if4729)
                    comp_iter64 = self.comp_iter()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 254:39: -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st)
                retval.st = self.templateLib.getInstanceOf(
                    "comp_if",
                    attributes={
                        "cond": (
                            (test_nocond63 is not None) and [test_nocond63.st] or [None]
                        )[0],
                        "comp_iter": (
                            (comp_iter64 is not None) and [comp_iter64.st] or [None]
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

    FOLLOW_code_snippet_in_scenario62 = frozenset([73, 97, 106])
    FOLLOW_NEWLINE_in_scenario66 = frozenset([73, 97, 106])
    FOLLOW_declaration_in_scenario70 = frozenset([73, 100, 106, 108])
    FOLLOW_code_snippet_in_scenario75 = frozenset([73, 100, 106, 108])
    FOLLOW_NEWLINE_in_scenario79 = frozenset([73, 100, 106, 108])
    FOLLOW_settings_in_scenario83 = frozenset([108])
    FOLLOW_stage_in_scenario86 = frozenset([1, 106, 122])
    FOLLOW_writers_in_scenario88 = frozenset([1, 106])
    FOLLOW_code_snippet_in_scenario94 = frozenset([1, 106])
    FOLLOW_SNIPPET_in_code_snippet217 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration240 = frozenset([43])
    FOLLOW_ID_in_declaration242 = frozenset([14, 73])
    FOLLOW_COLON_in_declaration245 = frozenset([43, 118])
    FOLLOW_name_in_declaration247 = frozenset([73])
    FOLLOW_NEWLINE_in_declaration251 = frozenset([1])
    FOLLOW_SETTINGS_in_settings274 = frozenset([14])
    FOLLOW_COLON_in_settings276 = frozenset([73])
    FOLLOW_NEWLINE_in_settings278 = frozenset([49])
    FOLLOW_INDENT_in_settings280 = frozenset([43, 106])
    FOLLOW_setting_in_settings285 = frozenset([19, 43, 106])
    FOLLOW_code_snippet_in_settings289 = frozenset([19, 43, 106])
    FOLLOW_DEDENT_in_settings293 = frozenset([1])
    FOLLOW_STAGE_in_stage320 = frozenset([14])
    FOLLOW_COLON_in_stage322 = frozenset([73])
    FOLLOW_NEWLINE_in_stage324 = frozenset([49])
    FOLLOW_INDENT_in_stage326 = frozenset(
        [
            11,
            15,
            18,
            21,
            24,
            28,
            31,
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
            68,
            74,
            76,
            80,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_stmts_in_stage328 = frozenset([19])
    FOLLOW_DEDENT_in_stage330 = frozenset([1])
    FOLLOW_WRITERS_in_writers345 = frozenset([14])
    FOLLOW_COLON_in_writers347 = frozenset([73])
    FOLLOW_NEWLINE_in_writers349 = frozenset([49])
    FOLLOW_INDENT_in_writers351 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_expr_stmt_in_writers356 = frozenset(
        [
            11,
            15,
            19,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_code_snippet_in_writers360 = frozenset(
        [
            11,
            15,
            19,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_writer_in_writers364 = frozenset(
        [
            11,
            15,
            19,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_DEDENT_in_writers368 = frozenset([1])
    FOLLOW_ID_in_setting392 = frozenset([5])
    FOLLOW_ASSIGN_in_setting394 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_setting396 = frozenset([73])
    FOLLOW_NEWLINE_in_setting398 = frozenset([1])
    FOLLOW_open_stmt_in_stmts527 = frozenset(
        [
            11,
            15,
            18,
            21,
            24,
            28,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_aug_expr_stmt_in_stmts534 = frozenset(
        [
            1,
            11,
            15,
            18,
            21,
            24,
            28,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_code_snippet_in_stmts538 = frozenset(
        [
            1,
            11,
            15,
            18,
            21,
            24,
            28,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_edit_stmt_in_stmts542 = frozenset(
        [
            1,
            11,
            15,
            18,
            21,
            24,
            28,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_behavior_stmt_in_stmts546 = frozenset(
        [
            1,
            11,
            15,
            18,
            21,
            24,
            28,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_ID_in_writer578 = frozenset([14])
    FOLLOW_COLON_in_writer580 = frozenset([73])
    FOLLOW_NEWLINE_in_writer582 = frozenset([49])
    FOLLOW_INDENT_in_writer584 = frozenset([43])
    FOLLOW_writer_param_in_writer587 = frozenset([19, 43])
    FOLLOW_DEDENT_in_writer593 = frozenset([1])
    FOLLOW_ID_in_writer_param622 = frozenset([5])
    FOLLOW_ASSIGN_in_writer_param624 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_writer_param626 = frozenset([73])
    FOLLOW_NEWLINE_in_writer_param628 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt642 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_open_stmt644 = frozenset([73])
    FOLLOW_NEWLINE_in_open_stmt646 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt662 = frozenset([43, 114, 118])
    FOLLOW_TIMELINE_in_edit_stmt665 = frozenset([14])
    FOLLOW_COLON_in_edit_stmt667 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_stmt669 = frozenset([49])
    FOLLOW_INDENT_in_edit_stmt671 = frozenset([43, 118])
    FOLLOW_name_in_edit_stmt676 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_edit_stmt680 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_stmt682 = frozenset([19, 43, 118])
    FOLLOW_DEDENT_in_edit_stmt686 = frozenset([1])
    FOLLOW_name_in_edit_stmt724 = frozenset([14])
    FOLLOW_edit_block_in_edit_stmt726 = frozenset([1])
    FOLLOW_CREATE_in_create_expr775 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            102,
            110,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_create_expr779 = frozenset([13, 37, 58, 67, 102, 110])
    FOLLOW_SHAPE_in_create_expr791 = frozenset([14, 73])
    FOLLOW_LIGHT_in_create_expr795 = frozenset([14, 73])
    FOLLOW_edit_block_in_create_expr801 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr806 = frozenset([1])
    FOLLOW_STEREO_in_create_expr942 = frozenset([13])
    FOLLOW_CAMERA_in_create_expr945 = frozenset([14, 73])
    FOLLOW_edit_block_in_create_expr951 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr956 = frozenset([1])
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_create_expr1093 = frozenset([14, 73])
    FOLLOW_edit_block_in_create_expr1098 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr1103 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr1234 = frozenset([14, 73])
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_instantiate_expr1318 = frozenset([14, 73])
    FOLLOW_edit_block_in_instantiate_expr1321 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr1326 = frozenset([1])
    FOLLOW_GROUP_in_group_expr1465 = frozenset([55])
    FOLLOW_LBRACK_in_group_expr1467 = frozenset([43, 118])
    FOLLOW_name_in_group_expr1471 = frozenset([16, 89])
    FOLLOW_COMMA_in_group_expr1474 = frozenset([43, 118])
    FOLLOW_name_in_group_expr1478 = frozenset([16, 89])
    FOLLOW_RBRACK_in_group_expr1482 = frozenset([14, 73])
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_get_expr1631 = frozenset([14, 73])
    FOLLOW_simple_block_in_get_expr1634 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr1638 = frozenset([1])
    FOLLOW_COLON_in_edit_block1730 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_block1732 = frozenset([49])
    FOLLOW_INDENT_in_edit_block1734 = frozenset(
        [28, 43, 61, 67, 70, 83, 91, 92, 95, 96, 98, 104, 116, 118, 120, 121]
    )
    FOLLOW_attr_in_edit_block1740 = frozenset(
        [19, 28, 43, 61, 67, 70, 83, 91, 92, 95, 96, 98, 104, 116, 118, 120, 121]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block1744 = frozenset(
        [19, 28, 43, 61, 67, 70, 83, 91, 92, 95, 96, 98, 104, 116, 118, 120, 121]
    )
    FOLLOW_DEDENT_in_edit_block1752 = frozenset([1])
    FOLLOW_COLON_in_simple_block1771 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_block1773 = frozenset([49])
    FOLLOW_INDENT_in_simple_block1775 = frozenset([43, 118])
    FOLLOW_simple_attr_in_simple_block1778 = frozenset([19, 43, 118])
    FOLLOW_DEDENT_in_simple_block1784 = frozenset([1])
    FOLLOW_core_attr_in_attr1799 = frozenset([1])
    FOLLOW_simple_attr_in_attr1803 = frozenset([1])
    FOLLOW_compound_attr_in_attr1807 = frozenset([1])
    FOLLOW_name_in_simple_attr1837 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_COLON_in_simple_attr1840 = frozenset([43, 118])
    FOLLOW_name_in_simple_attr1844 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_simple_attr1850 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_attr1852 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr1899 = frozenset([79])
    FOLLOW_ON_in_compound_attr1901 = frozenset([43, 118])
    FOLLOW_name_in_compound_attr1905 = frozenset([14, 73])
    FOLLOW_simple_block_in_compound_attr1910 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr1914 = frozenset([1])
    FOLLOW_ROT_AROUND_in_compound_attr1998 = frozenset([43, 118])
    FOLLOW_name_in_compound_attr2002 = frozenset([14, 73])
    FOLLOW_simple_block_in_compound_attr2007 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr2011 = frozenset([1])
    FOLLOW_PHYSICS_in_compound_attr2068 = frozenset([14, 73])
    FOLLOW_simple_block_in_compound_attr2073 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr2077 = frozenset([1])
    FOLLOW_MOVE_TO_CAM_in_compound_attr2130 = frozenset([43, 118])
    FOLLOW_name_in_compound_attr2134 = frozenset([14, 73])
    FOLLOW_simple_block_in_compound_attr2139 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr2143 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr2221 = frozenset([8, 115])
    FOLLOW_AXIS_in_core_attr2225 = frozenset([115])
    FOLLOW_TO_in_core_attr2228 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2232 = frozenset([73])
    FOLLOW_ROTATE_in_core_attr2256 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_AXIS_in_core_attr2260 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2265 = frozenset([73, 82])
    FOLLOW_ORDER_in_core_attr2267 = frozenset([73])
    FOLLOW_SCALE_in_core_attr2292 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2296 = frozenset([73])
    FOLLOW_LOOK_AT_in_core_attr2315 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2319 = frozenset([73])
    FOLLOW_UP_AXIS_in_core_attr2338 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2342 = frozenset([73])
    FOLLOW_SIZE_in_core_attr2361 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2365 = frozenset([73])
    FOLLOW_SEMANTICS_in_core_attr2384 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2388 = frozenset([73])
    FOLLOW_VISIBLE_in_core_attr2407 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2411 = frozenset([73])
    FOLLOW_MATERIAL_in_core_attr2430 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_core_attr2434 = frozenset([73])
    FOLLOW_NEWLINE_in_core_attr2451 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt2474 = frozenset([14])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt2476 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block2502 = frozenset([73])
    FOLLOW_NEWLINE_in_inner_behavior_block2504 = frozenset([49])
    FOLLOW_INDENT_in_inner_behavior_block2506 = frozenset(
        [43, 61, 67, 70, 83, 91, 92, 95, 96, 98, 104, 116, 118, 120, 121]
    )
    FOLLOW_attr_in_inner_behavior_block2510 = frozenset(
        [19, 43, 61, 67, 70, 83, 91, 92, 95, 96, 98, 104, 116, 118, 120, 121]
    )
    FOLLOW_DEDENT_in_inner_behavior_block2513 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt2533 = frozenset([14])
    FOLLOW_behavior_block_in_behavior_stmt2535 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr2557 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            113,
            117,
            118,
        ]
    )
    FOLLOW_test_in_behavior_expr2561 = frozenset([36, 113])
    FOLLOW_FRAMES_in_behavior_expr2567 = frozenset([1])
    FOLLOW_TIME_in_behavior_expr2571 = frozenset([1])
    FOLLOW_COLON_in_behavior_block2593 = frozenset([73])
    FOLLOW_NEWLINE_in_behavior_block2595 = frozenset([49])
    FOLLOW_INDENT_in_behavior_block2597 = frozenset(
        [
            11,
            15,
            18,
            21,
            24,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_aug_expr_stmt_in_behavior_block2602 = frozenset(
        [
            11,
            15,
            18,
            19,
            21,
            24,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_code_snippet_in_behavior_block2606 = frozenset(
        [
            11,
            15,
            18,
            19,
            21,
            24,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_edit_stmt_in_behavior_block2610 = frozenset(
        [
            11,
            15,
            18,
            19,
            21,
            24,
            31,
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
            68,
            74,
            76,
            84,
            101,
            106,
            111,
            117,
            118,
        ]
    )
    FOLLOW_DEDENT_in_behavior_block2614 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt2635 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_expr_stmt2640 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_ASSIGN_in_expr_stmt2644 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_testlist_in_expr_stmt2650 = frozenset([73])
    FOLLOW_fetch_expr_in_expr_stmt2654 = frozenset([73])
    FOLLOW_NEWLINE_in_expr_stmt2657 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt2695 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_aug_expr_stmt2707 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt2712 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt2716 = frozenset([73])
    FOLLOW_NEWLINE_in_aug_expr_stmt2719 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt2751 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt2766 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt2770 = frozenset([73])
    FOLLOW_NEWLINE_in_aug_expr_stmt2773 = frozenset([1])
    FOLLOW_model_expr_in_aug_expr_stmt2808 = frozenset([1])
    FOLLOW_model_expr_in_aug_expr_stmt2842 = frozenset([1])
    FOLLOW_create_expr_in_model_expr2859 = frozenset([1])
    FOLLOW_instantiate_expr_in_model_expr2864 = frozenset([1])
    FOLLOW_get_expr_in_model_expr2869 = frozenset([1])
    FOLLOW_group_expr_in_model_expr2874 = frozenset([1])
    FOLLOW_FETCH_in_fetch_expr2888 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_fetch_expr2892 = frozenset([37])
    FOLLOW_FROM_in_fetch_expr2894 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_fetch_expr2898 = frozenset([1, 59, 66, 90])
    FOLLOW_MATCH_in_fetch_expr2901 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_fetch_expr2905 = frozenset([1, 59, 90])
    FOLLOW_LIMIT_in_fetch_expr2910 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_fetch_expr2914 = frozenset([1, 90])
    FOLLOW_RECURSIVE_in_fetch_expr2918 = frozenset([1])
    FOLLOW_or_test_in_test2969 = frozenset([1, 47])
    FOLLOW_IF_in_test2972 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_or_test_in_test2976 = frozenset([26])
    FOLLOW_ELSE_in_test2978 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_test2982 = frozenset([1])
    FOLLOW_or_test_in_test_nocond3024 = frozenset([1])
    FOLLOW_and_test_in_or_test3046 = frozenset([1, 81])
    FOLLOW_OR_in_or_test3049 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_and_test_in_or_test3053 = frozenset([1, 81])
    FOLLOW_not_test_in_and_test3076 = frozenset([1, 4])
    FOLLOW_AND_in_and_test3079 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_not_test_in_and_test3083 = frozenset([1, 4])
    FOLLOW_NOT_in_not_test3104 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_not_test_in_not_test3108 = frozenset([1])
    FOLLOW_comparison_in_not_test3134 = frozenset([1])
    FOLLOW_expr_in_comparison3148 = frozenset([1, 27, 40, 41, 48, 53, 64, 65, 76, 77])
    FOLLOW_comp_op_in_comparison3153 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_in_comparison3157 = frozenset([1, 27, 40, 41, 48, 53, 64, 65, 76, 77])
    FOLLOW_LT_in_comp_op3187 = frozenset([1])
    FOLLOW_GT_in_comp_op3191 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op3195 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op3199 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op3203 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op3207 = frozenset([1])
    FOLLOW_IN_in_comp_op3211 = frozenset([1])
    FOLLOW_NOT_in_comp_op3215 = frozenset([48])
    FOLLOW_IN_in_comp_op3217 = frozenset([1])
    FOLLOW_IS_in_comp_op3221 = frozenset([1])
    FOLLOW_IS_in_comp_op3225 = frozenset([76])
    FOLLOW_NOT_in_comp_op3227 = frozenset([1])
    FOLLOW_xor_expr_in_expr3248 = frozenset([1, 12])
    FOLLOW_BIT_OR_in_expr3251 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_xor_expr_in_expr3255 = frozenset([1, 12])
    FOLLOW_and_expr_in_xor_expr3278 = frozenset([1, 123])
    FOLLOW_XOR_in_xor_expr3281 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_and_expr_in_xor_expr3285 = frozenset([1, 123])
    FOLLOW_shift_expr_in_and_expr3308 = frozenset([1, 10])
    FOLLOW_BIT_AND_in_and_expr3311 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_shift_expr_in_and_expr3315 = frozenset([1, 10])
    FOLLOW_arith_expr_in_shift_expr3336 = frozenset([1, 63, 94])
    FOLLOW_LSHIFT_in_shift_expr3342 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_RSHIFT_in_shift_expr3346 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_arith_expr_in_shift_expr3351 = frozenset([1, 63, 94])
    FOLLOW_term_in_arith_expr3377 = frozenset([1, 68, 84])
    FOLLOW_PLUS_in_arith_expr3383 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_MINUS_in_arith_expr3387 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_term_in_arith_expr3392 = frozenset([1, 68, 84])
    FOLLOW_factor_in_term3424 = frozenset([1, 22, 44, 69, 71])
    FOLLOW_MUL_in_term3430 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_DIV_in_term3434 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_MOD_in_term3438 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_IDIV_in_term3442 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_factor_in_term3447 = frozenset([1, 22, 44, 69, 71])
    FOLLOW_PLUS_in_factor3478 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_MINUS_in_factor3482 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_BIT_NOT_in_factor3486 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_factor_in_factor3491 = frozenset([1])
    FOLLOW_power_in_factor3521 = frozenset([1])
    FOLLOW_atom_expr_in_power3538 = frozenset([1, 86])
    FOLLOW_POWER_in_power3541 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_factor_in_power3543 = frozenset([1])
    FOLLOW_atom_in_atom_expr3568 = frozenset([1, 23, 55])
    FOLLOW_trailer_in_atom_expr3573 = frozenset([1, 23, 55])
    FOLLOW_LPAREN_in_atom3598 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_atom3602 = frozenset([93])
    FOLLOW_RPAREN_in_atom3604 = frozenset([1])
    FOLLOW_LBRACK_in_atom3619 = frozenset(
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
            68,
            74,
            76,
            84,
            89,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_testlist_comp_in_atom3621 = frozenset([89])
    FOLLOW_RBRACK_in_atom3624 = frozenset([1])
    FOLLOW_LT_in_atom3639 = frozenset(
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
            68,
            74,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_vector_comp_in_atom3641 = frozenset([40])
    FOLLOW_GT_in_atom3644 = frozenset([1])
    FOLLOW_LBRACE_in_atom3659 = frozenset(
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
            68,
            74,
            76,
            84,
            88,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_dict_or_set_maker_in_atom3661 = frozenset([88])
    FOLLOW_RBRACE_in_atom3664 = frozenset([1])
    FOLLOW_LEN_in_atom3679 = frozenset([62])
    FOLLOW_LPAREN_in_atom3681 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_atom3685 = frozenset([93])
    FOLLOW_RPAREN_in_atom3687 = frozenset([1])
    FOLLOW_name_in_atom3702 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom3712 = frozenset([1])
    FOLLOW_distribution_in_atom3728 = frozenset([1])
    FOLLOW_INTEGER_in_atom3738 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom3748 = frozenset([1])
    FOLLOW_STRING_in_atom3758 = frozenset([1])
    FOLLOW_NONE_in_atom3769 = frozenset([1])
    FOLLOW_TRUE_in_atom3781 = frozenset([1])
    FOLLOW_FALSE_in_atom3793 = frozenset([1])
    FOLLOW_ID_in_name3813 = frozenset([1])
    FOLLOW_UNDERSCORE_in_name3823 = frozenset([1])
    FOLLOW_DISTRIBUTION_in_distribution3840 = frozenset([62])
    FOLLOW_LPAREN_in_distribution3842 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_arglist_in_distribution3846 = frozenset([93])
    FOLLOW_RPAREN_in_distribution3848 = frozenset([1])
    FOLLOW_COMBINE_in_distribution3881 = frozenset([62])
    FOLLOW_LPAREN_in_distribution3883 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_arglist_in_distribution3887 = frozenset([93])
    FOLLOW_RPAREN_in_distribution3889 = frozenset([1])
    FOLLOW_test_in_testlist_comp3910 = frozenset([1, 16, 34, 87])
    FOLLOW_comp_for_in_testlist_comp3914 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp3962 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_testlist_comp3966 = frozenset([1, 16])
    FOLLOW_RANGE_in_testlist_comp4010 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_testlist_comp4014 = frozenset([1, 109])
    FOLLOW_STEP_in_testlist_comp4017 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_testlist_comp4021 = frozenset([1])
    FOLLOW_expr_in_vector_comp4085 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp4087 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_in_vector_comp4091 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp4093 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_in_vector_comp4097 = frozenset([1])
    FOLLOW_LBRACK_in_trailer4131 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_subscriptlist_in_trailer4133 = frozenset([89])
    FOLLOW_RBRACK_in_trailer4135 = frozenset([1])
    FOLLOW_DOT_in_trailer4163 = frozenset([43, 118])
    FOLLOW_name_in_trailer4165 = frozenset([1])
    FOLLOW_argument_in_arglist4189 = frozenset([1, 16])
    FOLLOW_COMMA_in_arglist4192 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_argument_in_arglist4196 = frozenset([1, 16])
    FOLLOW_test_in_argument4221 = frozenset([1, 5])
    FOLLOW_ASSIGN_in_argument4224 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_argument4228 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist4253 = frozenset([1, 16])
    FOLLOW_COMMA_in_subscriptlist4256 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_subscript__in_subscriptlist4260 = frozenset([1, 16])
    FOLLOW_test_in_subscript_4283 = frozenset([1, 14])
    FOLLOW_COLON_in_subscript_4286 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_subscript_4291 = frozenset([1, 14])
    FOLLOW_sliceop_in_subscript_4298 = frozenset([1])
    FOLLOW_COLON_in_subscript_4344 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_subscript_4349 = frozenset([1, 14])
    FOLLOW_sliceop_in_subscript_4356 = frozenset([1])
    FOLLOW_COLON_in_sliceop4391 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_sliceop4393 = frozenset([1])
    FOLLOW_expr_in_exprlist4413 = frozenset([1, 16])
    FOLLOW_COMMA_in_exprlist4416 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_in_exprlist4420 = frozenset([1, 16])
    FOLLOW_test_in_testlist4440 = frozenset([1, 16])
    FOLLOW_COMMA_in_testlist4443 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_testlist4447 = frozenset([1, 16])
    FOLLOW_test_in_dict_or_set_maker4468 = frozenset([1, 14, 16, 34])
    FOLLOW_COLON_in_dict_or_set_maker4472 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker4476 = frozenset([1, 16, 34])
    FOLLOW_comp_for_in_dict_or_set_maker4481 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker4540 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker4544 = frozenset([14])
    FOLLOW_COLON_in_dict_or_set_maker4546 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker4550 = frozenset([1, 16])
    FOLLOW_comp_for_in_dict_or_set_maker4588 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker4626 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker4630 = frozenset([1, 16])
    FOLLOW_comp_for_in_comp_iter4671 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter4675 = frozenset([1])
    FOLLOW_FOR_in_comp_for4688 = frozenset(
        [11, 15, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_exprlist_in_comp_for4690 = frozenset([48])
    FOLLOW_IN_in_comp_for4692 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_or_test_in_comp_for4694 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_for4696 = frozenset([1])
    FOLLOW_IF_in_comp_if4725 = frozenset(
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
            68,
            74,
            76,
            84,
            101,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_nocond_in_comp_if4727 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_if4729 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
