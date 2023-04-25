# $ANTLR 3.5.1 C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g 2023-04-26 00:01:51

import sys

from antlr3 import *

# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF = -1
ADD_ASSIGN = 4
AND = 5
AND_ASSIGN = 6
AROUND = 7
ASSIGN = 8
AT = 9
AXIS = 10
BIN_DIGIT = 11
BIT_AND = 12
BIT_NOT = 13
BIT_OR = 14
CAMERA = 15
CAM_TRANSLATE = 16
CHOICE = 17
COLON = 18
COMMA = 19
COMMENT = 20
CREATE = 21
DEDENT = 22
DEF = 23
DIGIT = 24
DIV = 25
DIV_ASSIGN = 26
DOT = 27
EDIT = 28
ELLIPSIS = 29
ELSE = 30
EQUALS = 31
EVERY = 32
EXPONENT = 33
EXPONENT_FLOAT = 34
FALSE = 35
FETCH = 36
FLOAT_NUMBER = 37
FOR = 38
FRACTION = 39
FRAMES = 40
FROM = 41
GET = 42
GROUP = 43
GT = 44
GT_EQ = 45
HEX_DIGIT = 46
ID = 47
IDIV = 48
IDIV_ASSIGN = 49
ID_CONTINUE = 50
ID_START = 51
IF = 52
IN = 53
INDENT = 54
INSTANTIATE = 55
INTEGER = 56
INT_PART = 57
IS = 58
LBRACE = 59
LBRACK = 60
LETTER = 61
LIGHT = 62
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
PLUS = 91
POINT_FLOAT = 92
POWER = 93
POWER_ASSIGN = 94
RANGE = 95
RBRACE = 96
RBRACK = 97
RETURN = 98
ROTATE = 99
RPAREN = 100
RSHIFT = 101
RSHIFT_ASSIGN = 102
SCALE = 103
SCATTER = 104
SCATTER_TYPE = 105
SCENARIO = 106
SEMANTICS = 107
SEMI = 108
SEQUENCE = 109
SETTINGS = 110
SETTING_ID = 111
SHAPES = 112
SHORT_STRING = 113
SIZE = 114
SKIP_ = 115
SNIPPET = 116
SPACES = 117
STAGE = 118
STEREO = 119
STRING = 120
STRING_ESCAPE_SEQ = 121
SUB_ASSIGN = 122
TEXTURE = 123
TIME = 124
TIMELINE = 125
TO = 126
TRANSLATE = 127
TRUE = 128
UNDERSCORE = 129
UNIFORM = 130
UNKNOWN = 131
UP_AXIS = 132
VISIBLE = 133
WRITERS = 134
XOR = 135
XOR_ASSIGN = 136

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
    7: "AROUND",
    8: "ASSIGN",
    9: "AT",
    10: "AXIS",
    11: "BIN_DIGIT",
    12: "BIT_AND",
    13: "BIT_NOT",
    14: "BIT_OR",
    15: "CAMERA",
    16: "CAM_TRANSLATE",
    17: "CHOICE",
    18: "COLON",
    19: "COMMA",
    20: "COMMENT",
    21: "CREATE",
    22: "DEDENT",
    23: "DEF",
    24: "DIGIT",
    25: "DIV",
    26: "DIV_ASSIGN",
    27: "DOT",
    28: "EDIT",
    29: "ELLIPSIS",
    30: "ELSE",
    31: "EQUALS",
    32: "EVERY",
    33: "EXPONENT",
    34: "EXPONENT_FLOAT",
    35: "FALSE",
    36: "FETCH",
    37: "FLOAT_NUMBER",
    38: "FOR",
    39: "FRACTION",
    40: "FRAMES",
    41: "FROM",
    42: "GET",
    43: "GROUP",
    44: "GT",
    45: "GT_EQ",
    46: "HEX_DIGIT",
    47: "ID",
    48: "IDIV",
    49: "IDIV_ASSIGN",
    50: "ID_CONTINUE",
    51: "ID_START",
    52: "IF",
    53: "IN",
    54: "INDENT",
    55: "INSTANTIATE",
    56: "INTEGER",
    57: "INT_PART",
    58: "IS",
    59: "LBRACE",
    60: "LBRACK",
    61: "LETTER",
    62: "LIGHT",
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
    91: "PLUS",
    92: "POINT_FLOAT",
    93: "POWER",
    94: "POWER_ASSIGN",
    95: "RANGE",
    96: "RBRACE",
    97: "RBRACK",
    98: "RETURN",
    99: "ROTATE",
    100: "RPAREN",
    101: "RSHIFT",
    102: "RSHIFT_ASSIGN",
    103: "SCALE",
    104: "SCATTER",
    105: "SCATTER_TYPE",
    106: "SCENARIO",
    107: "SEMANTICS",
    108: "SEMI",
    109: "SEQUENCE",
    110: "SETTINGS",
    111: "SETTING_ID",
    112: "SHAPES",
    113: "SHORT_STRING",
    114: "SIZE",
    115: "SKIP_",
    116: "SNIPPET",
    117: "SPACES",
    118: "STAGE",
    119: "STEREO",
    120: "STRING",
    121: "STRING_ESCAPE_SEQ",
    122: "SUB_ASSIGN",
    123: "TEXTURE",
    124: "TIME",
    125: "TIMELINE",
    126: "TO",
    127: "TRANSLATE",
    128: "TRUE",
    129: "UNDERSCORE",
    130: "UNIFORM",
    131: "UNKNOWN",
    132: "UP_AXIS",
    133: "VISIBLE",
    134: "WRITERS",
    135: "XOR",
    136: "XOR_ASSIGN",
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
    "AROUND",
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
    "DEF",
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
    "PLUS",
    "POINT_FLOAT",
    "POWER",
    "POWER_ASSIGN",
    "RANGE",
    "RBRACE",
    "RBRACK",
    "RETURN",
    "ROTATE",
    "RPAREN",
    "RSHIFT",
    "RSHIFT_ASSIGN",
    "SCALE",
    "SCATTER",
    "SCATTER_TYPE",
    "SCENARIO",
    "SEMANTICS",
    "SEMI",
    "SEQUENCE",
    "SETTINGS",
    "SETTING_ID",
    "SHAPES",
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
    "TEXTURE",
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
                pass
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
                        pass
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
                    pass
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
                    pass
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
                    pass
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
                pass
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
                    pass
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
                pass
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
                        pass
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
                pass
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
                pass
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
                        FETCH,
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
                            NEWLINE,
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
                        pass
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers131
                        )
                        self.expr_stmt()

                        self._state.following.pop()

                    elif alt7 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:13:57: writer
                        pass
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
                pass
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
                    pass
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
                        FETCH,
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
                        pass
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts165
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt9 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:38: edit_stmt
                        pass
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts169)
                        self.edit_stmt()

                        self._state.following.pop()

                    elif alt9 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:16:50: behavior_stmt
                        pass
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
                pass
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
                        pass
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
                pass
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
                pass
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
                    pass
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt219
                    )

                elif alt11 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:22:30: name
                    pass
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:24:1: create_expr : CREATE ( test )? ( ( ( STEREO )? CAMERA | SHAPES | name LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) ;
    def create_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:24:12: ( CREATE ( test )? ( ( ( STEREO )? CAMERA | SHAPES | name LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:3: CREATE ( test )? ( ( ( STEREO )? CAMERA | SHAPES | name LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                pass
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr235)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:10: ( test )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if LA12_0 in {
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
                    UNIFORM,
                }:
                    alt12 = 1
                elif LA12_0 in {ID, UNDERSCORE}:
                    LA12_2 = self.input.LA(2)

                    if LA12_2 in {
                        AND,
                        BIT_AND,
                        BIT_OR,
                        CAMERA,
                        DIV,
                        DOT,
                        EQUALS,
                        FROM,
                        GT,
                        GT_EQ,
                        ID,
                        IDIV,
                        IF,
                        IN,
                        IS,
                        LBRACK,
                        LSHIFT,
                        LT,
                        LT_EQ,
                        MATERIAL,
                        MINUS,
                        MOD,
                        MUL,
                        NOT,
                        NOT_EQ,
                        OR,
                        PLUS,
                        POWER,
                        RSHIFT,
                        SHAPES,
                        STEREO,
                        UNDERSCORE,
                        XOR,
                    }:
                        alt12 = 1
                if alt12 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:10: test
                    pass
                    self._state.following.append(self.FOLLOW_test_in_create_expr237)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:25:16: ( ( ( STEREO )? CAMERA | SHAPES | name LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if LA16_0 in {CAMERA, FROM, ID, SHAPES, STEREO, UNDERSCORE}:
                    alt16 = 1
                elif LA16_0 == MATERIAL:
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:5: ( ( STEREO )? CAMERA | SHAPES | name LIGHT | FROM test ) ( edit_block | NEWLINE )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:5: ( ( STEREO )? CAMERA | SHAPES | name LIGHT | FROM test )
                    alt14 = 4
                    LA14 = self.input.LA(1)
                    if LA14 in {CAMERA, STEREO}:
                        alt14 = 1
                    elif LA14 in {SHAPES}:
                        alt14 = 2
                    elif LA14 in {ID, UNDERSCORE}:
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
                            pass
                            self.match(
                                self.input, STEREO, self.FOLLOW_STEREO_in_create_expr247
                            )

                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr250
                        )

                    elif alt14 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:23: SHAPES
                        pass
                        self.match(
                            self.input, SHAPES, self.FOLLOW_SHAPES_in_create_expr254
                        )

                    elif alt14 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:32: name LIGHT
                        pass
                        self._state.following.append(self.FOLLOW_name_in_create_expr258)
                        self.name()

                        self._state.following.pop()

                        self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr260
                        )

                    elif alt14 == 4:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:45: FROM test
                        pass
                        self.match(self.input, FROM, self.FOLLOW_FROM_in_create_expr264)

                        self._state.following.append(self.FOLLOW_test_in_create_expr266)
                        self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:56: ( edit_block | NEWLINE )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:57: edit_block
                        pass
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr270
                        )
                        self.edit_block()

                        self._state.following.pop()

                    elif alt15 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:26:70: NEWLINE
                        pass
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr274
                        )

                elif alt16 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:7: MATERIAL ( simple_block )
                    pass
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr283
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:16: ( simple_block )
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:27:17: simple_block
                    pass
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

    # $ANTLR start "instantiate_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:1: instantiate_expr : INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) ;
    def instantiate_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:18: ( INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:20: INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE )
                pass
                self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr300,
                )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:32: ( test )?
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:33: test
                    pass
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr303
                    )
                    self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr307)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr309)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:50: ( edit_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:51: edit_block
                    pass
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr312
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt18 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:31:64: NEWLINE
                    pass
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instantiate_expr316
                    )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "instantiate_expr"

    # $ANTLR start "group_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:1: group_expr : GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) ;
    def group_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:18: ( GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:20: GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE )
                pass
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_expr330)

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr332)

                self._state.following.append(self.FOLLOW_name_in_group_expr334)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:38: ( COMMA name )*
                while True:  # loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if LA19_0 == COMMA:
                        alt19 = 1

                    if alt19 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:39: COMMA name
                        pass
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_group_expr337
                        )

                        self._state.following.append(self.FOLLOW_name_in_group_expr339)
                        self.name()

                        self._state.following.pop()

                    else:
                        break  # loop19

                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_group_expr343)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:59: ( edit_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:60: edit_block
                    pass
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr346
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt20 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:32:73: NEWLINE
                    pass
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_group_expr350
                    )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "group_expr"

    # $ANTLR start "get_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:1: get_expr : GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) ;
    def get_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:9: ( GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:12: GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE )
                pass
                self.match(self.input, GET, self.FOLLOW_GET_in_get_expr358)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:16: ( ( CAMERA | LIGHT | MATERIAL | name ) AT )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if LA22_0 in {CAMERA, LIGHT, MATERIAL}:
                    alt22 = 1
                elif LA22_0 in {ID, UNDERSCORE}:
                    LA22_2 = self.input.LA(2)

                    if LA22_2 == AT:
                        alt22 = 1
                if alt22 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:17: ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:17: ( CAMERA | LIGHT | MATERIAL | name )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:18: CAMERA
                        pass
                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr362
                        )

                    elif alt21 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:27: LIGHT
                        pass
                        self.match(self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr366)

                    elif alt21 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:35: MATERIAL
                        pass
                        self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr370
                        )

                    elif alt21 == 4:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:46: name
                        pass
                        self._state.following.append(self.FOLLOW_name_in_get_expr374)
                        self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr377)

                self._state.following.append(self.FOLLOW_test_in_get_expr381)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:62: ( simple_block | NEWLINE )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:63: simple_block
                    pass
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr384
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt23 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:33:78: NEWLINE
                    pass
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr388)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "get_expr"

    # $ANTLR start "edit_block"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:1: edit_block : COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT ;
    def edit_block(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:14: ( COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:16: COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT
                pass
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block399)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block401)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block403)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:37: ( attr | inner_behavior_stmt )+
                cnt24 = 0
                while True:  # loop24
                    alt24 = 3
                    LA24_0 = self.input.LA(1)

                    if LA24_0 in {
                        CAM_TRANSLATE,
                        ID,
                        LOOK_AT,
                        ROTATE,
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:38: attr
                        pass
                        self._state.following.append(self.FOLLOW_attr_in_edit_block406)
                        self.attr()

                        self._state.following.pop()

                    elif alt24 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:35:45: inner_behavior_stmt
                        pass
                        self._state.following.append(
                            self.FOLLOW_inner_behavior_stmt_in_edit_block410
                        )
                        self.inner_behavior_stmt()

                        self._state.following.pop()

                    else:
                        if cnt24 >= 1:
                            break  # loop24

                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_block414)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "edit_block"

    # $ANTLR start "simple_block"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:1: simple_block : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:14: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:16: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                pass
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block421)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block423)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block425)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:37: ( simple_attr )+
                cnt25 = 0
                while True:  # loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if LA25_0 in {ID, UNDERSCORE}:
                        alt25 = 1

                    if alt25 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:36:37: simple_attr
                        pass
                        self._state.following.append(
                            self.FOLLOW_simple_attr_in_simple_block427
                        )
                        self.simple_attr()

                        self._state.following.pop()

                    else:
                        if cnt25 >= 1:
                            break  # loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_simple_block430)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "simple_block"

    # $ANTLR start "attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:1: attr : ( core_attr | simple_attr | compound_attr );
    def attr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:15: ( core_attr | simple_attr | compound_attr )
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
                elif LA26 in {SCATTER}:
                    alt26 = 3
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:17: core_attr
                    pass
                    self._state.following.append(self.FOLLOW_core_attr_in_attr447)
                    self.core_attr()

                    self._state.following.pop()

                elif alt26 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:29: simple_attr
                    pass
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr451)
                    self.simple_attr()

                    self._state.following.pop()

                elif alt26 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:38:43: compound_attr
                    pass
                    self._state.following.append(self.FOLLOW_compound_attr_in_attr455)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:1: simple_attr : name ( COLON name )? ( test )? NEWLINE ;
    def simple_attr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:15: ( name ( COLON name )? ( test )? NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:17: name ( COLON name )? ( test )? NEWLINE
                pass
                self._state.following.append(self.FOLLOW_name_in_simple_attr464)
                self.name()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:22: ( COLON name )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if LA27_0 == COLON:
                    alt27 = 1
                if alt27 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:23: COLON name
                    pass
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr467)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr469)
                    self.name()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:36: ( test )?
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:39:36: test
                    pass
                    self._state.following.append(self.FOLLOW_test_in_simple_attr473)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_attr476)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "simple_attr"

    # $ANTLR start "compound_attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:41:1: compound_attr : SCATTER NEWLINE ;
    def compound_attr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:41:15: ( SCATTER NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:41:17: SCATTER NEWLINE
                pass
                self.match(self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr484)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_compound_attr486)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "compound_attr"

    # $ANTLR start "core_attr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:1: core_attr : ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE ;
    def core_attr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:43:10: ( ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:44:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test )
                alt32 = 9
                LA32 = self.input.LA(1)
                if LA32 in {TRANSLATE}:
                    alt32 = 1
                elif LA32 in {CAM_TRANSLATE}:
                    alt32 = 2
                elif LA32 in {ROTATE}:
                    alt32 = 3
                elif LA32 in {SCALE}:
                    alt32 = 4
                elif LA32 in {LOOK_AT}:
                    alt32 = 5
                elif LA32 in {UP_AXIS}:
                    alt32 = 6
                elif LA32 in {SIZE}:
                    alt32 = 7
                elif LA32 in {SEMANTICS}:
                    alt32 = 8
                elif LA32 in {VISIBLE}:
                    alt32 = 9
                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:5: TRANSLATE ( AXIS )? TO test
                    pass
                    self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr503
                    )

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:15: ( AXIS )?
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if LA29_0 == AXIS:
                        alt29 = 1
                    if alt29 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:45:15: AXIS
                        pass
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr505)

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr508)

                    self._state.following.append(self.FOLLOW_test_in_core_attr510)
                    self.test()

                    self._state.following.pop()

                elif alt32 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:46:7: CAM_TRANSLATE TO test
                    pass
                    self.match(
                        self.input,
                        CAM_TRANSLATE,
                        self.FOLLOW_CAM_TRANSLATE_in_core_attr518,
                    )

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr520)

                    self._state.following.append(self.FOLLOW_test_in_core_attr522)
                    self.test()

                    self._state.following.pop()

                elif alt32 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:7: ROTATE ( AXIS )? test ( ORDER )?
                    pass
                    self.match(self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr530)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:14: ( AXIS )?
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if LA30_0 == AXIS:
                        alt30 = 1
                    if alt30 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:14: AXIS
                        pass
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr532)

                    self._state.following.append(self.FOLLOW_test_in_core_attr535)
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:25: ( ORDER )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if LA31_0 == ORDER:
                        alt31 = 1
                    if alt31 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:47:25: ORDER
                        pass
                        self.match(self.input, ORDER, self.FOLLOW_ORDER_in_core_attr537)

                elif alt32 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:48:7: SCALE test
                    pass
                    self.match(self.input, SCALE, self.FOLLOW_SCALE_in_core_attr546)

                    self._state.following.append(self.FOLLOW_test_in_core_attr548)
                    self.test()

                    self._state.following.pop()

                elif alt32 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:49:7: LOOK_AT test
                    pass
                    self.match(self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr556)

                    self._state.following.append(self.FOLLOW_test_in_core_attr558)
                    self.test()

                    self._state.following.pop()

                elif alt32 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:50:7: UP_AXIS test
                    pass
                    self.match(self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr566)

                    self._state.following.append(self.FOLLOW_test_in_core_attr568)
                    self.test()

                    self._state.following.pop()

                elif alt32 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:51:7: SIZE test
                    pass
                    self.match(self.input, SIZE, self.FOLLOW_SIZE_in_core_attr576)

                    self._state.following.append(self.FOLLOW_test_in_core_attr578)
                    self.test()

                    self._state.following.pop()

                elif alt32 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:52:7: SEMANTICS test
                    pass
                    self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr586
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr588)
                    self.test()

                    self._state.following.pop()

                elif alt32 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:53:7: VISIBLE test
                    pass
                    self.match(self.input, VISIBLE, self.FOLLOW_VISIBLE_in_core_attr596)

                    self._state.following.append(self.FOLLOW_test_in_core_attr598)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_core_attr604)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "core_attr"

    # $ANTLR start "inner_behavior_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:1: inner_behavior_stmt : behavior_expr inner_behavior_block ;
    def inner_behavior_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:22: ( behavior_expr inner_behavior_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:57:24: behavior_expr inner_behavior_block
                pass
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_inner_behavior_stmt614
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_inner_behavior_block_in_inner_behavior_stmt616
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:58:1: inner_behavior_block : COLON NEWLINE INDENT ( attr )+ DEDENT ;
    def inner_behavior_block(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:58:22: ( COLON NEWLINE INDENT ( attr )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:58:24: COLON NEWLINE INDENT ( attr )+ DEDENT
                pass
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block623
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block625
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block627
                )

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:58:45: ( attr )+
                cnt33 = 0
                while True:  # loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if LA33_0 in {
                        CAM_TRANSLATE,
                        ID,
                        LOOK_AT,
                        ROTATE,
                        SCALE,
                        SCATTER,
                        SEMANTICS,
                        SIZE,
                        TRANSLATE,
                        UNDERSCORE,
                        UP_AXIS,
                        VISIBLE,
                    }:
                        alt33 = 1

                    if alt33 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:58:45: attr
                        pass
                        self._state.following.append(
                            self.FOLLOW_attr_in_inner_behavior_block629
                        )
                        self.attr()

                        self._state.following.pop()

                    else:
                        if cnt33 >= 1:
                            break  # loop33

                        eee = EarlyExitException(33, self.input)
                        raise eee

                    cnt33 += 1

                self.match(
                    self.input, DEDENT, self.FOLLOW_DEDENT_in_inner_behavior_block632
                )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "inner_behavior_block"

    # $ANTLR start "behavior_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:1: behavior_stmt : behavior_expr behavior_block ;
    def behavior_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:16: ( behavior_expr behavior_block )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:61:18: behavior_expr behavior_block
                pass
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_behavior_stmt643
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_behavior_block_in_behavior_stmt645
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:1: behavior_expr : EVERY ( test )? ( FRAMES | TIME ) ;
    def behavior_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:16: ( EVERY ( test )? ( FRAMES | TIME ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:18: EVERY ( test )? ( FRAMES | TIME )
                pass
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr653)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:24: ( test )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if LA34_0 in {
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
                    alt34 = 1
                if alt34 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:62:24: test
                    pass
                    self._state.following.append(self.FOLLOW_test_in_behavior_expr655)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:63:1: behavior_block : COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT ;
    def behavior_block(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:63:16: ( COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:63:18: COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT
                pass
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block671)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block673
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block675)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:63:39: ( aug_expr_stmt | edit_stmt )+
                cnt35 = 0
                while True:  # loop35
                    alt35 = 3
                    LA35_0 = self.input.LA(1)

                    if LA35_0 in {
                        BIT_NOT,
                        CHOICE,
                        CREATE,
                        FALSE,
                        FETCH,
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
                        alt35 = 1
                    elif LA35_0 == EDIT:
                        alt35 = 2

                    if alt35 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:63:40: aug_expr_stmt
                        pass
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block678
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt35 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:63:56: edit_stmt
                        pass
                        self._state.following.append(
                            self.FOLLOW_edit_stmt_in_behavior_block682
                        )
                        self.edit_stmt()

                        self._state.following.pop()

                    else:
                        if cnt35 >= 1:
                            break  # loop35

                        eee = EarlyExitException(35, self.input)
                        raise eee

                    cnt35 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_behavior_block686)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "behavior_block"

    # $ANTLR start "expr_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:1: expr_stmt : ( testlist ( ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) )? | fetch_expr ) NEWLINE ;
    def expr_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:10: ( ( testlist ( ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) )? | fetch_expr ) NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:12: ( testlist ( ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) )? | fetch_expr ) NEWLINE
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:66:12: ( testlist ( ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) )? | fetch_expr )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:5: testlist ( ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) )?
                    pass
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt701)
                    self.testlist()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:14: ( ( aug_assign | ASSIGN ) ( testlist | fetch_expr ) )?
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if LA38_0 in {
                        ADD_ASSIGN,
                        AND_ASSIGN,
                        ASSIGN,
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
                    if alt38 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:15: ( aug_assign | ASSIGN ) ( testlist | fetch_expr )
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:15: ( aug_assign | ASSIGN )
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if LA36_0 in {
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
                            alt36 = 1
                        elif LA36_0 == ASSIGN:
                            alt36 = 2
                        else:
                            nvae = NoViableAltException("", 36, 0, self.input)

                            raise nvae

                        if alt36 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:16: aug_assign
                            pass
                            self._state.following.append(
                                self.FOLLOW_aug_assign_in_expr_stmt705
                            )
                            self.aug_assign()

                            self._state.following.pop()

                        elif alt36 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:29: ASSIGN
                            pass
                            self.match(
                                self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr_stmt709
                            )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:37: ( testlist | fetch_expr )
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if LA37_0 in {
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
                            alt37 = 1
                        elif LA37_0 == FETCH:
                            alt37 = 2
                        else:
                            nvae = NoViableAltException("", 37, 0, self.input)

                            raise nvae

                        if alt37 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:38: testlist
                            pass
                            self._state.following.append(
                                self.FOLLOW_testlist_in_expr_stmt713
                            )
                            self.testlist()

                            self._state.following.pop()

                        elif alt37 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:67:49: fetch_expr
                            pass
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_expr_stmt717
                            )
                            self.fetch_expr()

                            self._state.following.pop()

                elif alt39 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:68:7: fetch_expr
                    pass
                    self._state.following.append(self.FOLLOW_fetch_expr_in_expr_stmt728)
                    self.fetch_expr()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expr_stmt734)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "expr_stmt"

    # $ANTLR start "aug_expr_stmt"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:1: aug_expr_stmt : ( testlist ( NEWLINE | aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) | fetch_expr NEWLINE | create_expr | instantiate_expr | get_expr | group_expr );
    def aug_expr_stmt(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:14: ( testlist ( NEWLINE | aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) | fetch_expr NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                alt44 = 6
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
                elif LA44 in {FETCH}:
                    alt44 = 2
                elif LA44 in {CREATE}:
                    alt44 = 3
                elif LA44 in {INSTANTIATE}:
                    alt44 = 4
                elif LA44 in {GET}:
                    alt44 = 5
                elif LA44 in {GROUP}:
                    alt44 = 6
                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae

                if alt44 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:5: testlist ( NEWLINE | aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    pass
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt746
                    )
                    self.testlist()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:14: ( NEWLINE | aug_assign ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    alt43 = 3
                    LA43 = self.input.LA(1)
                    if LA43 in {NEWLINE}:
                        alt43 = 1
                    elif LA43 in {
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
                        alt43 = 2
                    elif LA43 in {ASSIGN}:
                        alt43 = 3
                    else:
                        nvae = NoViableAltException("", 43, 0, self.input)

                        raise nvae

                    if alt43 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:7: NEWLINE
                        pass
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_aug_expr_stmt756
                        )

                    elif alt43 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:9: aug_assign ( testlist | fetch_expr )? NEWLINE
                        pass
                        self._state.following.append(
                            self.FOLLOW_aug_assign_in_aug_expr_stmt766
                        )
                        self.aug_assign()

                        self._state.following.pop()

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:20: ( testlist | fetch_expr )?
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:21: testlist
                            pass
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt769
                            )
                            self.testlist()

                            self._state.following.pop()

                        elif alt40 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:32: fetch_expr
                            pass
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt773
                            )
                            self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_aug_expr_stmt777
                        )

                    elif alt43 == 3:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:9: ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        pass
                        self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt787
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:16: ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:9: ( testlist | fetch_expr ) NEWLINE
                            pass
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:9: ( testlist | fetch_expr )
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
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:10: testlist
                                pass
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt800
                                )
                                self.testlist()

                                self._state.following.pop()

                            elif alt41 == 2:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:21: fetch_expr
                                pass
                                self._state.following.append(
                                    self.FOLLOW_fetch_expr_in_aug_expr_stmt804
                                )
                                self.fetch_expr()

                                self._state.following.pop()

                            self.match(
                                self.input,
                                NEWLINE,
                                self.FOLLOW_NEWLINE_in_aug_expr_stmt807,
                            )

                        elif alt42 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:11: create_expr
                            pass
                            self._state.following.append(
                                self.FOLLOW_create_expr_in_aug_expr_stmt819
                            )
                            self.create_expr()

                            self._state.following.pop()

                        elif alt42 == 3:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:25: instantiate_expr
                            pass
                            self._state.following.append(
                                self.FOLLOW_instantiate_expr_in_aug_expr_stmt823
                            )
                            self.instantiate_expr()

                            self._state.following.pop()

                        elif alt42 == 4:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:44: get_expr
                            pass
                            self._state.following.append(
                                self.FOLLOW_get_expr_in_aug_expr_stmt827
                            )
                            self.get_expr()

                            self._state.following.pop()

                        elif alt42 == 5:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:78:55: group_expr
                            pass
                            self._state.following.append(
                                self.FOLLOW_group_expr_in_aug_expr_stmt831
                            )
                            self.group_expr()

                            self._state.following.pop()

                elif alt44 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:5: fetch_expr NEWLINE
                    pass
                    self._state.following.append(
                        self.FOLLOW_fetch_expr_in_aug_expr_stmt851
                    )
                    self.fetch_expr()

                    self._state.following.pop()

                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_aug_expr_stmt853
                    )

                elif alt44 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:5: create_expr
                    pass
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_aug_expr_stmt859
                    )
                    self.create_expr()

                    self._state.following.pop()

                elif alt44 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:19: instantiate_expr
                    pass
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_aug_expr_stmt863
                    )
                    self.instantiate_expr()

                    self._state.following.pop()

                elif alt44 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:38: get_expr
                    pass
                    self._state.following.append(
                        self.FOLLOW_get_expr_in_aug_expr_stmt867
                    )
                    self.get_expr()

                    self._state.following.pop()

                elif alt44 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:82:49: group_expr
                    pass
                    self._state.following.append(
                        self.FOLLOW_group_expr_in_aug_expr_stmt871
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:85:1: fetch_expr : FETCH test FROM test ( MATCH test )? ;
    def fetch_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:85:12: ( FETCH test FROM test ( MATCH test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:85:14: FETCH test FROM test ( MATCH test )?
                pass
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr880)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr882)
                self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr884)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr886)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:85:35: ( MATCH test )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 == MATCH:
                    alt45 = 1
                if alt45 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:85:36: MATCH test
                    pass
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr889)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr891)
                    self.test()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "fetch_expr"

    # $ANTLR start "aug_assign"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:1: aug_assign : ( ADD_ASSIGN | SUB_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | POWER_ASSIGN | IDIV_ASSIGN );
    def aug_assign(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:86:11: ( ADD_ASSIGN | SUB_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | POWER_ASSIGN | IDIV_ASSIGN )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                pass
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:1: test : or_test ( IF or_test ELSE test )? ;
    def test(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:13: ( or_test ( IF or_test ELSE test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:15: or_test ( IF or_test ELSE test )?
                pass
                self._state.following.append(self.FOLLOW_or_test_in_test985)
                self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:23: ( IF or_test ELSE test )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 == IF:
                    alt46 = 1
                if alt46 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:24: IF or_test ELSE test
                    pass
                    self.match(self.input, IF, self.FOLLOW_IF_in_test988)

                    self._state.following.append(self.FOLLOW_or_test_in_test990)
                    self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test992)

                    self._state.following.append(self.FOLLOW_test_in_test994)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:1: test_nocond : or_test ;
    def test_nocond(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:13: ( or_test )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:15: or_test
                pass
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond1003)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:1: or_test : and_test ( OR and_test )* ;
    def or_test(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:13: ( and_test ( OR and_test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:15: and_test ( OR and_test )*
                pass
                self._state.following.append(self.FOLLOW_and_test_in_or_test1014)
                self.and_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:24: ( OR and_test )*
                while True:  # loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if LA47_0 == OR:
                        alt47 = 1

                    if alt47 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:25: OR and_test
                        pass
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test1017)

                        self._state.following.append(
                            self.FOLLOW_and_test_in_or_test1019
                        )
                        self.and_test()

                        self._state.following.pop()

                    else:
                        break  # loop47

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "or_test"

    # $ANTLR start "and_test"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:1: and_test : not_test ( AND not_test )* ;
    def and_test(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:13: ( not_test ( AND not_test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:15: not_test ( AND not_test )*
                pass
                self._state.following.append(self.FOLLOW_not_test_in_and_test1031)
                self.not_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:24: ( AND not_test )*
                while True:  # loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if LA48_0 == AND:
                        alt48 = 1

                    if alt48 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:25: AND not_test
                        pass
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test1034)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test1036
                        )
                        self.not_test()

                        self._state.following.pop()

                    else:
                        break  # loop48

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "and_test"

    # $ANTLR start "not_test"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:1: not_test : ( NOT not_test | comparison );
    def not_test(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:13: ( NOT not_test | comparison )
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if LA49_0 == NOT:
                    alt49 = 1
                elif LA49_0 in {
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
                    alt49 = 2
                else:
                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae

                if alt49 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:15: NOT not_test
                    pass
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1048)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1050)
                    self.not_test()

                    self._state.following.pop()

                elif alt49 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:30: comparison
                    pass
                    self._state.following.append(self.FOLLOW_comparison_in_not_test1054)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:1: comparison : expr ( comp_op expr )* ;
    def comparison(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:13: ( expr ( comp_op expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:15: expr ( comp_op expr )*
                pass
                self._state.following.append(self.FOLLOW_expr_in_comparison1062)
                self.expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:20: ( comp_op expr )*
                while True:  # loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if LA50_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt50 = 1

                    if alt50 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:21: comp_op expr
                        pass
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison1065
                        )
                        self.comp_op()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_expr_in_comparison1067)
                        self.expr()

                        self._state.following.pop()

                    else:
                        break  # loop50

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comparison"

    # $ANTLR start "comp_op"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:1: comp_op : ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT );
    def comp_op(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:13: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                alt51 = 10
                LA51 = self.input.LA(1)
                if LA51 in {LT}:
                    alt51 = 1
                elif LA51 in {GT}:
                    alt51 = 2
                elif LA51 in {EQUALS}:
                    alt51 = 3
                elif LA51 in {GT_EQ}:
                    alt51 = 4
                elif LA51 in {LT_EQ}:
                    alt51 = 5
                elif LA51 in {NOT_EQ}:
                    alt51 = 6
                elif LA51 in {IN}:
                    alt51 = 7
                elif LA51 in {NOT}:
                    alt51 = 8
                elif LA51 in {IS}:
                    LA51_9 = self.input.LA(2)

                    if LA51_9 == NOT:
                        alt51 = 10
                    elif LA51_9 in {
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
                        alt51 = 9
                    else:
                        nvae = NoViableAltException("", 51, 9, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 51, 0, self.input)

                    raise nvae

                if alt51 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:15: LT
                    pass
                    self.match(self.input, LT, self.FOLLOW_LT_in_comp_op1080)

                elif alt51 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:20: GT
                    pass
                    self.match(self.input, GT, self.FOLLOW_GT_in_comp_op1084)

                elif alt51 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:25: EQUALS
                    pass
                    self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op1088)

                elif alt51 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:34: GT_EQ
                    pass
                    self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op1092)

                elif alt51 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:42: LT_EQ
                    pass
                    self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op1096)

                elif alt51 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:50: NOT_EQ
                    pass
                    self.match(self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op1100)

                elif alt51 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:59: IN
                    pass
                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1104)

                elif alt51 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:64: NOT IN
                    pass
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1108)

                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1110)

                elif alt51 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:73: IS
                    pass
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1114)

                elif alt51 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:78: IS NOT
                    pass
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1118)

                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1120)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comp_op"

    # $ANTLR start "expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:1: expr : xor_expr ( BIT_OR xor_expr )* ;
    def expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:13: ( xor_expr ( BIT_OR xor_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:15: xor_expr ( BIT_OR xor_expr )*
                pass
                self._state.following.append(self.FOLLOW_xor_expr_in_expr1134)
                self.xor_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:24: ( BIT_OR xor_expr )*
                while True:  # loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if LA52_0 == BIT_OR:
                        alt52 = 1

                    if alt52 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:25: BIT_OR xor_expr
                        pass
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr1137)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr1139)
                        self.xor_expr()

                        self._state.following.pop()

                    else:
                        break  # loop52

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "expr"

    # $ANTLR start "xor_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:1: xor_expr : and_expr ( XOR and_expr )* ;
    def xor_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:13: ( and_expr ( XOR and_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:15: and_expr ( XOR and_expr )*
                pass
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1151)
                self.and_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:24: ( XOR and_expr )*
                while True:  # loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if LA53_0 == XOR:
                        alt53 = 1

                    if alt53 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:25: XOR and_expr
                        pass
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr1154)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr1156
                        )
                        self.and_expr()

                        self._state.following.pop()

                    else:
                        break  # loop53

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "xor_expr"

    # $ANTLR start "and_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:1: and_expr : shift_expr ( BIT_AND shift_expr )* ;
    def and_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:13: ( shift_expr ( BIT_AND shift_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:15: shift_expr ( BIT_AND shift_expr )*
                pass
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1168)
                self.shift_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:26: ( BIT_AND shift_expr )*
                while True:  # loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if LA54_0 == BIT_AND:
                        alt54 = 1

                    if alt54 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:111:27: BIT_AND shift_expr
                        pass
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr1171
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr1173
                        )
                        self.shift_expr()

                        self._state.following.pop()

                    else:
                        break  # loop54

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "and_expr"

    # $ANTLR start "shift_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:1: shift_expr : arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* ;
    def shift_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:13: ( arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:15: arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )*
                pass
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1183)
                self.arith_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:26: ( ( LSHIFT | RSHIFT ) arith_expr )*
                while True:  # loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if LA55_0 in {LSHIFT, RSHIFT}:
                        alt55 = 1

                    if alt55 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:112:27: ( LSHIFT | RSHIFT ) arith_expr
                        pass
                        if self.input.LA(1) in {LSHIFT, RSHIFT}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr1194
                        )
                        self.arith_expr()

                        self._state.following.pop()

                    else:
                        break  # loop55

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "shift_expr"

    # $ANTLR start "arith_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:1: arith_expr : term ( ( PLUS | MINUS ) term )* ;
    def arith_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:13: ( term ( ( PLUS | MINUS ) term )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:15: term ( ( PLUS | MINUS ) term )*
                pass
                self._state.following.append(self.FOLLOW_term_in_arith_expr1204)
                self.term()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:20: ( ( PLUS | MINUS ) term )*
                while True:  # loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if LA56_0 in {MINUS, PLUS}:
                        alt56 = 1

                    if alt56 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:21: ( PLUS | MINUS ) term
                        pass
                        if self.input.LA(1) in {MINUS, PLUS}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_term_in_arith_expr1215)
                        self.term()

                        self._state.following.pop()

                    else:
                        break  # loop56

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "arith_expr"

    # $ANTLR start "term"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:1: term : factor ( ( MUL | DIV | MOD | IDIV ) factor )* ;
    def term(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:13: ( factor ( ( MUL | DIV | MOD | IDIV ) factor )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:15: factor ( ( MUL | DIV | MOD | IDIV ) factor )*
                pass
                self._state.following.append(self.FOLLOW_factor_in_term1231)
                self.factor()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:22: ( ( MUL | DIV | MOD | IDIV ) factor )*
                while True:  # loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if LA57_0 in {DIV, IDIV, MOD, MUL}:
                        alt57 = 1

                    if alt57 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:114:23: ( MUL | DIV | MOD | IDIV ) factor
                        pass
                        if self.input.LA(1) in {DIV, IDIV, MOD, MUL}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_factor_in_term1250)
                        self.factor()

                        self._state.following.pop()

                    else:
                        break  # loop57

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "term"

    # $ANTLR start "factor"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:1: factor : ( ( PLUS | MINUS | BIT_NOT ) factor | power );
    def factor(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:13: ( ( PLUS | MINUS | BIT_NOT ) factor | power )
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if LA58_0 in {BIT_NOT, MINUS, PLUS}:
                    alt58 = 1
                elif LA58_0 in {
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
                    alt58 = 2
                else:
                    nvae = NoViableAltException("", 58, 0, self.input)

                    raise nvae

                if alt58 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:15: ( PLUS | MINUS | BIT_NOT ) factor
                    pass
                    if self.input.LA(1) in {BIT_NOT, MINUS, PLUS}:
                        self.input.consume()
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse

                    self._state.following.append(self.FOLLOW_factor_in_factor1276)
                    self.factor()

                    self._state.following.pop()

                elif alt58 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:115:49: power
                    pass
                    self._state.following.append(self.FOLLOW_power_in_factor1280)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:1: power : atom_expr ( POWER factor )? ;
    def power(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:13: ( atom_expr ( POWER factor )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:15: atom_expr ( POWER factor )?
                pass
                self._state.following.append(self.FOLLOW_atom_expr_in_power1293)
                self.atom_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:25: ( POWER factor )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if LA59_0 == POWER:
                    alt59 = 1
                if alt59 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:116:26: POWER factor
                    pass
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power1296)

                    self._state.following.append(self.FOLLOW_factor_in_power1298)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:1: atom_expr : atom ( trailer )* ;
    def atom_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:13: ( atom ( trailer )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:15: atom ( trailer )*
                pass
                self._state.following.append(self.FOLLOW_atom_in_atom_expr1309)
                self.atom()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:20: ( trailer )*
                while True:  # loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if LA60_0 in {DOT, LBRACK}:
                        alt60 = 1

                    if alt60 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:117:20: trailer
                        pass
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr1311
                        )
                        self.trailer()

                        self._state.following.pop()

                    else:
                        break  # loop60

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "atom_expr"

    # $ANTLR start "atom"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:1: atom : ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE );
    def atom(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:119:5: ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE )
                alt67 = 13
                LA67 = self.input.LA(1)
                if LA67 in {LPAREN}:
                    alt67 = 1
                elif LA67 in {LBRACK}:
                    alt67 = 2
                elif LA67 in {LT}:
                    alt67 = 3
                elif LA67 in {LBRACE}:
                    alt67 = 4
                elif LA67 in {ID, UNDERSCORE}:
                    alt67 = 5
                elif LA67 in {SETTING_ID}:
                    alt67 = 6
                elif LA67 in {CHOICE, LOG_UNIFORM, NORMAL, SEQUENCE, UNIFORM}:
                    alt67 = 7
                elif LA67 in {INTEGER}:
                    alt67 = 8
                elif LA67 in {FLOAT_NUMBER}:
                    alt67 = 9
                elif LA67 in {STRING}:
                    alt67 = 10
                elif LA67 in {NONE}:
                    alt67 = 11
                elif LA67 in {TRUE}:
                    alt67 = 12
                elif LA67 in {FALSE}:
                    alt67 = 13
                else:
                    nvae = NoViableAltException("", 67, 0, self.input)

                    raise nvae

                if alt67 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:120:3: LPAREN test RPAREN
                    pass
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1321)

                    self._state.following.append(self.FOLLOW_test_in_atom1323)
                    self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1325)

                elif alt67 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:5: LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK
                    pass
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom1331)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:12: ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) )
                    alt64 = 2
                    LA64 = self.input.LA(1)
                    if LA64 in {
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
                        alt64 = 1
                    elif LA64 in {MINUS}:
                        LA64_2 = self.input.LA(2)

                        if LA64_2 in {
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
                            alt64 = 1
                        elif LA64_2 == INTEGER:
                            LA64_4 = self.input.LA(3)

                            if LA64_4 == RANGE:
                                alt64 = 2
                            elif LA64_4 in {
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
                                alt64 = 1
                            else:
                                nvae = NoViableAltException("", 64, 4, self.input)

                                raise nvae

                        else:
                            nvae = NoViableAltException("", 64, 2, self.input)

                            raise nvae

                    elif LA64 in {INTEGER}:
                        LA64_3 = self.input.LA(2)

                        if LA64_3 == RANGE:
                            alt64 = 2
                        elif LA64_3 in {
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
                            alt64 = 1
                        else:
                            nvae = NoViableAltException("", 64, 3, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 64, 0, self.input)

                        raise nvae

                    if alt64 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:13: ( testlist_comp )?
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:13: ( testlist_comp )?
                        alt61 = 2
                        LA61_0 = self.input.LA(1)

                        if LA61_0 in {
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
                            alt61 = 1
                        if alt61 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:13: testlist_comp
                            pass
                            self._state.following.append(
                                self.FOLLOW_testlist_comp_in_atom1334
                            )
                            self.testlist_comp()

                            self._state.following.pop()

                    elif alt64 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:30: ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER )
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:30: ( ( MINUS )? INTEGER )
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:31: ( MINUS )? INTEGER
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:31: ( MINUS )?
                        alt62 = 2
                        LA62_0 = self.input.LA(1)

                        if LA62_0 == MINUS:
                            alt62 = 1
                        if alt62 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:31: MINUS
                            pass
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1340)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1343)

                        self.match(self.input, RANGE, self.FOLLOW_RANGE_in_atom1346)

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:53: ( ( MINUS )? INTEGER )
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:54: ( MINUS )? INTEGER
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:54: ( MINUS )?
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if LA63_0 == MINUS:
                            alt63 = 1
                        if alt63 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:121:54: MINUS
                            pass
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1349)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1352)

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom1356)

                elif alt67 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:5: LT ( vector_comp )? GT
                    pass
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom1362)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:8: ( vector_comp )?
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if LA65_0 in {
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
                        alt65 = 1
                    if alt65 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:122:8: vector_comp
                        pass
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom1364
                        )
                        self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom1367)

                elif alt67 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:5: LBRACE ( dict_or_set_maker )? RBRACE
                    pass
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom1373)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:12: ( dict_or_set_maker )?
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if LA66_0 in {
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
                        alt66 = 1
                    if alt66 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:123:12: dict_or_set_maker
                        pass
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom1375
                        )
                        self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom1378)

                elif alt67 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:124:5: name
                    pass
                    self._state.following.append(self.FOLLOW_name_in_atom1384)
                    self.name()

                    self._state.following.pop()

                elif alt67 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:124:12: SETTING_ID
                    pass
                    self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom1388
                    )

                elif alt67 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:124:25: distribution_expr
                    pass
                    self._state.following.append(
                        self.FOLLOW_distribution_expr_in_atom1392
                    )
                    self.distribution_expr()

                    self._state.following.pop()

                elif alt67 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:5: INTEGER
                    pass
                    self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1398)

                elif alt67 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:15: FLOAT_NUMBER
                    pass
                    self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom1402
                    )

                elif alt67 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:30: STRING
                    pass
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_atom1406)

                elif alt67 == 11:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:39: NONE
                    pass
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom1410)

                elif alt67 == 12:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:46: TRUE
                    pass
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom1414)

                elif alt67 == 13:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:125:53: FALSE
                    pass
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom1418)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "atom"

    # $ANTLR start "name"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:1: name : ( ID | UNDERSCORE );
    def name(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:5: ( ID | UNDERSCORE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                pass
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

    # $ANTLR start "primitives"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:1: primitives : ( SHAPES | ( STEREO )? CAMERA | LIGHT | MATERIAL );
    def primitives(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:12: ( SHAPES | ( STEREO )? CAMERA | LIGHT | MATERIAL )
                alt69 = 4
                LA69 = self.input.LA(1)
                if LA69 in {SHAPES}:
                    alt69 = 1
                elif LA69 in {CAMERA, STEREO}:
                    alt69 = 2
                elif LA69 in {LIGHT}:
                    alt69 = 3
                elif LA69 in {MATERIAL}:
                    alt69 = 4
                else:
                    nvae = NoViableAltException("", 69, 0, self.input)

                    raise nvae

                if alt69 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:14: SHAPES
                    pass
                    self.match(self.input, SHAPES, self.FOLLOW_SHAPES_in_primitives1447)

                elif alt69 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:23: ( STEREO )? CAMERA
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:23: ( STEREO )?
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if LA68_0 == STEREO:
                        alt68 = 1
                    if alt68 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:23: STEREO
                        pass
                        self.match(
                            self.input, STEREO, self.FOLLOW_STEREO_in_primitives1451
                        )

                    self.match(self.input, CAMERA, self.FOLLOW_CAMERA_in_primitives1454)

                elif alt69 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:40: LIGHT
                    pass
                    self.match(self.input, LIGHT, self.FOLLOW_LIGHT_in_primitives1458)

                elif alt69 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:48: MATERIAL
                    pass
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_primitives1462
                    )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "primitives"

    # $ANTLR start "distribution_expr"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:143:1: distribution_expr : distribution LPAREN arglist RPAREN ;
    def distribution_expr(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:143:19: ( distribution LPAREN arglist RPAREN )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:143:21: distribution LPAREN arglist RPAREN
                pass
                self._state.following.append(
                    self.FOLLOW_distribution_in_distribution_expr1470
                )
                self.distribution()

                self._state.following.pop()

                self.match(
                    self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution_expr1472
                )

                self._state.following.append(
                    self.FOLLOW_arglist_in_distribution_expr1474
                )
                self.arglist()

                self._state.following.pop()

                self.match(
                    self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution_expr1476
                )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "distribution_expr"

    # $ANTLR start "distribution"
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:144:1: distribution : ( UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM );
    def distribution(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:144:19: ( UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:
                pass
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:1: testlist_comp : test ( comp_for | ( COMMA test )* ) ;
    def testlist_comp(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:15: ( test ( comp_for | ( COMMA test )* ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:17: test ( comp_for | ( COMMA test )* )
                pass
                self._state.following.append(self.FOLLOW_test_in_testlist_comp1512)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:22: ( comp_for | ( COMMA test )* )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:24: comp_for
                    pass
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp1516
                    )
                    self.comp_for()

                    self._state.following.pop()

                elif alt71 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:35: ( COMMA test )*
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:35: ( COMMA test )*
                    while True:  # loop70
                        alt70 = 2
                        LA70_0 = self.input.LA(1)

                        if LA70_0 == COMMA:
                            alt70 = 1

                        if alt70 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:36: COMMA test
                            pass
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp1521,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp1523
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:1: vector_comp : expr COMMA expr COMMA expr ;
    def vector_comp(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:15: ( expr COMMA expr COMMA expr )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:17: expr COMMA expr COMMA expr
                pass
                self._state.following.append(self.FOLLOW_expr_in_vector_comp1535)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1537)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1539)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1541)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1543)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:1: trailer : ( LBRACK subscriptlist RBRACK | DOT name );
    def trailer(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:15: ( LBRACK subscriptlist RBRACK | DOT name )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:17: LBRACK subscriptlist RBRACK
                    pass
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer1559)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer1561
                    )
                    self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer1563)

                elif alt72 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:149:47: DOT name
                    pass
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer1567)

                    self._state.following.append(self.FOLLOW_name_in_trailer1569)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:1: arglist : argument ( COMMA argument )* ;
    def arglist(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:15: ( argument ( COMMA argument )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:17: argument ( COMMA argument )*
                pass
                self._state.following.append(self.FOLLOW_argument_in_arglist1582)
                self.argument()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:26: ( COMMA argument )*
                while True:  # loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if LA73_0 == COMMA:
                        alt73 = 1

                    if alt73 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:150:27: COMMA argument
                        pass
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist1585)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist1587
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:1: argument : test ( comp_for | ASSIGN test )? ;
    def argument(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:15: ( test ( comp_for | ASSIGN test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:17: test ( comp_for | ASSIGN test )?
                pass
                self._state.following.append(self.FOLLOW_test_in_argument1601)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:22: ( comp_for | ASSIGN test )?
                alt74 = 3
                LA74_0 = self.input.LA(1)

                if LA74_0 == FOR:
                    alt74 = 1
                elif LA74_0 == ASSIGN:
                    alt74 = 2
                if alt74 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:23: comp_for
                    pass
                    self._state.following.append(self.FOLLOW_comp_for_in_argument1604)
                    self.comp_for()

                    self._state.following.pop()

                elif alt74 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:151:34: ASSIGN test
                    pass
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument1608)

                    self._state.following.append(self.FOLLOW_test_in_argument1610)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:1: subscriptlist : subscript_ ( COMMA subscript_ )* ;
    def subscriptlist(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:15: ( subscript_ ( COMMA subscript_ )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:17: subscript_ ( COMMA subscript_ )*
                pass
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist1619
                )
                self.subscript_()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:28: ( COMMA subscript_ )*
                while True:  # loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if LA75_0 == COMMA:
                        alt75 = 1

                    if alt75 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:152:29: COMMA subscript_
                        pass
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist1622
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist1624
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:1: subscript_ : ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? );
    def subscript_(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:15: ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:17: test ( COLON ( test )? ( sliceop )? )?
                    pass
                    self._state.following.append(self.FOLLOW_test_in_subscript_1636)
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:22: ( COLON ( test )? ( sliceop )? )?
                    alt78 = 2
                    LA78_0 = self.input.LA(1)

                    if LA78_0 == COLON:
                        alt78 = 1
                    if alt78 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:23: COLON ( test )? ( sliceop )?
                        pass
                        self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_1639
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:29: ( test )?
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:30: test
                            pass
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_1642
                            )
                            self.test()

                            self._state.following.pop()

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:37: ( sliceop )?
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if LA77_0 == COLON:
                            alt77 = 1
                        if alt77 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:38: sliceop
                            pass
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_1647
                            )
                            self.sliceop()

                            self._state.following.pop()

                elif alt81 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:52: COLON ( test )? ( sliceop )?
                    pass
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript_1655)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:58: ( test )?
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:59: test
                        pass
                        self._state.following.append(self.FOLLOW_test_in_subscript_1658)
                        self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:66: ( sliceop )?
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if LA80_0 == COLON:
                        alt80 = 1
                    if alt80 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:153:67: sliceop
                        pass
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_1663
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:1: sliceop : COLON ( test )? ;
    def sliceop(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:15: ( COLON ( test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:17: COLON ( test )?
                pass
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop1678)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:23: ( test )?
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:154:23: test
                    pass
                    self._state.following.append(self.FOLLOW_test_in_sliceop1680)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:1: exprlist : expr ( COMMA expr )* ;
    def exprlist(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:10: ( expr ( COMMA expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:12: expr ( COMMA expr )*
                pass
                self._state.following.append(self.FOLLOW_expr_in_exprlist1689)
                self.expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:17: ( COMMA expr )*
                while True:  # loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if LA83_0 == COMMA:
                        alt83 = 1

                    if alt83 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:156:18: COMMA expr
                        pass
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist1692)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist1694)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:157:1: testlist : test ( COMMA test )* ;
    def testlist(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:157:10: ( test ( COMMA test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:157:12: test ( COMMA test )*
                pass
                self._state.following.append(self.FOLLOW_test_in_testlist1703)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:157:17: ( COMMA test )*
                while True:  # loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if LA84_0 == COMMA:
                        alt84 = 1

                    if alt84 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:157:18: COMMA test
                        pass
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist1706)

                        self._state.following.append(self.FOLLOW_test_in_testlist1708)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:158:1: dict_or_set_maker : test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) ;
    def dict_or_set_maker(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:158:18: ( test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:3: test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                pass
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker1718)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:8: ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:10: COLON test ( comp_for | ( COMMA test COLON test )* )
                    pass
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker1722
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker1724
                    )
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:21: ( comp_for | ( COMMA test COLON test )* )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:22: comp_for
                        pass
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1727
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt86 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:33: ( COMMA test COLON test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:33: ( COMMA test COLON test )*
                        while True:  # loop85
                            alt85 = 2
                            LA85_0 = self.input.LA(1)

                            if LA85_0 == COMMA:
                                alt85 = 1

                            if alt85 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:159:34: COMMA test COLON test
                                pass
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker1732,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1734
                                )
                                self.test()

                                self._state.following.pop()

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker1736,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1738
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop85

                elif alt89 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:10: ( comp_for | ( COMMA test )* )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:10: ( comp_for | ( COMMA test )* )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:11: comp_for
                        pass
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1753
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt88 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:22: ( COMMA test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:22: ( COMMA test )*
                        while True:  # loop87
                            alt87 = 2
                            LA87_0 = self.input.LA(1)

                            if LA87_0 == COMMA:
                                alt87 = 1

                            if alt87 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:160:23: COMMA test
                                pass
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker1758,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1760
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:163:1: comp_iter : ( comp_for | comp_if );
    def comp_iter(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:163:11: ( comp_for | comp_if )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:163:13: comp_for
                    pass
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter1774)
                    self.comp_for()

                    self._state.following.pop()

                elif alt90 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:163:24: comp_if
                    pass
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter1778)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:1: comp_for : FOR exprlist IN or_test ( comp_iter )? ;
    def comp_for(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:11: ( FOR exprlist IN or_test ( comp_iter )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:13: FOR exprlist IN or_test ( comp_iter )?
                pass
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for1786)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for1788)
                self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for1790)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for1792)
                self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:37: ( comp_iter )?
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if LA91_0 in {FOR, IF}:
                    alt91 = 1
                if alt91 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:164:37: comp_iter
                    pass
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for1794)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:1: comp_if : IF test_nocond ( comp_iter )? ;
    def comp_if(
        self,
    ):
        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:11: ( IF test_nocond ( comp_iter )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:13: IF test_nocond ( comp_iter )?
                pass
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if1804)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if1806)
                self.test_nocond()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:28: ( comp_iter )?
                alt92 = 2
                LA92_0 = self.input.LA(1)

                if LA92_0 in {FOR, IF}:
                    alt92 = 1
                if alt92 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:165:28: comp_iter
                    pass
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if1808)
                    self.comp_iter()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comp_if"

    FOLLOW_declaration_in_scenario35 = frozenset([1, 79, 110, 118, 134])
    FOLLOW_NEWLINE_in_scenario37 = frozenset([1, 79, 110, 118, 134])
    FOLLOW_settings_in_scenario40 = frozenset([1, 118, 134])
    FOLLOW_stage_in_scenario43 = frozenset([1, 134])
    FOLLOW_writers_in_scenario46 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration56 = frozenset([47, 129])
    FOLLOW_name_in_declaration58 = frozenset([18, 79])
    FOLLOW_COLON_in_declaration61 = frozenset([47, 129])
    FOLLOW_name_in_declaration63 = frozenset([79])
    FOLLOW_NEWLINE_in_declaration67 = frozenset([1])
    FOLLOW_SETTINGS_in_settings77 = frozenset([18])
    FOLLOW_COLON_in_settings79 = frozenset([79])
    FOLLOW_NEWLINE_in_settings81 = frozenset([54])
    FOLLOW_INDENT_in_settings83 = frozenset([47])
    FOLLOW_option_in_settings85 = frozenset([22, 47])
    FOLLOW_DEDENT_in_settings88 = frozenset([1])
    FOLLOW_STAGE_in_stage101 = frozenset([18])
    FOLLOW_COLON_in_stage103 = frozenset([79])
    FOLLOW_NEWLINE_in_stage105 = frozenset([54])
    FOLLOW_INDENT_in_stage107 = frozenset(
        [
            13,
            17,
            21,
            28,
            32,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            87,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_stmts_in_stage109 = frozenset([22])
    FOLLOW_DEDENT_in_stage111 = frozenset([1])
    FOLLOW_WRITERS_in_writers122 = frozenset([18])
    FOLLOW_COLON_in_writers124 = frozenset([79])
    FOLLOW_NEWLINE_in_writers126 = frozenset([54])
    FOLLOW_INDENT_in_writers128 = frozenset(
        [
            13,
            17,
            35,
            36,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_expr_stmt_in_writers131 = frozenset(
        [
            13,
            17,
            22,
            35,
            36,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_writer_in_writers135 = frozenset(
        [
            13,
            17,
            22,
            35,
            36,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_DEDENT_in_writers139 = frozenset([1])
    FOLLOW_ID_in_option147 = frozenset([8])
    FOLLOW_ASSIGN_in_option149 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_option151 = frozenset([79])
    FOLLOW_NEWLINE_in_option153 = frozenset([1])
    FOLLOW_open_stmt_in_stmts161 = frozenset(
        [
            13,
            17,
            21,
            28,
            32,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_aug_expr_stmt_in_stmts165 = frozenset(
        [
            1,
            13,
            17,
            21,
            28,
            32,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_edit_stmt_in_stmts169 = frozenset(
        [
            1,
            13,
            17,
            21,
            28,
            32,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_behavior_stmt_in_stmts173 = frozenset(
        [
            1,
            13,
            17,
            21,
            28,
            32,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_ID_in_writer182 = frozenset([18])
    FOLLOW_COLON_in_writer184 = frozenset([79])
    FOLLOW_NEWLINE_in_writer186 = frozenset([54])
    FOLLOW_INDENT_in_writer188 = frozenset([47])
    FOLLOW_option_in_writer190 = frozenset([22, 47])
    FOLLOW_DEDENT_in_writer193 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt205 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_open_stmt207 = frozenset([79])
    FOLLOW_NEWLINE_in_open_stmt209 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt216 = frozenset([47, 125, 129])
    FOLLOW_TIMELINE_in_edit_stmt219 = frozenset([18])
    FOLLOW_name_in_edit_stmt223 = frozenset([18])
    FOLLOW_edit_block_in_edit_stmt226 = frozenset([1])
    FOLLOW_CREATE_in_create_expr235 = frozenset(
        [
            13,
            15,
            17,
            35,
            37,
            41,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            72,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            112,
            119,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_create_expr237 = frozenset([15, 41, 47, 72, 112, 119, 129])
    FOLLOW_STEREO_in_create_expr247 = frozenset([15])
    FOLLOW_CAMERA_in_create_expr250 = frozenset([18, 79])
    FOLLOW_SHAPES_in_create_expr254 = frozenset([18, 79])
    FOLLOW_name_in_create_expr258 = frozenset([62])
    FOLLOW_LIGHT_in_create_expr260 = frozenset([18, 79])
    FOLLOW_FROM_in_create_expr264 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_create_expr266 = frozenset([18, 79])
    FOLLOW_edit_block_in_create_expr270 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr274 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr283 = frozenset([18])
    FOLLOW_simple_block_in_create_expr286 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr300 = frozenset(
        [
            13,
            17,
            35,
            37,
            41,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_instantiate_expr303 = frozenset([41])
    FOLLOW_FROM_in_instantiate_expr307 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_instantiate_expr309 = frozenset([18, 79])
    FOLLOW_edit_block_in_instantiate_expr312 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr316 = frozenset([1])
    FOLLOW_GROUP_in_group_expr330 = frozenset([60])
    FOLLOW_LBRACK_in_group_expr332 = frozenset([47, 129])
    FOLLOW_name_in_group_expr334 = frozenset([19, 97])
    FOLLOW_COMMA_in_group_expr337 = frozenset([47, 129])
    FOLLOW_name_in_group_expr339 = frozenset([19, 97])
    FOLLOW_RBRACK_in_group_expr343 = frozenset([18, 79])
    FOLLOW_edit_block_in_group_expr346 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr350 = frozenset([1])
    FOLLOW_GET_in_get_expr358 = frozenset(
        [
            13,
            15,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            62,
            64,
            66,
            69,
            72,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_CAMERA_in_get_expr362 = frozenset([9])
    FOLLOW_LIGHT_in_get_expr366 = frozenset([9])
    FOLLOW_MATERIAL_in_get_expr370 = frozenset([9])
    FOLLOW_name_in_get_expr374 = frozenset([9])
    FOLLOW_AT_in_get_expr377 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_get_expr381 = frozenset([18, 79])
    FOLLOW_simple_block_in_get_expr384 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr388 = frozenset([1])
    FOLLOW_COLON_in_edit_block399 = frozenset([79])
    FOLLOW_NEWLINE_in_edit_block401 = frozenset([54])
    FOLLOW_INDENT_in_edit_block403 = frozenset(
        [16, 32, 47, 65, 99, 103, 104, 107, 114, 127, 129, 132, 133]
    )
    FOLLOW_attr_in_edit_block406 = frozenset(
        [16, 22, 32, 47, 65, 99, 103, 104, 107, 114, 127, 129, 132, 133]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block410 = frozenset(
        [16, 22, 32, 47, 65, 99, 103, 104, 107, 114, 127, 129, 132, 133]
    )
    FOLLOW_DEDENT_in_edit_block414 = frozenset([1])
    FOLLOW_COLON_in_simple_block421 = frozenset([79])
    FOLLOW_NEWLINE_in_simple_block423 = frozenset([54])
    FOLLOW_INDENT_in_simple_block425 = frozenset([47, 129])
    FOLLOW_simple_attr_in_simple_block427 = frozenset([22, 47, 129])
    FOLLOW_DEDENT_in_simple_block430 = frozenset([1])
    FOLLOW_core_attr_in_attr447 = frozenset([1])
    FOLLOW_simple_attr_in_attr451 = frozenset([1])
    FOLLOW_compound_attr_in_attr455 = frozenset([1])
    FOLLOW_name_in_simple_attr464 = frozenset(
        [
            13,
            17,
            18,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            79,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_COLON_in_simple_attr467 = frozenset([47, 129])
    FOLLOW_name_in_simple_attr469 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            79,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_simple_attr473 = frozenset([79])
    FOLLOW_NEWLINE_in_simple_attr476 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr484 = frozenset([79])
    FOLLOW_NEWLINE_in_compound_attr486 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr503 = frozenset([10, 126])
    FOLLOW_AXIS_in_core_attr505 = frozenset([126])
    FOLLOW_TO_in_core_attr508 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr510 = frozenset([79])
    FOLLOW_CAM_TRANSLATE_in_core_attr518 = frozenset([126])
    FOLLOW_TO_in_core_attr520 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr522 = frozenset([79])
    FOLLOW_ROTATE_in_core_attr530 = frozenset(
        [
            10,
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_AXIS_in_core_attr532 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr535 = frozenset([79, 89])
    FOLLOW_ORDER_in_core_attr537 = frozenset([79])
    FOLLOW_SCALE_in_core_attr546 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr548 = frozenset([79])
    FOLLOW_LOOK_AT_in_core_attr556 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr558 = frozenset([79])
    FOLLOW_UP_AXIS_in_core_attr566 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr568 = frozenset([79])
    FOLLOW_SIZE_in_core_attr576 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr578 = frozenset([79])
    FOLLOW_SEMANTICS_in_core_attr586 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr588 = frozenset([79])
    FOLLOW_VISIBLE_in_core_attr596 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_core_attr598 = frozenset([79])
    FOLLOW_NEWLINE_in_core_attr604 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt614 = frozenset([18])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt616 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block623 = frozenset([79])
    FOLLOW_NEWLINE_in_inner_behavior_block625 = frozenset([54])
    FOLLOW_INDENT_in_inner_behavior_block627 = frozenset(
        [16, 47, 65, 99, 103, 104, 107, 114, 127, 129, 132, 133]
    )
    FOLLOW_attr_in_inner_behavior_block629 = frozenset(
        [16, 22, 47, 65, 99, 103, 104, 107, 114, 127, 129, 132, 133]
    )
    FOLLOW_DEDENT_in_inner_behavior_block632 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt643 = frozenset([18])
    FOLLOW_behavior_block_in_behavior_stmt645 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr653 = frozenset(
        [
            13,
            17,
            35,
            37,
            40,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            124,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_behavior_expr655 = frozenset([40, 124])
    FOLLOW_set_in_behavior_expr658 = frozenset([1])
    FOLLOW_COLON_in_behavior_block671 = frozenset([79])
    FOLLOW_NEWLINE_in_behavior_block673 = frozenset([54])
    FOLLOW_INDENT_in_behavior_block675 = frozenset(
        [
            13,
            17,
            21,
            28,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_aug_expr_stmt_in_behavior_block678 = frozenset(
        [
            13,
            17,
            21,
            22,
            28,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_edit_stmt_in_behavior_block682 = frozenset(
        [
            13,
            17,
            21,
            22,
            28,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_DEDENT_in_behavior_block686 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt701 = frozenset(
        [4, 6, 8, 26, 49, 68, 75, 77, 79, 90, 94, 102, 122, 136]
    )
    FOLLOW_aug_assign_in_expr_stmt705 = frozenset(
        [
            13,
            17,
            35,
            36,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_ASSIGN_in_expr_stmt709 = frozenset(
        [
            13,
            17,
            35,
            36,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_testlist_in_expr_stmt713 = frozenset([79])
    FOLLOW_fetch_expr_in_expr_stmt717 = frozenset([79])
    FOLLOW_fetch_expr_in_expr_stmt728 = frozenset([79])
    FOLLOW_NEWLINE_in_expr_stmt734 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt746 = frozenset(
        [4, 6, 8, 26, 49, 68, 75, 77, 79, 90, 94, 102, 122, 136]
    )
    FOLLOW_NEWLINE_in_aug_expr_stmt756 = frozenset([1])
    FOLLOW_aug_assign_in_aug_expr_stmt766 = frozenset(
        [
            13,
            17,
            35,
            36,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            79,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt769 = frozenset([79])
    FOLLOW_fetch_expr_in_aug_expr_stmt773 = frozenset([79])
    FOLLOW_NEWLINE_in_aug_expr_stmt777 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt787 = frozenset(
        [
            13,
            17,
            21,
            35,
            36,
            37,
            42,
            43,
            47,
            55,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt800 = frozenset([79])
    FOLLOW_fetch_expr_in_aug_expr_stmt804 = frozenset([79])
    FOLLOW_NEWLINE_in_aug_expr_stmt807 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt819 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt823 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt827 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt831 = frozenset([1])
    FOLLOW_fetch_expr_in_aug_expr_stmt851 = frozenset([79])
    FOLLOW_NEWLINE_in_aug_expr_stmt853 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt859 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt863 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt867 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt871 = frozenset([1])
    FOLLOW_FETCH_in_fetch_expr880 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_fetch_expr882 = frozenset([41])
    FOLLOW_FROM_in_fetch_expr884 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_fetch_expr886 = frozenset([1, 71])
    FOLLOW_MATCH_in_fetch_expr889 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_fetch_expr891 = frozenset([1])
    FOLLOW_or_test_in_test985 = frozenset([1, 52])
    FOLLOW_IF_in_test988 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_or_test_in_test990 = frozenset([30])
    FOLLOW_ELSE_in_test992 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_test994 = frozenset([1])
    FOLLOW_or_test_in_test_nocond1003 = frozenset([1])
    FOLLOW_and_test_in_or_test1014 = frozenset([1, 88])
    FOLLOW_OR_in_or_test1017 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_and_test_in_or_test1019 = frozenset([1, 88])
    FOLLOW_not_test_in_and_test1031 = frozenset([1, 5])
    FOLLOW_AND_in_and_test1034 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_not_test_in_and_test1036 = frozenset([1, 5])
    FOLLOW_NOT_in_not_test1048 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_not_test_in_not_test1050 = frozenset([1])
    FOLLOW_comparison_in_not_test1054 = frozenset([1])
    FOLLOW_expr_in_comparison1062 = frozenset([1, 31, 44, 45, 53, 58, 69, 70, 83, 84])
    FOLLOW_comp_op_in_comparison1065 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_expr_in_comparison1067 = frozenset([1, 31, 44, 45, 53, 58, 69, 70, 83, 84])
    FOLLOW_LT_in_comp_op1080 = frozenset([1])
    FOLLOW_GT_in_comp_op1084 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op1088 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op1092 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op1096 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op1100 = frozenset([1])
    FOLLOW_IN_in_comp_op1104 = frozenset([1])
    FOLLOW_NOT_in_comp_op1108 = frozenset([53])
    FOLLOW_IN_in_comp_op1110 = frozenset([1])
    FOLLOW_IS_in_comp_op1114 = frozenset([1])
    FOLLOW_IS_in_comp_op1118 = frozenset([83])
    FOLLOW_NOT_in_comp_op1120 = frozenset([1])
    FOLLOW_xor_expr_in_expr1134 = frozenset([1, 14])
    FOLLOW_BIT_OR_in_expr1137 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_xor_expr_in_expr1139 = frozenset([1, 14])
    FOLLOW_and_expr_in_xor_expr1151 = frozenset([1, 135])
    FOLLOW_XOR_in_xor_expr1154 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_and_expr_in_xor_expr1156 = frozenset([1, 135])
    FOLLOW_shift_expr_in_and_expr1168 = frozenset([1, 12])
    FOLLOW_BIT_AND_in_and_expr1171 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_shift_expr_in_and_expr1173 = frozenset([1, 12])
    FOLLOW_arith_expr_in_shift_expr1183 = frozenset([1, 67, 101])
    FOLLOW_set_in_shift_expr1186 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_arith_expr_in_shift_expr1194 = frozenset([1, 67, 101])
    FOLLOW_term_in_arith_expr1204 = frozenset([1, 73, 91])
    FOLLOW_set_in_arith_expr1207 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_term_in_arith_expr1215 = frozenset([1, 73, 91])
    FOLLOW_factor_in_term1231 = frozenset([1, 25, 48, 74, 76])
    FOLLOW_set_in_term1234 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_factor_in_term1250 = frozenset([1, 25, 48, 74, 76])
    FOLLOW_set_in_factor1264 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_factor_in_factor1276 = frozenset([1])
    FOLLOW_power_in_factor1280 = frozenset([1])
    FOLLOW_atom_expr_in_power1293 = frozenset([1, 93])
    FOLLOW_POWER_in_power1296 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_factor_in_power1298 = frozenset([1])
    FOLLOW_atom_in_atom_expr1309 = frozenset([1, 27, 60])
    FOLLOW_trailer_in_atom_expr1311 = frozenset([1, 27, 60])
    FOLLOW_LPAREN_in_atom1321 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_atom1323 = frozenset([100])
    FOLLOW_RPAREN_in_atom1325 = frozenset([1])
    FOLLOW_LBRACK_in_atom1331 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            97,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_testlist_comp_in_atom1334 = frozenset([97])
    FOLLOW_MINUS_in_atom1340 = frozenset([56])
    FOLLOW_INTEGER_in_atom1343 = frozenset([95])
    FOLLOW_RANGE_in_atom1346 = frozenset([56, 73])
    FOLLOW_MINUS_in_atom1349 = frozenset([56])
    FOLLOW_INTEGER_in_atom1352 = frozenset([97])
    FOLLOW_RBRACK_in_atom1356 = frozenset([1])
    FOLLOW_LT_in_atom1362 = frozenset(
        [
            13,
            17,
            35,
            37,
            44,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_vector_comp_in_atom1364 = frozenset([44])
    FOLLOW_GT_in_atom1367 = frozenset([1])
    FOLLOW_LBRACE_in_atom1373 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            96,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_dict_or_set_maker_in_atom1375 = frozenset([96])
    FOLLOW_RBRACE_in_atom1378 = frozenset([1])
    FOLLOW_name_in_atom1384 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom1388 = frozenset([1])
    FOLLOW_distribution_expr_in_atom1392 = frozenset([1])
    FOLLOW_INTEGER_in_atom1398 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom1402 = frozenset([1])
    FOLLOW_STRING_in_atom1406 = frozenset([1])
    FOLLOW_NONE_in_atom1410 = frozenset([1])
    FOLLOW_TRUE_in_atom1414 = frozenset([1])
    FOLLOW_FALSE_in_atom1418 = frozenset([1])
    FOLLOW_SHAPES_in_primitives1447 = frozenset([1])
    FOLLOW_STEREO_in_primitives1451 = frozenset([15])
    FOLLOW_CAMERA_in_primitives1454 = frozenset([1])
    FOLLOW_LIGHT_in_primitives1458 = frozenset([1])
    FOLLOW_MATERIAL_in_primitives1462 = frozenset([1])
    FOLLOW_distribution_in_distribution_expr1470 = frozenset([66])
    FOLLOW_LPAREN_in_distribution_expr1472 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_arglist_in_distribution_expr1474 = frozenset([100])
    FOLLOW_RPAREN_in_distribution_expr1476 = frozenset([1])
    FOLLOW_test_in_testlist_comp1512 = frozenset([1, 19, 38])
    FOLLOW_comp_for_in_testlist_comp1516 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp1521 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_testlist_comp1523 = frozenset([1, 19])
    FOLLOW_expr_in_vector_comp1535 = frozenset([19])
    FOLLOW_COMMA_in_vector_comp1537 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_expr_in_vector_comp1539 = frozenset([19])
    FOLLOW_COMMA_in_vector_comp1541 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_expr_in_vector_comp1543 = frozenset([1])
    FOLLOW_LBRACK_in_trailer1559 = frozenset(
        [
            13,
            17,
            18,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_subscriptlist_in_trailer1561 = frozenset([97])
    FOLLOW_RBRACK_in_trailer1563 = frozenset([1])
    FOLLOW_DOT_in_trailer1567 = frozenset([47, 129])
    FOLLOW_name_in_trailer1569 = frozenset([1])
    FOLLOW_argument_in_arglist1582 = frozenset([1, 19])
    FOLLOW_COMMA_in_arglist1585 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_argument_in_arglist1587 = frozenset([1, 19])
    FOLLOW_test_in_argument1601 = frozenset([1, 8, 38])
    FOLLOW_comp_for_in_argument1604 = frozenset([1])
    FOLLOW_ASSIGN_in_argument1608 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_argument1610 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist1619 = frozenset([1, 19])
    FOLLOW_COMMA_in_subscriptlist1622 = frozenset(
        [
            13,
            17,
            18,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_subscript__in_subscriptlist1624 = frozenset([1, 19])
    FOLLOW_test_in_subscript_1636 = frozenset([1, 18])
    FOLLOW_COLON_in_subscript_1639 = frozenset(
        [
            1,
            13,
            17,
            18,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_subscript_1642 = frozenset([1, 18])
    FOLLOW_sliceop_in_subscript_1647 = frozenset([1])
    FOLLOW_COLON_in_subscript_1655 = frozenset(
        [
            1,
            13,
            17,
            18,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_subscript_1658 = frozenset([1, 18])
    FOLLOW_sliceop_in_subscript_1663 = frozenset([1])
    FOLLOW_COLON_in_sliceop1678 = frozenset(
        [
            1,
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_sliceop1680 = frozenset([1])
    FOLLOW_expr_in_exprlist1689 = frozenset([1, 19])
    FOLLOW_COMMA_in_exprlist1692 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_expr_in_exprlist1694 = frozenset([1, 19])
    FOLLOW_test_in_testlist1703 = frozenset([1, 19])
    FOLLOW_COMMA_in_testlist1706 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_testlist1708 = frozenset([1, 19])
    FOLLOW_test_in_dict_or_set_maker1718 = frozenset([1, 18, 19, 38])
    FOLLOW_COLON_in_dict_or_set_maker1722 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1724 = frozenset([1, 19, 38])
    FOLLOW_comp_for_in_dict_or_set_maker1727 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1732 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1734 = frozenset([18])
    FOLLOW_COLON_in_dict_or_set_maker1736 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1738 = frozenset([1, 19])
    FOLLOW_comp_for_in_dict_or_set_maker1753 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1758 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1760 = frozenset([1, 19])
    FOLLOW_comp_for_in_comp_iter1774 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter1778 = frozenset([1])
    FOLLOW_FOR_in_comp_for1786 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_exprlist_in_comp_for1788 = frozenset([53])
    FOLLOW_IN_in_comp_for1790 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_or_test_in_comp_for1792 = frozenset([1, 38, 52])
    FOLLOW_comp_iter_in_comp_for1794 = frozenset([1])
    FOLLOW_IF_in_comp_if1804 = frozenset(
        [
            13,
            17,
            35,
            37,
            47,
            56,
            59,
            60,
            64,
            66,
            69,
            73,
            80,
            82,
            83,
            91,
            109,
            111,
            120,
            128,
            129,
            130,
        ]
    )
    FOLLOW_test_nocond_in_comp_if1806 = frozenset([1, 38, 52])
    FOLLOW_comp_iter_in_comp_if1808 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
