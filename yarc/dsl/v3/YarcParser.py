# $ANTLR 3.5.1 C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g 2023-04-29 10:47:04

import sys

from antlr3 import (
    BaseRecognizer,
    EarlyExitException,
    MismatchedSetException,
    NoViableAltException,
    Parser,
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

    # $ANTLR start "scenario"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:1: scenario : declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? ;
    def scenario(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:10: ( declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:12: declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )?
                self._state.following.append(self.FOLLOW_declaration_in_scenario35)
                self.declaration()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:24: ( NEWLINE )*
                while True:  # loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if LA1_0 == NEWLINE:
                        alt1 = 1

                    if alt1 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:24: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario37
                        )

                    else:
                        break  # loop1

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:33: ( settings )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if LA2_0 == SETTINGS:
                    alt2 = 1
                if alt2 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:33: settings
                    self._state.following.append(self.FOLLOW_settings_in_scenario40)
                    self.settings()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:43: ( stage )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if LA3_0 == STAGE:
                    alt3 = 1
                if alt3 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:43: stage
                    self._state.following.append(self.FOLLOW_stage_in_scenario43)
                    self.stage()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:50: ( writers )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == WRITERS:
                    alt4 = 1
                if alt4 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:8:50: writers
                    self._state.following.append(self.FOLLOW_writers_in_scenario46)
                    self.writers()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "scenario"

    # $ANTLR start "declaration"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:10:1: declaration : SCENARIO name ( COLON name )? NEWLINE ;
    def declaration(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:10:13: ( SCENARIO name ( COLON name )? NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:10:15: SCENARIO name ( COLON name )? NEWLINE
                self.match(self.input, SCENARIO, self.FOLLOW_SCENARIO_in_declaration56)

                self._state.following.append(self.FOLLOW_name_in_declaration58)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:10:29: ( COLON name )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if LA5_0 == COLON:
                    alt5 = 1
                if alt5 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:10:30: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration61)

                    self._state.following.append(self.FOLLOW_name_in_declaration63)
                    self.name()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_declaration67)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "declaration"

    # $ANTLR start "settings"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:1: settings : SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT ;
    def settings(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:13: ( SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:15: SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT
                self.match(self.input, SETTINGS, self.FOLLOW_SETTINGS_in_settings77)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_settings79)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_settings81)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_settings83)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:45: ( option )+
                cnt6 = 0
                while True:  # loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if LA6_0 == ID:
                        alt6 = 1

                    if alt6 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:11:45: option
                        self._state.following.append(self.FOLLOW_option_in_settings85)
                        self.option()

                        self._state.following.pop()

                    else:
                        if cnt6 >= 1:
                            break  # loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_settings88)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "settings"

    # $ANTLR start "stage"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:12:1: stage : STAGE COLON NEWLINE INDENT stmts DEDENT ;
    def stage(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:12:13: ( STAGE COLON NEWLINE INDENT stmts DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:12:15: STAGE COLON NEWLINE INDENT stmts DEDENT
                self.match(self.input, STAGE, self.FOLLOW_STAGE_in_stage101)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_stage103)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stage105)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stage107)

                self._state.following.append(self.FOLLOW_stmts_in_stage109)
                self.stmts()

                self._state.following.pop()

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stage111)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "stage"

    # $ANTLR start "writers"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:1: writers : WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT ;
    def writers(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:13: ( WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:15: WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT
                self.match(self.input, WRITERS, self.FOLLOW_WRITERS_in_writers122)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writers124)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writers126)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writers128)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:44: ( expr_stmt | writer )+
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:45: expr_stmt
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers131
                        )
                        self.expr_stmt()

                        self._state.following.pop()

                    elif alt7 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:57: writer
                        self._state.following.append(self.FOLLOW_writer_in_writers135)
                        self.writer()

                        self._state.following.pop()

                    else:
                        if cnt7 >= 1:
                            break  # loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writers139)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "writers"

    # $ANTLR start "option"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:15:1: option : ID ASSIGN test NEWLINE ;
    def option(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:15:8: ( ID ASSIGN test NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:15:10: ID ASSIGN test NEWLINE
                self.match(self.input, ID, self.FOLLOW_ID_in_option147)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_option149)

                self._state.following.append(self.FOLLOW_test_in_option151)
                self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_option153)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "option"

    # $ANTLR start "stmts"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:1: stmts : ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+ ;
    def stmts(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:8: ( ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+ )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:10: ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:10: ( open_stmt )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if LA8_0 == OPEN:
                    alt8 = 1
                if alt8 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:10: open_stmt
                    self._state.following.append(self.FOLLOW_open_stmt_in_stmts161)
                    self.open_stmt()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:21: ( aug_expr_stmt | edit_stmt | behavior_stmt )+
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:22: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts165
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt9 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:38: edit_stmt
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts169)
                        self.edit_stmt()

                        self._state.following.pop()

                    elif alt9 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:50: behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_behavior_stmt_in_stmts173
                        )
                        self.behavior_stmt()

                        self._state.following.pop()

                    else:
                        if cnt9 >= 1:
                            break  # loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "stmts"

    # $ANTLR start "writer"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:1: writer : ID COLON NEWLINE INDENT ( option )+ DEDENT ;
    def writer(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:8: ( ID COLON NEWLINE INDENT ( option )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:10: ID COLON NEWLINE INDENT ( option )+ DEDENT
                self.match(self.input, ID, self.FOLLOW_ID_in_writer182)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writer184)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer186)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writer188)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:34: ( option )+
                cnt10 = 0
                while True:  # loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if LA10_0 == ID:
                        alt10 = 1

                    if alt10 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:17:34: option
                        self._state.following.append(self.FOLLOW_option_in_writer190)
                        self.option()

                        self._state.following.pop()

                    else:
                        if cnt10 >= 1:
                            break  # loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writer193)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "writer"

    # $ANTLR start "open_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:21:1: open_stmt : OPEN test NEWLINE ;
    def open_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:21:11: ( OPEN test NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:21:13: OPEN test NEWLINE
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_open_stmt205)

                self._state.following.append(self.FOLLOW_test_in_open_stmt207)
                self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_open_stmt209)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "open_stmt"

    # $ANTLR start "edit_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:1: edit_stmt : EDIT ( TIMELINE | name ) edit_block ;
    def edit_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:11: ( EDIT ( TIMELINE | name ) edit_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:13: EDIT ( TIMELINE | name ) edit_block
                self.match(self.input, EDIT, self.FOLLOW_EDIT_in_edit_stmt216)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:18: ( TIMELINE | name )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:19: TIMELINE
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt219
                    )

                elif alt11 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:30: name
                    self._state.following.append(self.FOLLOW_name_in_edit_stmt223)
                    self.name()

                    self._state.following.pop()

                self._state.following.append(self.FOLLOW_edit_block_in_edit_stmt226)
                self.edit_block()

                self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "edit_stmt"

    # $ANTLR start "create_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:24:1: create_expr : CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) ;
    def create_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:24:12: ( CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:3: CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr235)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:10: ( test )?
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:10: test
                    self._state.following.append(self.FOLLOW_test_in_create_expr237)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:16: ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:6: ( STEREO )? CAMERA
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:6: ( STEREO )?
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if LA13_0 == STEREO:
                            alt13 = 1
                        if alt13 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:6: STEREO
                            self.match(
                                self.input, STEREO, self.FOLLOW_STEREO_in_create_expr247
                            )

                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr250
                        )

                    elif alt14 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:23: shapes
                        self._state.following.append(
                            self.FOLLOW_shapes_in_create_expr254
                        )
                        self.shapes()

                        self._state.following.pop()

                    elif alt14 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:32: light_type LIGHT
                        self._state.following.append(
                            self.FOLLOW_light_type_in_create_expr258
                        )
                        self.light_type()

                        self._state.following.pop()

                        self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr260
                        )

                    elif alt14 == 4:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:51: FROM test
                        self.match(self.input, FROM, self.FOLLOW_FROM_in_create_expr264)

                        self._state.following.append(self.FOLLOW_test_in_create_expr266)
                        self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:62: ( edit_block | NEWLINE )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:63: edit_block
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr270
                        )
                        self.edit_block()

                        self._state.following.pop()

                    elif alt15 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:76: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr274
                        )

                elif alt16 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:7: MATERIAL ( simple_block )
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr283
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:16: ( simple_block )
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:17: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_create_expr286
                    )
                    self.simple_block()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "create_expr"

    # $ANTLR start "shapes"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:1: shapes : ( SHAPES | SHAPES_OR_LIGHTS );
    def shapes(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:12: ( SHAPES | SHAPES_OR_LIGHTS )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {SHAPES, SHAPES_OR_LIGHTS}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "shapes"

    # $ANTLR start "light_type"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:1: light_type : ( LIGHT_TYPE | SHAPES_OR_LIGHTS );
    def light_type(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:12: ( LIGHT_TYPE | SHAPES_OR_LIGHTS )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {LIGHT_TYPE, SHAPES_OR_LIGHTS}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "light_type"

    # $ANTLR start "instantiate_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:1: instantiate_expr : INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) ;
    def instantiate_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:18: ( INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:20: INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE )
                self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr327,
                )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:32: ( test )?
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:33: test
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr330
                    )
                    self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr334)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr336)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:50: ( edit_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:51: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr339
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt18 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:34:64: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instantiate_expr343
                    )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "instantiate_expr"

    # $ANTLR start "group_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:1: group_expr : GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) ;
    def group_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:18: ( GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:20: GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE )
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_expr357)

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr359)

                self._state.following.append(self.FOLLOW_name_in_group_expr361)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:38: ( COMMA name )*
                while True:  # loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if LA19_0 == COMMA:
                        alt19 = 1

                    if alt19 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:39: COMMA name
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_group_expr364
                        )

                        self._state.following.append(self.FOLLOW_name_in_group_expr366)
                        self.name()

                        self._state.following.pop()

                    else:
                        break  # loop19

                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_group_expr370)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:59: ( edit_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:60: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr373
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt20 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:73: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_group_expr377
                    )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "group_expr"

    # $ANTLR start "get_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:1: get_expr : GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) ;
    def get_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:18: ( GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:20: GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE )
                self.match(self.input, GET, self.FOLLOW_GET_in_get_expr393)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:24: ( ( CAMERA | LIGHT | MATERIAL | name ) AT )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if LA22_0 in {CAMERA, LIGHT, MATERIAL}:
                    alt22 = 1
                elif LA22_0 in {ID, UNDERSCORE}:
                    LA22_2 = self.input.LA(2)

                    if LA22_2 == AT:
                        alt22 = 1
                if alt22 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:25: ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:25: ( CAMERA | LIGHT | MATERIAL | name )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:26: CAMERA
                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr397
                        )

                    elif alt21 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:35: LIGHT
                        self.match(self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr401)

                    elif alt21 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:43: MATERIAL
                        self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr405
                        )

                    elif alt21 == 4:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:54: name
                        self._state.following.append(self.FOLLOW_name_in_get_expr409)
                        self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr412)

                self._state.following.append(self.FOLLOW_test_in_get_expr416)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:70: ( simple_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:71: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr419
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt23 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:86: NEWLINE
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr423)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "get_expr"

    # $ANTLR start "edit_block"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:1: edit_block : COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT ;
    def edit_block(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:14: ( COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:16: COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block434)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block436)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block438)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:37: ( attr | inner_behavior_stmt )+
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:38: attr
                        self._state.following.append(self.FOLLOW_attr_in_edit_block441)
                        self.attr()

                        self._state.following.pop()

                    elif alt24 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:45: inner_behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_inner_behavior_stmt_in_edit_block445
                        )
                        self.inner_behavior_stmt()

                        self._state.following.pop()

                    else:
                        if cnt24 >= 1:
                            break  # loop24

                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_block449)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "edit_block"

    # $ANTLR start "simple_block"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:1: simple_block : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:14: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:16: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block456)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block458)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block460)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:37: ( simple_attr )+
                cnt25 = 0
                while True:  # loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if LA25_0 in {ID, UNDERSCORE}:
                        alt25 = 1

                    if alt25 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:37: simple_attr
                        self._state.following.append(
                            self.FOLLOW_simple_attr_in_simple_block462
                        )
                        self.simple_attr()

                        self._state.following.pop()

                    else:
                        if cnt25 >= 1:
                            break  # loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_simple_block465)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "simple_block"

    # $ANTLR start "attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:41:1: attr : ( core_attr | simple_attr | compound_attr );
    def attr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:41:15: ( core_attr | simple_attr | compound_attr )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:41:17: core_attr
                    self._state.following.append(self.FOLLOW_core_attr_in_attr482)
                    self.core_attr()

                    self._state.following.pop()

                elif alt26 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:41:29: simple_attr
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr486)
                    self.simple_attr()

                    self._state.following.pop()

                elif alt26 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:41:43: compound_attr
                    self._state.following.append(self.FOLLOW_compound_attr_in_attr490)
                    self.compound_attr()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "attr"

    # $ANTLR start "simple_attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:1: simple_attr : name ( COLON name )? ( test )? NEWLINE ;
    def simple_attr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:15: ( name ( COLON name )? ( test )? NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:17: name ( COLON name )? ( test )? NEWLINE
                self._state.following.append(self.FOLLOW_name_in_simple_attr499)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:22: ( COLON name )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if LA27_0 == COLON:
                    alt27 = 1
                if alt27 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:23: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr502)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr504)
                    self.name()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:36: ( test )?
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:42:36: test
                    self._state.following.append(self.FOLLOW_test_in_simple_attr508)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_attr511)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "simple_attr"

    # $ANTLR start "compound_attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:1: compound_attr : ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) ;
    def compound_attr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:15: ( ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:18: SCATTER ON name
                    self.match(
                        self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr520
                    )

                    self.match(self.input, ON, self.FOLLOW_ON_in_compound_attr522)

                    self._state.following.append(self.FOLLOW_name_in_compound_attr524)
                    self.name()

                    self._state.following.pop()

                elif alt29 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:36: ROT_AROUND name
                    self.match(
                        self.input,
                        ROT_AROUND,
                        self.FOLLOW_ROT_AROUND_in_compound_attr528,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr530)
                    self.name()

                    self._state.following.pop()

                elif alt29 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:54: PHYSICS
                    self.match(
                        self.input, PHYSICS, self.FOLLOW_PHYSICS_in_compound_attr534
                    )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:63: ( simple_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:64: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_compound_attr538
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt30 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:79: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_compound_attr542
                    )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "compound_attr"

    # $ANTLR start "core_attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:46:1: core_attr : ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE ;
    def core_attr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:46:10: ( ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:48:5: TRANSLATE ( AXIS )? TO test
                    self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr559
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:48:15: ( AXIS )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if LA31_0 == AXIS:
                        alt31 = 1
                    if alt31 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:48:15: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr561)

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr564)

                    self._state.following.append(self.FOLLOW_test_in_core_attr566)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:49:7: CAM_TRANSLATE TO test
                    self.match(
                        self.input,
                        CAM_TRANSLATE,
                        self.FOLLOW_CAM_TRANSLATE_in_core_attr574,
                    )

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr576)

                    self._state.following.append(self.FOLLOW_test_in_core_attr578)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:7: ROTATE ( AXIS )? test ( ORDER )?
                    self.match(self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr586)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:14: ( AXIS )?
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if LA32_0 == AXIS:
                        alt32 = 1
                    if alt32 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:14: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr588)

                    self._state.following.append(self.FOLLOW_test_in_core_attr591)
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:25: ( ORDER )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if LA33_0 == ORDER:
                        alt33 = 1
                    if alt33 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:25: ORDER
                        self.match(self.input, ORDER, self.FOLLOW_ORDER_in_core_attr593)

                elif alt34 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:51:7: SCALE test
                    self.match(self.input, SCALE, self.FOLLOW_SCALE_in_core_attr602)

                    self._state.following.append(self.FOLLOW_test_in_core_attr604)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:7: LOOK_AT test
                    self.match(self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr612)

                    self._state.following.append(self.FOLLOW_test_in_core_attr614)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:7: UP_AXIS test
                    self.match(self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr622)

                    self._state.following.append(self.FOLLOW_test_in_core_attr624)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:54:7: SIZE test
                    self.match(self.input, SIZE, self.FOLLOW_SIZE_in_core_attr632)

                    self._state.following.append(self.FOLLOW_test_in_core_attr634)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:55:7: SEMANTICS test
                    self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr642
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr644)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:56:7: VISIBLE test
                    self.match(self.input, VISIBLE, self.FOLLOW_VISIBLE_in_core_attr652)

                    self._state.following.append(self.FOLLOW_test_in_core_attr654)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_core_attr660)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "core_attr"

    # $ANTLR start "inner_behavior_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:1: inner_behavior_stmt : behavior_expr inner_behavior_block ;
    def inner_behavior_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:22: ( behavior_expr inner_behavior_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:60:24: behavior_expr inner_behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_inner_behavior_stmt670
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_inner_behavior_block_in_inner_behavior_stmt672
                )
                self.inner_behavior_block()

                self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "inner_behavior_stmt"

    # $ANTLR start "inner_behavior_block"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:1: inner_behavior_block : COLON NEWLINE INDENT ( attr )+ DEDENT ;
    def inner_behavior_block(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:22: ( COLON NEWLINE INDENT ( attr )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:24: COLON NEWLINE INDENT ( attr )+ DEDENT
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block679
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block681
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block683
                )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:45: ( attr )+
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:45: attr
                        self._state.following.append(
                            self.FOLLOW_attr_in_inner_behavior_block685
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
                    self.input, DEDENT, self.FOLLOW_DEDENT_in_inner_behavior_block688
                )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "inner_behavior_block"

    # $ANTLR start "behavior_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:64:1: behavior_stmt : behavior_expr behavior_block ;
    def behavior_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:64:16: ( behavior_expr behavior_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:64:18: behavior_expr behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_behavior_stmt699
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_behavior_block_in_behavior_stmt701
                )
                self.behavior_block()

                self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "behavior_stmt"

    # $ANTLR start "behavior_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:1: behavior_expr : EVERY ( test )? ( FRAMES | TIME ) ;
    def behavior_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:16: ( EVERY ( test )? ( FRAMES | TIME ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:18: EVERY ( test )? ( FRAMES | TIME )
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr709)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:24: ( test )?
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:65:24: test
                    self._state.following.append(self.FOLLOW_test_in_behavior_expr711)
                    self.test()

                    self._state.following.pop()

                if self.input.LA(1) in {FRAMES, TIME}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "behavior_expr"

    # $ANTLR start "behavior_block"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:1: behavior_block : COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT ;
    def behavior_block(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:16: ( COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:18: COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block727)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block729
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block731)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:39: ( aug_expr_stmt | edit_stmt )+
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:40: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block734
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt37 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:56: edit_stmt
                        self._state.following.append(
                            self.FOLLOW_edit_stmt_in_behavior_block738
                        )
                        self.edit_stmt()

                        self._state.following.pop()

                    else:
                        if cnt37 >= 1:
                            break  # loop37

                        eee = EarlyExitException(37, self.input)
                        raise eee

                    cnt37 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_behavior_block742)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "behavior_block"

    # $ANTLR start "expr_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:1: expr_stmt : testlist ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) NEWLINE ;
    def expr_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:11: ( testlist ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:13: testlist ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt752)
                self.testlist()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:22: ( aug_assign | ASSIGN )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:23: aug_assign
                    self._state.following.append(self.FOLLOW_aug_assign_in_expr_stmt755)
                    self.aug_assign()

                    self._state.following.pop()

                elif alt38 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:36: ASSIGN
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr_stmt759)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:44: ( testlist | fetch_expr )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:45: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt763)
                    self.testlist()

                    self._state.following.pop()

                elif alt39 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:69:56: fetch_expr
                    self._state.following.append(self.FOLLOW_fetch_expr_in_expr_stmt767)
                    self.fetch_expr()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expr_stmt770)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "expr_stmt"

    # $ANTLR start "aug_expr_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:71:1: aug_expr_stmt : ( ( testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr );
    def aug_expr_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:71:14: ( ( testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:71:16: ( testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:71:16: ( testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:5: testlist ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt783
                    )
                    self.testlist()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:14: ( aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:7: aug_assign ( testlist | fetch_expr )? NEWLINE
                        self._state.following.append(
                            self.FOLLOW_aug_assign_in_aug_expr_stmt793
                        )
                        self.aug_assign()

                        self._state.following.pop()

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:18: ( testlist | fetch_expr )?
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:19: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt796
                            )
                            self.testlist()

                            self._state.following.pop()

                        elif alt40 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:30: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt800
                            )
                            self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_aug_expr_stmt804
                        )

                    elif alt43 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:9: ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt814
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:16: ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:9: ( testlist | fetch_expr ) NEWLINE
                            pass
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:9: ( testlist | fetch_expr )
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
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:10: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt827
                                )
                                self.testlist()

                                self._state.following.pop()

                            elif alt41 == 2:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:21: fetch_expr
                                self._state.following.append(
                                    self.FOLLOW_fetch_expr_in_aug_expr_stmt831
                                )
                                self.fetch_expr()

                                self._state.following.pop()

                            self.match(
                                self.input,
                                NEWLINE,
                                self.FOLLOW_NEWLINE_in_aug_expr_stmt834,
                            )

                        elif alt42 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:11: create_expr
                            self._state.following.append(
                                self.FOLLOW_create_expr_in_aug_expr_stmt846
                            )
                            self.create_expr()

                            self._state.following.pop()

                        elif alt42 == 3:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:25: instantiate_expr
                            self._state.following.append(
                                self.FOLLOW_instantiate_expr_in_aug_expr_stmt850
                            )
                            self.instantiate_expr()

                            self._state.following.pop()

                        elif alt42 == 4:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:44: get_expr
                            self._state.following.append(
                                self.FOLLOW_get_expr_in_aug_expr_stmt854
                            )
                            self.get_expr()

                            self._state.following.pop()

                        elif alt42 == 5:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:55: group_expr
                            self._state.following.append(
                                self.FOLLOW_group_expr_in_aug_expr_stmt858
                            )
                            self.group_expr()

                            self._state.following.pop()

                elif alt44 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:80:5: create_expr
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_aug_expr_stmt882
                    )
                    self.create_expr()

                    self._state.following.pop()

                elif alt44 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:80:19: instantiate_expr
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_aug_expr_stmt886
                    )
                    self.instantiate_expr()

                    self._state.following.pop()

                elif alt44 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:80:38: get_expr
                    self._state.following.append(
                        self.FOLLOW_get_expr_in_aug_expr_stmt890
                    )
                    self.get_expr()

                    self._state.following.pop()

                elif alt44 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:80:49: group_expr
                    self._state.following.append(
                        self.FOLLOW_group_expr_in_aug_expr_stmt894
                    )
                    self.group_expr()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "aug_expr_stmt"

    # $ANTLR start "fetch_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:1: fetch_expr : FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )? ;
    def fetch_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:12: ( FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:14: FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )?
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr903)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr905)
                self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr907)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr909)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:35: ( MATCH test )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 == MATCH:
                    alt45 = 1
                if alt45 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:36: MATCH test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr912)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr914)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:49: ( LIMIT test )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 == LIMIT:
                    alt46 = 1
                if alt46 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:50: LIMIT test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr919)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr921)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:63: ( RECURSIVE )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if LA47_0 == RECURSIVE:
                    alt47 = 1
                if alt47 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:83:63: RECURSIVE
                    self.match(
                        self.input, RECURSIVE, self.FOLLOW_RECURSIVE_in_fetch_expr925
                    )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "fetch_expr"

    # $ANTLR start "aug_assign"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:1: aug_assign : ( ADD_ASSIGN | SUB_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | POWER_ASSIGN | IDIV_ASSIGN );
    def aug_assign(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:11: ( ADD_ASSIGN | SUB_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | POWER_ASSIGN | IDIV_ASSIGN )
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

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "aug_assign"

    # $ANTLR start "test"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:1: test : or_test ( IF or_test ELSE test )? ;
    def test(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:13: ( or_test ( IF or_test ELSE test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:15: or_test ( IF or_test ELSE test )?
                self._state.following.append(self.FOLLOW_or_test_in_test1018)
                self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:23: ( IF or_test ELSE test )?
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if LA48_0 == IF:
                    alt48 = 1
                if alt48 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:24: IF or_test ELSE test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test1021)

                    self._state.following.append(self.FOLLOW_or_test_in_test1023)
                    self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test1025)

                    self._state.following.append(self.FOLLOW_test_in_test1027)
                    self.test()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "test"

    # $ANTLR start "test_nocond"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:1: test_nocond : or_test ;
    def test_nocond(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:13: ( or_test )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond1036)
                self.or_test()

                self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "test_nocond"

    # $ANTLR start "or_test"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:1: or_test : and_test ( OR and_test )* ;
    def or_test(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:13: ( and_test ( OR and_test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:15: and_test ( OR and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test1047)
                self.and_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:24: ( OR and_test )*
                while True:  # loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if LA49_0 == OR:
                        alt49 = 1

                    if alt49 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:25: OR and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test1050)

                        self._state.following.append(
                            self.FOLLOW_and_test_in_or_test1052
                        )
                        self.and_test()

                        self._state.following.pop()

                    else:
                        break  # loop49

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "or_test"

    # $ANTLR start "and_test"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:1: and_test : not_test ( AND not_test )* ;
    def and_test(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:13: ( not_test ( AND not_test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:15: not_test ( AND not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test1064)
                self.not_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:24: ( AND not_test )*
                while True:  # loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if LA50_0 == AND:
                        alt50 = 1

                    if alt50 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:25: AND not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test1067)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test1069
                        )
                        self.not_test()

                        self._state.following.pop()

                    else:
                        break  # loop50

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "and_test"

    # $ANTLR start "not_test"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:1: not_test : ( NOT not_test | comparison );
    def not_test(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:13: ( NOT not_test | comparison )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:15: NOT not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1081)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1083)
                    self.not_test()

                    self._state.following.pop()

                elif alt51 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:30: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test1087)
                    self.comparison()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "not_test"

    # $ANTLR start "comparison"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:1: comparison : expr ( comp_op expr )* ;
    def comparison(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:13: ( expr ( comp_op expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:15: expr ( comp_op expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison1095)
                self.expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:20: ( comp_op expr )*
                while True:  # loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if LA52_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt52 = 1

                    if alt52 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:21: comp_op expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison1098
                        )
                        self.comp_op()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_expr_in_comparison1100)
                        self.expr()

                        self._state.following.pop()

                    else:
                        break  # loop52

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comparison"

    # $ANTLR start "comp_op"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:1: comp_op : ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT );
    def comp_op(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:13: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:15: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_comp_op1113)

                elif alt53 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:20: GT
                    self.match(self.input, GT, self.FOLLOW_GT_in_comp_op1117)

                elif alt53 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:25: EQUALS
                    self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op1121)

                elif alt53 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:34: GT_EQ
                    self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op1125)

                elif alt53 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:42: LT_EQ
                    self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op1129)

                elif alt53 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:50: NOT_EQ
                    self.match(self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op1133)

                elif alt53 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:59: IN
                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1137)

                elif alt53 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:64: NOT IN
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1141)

                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1143)

                elif alt53 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:73: IS
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1147)

                elif alt53 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:78: IS NOT
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1151)

                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1153)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comp_op"

    # $ANTLR start "expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:1: expr : xor_expr ( BIT_OR xor_expr )* ;
    def expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:13: ( xor_expr ( BIT_OR xor_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:15: xor_expr ( BIT_OR xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr1167)
                self.xor_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:24: ( BIT_OR xor_expr )*
                while True:  # loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if LA54_0 == BIT_OR:
                        alt54 = 1

                    if alt54 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:25: BIT_OR xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr1170)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr1172)
                        self.xor_expr()

                        self._state.following.pop()

                    else:
                        break  # loop54

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "expr"

    # $ANTLR start "xor_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:1: xor_expr : and_expr ( XOR and_expr )* ;
    def xor_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:13: ( and_expr ( XOR and_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:15: and_expr ( XOR and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1184)
                self.and_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:24: ( XOR and_expr )*
                while True:  # loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if LA55_0 == XOR:
                        alt55 = 1

                    if alt55 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:25: XOR and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr1187)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr1189
                        )
                        self.and_expr()

                        self._state.following.pop()

                    else:
                        break  # loop55

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "xor_expr"

    # $ANTLR start "and_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:1: and_expr : shift_expr ( BIT_AND shift_expr )* ;
    def and_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:13: ( shift_expr ( BIT_AND shift_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:15: shift_expr ( BIT_AND shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1201)
                self.shift_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:26: ( BIT_AND shift_expr )*
                while True:  # loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if LA56_0 == BIT_AND:
                        alt56 = 1

                    if alt56 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:27: BIT_AND shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr1204
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr1206
                        )
                        self.shift_expr()

                        self._state.following.pop()

                    else:
                        break  # loop56

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "and_expr"

    # $ANTLR start "shift_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:1: shift_expr : arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* ;
    def shift_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:13: ( arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:15: arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1216)
                self.arith_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:26: ( ( LSHIFT | RSHIFT ) arith_expr )*
                while True:  # loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if LA57_0 in {LSHIFT, RSHIFT}:
                        alt57 = 1

                    if alt57 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:27: ( LSHIFT | RSHIFT ) arith_expr
                        if self.input.LA(1) in {LSHIFT, RSHIFT}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr1227
                        )
                        self.arith_expr()

                        self._state.following.pop()

                    else:
                        break  # loop57

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "shift_expr"

    # $ANTLR start "arith_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:1: arith_expr : term ( ( PLUS | MINUS ) term )* ;
    def arith_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:13: ( term ( ( PLUS | MINUS ) term )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:15: term ( ( PLUS | MINUS ) term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr1237)
                self.term()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:20: ( ( PLUS | MINUS ) term )*
                while True:  # loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if LA58_0 in {MINUS, PLUS}:
                        alt58 = 1

                    if alt58 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:21: ( PLUS | MINUS ) term
                        if self.input.LA(1) in {MINUS, PLUS}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_term_in_arith_expr1248)
                        self.term()

                        self._state.following.pop()

                    else:
                        break  # loop58

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "arith_expr"

    # $ANTLR start "term"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:1: term : factor ( ( MUL | DIV | MOD | IDIV ) factor )* ;
    def term(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:13: ( factor ( ( MUL | DIV | MOD | IDIV ) factor )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:15: factor ( ( MUL | DIV | MOD | IDIV ) factor )*
                self._state.following.append(self.FOLLOW_factor_in_term1264)
                self.factor()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:22: ( ( MUL | DIV | MOD | IDIV ) factor )*
                while True:  # loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if LA59_0 in {DIV, IDIV, MOD, MUL}:
                        alt59 = 1

                    if alt59 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:23: ( MUL | DIV | MOD | IDIV ) factor
                        if self.input.LA(1) in {DIV, IDIV, MOD, MUL}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_factor_in_term1283)
                        self.factor()

                        self._state.following.pop()

                    else:
                        break  # loop59

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "term"

    # $ANTLR start "factor"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:1: factor : ( ( PLUS | MINUS | BIT_NOT ) factor | power );
    def factor(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:13: ( ( PLUS | MINUS | BIT_NOT ) factor | power )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:15: ( PLUS | MINUS | BIT_NOT ) factor
                    if self.input.LA(1) in {BIT_NOT, MINUS, PLUS}:
                        self.input.consume()
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse

                    self._state.following.append(self.FOLLOW_factor_in_factor1309)
                    self.factor()

                    self._state.following.pop()

                elif alt60 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:49: power
                    self._state.following.append(self.FOLLOW_power_in_factor1313)
                    self.power()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "factor"

    # $ANTLR start "power"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:1: power : atom_expr ( POWER factor )? ;
    def power(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:13: ( atom_expr ( POWER factor )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power1326)
                self.atom_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:25: ( POWER factor )?
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if LA61_0 == POWER:
                    alt61 = 1
                if alt61 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power1329)

                    self._state.following.append(self.FOLLOW_factor_in_power1331)
                    self.factor()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "power"

    # $ANTLR start "atom_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:1: atom_expr : atom ( trailer )* ;
    def atom_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:13: ( atom ( trailer )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:15: atom ( trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr1342)
                self.atom()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:20: ( trailer )*
                while True:  # loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if LA62_0 in {DOT, LBRACK}:
                        alt62 = 1

                    if alt62 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:23: trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr1347
                        )
                        self.trailer()

                        self._state.following.pop()

                    else:
                        break  # loop62

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "atom_expr"

    # $ANTLR start "atom"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:1: atom : ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE );
    def atom(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:5: ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:3: LPAREN test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1357)

                    self._state.following.append(self.FOLLOW_test_in_atom1359)
                    self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1361)

                elif alt69 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:5: LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom1367)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:12: ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:13: ( testlist_comp )?
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:13: ( testlist_comp )?
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:13: testlist_comp
                            self._state.following.append(
                                self.FOLLOW_testlist_comp_in_atom1370
                            )
                            self.testlist_comp()

                            self._state.following.pop()

                    elif alt66 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:30: ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER )
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:30: ( ( MINUS )? INTEGER )
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:31: ( MINUS )? INTEGER
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:31: ( MINUS )?
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if LA64_0 == MINUS:
                            alt64 = 1
                        if alt64 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:31: MINUS
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1376)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1379)

                        self.match(self.input, RANGE, self.FOLLOW_RANGE_in_atom1382)

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:53: ( ( MINUS )? INTEGER )
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:54: ( MINUS )? INTEGER
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:54: ( MINUS )?
                        alt65 = 2
                        LA65_0 = self.input.LA(1)

                        if LA65_0 == MINUS:
                            alt65 = 1
                        if alt65 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:118:54: MINUS
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1385)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1388)

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom1392)

                elif alt69 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom1398)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:8: ( vector_comp )?
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom1400
                        )
                        self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom1403)

                elif alt69 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom1409)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:12: ( dict_or_set_maker )?
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom1411
                        )
                        self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom1414)

                elif alt69 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom1420)
                    self.name()

                    self._state.following.pop()

                elif alt69 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:12: SETTING_ID
                    self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom1424
                    )

                elif alt69 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:25: distribution_expr
                    self._state.following.append(
                        self.FOLLOW_distribution_expr_in_atom1428
                    )
                    self.distribution_expr()

                    self._state.following.pop()

                elif alt69 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:5: INTEGER
                    self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1434)

                elif alt69 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:15: FLOAT_NUMBER
                    self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom1438
                    )

                elif alt69 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:30: STRING
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_atom1442)

                elif alt69 == 11:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:39: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom1446)

                elif alt69 == 12:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:46: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom1450)

                elif alt69 == 13:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:53: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom1454)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "atom"

    # $ANTLR start "name"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:1: name : ( ID | UNDERSCORE );
    def name(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:5: ( ID | UNDERSCORE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {ID, UNDERSCORE}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "name"

    # $ANTLR start "distribution_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:1: distribution_expr : distribution LPAREN arglist RPAREN ;
    def distribution_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:19: ( distribution LPAREN arglist RPAREN )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:21: distribution LPAREN arglist RPAREN
                self._state.following.append(
                    self.FOLLOW_distribution_in_distribution_expr1483
                )
                self.distribution()

                self._state.following.pop()

                self.match(
                    self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution_expr1485
                )

                self._state.following.append(
                    self.FOLLOW_arglist_in_distribution_expr1487
                )
                self.arglist()

                self._state.following.pop()

                self.match(
                    self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution_expr1489
                )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "distribution_expr"

    # $ANTLR start "distribution"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:1: distribution : ( UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM );
    def distribution(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:19: ( UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                if self.input.LA(1) in {CHOICE, LOG_UNIFORM, NORMAL, SEQUENCE, UNIFORM}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "distribution"

    # $ANTLR start "testlist_comp"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:1: testlist_comp : test ( comp_for | ( COMMA test )* ) ;
    def testlist_comp(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:15: ( test ( comp_for | ( COMMA test )* ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:17: test ( comp_for | ( COMMA test )* )
                self._state.following.append(self.FOLLOW_test_in_testlist_comp1525)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:22: ( comp_for | ( COMMA test )* )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:24: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp1529
                    )
                    self.comp_for()

                    self._state.following.pop()

                elif alt71 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:35: ( COMMA test )*
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:35: ( COMMA test )*
                    while True:  # loop70
                        alt70 = 2
                        LA70_0 = self.input.LA(1)

                        if LA70_0 == COMMA:
                            alt70 = 1

                        if alt70 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:36: COMMA test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp1534,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp1536
                            )
                            self.test()

                            self._state.following.pop()

                        else:
                            break  # loop70

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "testlist_comp"

    # $ANTLR start "vector_comp"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:1: vector_comp : expr COMMA expr COMMA expr ;
    def vector_comp(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:15: ( expr COMMA expr COMMA expr )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:17: expr COMMA expr COMMA expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp1548)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1550)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1552)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1554)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1556)
                self.expr()

                self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "vector_comp"

    # $ANTLR start "trailer"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:144:1: trailer : ( LBRACK subscriptlist RBRACK | DOT name );
    def trailer(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:144:15: ( LBRACK subscriptlist RBRACK | DOT name )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:144:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer1572)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer1574
                    )
                    self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer1576)

                elif alt72 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:144:47: DOT name
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer1580)

                    self._state.following.append(self.FOLLOW_name_in_trailer1582)
                    self.name()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "trailer"

    # $ANTLR start "arglist"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:1: arglist : argument ( COMMA argument )* ;
    def arglist(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:15: ( argument ( COMMA argument )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:17: argument ( COMMA argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist1595)
                self.argument()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:26: ( COMMA argument )*
                while True:  # loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if LA73_0 == COMMA:
                        alt73 = 1

                    if alt73 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:27: COMMA argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist1598)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist1600
                        )
                        self.argument()

                        self._state.following.pop()

                    else:
                        break  # loop73

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "arglist"

    # $ANTLR start "argument"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:1: argument : test ( comp_for | ASSIGN test )? ;
    def argument(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:15: ( test ( comp_for | ASSIGN test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:17: test ( comp_for | ASSIGN test )?
                self._state.following.append(self.FOLLOW_test_in_argument1614)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:22: ( comp_for | ASSIGN test )?
                alt74 = 3
                LA74_0 = self.input.LA(1)

                if LA74_0 == FOR:
                    alt74 = 1
                elif LA74_0 == ASSIGN:
                    alt74 = 2
                if alt74 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:23: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_argument1617)
                    self.comp_for()

                    self._state.following.pop()

                elif alt74 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:34: ASSIGN test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument1621)

                    self._state.following.append(self.FOLLOW_test_in_argument1623)
                    self.test()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "argument"

    # $ANTLR start "subscriptlist"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:1: subscriptlist : subscript_ ( COMMA subscript_ )* ;
    def subscriptlist(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:15: ( subscript_ ( COMMA subscript_ )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:17: subscript_ ( COMMA subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist1632
                )
                self.subscript_()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:28: ( COMMA subscript_ )*
                while True:  # loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if LA75_0 == COMMA:
                        alt75 = 1

                    if alt75 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:29: COMMA subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist1635
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist1637
                        )
                        self.subscript_()

                        self._state.following.pop()

                    else:
                        break  # loop75

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "subscriptlist"

    # $ANTLR start "subscript_"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:1: subscript_ : ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? );
    def subscript_(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:15: ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:17: test ( COLON ( test )? ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_1649)
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:22: ( COLON ( test )? ( sliceop )? )?
                    alt78 = 2
                    LA78_0 = self.input.LA(1)

                    if LA78_0 == COLON:
                        alt78 = 1
                    if alt78 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:23: COLON ( test )? ( sliceop )?
                        self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_1652
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:29: ( test )?
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:30: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_1655
                            )
                            self.test()

                            self._state.following.pop()

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:37: ( sliceop )?
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if LA77_0 == COLON:
                            alt77 = 1
                        if alt77 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:38: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_1660
                            )
                            self.sliceop()

                            self._state.following.pop()

                elif alt81 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:52: COLON ( test )? ( sliceop )?
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript_1668)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:58: ( test )?
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:59: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_1671)
                        self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:66: ( sliceop )?
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if LA80_0 == COLON:
                        alt80 = 1
                    if alt80 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:148:67: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_1676
                        )
                        self.sliceop()

                        self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "subscript_"

    # $ANTLR start "sliceop"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:1: sliceop : COLON ( test )? ;
    def sliceop(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:15: ( COLON ( test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop1691)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:23: ( test )?
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop1693)
                    self.test()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "sliceop"

    # $ANTLR start "exprlist"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:1: exprlist : expr ( COMMA expr )* ;
    def exprlist(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:10: ( expr ( COMMA expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:12: expr ( COMMA expr )*
                self._state.following.append(self.FOLLOW_expr_in_exprlist1702)
                self.expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:17: ( COMMA expr )*
                while True:  # loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if LA83_0 == COMMA:
                        alt83 = 1

                    if alt83 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:18: COMMA expr
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist1705)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist1707)
                        self.expr()

                        self._state.following.pop()

                    else:
                        break  # loop83

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "exprlist"

    # $ANTLR start "testlist"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:1: testlist : test ( COMMA test )* ;
    def testlist(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:10: ( test ( COMMA test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:12: test ( COMMA test )*
                self._state.following.append(self.FOLLOW_test_in_testlist1716)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:17: ( COMMA test )*
                while True:  # loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if LA84_0 == COMMA:
                        alt84 = 1

                    if alt84 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:18: COMMA test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist1719)

                        self._state.following.append(self.FOLLOW_test_in_testlist1721)
                        self.test()

                        self._state.following.pop()

                    else:
                        break  # loop84

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "testlist"

    # $ANTLR start "dict_or_set_maker"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:1: dict_or_set_maker : test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) ;
    def dict_or_set_maker(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:18: ( test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:3: test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker1731)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:8: ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:10: COLON test ( comp_for | ( COMMA test COLON test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker1735
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker1737
                    )
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:21: ( comp_for | ( COMMA test COLON test )* )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:22: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1740
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt86 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:33: ( COMMA test COLON test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:33: ( COMMA test COLON test )*
                        while True:  # loop85
                            alt85 = 2
                            LA85_0 = self.input.LA(1)

                            if LA85_0 == COMMA:
                                alt85 = 1

                            if alt85 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:34: COMMA test COLON test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker1745,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1747
                                )
                                self.test()

                                self._state.following.pop()

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker1749,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1751
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop85

                elif alt89 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:10: ( comp_for | ( COMMA test )* )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:10: ( comp_for | ( COMMA test )* )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:11: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1766
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt88 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:22: ( COMMA test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:22: ( COMMA test )*
                        while True:  # loop87
                            alt87 = 2
                            LA87_0 = self.input.LA(1)

                            if LA87_0 == COMMA:
                                alt87 = 1

                            if alt87 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:155:23: COMMA test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker1771,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1773
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop87

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "dict_or_set_maker"

    # $ANTLR start "comp_iter"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:158:1: comp_iter : ( comp_for | comp_if );
    def comp_iter(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:158:11: ( comp_for | comp_if )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:158:13: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter1787)
                    self.comp_for()

                    self._state.following.pop()

                elif alt90 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:158:24: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter1791)
                    self.comp_if()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comp_iter"

    # $ANTLR start "comp_for"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:1: comp_for : FOR exprlist IN or_test ( comp_iter )? ;
    def comp_for(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:11: ( FOR exprlist IN or_test ( comp_iter )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:13: FOR exprlist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for1799)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for1801)
                self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for1803)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for1805)
                self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:37: ( comp_iter )?
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if LA91_0 in {FOR, IF}:
                    alt91 = 1
                if alt91 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:37: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for1807)
                    self.comp_iter()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comp_for"

    # $ANTLR start "comp_if"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:1: comp_if : IF test_nocond ( comp_iter )? ;
    def comp_if(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:11: ( IF test_nocond ( comp_iter )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if1817)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if1819)
                self.test_nocond()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:28: ( comp_iter )?
                alt92 = 2
                LA92_0 = self.input.LA(1)

                if LA92_0 in {FOR, IF}:
                    alt92 = 1
                if alt92 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if1821)
                    self.comp_iter()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comp_if"

    FOLLOW_declaration_in_scenario35 = frozenset([1, 79, 111, 120, 135])
    FOLLOW_NEWLINE_in_scenario37 = frozenset([1, 79, 111, 120, 135])
    FOLLOW_settings_in_scenario40 = frozenset([1, 120, 135])
    FOLLOW_stage_in_scenario43 = frozenset([1, 135])
    FOLLOW_writers_in_scenario46 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration56 = frozenset([45, 130])
    FOLLOW_name_in_declaration58 = frozenset([17, 79])
    FOLLOW_COLON_in_declaration61 = frozenset([45, 130])
    FOLLOW_name_in_declaration63 = frozenset([79])
    FOLLOW_NEWLINE_in_declaration67 = frozenset([1])
    FOLLOW_SETTINGS_in_settings77 = frozenset([17])
    FOLLOW_COLON_in_settings79 = frozenset([79])
    FOLLOW_NEWLINE_in_settings81 = frozenset([52])
    FOLLOW_INDENT_in_settings83 = frozenset([45])
    FOLLOW_option_in_settings85 = frozenset([21, 45])
    FOLLOW_DEDENT_in_settings88 = frozenset([1])
    FOLLOW_STAGE_in_stage101 = frozenset([17])
    FOLLOW_COLON_in_stage103 = frozenset([79])
    FOLLOW_NEWLINE_in_stage105 = frozenset([52])
    FOLLOW_INDENT_in_stage107 = frozenset(
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
    FOLLOW_stmts_in_stage109 = frozenset([21])
    FOLLOW_DEDENT_in_stage111 = frozenset([1])
    FOLLOW_WRITERS_in_writers122 = frozenset([17])
    FOLLOW_COLON_in_writers124 = frozenset([79])
    FOLLOW_NEWLINE_in_writers126 = frozenset([52])
    FOLLOW_INDENT_in_writers128 = frozenset(
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
    FOLLOW_expr_stmt_in_writers131 = frozenset(
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
    FOLLOW_writer_in_writers135 = frozenset(
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
    FOLLOW_DEDENT_in_writers139 = frozenset([1])
    FOLLOW_ID_in_option147 = frozenset([7])
    FOLLOW_ASSIGN_in_option149 = frozenset(
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
    FOLLOW_test_in_option151 = frozenset([79])
    FOLLOW_NEWLINE_in_option153 = frozenset([1])
    FOLLOW_open_stmt_in_stmts161 = frozenset(
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
    FOLLOW_aug_expr_stmt_in_stmts165 = frozenset(
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
    FOLLOW_edit_stmt_in_stmts169 = frozenset(
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
    FOLLOW_behavior_stmt_in_stmts173 = frozenset(
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
    FOLLOW_ID_in_writer182 = frozenset([17])
    FOLLOW_COLON_in_writer184 = frozenset([79])
    FOLLOW_NEWLINE_in_writer186 = frozenset([52])
    FOLLOW_INDENT_in_writer188 = frozenset([45])
    FOLLOW_option_in_writer190 = frozenset([21, 45])
    FOLLOW_DEDENT_in_writer193 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt205 = frozenset(
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
    FOLLOW_test_in_open_stmt207 = frozenset([79])
    FOLLOW_NEWLINE_in_open_stmt209 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt216 = frozenset([45, 126, 130])
    FOLLOW_TIMELINE_in_edit_stmt219 = frozenset([17])
    FOLLOW_name_in_edit_stmt223 = frozenset([17])
    FOLLOW_edit_block_in_edit_stmt226 = frozenset([1])
    FOLLOW_CREATE_in_create_expr235 = frozenset(
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
    FOLLOW_test_in_create_expr237 = frozenset([14, 39, 61, 72, 113, 114, 121])
    FOLLOW_STEREO_in_create_expr247 = frozenset([14])
    FOLLOW_CAMERA_in_create_expr250 = frozenset([17, 79])
    FOLLOW_shapes_in_create_expr254 = frozenset([17, 79])
    FOLLOW_light_type_in_create_expr258 = frozenset([60])
    FOLLOW_LIGHT_in_create_expr260 = frozenset([17, 79])
    FOLLOW_FROM_in_create_expr264 = frozenset(
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
    FOLLOW_test_in_create_expr266 = frozenset([17, 79])
    FOLLOW_edit_block_in_create_expr270 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr274 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr283 = frozenset([17])
    FOLLOW_simple_block_in_create_expr286 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr327 = frozenset(
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
    FOLLOW_test_in_instantiate_expr330 = frozenset([39])
    FOLLOW_FROM_in_instantiate_expr334 = frozenset(
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
    FOLLOW_test_in_instantiate_expr336 = frozenset([17, 79])
    FOLLOW_edit_block_in_instantiate_expr339 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr343 = frozenset([1])
    FOLLOW_GROUP_in_group_expr357 = frozenset([58])
    FOLLOW_LBRACK_in_group_expr359 = frozenset([45, 130])
    FOLLOW_name_in_group_expr361 = frozenset([18, 98])
    FOLLOW_COMMA_in_group_expr364 = frozenset([45, 130])
    FOLLOW_name_in_group_expr366 = frozenset([18, 98])
    FOLLOW_RBRACK_in_group_expr370 = frozenset([17, 79])
    FOLLOW_edit_block_in_group_expr373 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr377 = frozenset([1])
    FOLLOW_GET_in_get_expr393 = frozenset(
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
    FOLLOW_CAMERA_in_get_expr397 = frozenset([8])
    FOLLOW_LIGHT_in_get_expr401 = frozenset([8])
    FOLLOW_MATERIAL_in_get_expr405 = frozenset([8])
    FOLLOW_name_in_get_expr409 = frozenset([8])
    FOLLOW_AT_in_get_expr412 = frozenset(
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
    FOLLOW_test_in_get_expr416 = frozenset([17, 79])
    FOLLOW_simple_block_in_get_expr419 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr423 = frozenset([1])
    FOLLOW_COLON_in_edit_block434 = frozenset([79])
    FOLLOW_NEWLINE_in_edit_block436 = frozenset([52])
    FOLLOW_INDENT_in_edit_block438 = frozenset(
        [15, 30, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_attr_in_edit_block441 = frozenset(
        [15, 21, 30, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block445 = frozenset(
        [15, 21, 30, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_DEDENT_in_edit_block449 = frozenset([1])
    FOLLOW_COLON_in_simple_block456 = frozenset([79])
    FOLLOW_NEWLINE_in_simple_block458 = frozenset([52])
    FOLLOW_INDENT_in_simple_block460 = frozenset([45, 130])
    FOLLOW_simple_attr_in_simple_block462 = frozenset([21, 45, 130])
    FOLLOW_DEDENT_in_simple_block465 = frozenset([1])
    FOLLOW_core_attr_in_attr482 = frozenset([1])
    FOLLOW_simple_attr_in_attr486 = frozenset([1])
    FOLLOW_compound_attr_in_attr490 = frozenset([1])
    FOLLOW_name_in_simple_attr499 = frozenset(
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
    FOLLOW_COLON_in_simple_attr502 = frozenset([45, 130])
    FOLLOW_name_in_simple_attr504 = frozenset(
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
    FOLLOW_test_in_simple_attr508 = frozenset([79])
    FOLLOW_NEWLINE_in_simple_attr511 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr520 = frozenset([86])
    FOLLOW_ON_in_compound_attr522 = frozenset([45, 130])
    FOLLOW_name_in_compound_attr524 = frozenset([17, 79])
    FOLLOW_ROT_AROUND_in_compound_attr528 = frozenset([45, 130])
    FOLLOW_name_in_compound_attr530 = frozenset([17, 79])
    FOLLOW_PHYSICS_in_compound_attr534 = frozenset([17, 79])
    FOLLOW_simple_block_in_compound_attr538 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr542 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr559 = frozenset([9, 127])
    FOLLOW_AXIS_in_core_attr561 = frozenset([127])
    FOLLOW_TO_in_core_attr564 = frozenset(
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
    FOLLOW_test_in_core_attr566 = frozenset([79])
    FOLLOW_CAM_TRANSLATE_in_core_attr574 = frozenset([127])
    FOLLOW_TO_in_core_attr576 = frozenset(
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
    FOLLOW_test_in_core_attr578 = frozenset([79])
    FOLLOW_ROTATE_in_core_attr586 = frozenset(
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
    FOLLOW_AXIS_in_core_attr588 = frozenset(
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
    FOLLOW_test_in_core_attr591 = frozenset([79, 89])
    FOLLOW_ORDER_in_core_attr593 = frozenset([79])
    FOLLOW_SCALE_in_core_attr602 = frozenset(
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
    FOLLOW_test_in_core_attr604 = frozenset([79])
    FOLLOW_LOOK_AT_in_core_attr612 = frozenset(
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
    FOLLOW_test_in_core_attr614 = frozenset([79])
    FOLLOW_UP_AXIS_in_core_attr622 = frozenset(
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
    FOLLOW_test_in_core_attr624 = frozenset([79])
    FOLLOW_SIZE_in_core_attr632 = frozenset(
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
    FOLLOW_test_in_core_attr634 = frozenset([79])
    FOLLOW_SEMANTICS_in_core_attr642 = frozenset(
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
    FOLLOW_test_in_core_attr644 = frozenset([79])
    FOLLOW_VISIBLE_in_core_attr652 = frozenset(
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
    FOLLOW_test_in_core_attr654 = frozenset([79])
    FOLLOW_NEWLINE_in_core_attr660 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt670 = frozenset([17])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt672 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block679 = frozenset([79])
    FOLLOW_NEWLINE_in_inner_behavior_block681 = frozenset([52])
    FOLLOW_INDENT_in_inner_behavior_block683 = frozenset(
        [15, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_attr_in_inner_behavior_block685 = frozenset(
        [15, 21, 45, 65, 91, 100, 101, 105, 106, 108, 116, 128, 130, 133, 134]
    )
    FOLLOW_DEDENT_in_inner_behavior_block688 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt699 = frozenset([17])
    FOLLOW_behavior_block_in_behavior_stmt701 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr709 = frozenset(
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
    FOLLOW_test_in_behavior_expr711 = frozenset([38, 125])
    FOLLOW_set_in_behavior_expr714 = frozenset([1])
    FOLLOW_COLON_in_behavior_block727 = frozenset([79])
    FOLLOW_NEWLINE_in_behavior_block729 = frozenset([52])
    FOLLOW_INDENT_in_behavior_block731 = frozenset(
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
    FOLLOW_aug_expr_stmt_in_behavior_block734 = frozenset(
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
    FOLLOW_edit_stmt_in_behavior_block738 = frozenset(
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
    FOLLOW_DEDENT_in_behavior_block742 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt752 = frozenset(
        [4, 6, 7, 24, 47, 68, 75, 77, 90, 95, 104, 124, 137]
    )
    FOLLOW_aug_assign_in_expr_stmt755 = frozenset(
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
    FOLLOW_ASSIGN_in_expr_stmt759 = frozenset(
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
    FOLLOW_testlist_in_expr_stmt763 = frozenset([79])
    FOLLOW_fetch_expr_in_expr_stmt767 = frozenset([79])
    FOLLOW_NEWLINE_in_expr_stmt770 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt783 = frozenset(
        [4, 6, 7, 24, 47, 68, 75, 77, 90, 95, 104, 124, 137]
    )
    FOLLOW_aug_assign_in_aug_expr_stmt793 = frozenset(
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
    FOLLOW_testlist_in_aug_expr_stmt796 = frozenset([79])
    FOLLOW_fetch_expr_in_aug_expr_stmt800 = frozenset([79])
    FOLLOW_NEWLINE_in_aug_expr_stmt804 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt814 = frozenset(
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
    FOLLOW_testlist_in_aug_expr_stmt827 = frozenset([79])
    FOLLOW_fetch_expr_in_aug_expr_stmt831 = frozenset([79])
    FOLLOW_NEWLINE_in_aug_expr_stmt834 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt846 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt850 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt854 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt858 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt882 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt886 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt890 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt894 = frozenset([1])
    FOLLOW_FETCH_in_fetch_expr903 = frozenset(
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
    FOLLOW_test_in_fetch_expr905 = frozenset([39])
    FOLLOW_FROM_in_fetch_expr907 = frozenset(
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
    FOLLOW_test_in_fetch_expr909 = frozenset([1, 62, 71, 99])
    FOLLOW_MATCH_in_fetch_expr912 = frozenset(
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
    FOLLOW_test_in_fetch_expr914 = frozenset([1, 62, 99])
    FOLLOW_LIMIT_in_fetch_expr919 = frozenset(
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
    FOLLOW_test_in_fetch_expr921 = frozenset([1, 99])
    FOLLOW_RECURSIVE_in_fetch_expr925 = frozenset([1])
    FOLLOW_or_test_in_test1018 = frozenset([1, 50])
    FOLLOW_IF_in_test1021 = frozenset(
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
    FOLLOW_or_test_in_test1023 = frozenset([28])
    FOLLOW_ELSE_in_test1025 = frozenset(
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
    FOLLOW_test_in_test1027 = frozenset([1])
    FOLLOW_or_test_in_test_nocond1036 = frozenset([1])
    FOLLOW_and_test_in_or_test1047 = frozenset([1, 88])
    FOLLOW_OR_in_or_test1050 = frozenset(
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
    FOLLOW_and_test_in_or_test1052 = frozenset([1, 88])
    FOLLOW_not_test_in_and_test1064 = frozenset([1, 5])
    FOLLOW_AND_in_and_test1067 = frozenset(
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
    FOLLOW_not_test_in_and_test1069 = frozenset([1, 5])
    FOLLOW_NOT_in_not_test1081 = frozenset(
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
    FOLLOW_not_test_in_not_test1083 = frozenset([1])
    FOLLOW_comparison_in_not_test1087 = frozenset([1])
    FOLLOW_expr_in_comparison1095 = frozenset([1, 29, 42, 43, 51, 56, 69, 70, 83, 84])
    FOLLOW_comp_op_in_comparison1098 = frozenset(
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
    FOLLOW_expr_in_comparison1100 = frozenset([1, 29, 42, 43, 51, 56, 69, 70, 83, 84])
    FOLLOW_LT_in_comp_op1113 = frozenset([1])
    FOLLOW_GT_in_comp_op1117 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op1121 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op1125 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op1129 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op1133 = frozenset([1])
    FOLLOW_IN_in_comp_op1137 = frozenset([1])
    FOLLOW_NOT_in_comp_op1141 = frozenset([51])
    FOLLOW_IN_in_comp_op1143 = frozenset([1])
    FOLLOW_IS_in_comp_op1147 = frozenset([1])
    FOLLOW_IS_in_comp_op1151 = frozenset([83])
    FOLLOW_NOT_in_comp_op1153 = frozenset([1])
    FOLLOW_xor_expr_in_expr1167 = frozenset([1, 13])
    FOLLOW_BIT_OR_in_expr1170 = frozenset(
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
    FOLLOW_xor_expr_in_expr1172 = frozenset([1, 13])
    FOLLOW_and_expr_in_xor_expr1184 = frozenset([1, 136])
    FOLLOW_XOR_in_xor_expr1187 = frozenset(
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
    FOLLOW_and_expr_in_xor_expr1189 = frozenset([1, 136])
    FOLLOW_shift_expr_in_and_expr1201 = frozenset([1, 11])
    FOLLOW_BIT_AND_in_and_expr1204 = frozenset(
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
    FOLLOW_shift_expr_in_and_expr1206 = frozenset([1, 11])
    FOLLOW_arith_expr_in_shift_expr1216 = frozenset([1, 67, 103])
    FOLLOW_set_in_shift_expr1219 = frozenset(
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
    FOLLOW_arith_expr_in_shift_expr1227 = frozenset([1, 67, 103])
    FOLLOW_term_in_arith_expr1237 = frozenset([1, 73, 92])
    FOLLOW_set_in_arith_expr1240 = frozenset(
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
    FOLLOW_term_in_arith_expr1248 = frozenset([1, 73, 92])
    FOLLOW_factor_in_term1264 = frozenset([1, 23, 46, 74, 76])
    FOLLOW_set_in_term1267 = frozenset(
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
    FOLLOW_factor_in_term1283 = frozenset([1, 23, 46, 74, 76])
    FOLLOW_set_in_factor1297 = frozenset(
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
    FOLLOW_factor_in_factor1309 = frozenset([1])
    FOLLOW_power_in_factor1313 = frozenset([1])
    FOLLOW_atom_expr_in_power1326 = frozenset([1, 94])
    FOLLOW_POWER_in_power1329 = frozenset(
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
    FOLLOW_factor_in_power1331 = frozenset([1])
    FOLLOW_atom_in_atom_expr1342 = frozenset([1, 25, 58])
    FOLLOW_trailer_in_atom_expr1347 = frozenset([1, 25, 58])
    FOLLOW_LPAREN_in_atom1357 = frozenset(
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
    FOLLOW_test_in_atom1359 = frozenset([102])
    FOLLOW_RPAREN_in_atom1361 = frozenset([1])
    FOLLOW_LBRACK_in_atom1367 = frozenset(
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
    FOLLOW_testlist_comp_in_atom1370 = frozenset([98])
    FOLLOW_MINUS_in_atom1376 = frozenset([54])
    FOLLOW_INTEGER_in_atom1379 = frozenset([96])
    FOLLOW_RANGE_in_atom1382 = frozenset([54, 73])
    FOLLOW_MINUS_in_atom1385 = frozenset([54])
    FOLLOW_INTEGER_in_atom1388 = frozenset([98])
    FOLLOW_RBRACK_in_atom1392 = frozenset([1])
    FOLLOW_LT_in_atom1398 = frozenset(
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
    FOLLOW_vector_comp_in_atom1400 = frozenset([42])
    FOLLOW_GT_in_atom1403 = frozenset([1])
    FOLLOW_LBRACE_in_atom1409 = frozenset(
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
    FOLLOW_dict_or_set_maker_in_atom1411 = frozenset([97])
    FOLLOW_RBRACE_in_atom1414 = frozenset([1])
    FOLLOW_name_in_atom1420 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom1424 = frozenset([1])
    FOLLOW_distribution_expr_in_atom1428 = frozenset([1])
    FOLLOW_INTEGER_in_atom1434 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom1438 = frozenset([1])
    FOLLOW_STRING_in_atom1442 = frozenset([1])
    FOLLOW_NONE_in_atom1446 = frozenset([1])
    FOLLOW_TRUE_in_atom1450 = frozenset([1])
    FOLLOW_FALSE_in_atom1454 = frozenset([1])
    FOLLOW_distribution_in_distribution_expr1483 = frozenset([66])
    FOLLOW_LPAREN_in_distribution_expr1485 = frozenset(
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
    FOLLOW_arglist_in_distribution_expr1487 = frozenset([102])
    FOLLOW_RPAREN_in_distribution_expr1489 = frozenset([1])
    FOLLOW_test_in_testlist_comp1525 = frozenset([1, 18, 36])
    FOLLOW_comp_for_in_testlist_comp1529 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp1534 = frozenset(
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
    FOLLOW_test_in_testlist_comp1536 = frozenset([1, 18])
    FOLLOW_expr_in_vector_comp1548 = frozenset([18])
    FOLLOW_COMMA_in_vector_comp1550 = frozenset(
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
    FOLLOW_expr_in_vector_comp1552 = frozenset([18])
    FOLLOW_COMMA_in_vector_comp1554 = frozenset(
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
    FOLLOW_expr_in_vector_comp1556 = frozenset([1])
    FOLLOW_LBRACK_in_trailer1572 = frozenset(
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
    FOLLOW_subscriptlist_in_trailer1574 = frozenset([98])
    FOLLOW_RBRACK_in_trailer1576 = frozenset([1])
    FOLLOW_DOT_in_trailer1580 = frozenset([45, 130])
    FOLLOW_name_in_trailer1582 = frozenset([1])
    FOLLOW_argument_in_arglist1595 = frozenset([1, 18])
    FOLLOW_COMMA_in_arglist1598 = frozenset(
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
    FOLLOW_argument_in_arglist1600 = frozenset([1, 18])
    FOLLOW_test_in_argument1614 = frozenset([1, 7, 36])
    FOLLOW_comp_for_in_argument1617 = frozenset([1])
    FOLLOW_ASSIGN_in_argument1621 = frozenset(
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
    FOLLOW_test_in_argument1623 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist1632 = frozenset([1, 18])
    FOLLOW_COMMA_in_subscriptlist1635 = frozenset(
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
    FOLLOW_subscript__in_subscriptlist1637 = frozenset([1, 18])
    FOLLOW_test_in_subscript_1649 = frozenset([1, 17])
    FOLLOW_COLON_in_subscript_1652 = frozenset(
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
    FOLLOW_test_in_subscript_1655 = frozenset([1, 17])
    FOLLOW_sliceop_in_subscript_1660 = frozenset([1])
    FOLLOW_COLON_in_subscript_1668 = frozenset(
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
    FOLLOW_test_in_subscript_1671 = frozenset([1, 17])
    FOLLOW_sliceop_in_subscript_1676 = frozenset([1])
    FOLLOW_COLON_in_sliceop1691 = frozenset(
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
    FOLLOW_test_in_sliceop1693 = frozenset([1])
    FOLLOW_expr_in_exprlist1702 = frozenset([1, 18])
    FOLLOW_COMMA_in_exprlist1705 = frozenset(
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
    FOLLOW_expr_in_exprlist1707 = frozenset([1, 18])
    FOLLOW_test_in_testlist1716 = frozenset([1, 18])
    FOLLOW_COMMA_in_testlist1719 = frozenset(
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
    FOLLOW_test_in_testlist1721 = frozenset([1, 18])
    FOLLOW_test_in_dict_or_set_maker1731 = frozenset([1, 17, 18, 36])
    FOLLOW_COLON_in_dict_or_set_maker1735 = frozenset(
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
    FOLLOW_test_in_dict_or_set_maker1737 = frozenset([1, 18, 36])
    FOLLOW_comp_for_in_dict_or_set_maker1740 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1745 = frozenset(
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
    FOLLOW_test_in_dict_or_set_maker1747 = frozenset([17])
    FOLLOW_COLON_in_dict_or_set_maker1749 = frozenset(
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
    FOLLOW_test_in_dict_or_set_maker1751 = frozenset([1, 18])
    FOLLOW_comp_for_in_dict_or_set_maker1766 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1771 = frozenset(
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
    FOLLOW_test_in_dict_or_set_maker1773 = frozenset([1, 18])
    FOLLOW_comp_for_in_comp_iter1787 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter1791 = frozenset([1])
    FOLLOW_FOR_in_comp_for1799 = frozenset(
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
    FOLLOW_exprlist_in_comp_for1801 = frozenset([51])
    FOLLOW_IN_in_comp_for1803 = frozenset(
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
    FOLLOW_or_test_in_comp_for1805 = frozenset([1, 36, 50])
    FOLLOW_comp_iter_in_comp_for1807 = frozenset([1])
    FOLLOW_IF_in_comp_if1817 = frozenset(
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
    FOLLOW_test_nocond_in_comp_if1819 = frozenset([1, 36, 50])
    FOLLOW_comp_iter_in_comp_if1821 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
