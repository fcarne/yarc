# $ANTLR 3.5.1 C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g 2023-05-05 23:27:50

import sys

import stringtemplate3
from antlr3 import (
    BaseRecognizer,
    EarlyExitException,
    MismatchedSetException,
    NoViableAltException,
    Parser,
    ParserRuleReturnScope,
    RecognitionException,
    RecognizerSharedState,
    Token,
)

# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF = -1
ADD_ASSIGN = 4
AND = 5
AND_ASSIGN = 6
ASSIGN = 7
AT = 8
AXIS = 9
BIN_DIGIT = 10
BIT_AND = 11
BIT_NOT = 12
BIT_OR = 13
CAMERA = 14
CAM_TRANSLATE = 15
CHOICE = 16
COLON = 17
COMMA = 18
COMMENT = 19
CREATE = 20
DEDENT = 21
DIGIT = 22
DIV = 23
DIV_ASSIGN = 24
DOT = 25
EDIT = 26
ELLIPSIS = 27
ELSE = 28
EQUALS = 29
EVERY = 30
EXPONENT = 31
EXPONENT_FLOAT = 32
FALSE = 33
FETCH = 34
FLOAT_NUMBER = 35
FOR = 36
FRACTION = 37
FRAMES = 38
FROM = 39
GET = 40
GROUP = 41
GT = 42
GT_EQ = 43
HEX_DIGIT = 44
ID = 45
IDIV = 46
IDIV_ASSIGN = 47
ID_CONTINUE = 48
ID_START = 49
IF = 50
IN = 51
INDENT = 52
INSTANTIATE = 53
INTEGER = 54
INT_PART = 55
IS = 56
LBRACE = 57
LBRACK = 58
LETTER = 59
LIGHT = 60
LIGHT_TYPE = 61
LIMIT = 62
LINE_JOINING = 63
LOG_UNIFORM = 64
LOOK_AT = 65
LPAREN = 66
LSHIFT = 67
LSHIFT_ASSIGN = 68
LT = 69
LT_EQ = 70
MATCH = 71
MATERIAL = 72
MINUS = 73
MOD = 74
MOD_ASSIGN = 75
MUL = 76
MULT_ASSIGN = 77
NESTED_CODE = 78
NEWLINE = 79
NONE = 80
NON_ZERO_DIGIT = 81
NORMAL = 82
NOT = 83
NOT_EQ = 84
OCT_DIGIT = 85
ON = 86
OPEN = 87
OR = 88
ORDER = 89
OR_ASSIGN = 90
PHYSICS = 91
PLUS = 92
POINT_FLOAT = 93
POWER = 94
POWER_ASSIGN = 95
RANGE = 96
RBRACE = 97
RBRACK = 98
RECURSIVE = 99
ROTATE = 100
ROT_AROUND = 101
RPAREN = 102
RSHIFT = 103
RSHIFT_ASSIGN = 104
SCALE = 105
SCATTER = 106
SCENARIO = 107
SEMANTICS = 108
SEMI = 109
SEQUENCE = 110
SETTINGS = 111
SETTING_ID = 112
SHAPES = 113
SHAPES_OR_LIGHTS = 114
SHORT_STRING = 115
SIZE = 116
SKIP_ = 117
SNIPPET = 118
SPACES = 119
STAGE = 120
STEREO = 121
STRING = 122
STRING_ESCAPE_SEQ = 123
SUB_ASSIGN = 124
TIME = 125
TIMELINE = 126
TO = 127
TRANSLATE = 128
TRUE = 129
UNDERSCORE = 130
UNIFORM = 131
UNKNOWN = 132
UP_AXIS = 133
VISIBLE = 134
WRITERS = 135
XOR = 136
XOR_ASSIGN = 137

# token names
tokenNamesMap = {
    0: "<invalid>",
    1: "<EOR>",
    2: "<DOWN>",
    3: "<UP>",
    -1: "EOF",
    4: "ADD_ASSIGN",
    5: "AND",
    6: "AND_ASSIGN",
    7: "ASSIGN",
    8: "AT",
    9: "AXIS",
    10: "BIN_DIGIT",
    11: "BIT_AND",
    12: "BIT_NOT",
    13: "BIT_OR",
    14: "CAMERA",
    15: "CAM_TRANSLATE",
    16: "CHOICE",
    17: "COLON",
    18: "COMMA",
    19: "COMMENT",
    20: "CREATE",
    21: "DEDENT",
    22: "DIGIT",
    23: "DIV",
    24: "DIV_ASSIGN",
    25: "DOT",
    26: "EDIT",
    27: "ELLIPSIS",
    28: "ELSE",
    29: "EQUALS",
    30: "EVERY",
    31: "EXPONENT",
    32: "EXPONENT_FLOAT",
    33: "FALSE",
    34: "FETCH",
    35: "FLOAT_NUMBER",
    36: "FOR",
    37: "FRACTION",
    38: "FRAMES",
    39: "FROM",
    40: "GET",
    41: "GROUP",
    42: "GT",
    43: "GT_EQ",
    44: "HEX_DIGIT",
    45: "ID",
    46: "IDIV",
    47: "IDIV_ASSIGN",
    48: "ID_CONTINUE",
    49: "ID_START",
    50: "IF",
    51: "IN",
    52: "INDENT",
    53: "INSTANTIATE",
    54: "INTEGER",
    55: "INT_PART",
    56: "IS",
    57: "LBRACE",
    58: "LBRACK",
    59: "LETTER",
    60: "LIGHT",
    61: "LIGHT_TYPE",
    62: "LIMIT",
    63: "LINE_JOINING",
    64: "LOG_UNIFORM",
    65: "LOOK_AT",
    66: "LPAREN",
    67: "LSHIFT",
    68: "LSHIFT_ASSIGN",
    69: "LT",
    70: "LT_EQ",
    71: "MATCH",
    72: "MATERIAL",
    73: "MINUS",
    74: "MOD",
    75: "MOD_ASSIGN",
    76: "MUL",
    77: "MULT_ASSIGN",
    78: "NESTED_CODE",
    79: "NEWLINE",
    80: "NONE",
    81: "NON_ZERO_DIGIT",
    82: "NORMAL",
    83: "NOT",
    84: "NOT_EQ",
    85: "OCT_DIGIT",
    86: "ON",
    87: "OPEN",
    88: "OR",
    89: "ORDER",
    90: "OR_ASSIGN",
    91: "PHYSICS",
    92: "PLUS",
    93: "POINT_FLOAT",
    94: "POWER",
    95: "POWER_ASSIGN",
    96: "RANGE",
    97: "RBRACE",
    98: "RBRACK",
    99: "RECURSIVE",
    100: "ROTATE",
    101: "ROT_AROUND",
    102: "RPAREN",
    103: "RSHIFT",
    104: "RSHIFT_ASSIGN",
    105: "SCALE",
    106: "SCATTER",
    107: "SCENARIO",
    108: "SEMANTICS",
    109: "SEMI",
    110: "SEQUENCE",
    111: "SETTINGS",
    112: "SETTING_ID",
    113: "SHAPES",
    114: "SHAPES_OR_LIGHTS",
    115: "SHORT_STRING",
    116: "SIZE",
    117: "SKIP_",
    118: "SNIPPET",
    119: "SPACES",
    120: "STAGE",
    121: "STEREO",
    122: "STRING",
    123: "STRING_ESCAPE_SEQ",
    124: "SUB_ASSIGN",
    125: "TIME",
    126: "TIMELINE",
    127: "TO",
    128: "TRANSLATE",
    129: "TRUE",
    130: "UNDERSCORE",
    131: "UNIFORM",
    132: "UNKNOWN",
    133: "UP_AXIS",
    134: "VISIBLE",
    135: "WRITERS",
    136: "XOR",
    137: "XOR_ASSIGN",
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>",
    "<EOR>",
    "<DOWN>",
    "<UP>",
    "ADD_ASSIGN",
    "AND",
    "AND_ASSIGN",
    "ASSIGN",
    "AT",
    "AXIS",
    "BIN_DIGIT",
    "BIT_AND",
    "BIT_NOT",
    "BIT_OR",
    "CAMERA",
    "CAM_TRANSLATE",
    "CHOICE",
    "COLON",
    "COMMA",
    "COMMENT",
    "CREATE",
    "DEDENT",
    "DIGIT",
    "DIV",
    "DIV_ASSIGN",
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
    "IDIV_ASSIGN",
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
    "LETTER",
    "LIGHT",
    "LIGHT_TYPE",
    "LIMIT",
    "LINE_JOINING",
    "LOG_UNIFORM",
    "LOOK_AT",
    "LPAREN",
    "LSHIFT",
    "LSHIFT_ASSIGN",
    "LT",
    "LT_EQ",
    "MATCH",
    "MATERIAL",
    "MINUS",
    "MOD",
    "MOD_ASSIGN",
    "MUL",
    "MULT_ASSIGN",
    "NESTED_CODE",
    "NEWLINE",
    "NONE",
    "NON_ZERO_DIGIT",
    "NORMAL",
    "NOT",
    "NOT_EQ",
    "OCT_DIGIT",
    "ON",
    "OPEN",
    "OR",
    "ORDER",
    "OR_ASSIGN",
    "PHYSICS",
    "PLUS",
    "POINT_FLOAT",
    "POWER",
    "POWER_ASSIGN",
    "RANGE",
    "RBRACE",
    "RBRACK",
    "RECURSIVE",
    "ROTATE",
    "ROT_AROUND",
    "RPAREN",
    "RSHIFT",
    "RSHIFT_ASSIGN",
    "SCALE",
    "SCATTER",
    "SCENARIO",
    "SEMANTICS",
    "SEMI",
    "SEQUENCE",
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
    "STEREO",
    "STRING",
    "STRING_ESCAPE_SEQ",
    "SUB_ASSIGN",
    "TIME",
    "TIMELINE",
    "TO",
    "TRANSLATE",
    "TRUE",
    "UNDERSCORE",
    "UNIFORM",
    "UNKNOWN",
    "UP_AXIS",
    "VISIBLE",
    "WRITERS",
    "XOR",
    "XOR_ASSIGN",
]


