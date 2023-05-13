# $ANTLR 3.5.1 C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g 2023-05-13 14:01:56

import sys

import stringtemplate3
from antlr3 import (
    BaseRecognizer,
    EarlyExitException,
    MismatchedSetException,
    NoViableAltException,
    ParserRuleReturnScope,
    RecognitionException,
    RecognizerSharedState,
    Token,
)

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
CAM_TRANSLATE = 14
COLON = 15
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
LIGHT_TYPE = 59
LIMIT = 60
LINE_JOINING = 61
LOOK_AT = 62
LPAREN = 63
LSHIFT = 64
LT = 65
LT_EQ = 66
MATCH = 67
MATERIAL = 68
MINUS = 69
MOD = 70
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
SHAPES = 102
SHAPES_OR_LIGHTS = 103
SHORT_STRING = 104
SIZE = 105
SKIP_ = 106
SNIPPET = 107
SPACES = 108
STAGE = 109
STEP = 110
STEREO = 111
STRING = 112
STRING_ESCAPE_SEQ = 113
TIME = 114
TIMELINE = 115
TO = 116
TRANSLATE = 117
TRUE = 118
UNDERSCORE = 119
UNKNOWN = 120
UP_AXIS = 121
VISIBLE = 122
WRITERS = 123
XOR = 124

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
    14: "CAM_TRANSLATE",
    15: "COLON",
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
    59: "LIGHT_TYPE",
    60: "LIMIT",
    61: "LINE_JOINING",
    62: "LOOK_AT",
    63: "LPAREN",
    64: "LSHIFT",
    65: "LT",
    66: "LT_EQ",
    67: "MATCH",
    68: "MATERIAL",
    69: "MINUS",
    70: "MOD",
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
    102: "SHAPES",
    103: "SHAPES_OR_LIGHTS",
    104: "SHORT_STRING",
    105: "SIZE",
    106: "SKIP_",
    107: "SNIPPET",
    108: "SPACES",
    109: "STAGE",
    110: "STEP",
    111: "STEREO",
    112: "STRING",
    113: "STRING_ESCAPE_SEQ",
    114: "TIME",
    115: "TIMELINE",
    116: "TO",
    117: "TRANSLATE",
    118: "TRUE",
    119: "UNDERSCORE",
    120: "UNKNOWN",
    121: "UP_AXIS",
    122: "VISIBLE",
    123: "WRITERS",
    124: "XOR",
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
    "CAM_TRANSLATE",
    "COLON",
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
    "LIGHT_TYPE",
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
    "SHAPES",
    "SHAPES_OR_LIGHTS",
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
    grammarFileName = "C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g"
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:1: scenario : declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st);
    def scenario(
        self,
    ):
        retval = self.scenario_return()
        retval.start = self.input.LT(1)

        declaration1 = None
        settings2 = None
        stage3 = None
        writers4 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:10: ( declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:12: declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )?
                self._state.following.append(self.FOLLOW_declaration_in_scenario59)
                declaration1 = self.declaration()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:24: ( NEWLINE )*
                while True:  # loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if LA1_0 == NEWLINE:
                        alt1 = 1

                    if alt1 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:24: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario61
                        )

                    else:
                        break  # loop1

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:33: ( settings )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if LA2_0 == SETTINGS:
                    alt2 = 1
                if alt2 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:33: settings
                    self._state.following.append(self.FOLLOW_settings_in_scenario64)
                    settings2 = self.settings()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:43: ( stage )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if LA3_0 == STAGE:
                    alt3 = 1
                if alt3 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:43: stage
                    self._state.following.append(self.FOLLOW_stage_in_scenario67)
                    stage3 = self.stage()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:50: ( writers )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == WRITERS:
                    alt4 = 1
                if alt4 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:19:50: writers
                    self._state.following.append(self.FOLLOW_writers_in_scenario70)
                    writers4 = self.writers()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 20:3: -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st)
                retval.st = self.templateLib.getInstanceOf(
                    "scenario",
                    attributes={
                        "name": (
                            (declaration1 is not None)
                            and [declaration1.scenario_name]
                            or [None]
                        )[0],
                        "settings": (
                            (settings2 is not None) and [settings2.st] or [None]
                        )[0],
                        "stage": ((stage3 is not None) and [stage3.st] or [None])[0],
                        "writers": ((writers4 is not None) and [writers4.st] or [None])[
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

    # $ANTLR end "scenario"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:1: declaration returns [scenario_name] : SCENARIO ID ( COLON name )? NEWLINE ;
    def declaration(
        self,
    ):
        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        ID5 = None
        name6 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:37: ( SCENARIO ID ( COLON name )? NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:39: SCENARIO ID ( COLON name )? NEWLINE
                self.match(self.input, SCENARIO, self.FOLLOW_SCENARIO_in_declaration112)

                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_declaration114)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:51: ( COLON name )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if LA5_0 == COLON:
                    alt5 = 1
                if alt5 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:52: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration117)

                    self._state.following.append(self.FOLLOW_name_in_declaration119)
                    name6 = self.name()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_declaration123)

                # action start
                retval.scenario_name = ID5.text
                # action end

                # action start
                self.handler = HandlerFactory.get_handler(
                    (
                        (name6 is not None)
                        and [self.input.toString(name6.start, name6.stop)]
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:1: settings : SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT -> settings(setting_list=$sets);
    def settings(
        self,
    ):
        retval = self.settings_return()
        retval.start = self.input.LT(1)

        list_sets = None
        sets = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:13: ( SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT -> settings(setting_list=$sets))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:15: SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT
                self.match(self.input, SETTINGS, self.FOLLOW_SETTINGS_in_settings146)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_settings148)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_settings150)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_settings152)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:49: (sets+= setting )+
                cnt6 = 0
                while True:  # loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if LA6_0 == ID:
                        alt6 = 1

                    if alt6 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:49: sets+= setting
                        self._state.following.append(self.FOLLOW_setting_in_settings156)
                        sets = self.setting()

                        self._state.following.pop()
                        if list_sets is None:
                            list_sets = []
                        list_sets.append(sets.st)

                    else:
                        if cnt6 >= 1:
                            break  # loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_settings159)

                # TEMPLATE REWRITE
                # 27:67: -> settings(setting_list=$sets)
                retval.st = self.templateLib.getInstanceOf(
                    "settings", attributes={"setting_list": list_sets}
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:28:1: stage : STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st};
    def stage(
        self,
    ):
        retval = self.stage_return()
        retval.start = self.input.LT(1)

        stmts7 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:28:13: ( STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st})
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:28:15: STAGE COLON NEWLINE INDENT stmts DEDENT
                self.match(self.input, STAGE, self.FOLLOW_STAGE_in_stage181)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_stage183)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stage185)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stage187)

                self._state.following.append(self.FOLLOW_stmts_in_stage189)
                stmts7 = self.stmts()

                self._state.following.pop()

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stage191)

                # TEMPLATE REWRITE
                # 28:55: -> {$stmts.st}
                retval.st = ((stmts7 is not None) and [stmts7.st] or [None])[0]

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:29:1: writers : WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | writer )+ DEDENT -> writers(stmts=$stmts_);
    def writers(
        self,
    ):
        retval = self.writers_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:29:13: ( WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | writer )+ DEDENT -> writers(stmts=$stmts_))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:29:15: WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | writer )+ DEDENT
                self.match(self.input, WRITERS, self.FOLLOW_WRITERS_in_writers206)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writers208)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writers210)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writers212)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:29:52: ( expr_stmt | writer )+
                cnt7 = 0
                while True:  # loop7
                    alt7 = 3
                    LA7_0 = self.input.LA(1)

                    if LA7_0 in {
                        BIT_NOT,
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
                        alt7 = 1
                    elif LA7_0 == ID:
                        LA7_3 = self.input.LA(2)

                        if LA7_3 == COLON:
                            alt7 = 2
                        elif LA7_3 in {
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
                            alt7 = 1

                    if alt7 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:29:53: expr_stmt
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers217
                        )
                        stmts_ = self.expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt7 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:29:65: writer
                        self._state.following.append(self.FOLLOW_writer_in_writers221)
                        stmts_ = self.writer()

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

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writers225)

                # TEMPLATE REWRITE
                # 29:81: -> writers(stmts=$stmts_)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:1: setting : ID ASSIGN test NEWLINE -> setting(setting=$ID.textvalue=$test.st);
    def setting(
        self,
    ):
        retval = self.setting_return()
        retval.start = self.input.LT(1)

        ID8 = None
        test9 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:16: ( ID ASSIGN test NEWLINE -> setting(setting=$ID.textvalue=$test.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:18: ID ASSIGN test NEWLINE
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_setting249)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_setting251)

                self._state.following.append(self.FOLLOW_test_in_setting253)
                test9 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_setting255)

                # TEMPLATE REWRITE
                # 31:41: -> setting(setting=$ID.textvalue=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "setting",
                    attributes={
                        "setting": ID8.text,
                        "value": ((test9 is not None) and [test9.st] or [None])[0],
                    },
                )

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:1: stmts :stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | edit_stmt | behavior_stmt )+ -> stage(stmts=$stmts_);
    def stmts(
        self,
    ):
        retval = self.stmts_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:16: (stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | edit_stmt | behavior_stmt )+ -> stage(stmts=$stmts_))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:18: stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:26: ( open_stmt )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if LA8_0 == OPEN:
                    alt8 = 1
                if alt8 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:27: open_stmt
                    self._state.following.append(self.FOLLOW_open_stmt_in_stmts289)
                    stmts_ = self.open_stmt()

                    self._state.following.pop()
                    if list_stmts_ is None:
                        list_stmts_ = []
                    list_stmts_.append(stmts_.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:47: ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                cnt9 = 0
                while True:  # loop9
                    alt9 = 4
                    LA9 = self.input.LA(1)
                    if LA9 in {
                        BIT_NOT,
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
                        alt9 = 1
                    elif LA9 in {EDIT}:
                        alt9 = 2
                    elif LA9 in {EVERY}:
                        alt9 = 3

                    if alt9 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:48: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts296
                        )
                        stmts_ = self.aug_expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt9 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:64: edit_stmt
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts300)
                        stmts_ = self.edit_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt9 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:76: behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_behavior_stmt_in_stmts304
                        )
                        stmts_ = self.behavior_stmt()

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

                # TEMPLATE REWRITE
                # 32:92: -> stage(stmts=$stmts_)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:1: writer : ID COLON NEWLINE INDENT (writer_params+= writer_param )+ DEDENT -> writer(writer_id=$ID.textwriter_params=$writer_paramsrps=[\"rp\"]);
    def writer(
        self,
    ):
        retval = self.writer_return()
        retval.start = self.input.LT(1)

        ID10 = None
        list_writer_params = None
        writer_params = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:16: ( ID COLON NEWLINE INDENT (writer_params+= writer_param )+ DEDENT -> writer(writer_id=$ID.textwriter_params=$writer_paramsrps=[\"rp\"]))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:18: ID COLON NEWLINE INDENT (writer_params+= writer_param )+ DEDENT
                ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_writer330)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writer332)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer334)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writer336)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:55: (writer_params+= writer_param )+
                cnt10 = 0
                while True:  # loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if LA10_0 == ID:
                        alt10 = 1

                    if alt10 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:55: writer_params+= writer_param
                        self._state.following.append(
                            self.FOLLOW_writer_param_in_writer340
                        )
                        writer_params = self.writer_param()

                        self._state.following.pop()
                        if list_writer_params is None:
                            list_writer_params = []
                        list_writer_params.append(writer_params.st)

                    else:
                        if cnt10 >= 1:
                            break  # loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writer343)

                # TEMPLATE REWRITE
                # 33:78: -> writer(writer_id=$ID.textwriter_params=$writer_paramsrps=[\"rp\"])
                retval.st = self.templateLib.getInstanceOf(
                    "writer",
                    attributes={
                        "writer_id": ID10.text,
                        "writer_params": list_writer_params,
                        "rps": ["rp"],
                    },
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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "writer_param"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:1: writer_param : ID ASSIGN test NEWLINE -> writer_param(param=$ID.textvalue=$test.st);
    def writer_param(
        self,
    ):
        retval = self.writer_param_return()
        retval.start = self.input.LT(1)

        ID11 = None
        test12 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:16: ( ID ASSIGN test NEWLINE -> writer_param(param=$ID.textvalue=$test.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:18: ID ASSIGN test NEWLINE
                ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_writer_param372)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_writer_param374)

                self._state.following.append(self.FOLLOW_test_in_writer_param376)
                test12 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer_param378)

                # TEMPLATE REWRITE
                # 34:41: -> writer_param(param=$ID.textvalue=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "writer_param",
                    attributes={
                        "param": ID11.text,
                        "value": ((test12 is not None) and [test12.st] or [None])[0],
                    },
                )

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:1: open_stmt : OPEN test NEWLINE -> open_stmt(path=$test.st);
    def open_stmt(
        self,
    ):
        retval = self.open_stmt_return()
        retval.start = self.input.LT(1)

        test13 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:11: ( OPEN test NEWLINE -> open_stmt(path=$test.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:13: OPEN test NEWLINE
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_open_stmt404)

                self._state.following.append(self.FOLLOW_test_in_open_stmt406)
                test13 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_open_stmt408)

                # TEMPLATE REWRITE
                # 38:31: -> open_stmt(path=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "open_stmt",
                    attributes={
                        "path": ((test13 is not None) and [test13.st] or [None])[0]
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:1: edit_stmt : EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)| name edit_block ) ;
    def edit_stmt(
        self,
    ):
        retval = self.edit_stmt_return()
        retval.start = self.input.LT(1)

        list_params = None
        list_values = None
        params = None
        values = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:11: ( EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)| name edit_block ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:13: EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)| name edit_block )
                self.match(self.input, EDIT, self.FOLLOW_EDIT_in_edit_stmt424)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:18: ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)| name edit_block )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if LA12_0 == TIMELINE:
                    alt12 = 1
                elif LA12_0 in {ID, UNDERSCORE}:
                    alt12 = 2
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:19: TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt427
                    )

                    self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_stmt429)

                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_stmt431)

                    self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_stmt433)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:49: (params+= name values+= test NEWLINE )+
                    cnt11 = 0
                    while True:  # loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if LA11_0 in {ID, UNDERSCORE}:
                            alt11 = 1

                        if alt11 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:50: params+= name values+= test NEWLINE
                            self._state.following.append(
                                self.FOLLOW_name_in_edit_stmt438
                            )
                            params = self.name()

                            self._state.following.pop()
                            if list_params is None:
                                list_params = []
                            list_params.append(params.st)

                            self._state.following.append(
                                self.FOLLOW_test_in_edit_stmt442
                            )
                            values = self.test()

                            self._state.following.pop()
                            if list_values is None:
                                list_values = []
                            list_values.append(values.st)

                            self.match(
                                self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_stmt444
                            )

                        else:
                            if cnt11 >= 1:
                                break  # loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1

                    self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_stmt448)

                    # TEMPLATE REWRITE
                    # 39:93: -> edit_timeline(params=$paramsvalues=$values)
                    retval.st = self.templateLib.getInstanceOf(
                        "edit_timeline",
                        attributes={"params": list_params, "values": list_values},
                    )

                elif alt12 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:40:20: name edit_block
                    self._state.following.append(self.FOLLOW_name_in_edit_stmt484)
                    self.name()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_edit_block_in_edit_stmt486)
                    self.edit_block()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:1: create_expr : CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) ;
    def create_expr(
        self,
    ):
        retval = self.create_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:12: ( CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:3: CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr496)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:10: ( test )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if LA13_0 in {
                    BIT_NOT,
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
                    alt13 = 1
                if alt13 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:10: test
                    self._state.following.append(self.FOLLOW_test_in_create_expr498)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:16: ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if LA17_0 in {
                    CAMERA,
                    FROM,
                    LIGHT_TYPE,
                    SHAPES,
                    SHAPES_OR_LIGHTS,
                    STEREO,
                }:
                    alt17 = 1
                elif LA17_0 == MATERIAL:
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test )
                    alt15 = 4
                    LA15 = self.input.LA(1)
                    if LA15 in {CAMERA, STEREO}:
                        alt15 = 1
                    elif LA15 in {SHAPES_OR_LIGHTS}:
                        LA15_2 = self.input.LA(2)

                        if LA15_2 in {COLON, NEWLINE}:
                            alt15 = 2
                        elif LA15_2 == LIGHT:
                            alt15 = 3
                        else:
                            nvae = NoViableAltException("", 15, 2, self.input)

                            raise nvae

                    elif LA15 in {SHAPES}:
                        alt15 = 2
                    elif LA15 in {LIGHT_TYPE}:
                        alt15 = 3
                    elif LA15 in {FROM}:
                        alt15 = 4
                    else:
                        nvae = NoViableAltException("", 15, 0, self.input)

                        raise nvae

                    if alt15 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:6: ( STEREO )? CAMERA
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:6: ( STEREO )?
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if LA14_0 == STEREO:
                            alt14 = 1
                        if alt14 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:6: STEREO
                            self.match(
                                self.input, STEREO, self.FOLLOW_STEREO_in_create_expr508
                            )

                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr511
                        )

                    elif alt15 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:23: shapes
                        self._state.following.append(
                            self.FOLLOW_shapes_in_create_expr515
                        )
                        self.shapes()

                        self._state.following.pop()

                    elif alt15 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:32: light_type LIGHT
                        self._state.following.append(
                            self.FOLLOW_light_type_in_create_expr519
                        )
                        self.light_type()

                        self._state.following.pop()

                        self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr521
                        )

                    elif alt15 == 4:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:51: FROM test
                        self.match(self.input, FROM, self.FOLLOW_FROM_in_create_expr525)

                        self._state.following.append(self.FOLLOW_test_in_create_expr527)
                        self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:62: ( edit_block | NEWLINE )
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if LA16_0 == COLON:
                        alt16 = 1
                    elif LA16_0 == NEWLINE:
                        alt16 = 2
                    else:
                        nvae = NoViableAltException("", 16, 0, self.input)

                        raise nvae

                    if alt16 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:63: edit_block
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr531
                        )
                        self.edit_block()

                        self._state.following.pop()

                    elif alt16 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:76: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr535
                        )

                elif alt17 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:7: MATERIAL ( simple_block )
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr544
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:16: ( simple_block )
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:17: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_create_expr547
                    )
                    self.simple_block()

                    self._state.following.pop()

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "create_expr"

    class shapes_return(ParserRuleReturnScope):
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

    # $ANTLR start "shapes"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:49:1: shapes : ( SHAPES | SHAPES_OR_LIGHTS );
    def shapes(
        self,
    ):
        retval = self.shapes_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:49:12: ( SHAPES | SHAPES_OR_LIGHTS )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {SHAPES, SHAPES_OR_LIGHTS}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "shapes"

    class light_type_return(ParserRuleReturnScope):
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

    # $ANTLR start "light_type"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:1: light_type : ( LIGHT_TYPE | SHAPES_OR_LIGHTS );
    def light_type(
        self,
    ):
        retval = self.light_type_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:12: ( LIGHT_TYPE | SHAPES_OR_LIGHTS )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {LIGHT_TYPE, SHAPES_OR_LIGHTS}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "light_type"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:1: instantiate_expr : INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) ;
    def instantiate_expr(
        self,
    ):
        retval = self.instantiate_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:18: ( INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:20: INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE )
                self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr588,
                )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:32: ( test )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if LA18_0 in {
                    BIT_NOT,
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
                    alt18 = 1
                if alt18 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:33: test
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr591
                    )
                    self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr595)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr597)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:50: ( edit_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:51: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr600
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt19 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:64: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instantiate_expr604
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:1: group_expr : GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) ;
    def group_expr(
        self,
    ):
        retval = self.group_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:18: ( GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:20: GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE )
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_expr618)

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr620)

                self._state.following.append(self.FOLLOW_name_in_group_expr622)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:38: ( COMMA name )*
                while True:  # loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if LA20_0 == COMMA:
                        alt20 = 1

                    if alt20 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:39: COMMA name
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_group_expr625
                        )

                        self._state.following.append(self.FOLLOW_name_in_group_expr627)
                        self.name()

                        self._state.following.pop()

                    else:
                        break  # loop20

                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_group_expr631)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:59: ( edit_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:60: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr634
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt21 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:73: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_group_expr638
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:1: get_expr : GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) ;
    def get_expr(
        self,
    ):
        retval = self.get_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:18: ( GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:20: GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE )
                self.match(self.input, GET, self.FOLLOW_GET_in_get_expr654)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:24: ( ( CAMERA | LIGHT | MATERIAL | name ) AT )?
                alt23 = 2
                LA23 = self.input.LA(1)
                if LA23 in {CAMERA, LIGHT, MATERIAL}:
                    alt23 = 1
                elif LA23 in {ID}:
                    LA23_2 = self.input.LA(2)

                    if LA23_2 == AT:
                        alt23 = 1
                elif LA23 in {UNDERSCORE}:
                    LA23_3 = self.input.LA(2)

                    if LA23_3 == AT:
                        alt23 = 1
                if alt23 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:25: ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:25: ( CAMERA | LIGHT | MATERIAL | name )
                    alt22 = 4
                    LA22 = self.input.LA(1)
                    if LA22 in {CAMERA}:
                        alt22 = 1
                    elif LA22 in {LIGHT}:
                        alt22 = 2
                    elif LA22 in {MATERIAL}:
                        alt22 = 3
                    elif LA22 in {ID, UNDERSCORE}:
                        alt22 = 4
                    else:
                        nvae = NoViableAltException("", 22, 0, self.input)

                        raise nvae

                    if alt22 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:26: CAMERA
                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr658
                        )

                    elif alt22 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:35: LIGHT
                        self.match(self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr662)

                    elif alt22 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:43: MATERIAL
                        self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr666
                        )

                    elif alt22 == 4:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:54: name
                        self._state.following.append(self.FOLLOW_name_in_get_expr670)
                        self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr673)

                self._state.following.append(self.FOLLOW_test_in_get_expr677)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:70: ( simple_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:71: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr680
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt24 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:86: NEWLINE
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr684)

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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "edit_block"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:56:1: edit_block : COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT ;
    def edit_block(
        self,
    ):
        retval = self.edit_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:56:14: ( COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:56:16: COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block695)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block697)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block699)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:56:37: ( attr | inner_behavior_stmt )+
                cnt25 = 0
                while True:  # loop25
                    alt25 = 3
                    LA25_0 = self.input.LA(1)

                    if LA25_0 in {
                        CAM_TRANSLATE,
                        ID,
                        LOOK_AT,
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
                        alt25 = 1
                    elif LA25_0 == EVERY:
                        alt25 = 2

                    if alt25 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:56:38: attr
                        self._state.following.append(self.FOLLOW_attr_in_edit_block702)
                        self.attr()

                        self._state.following.pop()

                    elif alt25 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:56:45: inner_behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_inner_behavior_stmt_in_edit_block706
                        )
                        self.inner_behavior_stmt()

                        self._state.following.pop()

                    else:
                        if cnt25 >= 1:
                            break  # loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_block710)

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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "simple_block"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:1: simple_block : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        retval = self.simple_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:14: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:16: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block717)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block719)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block721)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:37: ( simple_attr )+
                cnt26 = 0
                while True:  # loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if LA26_0 in {ID, UNDERSCORE}:
                        alt26 = 1

                    if alt26 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:37: simple_attr
                        self._state.following.append(
                            self.FOLLOW_simple_attr_in_simple_block723
                        )
                        self.simple_attr()

                        self._state.following.pop()

                    else:
                        if cnt26 >= 1:
                            break  # loop26

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_simple_block726)

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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:59:1: attr : attr_= ( core_attr | simple_attr | compound_attr ) -> {$attr_.st};
    def attr(
        self,
    ):
        retval = self.attr_return()
        retval.start = self.input.LT(1)

        attr_ = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:59:15: (attr_= ( core_attr | simple_attr | compound_attr ) -> {$attr_.st})
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:59:17: attr_= ( core_attr | simple_attr | compound_attr )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:59:23: ( core_attr | simple_attr | compound_attr )
                alt27 = 3
                LA27 = self.input.LA(1)
                if LA27 in {
                    CAM_TRANSLATE,
                    LOOK_AT,
                    ROTATE,
                    SCALE,
                    SEMANTICS,
                    SIZE,
                    TRANSLATE,
                    UP_AXIS,
                    VISIBLE,
                }:
                    alt27 = 1
                elif LA27 in {ID, UNDERSCORE}:
                    alt27 = 2
                elif LA27 in {PHYSICS, ROT_AROUND, SCATTER}:
                    alt27 = 3
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:59:24: core_attr
                    self._state.following.append(self.FOLLOW_core_attr_in_attr746)
                    attr_ = self.core_attr()

                    self._state.following.pop()

                elif alt27 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:59:36: simple_attr
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr750)
                    attr_ = self.simple_attr()

                    self._state.following.pop()

                elif alt27 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:59:50: compound_attr
                    self._state.following.append(self.FOLLOW_compound_attr_in_attr754)
                    attr_ = self.compound_attr()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 59:65: -> {$attr_.st}
                retval.st = attr_.st

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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "simple_attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:1: simple_attr : name ( COLON name )? ( test )? NEWLINE ;
    def simple_attr(
        self,
    ):
        retval = self.simple_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:15: ( name ( COLON name )? ( test )? NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:17: name ( COLON name )? ( test )? NEWLINE
                self._state.following.append(self.FOLLOW_name_in_simple_attr768)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:22: ( COLON name )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if LA28_0 == COLON:
                    alt28 = 1
                if alt28 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:23: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr771)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr773)
                    self.name()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:36: ( test )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if LA29_0 in {
                    BIT_NOT,
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
                    alt29 = 1
                if alt29 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:36: test
                    self._state.following.append(self.FOLLOW_test_in_simple_attr777)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_attr780)

                retval.stop = self.input.LT(-1)

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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "compound_attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:1: compound_attr : ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) ;
    def compound_attr(
        self,
    ):
        retval = self.compound_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:15: ( ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS )
                alt30 = 3
                LA30 = self.input.LA(1)
                if LA30 in {SCATTER}:
                    alt30 = 1
                elif LA30 in {ROT_AROUND}:
                    alt30 = 2
                elif LA30 in {PHYSICS}:
                    alt30 = 3
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:18: SCATTER ON name
                    self.match(
                        self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr789
                    )

                    self.match(self.input, ON, self.FOLLOW_ON_in_compound_attr791)

                    self._state.following.append(self.FOLLOW_name_in_compound_attr793)
                    self.name()

                    self._state.following.pop()

                elif alt30 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:36: ROT_AROUND name
                    self.match(
                        self.input,
                        ROT_AROUND,
                        self.FOLLOW_ROT_AROUND_in_compound_attr797,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr799)
                    self.name()

                    self._state.following.pop()

                elif alt30 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:54: PHYSICS
                    self.match(
                        self.input, PHYSICS, self.FOLLOW_PHYSICS_in_compound_attr803
                    )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:63: ( simple_block | NEWLINE )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if LA31_0 == COLON:
                    alt31 = 1
                elif LA31_0 == NEWLINE:
                    alt31 = 2
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:64: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_compound_attr807
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt31 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:79: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_compound_attr811
                    )

                retval.stop = self.input.LT(-1)

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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "core_attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:64:1: core_attr : ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE ;
    def core_attr(
        self,
    ):
        retval = self.core_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:64:10: ( ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test )
                alt35 = 9
                LA35 = self.input.LA(1)
                if LA35 in {TRANSLATE}:
                    alt35 = 1
                elif LA35 in {CAM_TRANSLATE}:
                    alt35 = 2
                elif LA35 in {ROTATE}:
                    alt35 = 3
                elif LA35 in {SCALE}:
                    alt35 = 4
                elif LA35 in {LOOK_AT}:
                    alt35 = 5
                elif LA35 in {UP_AXIS}:
                    alt35 = 6
                elif LA35 in {SIZE}:
                    alt35 = 7
                elif LA35 in {SEMANTICS}:
                    alt35 = 8
                elif LA35 in {VISIBLE}:
                    alt35 = 9
                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:5: TRANSLATE ( AXIS )? TO test
                    self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr828
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:15: ( AXIS )?
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if LA32_0 == AXIS:
                        alt32 = 1
                    if alt32 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:15: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr830)

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr833)

                    self._state.following.append(self.FOLLOW_test_in_core_attr835)
                    self.test()

                    self._state.following.pop()

                elif alt35 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:7: CAM_TRANSLATE TO test
                    self.match(
                        self.input,
                        CAM_TRANSLATE,
                        self.FOLLOW_CAM_TRANSLATE_in_core_attr843,
                    )

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr845)

                    self._state.following.append(self.FOLLOW_test_in_core_attr847)
                    self.test()

                    self._state.following.pop()

                elif alt35 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:68:7: ROTATE ( AXIS )? test ( ORDER )?
                    self.match(self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr855)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:68:14: ( AXIS )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if LA33_0 == AXIS:
                        alt33 = 1
                    if alt33 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:68:14: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr857)

                    self._state.following.append(self.FOLLOW_test_in_core_attr860)
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:68:25: ( ORDER )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if LA34_0 == ORDER:
                        alt34 = 1
                    if alt34 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:68:25: ORDER
                        self.match(self.input, ORDER, self.FOLLOW_ORDER_in_core_attr862)

                elif alt35 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:7: SCALE test
                    self.match(self.input, SCALE, self.FOLLOW_SCALE_in_core_attr871)

                    self._state.following.append(self.FOLLOW_test_in_core_attr873)
                    self.test()

                    self._state.following.pop()

                elif alt35 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:7: LOOK_AT test
                    self.match(self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr881)

                    self._state.following.append(self.FOLLOW_test_in_core_attr883)
                    self.test()

                    self._state.following.pop()

                elif alt35 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:71:7: UP_AXIS test
                    self.match(self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr891)

                    self._state.following.append(self.FOLLOW_test_in_core_attr893)
                    self.test()

                    self._state.following.pop()

                elif alt35 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:7: SIZE test
                    self.match(self.input, SIZE, self.FOLLOW_SIZE_in_core_attr901)

                    self._state.following.append(self.FOLLOW_test_in_core_attr903)
                    self.test()

                    self._state.following.pop()

                elif alt35 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:7: SEMANTICS test
                    self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr911
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr913)
                    self.test()

                    self._state.following.pop()

                elif alt35 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:7: VISIBLE test
                    self.match(self.input, VISIBLE, self.FOLLOW_VISIBLE_in_core_attr921)

                    self._state.following.append(self.FOLLOW_test_in_core_attr923)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_core_attr929)

                retval.stop = self.input.LT(-1)

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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "inner_behavior_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:1: inner_behavior_stmt : behavior_expr inner_behavior_block ;
    def inner_behavior_stmt(
        self,
    ):
        retval = self.inner_behavior_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:22: ( behavior_expr inner_behavior_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:24: behavior_expr inner_behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_inner_behavior_stmt939
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_inner_behavior_block_in_inner_behavior_stmt941
                )
                self.inner_behavior_block()

                self._state.following.pop()

                retval.stop = self.input.LT(-1)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:1: inner_behavior_block : COLON NEWLINE INDENT ( attr )+ DEDENT ;
    def inner_behavior_block(
        self,
    ):
        retval = self.inner_behavior_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:22: ( COLON NEWLINE INDENT ( attr )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:24: COLON NEWLINE INDENT ( attr )+ DEDENT
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block948
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block950
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block952
                )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:45: ( attr )+
                cnt36 = 0
                while True:  # loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if LA36_0 in {
                        CAM_TRANSLATE,
                        ID,
                        LOOK_AT,
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
                        alt36 = 1

                    if alt36 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:45: attr
                        self._state.following.append(
                            self.FOLLOW_attr_in_inner_behavior_block954
                        )
                        self.attr()

                        self._state.following.pop()

                    else:
                        if cnt36 >= 1:
                            break  # loop36

                        eee = EarlyExitException(36, self.input)
                        raise eee

                    cnt36 += 1

                self.match(
                    self.input, DEDENT, self.FOLLOW_DEDENT_in_inner_behavior_block957
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:1: behavior_stmt : behavior_expr behavior_block ;
    def behavior_stmt(
        self,
    ):
        retval = self.behavior_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:16: ( behavior_expr behavior_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:18: behavior_expr behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_behavior_stmt968
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_behavior_block_in_behavior_stmt970
                )
                self.behavior_block()

                self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:1: behavior_expr : EVERY ( test )? ( FRAMES | TIME ) ;
    def behavior_expr(
        self,
    ):
        retval = self.behavior_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:16: ( EVERY ( test )? ( FRAMES | TIME ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:18: EVERY ( test )? ( FRAMES | TIME )
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr978)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:24: ( test )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if LA37_0 in {
                    BIT_NOT,
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
                    alt37 = 1
                if alt37 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:24: test
                    self._state.following.append(self.FOLLOW_test_in_behavior_expr980)
                    self.test()

                    self._state.following.pop()

                if self.input.LA(1) in {FRAMES, TIME}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:1: behavior_block : COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT ;
    def behavior_block(
        self,
    ):
        retval = self.behavior_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:16: ( COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:18: COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block996)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block998
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block1000)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:39: ( aug_expr_stmt | edit_stmt )+
                cnt38 = 0
                while True:  # loop38
                    alt38 = 3
                    LA38_0 = self.input.LA(1)

                    if LA38_0 in {
                        BIT_NOT,
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
                        alt38 = 1
                    elif LA38_0 == EDIT:
                        alt38 = 2

                    if alt38 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:40: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block1003
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt38 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:56: edit_stmt
                        self._state.following.append(
                            self.FOLLOW_edit_stmt_in_behavior_block1007
                        )
                        self.edit_stmt()

                        self._state.following.pop()

                    else:
                        if cnt38 >= 1:
                            break  # loop38

                        eee = EarlyExitException(38, self.input)
                        raise eee

                    cnt38 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_behavior_block1011)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:1: expr_stmt : assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st);
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
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:11: (assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:13: assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt1023)
                assignable = self.testlist()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:36: ( AUG_ASSIGN | ASSIGN )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if LA39_0 == AUG_ASSIGN:
                    alt39 = 1
                elif LA39_0 == ASSIGN:
                    alt39 = 2
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:37: AUG_ASSIGN
                    op = self.match(
                        self.input, AUG_ASSIGN, self.FOLLOW_AUG_ASSIGN_in_expr_stmt1028
                    )

                elif alt39 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:50: ASSIGN
                    op = self.match(
                        self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr_stmt1032
                    )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:64: ( testlist | fetch_expr )
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if LA40_0 in {
                    BIT_NOT,
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
                    alt40 = 1
                elif LA40_0 == FETCH:
                    alt40 = 2
                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae

                if alt40 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:65: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt1038)
                    value = self.testlist()

                    self._state.following.pop()

                elif alt40 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:76: fetch_expr
                    self._state.following.append(
                        self.FOLLOW_fetch_expr_in_expr_stmt1042
                    )
                    value = self.fetch_expr()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expr_stmt1045)

                # TEMPLATE REWRITE
                # 87:3: -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:1: aug_expr_stmt : ( ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr );
    def aug_expr_stmt(
        self,
    ):
        retval = self.aug_expr_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:14: ( ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr )
                alt45 = 5
                LA45 = self.input.LA(1)
                if LA45 in {
                    BIT_NOT,
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
                elif LA45 in {CREATE}:
                    alt45 = 2
                elif LA45 in {INSTANTIATE}:
                    alt45 = 3
                elif LA45 in {GET}:
                    alt45 = 4
                elif LA45 in {GROUP}:
                    alt45 = 5
                else:
                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae

                if alt45 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:16: ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:16: ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:90:5: testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt1080
                    )
                    self.testlist()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:90:14: ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if LA44_0 == AUG_ASSIGN:
                        alt44 = 1
                    elif LA44_0 == ASSIGN:
                        alt44 = 2
                    else:
                        nvae = NoViableAltException("", 44, 0, self.input)

                        raise nvae

                    if alt44 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:91:7: AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE
                        self.match(
                            self.input,
                            AUG_ASSIGN,
                            self.FOLLOW_AUG_ASSIGN_in_aug_expr_stmt1090,
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:91:18: ( testlist | fetch_expr )?
                        alt41 = 3
                        LA41_0 = self.input.LA(1)

                        if LA41_0 in {
                            BIT_NOT,
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
                            alt41 = 1
                        elif LA41_0 == FETCH:
                            alt41 = 2
                        if alt41 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:91:19: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt1093
                            )
                            self.testlist()

                            self._state.following.pop()

                        elif alt41 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:91:30: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt1097
                            )
                            self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_aug_expr_stmt1101,
                        )

                    elif alt44 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:92:9: ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt1111
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:92:16: ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        alt43 = 5
                        LA43 = self.input.LA(1)
                        if LA43 in {
                            BIT_NOT,
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
                            alt43 = 1
                        elif LA43 in {CREATE}:
                            alt43 = 2
                        elif LA43 in {INSTANTIATE}:
                            alt43 = 3
                        elif LA43 in {GET}:
                            alt43 = 4
                        elif LA43 in {GROUP}:
                            alt43 = 5
                        else:
                            nvae = NoViableAltException("", 43, 0, self.input)

                            raise nvae

                        if alt43 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:9: ( testlist | fetch_expr ) NEWLINE
                            pass
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:9: ( testlist | fetch_expr )
                            alt42 = 2
                            LA42_0 = self.input.LA(1)

                            if LA42_0 in {
                                BIT_NOT,
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
                                alt42 = 1
                            elif LA42_0 == FETCH:
                                alt42 = 2
                            else:
                                nvae = NoViableAltException("", 42, 0, self.input)

                                raise nvae

                            if alt42 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:10: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt1124
                                )
                                self.testlist()

                                self._state.following.pop()

                            elif alt42 == 2:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:21: fetch_expr
                                self._state.following.append(
                                    self.FOLLOW_fetch_expr_in_aug_expr_stmt1128
                                )
                                self.fetch_expr()

                                self._state.following.pop()

                            self.match(
                                self.input,
                                NEWLINE,
                                self.FOLLOW_NEWLINE_in_aug_expr_stmt1131,
                            )

                        elif alt43 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:11: create_expr
                            self._state.following.append(
                                self.FOLLOW_create_expr_in_aug_expr_stmt1143
                            )
                            self.create_expr()

                            self._state.following.pop()

                        elif alt43 == 3:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:25: instantiate_expr
                            self._state.following.append(
                                self.FOLLOW_instantiate_expr_in_aug_expr_stmt1147
                            )
                            self.instantiate_expr()

                            self._state.following.pop()

                        elif alt43 == 4:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:44: get_expr
                            self._state.following.append(
                                self.FOLLOW_get_expr_in_aug_expr_stmt1151
                            )
                            self.get_expr()

                            self._state.following.pop()

                        elif alt43 == 5:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:55: group_expr
                            self._state.following.append(
                                self.FOLLOW_group_expr_in_aug_expr_stmt1155
                            )
                            self.group_expr()

                            self._state.following.pop()

                elif alt45 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:5: create_expr
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_aug_expr_stmt1179
                    )
                    self.create_expr()

                    self._state.following.pop()

                elif alt45 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:19: instantiate_expr
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_aug_expr_stmt1183
                    )
                    self.instantiate_expr()

                    self._state.following.pop()

                elif alt45 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:38: get_expr
                    self._state.following.append(
                        self.FOLLOW_get_expr_in_aug_expr_stmt1187
                    )
                    self.get_expr()

                    self._state.following.pop()

                elif alt45 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:49: group_expr
                    self._state.following.append(
                        self.FOLLOW_group_expr_in_aug_expr_stmt1191
                    )
                    self.group_expr()

                    self._state.following.pop()

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "aug_expr_stmt"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:1: fetch_expr : FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )? -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE);
    def fetch_expr(
        self,
    ):
        retval = self.fetch_expr_return()
        retval.start = self.input.LT(1)

        RECURSIVE14 = None
        ext = None
        path = None
        filter = None
        limit = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:12: ( FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )? -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:14: FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )?
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr1200)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr1204)
                ext = self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr1206)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr1210)
                path = self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:44: ( MATCH filter= test )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 == MATCH:
                    alt46 = 1
                if alt46 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:45: MATCH filter= test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr1213)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr1217)
                    filter = self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:65: ( LIMIT limit= test )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if LA47_0 == LIMIT:
                    alt47 = 1
                if alt47 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:66: LIMIT limit= test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr1222)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr1226)
                    limit = self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:85: ( RECURSIVE )?
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if LA48_0 == RECURSIVE:
                    alt48 = 1
                if alt48 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:85: RECURSIVE
                    RECURSIVE14 = self.match(
                        self.input, RECURSIVE, self.FOLLOW_RECURSIVE_in_fetch_expr1230
                    )

                # TEMPLATE REWRITE
                # 102:3: -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE)
                retval.st = self.templateLib.getInstanceOf(
                    "fetch_expr",
                    attributes={
                        "ext": ((ext is not None) and [ext.st] or [None])[0],
                        "path": ((path is not None) and [path.st] or [None])[0],
                        "filter": ((filter is not None) and [filter.st] or [None])[0],
                        "limit": ((limit is not None) and [limit.st] or [None])[0],
                        "recursive": RECURSIVE14,
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:1: test : expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st);
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
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:13: (expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:15: expr_= or_test ( IF cond= or_test ELSE else_expr= test )?
                self._state.following.append(self.FOLLOW_or_test_in_test1281)
                expr_ = self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:29: ( IF cond= or_test ELSE else_expr= test )?
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if LA49_0 == IF:
                    alt49 = 1
                if alt49 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:30: IF cond= or_test ELSE else_expr= test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test1284)

                    self._state.following.append(self.FOLLOW_or_test_in_test1288)
                    cond = self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test1290)

                    self._state.following.append(self.FOLLOW_test_in_test1294)
                    else_expr = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 106:13: -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:1: test_nocond : or_test -> test(expr=$or_test.st);
    def test_nocond(
        self,
    ):
        retval = self.test_nocond_return()
        retval.start = self.input.LT(1)

        or_test15 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:13: ( or_test -> test(expr=$or_test.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond1336)
                or_test15 = self.or_test()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 107:23: -> test(expr=$or_test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "test",
                    attributes={
                        "expr": ((or_test15 is not None) and [or_test15.st] or [None])[
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:1: or_test :exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs);
    def or_test(
        self,
    ):
        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:13: (exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:15: exprs+= and_test ( OR exprs+= and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test1358)
                exprs = self.and_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:31: ( OR exprs+= and_test )*
                while True:  # loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if LA50_0 == OR:
                        alt50 = 1

                    if alt50 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:32: OR exprs+= and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test1361)

                        self._state.following.append(
                            self.FOLLOW_and_test_in_or_test1365
                        )
                        exprs = self.and_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop50

                # TEMPLATE REWRITE
                # 108:53: -> or_test(exprs=$exprs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:1: and_test :exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs);
    def and_test(
        self,
    ):
        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:13: (exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:15: exprs+= not_test ( AND exprs+= not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test1388)
                exprs = self.not_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:31: ( AND exprs+= not_test )*
                while True:  # loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if LA51_0 == AND:
                        alt51 = 1

                    if alt51 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:32: AND exprs+= not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test1391)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test1395
                        )
                        exprs = self.not_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop51

                # TEMPLATE REWRITE
                # 109:54: -> and_test(exprs=$exprs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:1: not_test : ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st});
    def not_test(
        self,
    ):
        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        expr_ = None
        comparison16 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:13: ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st})
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if LA52_0 == NOT:
                    alt52 = 1
                elif LA52_0 in {
                    BIT_NOT,
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
                    alt52 = 2
                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:15: NOT expr_= not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1416)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1420)
                    expr_ = self.not_test()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 110:35: -> not_test(expr=$expr_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "not_test",
                        attributes={
                            "expr": ((expr_ is not None) and [expr_.st] or [None])[0]
                        },
                    )

                elif alt52 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:15: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test1446)
                    comparison16 = self.comparison()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 111:26: -> {$comparison.st}
                    retval.st = (
                        (comparison16 is not None) and [comparison16.st] or [None]
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:1: comparison :exprs+= expr ( comp_op exprs+= expr )* -> comparison(exprs=$exprsop=$comp_op.text);
    def comparison(
        self,
    ):
        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        comp_op17 = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:13: (exprs+= expr ( comp_op exprs+= expr )* -> comparison(exprs=$exprsop=$comp_op.text))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:15: exprs+= expr ( comp_op exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison1460)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:27: ( comp_op exprs+= expr )*
                while True:  # loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if LA53_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt53 = 1

                    if alt53 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:28: comp_op exprs+= expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison1463
                        )
                        comp_op17 = self.comp_op()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_expr_in_comparison1467)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop53

                # TEMPLATE REWRITE
                # 112:50: -> comparison(exprs=$exprsop=$comp_op.text)
                retval.st = self.templateLib.getInstanceOf(
                    "comparison",
                    attributes={
                        "exprs": list_exprs,
                        "op": (
                            (comp_op17 is not None)
                            and [self.input.toString(comp_op17.start, comp_op17.stop)]
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:1: comp_op : ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT );
    def comp_op(
        self,
    ):
        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:13: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                alt54 = 10
                LA54 = self.input.LA(1)
                if LA54 in {LT}:
                    alt54 = 1
                elif LA54 in {GT}:
                    alt54 = 2
                elif LA54 in {EQUALS}:
                    alt54 = 3
                elif LA54 in {GT_EQ}:
                    alt54 = 4
                elif LA54 in {LT_EQ}:
                    alt54 = 5
                elif LA54 in {NOT_EQ}:
                    alt54 = 6
                elif LA54 in {IN}:
                    alt54 = 7
                elif LA54 in {NOT}:
                    alt54 = 8
                elif LA54 in {IS}:
                    LA54_9 = self.input.LA(2)

                    if LA54_9 == NOT:
                        alt54 = 10
                    elif LA54_9 in {
                        BIT_NOT,
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
                        alt54 = 9
                    else:
                        nvae = NoViableAltException("", 54, 9, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae

                if alt54 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:15: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_comp_op1494)

                elif alt54 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:20: GT
                    self.match(self.input, GT, self.FOLLOW_GT_in_comp_op1498)

                elif alt54 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:25: EQUALS
                    self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op1502)

                elif alt54 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:34: GT_EQ
                    self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op1506)

                elif alt54 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:42: LT_EQ
                    self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op1510)

                elif alt54 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:50: NOT_EQ
                    self.match(self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op1514)

                elif alt54 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:59: IN
                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1518)

                elif alt54 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:64: NOT IN
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1522)

                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1524)

                elif alt54 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:73: IS
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1528)

                elif alt54 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:78: IS NOT
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1532)

                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1534)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:1: expr :exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs);
    def expr(
        self,
    ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:13: (exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:15: exprs+= xor_expr ( BIT_OR exprs+= xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr1551)
                exprs = self.xor_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:31: ( BIT_OR exprs+= xor_expr )*
                while True:  # loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if LA55_0 == BIT_OR:
                        alt55 = 1

                    if alt55 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:32: BIT_OR exprs+= xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr1554)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr1558)
                        exprs = self.xor_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop55

                # TEMPLATE REWRITE
                # 114:57: -> expr(exprs=$exprs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:1: xor_expr :exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs);
    def xor_expr(
        self,
    ):
        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:13: (exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:15: exprs+= and_expr ( XOR exprs+= and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1581)
                exprs = self.and_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:31: ( XOR exprs+= and_expr )*
                while True:  # loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if LA56_0 == XOR:
                        alt56 = 1

                    if alt56 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:32: XOR exprs+= and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr1584)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr1588
                        )
                        exprs = self.and_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop56

                # TEMPLATE REWRITE
                # 115:54: -> xor_expr(exprs=$exprs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:1: and_expr :exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs);
    def and_expr(
        self,
    ):
        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:13: (exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:15: exprs+= shift_expr ( BIT_AND exprs+= shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1611)
                exprs = self.shift_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:33: ( BIT_AND exprs+= shift_expr )*
                while True:  # loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if LA57_0 == BIT_AND:
                        alt57 = 1

                    if alt57 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:34: BIT_AND exprs+= shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr1614
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr1618
                        )
                        exprs = self.shift_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop57

                # TEMPLATE REWRITE
                # 116:62: -> and_expr(exprs=$exprs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:1: shift_expr :exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsop=$op);
    def shift_expr(
        self,
    ):
        retval = self.shift_expr_return()
        retval.start = self.input.LT(1)

        op = None
        list_exprs = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:13: (exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsop=$op))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:15: exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1639)
                exprs = self.arith_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:33: (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                while True:  # loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if LA59_0 in {LSHIFT, RSHIFT}:
                        alt59 = 1

                    if alt59 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:34: op= ( LSHIFT | RSHIFT ) exprs+= arith_expr
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:37: ( LSHIFT | RSHIFT )
                        alt58 = 2
                        LA58_0 = self.input.LA(1)

                        if LA58_0 == LSHIFT:
                            alt58 = 1
                        elif LA58_0 == RSHIFT:
                            alt58 = 2
                        else:
                            nvae = NoViableAltException("", 58, 0, self.input)

                            raise nvae

                        if alt58 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:38: LSHIFT
                            op = self.match(
                                self.input, LSHIFT, self.FOLLOW_LSHIFT_in_shift_expr1645
                            )

                        elif alt58 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:47: RSHIFT
                            op = self.match(
                                self.input, RSHIFT, self.FOLLOW_RSHIFT_in_shift_expr1649
                            )

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr1654
                        )
                        exprs = self.arith_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop59

                # TEMPLATE REWRITE
                # 117:75: -> shift_expr(exprs=$exprsop=$op)
                retval.st = self.templateLib.getInstanceOf(
                    "shift_expr", attributes={"exprs": list_exprs, "op": op}
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:1: arith_expr :terms+= term (op= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsop=$op);
    def arith_expr(
        self,
    ):
        retval = self.arith_expr_return()
        retval.start = self.input.LT(1)

        op = None
        list_terms = None
        terms = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:13: (terms+= term (op= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsop=$op))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:15: terms+= term (op= ( PLUS | MINUS ) terms+= term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr1680)
                terms = self.term()

                self._state.following.pop()
                if list_terms is None:
                    list_terms = []
                list_terms.append(terms.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:27: (op= ( PLUS | MINUS ) terms+= term )*
                while True:  # loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if LA61_0 in {MINUS, PLUS}:
                        alt61 = 1

                    if alt61 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:28: op= ( PLUS | MINUS ) terms+= term
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:31: ( PLUS | MINUS )
                        alt60 = 2
                        LA60_0 = self.input.LA(1)

                        if LA60_0 == PLUS:
                            alt60 = 1
                        elif LA60_0 == MINUS:
                            alt60 = 2
                        else:
                            nvae = NoViableAltException("", 60, 0, self.input)

                            raise nvae

                        if alt60 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:32: PLUS
                            op = self.match(
                                self.input, PLUS, self.FOLLOW_PLUS_in_arith_expr1686
                            )

                        elif alt60 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:39: MINUS
                            op = self.match(
                                self.input, MINUS, self.FOLLOW_MINUS_in_arith_expr1690
                            )

                        self._state.following.append(self.FOLLOW_term_in_arith_expr1695)
                        terms = self.term()

                        self._state.following.pop()
                        if list_terms is None:
                            list_terms = []
                        list_terms.append(terms.st)

                    else:
                        break  # loop61

                # TEMPLATE REWRITE
                # 118:60: -> arith_expr(terms=$termsop=$op)
                retval.st = self.templateLib.getInstanceOf(
                    "arith_expr", attributes={"terms": list_terms, "op": op}
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:1: term :factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsop=$op);
    def term(
        self,
    ):
        retval = self.term_return()
        retval.start = self.input.LT(1)

        op = None
        list_factors = None
        factors = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:13: (factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsop=$op))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:15: factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                self._state.following.append(self.FOLLOW_factor_in_term1727)
                factors = self.factor()

                self._state.following.pop()
                if list_factors is None:
                    list_factors = []
                list_factors.append(factors.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:31: (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                while True:  # loop63
                    alt63 = 2
                    LA63_0 = self.input.LA(1)

                    if LA63_0 in {DIV, IDIV, MOD, MUL}:
                        alt63 = 1

                    if alt63 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:32: op= ( MUL | DIV | MOD | IDIV ) factors+= factor
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:35: ( MUL | DIV | MOD | IDIV )
                        alt62 = 4
                        LA62 = self.input.LA(1)
                        if LA62 in {MUL}:
                            alt62 = 1
                        elif LA62 in {DIV}:
                            alt62 = 2
                        elif LA62 in {MOD}:
                            alt62 = 3
                        elif LA62 in {IDIV}:
                            alt62 = 4
                        else:
                            nvae = NoViableAltException("", 62, 0, self.input)

                            raise nvae

                        if alt62 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:36: MUL
                            op = self.match(
                                self.input, MUL, self.FOLLOW_MUL_in_term1733
                            )

                        elif alt62 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:42: DIV
                            op = self.match(
                                self.input, DIV, self.FOLLOW_DIV_in_term1737
                            )

                        elif alt62 == 3:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:48: MOD
                            op = self.match(
                                self.input, MOD, self.FOLLOW_MOD_in_term1741
                            )

                        elif alt62 == 4:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:54: IDIV
                            op = self.match(
                                self.input, IDIV, self.FOLLOW_IDIV_in_term1745
                            )

                        self._state.following.append(self.FOLLOW_factor_in_term1750)
                        factors = self.factor()

                        self._state.following.pop()
                        if list_factors is None:
                            list_factors = []
                        list_factors.append(factors.st)

                    else:
                        break  # loop63

                # TEMPLATE REWRITE
                # 119:78: -> term(factors=$factorsop=$op)
                retval.st = self.templateLib.getInstanceOf(
                    "term", attributes={"factors": list_factors, "op": op}
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:1: factor : (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st});
    def factor(
        self,
    ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)

        prefix = None
        factor_ = None
        power18 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:13: (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st})
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if LA65_0 in {BIT_NOT, MINUS, PLUS}:
                    alt65 = 1
                elif LA65_0 in {
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
                    alt65 = 2
                else:
                    nvae = NoViableAltException("", 65, 0, self.input)

                    raise nvae

                if alt65 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:15: prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:22: ( PLUS | MINUS | BIT_NOT )
                    alt64 = 3
                    LA64 = self.input.LA(1)
                    if LA64 in {PLUS}:
                        alt64 = 1
                    elif LA64 in {MINUS}:
                        alt64 = 2
                    elif LA64 in {BIT_NOT}:
                        alt64 = 3
                    else:
                        nvae = NoViableAltException("", 64, 0, self.input)

                        raise nvae

                    if alt64 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:23: PLUS
                        prefix = self.match(
                            self.input, PLUS, self.FOLLOW_PLUS_in_factor1781
                        )

                    elif alt64 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:30: MINUS
                        prefix = self.match(
                            self.input, MINUS, self.FOLLOW_MINUS_in_factor1785
                        )

                    elif alt64 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:38: BIT_NOT
                        prefix = self.match(
                            self.input, BIT_NOT, self.FOLLOW_BIT_NOT_in_factor1789
                        )

                    self._state.following.append(self.FOLLOW_factor_in_factor1794)
                    factor_ = self.factor()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 120:62: -> prefix_factor(factor=$factor_.stprefix=$prefix)
                    retval.st = self.templateLib.getInstanceOf(
                        "prefix_factor",
                        attributes={
                            "factor": (
                                (factor_ is not None) and [factor_.st] or [None]
                            )[0],
                            "prefix": prefix,
                        },
                    )

                elif alt65 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:15: power
                    self._state.following.append(self.FOLLOW_power_in_factor1824)
                    power18 = self.power()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 121:21: -> {$power.st}
                    retval.st = ((power18 is not None) and [power18.st] or [None])[0]

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:1: power : atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st);
    def power(
        self,
    ):
        retval = self.power_return()
        retval.start = self.input.LT(1)

        atom_expr19 = None
        factor20 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:13: ( atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power1841)
                atom_expr19 = self.atom_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:25: ( POWER factor )?
                alt66 = 2
                LA66_0 = self.input.LA(1)

                if LA66_0 == POWER:
                    alt66 = 1
                if alt66 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power1844)

                    self._state.following.append(self.FOLLOW_factor_in_power1846)
                    factor20 = self.factor()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 122:41: -> power(atom=$atom_expr.stfactor=$factor.st)
                retval.st = self.templateLib.getInstanceOf(
                    "power",
                    attributes={
                        "atom": (
                            (atom_expr19 is not None) and [atom_expr19.st] or [None]
                        )[0],
                        "factor": ((factor20 is not None) and [factor20.st] or [None])[
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:1: atom_expr : atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers);
    def atom_expr(
        self,
    ):
        retval = self.atom_expr_return()
        retval.start = self.input.LT(1)

        list_trailers = None
        atom21 = None
        trailers = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:13: ( atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:15: atom (trailers+= trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr1871)
                atom21 = self.atom()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:20: (trailers+= trailer )*
                while True:  # loop67
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if LA67_0 in {DOT, LBRACK}:
                        alt67 = 1

                    if alt67 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:21: trailers+= trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr1876
                        )
                        trailers = self.trailer()

                        self._state.following.pop()
                        if list_trailers is None:
                            list_trailers = []
                        list_trailers.append(trailers.st)

                    else:
                        break  # loop67

                # TEMPLATE REWRITE
                # 123:41: -> atom_expr(atom=$atom.sttrailers=$trailers)
                retval.st = self.templateLib.getInstanceOf(
                    "atom_expr",
                    attributes={
                        "atom": ((atom21 is not None) and [atom21.st] or [None])[0],
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:124:1: atom : ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false() ;
    def atom(
        self,
    ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)

        SETTING_ID26 = None
        DISTRIBUTION27 = None
        INTEGER29 = None
        FLOAT_NUMBER30 = None
        STRING31 = None
        test_ = None
        testlist_comp22 = None
        vector_comp23 = None
        dict_or_set_maker24 = None
        name25 = None
        arglist28 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:124:5: ( ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false() )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false()
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false()
                alt71 = 14
                LA71 = self.input.LA(1)
                if LA71 in {LPAREN}:
                    alt71 = 1
                elif LA71 in {LBRACK}:
                    alt71 = 2
                elif LA71 in {LT}:
                    alt71 = 3
                elif LA71 in {LBRACE}:
                    alt71 = 4
                elif LA71 in {LEN}:
                    alt71 = 5
                elif LA71 in {ID, UNDERSCORE}:
                    alt71 = 6
                elif LA71 in {SETTING_ID}:
                    alt71 = 7
                elif LA71 in {DISTRIBUTION}:
                    alt71 = 8
                elif LA71 in {INTEGER}:
                    alt71 = 9
                elif LA71 in {FLOAT_NUMBER}:
                    alt71 = 10
                elif LA71 in {STRING}:
                    alt71 = 11
                elif LA71 in {NONE}:
                    alt71 = 12
                elif LA71 in {TRUE}:
                    alt71 = 13
                elif LA71 in {FALSE}:
                    alt71 = 14
                else:
                    nvae = NoViableAltException("", 71, 0, self.input)

                    raise nvae

                if alt71 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:4: LPAREN test_= test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1901)

                    self._state.following.append(self.FOLLOW_test_in_atom1905)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1907)

                    # TEMPLATE REWRITE
                    # 125:29: -> parenthesized_expr(expr=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "parenthesized_expr",
                        attributes={
                            "expr": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt71 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:126:5: LBRACK ( testlist_comp )? RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom1922)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:126:12: ( testlist_comp )?
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if LA68_0 in {
                        BIT_NOT,
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
                        alt68 = 1
                    if alt68 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:126:12: testlist_comp
                        self._state.following.append(
                            self.FOLLOW_testlist_comp_in_atom1924
                        )
                        testlist_comp22 = self.testlist_comp()

                        self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom1927)

                    # TEMPLATE REWRITE
                    # 126:34: -> list(list_comp=$testlist_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list",
                        attributes={
                            "list_comp": (
                                (testlist_comp22 is not None)
                                and [testlist_comp22.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt71 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:127:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom1942)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:127:8: ( vector_comp )?
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if LA69_0 in {
                        BIT_NOT,
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
                        alt69 = 1
                    if alt69 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:127:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom1944
                        )
                        vector_comp23 = self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom1947)

                    # TEMPLATE REWRITE
                    # 127:24: -> vector(values=$vector_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "vector",
                        attributes={
                            "values": (
                                (vector_comp23 is not None)
                                and [vector_comp23.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt71 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom1962)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:12: ( dict_or_set_maker )?
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if LA70_0 in {
                        BIT_NOT,
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
                        alt70 = 1
                    if alt70 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom1964
                        )
                        dict_or_set_maker24 = self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom1967)

                    # TEMPLATE REWRITE
                    # 128:38: -> dict(dict_comp=$dict_or_set_maker.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dict",
                        attributes={
                            "dict_comp": (
                                (dict_or_set_maker24 is not None)
                                and [dict_or_set_maker24.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt71 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:129:5: LEN LPAREN test_= test RPAREN
                    self.match(self.input, LEN, self.FOLLOW_LEN_in_atom1982)

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1984)

                    self._state.following.append(self.FOLLOW_test_in_atom1988)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1990)

                    # TEMPLATE REWRITE
                    # 129:34: -> len(value=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "len",
                        attributes={
                            "value": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt71 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:130:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom2005)
                    name25 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 130:10: -> {$name.st}
                    retval.st = ((name25 is not None) and [name25.st] or [None])[0]

                elif alt71 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:131:5: SETTING_ID
                    SETTING_ID26 = self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom2015
                    )

                    # TEMPLATE REWRITE
                    # 131:16: -> setting_id(id=$SETTING_ID.text)
                    retval.st = self.templateLib.getInstanceOf(
                        "setting_id", attributes={"id": SETTING_ID26.text}
                    )

                elif alt71 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:132:5: DISTRIBUTION LPAREN arglist RPAREN
                    DISTRIBUTION27 = self.match(
                        self.input, DISTRIBUTION, self.FOLLOW_DISTRIBUTION_in_atom2031
                    )

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom2033)

                    self._state.following.append(self.FOLLOW_arglist_in_atom2035)
                    arglist28 = self.arglist()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom2037)

                    # TEMPLATE REWRITE
                    # 132:40: -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "distribution",
                        attributes={
                            "name": DISTRIBUTION27.text,
                            "arglist": (
                                (arglist28 is not None) and [arglist28.st] or [None]
                            )[0],
                        },
                    )

                elif alt71 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:133:5: INTEGER
                    INTEGER29 = self.match(
                        self.input, INTEGER, self.FOLLOW_INTEGER_in_atom2057
                    )

                    # TEMPLATE REWRITE
                    # 133:13: -> {$INTEGER.text}
                    retval.st = INTEGER29.text

                elif alt71 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:134:5: FLOAT_NUMBER
                    FLOAT_NUMBER30 = self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom2067
                    )

                    # TEMPLATE REWRITE
                    # 134:18: -> {$FLOAT_NUMBER.text}
                    retval.st = FLOAT_NUMBER30.text

                elif alt71 == 11:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:5: STRING
                    STRING31 = self.match(
                        self.input, STRING, self.FOLLOW_STRING_in_atom2077
                    )

                    # TEMPLATE REWRITE
                    # 135:12: -> {$STRING.text}
                    retval.st = STRING31.text

                elif alt71 == 12:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:136:5: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom2088)

                    # TEMPLATE REWRITE
                    # 136:10: -> null(
                    retval.st = self.templateLib.getInstanceOf("null")

                elif alt71 == 13:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:137:5: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom2100)

                    # TEMPLATE REWRITE
                    # 137:10: -> true(
                    retval.st = self.templateLib.getInstanceOf("true")

                elif alt71 == 14:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:5: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom2112)

                    # TEMPLATE REWRITE
                    # 138:11: -> false(
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:1: name : ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text});
    def name(
        self,
    ):
        retval = self.name_return()
        retval.start = self.input.LT(1)

        ID32 = None
        UNDERSCORE33 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:5: ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text})
                alt72 = 2
                LA72_0 = self.input.LA(1)

                if LA72_0 == ID:
                    alt72 = 1
                elif LA72_0 == UNDERSCORE:
                    alt72 = 2
                else:
                    nvae = NoViableAltException("", 72, 0, self.input)

                    raise nvae

                if alt72 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:143:3: ID
                    ID32 = self.match(self.input, ID, self.FOLLOW_ID_in_name2132)

                    # TEMPLATE REWRITE
                    # 143:6: -> {$ID.text}
                    retval.st = ID32.text

                elif alt72 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:144:5: UNDERSCORE
                    UNDERSCORE33 = self.match(
                        self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_name2142
                    )

                    # TEMPLATE REWRITE
                    # 144:16: -> {$UNDERSCORE.text}
                    retval.st = UNDERSCORE33.text

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "name"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:1: testlist_comp :exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) ;
    def testlist_comp(
        self,
    ):
        retval = self.testlist_comp_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        to = None
        step = None
        comp_for34 = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:15: (exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:17: exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                self._state.following.append(self.FOLLOW_test_in_testlist_comp2161)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:29: ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                alt75 = 3
                LA75 = self.input.LA(1)
                if LA75 in {FOR}:
                    alt75 = 1
                elif LA75 in {COMMA, RBRACK}:
                    alt75 = 2
                elif LA75 in {RANGE}:
                    alt75 = 3
                else:
                    nvae = NoViableAltException("", 75, 0, self.input)

                    raise nvae

                if alt75 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:31: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp2165
                    )
                    comp_for34 = self.comp_for()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 155:40: -> list_comp(expr=$exprs[0]for=$comp_for.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list_comp",
                        attributes={
                            "expr": list_exprs[0],
                            "for": (
                                (comp_for34 is not None) and [comp_for34.st] or [None]
                            )[0],
                        },
                    )

                elif alt75 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:24: ( COMMA exprs+= test )*
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:24: ( COMMA exprs+= test )*
                    while True:  # loop73
                        alt73 = 2
                        LA73_0 = self.input.LA(1)

                        if LA73_0 == COMMA:
                            alt73 = 1

                        if alt73 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:25: COMMA exprs+= test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp2205,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp2209
                            )
                            exprs = self.test()

                            self._state.following.pop()
                            if list_exprs is None:
                                list_exprs = []
                            list_exprs.append(exprs.st)

                        else:
                            break  # loop73

                    # TEMPLATE REWRITE
                    # 156:45: -> test_list(exprs=$exprs)
                    retval.st = self.templateLib.getInstanceOf(
                        "test_list", attributes={"exprs": list_exprs}
                    )

                elif alt75 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:157:24: RANGE to= test ( STEP step= test )?
                    self.match(
                        self.input, RANGE, self.FOLLOW_RANGE_in_testlist_comp2245
                    )

                    self._state.following.append(self.FOLLOW_test_in_testlist_comp2249)
                    to = self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:157:38: ( STEP step= test )?
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if LA74_0 == STEP:
                        alt74 = 1
                    if alt74 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:157:39: STEP step= test
                        self.match(
                            self.input, STEP, self.FOLLOW_STEP_in_testlist_comp2252
                        )

                        self._state.following.append(
                            self.FOLLOW_test_in_testlist_comp2256
                        )
                        step = self.test()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 157:56: -> range(from=$exprs[0]to=$to.ststep=$step.st)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:1: vector_comp : x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st);
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
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:15: (x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:17: x= expr COMMA y= expr COMMA z= expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp2305)
                x = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp2307)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp2311)
                y = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp2313)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp2317)
                z = self.expr()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 160:50: -> vector_comp(x=$x.sty=$y.stz=$z.st)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:162:1: trailer : ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st));
    def trailer(
        self,
    ):
        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        subscriptlist35 = None
        name36 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:162:15: ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st))
                alt76 = 2
                LA76_0 = self.input.LA(1)

                if LA76_0 == LBRACK:
                    alt76 = 1
                elif LA76_0 == DOT:
                    alt76 = 2
                else:
                    nvae = NoViableAltException("", 76, 0, self.input)

                    raise nvae

                if alt76 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:162:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer2351)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer2353
                    )
                    subscriptlist35 = self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer2355)

                    # TEMPLATE REWRITE
                    # 162:45: -> index(index=$subscriptlist.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "index",
                        attributes={
                            "index": (
                                (subscriptlist35 is not None)
                                and [subscriptlist35.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt76 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:163:17: DOT name
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer2383)

                    self._state.following.append(self.FOLLOW_name_in_trailer2385)
                    name36 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 163:26: -> dot_attr(attr=$name.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dot_attr",
                        attributes={
                            "attr": ((name36 is not None) and [name36.st] or [None])[0]
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:1: arglist :args+= argument ( COMMA args+= argument )* -> arg_list(args=$args);
    def arglist(
        self,
    ):
        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        list_args = None
        args = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:15: (args+= argument ( COMMA args+= argument )* -> arg_list(args=$args))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:17: args+= argument ( COMMA args+= argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist2409)
                args = self.argument()

                self._state.following.pop()
                if list_args is None:
                    list_args = []
                list_args.append(args.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:32: ( COMMA args+= argument )*
                while True:  # loop77
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if LA77_0 == COMMA:
                        alt77 = 1

                    if alt77 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:33: COMMA args+= argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2412)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist2416
                        )
                        args = self.argument()

                        self._state.following.pop()
                        if list_args is None:
                            list_args = []
                        list_args.append(args.st)

                    else:
                        break  # loop77

                # TEMPLATE REWRITE
                # 164:56: -> arg_list(args=$args)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:1: argument : kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st);
    def argument(
        self,
    ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)

        kw_or_arg = None
        arg = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:15: (kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:17: kw_or_arg= test ( ASSIGN arg= test )?
                self._state.following.append(self.FOLLOW_test_in_argument2441)
                kw_or_arg = self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:32: ( ASSIGN arg= test )?
                alt78 = 2
                LA78_0 = self.input.LA(1)

                if LA78_0 == ASSIGN:
                    alt78 = 1
                if alt78 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:33: ASSIGN arg= test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument2444)

                    self._state.following.append(self.FOLLOW_test_in_argument2448)
                    arg = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 165:51: -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:166:1: subscriptlist :subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs);
    def subscriptlist(
        self,
    ):
        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        list_subs = None
        subs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:166:15: (subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:166:17: subs+= subscript_ ( COMMA subs+= subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist2473
                )
                subs = self.subscript_()

                self._state.following.pop()
                if list_subs is None:
                    list_subs = []
                list_subs.append(subs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:166:34: ( COMMA subs+= subscript_ )*
                while True:  # loop79
                    alt79 = 2
                    LA79_0 = self.input.LA(1)

                    if LA79_0 == COMMA:
                        alt79 = 1

                    if alt79 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:166:35: COMMA subs+= subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist2476
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist2480
                        )
                        subs = self.subscript_()

                        self._state.following.pop()
                        if list_subs is None:
                            list_subs = []
                        list_subs.append(subs.st)

                    else:
                        break  # loop79

                # TEMPLATE REWRITE
                # 166:60: -> subscript_list(subs=$subs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:1: subscript_ : (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st));
    def subscript_(
        self,
    ):
        retval = self.subscript__return()
        retval.start = self.input.LT(1)

        to = None
        step = None
        COLON37 = None
        COLON38 = None
        from_ = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:15: (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st))
                alt85 = 2
                LA85_0 = self.input.LA(1)

                if LA85_0 in {
                    BIT_NOT,
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
                    alt85 = 1
                elif LA85_0 == COLON:
                    alt85 = 2
                else:
                    nvae = NoViableAltException("", 85, 0, self.input)

                    raise nvae

                if alt85 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:17: from_= test ( COLON to= ( test )? step= ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_2503)
                    from_ = self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:28: ( COLON to= ( test )? step= ( sliceop )? )?
                    alt82 = 2
                    LA82_0 = self.input.LA(1)

                    if LA82_0 == COLON:
                        alt82 = 1
                    if alt82 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:29: COLON to= ( test )? step= ( sliceop )?
                        COLON37 = self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_2506
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:38: ( test )?
                        alt80 = 2
                        LA80_0 = self.input.LA(1)

                        if LA80_0 in {
                            BIT_NOT,
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:39: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_2511
                            )
                            to = self.test()

                            self._state.following.pop()

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:51: ( sliceop )?
                        alt81 = 2
                        LA81_0 = self.input.LA(1)

                        if LA81_0 == COLON:
                            alt81 = 1
                        if alt81 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:167:52: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_2518
                            )
                            step = self.sliceop()

                            self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 167:64: -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={
                            "from": ((from_ is not None) and [from_.st] or [None])[0],
                            "colon": COLON37,
                            "to": to.st,
                            "step": step.st,
                        },
                    )

                elif alt85 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:168:17: COLON to= ( test )? step= ( sliceop )?
                    COLON38 = self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_subscript_2564
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:168:26: ( test )?
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if LA83_0 in {
                        BIT_NOT,
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
                        alt83 = 1
                    if alt83 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:168:27: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_2569)
                        to = self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:168:39: ( sliceop )?
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if LA84_0 == COLON:
                        alt84 = 1
                    if alt84 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:168:40: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_2576
                        )
                        step = self.sliceop()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 168:51: -> subscript(colon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={"colon": COLON38, "to": to.st, "step": step.st},
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:169:1: sliceop : COLON ( test )? -> subscipt_step(step=$test.st);
    def sliceop(
        self,
    ):
        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        test39 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:169:15: ( COLON ( test )? -> subscipt_step(step=$test.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:169:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop2611)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:169:23: ( test )?
                alt86 = 2
                LA86_0 = self.input.LA(1)

                if LA86_0 in {
                    BIT_NOT,
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
                    alt86 = 1
                if alt86 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:169:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop2613)
                    test39 = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 169:29: -> subscipt_step(step=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "subscipt_step",
                    attributes={
                        "step": ((test39 is not None) and [test39.st] or [None])[0]
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:171:1: exprlist :exprs+= expr ( COMMA exprs+= expr )* -> test_list(exprs=$exprs);
    def exprlist(
        self,
    ):
        retval = self.exprlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:171:10: (exprs+= expr ( COMMA exprs+= expr )* -> test_list(exprs=$exprs))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:171:12: exprs+= expr ( COMMA exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_exprlist2633)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:171:24: ( COMMA exprs+= expr )*
                while True:  # loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if LA87_0 == COMMA:
                        alt87 = 1

                    if alt87 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:171:25: COMMA exprs+= expr
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist2636)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist2640)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop87

                # TEMPLATE REWRITE
                # 171:45: -> test_list(exprs=$exprs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:172:1: testlist :exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs);
    def testlist(
        self,
    ):
        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:172:10: (exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:172:12: exprs+= test ( COMMA exprs+= test )*
                self._state.following.append(self.FOLLOW_test_in_testlist2660)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:172:24: ( COMMA exprs+= test )*
                while True:  # loop88
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if LA88_0 == COMMA:
                        alt88 = 1

                    if alt88 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:172:25: COMMA exprs+= test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist2663)

                        self._state.following.append(self.FOLLOW_test_in_testlist2667)
                        exprs = self.test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop88

                # TEMPLATE REWRITE
                # 172:45: -> test_list(exprs=$exprs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:173:1: dict_or_set_maker :exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs)) ;
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
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:173:18: (exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs)) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:174:3: exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs))
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker2688)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:174:15: ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs))
                alt93 = 2
                LA93_0 = self.input.LA(1)

                if LA93_0 == COLON:
                    alt93 = 1
                elif LA93_0 in {COMMA, FOR, RBRACE}:
                    alt93 = 2
                else:
                    nvae = NoViableAltException("", 93, 0, self.input)

                    raise nvae

                if alt93 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:174:17: COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker2692
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker2696
                    )
                    values = self.test()

                    self._state.following.pop()
                    if list_values is None:
                        list_values = []
                    list_values.append(values.st)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:174:36: (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* )
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if LA90_0 == FOR:
                        alt90 = 1
                    elif LA90_0 in {COMMA, RBRACE}:
                        alt90 = 2
                    else:
                        nvae = NoViableAltException("", 90, 0, self.input)

                        raise nvae

                    if alt90 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:174:37: for_= comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker2701
                        )
                        for_ = self.comp_for()

                        self._state.following.pop()

                        # TEMPLATE REWRITE
                        # 174:51: -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "dict_comp",
                            attributes={
                                "key": list_exprs[0],
                                "value": list_values[0],
                                "for": ((for_ is not None) and [for_.st] or [None])[0],
                            },
                        )

                    elif alt90 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:175:38: ( COMMA exprs+= test COLON values+= test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:175:38: ( COMMA exprs+= test COLON values+= test )*
                        while True:  # loop89
                            alt89 = 2
                            LA89_0 = self.input.LA(1)

                            if LA89_0 == COMMA:
                                alt89 = 1

                            if alt89 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:175:39: COMMA exprs+= test COLON values+= test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker2760,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker2764
                                )
                                exprs = self.test()

                                self._state.following.pop()
                                if list_exprs is None:
                                    list_exprs = []
                                list_exprs.append(exprs.st)

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker2766,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker2770
                                )
                                values = self.test()

                                self._state.following.pop()
                                if list_values is None:
                                    list_values = []
                                list_values.append(values.st)

                            else:
                                break  # loop89

                    # TEMPLATE REWRITE
                    # 175:79: -> key_value_list(keys=$exprsvalues=$values)
                    retval.st = self.templateLib.getInstanceOf(
                        "key_value_list",
                        attributes={"keys": list_exprs, "values": list_values},
                    )

                elif alt93 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:176:17: (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:176:17: (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* )
                    alt92 = 2
                    LA92_0 = self.input.LA(1)

                    if LA92_0 == FOR:
                        alt92 = 1
                    elif LA92_0 in {COMMA, RBRACE}:
                        alt92 = 2
                    else:
                        nvae = NoViableAltException("", 92, 0, self.input)

                        raise nvae

                    if alt92 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:176:18: for_= comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker2808
                        )
                        for_ = self.comp_for()

                        self._state.following.pop()

                        # TEMPLATE REWRITE
                        # 176:32: -> list_comp(expr=$exprs[0]for=$for_.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "list_comp",
                            attributes={
                                "expr": list_exprs[0],
                                "for": ((for_ is not None) and [for_.st] or [None])[0],
                            },
                        )

                    elif alt92 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:177:19: ( COMMA exprs+= test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:177:19: ( COMMA exprs+= test )*
                        while True:  # loop91
                            alt91 = 2
                            LA91_0 = self.input.LA(1)

                            if LA91_0 == COMMA:
                                alt91 = 1

                            if alt91 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:177:20: COMMA exprs+= test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker2846,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker2850
                                )
                                exprs = self.test()

                                self._state.following.pop()
                                if list_exprs is None:
                                    list_exprs = []
                                list_exprs.append(exprs.st)

                            else:
                                break  # loop91

                    # TEMPLATE REWRITE
                    # 177:42: -> test_list(exprs=$exprs)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:181:1: comp_iter : comp= ( comp_for | comp_if ) -> {$comp.st};
    def comp_iter(
        self,
    ):
        retval = self.comp_iter_return()
        retval.start = self.input.LT(1)

        comp = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:181:11: (comp= ( comp_for | comp_if ) -> {$comp.st})
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:181:13: comp= ( comp_for | comp_if )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:181:18: ( comp_for | comp_if )
                alt94 = 2
                LA94_0 = self.input.LA(1)

                if LA94_0 == FOR:
                    alt94 = 1
                elif LA94_0 == IF:
                    alt94 = 2
                else:
                    nvae = NoViableAltException("", 94, 0, self.input)

                    raise nvae

                if alt94 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:181:19: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter2891)
                    comp = self.comp_for()

                    self._state.following.pop()

                elif alt94 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:181:30: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter2895)
                    comp = self.comp_if()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 181:39: -> {$comp.st}
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:182:1: comp_for : FOR exprlist IN or_test ( comp_iter )? -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st);
    def comp_for(
        self,
    ):
        retval = self.comp_for_return()
        retval.start = self.input.LT(1)

        exprlist40 = None
        or_test41 = None
        comp_iter42 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:182:11: ( FOR exprlist IN or_test ( comp_iter )? -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:182:13: FOR exprlist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for2908)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for2910)
                exprlist40 = self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for2912)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for2914)
                or_test41 = self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:182:37: ( comp_iter )?
                alt95 = 2
                LA95_0 = self.input.LA(1)

                if LA95_0 in {FOR, IF}:
                    alt95 = 1
                if alt95 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:182:37: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for2916)
                    comp_iter42 = self.comp_iter()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 182:48: -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st)
                retval.st = self.templateLib.getInstanceOf(
                    "comp_for",
                    attributes={
                        "exprs": (
                            (exprlist40 is not None) and [exprlist40.st] or [None]
                        )[0],
                        "seq": ((or_test41 is not None) and [or_test41.st] or [None])[
                            0
                        ],
                        "comp_iter": (
                            (comp_iter42 is not None) and [comp_iter42.st] or [None]
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:183:1: comp_if : IF test_nocond ( comp_iter )? -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st);
    def comp_if(
        self,
    ):
        retval = self.comp_if_return()
        retval.start = self.input.LT(1)

        test_nocond43 = None
        comp_iter44 = None

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:183:11: ( IF test_nocond ( comp_iter )? -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st))
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:183:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if2945)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if2947)
                test_nocond43 = self.test_nocond()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:183:28: ( comp_iter )?
                alt96 = 2
                LA96_0 = self.input.LA(1)

                if LA96_0 in {FOR, IF}:
                    alt96 = 1
                if alt96 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:183:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if2949)
                    comp_iter44 = self.comp_iter()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 183:39: -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st)
                retval.st = self.templateLib.getInstanceOf(
                    "comp_if",
                    attributes={
                        "cond": (
                            (test_nocond43 is not None) and [test_nocond43.st] or [None]
                        )[0],
                        "comp_iter": (
                            (comp_iter44 is not None) and [comp_iter44.st] or [None]
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

    FOLLOW_declaration_in_scenario59 = frozenset([1, 73, 100, 109, 123])
    FOLLOW_NEWLINE_in_scenario61 = frozenset([1, 73, 100, 109, 123])
    FOLLOW_settings_in_scenario64 = frozenset([1, 109, 123])
    FOLLOW_stage_in_scenario67 = frozenset([1, 123])
    FOLLOW_writers_in_scenario70 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration112 = frozenset([43])
    FOLLOW_ID_in_declaration114 = frozenset([15, 73])
    FOLLOW_COLON_in_declaration117 = frozenset([43, 119])
    FOLLOW_name_in_declaration119 = frozenset([73])
    FOLLOW_NEWLINE_in_declaration123 = frozenset([1])
    FOLLOW_SETTINGS_in_settings146 = frozenset([15])
    FOLLOW_COLON_in_settings148 = frozenset([73])
    FOLLOW_NEWLINE_in_settings150 = frozenset([49])
    FOLLOW_INDENT_in_settings152 = frozenset([43])
    FOLLOW_setting_in_settings156 = frozenset([19, 43])
    FOLLOW_DEDENT_in_settings159 = frozenset([1])
    FOLLOW_STAGE_in_stage181 = frozenset([15])
    FOLLOW_COLON_in_stage183 = frozenset([73])
    FOLLOW_NEWLINE_in_stage185 = frozenset([49])
    FOLLOW_INDENT_in_stage187 = frozenset(
        [
            11,
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
            63,
            65,
            69,
            74,
            76,
            80,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_stmts_in_stage189 = frozenset([19])
    FOLLOW_DEDENT_in_stage191 = frozenset([1])
    FOLLOW_WRITERS_in_writers206 = frozenset([15])
    FOLLOW_COLON_in_writers208 = frozenset([73])
    FOLLOW_NEWLINE_in_writers210 = frozenset([49])
    FOLLOW_INDENT_in_writers212 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_stmt_in_writers217 = frozenset(
        [
            11,
            19,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_writer_in_writers221 = frozenset(
        [
            11,
            19,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_DEDENT_in_writers225 = frozenset([1])
    FOLLOW_ID_in_setting249 = frozenset([5])
    FOLLOW_ASSIGN_in_setting251 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_setting253 = frozenset([73])
    FOLLOW_NEWLINE_in_setting255 = frozenset([1])
    FOLLOW_open_stmt_in_stmts289 = frozenset(
        [
            11,
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_aug_expr_stmt_in_stmts296 = frozenset(
        [
            1,
            11,
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_edit_stmt_in_stmts300 = frozenset(
        [
            1,
            11,
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_behavior_stmt_in_stmts304 = frozenset(
        [
            1,
            11,
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_ID_in_writer330 = frozenset([15])
    FOLLOW_COLON_in_writer332 = frozenset([73])
    FOLLOW_NEWLINE_in_writer334 = frozenset([49])
    FOLLOW_INDENT_in_writer336 = frozenset([43])
    FOLLOW_writer_param_in_writer340 = frozenset([19, 43])
    FOLLOW_DEDENT_in_writer343 = frozenset([1])
    FOLLOW_ID_in_writer_param372 = frozenset([5])
    FOLLOW_ASSIGN_in_writer_param374 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_writer_param376 = frozenset([73])
    FOLLOW_NEWLINE_in_writer_param378 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt404 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_open_stmt406 = frozenset([73])
    FOLLOW_NEWLINE_in_open_stmt408 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt424 = frozenset([43, 115, 119])
    FOLLOW_TIMELINE_in_edit_stmt427 = frozenset([15])
    FOLLOW_COLON_in_edit_stmt429 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_stmt431 = frozenset([49])
    FOLLOW_INDENT_in_edit_stmt433 = frozenset([43, 119])
    FOLLOW_name_in_edit_stmt438 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_edit_stmt442 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_stmt444 = frozenset([19, 43, 119])
    FOLLOW_DEDENT_in_edit_stmt448 = frozenset([1])
    FOLLOW_name_in_edit_stmt484 = frozenset([15])
    FOLLOW_edit_block_in_edit_stmt486 = frozenset([1])
    FOLLOW_CREATE_in_create_expr496 = frozenset(
        [
            11,
            13,
            21,
            31,
            33,
            37,
            43,
            51,
            54,
            55,
            56,
            59,
            63,
            65,
            68,
            69,
            74,
            76,
            84,
            101,
            102,
            103,
            111,
            112,
            118,
            119,
        ]
    )
    FOLLOW_test_in_create_expr498 = frozenset([13, 37, 59, 68, 102, 103, 111])
    FOLLOW_STEREO_in_create_expr508 = frozenset([13])
    FOLLOW_CAMERA_in_create_expr511 = frozenset([15, 73])
    FOLLOW_shapes_in_create_expr515 = frozenset([15, 73])
    FOLLOW_light_type_in_create_expr519 = frozenset([58])
    FOLLOW_LIGHT_in_create_expr521 = frozenset([15, 73])
    FOLLOW_FROM_in_create_expr525 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_create_expr527 = frozenset([15, 73])
    FOLLOW_edit_block_in_create_expr531 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr535 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr544 = frozenset([15])
    FOLLOW_simple_block_in_create_expr547 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr588 = frozenset(
        [
            11,
            21,
            31,
            33,
            37,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_test_in_instantiate_expr591 = frozenset([37])
    FOLLOW_FROM_in_instantiate_expr595 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_instantiate_expr597 = frozenset([15, 73])
    FOLLOW_edit_block_in_instantiate_expr600 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr604 = frozenset([1])
    FOLLOW_GROUP_in_group_expr618 = frozenset([55])
    FOLLOW_LBRACK_in_group_expr620 = frozenset([43, 119])
    FOLLOW_name_in_group_expr622 = frozenset([16, 89])
    FOLLOW_COMMA_in_group_expr625 = frozenset([43, 119])
    FOLLOW_name_in_group_expr627 = frozenset([16, 89])
    FOLLOW_RBRACK_in_group_expr631 = frozenset([15, 73])
    FOLLOW_edit_block_in_group_expr634 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr638 = frozenset([1])
    FOLLOW_GET_in_get_expr654 = frozenset(
        [
            11,
            13,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            58,
            63,
            65,
            68,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_CAMERA_in_get_expr658 = frozenset([6])
    FOLLOW_LIGHT_in_get_expr662 = frozenset([6])
    FOLLOW_MATERIAL_in_get_expr666 = frozenset([6])
    FOLLOW_name_in_get_expr670 = frozenset([6])
    FOLLOW_AT_in_get_expr673 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_get_expr677 = frozenset([15, 73])
    FOLLOW_simple_block_in_get_expr680 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr684 = frozenset([1])
    FOLLOW_COLON_in_edit_block695 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_block697 = frozenset([49])
    FOLLOW_INDENT_in_edit_block699 = frozenset(
        [14, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_attr_in_edit_block702 = frozenset(
        [14, 19, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block706 = frozenset(
        [14, 19, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_DEDENT_in_edit_block710 = frozenset([1])
    FOLLOW_COLON_in_simple_block717 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_block719 = frozenset([49])
    FOLLOW_INDENT_in_simple_block721 = frozenset([43, 119])
    FOLLOW_simple_attr_in_simple_block723 = frozenset([19, 43, 119])
    FOLLOW_DEDENT_in_simple_block726 = frozenset([1])
    FOLLOW_core_attr_in_attr746 = frozenset([1])
    FOLLOW_simple_attr_in_attr750 = frozenset([1])
    FOLLOW_compound_attr_in_attr754 = frozenset([1])
    FOLLOW_name_in_simple_attr768 = frozenset(
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
            63,
            65,
            69,
            73,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_COLON_in_simple_attr771 = frozenset([43, 119])
    FOLLOW_name_in_simple_attr773 = frozenset(
        [
            11,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            73,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_test_in_simple_attr777 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_attr780 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr789 = frozenset([79])
    FOLLOW_ON_in_compound_attr791 = frozenset([43, 119])
    FOLLOW_name_in_compound_attr793 = frozenset([15, 73])
    FOLLOW_ROT_AROUND_in_compound_attr797 = frozenset([43, 119])
    FOLLOW_name_in_compound_attr799 = frozenset([15, 73])
    FOLLOW_PHYSICS_in_compound_attr803 = frozenset([15, 73])
    FOLLOW_simple_block_in_compound_attr807 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr811 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr828 = frozenset([8, 116])
    FOLLOW_AXIS_in_core_attr830 = frozenset([116])
    FOLLOW_TO_in_core_attr833 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr835 = frozenset([73])
    FOLLOW_CAM_TRANSLATE_in_core_attr843 = frozenset([116])
    FOLLOW_TO_in_core_attr845 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr847 = frozenset([73])
    FOLLOW_ROTATE_in_core_attr855 = frozenset(
        [
            8,
            11,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_AXIS_in_core_attr857 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr860 = frozenset([73, 82])
    FOLLOW_ORDER_in_core_attr862 = frozenset([73])
    FOLLOW_SCALE_in_core_attr871 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr873 = frozenset([73])
    FOLLOW_LOOK_AT_in_core_attr881 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr883 = frozenset([73])
    FOLLOW_UP_AXIS_in_core_attr891 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr893 = frozenset([73])
    FOLLOW_SIZE_in_core_attr901 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr903 = frozenset([73])
    FOLLOW_SEMANTICS_in_core_attr911 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr913 = frozenset([73])
    FOLLOW_VISIBLE_in_core_attr921 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr923 = frozenset([73])
    FOLLOW_NEWLINE_in_core_attr929 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt939 = frozenset([15])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt941 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block948 = frozenset([73])
    FOLLOW_NEWLINE_in_inner_behavior_block950 = frozenset([49])
    FOLLOW_INDENT_in_inner_behavior_block952 = frozenset(
        [14, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_attr_in_inner_behavior_block954 = frozenset(
        [14, 19, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_DEDENT_in_inner_behavior_block957 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt968 = frozenset([15])
    FOLLOW_behavior_block_in_behavior_stmt970 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr978 = frozenset(
        [
            11,
            21,
            31,
            33,
            36,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            114,
            118,
            119,
        ]
    )
    FOLLOW_test_in_behavior_expr980 = frozenset([36, 114])
    FOLLOW_set_in_behavior_expr983 = frozenset([1])
    FOLLOW_COLON_in_behavior_block996 = frozenset([73])
    FOLLOW_NEWLINE_in_behavior_block998 = frozenset([49])
    FOLLOW_INDENT_in_behavior_block1000 = frozenset(
        [
            11,
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_aug_expr_stmt_in_behavior_block1003 = frozenset(
        [
            11,
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_edit_stmt_in_behavior_block1007 = frozenset(
        [
            11,
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_DEDENT_in_behavior_block1011 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt1023 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_expr_stmt1028 = frozenset(
        [
            11,
            21,
            31,
            32,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_ASSIGN_in_expr_stmt1032 = frozenset(
        [
            11,
            21,
            31,
            32,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_testlist_in_expr_stmt1038 = frozenset([73])
    FOLLOW_fetch_expr_in_expr_stmt1042 = frozenset([73])
    FOLLOW_NEWLINE_in_expr_stmt1045 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt1080 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_aug_expr_stmt1090 = frozenset(
        [
            11,
            21,
            31,
            32,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            73,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt1093 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt1097 = frozenset([73])
    FOLLOW_NEWLINE_in_aug_expr_stmt1101 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt1111 = frozenset(
        [
            11,
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt1124 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt1128 = frozenset([73])
    FOLLOW_NEWLINE_in_aug_expr_stmt1131 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt1143 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt1147 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt1151 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt1155 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt1179 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt1183 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt1187 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt1191 = frozenset([1])
    FOLLOW_FETCH_in_fetch_expr1200 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_fetch_expr1204 = frozenset([37])
    FOLLOW_FROM_in_fetch_expr1206 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_fetch_expr1210 = frozenset([1, 60, 67, 90])
    FOLLOW_MATCH_in_fetch_expr1213 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_fetch_expr1217 = frozenset([1, 60, 90])
    FOLLOW_LIMIT_in_fetch_expr1222 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_fetch_expr1226 = frozenset([1, 90])
    FOLLOW_RECURSIVE_in_fetch_expr1230 = frozenset([1])
    FOLLOW_or_test_in_test1281 = frozenset([1, 47])
    FOLLOW_IF_in_test1284 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_or_test_in_test1288 = frozenset([26])
    FOLLOW_ELSE_in_test1290 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_test1294 = frozenset([1])
    FOLLOW_or_test_in_test_nocond1336 = frozenset([1])
    FOLLOW_and_test_in_or_test1358 = frozenset([1, 81])
    FOLLOW_OR_in_or_test1361 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_and_test_in_or_test1365 = frozenset([1, 81])
    FOLLOW_not_test_in_and_test1388 = frozenset([1, 4])
    FOLLOW_AND_in_and_test1391 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_not_test_in_and_test1395 = frozenset([1, 4])
    FOLLOW_NOT_in_not_test1416 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_not_test_in_not_test1420 = frozenset([1])
    FOLLOW_comparison_in_not_test1446 = frozenset([1])
    FOLLOW_expr_in_comparison1460 = frozenset([1, 27, 40, 41, 48, 53, 65, 66, 76, 77])
    FOLLOW_comp_op_in_comparison1463 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_in_comparison1467 = frozenset([1, 27, 40, 41, 48, 53, 65, 66, 76, 77])
    FOLLOW_LT_in_comp_op1494 = frozenset([1])
    FOLLOW_GT_in_comp_op1498 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op1502 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op1506 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op1510 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op1514 = frozenset([1])
    FOLLOW_IN_in_comp_op1518 = frozenset([1])
    FOLLOW_NOT_in_comp_op1522 = frozenset([48])
    FOLLOW_IN_in_comp_op1524 = frozenset([1])
    FOLLOW_IS_in_comp_op1528 = frozenset([1])
    FOLLOW_IS_in_comp_op1532 = frozenset([76])
    FOLLOW_NOT_in_comp_op1534 = frozenset([1])
    FOLLOW_xor_expr_in_expr1551 = frozenset([1, 12])
    FOLLOW_BIT_OR_in_expr1554 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_xor_expr_in_expr1558 = frozenset([1, 12])
    FOLLOW_and_expr_in_xor_expr1581 = frozenset([1, 124])
    FOLLOW_XOR_in_xor_expr1584 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_and_expr_in_xor_expr1588 = frozenset([1, 124])
    FOLLOW_shift_expr_in_and_expr1611 = frozenset([1, 10])
    FOLLOW_BIT_AND_in_and_expr1614 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_shift_expr_in_and_expr1618 = frozenset([1, 10])
    FOLLOW_arith_expr_in_shift_expr1639 = frozenset([1, 64, 94])
    FOLLOW_LSHIFT_in_shift_expr1645 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_RSHIFT_in_shift_expr1649 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_arith_expr_in_shift_expr1654 = frozenset([1, 64, 94])
    FOLLOW_term_in_arith_expr1680 = frozenset([1, 69, 84])
    FOLLOW_PLUS_in_arith_expr1686 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_MINUS_in_arith_expr1690 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_term_in_arith_expr1695 = frozenset([1, 69, 84])
    FOLLOW_factor_in_term1727 = frozenset([1, 22, 44, 70, 71])
    FOLLOW_MUL_in_term1733 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_DIV_in_term1737 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_MOD_in_term1741 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_IDIV_in_term1745 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_factor_in_term1750 = frozenset([1, 22, 44, 70, 71])
    FOLLOW_PLUS_in_factor1781 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_MINUS_in_factor1785 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_BIT_NOT_in_factor1789 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_factor_in_factor1794 = frozenset([1])
    FOLLOW_power_in_factor1824 = frozenset([1])
    FOLLOW_atom_expr_in_power1841 = frozenset([1, 86])
    FOLLOW_POWER_in_power1844 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_factor_in_power1846 = frozenset([1])
    FOLLOW_atom_in_atom_expr1871 = frozenset([1, 23, 55])
    FOLLOW_trailer_in_atom_expr1876 = frozenset([1, 23, 55])
    FOLLOW_LPAREN_in_atom1901 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_atom1905 = frozenset([93])
    FOLLOW_RPAREN_in_atom1907 = frozenset([1])
    FOLLOW_LBRACK_in_atom1922 = frozenset(
        [
            11,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            89,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_testlist_comp_in_atom1924 = frozenset([89])
    FOLLOW_RBRACK_in_atom1927 = frozenset([1])
    FOLLOW_LT_in_atom1942 = frozenset(
        [11, 21, 31, 33, 40, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_vector_comp_in_atom1944 = frozenset([40])
    FOLLOW_GT_in_atom1947 = frozenset([1])
    FOLLOW_LBRACE_in_atom1962 = frozenset(
        [
            11,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            88,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_dict_or_set_maker_in_atom1964 = frozenset([88])
    FOLLOW_RBRACE_in_atom1967 = frozenset([1])
    FOLLOW_LEN_in_atom1982 = frozenset([63])
    FOLLOW_LPAREN_in_atom1984 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_atom1988 = frozenset([93])
    FOLLOW_RPAREN_in_atom1990 = frozenset([1])
    FOLLOW_name_in_atom2005 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom2015 = frozenset([1])
    FOLLOW_DISTRIBUTION_in_atom2031 = frozenset([63])
    FOLLOW_LPAREN_in_atom2033 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_arglist_in_atom2035 = frozenset([93])
    FOLLOW_RPAREN_in_atom2037 = frozenset([1])
    FOLLOW_INTEGER_in_atom2057 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom2067 = frozenset([1])
    FOLLOW_STRING_in_atom2077 = frozenset([1])
    FOLLOW_NONE_in_atom2088 = frozenset([1])
    FOLLOW_TRUE_in_atom2100 = frozenset([1])
    FOLLOW_FALSE_in_atom2112 = frozenset([1])
    FOLLOW_ID_in_name2132 = frozenset([1])
    FOLLOW_UNDERSCORE_in_name2142 = frozenset([1])
    FOLLOW_test_in_testlist_comp2161 = frozenset([1, 16, 34, 87])
    FOLLOW_comp_for_in_testlist_comp2165 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp2205 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_testlist_comp2209 = frozenset([1, 16])
    FOLLOW_RANGE_in_testlist_comp2245 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_testlist_comp2249 = frozenset([1, 110])
    FOLLOW_STEP_in_testlist_comp2252 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_testlist_comp2256 = frozenset([1])
    FOLLOW_expr_in_vector_comp2305 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp2307 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_in_vector_comp2311 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp2313 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_in_vector_comp2317 = frozenset([1])
    FOLLOW_LBRACK_in_trailer2351 = frozenset(
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_subscriptlist_in_trailer2353 = frozenset([89])
    FOLLOW_RBRACK_in_trailer2355 = frozenset([1])
    FOLLOW_DOT_in_trailer2383 = frozenset([43, 119])
    FOLLOW_name_in_trailer2385 = frozenset([1])
    FOLLOW_argument_in_arglist2409 = frozenset([1, 16])
    FOLLOW_COMMA_in_arglist2412 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_argument_in_arglist2416 = frozenset([1, 16])
    FOLLOW_test_in_argument2441 = frozenset([1, 5])
    FOLLOW_ASSIGN_in_argument2444 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_argument2448 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist2473 = frozenset([1, 16])
    FOLLOW_COMMA_in_subscriptlist2476 = frozenset(
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_subscript__in_subscriptlist2480 = frozenset([1, 16])
    FOLLOW_test_in_subscript_2503 = frozenset([1, 15])
    FOLLOW_COLON_in_subscript_2506 = frozenset(
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_test_in_subscript_2511 = frozenset([1, 15])
    FOLLOW_sliceop_in_subscript_2518 = frozenset([1])
    FOLLOW_COLON_in_subscript_2564 = frozenset(
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
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_test_in_subscript_2569 = frozenset([1, 15])
    FOLLOW_sliceop_in_subscript_2576 = frozenset([1])
    FOLLOW_COLON_in_sliceop2611 = frozenset(
        [
            1,
            11,
            21,
            31,
            33,
            43,
            51,
            54,
            55,
            56,
            63,
            65,
            69,
            74,
            76,
            84,
            101,
            112,
            118,
            119,
        ]
    )
    FOLLOW_test_in_sliceop2613 = frozenset([1])
    FOLLOW_expr_in_exprlist2633 = frozenset([1, 16])
    FOLLOW_COMMA_in_exprlist2636 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_in_exprlist2640 = frozenset([1, 16])
    FOLLOW_test_in_testlist2660 = frozenset([1, 16])
    FOLLOW_COMMA_in_testlist2663 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_testlist2667 = frozenset([1, 16])
    FOLLOW_test_in_dict_or_set_maker2688 = frozenset([1, 15, 16, 34])
    FOLLOW_COLON_in_dict_or_set_maker2692 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_dict_or_set_maker2696 = frozenset([1, 16, 34])
    FOLLOW_comp_for_in_dict_or_set_maker2701 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker2760 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_dict_or_set_maker2764 = frozenset([15])
    FOLLOW_COLON_in_dict_or_set_maker2766 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_dict_or_set_maker2770 = frozenset([1, 16])
    FOLLOW_comp_for_in_dict_or_set_maker2808 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker2846 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_dict_or_set_maker2850 = frozenset([1, 16])
    FOLLOW_comp_for_in_comp_iter2891 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter2895 = frozenset([1])
    FOLLOW_FOR_in_comp_for2908 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_exprlist_in_comp_for2910 = frozenset([48])
    FOLLOW_IN_in_comp_for2912 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_or_test_in_comp_for2914 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_for2916 = frozenset([1])
    FOLLOW_IF_in_comp_if2945 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_nocond_in_comp_if2947 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_if2949 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