class YarcParser(Parser):
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:1: scenario : declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? ;
    def scenario(
        self,
    ):
        retval = self.scenario_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:10: ( declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:12: declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )?
                self._state.following.append(self.FOLLOW_declaration_in_scenario44)
                self.declaration()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:24: ( NEWLINE )*
                while True:  # loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if LA1_0 == NEWLINE:
                        alt1 = 1

                    if alt1 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:24: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario46
                        )

                    else:
                        break  # loop1

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:33: ( settings )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if LA2_0 == SETTINGS:
                    alt2 = 1
                if alt2 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:33: settings
                    self._state.following.append(self.FOLLOW_settings_in_scenario49)
                    self.settings()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:43: ( stage )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if LA3_0 == STAGE:
                    alt3 = 1
                if alt3 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:43: stage
                    self._state.following.append(self.FOLLOW_stage_in_scenario52)
                    self.stage()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:50: ( writers )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == WRITERS:
                    alt4 = 1
                if alt4 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:9:50: writers
                    self._state.following.append(self.FOLLOW_writers_in_scenario55)
                    self.writers()

                    self._state.following.pop()

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

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "declaration"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:1: declaration : SCENARIO name ( COLON name )? NEWLINE ;
    def declaration(
        self,
    ):
        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:13: ( SCENARIO name ( COLON name )? NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:15: SCENARIO name ( COLON name )? NEWLINE
                self.match(self.input, SCENARIO, self.FOLLOW_SCENARIO_in_declaration65)

                self._state.following.append(self.FOLLOW_name_in_declaration67)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:29: ( COLON name )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if LA5_0 == COLON:
                    alt5 = 1
                if alt5 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:30: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration70)

                    self._state.following.append(self.FOLLOW_name_in_declaration72)
                    self.name()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_declaration76)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:12:1: settings : SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT ;
    def settings(
        self,
    ):
        retval = self.settings_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:12:13: ( SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:12:15: SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT
                self.match(self.input, SETTINGS, self.FOLLOW_SETTINGS_in_settings86)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_settings88)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_settings90)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_settings92)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:12:45: ( option )+
                cnt6 = 0
                while True:  # loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if LA6_0 == ID:
                        alt6 = 1

                    if alt6 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:12:45: option
                        self._state.following.append(self.FOLLOW_option_in_settings94)
                        self.option()

                        self._state.following.pop()

                    else:
                        if cnt6 >= 1:
                            break  # loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_settings97)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:1: stage : STAGE COLON NEWLINE INDENT stmts DEDENT ;
    def stage(
        self,
    ):
        retval = self.stage_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:13: ( STAGE COLON NEWLINE INDENT stmts DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:15: STAGE COLON NEWLINE INDENT stmts DEDENT
                self.match(self.input, STAGE, self.FOLLOW_STAGE_in_stage110)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_stage112)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stage114)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stage116)

                self._state.following.append(self.FOLLOW_stmts_in_stage118)
                self.stmts()

                self._state.following.pop()

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stage120)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:14:1: writers : WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT ;
    def writers(
        self,
    ):
        retval = self.writers_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:14:13: ( WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:14:15: WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT
                self.match(self.input, WRITERS, self.FOLLOW_WRITERS_in_writers131)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writers133)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writers135)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writers137)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:14:44: ( expr_stmt | writer )+
                cnt7 = 0
                while True:  # loop7
                    alt7 = 3
                    LA7_0 = self.input.LA(1)

                    if LA7_0 in {
                        BIT_NOT,
                        CHOICE,
                        FALSE,
                        FLOAT_NUMBER,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LOG_UNIFORM,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NORMAL,
                        NOT,
                        PLUS,
                        SEQUENCE,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                        UNIFORM,
                    }:
                        alt7 = 1
                    elif LA7_0 == ID:
                        LA7_3 = self.input.LA(2)

                        if LA7_3 == COLON:
                            alt7 = 2
                        elif (MINUS <= LA7_3 <= MULT_ASSIGN) or LA7_3 in {
                            ADD_ASSIGN,
                            AND,
                            AND_ASSIGN,
                            ASSIGN,
                            BIT_AND,
                            BIT_OR,
                            COMMA,
                            DIV,
                            DIV_ASSIGN,
                            DOT,
                            EQUALS,
                            GT,
                            GT_EQ,
                            IDIV,
                            IDIV_ASSIGN,
                            IF,
                            IN,
                            IS,
                            LBRACK,
                            LSHIFT,
                            LSHIFT_ASSIGN,
                            LT,
                            LT_EQ,
                            NOT,
                            NOT_EQ,
                            OR,
                            OR_ASSIGN,
                            PLUS,
                            POWER,
                            POWER_ASSIGN,
                            RSHIFT,
                            RSHIFT_ASSIGN,
                            SUB_ASSIGN,
                            XOR,
                            XOR_ASSIGN,
                        }:
                            alt7 = 1

                    if alt7 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:14:45: expr_stmt
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers140
                        )
                        self.expr_stmt()

                        self._state.following.pop()

                    elif alt7 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:14:57: writer
                        self._state.following.append(self.FOLLOW_writer_in_writers144)
                        self.writer()

                        self._state.following.pop()

                    else:
                        if cnt7 >= 1:
                            break  # loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writers148)

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "writers"

    class option_return(ParserRuleReturnScope):
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

    # $ANTLR start "option"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:1: option : ID ASSIGN test NEWLINE ;
    def option(
        self,
    ):
        retval = self.option_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:8: ( ID ASSIGN test NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:10: ID ASSIGN test NEWLINE
                self.match(self.input, ID, self.FOLLOW_ID_in_option156)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_option158)

                self._state.following.append(self.FOLLOW_test_in_option160)
                self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_option162)

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "option"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:1: stmts : ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+ ;
    def stmts(
        self,
    ):
        retval = self.stmts_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:8: ( ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+ )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:10: ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:10: ( open_stmt )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if LA8_0 == OPEN:
                    alt8 = 1
                if alt8 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:10: open_stmt
                    self._state.following.append(self.FOLLOW_open_stmt_in_stmts170)
                    self.open_stmt()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:21: ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                cnt9 = 0
                while True:  # loop9
                    alt9 = 4
                    LA9 = self.input.LA(1)
                    if LA9 in {
                        BIT_NOT,
                        CHOICE,
                        CREATE,
                        FALSE,
                        FLOAT_NUMBER,
                        GET,
                        GROUP,
                        ID,
                        INSTANTIATE,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LOG_UNIFORM,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NORMAL,
                        NOT,
                        PLUS,
                        SEQUENCE,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                        UNIFORM,
                    }:
                        alt9 = 1
                    elif LA9 in {EDIT}:
                        alt9 = 2
                    elif LA9 in {EVERY}:
                        alt9 = 3

                    if alt9 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:22: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts174
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt9 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:38: edit_stmt
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts178)
                        self.edit_stmt()

                        self._state.following.pop()

                    elif alt9 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:50: behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_behavior_stmt_in_stmts182
                        )
                        self.behavior_stmt()

                        self._state.following.pop()

                    else:
                        if cnt9 >= 1:
                            break  # loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:18:1: writer : ID COLON NEWLINE INDENT ( option )+ DEDENT ;
    def writer(
        self,
    ):
        retval = self.writer_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:18:8: ( ID COLON NEWLINE INDENT ( option )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:18:10: ID COLON NEWLINE INDENT ( option )+ DEDENT
                self.match(self.input, ID, self.FOLLOW_ID_in_writer191)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writer193)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer195)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writer197)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:18:34: ( option )+
                cnt10 = 0
                while True:  # loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if LA10_0 == ID:
                        alt10 = 1

                    if alt10 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:18:34: option
                        self._state.following.append(self.FOLLOW_option_in_writer199)
                        self.option()

                        self._state.following.pop()

                    else:
                        if cnt10 >= 1:
                            break  # loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writer202)

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "writer"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:1: open_stmt : OPEN test NEWLINE ;
    def open_stmt(
        self,
    ):
        retval = self.open_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:11: ( OPEN test NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:13: OPEN test NEWLINE
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_open_stmt214)

                self._state.following.append(self.FOLLOW_test_in_open_stmt216)
                self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_open_stmt218)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:1: edit_stmt : EDIT ( TIMELINE | name ) edit_block ;
    def edit_stmt(
        self,
    ):
        retval = self.edit_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:11: ( EDIT ( TIMELINE | name ) edit_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:13: EDIT ( TIMELINE | name ) edit_block
                self.match(self.input, EDIT, self.FOLLOW_EDIT_in_edit_stmt225)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:18: ( TIMELINE | name )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if LA11_0 == TIMELINE:
                    alt11 = 1
                elif LA11_0 in {ID, UNDERSCORE}:
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:19: TIMELINE
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt228
                    )

                elif alt11 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:23:30: name
                    self._state.following.append(self.FOLLOW_name_in_edit_stmt232)
                    self.name()

                    self._state.following.pop()

                self._state.following.append(self.FOLLOW_edit_block_in_edit_stmt235)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:1: create_expr : CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) ;
    def create_expr(
        self,
    ):
        retval = self.create_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:12: ( CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:3: CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr244)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:10: ( test )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if LA12_0 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    NOT,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt12 = 1
                if alt12 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:10: test
                    self._state.following.append(self.FOLLOW_test_in_create_expr246)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:16: ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if LA16_0 in {
                    CAMERA,
                    FROM,
                    LIGHT_TYPE,
                    SHAPES,
                    SHAPES_OR_LIGHTS,
                    STEREO,
                }:
                    alt16 = 1
                elif LA16_0 == MATERIAL:
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test )
                    alt14 = 4
                    LA14 = self.input.LA(1)
                    if LA14 in {CAMERA, STEREO}:
                        alt14 = 1
                    elif LA14 in {SHAPES_OR_LIGHTS}:
                        LA14_2 = self.input.LA(2)

                        if LA14_2 in {COLON, NEWLINE}:
                            alt14 = 2
                        elif LA14_2 == LIGHT:
                            alt14 = 3
                        else:
                            nvae = NoViableAltException("", 14, 2, self.input)

                            raise nvae

                    elif LA14 in {SHAPES}:
                        alt14 = 2
                    elif LA14 in {LIGHT_TYPE}:
                        alt14 = 3
                    elif LA14 in {FROM}:
                        alt14 = 4
                    else:
                        nvae = NoViableAltException("", 14, 0, self.input)

                        raise nvae

                    if alt14 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:6: ( STEREO )? CAMERA
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:6: ( STEREO )?
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if LA13_0 == STEREO:
                            alt13 = 1
                        if alt13 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:6: STEREO
                            self.match(
                                self.input, STEREO, self.FOLLOW_STEREO_in_create_expr256
                            )

                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr259
                        )

                    elif alt14 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:23: shapes
                        self._state.following.append(
                            self.FOLLOW_shapes_in_create_expr263
                        )
                        self.shapes()

                        self._state.following.pop()

                    elif alt14 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:32: light_type LIGHT
                        self._state.following.append(
                            self.FOLLOW_light_type_in_create_expr267
                        )
                        self.light_type()

                        self._state.following.pop()

                        self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr269
                        )

                    elif alt14 == 4:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:51: FROM test
                        self.match(self.input, FROM, self.FOLLOW_FROM_in_create_expr273)

                        self._state.following.append(self.FOLLOW_test_in_create_expr275)
                        self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:62: ( edit_block | NEWLINE )
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if LA15_0 == COLON:
                        alt15 = 1
                    elif LA15_0 == NEWLINE:
                        alt15 = 2
                    else:
                        nvae = NoViableAltException("", 15, 0, self.input)

                        raise nvae

                    if alt15 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:63: edit_block
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr279
                        )
                        self.edit_block()

                        self._state.following.pop()

                    elif alt15 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:76: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr283
                        )

                elif alt16 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:28:7: MATERIAL ( simple_block )
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr292
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:28:16: ( simple_block )
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:28:17: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_create_expr295
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:1: shapes : ( SHAPES | SHAPES_OR_LIGHTS );
    def shapes(
        self,
    ):
        retval = self.shapes_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:12: ( SHAPES | SHAPES_OR_LIGHTS )
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:1: light_type : ( LIGHT_TYPE | SHAPES_OR_LIGHTS );
    def light_type(
        self,
    ):
        retval = self.light_type_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:12: ( LIGHT_TYPE | SHAPES_OR_LIGHTS )
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:1: instantiate_expr : INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) ;
    def instantiate_expr(
        self,
    ):
        retval = self.instantiate_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:18: ( INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:20: INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE )
                self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr336,
                )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:32: ( test )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if LA17_0 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    NOT,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt17 = 1
                if alt17 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:33: test
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr339
                    )
                    self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr343)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr345)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:50: ( edit_block | NEWLINE )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if LA18_0 == COLON:
                    alt18 = 1
                elif LA18_0 == NEWLINE:
                    alt18 = 2
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:51: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr348
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt18 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:64: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instantiate_expr352
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:1: group_expr : GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) ;
    def group_expr(
        self,
    ):
        retval = self.group_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:18: ( GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:20: GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE )
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_expr366)

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr368)

                self._state.following.append(self.FOLLOW_name_in_group_expr370)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:38: ( COMMA name )*
                while True:  # loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if LA19_0 == COMMA:
                        alt19 = 1

                    if alt19 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:39: COMMA name
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_group_expr373
                        )

                        self._state.following.append(self.FOLLOW_name_in_group_expr375)
                        self.name()

                        self._state.following.pop()

                    else:
                        break  # loop19

                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_group_expr379)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:59: ( edit_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:60: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr382
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt20 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:73: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_group_expr386
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:1: get_expr : GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) ;
    def get_expr(
        self,
    ):
        retval = self.get_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:18: ( GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:20: GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE )
                self.match(self.input, GET, self.FOLLOW_GET_in_get_expr402)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:24: ( ( CAMERA | LIGHT | MATERIAL | name ) AT )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if LA22_0 in {CAMERA, LIGHT, MATERIAL}:
                    alt22 = 1
                elif LA22_0 in {ID, UNDERSCORE}:
                    LA22_2 = self.input.LA(2)

                    if LA22_2 == AT:
                        alt22 = 1
                if alt22 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:25: ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:25: ( CAMERA | LIGHT | MATERIAL | name )
                    alt21 = 4
                    LA21 = self.input.LA(1)
                    if LA21 in {CAMERA}:
                        alt21 = 1
                    elif LA21 in {LIGHT}:
                        alt21 = 2
                    elif LA21 in {MATERIAL}:
                        alt21 = 3
                    elif LA21 in {ID, UNDERSCORE}:
                        alt21 = 4
                    else:
                        nvae = NoViableAltException("", 21, 0, self.input)

                        raise nvae

                    if alt21 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:26: CAMERA
                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr406
                        )

                    elif alt21 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:35: LIGHT
                        self.match(self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr410)

                    elif alt21 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:43: MATERIAL
                        self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr414
                        )

                    elif alt21 == 4:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:54: name
                        self._state.following.append(self.FOLLOW_name_in_get_expr418)
                        self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr421)

                self._state.following.append(self.FOLLOW_test_in_get_expr425)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:70: ( simple_block | NEWLINE )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if LA23_0 == COLON:
                    alt23 = 1
                elif LA23_0 == NEWLINE:
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:71: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr428
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt23 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:37:86: NEWLINE
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr432)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:1: edit_block : COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT ;
    def edit_block(
        self,
    ):
        retval = self.edit_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:14: ( COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:16: COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block443)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block445)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block447)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:37: ( attr | inner_behavior_stmt )+
                cnt24 = 0
                while True:  # loop24
                    alt24 = 3
                    LA24_0 = self.input.LA(1)

                    if LA24_0 in {
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
                        alt24 = 1
                    elif LA24_0 == EVERY:
                        alt24 = 2

                    if alt24 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:38: attr
                        self._state.following.append(self.FOLLOW_attr_in_edit_block450)
                        self.attr()

                        self._state.following.pop()

                    elif alt24 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:45: inner_behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_inner_behavior_stmt_in_edit_block454
                        )
                        self.inner_behavior_stmt()

                        self._state.following.pop()

                    else:
                        if cnt24 >= 1:
                            break  # loop24

                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_block458)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:40:1: simple_block : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        retval = self.simple_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:40:14: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:40:16: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block465)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block467)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block469)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:40:37: ( simple_attr )+
                cnt25 = 0
                while True:  # loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if LA25_0 in {ID, UNDERSCORE}:
                        alt25 = 1

                    if alt25 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:40:37: simple_attr
                        self._state.following.append(
                            self.FOLLOW_simple_attr_in_simple_block471
                        )
                        self.simple_attr()

                        self._state.following.pop()

                    else:
                        if cnt25 >= 1:
                            break  # loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_simple_block474)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:1: attr : ( core_attr | simple_attr | compound_attr );
    def attr(
        self,
    ):
        retval = self.attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:15: ( core_attr | simple_attr | compound_attr )
                alt26 = 3
                LA26 = self.input.LA(1)
                if LA26 in {
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
                    alt26 = 1
                elif LA26 in {ID, UNDERSCORE}:
                    alt26 = 2
                elif LA26 in {PHYSICS, ROT_AROUND, SCATTER}:
                    alt26 = 3
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:17: core_attr
                    self._state.following.append(self.FOLLOW_core_attr_in_attr491)
                    self.core_attr()

                    self._state.following.pop()

                elif alt26 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:29: simple_attr
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr495)
                    self.simple_attr()

                    self._state.following.pop()

                elif alt26 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:43: compound_attr
                    self._state.following.append(self.FOLLOW_compound_attr_in_attr499)
                    self.compound_attr()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:1: simple_attr : name ( COLON name )? ( test )? NEWLINE ;
    def simple_attr(
        self,
    ):
        retval = self.simple_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:15: ( name ( COLON name )? ( test )? NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:17: name ( COLON name )? ( test )? NEWLINE
                self._state.following.append(self.FOLLOW_name_in_simple_attr508)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:22: ( COLON name )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if LA27_0 == COLON:
                    alt27 = 1
                if alt27 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:23: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr511)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr513)
                    self.name()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:36: ( test )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if LA28_0 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    NOT,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt28 = 1
                if alt28 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:36: test
                    self._state.following.append(self.FOLLOW_test_in_simple_attr517)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_attr520)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:1: compound_attr : ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) ;
    def compound_attr(
        self,
    ):
        retval = self.compound_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:15: ( ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS )
                alt29 = 3
                LA29 = self.input.LA(1)
                if LA29 in {SCATTER}:
                    alt29 = 1
                elif LA29 in {ROT_AROUND}:
                    alt29 = 2
                elif LA29 in {PHYSICS}:
                    alt29 = 3
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:18: SCATTER ON name
                    self.match(
                        self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr529
                    )

                    self.match(self.input, ON, self.FOLLOW_ON_in_compound_attr531)

                    self._state.following.append(self.FOLLOW_name_in_compound_attr533)
                    self.name()

                    self._state.following.pop()

                elif alt29 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:36: ROT_AROUND name
                    self.match(
                        self.input,
                        ROT_AROUND,
                        self.FOLLOW_ROT_AROUND_in_compound_attr537,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr539)
                    self.name()

                    self._state.following.pop()

                elif alt29 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:54: PHYSICS
                    self.match(
                        self.input, PHYSICS, self.FOLLOW_PHYSICS_in_compound_attr543
                    )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:63: ( simple_block | NEWLINE )
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if LA30_0 == COLON:
                    alt30 = 1
                elif LA30_0 == NEWLINE:
                    alt30 = 2
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:64: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_compound_attr547
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt30 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:79: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_compound_attr551
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:1: core_attr : ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE ;
    def core_attr(
        self,
    ):
        retval = self.core_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:10: ( ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:48:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:48:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test )
                alt34 = 9
                LA34 = self.input.LA(1)
                if LA34 in {TRANSLATE}:
                    alt34 = 1
                elif LA34 in {CAM_TRANSLATE}:
                    alt34 = 2
                elif LA34 in {ROTATE}:
                    alt34 = 3
                elif LA34 in {SCALE}:
                    alt34 = 4
                elif LA34 in {LOOK_AT}:
                    alt34 = 5
                elif LA34 in {UP_AXIS}:
                    alt34 = 6
                elif LA34 in {SIZE}:
                    alt34 = 7
                elif LA34 in {SEMANTICS}:
                    alt34 = 8
                elif LA34 in {VISIBLE}:
                    alt34 = 9
                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:49:5: TRANSLATE ( AXIS )? TO test
                    self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr568
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:49:15: ( AXIS )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if LA31_0 == AXIS:
                        alt31 = 1
                    if alt31 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:49:15: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr570)

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr573)

                    self._state.following.append(self.FOLLOW_test_in_core_attr575)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:7: CAM_TRANSLATE TO test
                    self.match(
                        self.input,
                        CAM_TRANSLATE,
                        self.FOLLOW_CAM_TRANSLATE_in_core_attr583,
                    )

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr585)

                    self._state.following.append(self.FOLLOW_test_in_core_attr587)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:51:7: ROTATE ( AXIS )? test ( ORDER )?
                    self.match(self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr595)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:51:14: ( AXIS )?
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if LA32_0 == AXIS:
                        alt32 = 1
                    if alt32 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:51:14: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr597)

                    self._state.following.append(self.FOLLOW_test_in_core_attr600)
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:51:25: ( ORDER )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if LA33_0 == ORDER:
                        alt33 = 1
                    if alt33 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:51:25: ORDER
                        self.match(self.input, ORDER, self.FOLLOW_ORDER_in_core_attr602)

                elif alt34 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:7: SCALE test
                    self.match(self.input, SCALE, self.FOLLOW_SCALE_in_core_attr611)

                    self._state.following.append(self.FOLLOW_test_in_core_attr613)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:7: LOOK_AT test
                    self.match(self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr621)

                    self._state.following.append(self.FOLLOW_test_in_core_attr623)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:7: UP_AXIS test
                    self.match(self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr631)

                    self._state.following.append(self.FOLLOW_test_in_core_attr633)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:55:7: SIZE test
                    self.match(self.input, SIZE, self.FOLLOW_SIZE_in_core_attr641)

                    self._state.following.append(self.FOLLOW_test_in_core_attr643)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:56:7: SEMANTICS test
                    self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr651
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr653)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:7: VISIBLE test
                    self.match(self.input, VISIBLE, self.FOLLOW_VISIBLE_in_core_attr661)

                    self._state.following.append(self.FOLLOW_test_in_core_attr663)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_core_attr669)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:1: inner_behavior_stmt : behavior_expr inner_behavior_block ;
    def inner_behavior_stmt(
        self,
    ):
        retval = self.inner_behavior_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:22: ( behavior_expr inner_behavior_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:24: behavior_expr inner_behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_inner_behavior_stmt679
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_inner_behavior_block_in_inner_behavior_stmt681
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:1: inner_behavior_block : COLON NEWLINE INDENT ( attr )+ DEDENT ;
    def inner_behavior_block(
        self,
    ):
        retval = self.inner_behavior_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:22: ( COLON NEWLINE INDENT ( attr )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:24: COLON NEWLINE INDENT ( attr )+ DEDENT
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block688
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block690
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block692
                )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:45: ( attr )+
                cnt35 = 0
                while True:  # loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if LA35_0 in {
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
                        alt35 = 1

                    if alt35 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:45: attr
                        self._state.following.append(
                            self.FOLLOW_attr_in_inner_behavior_block694
                        )
                        self.attr()

                        self._state.following.pop()

                    else:
                        if cnt35 >= 1:
                            break  # loop35

                        eee = EarlyExitException(35, self.input)
                        raise eee

                    cnt35 += 1

                self.match(
                    self.input, DEDENT, self.FOLLOW_DEDENT_in_inner_behavior_block697
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:1: behavior_stmt : behavior_expr behavior_block ;
    def behavior_stmt(
        self,
    ):
        retval = self.behavior_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:16: ( behavior_expr behavior_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:18: behavior_expr behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_behavior_stmt708
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_behavior_block_in_behavior_stmt710
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:1: behavior_expr : EVERY ( test )? ( FRAMES | TIME ) ;
    def behavior_expr(
        self,
    ):
        retval = self.behavior_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:16: ( EVERY ( test )? ( FRAMES | TIME ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:18: EVERY ( test )? ( FRAMES | TIME )
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr718)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:24: ( test )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if LA36_0 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    NOT,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt36 = 1
                if alt36 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:24: test
                    self._state.following.append(self.FOLLOW_test_in_behavior_expr720)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:1: behavior_block : COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT ;
    def behavior_block(
        self,
    ):
        retval = self.behavior_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:16: ( COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:18: COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block736)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block738
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block740)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:39: ( aug_expr_stmt | edit_stmt )+
                cnt37 = 0
                while True:  # loop37
                    alt37 = 3
                    LA37_0 = self.input.LA(1)

                    if LA37_0 in {
                        BIT_NOT,
                        CHOICE,
                        CREATE,
                        FALSE,
                        FLOAT_NUMBER,
                        GET,
                        GROUP,
                        ID,
                        INSTANTIATE,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LOG_UNIFORM,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NORMAL,
                        NOT,
                        PLUS,
                        SEQUENCE,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                        UNIFORM,
                    }:
                        alt37 = 1
                    elif LA37_0 == EDIT:
                        alt37 = 2

                    if alt37 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:40: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block743
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt37 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:56: edit_stmt
                        self._state.following.append(
                            self.FOLLOW_edit_stmt_in_behavior_block747
                        )
                        self.edit_stmt()

                        self._state.following.pop()

                    else:
                        if cnt37 >= 1:
                            break  # loop37

                        eee = EarlyExitException(37, self.input)
                        raise eee

                    cnt37 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_behavior_block751)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:1: expr_stmt : testlist ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) NEWLINE ;
    def expr_stmt(
        self,
    ):
        retval = self.expr_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:11: ( testlist ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:13: testlist ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt761)
                self.testlist()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:22: ( aug_assign | ASSIGN )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if LA38_0 in {
                    ADD_ASSIGN,
                    AND_ASSIGN,
                    DIV_ASSIGN,
                    IDIV_ASSIGN,
                    LSHIFT_ASSIGN,
                    MOD_ASSIGN,
                    MULT_ASSIGN,
                    OR_ASSIGN,
                    POWER_ASSIGN,
                    RSHIFT_ASSIGN,
                    SUB_ASSIGN,
                    XOR_ASSIGN,
                }:
                    alt38 = 1
                elif LA38_0 == ASSIGN:
                    alt38 = 2
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae

                if alt38 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:23: aug_assign
                    self._state.following.append(self.FOLLOW_aug_assign_in_expr_stmt764)
                    self.aug_assign()

                    self._state.following.pop()

                elif alt38 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:36: ASSIGN
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr_stmt768)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:44: ( testlist | fetch_expr )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if LA39_0 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    NOT,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt39 = 1
                elif LA39_0 == FETCH:
                    alt39 = 2
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:45: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt772)
                    self.testlist()

                    self._state.following.pop()

                elif alt39 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:56: fetch_expr
                    self._state.following.append(self.FOLLOW_fetch_expr_in_expr_stmt776)
                    self.fetch_expr()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expr_stmt779)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:1: aug_expr_stmt : ( ( testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr );
    def aug_expr_stmt(
        self,
    ):
        retval = self.aug_expr_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:14: ( ( testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr )
                alt44 = 5
                LA44 = self.input.LA(1)
                if LA44 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    NOT,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt44 = 1
                elif LA44 in {CREATE}:
                    alt44 = 2
                elif LA44 in {INSTANTIATE}:
                    alt44 = 3
                elif LA44 in {GET}:
                    alt44 = 4
                elif LA44 in {GROUP}:
                    alt44 = 5
                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae

                if alt44 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:16: ( testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:16: ( testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:5: testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt792
                    )
                    self.testlist()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:14: ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if LA43_0 in {
                        ADD_ASSIGN,
                        AND_ASSIGN,
                        DIV_ASSIGN,
                        IDIV_ASSIGN,
                        LSHIFT_ASSIGN,
                        MOD_ASSIGN,
                        MULT_ASSIGN,
                        OR_ASSIGN,
                        POWER_ASSIGN,
                        RSHIFT_ASSIGN,
                        SUB_ASSIGN,
                        XOR_ASSIGN,
                    }:
                        alt43 = 1
                    elif LA43_0 == ASSIGN:
                        alt43 = 2
                    else:
                        nvae = NoViableAltException("", 43, 0, self.input)

                        raise nvae

                    if alt43 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:7: aug_assign ( testlist | fetch_expr )? NEWLINE
                        self._state.following.append(
                            self.FOLLOW_aug_assign_in_aug_expr_stmt802
                        )
                        self.aug_assign()

                        self._state.following.pop()

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:18: ( testlist | fetch_expr )?
                        alt40 = 3
                        LA40_0 = self.input.LA(1)

                        if LA40_0 in {
                            BIT_NOT,
                            CHOICE,
                            FALSE,
                            FLOAT_NUMBER,
                            ID,
                            INTEGER,
                            LBRACE,
                            LBRACK,
                            LOG_UNIFORM,
                            LPAREN,
                            LT,
                            MINUS,
                            NONE,
                            NORMAL,
                            NOT,
                            PLUS,
                            SEQUENCE,
                            SETTING_ID,
                            STRING,
                            TRUE,
                            UNDERSCORE,
                            UNIFORM,
                        }:
                            alt40 = 1
                        elif LA40_0 == FETCH:
                            alt40 = 2
                        if alt40 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:19: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt805
                            )
                            self.testlist()

                            self._state.following.pop()

                        elif alt40 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:30: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt809
                            )
                            self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_aug_expr_stmt813
                        )

                    elif alt43 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:9: ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt823
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:16: ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        alt42 = 5
                        LA42 = self.input.LA(1)
                        if LA42 in {
                            BIT_NOT,
                            CHOICE,
                            FALSE,
                            FETCH,
                            FLOAT_NUMBER,
                            ID,
                            INTEGER,
                            LBRACE,
                            LBRACK,
                            LOG_UNIFORM,
                            LPAREN,
                            LT,
                            MINUS,
                            NONE,
                            NORMAL,
                            NOT,
                            PLUS,
                            SEQUENCE,
                            SETTING_ID,
                            STRING,
                            TRUE,
                            UNDERSCORE,
                            UNIFORM,
                        }:
                            alt42 = 1
                        elif LA42 in {CREATE}:
                            alt42 = 2
                        elif LA42 in {INSTANTIATE}:
                            alt42 = 3
                        elif LA42 in {GET}:
                            alt42 = 4
                        elif LA42 in {GROUP}:
                            alt42 = 5
                        else:
                            nvae = NoViableAltException("", 42, 0, self.input)

                            raise nvae

                        if alt42 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:9: ( testlist | fetch_expr ) NEWLINE
                            pass
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:9: ( testlist | fetch_expr )
                            alt41 = 2
                            LA41_0 = self.input.LA(1)

                            if LA41_0 in {
                                BIT_NOT,
                                CHOICE,
                                FALSE,
                                FLOAT_NUMBER,
                                ID,
                                INTEGER,
                                LBRACE,
                                LBRACK,
                                LOG_UNIFORM,
                                LPAREN,
                                LT,
                                MINUS,
                                NONE,
                                NORMAL,
                                NOT,
                                PLUS,
                                SEQUENCE,
                                SETTING_ID,
                                STRING,
                                TRUE,
                                UNDERSCORE,
                                UNIFORM,
                            }:
                                alt41 = 1
                            elif LA41_0 == FETCH:
                                alt41 = 2
                            else:
                                nvae = NoViableAltException("", 41, 0, self.input)

                                raise nvae

                            if alt41 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:10: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt836
                                )
                                self.testlist()

                                self._state.following.pop()

                            elif alt41 == 2:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:21: fetch_expr
                                self._state.following.append(
                                    self.FOLLOW_fetch_expr_in_aug_expr_stmt840
                                )
                                self.fetch_expr()

                                self._state.following.pop()

                            self.match(
                                self.input,
                                NEWLINE,
                                self.FOLLOW_NEWLINE_in_aug_expr_stmt843,
                            )

                        elif alt42 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:11: create_expr
                            self._state.following.append(
                                self.FOLLOW_create_expr_in_aug_expr_stmt855
                            )
                            self.create_expr()

                            self._state.following.pop()

                        elif alt42 == 3:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:25: instantiate_expr
                            self._state.following.append(
                                self.FOLLOW_instantiate_expr_in_aug_expr_stmt859
                            )
                            self.instantiate_expr()

                            self._state.following.pop()

                        elif alt42 == 4:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:44: get_expr
                            self._state.following.append(
                                self.FOLLOW_get_expr_in_aug_expr_stmt863
                            )
                            self.get_expr()

                            self._state.following.pop()

                        elif alt42 == 5:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:55: group_expr
                            self._state.following.append(
                                self.FOLLOW_group_expr_in_aug_expr_stmt867
                            )
                            self.group_expr()

                            self._state.following.pop()

                elif alt44 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:5: create_expr
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_aug_expr_stmt891
                    )
                    self.create_expr()

                    self._state.following.pop()

                elif alt44 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:19: instantiate_expr
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_aug_expr_stmt895
                    )
                    self.instantiate_expr()

                    self._state.following.pop()

                elif alt44 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:38: get_expr
                    self._state.following.append(
                        self.FOLLOW_get_expr_in_aug_expr_stmt899
                    )
                    self.get_expr()

                    self._state.following.pop()

                elif alt44 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:49: group_expr
                    self._state.following.append(
                        self.FOLLOW_group_expr_in_aug_expr_stmt903
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:1: fetch_expr : FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )? ;
    def fetch_expr(
        self,
    ):
        retval = self.fetch_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:12: ( FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:14: FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )?
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr912)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr914)
                self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr916)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr918)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:35: ( MATCH test )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 == MATCH:
                    alt45 = 1
                if alt45 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:36: MATCH test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr921)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr923)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:49: ( LIMIT test )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 == LIMIT:
                    alt46 = 1
                if alt46 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:50: LIMIT test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr928)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr930)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:63: ( RECURSIVE )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if LA47_0 == RECURSIVE:
                    alt47 = 1
                if alt47 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:63: RECURSIVE
                    self.match(
                        self.input, RECURSIVE, self.FOLLOW_RECURSIVE_in_fetch_expr934
                    )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "fetch_expr"

    class aug_assign_return(ParserRuleReturnScope):
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

    # $ANTLR start "aug_assign"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:85:1: aug_assign : ( ADD_ASSIGN | SUB_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | POWER_ASSIGN | IDIV_ASSIGN );
    def aug_assign(
        self,
    ):
        retval = self.aug_assign_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:85:11: ( ADD_ASSIGN | SUB_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | POWER_ASSIGN | IDIV_ASSIGN )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {
                    ADD_ASSIGN,
                    AND_ASSIGN,
                    DIV_ASSIGN,
                    IDIV_ASSIGN,
                    LSHIFT_ASSIGN,
                    MOD_ASSIGN,
                    MULT_ASSIGN,
                    OR_ASSIGN,
                    POWER_ASSIGN,
                    RSHIFT_ASSIGN,
                    SUB_ASSIGN,
                    XOR_ASSIGN,
                }:
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

    # $ANTLR end "aug_assign"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:1: test : or_test ( IF or_test ELSE test )? ;
    def test(
        self,
    ):
        retval = self.test_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:13: ( or_test ( IF or_test ELSE test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:15: or_test ( IF or_test ELSE test )?
                self._state.following.append(self.FOLLOW_or_test_in_test1027)
                self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:23: ( IF or_test ELSE test )?
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if LA48_0 == IF:
                    alt48 = 1
                if alt48 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:24: IF or_test ELSE test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test1030)

                    self._state.following.append(self.FOLLOW_or_test_in_test1032)
                    self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test1034)

                    self._state.following.append(self.FOLLOW_test_in_test1036)
                    self.test()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:1: test_nocond : or_test ;
    def test_nocond(
        self,
    ):
        retval = self.test_nocond_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:13: ( or_test )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond1045)
                self.or_test()

                self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:1: or_test : and_test ( OR and_test )* ;
    def or_test(
        self,
    ):
        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:13: ( and_test ( OR and_test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:15: and_test ( OR and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test1056)
                self.and_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:24: ( OR and_test )*
                while True:  # loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if LA49_0 == OR:
                        alt49 = 1

                    if alt49 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:25: OR and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test1059)

                        self._state.following.append(
                            self.FOLLOW_and_test_in_or_test1061
                        )
                        self.and_test()

                        self._state.following.pop()

                    else:
                        break  # loop49

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:1: and_test : not_test ( AND not_test )* ;
    def and_test(
        self,
    ):
        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:13: ( not_test ( AND not_test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:15: not_test ( AND not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test1073)
                self.not_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:24: ( AND not_test )*
                while True:  # loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if LA50_0 == AND:
                        alt50 = 1

                    if alt50 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:25: AND not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test1076)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test1078
                        )
                        self.not_test()

                        self._state.following.pop()

                    else:
                        break  # loop50

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:1: not_test : ( NOT not_test | comparison );
    def not_test(
        self,
    ):
        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:13: ( NOT not_test | comparison )
                alt51 = 2
                LA51_0 = self.input.LA(1)

                if LA51_0 == NOT:
                    alt51 = 1
                elif LA51_0 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt51 = 2
                else:
                    nvae = NoViableAltException("", 51, 0, self.input)

                    raise nvae

                if alt51 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:15: NOT not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1090)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1092)
                    self.not_test()

                    self._state.following.pop()

                elif alt51 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:30: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test1096)
                    self.comparison()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:1: comparison : expr ( comp_op expr )* ;
    def comparison(
        self,
    ):
        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:13: ( expr ( comp_op expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:15: expr ( comp_op expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison1104)
                self.expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:20: ( comp_op expr )*
                while True:  # loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if LA52_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt52 = 1

                    if alt52 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:21: comp_op expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison1107
                        )
                        self.comp_op()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_expr_in_comparison1109)
                        self.expr()

                        self._state.following.pop()

                    else:
                        break  # loop52

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:1: comp_op : ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT );
    def comp_op(
        self,
    ):
        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:13: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                alt53 = 10
                LA53 = self.input.LA(1)
                if LA53 in {LT}:
                    alt53 = 1
                elif LA53 in {GT}:
                    alt53 = 2
                elif LA53 in {EQUALS}:
                    alt53 = 3
                elif LA53 in {GT_EQ}:
                    alt53 = 4
                elif LA53 in {LT_EQ}:
                    alt53 = 5
                elif LA53 in {NOT_EQ}:
                    alt53 = 6
                elif LA53 in {IN}:
                    alt53 = 7
                elif LA53 in {NOT}:
                    alt53 = 8
                elif LA53 in {IS}:
                    LA53_9 = self.input.LA(2)

                    if LA53_9 == NOT:
                        alt53 = 10
                    elif LA53_9 in {
                        BIT_NOT,
                        CHOICE,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LOG_UNIFORM,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NORMAL,
                        PLUS,
                        SEQUENCE,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                        UNIFORM,
                    }:
                        alt53 = 9
                    else:
                        nvae = NoViableAltException("", 53, 9, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 53, 0, self.input)

                    raise nvae

                if alt53 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:15: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_comp_op1122)

                elif alt53 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:20: GT
                    self.match(self.input, GT, self.FOLLOW_GT_in_comp_op1126)

                elif alt53 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:25: EQUALS
                    self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op1130)

                elif alt53 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:34: GT_EQ
                    self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op1134)

                elif alt53 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:42: LT_EQ
                    self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op1138)

                elif alt53 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:50: NOT_EQ
                    self.match(self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op1142)

                elif alt53 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:59: IN
                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1146)

                elif alt53 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:64: NOT IN
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1150)

                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1152)

                elif alt53 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:73: IS
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1156)

                elif alt53 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:78: IS NOT
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1160)

                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1162)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:1: expr : xor_expr ( BIT_OR xor_expr )* ;
    def expr(
        self,
    ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:13: ( xor_expr ( BIT_OR xor_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:15: xor_expr ( BIT_OR xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr1176)
                self.xor_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:24: ( BIT_OR xor_expr )*
                while True:  # loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if LA54_0 == BIT_OR:
                        alt54 = 1

                    if alt54 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:25: BIT_OR xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr1179)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr1181)
                        self.xor_expr()

                        self._state.following.pop()

                    else:
                        break  # loop54

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:1: xor_expr : and_expr ( XOR and_expr )* ;
    def xor_expr(
        self,
    ):
        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:13: ( and_expr ( XOR and_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:15: and_expr ( XOR and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1193)
                self.and_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:24: ( XOR and_expr )*
                while True:  # loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if LA55_0 == XOR:
                        alt55 = 1

                    if alt55 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:25: XOR and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr1196)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr1198
                        )
                        self.and_expr()

                        self._state.following.pop()

                    else:
                        break  # loop55

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:1: and_expr : shift_expr ( BIT_AND shift_expr )* ;
    def and_expr(
        self,
    ):
        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:13: ( shift_expr ( BIT_AND shift_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:15: shift_expr ( BIT_AND shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1210)
                self.shift_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:26: ( BIT_AND shift_expr )*
                while True:  # loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if LA56_0 == BIT_AND:
                        alt56 = 1

                    if alt56 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:27: BIT_AND shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr1213
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr1215
                        )
                        self.shift_expr()

                        self._state.following.pop()

                    else:
                        break  # loop56

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:1: shift_expr : arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* ;
    def shift_expr(
        self,
    ):
        retval = self.shift_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:13: ( arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:15: arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1225)
                self.arith_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:26: ( ( LSHIFT | RSHIFT ) arith_expr )*
                while True:  # loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if LA57_0 in {LSHIFT, RSHIFT}:
                        alt57 = 1

                    if alt57 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:27: ( LSHIFT | RSHIFT ) arith_expr
                        if self.input.LA(1) in {LSHIFT, RSHIFT}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr1236
                        )
                        self.arith_expr()

                        self._state.following.pop()

                    else:
                        break  # loop57

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:1: arith_expr : term ( ( PLUS | MINUS ) term )* ;
    def arith_expr(
        self,
    ):
        retval = self.arith_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:13: ( term ( ( PLUS | MINUS ) term )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:15: term ( ( PLUS | MINUS ) term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr1246)
                self.term()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:20: ( ( PLUS | MINUS ) term )*
                while True:  # loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if LA58_0 in {MINUS, PLUS}:
                        alt58 = 1

                    if alt58 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:21: ( PLUS | MINUS ) term
                        if self.input.LA(1) in {MINUS, PLUS}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_term_in_arith_expr1257)
                        self.term()

                        self._state.following.pop()

                    else:
                        break  # loop58

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:1: term : factor ( ( MUL | DIV | MOD | IDIV ) factor )* ;
    def term(
        self,
    ):
        retval = self.term_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:13: ( factor ( ( MUL | DIV | MOD | IDIV ) factor )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:15: factor ( ( MUL | DIV | MOD | IDIV ) factor )*
                self._state.following.append(self.FOLLOW_factor_in_term1273)
                self.factor()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:22: ( ( MUL | DIV | MOD | IDIV ) factor )*
                while True:  # loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if LA59_0 in {DIV, IDIV, MOD, MUL}:
                        alt59 = 1

                    if alt59 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:23: ( MUL | DIV | MOD | IDIV ) factor
                        if self.input.LA(1) in {DIV, IDIV, MOD, MUL}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_factor_in_term1292)
                        self.factor()

                        self._state.following.pop()

                    else:
                        break  # loop59

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:1: factor : ( ( PLUS | MINUS | BIT_NOT ) factor | power );
    def factor(
        self,
    ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:13: ( ( PLUS | MINUS | BIT_NOT ) factor | power )
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if LA60_0 in {BIT_NOT, MINUS, PLUS}:
                    alt60 = 1
                elif LA60_0 in {
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    NONE,
                    NORMAL,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt60 = 2
                else:
                    nvae = NoViableAltException("", 60, 0, self.input)

                    raise nvae

                if alt60 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:15: ( PLUS | MINUS | BIT_NOT ) factor
                    if self.input.LA(1) in {BIT_NOT, MINUS, PLUS}:
                        self.input.consume()
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse

                    self._state.following.append(self.FOLLOW_factor_in_factor1318)
                    self.factor()

                    self._state.following.pop()

                elif alt60 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:49: power
                    self._state.following.append(self.FOLLOW_power_in_factor1322)
                    self.power()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:1: power : atom_expr ( POWER factor )? ;
    def power(
        self,
    ):
        retval = self.power_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:13: ( atom_expr ( POWER factor )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power1335)
                self.atom_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:25: ( POWER factor )?
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if LA61_0 == POWER:
                    alt61 = 1
                if alt61 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power1338)

                    self._state.following.append(self.FOLLOW_factor_in_power1340)
                    self.factor()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:1: atom_expr : atom ( trailer )* ;
    def atom_expr(
        self,
    ):
        retval = self.atom_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:13: ( atom ( trailer )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:15: atom ( trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr1351)
                self.atom()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:20: ( trailer )*
                while True:  # loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if LA62_0 in {DOT, LBRACK}:
                        alt62 = 1

                    if alt62 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:23: trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr1356
                        )
                        self.trailer()

                        self._state.following.pop()

                    else:
                        break  # loop62

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:1: atom : ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE );
    def atom(
        self,
    ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:5: ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE )
                alt69 = 13
                LA69 = self.input.LA(1)
                if LA69 in {LPAREN}:
                    alt69 = 1
                elif LA69 in {LBRACK}:
                    alt69 = 2
                elif LA69 in {LT}:
                    alt69 = 3
                elif LA69 in {LBRACE}:
                    alt69 = 4
                elif LA69 in {ID, UNDERSCORE}:
                    alt69 = 5
                elif LA69 in {SETTING_ID}:
                    alt69 = 6
                elif LA69 in {CHOICE, LOG_UNIFORM, NORMAL, SEQUENCE, UNIFORM}:
                    alt69 = 7
                elif LA69 in {INTEGER}:
                    alt69 = 8
                elif LA69 in {FLOAT_NUMBER}:
                    alt69 = 9
                elif LA69 in {STRING}:
                    alt69 = 10
                elif LA69 in {NONE}:
                    alt69 = 11
                elif LA69 in {TRUE}:
                    alt69 = 12
                elif LA69 in {FALSE}:
                    alt69 = 13
                else:
                    nvae = NoViableAltException("", 69, 0, self.input)

                    raise nvae

                if alt69 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:3: LPAREN test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1366)

                    self._state.following.append(self.FOLLOW_test_in_atom1368)
                    self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1370)

                elif alt69 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:5: LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom1376)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:12: ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) )
                    alt66 = 2
                    LA66 = self.input.LA(1)
                    if LA66 in {
                        BIT_NOT,
                        CHOICE,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        LBRACE,
                        LBRACK,
                        LOG_UNIFORM,
                        LPAREN,
                        LT,
                        NONE,
                        NORMAL,
                        NOT,
                        PLUS,
                        RBRACK,
                        SEQUENCE,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                        UNIFORM,
                    }:
                        alt66 = 1
                    elif LA66 in {MINUS}:
                        LA66_2 = self.input.LA(2)

                        if LA66_2 in {
                            BIT_NOT,
                            CHOICE,
                            FALSE,
                            FLOAT_NUMBER,
                            ID,
                            LBRACE,
                            LBRACK,
                            LOG_UNIFORM,
                            LPAREN,
                            LT,
                            MINUS,
                            NONE,
                            NORMAL,
                            PLUS,
                            SEQUENCE,
                            SETTING_ID,
                            STRING,
                            TRUE,
                            UNDERSCORE,
                            UNIFORM,
                        }:
                            alt66 = 1
                        elif LA66_2 == INTEGER:
                            LA66_4 = self.input.LA(3)

                            if LA66_4 == RANGE:
                                alt66 = 2
                            elif LA66_4 in {
                                AND,
                                BIT_AND,
                                BIT_OR,
                                COMMA,
                                DIV,
                                DOT,
                                EQUALS,
                                FOR,
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
                                RBRACK,
                                RSHIFT,
                                XOR,
                            }:
                                alt66 = 1
                            else:
                                nvae = NoViableAltException("", 66, 4, self.input)

                                raise nvae

                        else:
                            nvae = NoViableAltException("", 66, 2, self.input)

                            raise nvae

                    elif LA66 in {INTEGER}:
                        LA66_3 = self.input.LA(2)

                        if LA66_3 == RANGE:
                            alt66 = 2
                        elif LA66_3 in {
                            AND,
                            BIT_AND,
                            BIT_OR,
                            COMMA,
                            DIV,
                            DOT,
                            EQUALS,
                            FOR,
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
                            RBRACK,
                            RSHIFT,
                            XOR,
                        }:
                            alt66 = 1
                        else:
                            nvae = NoViableAltException("", 66, 3, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 66, 0, self.input)

                        raise nvae

                    if alt66 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:13: ( testlist_comp )?
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:13: ( testlist_comp )?
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if LA63_0 in {
                            BIT_NOT,
                            CHOICE,
                            FALSE,
                            FLOAT_NUMBER,
                            ID,
                            INTEGER,
                            LBRACE,
                            LBRACK,
                            LOG_UNIFORM,
                            LPAREN,
                            LT,
                            MINUS,
                            NONE,
                            NORMAL,
                            NOT,
                            PLUS,
                            SEQUENCE,
                            SETTING_ID,
                            STRING,
                            TRUE,
                            UNDERSCORE,
                            UNIFORM,
                        }:
                            alt63 = 1
                        if alt63 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:13: testlist_comp
                            self._state.following.append(
                                self.FOLLOW_testlist_comp_in_atom1379
                            )
                            self.testlist_comp()

                            self._state.following.pop()

                    elif alt66 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:30: ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER )
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:30: ( ( MINUS )? INTEGER )
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:31: ( MINUS )? INTEGER
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:31: ( MINUS )?
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if LA64_0 == MINUS:
                            alt64 = 1
                        if alt64 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:31: MINUS
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1385)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1388)

                        self.match(self.input, RANGE, self.FOLLOW_RANGE_in_atom1391)

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:53: ( ( MINUS )? INTEGER )
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:54: ( MINUS )? INTEGER
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:54: ( MINUS )?
                        alt65 = 2
                        LA65_0 = self.input.LA(1)

                        if LA65_0 == MINUS:
                            alt65 = 1
                        if alt65 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:54: MINUS
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1394)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1397)

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom1401)

                elif alt69 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom1407)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:8: ( vector_comp )?
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if LA67_0 in {
                        BIT_NOT,
                        CHOICE,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LOG_UNIFORM,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NORMAL,
                        PLUS,
                        SEQUENCE,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                        UNIFORM,
                    }:
                        alt67 = 1
                    if alt67 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom1409
                        )
                        self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom1412)

                elif alt69 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom1418)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:12: ( dict_or_set_maker )?
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if LA68_0 in {
                        BIT_NOT,
                        CHOICE,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LOG_UNIFORM,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NORMAL,
                        NOT,
                        PLUS,
                        SEQUENCE,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                        UNIFORM,
                    }:
                        alt68 = 1
                    if alt68 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom1420
                        )
                        self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom1423)

                elif alt69 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom1429)
                    self.name()

                    self._state.following.pop()

                elif alt69 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:12: SETTING_ID
                    self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom1433
                    )

                elif alt69 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:25: distribution_expr
                    self._state.following.append(
                        self.FOLLOW_distribution_expr_in_atom1437
                    )
                    self.distribution_expr()

                    self._state.following.pop()

                elif alt69 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:5: INTEGER
                    self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1443)

                elif alt69 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:15: FLOAT_NUMBER
                    self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom1447
                    )

                elif alt69 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:30: STRING
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_atom1451)

                elif alt69 == 11:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:39: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom1455)

                elif alt69 == 12:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:46: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom1459)

                elif alt69 == 13:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:53: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom1463)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:126:1: name : ( ID | UNDERSCORE );
    def name(
        self,
    ):
        retval = self.name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:126:5: ( ID | UNDERSCORE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {ID, UNDERSCORE}:
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

    # $ANTLR end "name"

    class distribution_expr_return(ParserRuleReturnScope):
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

    # $ANTLR start "distribution_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:1: distribution_expr : distribution LPAREN arglist RPAREN ;
    def distribution_expr(
        self,
    ):
        retval = self.distribution_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:19: ( distribution LPAREN arglist RPAREN )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:21: distribution LPAREN arglist RPAREN
                self._state.following.append(
                    self.FOLLOW_distribution_in_distribution_expr1492
                )
                self.distribution()

                self._state.following.pop()

                self.match(
                    self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution_expr1494
                )

                self._state.following.append(
                    self.FOLLOW_arglist_in_distribution_expr1496
                )
                self.arglist()

                self._state.following.pop()

                self.match(
                    self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution_expr1498
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "distribution_expr"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:140:1: distribution : ( UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM );
    def distribution(
        self,
    ):
        retval = self.distribution_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:140:19: ( UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {CHOICE, LOG_UNIFORM, NORMAL, SEQUENCE, UNIFORM}:
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:1: testlist_comp : test ( comp_for | ( COMMA test )* ) ;
    def testlist_comp(
        self,
    ):
        retval = self.testlist_comp_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:15: ( test ( comp_for | ( COMMA test )* ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:17: test ( comp_for | ( COMMA test )* )
                self._state.following.append(self.FOLLOW_test_in_testlist_comp1534)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:22: ( comp_for | ( COMMA test )* )
                alt71 = 2
                LA71_0 = self.input.LA(1)

                if LA71_0 == FOR:
                    alt71 = 1
                elif LA71_0 in {COMMA, RBRACK}:
                    alt71 = 2
                else:
                    nvae = NoViableAltException("", 71, 0, self.input)

                    raise nvae

                if alt71 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:24: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp1538
                    )
                    self.comp_for()

                    self._state.following.pop()

                elif alt71 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:35: ( COMMA test )*
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:35: ( COMMA test )*
                    while True:  # loop70
                        alt70 = 2
                        LA70_0 = self.input.LA(1)

                        if LA70_0 == COMMA:
                            alt70 = 1

                        if alt70 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:36: COMMA test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp1543,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp1545
                            )
                            self.test()

                            self._state.following.pop()

                        else:
                            break  # loop70

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:143:1: vector_comp : expr COMMA expr COMMA expr ;
    def vector_comp(
        self,
    ):
        retval = self.vector_comp_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:143:15: ( expr COMMA expr COMMA expr )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:143:17: expr COMMA expr COMMA expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp1557)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1559)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1561)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1563)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1565)
                self.expr()

                self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:1: trailer : ( LBRACK subscriptlist RBRACK | DOT name );
    def trailer(
        self,
    ):
        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:15: ( LBRACK subscriptlist RBRACK | DOT name )
                alt72 = 2
                LA72_0 = self.input.LA(1)

                if LA72_0 == LBRACK:
                    alt72 = 1
                elif LA72_0 == DOT:
                    alt72 = 2
                else:
                    nvae = NoViableAltException("", 72, 0, self.input)

                    raise nvae

                if alt72 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer1581)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer1583
                    )
                    self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer1585)

                elif alt72 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:47: DOT name
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer1589)

                    self._state.following.append(self.FOLLOW_name_in_trailer1591)
                    self.name()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:1: arglist : argument ( COMMA argument )* ;
    def arglist(
        self,
    ):
        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:15: ( argument ( COMMA argument )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:17: argument ( COMMA argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist1604)
                self.argument()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:26: ( COMMA argument )*
                while True:  # loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if LA73_0 == COMMA:
                        alt73 = 1

                    if alt73 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:27: COMMA argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist1607)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist1609
                        )
                        self.argument()

                        self._state.following.pop()

                    else:
                        break  # loop73

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:1: argument : test ( comp_for | ASSIGN test )? ;
    def argument(
        self,
    ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:15: ( test ( comp_for | ASSIGN test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:17: test ( comp_for | ASSIGN test )?
                self._state.following.append(self.FOLLOW_test_in_argument1623)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:22: ( comp_for | ASSIGN test )?
                alt74 = 3
                LA74_0 = self.input.LA(1)

                if LA74_0 == FOR:
                    alt74 = 1
                elif LA74_0 == ASSIGN:
                    alt74 = 2
                if alt74 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:23: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_argument1626)
                    self.comp_for()

                    self._state.following.pop()

                elif alt74 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:34: ASSIGN test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument1630)

                    self._state.following.append(self.FOLLOW_test_in_argument1632)
                    self.test()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:1: subscriptlist : subscript_ ( COMMA subscript_ )* ;
    def subscriptlist(
        self,
    ):
        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:15: ( subscript_ ( COMMA subscript_ )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:17: subscript_ ( COMMA subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist1641
                )
                self.subscript_()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:28: ( COMMA subscript_ )*
                while True:  # loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if LA75_0 == COMMA:
                        alt75 = 1

                    if alt75 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:29: COMMA subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist1644
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist1646
                        )
                        self.subscript_()

                        self._state.following.pop()

                    else:
                        break  # loop75

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:1: subscript_ : ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? );
    def subscript_(
        self,
    ):
        retval = self.subscript__return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:15: ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? )
                alt81 = 2
                LA81_0 = self.input.LA(1)

                if LA81_0 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    NOT,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt81 = 1
                elif LA81_0 == COLON:
                    alt81 = 2
                else:
                    nvae = NoViableAltException("", 81, 0, self.input)

                    raise nvae

                if alt81 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:17: test ( COLON ( test )? ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_1658)
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:22: ( COLON ( test )? ( sliceop )? )?
                    alt78 = 2
                    LA78_0 = self.input.LA(1)

                    if LA78_0 == COLON:
                        alt78 = 1
                    if alt78 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:23: COLON ( test )? ( sliceop )?
                        self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_1661
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:29: ( test )?
                        alt76 = 2
                        LA76_0 = self.input.LA(1)

                        if LA76_0 in {
                            BIT_NOT,
                            CHOICE,
                            FALSE,
                            FLOAT_NUMBER,
                            ID,
                            INTEGER,
                            LBRACE,
                            LBRACK,
                            LOG_UNIFORM,
                            LPAREN,
                            LT,
                            MINUS,
                            NONE,
                            NORMAL,
                            NOT,
                            PLUS,
                            SEQUENCE,
                            SETTING_ID,
                            STRING,
                            TRUE,
                            UNDERSCORE,
                            UNIFORM,
                        }:
                            alt76 = 1
                        if alt76 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:30: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_1664
                            )
                            self.test()

                            self._state.following.pop()

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:37: ( sliceop )?
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if LA77_0 == COLON:
                            alt77 = 1
                        if alt77 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:38: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_1669
                            )
                            self.sliceop()

                            self._state.following.pop()

                elif alt81 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:52: COLON ( test )? ( sliceop )?
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript_1677)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:58: ( test )?
                    alt79 = 2
                    LA79_0 = self.input.LA(1)

                    if LA79_0 in {
                        BIT_NOT,
                        CHOICE,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        INTEGER,
                        LBRACE,
                        LBRACK,
                        LOG_UNIFORM,
                        LPAREN,
                        LT,
                        MINUS,
                        NONE,
                        NORMAL,
                        NOT,
                        PLUS,
                        SEQUENCE,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                        UNIFORM,
                    }:
                        alt79 = 1
                    if alt79 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:59: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_1680)
                        self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:66: ( sliceop )?
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if LA80_0 == COLON:
                        alt80 = 1
                    if alt80 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:67: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_1685
                        )
                        self.sliceop()

                        self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:1: sliceop : COLON ( test )? ;
    def sliceop(
        self,
    ):
        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:15: ( COLON ( test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop1700)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:23: ( test )?
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if LA82_0 in {
                    BIT_NOT,
                    CHOICE,
                    FALSE,
                    FLOAT_NUMBER,
                    ID,
                    INTEGER,
                    LBRACE,
                    LBRACK,
                    LOG_UNIFORM,
                    LPAREN,
                    LT,
                    MINUS,
                    NONE,
                    NORMAL,
                    NOT,
                    PLUS,
                    SEQUENCE,
                    SETTING_ID,
                    STRING,
                    TRUE,
                    UNDERSCORE,
                    UNIFORM,
                }:
                    alt82 = 1
                if alt82 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop1702)
                    self.test()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:1: exprlist : expr ( COMMA expr )* ;
    def exprlist(
        self,
    ):
        retval = self.exprlist_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:10: ( expr ( COMMA expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:12: expr ( COMMA expr )*
                self._state.following.append(self.FOLLOW_expr_in_exprlist1711)
                self.expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:17: ( COMMA expr )*
                while True:  # loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if LA83_0 == COMMA:
                        alt83 = 1

                    if alt83 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:18: COMMA expr
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist1714)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist1716)
                        self.expr()

                        self._state.following.pop()

                    else:
                        break  # loop83

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:1: testlist : test ( COMMA test )* ;
    def testlist(
        self,
    ):
        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:10: ( test ( COMMA test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:12: test ( COMMA test )*
                self._state.following.append(self.FOLLOW_test_in_testlist1725)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:17: ( COMMA test )*
                while True:  # loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if LA84_0 == COMMA:
                        alt84 = 1

                    if alt84 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:18: COMMA test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist1728)

                        self._state.following.append(self.FOLLOW_test_in_testlist1730)
                        self.test()

                        self._state.following.pop()

                    else:
                        break  # loop84

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:1: dict_or_set_maker : test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) ;
    def dict_or_set_maker(
        self,
    ):
        retval = self.dict_or_set_maker_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:18: ( test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:3: test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker1740)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:8: ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                alt89 = 2
                LA89_0 = self.input.LA(1)

                if LA89_0 == COLON:
                    alt89 = 1
                elif LA89_0 in {COMMA, FOR, RBRACE}:
                    alt89 = 2
                else:
                    nvae = NoViableAltException("", 89, 0, self.input)

                    raise nvae

                if alt89 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:10: COLON test ( comp_for | ( COMMA test COLON test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker1744
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker1746
                    )
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:21: ( comp_for | ( COMMA test COLON test )* )
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if LA86_0 == FOR:
                        alt86 = 1
                    elif LA86_0 in {COMMA, RBRACE}:
                        alt86 = 2
                    else:
                        nvae = NoViableAltException("", 86, 0, self.input)

                        raise nvae

                    if alt86 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:22: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1749
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt86 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:33: ( COMMA test COLON test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:33: ( COMMA test COLON test )*
                        while True:  # loop85
                            alt85 = 2
                            LA85_0 = self.input.LA(1)

                            if LA85_0 == COMMA:
                                alt85 = 1

                            if alt85 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:34: COMMA test COLON test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker1754,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1756
                                )
                                self.test()

                                self._state.following.pop()

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker1758,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1760
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop85

                elif alt89 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:10: ( comp_for | ( COMMA test )* )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:10: ( comp_for | ( COMMA test )* )
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if LA88_0 == FOR:
                        alt88 = 1
                    elif LA88_0 in {COMMA, RBRACE}:
                        alt88 = 2
                    else:
                        nvae = NoViableAltException("", 88, 0, self.input)

                        raise nvae

                    if alt88 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:11: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1775
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt88 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:22: ( COMMA test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:22: ( COMMA test )*
                        while True:  # loop87
                            alt87 = 2
                            LA87_0 = self.input.LA(1)

                            if LA87_0 == COMMA:
                                alt87 = 1

                            if alt87 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:23: COMMA test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker1780,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1782
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop87

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:1: comp_iter : ( comp_for | comp_if );
    def comp_iter(
        self,
    ):
        retval = self.comp_iter_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:11: ( comp_for | comp_if )
                alt90 = 2
                LA90_0 = self.input.LA(1)

                if LA90_0 == FOR:
                    alt90 = 1
                elif LA90_0 == IF:
                    alt90 = 2
                else:
                    nvae = NoViableAltException("", 90, 0, self.input)

                    raise nvae

                if alt90 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:13: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter1796)
                    self.comp_for()

                    self._state.following.pop()

                elif alt90 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:24: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter1800)
                    self.comp_if()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:1: comp_for : FOR exprlist IN or_test ( comp_iter )? ;
    def comp_for(
        self,
    ):
        retval = self.comp_for_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:11: ( FOR exprlist IN or_test ( comp_iter )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:13: FOR exprlist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for1808)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for1810)
                self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for1812)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for1814)
                self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:37: ( comp_iter )?
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if LA91_0 in {FOR, IF}:
                    alt91 = 1
                if alt91 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:37: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for1816)
                    self.comp_iter()

                    self._state.following.pop()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:161:1: comp_if : IF test_nocond ( comp_iter )? ;
    def comp_if(
        self,
    ):
        retval = self.comp_if_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:161:11: ( IF test_nocond ( comp_iter )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:161:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if1826)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if1828)
                self.test_nocond()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:161:28: ( comp_iter )?
                alt92 = 2
                LA92_0 = self.input.LA(1)

                if LA92_0 in {FOR, IF}:
                    alt92 = 1
                if alt92 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:161:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if1830)
                    self.comp_iter()

                    self._state.following.pop()

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "comp_if"

    FOLLOW_declaration_in_scenario44 = frozenset([1, 79, 111, 120, 135])
    FOLLOW_NEWLINE_in_scenario46 = frozenset([1, 79, 111, 120, 135])
    FOLLOW_settings_in_scenario49 = frozenset([1, 120, 135])
    FOLLOW_stage_in_scenario52 = frozenset([1, 135])
    FOLLOW_writers_in_scenario55 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration65 = frozenset([45, 130])
    FOLLOW_name_in_declaration67 = frozenset([17, 79])
    FOLLOW_COLON_in_declaration70 = frozenset([45, 130])
    FOLLOW_name_in_declaration72 = frozenset([79])
    FOLLOW_NEWLINE_in_declaration76 = frozenset([1])
    FOLLOW_SETTINGS_in_settings86 = frozenset([17])
    FOLLOW_COLON_in_settings88 = frozenset([79])
    FOLLOW_NEWLINE_in_settings90 = frozenset([52])
    FOLLOW_INDENT_in_settings92 = frozenset([45])
    FOLLOW_option_in_settings94 = frozenset([21, 45])
    FOLLOW_DEDENT_in_settings97 = frozenset([1])
    FOLLOW_STAGE_in_stage110 = frozenset([17])
    FOLLOW_COLON_in_stage112 = frozenset([79])
    FOLLOW_NEWLINE_in_stage114 = frozenset([52])
    FOLLOW_INDENT_in_stage116 = frozenset(
        [
            12,
            16,
            20,
            26,
            30,
            33,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            87,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_stmts_in_stage118 = frozenset([21])
    FOLLOW_DEDENT_in_stage120 = frozenset([1])
    FOLLOW_WRITERS_in_writers131 = frozenset([17])
    FOLLOW_COLON_in_writers133 = frozenset([79])
    FOLLOW_NEWLINE_in_writers135 = frozenset([52])
    FOLLOW_INDENT_in_writers137 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_expr_stmt_in_writers140 = frozenset(
        [
            12,
            16,
            21,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_writer_in_writers144 = frozenset(
        [
            12,
            16,
            21,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_DEDENT_in_writers148 = frozenset([1])
    FOLLOW_ID_in_option156 = frozenset([7])
    FOLLOW_ASSIGN_in_option158 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_option160 = frozenset([79])
    FOLLOW_NEWLINE_in_option162 = frozenset([1])
    FOLLOW_open_stmt_in_stmts170 = frozenset(
        [
            12,
            16,
            20,
            26,
            30,
            33,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_aug_expr_stmt_in_stmts174 = frozenset(
        [
            1,
            12,
            16,
            20,
            26,
            30,
            33,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_edit_stmt_in_stmts178 = frozenset(
        [
            1,
            12,
            16,
            20,
            26,
            30,
            33,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_behavior_stmt_in_stmts182 = frozenset(
        [
            1,
            12,
            16,
            20,
            26,
            30,
            33,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_ID_in_writer191 = frozenset([17])
    FOLLOW_COLON_in_writer193 = frozenset([79])
    FOLLOW_NEWLINE_in_writer195 = frozenset([52])
    FOLLOW_INDENT_in_writer197 = frozenset([45])
    FOLLOW_option_in_writer199 = frozenset([21, 45])
    FOLLOW_DEDENT_in_writer202 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt214 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_open_stmt216 = frozenset([79])
    FOLLOW_NEWLINE_in_open_stmt218 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt225 = frozenset([45, 126, 130])
    FOLLOW_TIMELINE_in_edit_stmt228 = frozenset([17])
    FOLLOW_name_in_edit_stmt232 = frozenset([17])
    FOLLOW_edit_block_in_edit_stmt235 = frozenset([1])
    FOLLOW_CREATE_in_create_expr244 = frozenset(
        [
            12,
            14,
            16,
            33,
            35,
            39,
            45,
            54,
            57,
            58,
            61,
            64,
            66,
            69,
            72,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            113,
            114,
            121,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_create_expr246 = frozenset([14, 39, 61, 72, 113, 114, 121])
    FOLLOW_STEREO_in_create_expr256 = frozenset([14])
    FOLLOW_CAMERA_in_create_expr259 = frozenset([17, 79])
    FOLLOW_shapes_in_create_expr263 = frozenset([17, 79])
    FOLLOW_light_type_in_create_expr267 = frozenset([60])
    FOLLOW_LIGHT_in_create_expr269 = frozenset([17, 79])
    FOLLOW_FROM_in_create_expr273 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_create_expr275 = frozenset([17, 79])
    FOLLOW_edit_block_in_create_expr279 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr283 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr292 = frozenset([17])
    FOLLOW_simple_block_in_create_expr295 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr336 = frozenset(
        [
            12,
            16,
            33,
            35,
            39,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_instantiate_expr339 = frozenset([39])
    FOLLOW_FROM_in_instantiate_expr343 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_instantiate_expr345 = frozenset([17, 79])
    FOLLOW_edit_block_in_instantiate_expr348 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr352 = frozenset([1])
    FOLLOW_GROUP_in_group_expr366 = frozenset([58])
    FOLLOW_LBRACK_in_group_expr368 = frozenset([45, 130])
    FOLLOW_name_in_group_expr370 = frozenset([18, 98])
    FOLLOW_COMMA_in_group_expr373 = frozenset([45, 130])
    FOLLOW_name_in_group_expr375 = frozenset([18, 98])
    FOLLOW_RBRACK_in_group_expr379 = frozenset([17, 79])
    FOLLOW_edit_block_in_group_expr382 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr386 = frozenset([1])
    FOLLOW_GET_in_get_expr402 = frozenset(
        [
            12,
            14,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            60,
            64,
            66,
            69,
            72,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_CAMERA_in_get_expr406 = frozenset([8])
    FOLLOW_LIGHT_in_get_expr410 = frozenset([8])
    FOLLOW_MATERIAL_in_get_expr414 = frozenset([8])
    FOLLOW_name_in_get_expr418 = frozenset([8])
    FOLLOW_AT_in_get_expr421 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_get_expr425 = frozenset([17, 79])
    FOLLOW_simple_block_in_get_expr428 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr432 = frozenset([1])
    FOLLOW_COLON_in_edit_block443 = frozenset([79])
    FOLLOW_NEWLINE_in_edit_block445 = frozenset([52])
    FOLLOW_INDENT_in_edit_block447 = frozenset(
        [15, 30, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_attr_in_edit_block450 = frozenset(
        [15, 21, 30, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block454 = frozenset(
        [15, 21, 30, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_DEDENT_in_edit_block458 = frozenset([1])
    FOLLOW_COLON_in_simple_block465 = frozenset([79])
    FOLLOW_NEWLINE_in_simple_block467 = frozenset([52])
    FOLLOW_INDENT_in_simple_block469 = frozenset([45, 130])
    FOLLOW_simple_attr_in_simple_block471 = frozenset([21, 45, 130])
    FOLLOW_DEDENT_in_simple_block474 = frozenset([1])
    FOLLOW_core_attr_in_attr491 = frozenset([1])
    FOLLOW_simple_attr_in_attr495 = frozenset([1])
    FOLLOW_compound_attr_in_attr499 = frozenset([1])
    FOLLOW_name_in_simple_attr508 = frozenset(
        [
            12,
            16,
            17,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            79,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_COLON_in_simple_attr511 = frozenset([45, 130])
    FOLLOW_name_in_simple_attr513 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            79,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_simple_attr517 = frozenset([79])
    FOLLOW_NEWLINE_in_simple_attr520 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr529 = frozenset([86])
    FOLLOW_ON_in_compound_attr531 = frozenset([45, 130])
    FOLLOW_name_in_compound_attr533 = frozenset([17, 79])
    FOLLOW_ROT_AROUND_in_compound_attr537 = frozenset([45, 130])
    FOLLOW_name_in_compound_attr539 = frozenset([17, 79])
    FOLLOW_PHYSICS_in_compound_attr543 = frozenset([17, 79])
    FOLLOW_simple_block_in_compound_attr547 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr551 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr568 = frozenset([9, 127])
    FOLLOW_AXIS_in_core_attr570 = frozenset([127])
    FOLLOW_TO_in_core_attr573 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr575 = frozenset([79])
    FOLLOW_CAM_TRANSLATE_in_core_attr583 = frozenset([127])
    FOLLOW_TO_in_core_attr585 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr587 = frozenset([79])
    FOLLOW_ROTATE_in_core_attr595 = frozenset(
        [
            9,
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_AXIS_in_core_attr597 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr600 = frozenset([79, 89])
    FOLLOW_ORDER_in_core_attr602 = frozenset([79])
    FOLLOW_SCALE_in_core_attr611 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr613 = frozenset([79])
    FOLLOW_LOOK_AT_in_core_attr621 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr623 = frozenset([79])
    FOLLOW_UP_AXIS_in_core_attr631 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr633 = frozenset([79])
    FOLLOW_SIZE_in_core_attr641 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr643 = frozenset([79])
    FOLLOW_SEMANTICS_in_core_attr651 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr653 = frozenset([79])
    FOLLOW_VISIBLE_in_core_attr661 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_core_attr663 = frozenset([79])
    FOLLOW_NEWLINE_in_core_attr669 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt679 = frozenset([17])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt681 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block688 = frozenset([79])
    FOLLOW_NEWLINE_in_inner_behavior_block690 = frozenset([52])
    FOLLOW_INDENT_in_inner_behavior_block692 = frozenset(
        [15, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_attr_in_inner_behavior_block694 = frozenset(
        [15, 21, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_DEDENT_in_inner_behavior_block697 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt708 = frozenset([17])
    FOLLOW_behavior_block_in_behavior_stmt710 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr718 = frozenset(
        [
            12,
            16,
            33,
            35,
            38,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            125,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_behavior_expr720 = frozenset([38, 125])
    FOLLOW_set_in_behavior_expr723 = frozenset([1])
    FOLLOW_COLON_in_behavior_block736 = frozenset([79])
    FOLLOW_NEWLINE_in_behavior_block738 = frozenset([52])
    FOLLOW_INDENT_in_behavior_block740 = frozenset(
        [
            12,
            16,
            20,
            26,
            33,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_aug_expr_stmt_in_behavior_block743 = frozenset(
        [
            12,
            16,
            20,
            21,
            26,
            33,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_edit_stmt_in_behavior_block747 = frozenset(
        [
            12,
            16,
            20,
            21,
            26,
            33,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_DEDENT_in_behavior_block751 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt761 = frozenset(
        [4, 6, 7, 24, 47, 68, 75, 77, 90, 95, 104, 124, 137]
    )
    FOLLOW_aug_assign_in_expr_stmt764 = frozenset(
        [
            12,
            16,
            33,
            34,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_ASSIGN_in_expr_stmt768 = frozenset(
        [
            12,
            16,
            33,
            34,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_testlist_in_expr_stmt772 = frozenset([79])
    FOLLOW_fetch_expr_in_expr_stmt776 = frozenset([79])
    FOLLOW_NEWLINE_in_expr_stmt779 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt792 = frozenset(
        [4, 6, 7, 24, 47, 68, 75, 77, 90, 95, 104, 124, 137]
    )
    FOLLOW_aug_assign_in_aug_expr_stmt802 = frozenset(
        [
            12,
            16,
            33,
            34,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            79,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt805 = frozenset([79])
    FOLLOW_fetch_expr_in_aug_expr_stmt809 = frozenset([79])
    FOLLOW_NEWLINE_in_aug_expr_stmt813 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt823 = frozenset(
        [
            12,
            16,
            20,
            33,
            34,
            35,
            40,
            41,
            45,
            53,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt836 = frozenset([79])
    FOLLOW_fetch_expr_in_aug_expr_stmt840 = frozenset([79])
    FOLLOW_NEWLINE_in_aug_expr_stmt843 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt855 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt859 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt863 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt867 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt891 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt895 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt899 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt903 = frozenset([1])
    FOLLOW_FETCH_in_fetch_expr912 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_fetch_expr914 = frozenset([39])
    FOLLOW_FROM_in_fetch_expr916 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_fetch_expr918 = frozenset([1, 62, 71, 99])
    FOLLOW_MATCH_in_fetch_expr921 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_fetch_expr923 = frozenset([1, 62, 99])
    FOLLOW_LIMIT_in_fetch_expr928 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_fetch_expr930 = frozenset([1, 99])
    FOLLOW_RECURSIVE_in_fetch_expr934 = frozenset([1])
    FOLLOW_or_test_in_test1027 = frozenset([1, 50])
    FOLLOW_IF_in_test1030 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_or_test_in_test1032 = frozenset([28])
    FOLLOW_ELSE_in_test1034 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_test1036 = frozenset([1])
    FOLLOW_or_test_in_test_nocond1045 = frozenset([1])
    FOLLOW_and_test_in_or_test1056 = frozenset([1, 88])
    FOLLOW_OR_in_or_test1059 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_and_test_in_or_test1061 = frozenset([1, 88])
    FOLLOW_not_test_in_and_test1073 = frozenset([1, 5])
    FOLLOW_AND_in_and_test1076 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_not_test_in_and_test1078 = frozenset([1, 5])
    FOLLOW_NOT_in_not_test1090 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_not_test_in_not_test1092 = frozenset([1])
    FOLLOW_comparison_in_not_test1096 = frozenset([1])
    FOLLOW_expr_in_comparison1104 = frozenset([1, 29, 42, 43, 51, 56, 69, 70, 83, 84])
    FOLLOW_comp_op_in_comparison1107 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_expr_in_comparison1109 = frozenset([1, 29, 42, 43, 51, 56, 69, 70, 83, 84])
    FOLLOW_LT_in_comp_op1122 = frozenset([1])
    FOLLOW_GT_in_comp_op1126 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op1130 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op1134 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op1138 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op1142 = frozenset([1])
    FOLLOW_IN_in_comp_op1146 = frozenset([1])
    FOLLOW_NOT_in_comp_op1150 = frozenset([51])
    FOLLOW_IN_in_comp_op1152 = frozenset([1])
    FOLLOW_IS_in_comp_op1156 = frozenset([1])
    FOLLOW_IS_in_comp_op1160 = frozenset([83])
    FOLLOW_NOT_in_comp_op1162 = frozenset([1])
    FOLLOW_xor_expr_in_expr1176 = frozenset([1, 13])
    FOLLOW_BIT_OR_in_expr1179 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_xor_expr_in_expr1181 = frozenset([1, 13])
    FOLLOW_and_expr_in_xor_expr1193 = frozenset([1, 136])
    FOLLOW_XOR_in_xor_expr1196 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_and_expr_in_xor_expr1198 = frozenset([1, 136])
    FOLLOW_shift_expr_in_and_expr1210 = frozenset([1, 11])
    FOLLOW_BIT_AND_in_and_expr1213 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_shift_expr_in_and_expr1215 = frozenset([1, 11])
    FOLLOW_arith_expr_in_shift_expr1225 = frozenset([1, 67, 103])
    FOLLOW_set_in_shift_expr1228 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_arith_expr_in_shift_expr1236 = frozenset([1, 67, 103])
    FOLLOW_term_in_arith_expr1246 = frozenset([1, 73, 92])
    FOLLOW_set_in_arith_expr1249 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_term_in_arith_expr1257 = frozenset([1, 73, 92])
    FOLLOW_factor_in_term1273 = frozenset([1, 23, 46, 74, 76])
    FOLLOW_set_in_term1276 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_factor_in_term1292 = frozenset([1, 23, 46, 74, 76])
    FOLLOW_set_in_factor1306 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_factor_in_factor1318 = frozenset([1])
    FOLLOW_power_in_factor1322 = frozenset([1])
    FOLLOW_atom_expr_in_power1335 = frozenset([1, 94])
    FOLLOW_POWER_in_power1338 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_factor_in_power1340 = frozenset([1])
    FOLLOW_atom_in_atom_expr1351 = frozenset([1, 25, 58])
    FOLLOW_trailer_in_atom_expr1356 = frozenset([1, 25, 58])
    FOLLOW_LPAREN_in_atom1366 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_atom1368 = frozenset([102])
    FOLLOW_RPAREN_in_atom1370 = frozenset([1])
    FOLLOW_LBRACK_in_atom1376 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            98,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_testlist_comp_in_atom1379 = frozenset([98])
    FOLLOW_MINUS_in_atom1385 = frozenset([54])
    FOLLOW_INTEGER_in_atom1388 = frozenset([96])
    FOLLOW_RANGE_in_atom1391 = frozenset([54, 73])
    FOLLOW_MINUS_in_atom1394 = frozenset([54])
    FOLLOW_INTEGER_in_atom1397 = frozenset([98])
    FOLLOW_RBRACK_in_atom1401 = frozenset([1])
    FOLLOW_LT_in_atom1407 = frozenset(
        [
            12,
            16,
            33,
            35,
            42,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_vector_comp_in_atom1409 = frozenset([42])
    FOLLOW_GT_in_atom1412 = frozenset([1])
    FOLLOW_LBRACE_in_atom1418 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            97,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_dict_or_set_maker_in_atom1420 = frozenset([97])
    FOLLOW_RBRACE_in_atom1423 = frozenset([1])
    FOLLOW_name_in_atom1429 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom1433 = frozenset([1])
    FOLLOW_distribution_expr_in_atom1437 = frozenset([1])
    FOLLOW_INTEGER_in_atom1443 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom1447 = frozenset([1])
    FOLLOW_STRING_in_atom1451 = frozenset([1])
    FOLLOW_NONE_in_atom1455 = frozenset([1])
    FOLLOW_TRUE_in_atom1459 = frozenset([1])
    FOLLOW_FALSE_in_atom1463 = frozenset([1])
    FOLLOW_distribution_in_distribution_expr1492 = frozenset([66])
    FOLLOW_LPAREN_in_distribution_expr1494 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_arglist_in_distribution_expr1496 = frozenset([102])
    FOLLOW_RPAREN_in_distribution_expr1498 = frozenset([1])
    FOLLOW_test_in_testlist_comp1534 = frozenset([1, 18, 36])
    FOLLOW_comp_for_in_testlist_comp1538 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp1543 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_testlist_comp1545 = frozenset([1, 18])
    FOLLOW_expr_in_vector_comp1557 = frozenset([18])
    FOLLOW_COMMA_in_vector_comp1559 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_expr_in_vector_comp1561 = frozenset([18])
    FOLLOW_COMMA_in_vector_comp1563 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_expr_in_vector_comp1565 = frozenset([1])
    FOLLOW_LBRACK_in_trailer1581 = frozenset(
        [
            12,
            16,
            17,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_subscriptlist_in_trailer1583 = frozenset([98])
    FOLLOW_RBRACK_in_trailer1585 = frozenset([1])
    FOLLOW_DOT_in_trailer1589 = frozenset([45, 130])
    FOLLOW_name_in_trailer1591 = frozenset([1])
    FOLLOW_argument_in_arglist1604 = frozenset([1, 18])
    FOLLOW_COMMA_in_arglist1607 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_argument_in_arglist1609 = frozenset([1, 18])
    FOLLOW_test_in_argument1623 = frozenset([1, 7, 36])
    FOLLOW_comp_for_in_argument1626 = frozenset([1])
    FOLLOW_ASSIGN_in_argument1630 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_argument1632 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist1641 = frozenset([1, 18])
    FOLLOW_COMMA_in_subscriptlist1644 = frozenset(
        [
            12,
            16,
            17,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_subscript__in_subscriptlist1646 = frozenset([1, 18])
    FOLLOW_test_in_subscript_1658 = frozenset([1, 17])
    FOLLOW_COLON_in_subscript_1661 = frozenset(
        [
            1,
            12,
            16,
            17,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_subscript_1664 = frozenset([1, 17])
    FOLLOW_sliceop_in_subscript_1669 = frozenset([1])
    FOLLOW_COLON_in_subscript_1677 = frozenset(
        [
            1,
            12,
            16,
            17,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_subscript_1680 = frozenset([1, 17])
    FOLLOW_sliceop_in_subscript_1685 = frozenset([1])
    FOLLOW_COLON_in_sliceop1700 = frozenset(
        [
            1,
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_sliceop1702 = frozenset([1])
    FOLLOW_expr_in_exprlist1711 = frozenset([1, 18])
    FOLLOW_COMMA_in_exprlist1714 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_expr_in_exprlist1716 = frozenset([1, 18])
    FOLLOW_test_in_testlist1725 = frozenset([1, 18])
    FOLLOW_COMMA_in_testlist1728 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_testlist1730 = frozenset([1, 18])
    FOLLOW_test_in_dict_or_set_maker1740 = frozenset([1, 17, 18, 36])
    FOLLOW_COLON_in_dict_or_set_maker1744 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1746 = frozenset([1, 18, 36])
    FOLLOW_comp_for_in_dict_or_set_maker1749 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1754 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1756 = frozenset([17])
    FOLLOW_COLON_in_dict_or_set_maker1758 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1760 = frozenset([1, 18])
    FOLLOW_comp_for_in_dict_or_set_maker1775 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1780 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1782 = frozenset([1, 18])
    FOLLOW_comp_for_in_comp_iter1796 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter1800 = frozenset([1])
    FOLLOW_FOR_in_comp_for1808 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_exprlist_in_comp_for1810 = frozenset([51])
    FOLLOW_IN_in_comp_for1812 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_or_test_in_comp_for1814 = frozenset([1, 36, 50])
    FOLLOW_comp_iter_in_comp_for1816 = frozenset([1])
    FOLLOW_IF_in_comp_if1826 = frozenset(
        [
            12,
            16,
            33,
            35,
            45,
            54,
            57,
            58,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            92,
            110,
            112,
            122,
            129,
            130,
            131,
        ]
    )
    FOLLOW_test_nocond_in_comp_if1828 = frozenset([1, 36, 50])
    FOLLOW_comp_iter_in_comp_if1830 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
