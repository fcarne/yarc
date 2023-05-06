# $ANTLR 3.5.1 /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g 2023-05-02 23:19:08

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
CHOICE = 15
COLON = 16
COMMA = 17
COMMENT = 18
CREATE = 19
DEDENT = 20
DIGIT = 21
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
LETTER = 56
LIGHT = 57
LIGHT_TYPE = 58
LIMIT = 59
LINE_JOINING = 60
LOG_UNIFORM = 61
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
NORMAL = 76
NOT = 77
NOT_EQ = 78
OCT_DIGIT = 79
ON = 80
OPEN = 81
OR = 82
ORDER = 83
PHYSICS = 84
PLUS = 85
POINT_FLOAT = 86
POWER = 87
RANGE = 88
RBRACE = 89
RBRACK = 90
RECURSIVE = 91
ROTATE = 92
ROT_AROUND = 93
RPAREN = 94
RSHIFT = 95
SCALE = 96
SCATTER = 97
SCENARIO = 98
SEMANTICS = 99
SEMI = 100
SEQUENCE = 101
SETTINGS = 102
SETTING_ID = 103
SHAPES = 104
SHAPES_OR_LIGHTS = 105
SHORT_STRING = 106
SIZE = 107
SKIP_ = 108
SNIPPET = 109
SPACES = 110
STAGE = 111
STEREO = 112
STRING = 113
STRING_ESCAPE_SEQ = 114
TIME = 115
TIMELINE = 116
TO = 117
TRANSLATE = 118
TRUE = 119
UNDERSCORE = 120
UNIFORM = 121
UNKNOWN = 122
UP_AXIS = 123
VISIBLE = 124
WRITERS = 125
XOR = 126

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
    15: "CHOICE",
    16: "COLON",
    17: "COMMA",
    18: "COMMENT",
    19: "CREATE",
    20: "DEDENT",
    21: "DIGIT",
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
    56: "LETTER",
    57: "LIGHT",
    58: "LIGHT_TYPE",
    59: "LIMIT",
    60: "LINE_JOINING",
    61: "LOG_UNIFORM",
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
    76: "NORMAL",
    77: "NOT",
    78: "NOT_EQ",
    79: "OCT_DIGIT",
    80: "ON",
    81: "OPEN",
    82: "OR",
    83: "ORDER",
    84: "PHYSICS",
    85: "PLUS",
    86: "POINT_FLOAT",
    87: "POWER",
    88: "RANGE",
    89: "RBRACE",
    90: "RBRACK",
    91: "RECURSIVE",
    92: "ROTATE",
    93: "ROT_AROUND",
    94: "RPAREN",
    95: "RSHIFT",
    96: "SCALE",
    97: "SCATTER",
    98: "SCENARIO",
    99: "SEMANTICS",
    100: "SEMI",
    101: "SEQUENCE",
    102: "SETTINGS",
    103: "SETTING_ID",
    104: "SHAPES",
    105: "SHAPES_OR_LIGHTS",
    106: "SHORT_STRING",
    107: "SIZE",
    108: "SKIP_",
    109: "SNIPPET",
    110: "SPACES",
    111: "STAGE",
    112: "STEREO",
    113: "STRING",
    114: "STRING_ESCAPE_SEQ",
    115: "TIME",
    116: "TIMELINE",
    117: "TO",
    118: "TRANSLATE",
    119: "TRUE",
    120: "UNDERSCORE",
    121: "UNIFORM",
    122: "UNKNOWN",
    123: "UP_AXIS",
    124: "VISIBLE",
    125: "WRITERS",
    126: "XOR",
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
    "CHOICE",
    "COLON",
    "COMMA",
    "COMMENT",
    "CREATE",
    "DEDENT",
    "DIGIT",
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
    "LETTER",
    "LIGHT",
    "LIGHT_TYPE",
    "LIMIT",
    "LINE_JOINING",
    "LOG_UNIFORM",
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
    "NORMAL",
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
]


class YarcParser(Parser):
    grammarFileName = "/media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)

        self.delegates = []

    # $ANTLR start "scenario"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:1: scenario : declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? ;
    def scenario(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:10: ( declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:12: declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )?
                self._state.following.append(self.FOLLOW_declaration_in_scenario35)
                self.declaration()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:24: ( NEWLINE )*
                while True:  # loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if LA1_0 == NEWLINE:
                        alt1 = 1

                    if alt1 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:24: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario37
                        )

                    else:
                        break  # loop1

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:33: ( settings )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if LA2_0 == SETTINGS:
                    alt2 = 1
                if alt2 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:33: settings
                    self._state.following.append(self.FOLLOW_settings_in_scenario40)
                    self.settings()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:43: ( stage )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if LA3_0 == STAGE:
                    alt3 = 1
                if alt3 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:43: stage
                    self._state.following.append(self.FOLLOW_stage_in_scenario43)
                    self.stage()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:50: ( writers )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == WRITERS:
                    alt4 = 1
                if alt4 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:8:50: writers
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:10:1: declaration : SCENARIO name ( COLON name )? NEWLINE ;
    def declaration(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:10:13: ( SCENARIO name ( COLON name )? NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:10:15: SCENARIO name ( COLON name )? NEWLINE
                self.match(self.input, SCENARIO, self.FOLLOW_SCENARIO_in_declaration56)

                self._state.following.append(self.FOLLOW_name_in_declaration58)
                self.name()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:10:29: ( COLON name )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if LA5_0 == COLON:
                    alt5 = 1
                if alt5 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:10:30: COLON name
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:11:1: settings : SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT ;
    def settings(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:11:13: ( SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:11:15: SETTINGS COLON NEWLINE INDENT ( option )+ DEDENT
                self.match(self.input, SETTINGS, self.FOLLOW_SETTINGS_in_settings77)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_settings79)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_settings81)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_settings83)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:11:45: ( option )+
                cnt6 = 0
                while True:  # loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if LA6_0 == ID:
                        alt6 = 1

                    if alt6 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:11:45: option
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:12:1: stage : STAGE COLON NEWLINE INDENT stmts DEDENT ;
    def stage(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:12:13: ( STAGE COLON NEWLINE INDENT stmts DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:12:15: STAGE COLON NEWLINE INDENT stmts DEDENT
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:1: writers : WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT ;
    def writers(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:13: ( WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:15: WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT
                self.match(self.input, WRITERS, self.FOLLOW_WRITERS_in_writers122)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writers124)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writers126)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writers128)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:44: ( expr_stmt | writer )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:45: expr_stmt
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers131
                        )
                        self.expr_stmt()

                        self._state.following.pop()

                    elif alt7 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:57: writer
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:15:1: option : ID ASSIGN test NEWLINE ;
    def option(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:15:8: ( ID ASSIGN test NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:15:10: ID ASSIGN test NEWLINE
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:1: stmts : ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+ ;
    def stmts(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:8: ( ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+ )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:10: ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:10: ( open_stmt )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if LA8_0 == OPEN:
                    alt8 = 1
                if alt8 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:10: open_stmt
                    self._state.following.append(self.FOLLOW_open_stmt_in_stmts161)
                    self.open_stmt()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:21: ( aug_expr_stmt | edit_stmt | behavior_stmt )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:22: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts165
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt9 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:38: edit_stmt
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts169)
                        self.edit_stmt()

                        self._state.following.pop()

                    elif alt9 == 3:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:50: behavior_stmt
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:17:1: writer : ID COLON NEWLINE INDENT ( option )+ DEDENT ;
    def writer(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:17:8: ( ID COLON NEWLINE INDENT ( option )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:17:10: ID COLON NEWLINE INDENT ( option )+ DEDENT
                self.match(self.input, ID, self.FOLLOW_ID_in_writer182)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writer184)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer186)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writer188)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:17:34: ( option )+
                cnt10 = 0
                while True:  # loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if LA10_0 == ID:
                        alt10 = 1

                    if alt10 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:17:34: option
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:21:1: open_stmt : OPEN test NEWLINE ;
    def open_stmt(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:21:11: ( OPEN test NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:21:13: OPEN test NEWLINE
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:22:1: edit_stmt : EDIT ( TIMELINE | name ) edit_block ;
    def edit_stmt(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:22:11: ( EDIT ( TIMELINE | name ) edit_block )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:22:13: EDIT ( TIMELINE | name ) edit_block
                self.match(self.input, EDIT, self.FOLLOW_EDIT_in_edit_stmt216)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:22:18: ( TIMELINE | name )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:22:19: TIMELINE
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt219
                    )

                elif alt11 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:22:30: name
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:24:1: create_expr : CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) ;
    def create_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:24:12: ( CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:3: CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr235)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:10: ( test )?
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:10: test
                    self._state.following.append(self.FOLLOW_test_in_create_expr237)
                    self.test()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:16: ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE )
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:6: ( STEREO )? CAMERA
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:6: ( STEREO )?
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if LA13_0 == STEREO:
                            alt13 = 1
                        if alt13 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:6: STEREO
                            self.match(
                                self.input, STEREO, self.FOLLOW_STEREO_in_create_expr247
                            )

                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr250
                        )

                    elif alt14 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:23: shapes
                        self._state.following.append(
                            self.FOLLOW_shapes_in_create_expr254
                        )
                        self.shapes()

                        self._state.following.pop()

                    elif alt14 == 3:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:32: light_type LIGHT
                        self._state.following.append(
                            self.FOLLOW_light_type_in_create_expr258
                        )
                        self.light_type()

                        self._state.following.pop()

                        self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr260
                        )

                    elif alt14 == 4:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:51: FROM test
                        self.match(self.input, FROM, self.FOLLOW_FROM_in_create_expr264)

                        self._state.following.append(self.FOLLOW_test_in_create_expr266)
                        self.test()

                        self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:62: ( edit_block | NEWLINE )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:63: edit_block
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr270
                        )
                        self.edit_block()

                        self._state.following.pop()

                    elif alt15 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:26:76: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr274
                        )

                elif alt16 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:27:7: MATERIAL ( simple_block )
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr283
                    )

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:27:16: ( simple_block )
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:27:17: simple_block
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:31:1: shapes : ( SHAPES | SHAPES_OR_LIGHTS );
    def shapes(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:31:12: ( SHAPES | SHAPES_OR_LIGHTS )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:32:1: light_type : ( LIGHT_TYPE | SHAPES_OR_LIGHTS );
    def light_type(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:32:12: ( LIGHT_TYPE | SHAPES_OR_LIGHTS )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:1: instantiate_expr : INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) ;
    def instantiate_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:18: ( INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:20: INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE )
                self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr327,
                )

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:32: ( test )?
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:33: test
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr330
                    )
                    self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr334)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr336)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:50: ( edit_block | NEWLINE )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:51: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr339
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt18 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:64: NEWLINE
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:1: group_expr : GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) ;
    def group_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:18: ( GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:20: GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE )
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_expr357)

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr359)

                self._state.following.append(self.FOLLOW_name_in_group_expr361)
                self.name()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:38: ( COMMA name )*
                while True:  # loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if LA19_0 == COMMA:
                        alt19 = 1

                    if alt19 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:39: COMMA name
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_group_expr364
                        )

                        self._state.following.append(self.FOLLOW_name_in_group_expr366)
                        self.name()

                        self._state.following.pop()

                    else:
                        break  # loop19

                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_group_expr370)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:59: ( edit_block | NEWLINE )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:60: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr373
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt20 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:73: NEWLINE
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:1: get_expr : GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) ;
    def get_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:18: ( GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:20: GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE )
                self.match(self.input, GET, self.FOLLOW_GET_in_get_expr393)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:24: ( ( CAMERA | LIGHT | MATERIAL | name ) AT )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if LA22_0 in {CAMERA, LIGHT, MATERIAL}:
                    alt22 = 1
                elif LA22_0 in {ID, UNDERSCORE}:
                    LA22_2 = self.input.LA(2)

                    if LA22_2 == AT:
                        alt22 = 1
                if alt22 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:25: ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:25: ( CAMERA | LIGHT | MATERIAL | name )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:26: CAMERA
                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr397
                        )

                    elif alt21 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:35: LIGHT
                        self.match(self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr401)

                    elif alt21 == 3:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:43: MATERIAL
                        self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr405
                        )

                    elif alt21 == 4:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:54: name
                        self._state.following.append(self.FOLLOW_name_in_get_expr409)
                        self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr412)

                self._state.following.append(self.FOLLOW_test_in_get_expr416)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:70: ( simple_block | NEWLINE )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:71: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr419
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt23 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:36:86: NEWLINE
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr423)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "get_expr"

    # $ANTLR start "edit_block"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:1: edit_block : COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT ;
    def edit_block(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:14: ( COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:16: COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block434)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block436)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block438)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:37: ( attr | inner_behavior_stmt )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:38: attr
                        self._state.following.append(self.FOLLOW_attr_in_edit_block441)
                        self.attr()

                        self._state.following.pop()

                    elif alt24 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:45: inner_behavior_stmt
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:1: simple_block : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:14: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:16: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block456)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block458)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block460)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:37: ( simple_attr )+
                cnt25 = 0
                while True:  # loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if LA25_0 in {ID, UNDERSCORE}:
                        alt25 = 1

                    if alt25 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:37: simple_attr
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:1: attr : ( core_attr | simple_attr | compound_attr );
    def attr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:15: ( core_attr | simple_attr | compound_attr )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:17: core_attr
                    self._state.following.append(self.FOLLOW_core_attr_in_attr482)
                    self.core_attr()

                    self._state.following.pop()

                elif alt26 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:29: simple_attr
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr486)
                    self.simple_attr()

                    self._state.following.pop()

                elif alt26 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:43: compound_attr
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:1: simple_attr : name ( COLON name )? ( test )? NEWLINE ;
    def simple_attr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:15: ( name ( COLON name )? ( test )? NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:17: name ( COLON name )? ( test )? NEWLINE
                self._state.following.append(self.FOLLOW_name_in_simple_attr499)
                self.name()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:22: ( COLON name )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if LA27_0 == COLON:
                    alt27 = 1
                if alt27 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:23: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr502)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr504)
                    self.name()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:36: ( test )?
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:36: test
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:1: compound_attr : ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) ;
    def compound_attr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:15: ( ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE )
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:18: SCATTER ON name
                    self.match(
                        self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr520
                    )

                    self.match(self.input, ON, self.FOLLOW_ON_in_compound_attr522)

                    self._state.following.append(self.FOLLOW_name_in_compound_attr524)
                    self.name()

                    self._state.following.pop()

                elif alt29 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:36: ROT_AROUND name
                    self.match(
                        self.input,
                        ROT_AROUND,
                        self.FOLLOW_ROT_AROUND_in_compound_attr528,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr530)
                    self.name()

                    self._state.following.pop()

                elif alt29 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:54: PHYSICS
                    self.match(
                        self.input, PHYSICS, self.FOLLOW_PHYSICS_in_compound_attr534
                    )

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:63: ( simple_block | NEWLINE )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:64: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_compound_attr538
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt30 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:79: NEWLINE
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:46:1: core_attr : ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE ;
    def core_attr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:46:10: ( ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:48:5: TRANSLATE ( AXIS )? TO test
                    self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr559
                    )

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:48:15: ( AXIS )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if LA31_0 == AXIS:
                        alt31 = 1
                    if alt31 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:48:15: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr561)

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr564)

                    self._state.following.append(self.FOLLOW_test_in_core_attr566)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:49:7: CAM_TRANSLATE TO test
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:50:7: ROTATE ( AXIS )? test ( ORDER )?
                    self.match(self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr586)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:50:14: ( AXIS )?
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if LA32_0 == AXIS:
                        alt32 = 1
                    if alt32 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:50:14: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr588)

                    self._state.following.append(self.FOLLOW_test_in_core_attr591)
                    self.test()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:50:25: ( ORDER )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if LA33_0 == ORDER:
                        alt33 = 1
                    if alt33 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:50:25: ORDER
                        self.match(self.input, ORDER, self.FOLLOW_ORDER_in_core_attr593)

                elif alt34 == 4:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:51:7: SCALE test
                    self.match(self.input, SCALE, self.FOLLOW_SCALE_in_core_attr602)

                    self._state.following.append(self.FOLLOW_test_in_core_attr604)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 5:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:52:7: LOOK_AT test
                    self.match(self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr612)

                    self._state.following.append(self.FOLLOW_test_in_core_attr614)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 6:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:53:7: UP_AXIS test
                    self.match(self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr622)

                    self._state.following.append(self.FOLLOW_test_in_core_attr624)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 7:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:54:7: SIZE test
                    self.match(self.input, SIZE, self.FOLLOW_SIZE_in_core_attr632)

                    self._state.following.append(self.FOLLOW_test_in_core_attr634)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 8:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:55:7: SEMANTICS test
                    self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr642
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr644)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 9:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:56:7: VISIBLE test
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:60:1: inner_behavior_stmt : behavior_expr inner_behavior_block ;
    def inner_behavior_stmt(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:60:22: ( behavior_expr inner_behavior_block )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:60:24: behavior_expr inner_behavior_block
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:61:1: inner_behavior_block : COLON NEWLINE INDENT ( attr )+ DEDENT ;
    def inner_behavior_block(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:61:22: ( COLON NEWLINE INDENT ( attr )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:61:24: COLON NEWLINE INDENT ( attr )+ DEDENT
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block679
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block681
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block683
                )

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:61:45: ( attr )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:61:45: attr
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:64:1: behavior_stmt : behavior_expr behavior_block ;
    def behavior_stmt(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:64:16: ( behavior_expr behavior_block )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:64:18: behavior_expr behavior_block
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:65:1: behavior_expr : EVERY ( test )? ( FRAMES | TIME ) ;
    def behavior_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:65:16: ( EVERY ( test )? ( FRAMES | TIME ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:65:18: EVERY ( test )? ( FRAMES | TIME )
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr709)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:65:24: ( test )?
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:65:24: test
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:66:1: behavior_block : COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT ;
    def behavior_block(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:66:16: ( COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:66:18: COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block727)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block729
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block731)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:66:39: ( aug_expr_stmt | edit_stmt )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:66:40: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block734
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt37 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:66:56: edit_stmt
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:1: expr_stmt : testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE ;
    def expr_stmt(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:11: ( testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:13: testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt752)
                self.testlist()

                self._state.following.pop()

                if self.input.LA(1) in {ASSIGN, AUG_ASSIGN}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:44: ( testlist | fetch_expr )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if LA38_0 in {
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
                    alt38 = 1
                elif LA38_0 == FETCH:
                    alt38 = 2
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae

                if alt38 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:45: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt763)
                    self.testlist()

                    self._state.following.pop()

                elif alt38 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:56: fetch_expr
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:71:1: aug_expr_stmt : ( ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr );
    def aug_expr_stmt(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:71:14: ( ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr )
                alt43 = 5
                LA43 = self.input.LA(1)
                if LA43 in {
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:71:16: ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:71:16: ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:72:5: testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt783
                    )
                    self.testlist()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:72:14: ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if LA42_0 == AUG_ASSIGN:
                        alt42 = 1
                    elif LA42_0 == ASSIGN:
                        alt42 = 2
                    else:
                        nvae = NoViableAltException("", 42, 0, self.input)

                        raise nvae

                    if alt42 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:73:7: AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE
                        self.match(
                            self.input,
                            AUG_ASSIGN,
                            self.FOLLOW_AUG_ASSIGN_in_aug_expr_stmt793,
                        )

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:73:18: ( testlist | fetch_expr )?
                        alt39 = 3
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
                        if alt39 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:73:19: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt796
                            )
                            self.testlist()

                            self._state.following.pop()

                        elif alt39 == 2:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:73:30: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt800
                            )
                            self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_aug_expr_stmt804
                        )

                    elif alt42 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:74:9: ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt814
                        )

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:74:16: ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        alt41 = 5
                        LA41 = self.input.LA(1)
                        if LA41 in {
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
                            alt41 = 1
                        elif LA41 in {CREATE}:
                            alt41 = 2
                        elif LA41 in {INSTANTIATE}:
                            alt41 = 3
                        elif LA41 in {GET}:
                            alt41 = 4
                        elif LA41 in {GROUP}:
                            alt41 = 5
                        else:
                            nvae = NoViableAltException("", 41, 0, self.input)

                            raise nvae

                        if alt41 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:75:9: ( testlist | fetch_expr ) NEWLINE
                            pass
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:75:9: ( testlist | fetch_expr )
                            alt40 = 2
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
                            else:
                                nvae = NoViableAltException("", 40, 0, self.input)

                                raise nvae

                            if alt40 == 1:
                                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:75:10: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt827
                                )
                                self.testlist()

                                self._state.following.pop()

                            elif alt40 == 2:
                                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:75:21: fetch_expr
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

                        elif alt41 == 2:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:76:11: create_expr
                            self._state.following.append(
                                self.FOLLOW_create_expr_in_aug_expr_stmt846
                            )
                            self.create_expr()

                            self._state.following.pop()

                        elif alt41 == 3:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:76:25: instantiate_expr
                            self._state.following.append(
                                self.FOLLOW_instantiate_expr_in_aug_expr_stmt850
                            )
                            self.instantiate_expr()

                            self._state.following.pop()

                        elif alt41 == 4:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:76:44: get_expr
                            self._state.following.append(
                                self.FOLLOW_get_expr_in_aug_expr_stmt854
                            )
                            self.get_expr()

                            self._state.following.pop()

                        elif alt41 == 5:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:76:55: group_expr
                            self._state.following.append(
                                self.FOLLOW_group_expr_in_aug_expr_stmt858
                            )
                            self.group_expr()

                            self._state.following.pop()

                elif alt43 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:80:5: create_expr
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_aug_expr_stmt882
                    )
                    self.create_expr()

                    self._state.following.pop()

                elif alt43 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:80:19: instantiate_expr
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_aug_expr_stmt886
                    )
                    self.instantiate_expr()

                    self._state.following.pop()

                elif alt43 == 4:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:80:38: get_expr
                    self._state.following.append(
                        self.FOLLOW_get_expr_in_aug_expr_stmt890
                    )
                    self.get_expr()

                    self._state.following.pop()

                elif alt43 == 5:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:80:49: group_expr
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:1: fetch_expr : FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )? ;
    def fetch_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:12: ( FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:14: FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )?
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr903)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr905)
                self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr907)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr909)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:35: ( MATCH test )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if LA44_0 == MATCH:
                    alt44 = 1
                if alt44 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:36: MATCH test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr912)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr914)
                    self.test()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:49: ( LIMIT test )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 == LIMIT:
                    alt45 = 1
                if alt45 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:50: LIMIT test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr919)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr921)
                    self.test()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:63: ( RECURSIVE )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 == RECURSIVE:
                    alt46 = 1
                if alt46 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:63: RECURSIVE
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

    # $ANTLR start "test"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:1: test : or_test ( IF or_test ELSE test )? ;
    def test(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:13: ( or_test ( IF or_test ELSE test )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:15: or_test ( IF or_test ELSE test )?
                self._state.following.append(self.FOLLOW_or_test_in_test943)
                self.or_test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:23: ( IF or_test ELSE test )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if LA47_0 == IF:
                    alt47 = 1
                if alt47 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:24: IF or_test ELSE test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test946)

                    self._state.following.append(self.FOLLOW_or_test_in_test948)
                    self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test950)

                    self._state.following.append(self.FOLLOW_test_in_test952)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:87:1: test_nocond : or_test ;
    def test_nocond(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:87:13: ( or_test )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:87:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond961)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:88:1: or_test : and_test ( OR and_test )* ;
    def or_test(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:88:13: ( and_test ( OR and_test )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:88:15: and_test ( OR and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test972)
                self.and_test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:88:24: ( OR and_test )*
                while True:  # loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if LA48_0 == OR:
                        alt48 = 1

                    if alt48 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:88:25: OR and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test975)

                        self._state.following.append(self.FOLLOW_and_test_in_or_test977)
                        self.and_test()

                        self._state.following.pop()

                    else:
                        break  # loop48

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "or_test"

    # $ANTLR start "and_test"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:1: and_test : not_test ( AND not_test )* ;
    def and_test(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:13: ( not_test ( AND not_test )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:15: not_test ( AND not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test989)
                self.not_test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:24: ( AND not_test )*
                while True:  # loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if LA49_0 == AND:
                        alt49 = 1

                    if alt49 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:25: AND not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test992)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test994
                        )
                        self.not_test()

                        self._state.following.pop()

                    else:
                        break  # loop49

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "and_test"

    # $ANTLR start "not_test"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:90:1: not_test : ( NOT not_test | comparison );
    def not_test(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:90:13: ( NOT not_test | comparison )
                alt50 = 2
                LA50_0 = self.input.LA(1)

                if LA50_0 == NOT:
                    alt50 = 1
                elif LA50_0 in {
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
                    alt50 = 2
                else:
                    nvae = NoViableAltException("", 50, 0, self.input)

                    raise nvae

                if alt50 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:90:15: NOT not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1006)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1008)
                    self.not_test()

                    self._state.following.pop()

                elif alt50 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:90:30: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test1012)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:91:1: comparison : expr ( comp_op expr )* ;
    def comparison(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:91:13: ( expr ( comp_op expr )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:91:15: expr ( comp_op expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison1020)
                self.expr()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:91:20: ( comp_op expr )*
                while True:  # loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if LA51_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt51 = 1

                    if alt51 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:91:21: comp_op expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison1023
                        )
                        self.comp_op()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_expr_in_comparison1025)
                        self.expr()

                        self._state.following.pop()

                    else:
                        break  # loop51

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comparison"

    # $ANTLR start "comp_op"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:1: comp_op : ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT );
    def comp_op(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:13: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                alt52 = 10
                LA52 = self.input.LA(1)
                if LA52 in {LT}:
                    alt52 = 1
                elif LA52 in {GT}:
                    alt52 = 2
                elif LA52 in {EQUALS}:
                    alt52 = 3
                elif LA52 in {GT_EQ}:
                    alt52 = 4
                elif LA52 in {LT_EQ}:
                    alt52 = 5
                elif LA52 in {NOT_EQ}:
                    alt52 = 6
                elif LA52 in {IN}:
                    alt52 = 7
                elif LA52 in {NOT}:
                    alt52 = 8
                elif LA52 in {IS}:
                    LA52_9 = self.input.LA(2)

                    if LA52_9 == NOT:
                        alt52 = 10
                    elif LA52_9 in {
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
                        alt52 = 9
                    else:
                        nvae = NoViableAltException("", 52, 9, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:15: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_comp_op1038)

                elif alt52 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:20: GT
                    self.match(self.input, GT, self.FOLLOW_GT_in_comp_op1042)

                elif alt52 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:25: EQUALS
                    self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op1046)

                elif alt52 == 4:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:34: GT_EQ
                    self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op1050)

                elif alt52 == 5:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:42: LT_EQ
                    self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op1054)

                elif alt52 == 6:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:50: NOT_EQ
                    self.match(self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op1058)

                elif alt52 == 7:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:59: IN
                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1062)

                elif alt52 == 8:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:64: NOT IN
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1066)

                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1068)

                elif alt52 == 9:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:73: IS
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1072)

                elif alt52 == 10:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:78: IS NOT
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1076)

                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1078)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comp_op"

    # $ANTLR start "expr"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:1: expr : xor_expr ( BIT_OR xor_expr )* ;
    def expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:13: ( xor_expr ( BIT_OR xor_expr )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:15: xor_expr ( BIT_OR xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr1092)
                self.xor_expr()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:24: ( BIT_OR xor_expr )*
                while True:  # loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if LA53_0 == BIT_OR:
                        alt53 = 1

                    if alt53 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:25: BIT_OR xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr1095)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr1097)
                        self.xor_expr()

                        self._state.following.pop()

                    else:
                        break  # loop53

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "expr"

    # $ANTLR start "xor_expr"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:94:1: xor_expr : and_expr ( XOR and_expr )* ;
    def xor_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:94:13: ( and_expr ( XOR and_expr )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:94:15: and_expr ( XOR and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1109)
                self.and_expr()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:94:24: ( XOR and_expr )*
                while True:  # loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if LA54_0 == XOR:
                        alt54 = 1

                    if alt54 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:94:25: XOR and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr1112)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr1114
                        )
                        self.and_expr()

                        self._state.following.pop()

                    else:
                        break  # loop54

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "xor_expr"

    # $ANTLR start "and_expr"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:95:1: and_expr : shift_expr ( BIT_AND shift_expr )* ;
    def and_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:95:13: ( shift_expr ( BIT_AND shift_expr )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:95:15: shift_expr ( BIT_AND shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1126)
                self.shift_expr()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:95:26: ( BIT_AND shift_expr )*
                while True:  # loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if LA55_0 == BIT_AND:
                        alt55 = 1

                    if alt55 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:95:27: BIT_AND shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr1129
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr1131
                        )
                        self.shift_expr()

                        self._state.following.pop()

                    else:
                        break  # loop55

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "and_expr"

    # $ANTLR start "shift_expr"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:1: shift_expr : arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* ;
    def shift_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:13: ( arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:15: arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1141)
                self.arith_expr()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:26: ( ( LSHIFT | RSHIFT ) arith_expr )*
                while True:  # loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if LA56_0 in {LSHIFT, RSHIFT}:
                        alt56 = 1

                    if alt56 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:27: ( LSHIFT | RSHIFT ) arith_expr
                        if self.input.LA(1) in {LSHIFT, RSHIFT}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr1152
                        )
                        self.arith_expr()

                        self._state.following.pop()

                    else:
                        break  # loop56

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "shift_expr"

    # $ANTLR start "arith_expr"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:1: arith_expr : term ( ( PLUS | MINUS ) term )* ;
    def arith_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:13: ( term ( ( PLUS | MINUS ) term )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:15: term ( ( PLUS | MINUS ) term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr1162)
                self.term()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:20: ( ( PLUS | MINUS ) term )*
                while True:  # loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if LA57_0 in {MINUS, PLUS}:
                        alt57 = 1

                    if alt57 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:21: ( PLUS | MINUS ) term
                        if self.input.LA(1) in {MINUS, PLUS}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_term_in_arith_expr1173)
                        self.term()

                        self._state.following.pop()

                    else:
                        break  # loop57

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "arith_expr"

    # $ANTLR start "term"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:1: term : factor ( ( MUL | DIV | MOD | IDIV ) factor )* ;
    def term(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:13: ( factor ( ( MUL | DIV | MOD | IDIV ) factor )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:15: factor ( ( MUL | DIV | MOD | IDIV ) factor )*
                self._state.following.append(self.FOLLOW_factor_in_term1189)
                self.factor()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:22: ( ( MUL | DIV | MOD | IDIV ) factor )*
                while True:  # loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if LA58_0 in {DIV, IDIV, MOD, MUL}:
                        alt58 = 1

                    if alt58 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:23: ( MUL | DIV | MOD | IDIV ) factor
                        if self.input.LA(1) in {DIV, IDIV, MOD, MUL}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_factor_in_term1208)
                        self.factor()

                        self._state.following.pop()

                    else:
                        break  # loop58

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "term"

    # $ANTLR start "factor"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:1: factor : ( ( PLUS | MINUS | BIT_NOT ) factor | power );
    def factor(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:13: ( ( PLUS | MINUS | BIT_NOT ) factor | power )
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if LA59_0 in {BIT_NOT, MINUS, PLUS}:
                    alt59 = 1
                elif LA59_0 in {
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
                    alt59 = 2
                else:
                    nvae = NoViableAltException("", 59, 0, self.input)

                    raise nvae

                if alt59 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:15: ( PLUS | MINUS | BIT_NOT ) factor
                    if self.input.LA(1) in {BIT_NOT, MINUS, PLUS}:
                        self.input.consume()
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse

                    self._state.following.append(self.FOLLOW_factor_in_factor1234)
                    self.factor()

                    self._state.following.pop()

                elif alt59 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:49: power
                    self._state.following.append(self.FOLLOW_power_in_factor1238)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:1: power : atom_expr ( POWER factor )? ;
    def power(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:13: ( atom_expr ( POWER factor )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power1251)
                self.atom_expr()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:25: ( POWER factor )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if LA60_0 == POWER:
                    alt60 = 1
                if alt60 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power1254)

                    self._state.following.append(self.FOLLOW_factor_in_power1256)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:1: atom_expr : atom ( trailer )* ;
    def atom_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:13: ( atom ( trailer )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:15: atom ( trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr1267)
                self.atom()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:20: ( trailer )*
                while True:  # loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if LA61_0 in {DOT, LBRACK}:
                        alt61 = 1

                    if alt61 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:23: trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr1272
                        )
                        self.trailer()

                        self._state.following.pop()

                    else:
                        break  # loop61

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "atom_expr"

    # $ANTLR start "atom"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:1: atom : ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE );
    def atom(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:5: ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE )
                alt68 = 13
                LA68 = self.input.LA(1)
                if LA68 in {LPAREN}:
                    alt68 = 1
                elif LA68 in {LBRACK}:
                    alt68 = 2
                elif LA68 in {LT}:
                    alt68 = 3
                elif LA68 in {LBRACE}:
                    alt68 = 4
                elif LA68 in {ID, UNDERSCORE}:
                    alt68 = 5
                elif LA68 in {SETTING_ID}:
                    alt68 = 6
                elif LA68 in {CHOICE, LOG_UNIFORM, NORMAL, SEQUENCE, UNIFORM}:
                    alt68 = 7
                elif LA68 in {INTEGER}:
                    alt68 = 8
                elif LA68 in {FLOAT_NUMBER}:
                    alt68 = 9
                elif LA68 in {STRING}:
                    alt68 = 10
                elif LA68 in {NONE}:
                    alt68 = 11
                elif LA68 in {TRUE}:
                    alt68 = 12
                elif LA68 in {FALSE}:
                    alt68 = 13
                else:
                    nvae = NoViableAltException("", 68, 0, self.input)

                    raise nvae

                if alt68 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:3: LPAREN test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1282)

                    self._state.following.append(self.FOLLOW_test_in_atom1284)
                    self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1286)

                elif alt68 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:5: LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom1292)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:12: ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) )
                    alt65 = 2
                    LA65 = self.input.LA(1)
                    if LA65 in {
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
                        alt65 = 1
                    elif LA65 in {MINUS}:
                        LA65_2 = self.input.LA(2)

                        if LA65_2 in {
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
                            alt65 = 1
                        elif LA65_2 == INTEGER:
                            LA65_4 = self.input.LA(3)

                            if LA65_4 == RANGE:
                                alt65 = 2
                            elif LA65_4 in {
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
                                alt65 = 1
                            else:
                                nvae = NoViableAltException("", 65, 4, self.input)

                                raise nvae

                        else:
                            nvae = NoViableAltException("", 65, 2, self.input)

                            raise nvae

                    elif LA65 in {INTEGER}:
                        LA65_3 = self.input.LA(2)

                        if LA65_3 == RANGE:
                            alt65 = 2
                        elif LA65_3 in {
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
                            alt65 = 1
                        else:
                            nvae = NoViableAltException("", 65, 3, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 65, 0, self.input)

                        raise nvae

                    if alt65 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:13: ( testlist_comp )?
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:13: ( testlist_comp )?
                        alt62 = 2
                        LA62_0 = self.input.LA(1)

                        if LA62_0 in {
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
                            alt62 = 1
                        if alt62 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:13: testlist_comp
                            self._state.following.append(
                                self.FOLLOW_testlist_comp_in_atom1295
                            )
                            self.testlist_comp()

                            self._state.following.pop()

                    elif alt65 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:30: ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER )
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:30: ( ( MINUS )? INTEGER )
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:31: ( MINUS )? INTEGER
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:31: ( MINUS )?
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if LA63_0 == MINUS:
                            alt63 = 1
                        if alt63 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:31: MINUS
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1301)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1304)

                        self.match(self.input, RANGE, self.FOLLOW_RANGE_in_atom1307)

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:53: ( ( MINUS )? INTEGER )
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:54: ( MINUS )? INTEGER
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:54: ( MINUS )?
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if LA64_0 == MINUS:
                            alt64 = 1
                        if alt64 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:54: MINUS
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1310)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1313)

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom1317)

                elif alt68 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:105:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom1323)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:105:8: ( vector_comp )?
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:105:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom1325
                        )
                        self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom1328)

                elif alt68 == 4:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:106:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom1334)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:106:12: ( dict_or_set_maker )?
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
                        NOT,
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:106:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom1336
                        )
                        self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom1339)

                elif alt68 == 5:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:107:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom1345)
                    self.name()

                    self._state.following.pop()

                elif alt68 == 6:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:107:12: SETTING_ID
                    self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom1349
                    )

                elif alt68 == 7:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:107:25: distribution_expr
                    self._state.following.append(
                        self.FOLLOW_distribution_expr_in_atom1353
                    )
                    self.distribution_expr()

                    self._state.following.pop()

                elif alt68 == 8:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:108:5: INTEGER
                    self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1359)

                elif alt68 == 9:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:108:15: FLOAT_NUMBER
                    self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom1363
                    )

                elif alt68 == 10:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:108:30: STRING
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_atom1367)

                elif alt68 == 11:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:108:39: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom1371)

                elif alt68 == 12:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:108:46: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom1375)

                elif alt68 == 13:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:108:53: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom1379)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "atom"

    # $ANTLR start "name"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:111:1: name : ( ID | UNDERSCORE );
    def name(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:111:5: ( ID | UNDERSCORE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:124:1: distribution_expr : distribution LPAREN arglist RPAREN ;
    def distribution_expr(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:124:19: ( distribution LPAREN arglist RPAREN )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:124:21: distribution LPAREN arglist RPAREN
                self._state.following.append(
                    self.FOLLOW_distribution_in_distribution_expr1408
                )
                self.distribution()

                self._state.following.pop()

                self.match(
                    self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution_expr1410
                )

                self._state.following.append(
                    self.FOLLOW_arglist_in_distribution_expr1412
                )
                self.arglist()

                self._state.following.pop()

                self.match(
                    self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution_expr1414
                )

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "distribution_expr"

    # $ANTLR start "distribution"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:125:1: distribution : ( UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM );
    def distribution(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:125:19: ( UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:1: testlist_comp : test ( comp_for | ( COMMA test )* ) ;
    def testlist_comp(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:15: ( test ( comp_for | ( COMMA test )* ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:17: test ( comp_for | ( COMMA test )* )
                self._state.following.append(self.FOLLOW_test_in_testlist_comp1450)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:22: ( comp_for | ( COMMA test )* )
                alt70 = 2
                LA70_0 = self.input.LA(1)

                if LA70_0 == FOR:
                    alt70 = 1
                elif LA70_0 in {COMMA, RBRACK}:
                    alt70 = 2
                else:
                    nvae = NoViableAltException("", 70, 0, self.input)

                    raise nvae

                if alt70 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:24: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp1454
                    )
                    self.comp_for()

                    self._state.following.pop()

                elif alt70 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:35: ( COMMA test )*
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:35: ( COMMA test )*
                    while True:  # loop69
                        alt69 = 2
                        LA69_0 = self.input.LA(1)

                        if LA69_0 == COMMA:
                            alt69 = 1

                        if alt69 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:36: COMMA test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp1459,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp1461
                            )
                            self.test()

                            self._state.following.pop()

                        else:
                            break  # loop69

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "testlist_comp"

    # $ANTLR start "vector_comp"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:128:1: vector_comp : expr COMMA expr COMMA expr ;
    def vector_comp(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:128:15: ( expr COMMA expr COMMA expr )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:128:17: expr COMMA expr COMMA expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp1473)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1475)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1477)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1479)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1481)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:130:1: trailer : ( LBRACK subscriptlist RBRACK | DOT name );
    def trailer(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:130:15: ( LBRACK subscriptlist RBRACK | DOT name )
                alt71 = 2
                LA71_0 = self.input.LA(1)

                if LA71_0 == LBRACK:
                    alt71 = 1
                elif LA71_0 == DOT:
                    alt71 = 2
                else:
                    nvae = NoViableAltException("", 71, 0, self.input)

                    raise nvae

                if alt71 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:130:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer1497)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer1499
                    )
                    self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer1501)

                elif alt71 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:130:47: DOT name
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer1505)

                    self._state.following.append(self.FOLLOW_name_in_trailer1507)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:131:1: arglist : argument ( COMMA argument )* ;
    def arglist(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:131:15: ( argument ( COMMA argument )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:131:17: argument ( COMMA argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist1520)
                self.argument()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:131:26: ( COMMA argument )*
                while True:  # loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if LA72_0 == COMMA:
                        alt72 = 1

                    if alt72 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:131:27: COMMA argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist1523)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist1525
                        )
                        self.argument()

                        self._state.following.pop()

                    else:
                        break  # loop72

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "arglist"

    # $ANTLR start "argument"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:132:1: argument : test ( comp_for | ASSIGN test )? ;
    def argument(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:132:15: ( test ( comp_for | ASSIGN test )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:132:17: test ( comp_for | ASSIGN test )?
                self._state.following.append(self.FOLLOW_test_in_argument1539)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:132:22: ( comp_for | ASSIGN test )?
                alt73 = 3
                LA73_0 = self.input.LA(1)

                if LA73_0 == FOR:
                    alt73 = 1
                elif LA73_0 == ASSIGN:
                    alt73 = 2
                if alt73 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:132:23: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_argument1542)
                    self.comp_for()

                    self._state.following.pop()

                elif alt73 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:132:34: ASSIGN test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument1546)

                    self._state.following.append(self.FOLLOW_test_in_argument1548)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:133:1: subscriptlist : subscript_ ( COMMA subscript_ )* ;
    def subscriptlist(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:133:15: ( subscript_ ( COMMA subscript_ )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:133:17: subscript_ ( COMMA subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist1557
                )
                self.subscript_()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:133:28: ( COMMA subscript_ )*
                while True:  # loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if LA74_0 == COMMA:
                        alt74 = 1

                    if alt74 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:133:29: COMMA subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist1560
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist1562
                        )
                        self.subscript_()

                        self._state.following.pop()

                    else:
                        break  # loop74

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "subscriptlist"

    # $ANTLR start "subscript_"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:1: subscript_ : ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? );
    def subscript_(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:15: ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? )
                alt80 = 2
                LA80_0 = self.input.LA(1)

                if LA80_0 in {
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
                    alt80 = 1
                elif LA80_0 == COLON:
                    alt80 = 2
                else:
                    nvae = NoViableAltException("", 80, 0, self.input)

                    raise nvae

                if alt80 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:17: test ( COLON ( test )? ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_1574)
                    self.test()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:22: ( COLON ( test )? ( sliceop )? )?
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if LA77_0 == COLON:
                        alt77 = 1
                    if alt77 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:23: COLON ( test )? ( sliceop )?
                        self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_1577
                        )

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:29: ( test )?
                        alt75 = 2
                        LA75_0 = self.input.LA(1)

                        if LA75_0 in {
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
                            alt75 = 1
                        if alt75 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:30: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_1580
                            )
                            self.test()

                            self._state.following.pop()

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:37: ( sliceop )?
                        alt76 = 2
                        LA76_0 = self.input.LA(1)

                        if LA76_0 == COLON:
                            alt76 = 1
                        if alt76 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:38: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_1585
                            )
                            self.sliceop()

                            self._state.following.pop()

                elif alt80 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:52: COLON ( test )? ( sliceop )?
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript_1593)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:58: ( test )?
                    alt78 = 2
                    LA78_0 = self.input.LA(1)

                    if LA78_0 in {
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
                        alt78 = 1
                    if alt78 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:59: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_1596)
                        self.test()

                        self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:66: ( sliceop )?
                    alt79 = 2
                    LA79_0 = self.input.LA(1)

                    if LA79_0 == COLON:
                        alt79 = 1
                    if alt79 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:134:67: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_1601
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:135:1: sliceop : COLON ( test )? ;
    def sliceop(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:135:15: ( COLON ( test )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:135:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop1616)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:135:23: ( test )?
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
                if alt81 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:135:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop1618)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:137:1: exprlist : expr ( COMMA expr )* ;
    def exprlist(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:137:10: ( expr ( COMMA expr )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:137:12: expr ( COMMA expr )*
                self._state.following.append(self.FOLLOW_expr_in_exprlist1627)
                self.expr()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:137:17: ( COMMA expr )*
                while True:  # loop82
                    alt82 = 2
                    LA82_0 = self.input.LA(1)

                    if LA82_0 == COMMA:
                        alt82 = 1

                    if alt82 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:137:18: COMMA expr
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist1630)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist1632)
                        self.expr()

                        self._state.following.pop()

                    else:
                        break  # loop82

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "exprlist"

    # $ANTLR start "testlist"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:138:1: testlist : test ( COMMA test )* ;
    def testlist(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:138:10: ( test ( COMMA test )* )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:138:12: test ( COMMA test )*
                self._state.following.append(self.FOLLOW_test_in_testlist1641)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:138:17: ( COMMA test )*
                while True:  # loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if LA83_0 == COMMA:
                        alt83 = 1

                    if alt83 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:138:18: COMMA test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist1644)

                        self._state.following.append(self.FOLLOW_test_in_testlist1646)
                        self.test()

                        self._state.following.pop()

                    else:
                        break  # loop83

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "testlist"

    # $ANTLR start "dict_or_set_maker"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:139:1: dict_or_set_maker : test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) ;
    def dict_or_set_maker(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:139:18: ( test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:3: test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker1656)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:8: ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                alt88 = 2
                LA88_0 = self.input.LA(1)

                if LA88_0 == COLON:
                    alt88 = 1
                elif LA88_0 in {COMMA, FOR, RBRACE}:
                    alt88 = 2
                else:
                    nvae = NoViableAltException("", 88, 0, self.input)

                    raise nvae

                if alt88 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:10: COLON test ( comp_for | ( COMMA test COLON test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker1660
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker1662
                    )
                    self.test()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:21: ( comp_for | ( COMMA test COLON test )* )
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if LA85_0 == FOR:
                        alt85 = 1
                    elif LA85_0 in {COMMA, RBRACE}:
                        alt85 = 2
                    else:
                        nvae = NoViableAltException("", 85, 0, self.input)

                        raise nvae

                    if alt85 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:22: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1665
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt85 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:33: ( COMMA test COLON test )*
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:33: ( COMMA test COLON test )*
                        while True:  # loop84
                            alt84 = 2
                            LA84_0 = self.input.LA(1)

                            if LA84_0 == COMMA:
                                alt84 = 1

                            if alt84 == 1:
                                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:34: COMMA test COLON test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker1670,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1672
                                )
                                self.test()

                                self._state.following.pop()

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker1674,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1676
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop84

                elif alt88 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:10: ( comp_for | ( COMMA test )* )
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:10: ( comp_for | ( COMMA test )* )
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if LA87_0 == FOR:
                        alt87 = 1
                    elif LA87_0 in {COMMA, RBRACE}:
                        alt87 = 2
                    else:
                        nvae = NoViableAltException("", 87, 0, self.input)

                        raise nvae

                    if alt87 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:11: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1691
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt87 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:22: ( COMMA test )*
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:22: ( COMMA test )*
                        while True:  # loop86
                            alt86 = 2
                            LA86_0 = self.input.LA(1)

                            if LA86_0 == COMMA:
                                alt86 = 1

                            if alt86 == 1:
                                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:23: COMMA test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker1696,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker1698
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop86

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "dict_or_set_maker"

    # $ANTLR start "comp_iter"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:144:1: comp_iter : ( comp_for | comp_if );
    def comp_iter(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:144:11: ( comp_for | comp_if )
                alt89 = 2
                LA89_0 = self.input.LA(1)

                if LA89_0 == FOR:
                    alt89 = 1
                elif LA89_0 == IF:
                    alt89 = 2
                else:
                    nvae = NoViableAltException("", 89, 0, self.input)

                    raise nvae

                if alt89 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:144:13: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter1712)
                    self.comp_for()

                    self._state.following.pop()

                elif alt89 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:144:24: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter1716)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:145:1: comp_for : FOR exprlist IN or_test ( comp_iter )? ;
    def comp_for(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:145:11: ( FOR exprlist IN or_test ( comp_iter )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:145:13: FOR exprlist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for1724)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for1726)
                self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for1728)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for1730)
                self.or_test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:145:37: ( comp_iter )?
                alt90 = 2
                LA90_0 = self.input.LA(1)

                if LA90_0 in {FOR, IF}:
                    alt90 = 1
                if alt90 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:145:37: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for1732)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:146:1: comp_if : IF test_nocond ( comp_iter )? ;
    def comp_if(
        self,
    ):
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:146:11: ( IF test_nocond ( comp_iter )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:146:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if1742)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if1744)
                self.test_nocond()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:146:28: ( comp_iter )?
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if LA91_0 in {FOR, IF}:
                    alt91 = 1
                if alt91 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:146:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if1746)
                    self.comp_iter()

                    self._state.following.pop()

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return

    # $ANTLR end "comp_if"

    FOLLOW_declaration_in_scenario35 = frozenset([1, 73, 102, 111, 125])
    FOLLOW_NEWLINE_in_scenario37 = frozenset([1, 73, 102, 111, 125])
    FOLLOW_settings_in_scenario40 = frozenset([1, 111, 125])
    FOLLOW_stage_in_scenario43 = frozenset([1, 125])
    FOLLOW_writers_in_scenario46 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration56 = frozenset([43, 120])
    FOLLOW_name_in_declaration58 = frozenset([16, 73])
    FOLLOW_COLON_in_declaration61 = frozenset([43, 120])
    FOLLOW_name_in_declaration63 = frozenset([73])
    FOLLOW_NEWLINE_in_declaration67 = frozenset([1])
    FOLLOW_SETTINGS_in_settings77 = frozenset([16])
    FOLLOW_COLON_in_settings79 = frozenset([73])
    FOLLOW_NEWLINE_in_settings81 = frozenset([49])
    FOLLOW_INDENT_in_settings83 = frozenset([43])
    FOLLOW_option_in_settings85 = frozenset([20, 43])
    FOLLOW_DEDENT_in_settings88 = frozenset([1])
    FOLLOW_STAGE_in_stage101 = frozenset([16])
    FOLLOW_COLON_in_stage103 = frozenset([73])
    FOLLOW_NEWLINE_in_stage105 = frozenset([49])
    FOLLOW_INDENT_in_stage107 = frozenset(
        [
            11,
            15,
            19,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            81,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_stmts_in_stage109 = frozenset([20])
    FOLLOW_DEDENT_in_stage111 = frozenset([1])
    FOLLOW_WRITERS_in_writers122 = frozenset([16])
    FOLLOW_COLON_in_writers124 = frozenset([73])
    FOLLOW_NEWLINE_in_writers126 = frozenset([49])
    FOLLOW_INDENT_in_writers128 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_expr_stmt_in_writers131 = frozenset(
        [
            11,
            15,
            20,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_writer_in_writers135 = frozenset(
        [
            11,
            15,
            20,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_DEDENT_in_writers139 = frozenset([1])
    FOLLOW_ID_in_option147 = frozenset([5])
    FOLLOW_ASSIGN_in_option149 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_option151 = frozenset([73])
    FOLLOW_NEWLINE_in_option153 = frozenset([1])
    FOLLOW_open_stmt_in_stmts161 = frozenset(
        [
            11,
            15,
            19,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_aug_expr_stmt_in_stmts165 = frozenset(
        [
            1,
            11,
            15,
            19,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_edit_stmt_in_stmts169 = frozenset(
        [
            1,
            11,
            15,
            19,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_behavior_stmt_in_stmts173 = frozenset(
        [
            1,
            11,
            15,
            19,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_ID_in_writer182 = frozenset([16])
    FOLLOW_COLON_in_writer184 = frozenset([73])
    FOLLOW_NEWLINE_in_writer186 = frozenset([49])
    FOLLOW_INDENT_in_writer188 = frozenset([43])
    FOLLOW_option_in_writer190 = frozenset([20, 43])
    FOLLOW_DEDENT_in_writer193 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt205 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_open_stmt207 = frozenset([73])
    FOLLOW_NEWLINE_in_open_stmt209 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt216 = frozenset([43, 116, 120])
    FOLLOW_TIMELINE_in_edit_stmt219 = frozenset([16])
    FOLLOW_name_in_edit_stmt223 = frozenset([16])
    FOLLOW_edit_block_in_edit_stmt226 = frozenset([1])
    FOLLOW_CREATE_in_create_expr235 = frozenset(
        [
            11,
            13,
            15,
            31,
            33,
            37,
            43,
            51,
            54,
            55,
            58,
            61,
            63,
            65,
            68,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            104,
            105,
            112,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_create_expr237 = frozenset([13, 37, 58, 68, 104, 105, 112])
    FOLLOW_STEREO_in_create_expr247 = frozenset([13])
    FOLLOW_CAMERA_in_create_expr250 = frozenset([16, 73])
    FOLLOW_shapes_in_create_expr254 = frozenset([16, 73])
    FOLLOW_light_type_in_create_expr258 = frozenset([57])
    FOLLOW_LIGHT_in_create_expr260 = frozenset([16, 73])
    FOLLOW_FROM_in_create_expr264 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_create_expr266 = frozenset([16, 73])
    FOLLOW_edit_block_in_create_expr270 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr274 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr283 = frozenset([16])
    FOLLOW_simple_block_in_create_expr286 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr327 = frozenset(
        [
            11,
            15,
            31,
            33,
            37,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_instantiate_expr330 = frozenset([37])
    FOLLOW_FROM_in_instantiate_expr334 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_instantiate_expr336 = frozenset([16, 73])
    FOLLOW_edit_block_in_instantiate_expr339 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr343 = frozenset([1])
    FOLLOW_GROUP_in_group_expr357 = frozenset([55])
    FOLLOW_LBRACK_in_group_expr359 = frozenset([43, 120])
    FOLLOW_name_in_group_expr361 = frozenset([17, 90])
    FOLLOW_COMMA_in_group_expr364 = frozenset([43, 120])
    FOLLOW_name_in_group_expr366 = frozenset([17, 90])
    FOLLOW_RBRACK_in_group_expr370 = frozenset([16, 73])
    FOLLOW_edit_block_in_group_expr373 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr377 = frozenset([1])
    FOLLOW_GET_in_get_expr393 = frozenset(
        [
            11,
            13,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            57,
            61,
            63,
            65,
            68,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_CAMERA_in_get_expr397 = frozenset([6])
    FOLLOW_LIGHT_in_get_expr401 = frozenset([6])
    FOLLOW_MATERIAL_in_get_expr405 = frozenset([6])
    FOLLOW_name_in_get_expr409 = frozenset([6])
    FOLLOW_AT_in_get_expr412 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_get_expr416 = frozenset([16, 73])
    FOLLOW_simple_block_in_get_expr419 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr423 = frozenset([1])
    FOLLOW_COLON_in_edit_block434 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_block436 = frozenset([49])
    FOLLOW_INDENT_in_edit_block438 = frozenset(
        [14, 28, 43, 62, 84, 92, 93, 96, 97, 99, 107, 118, 120, 123, 124]
    )
    FOLLOW_attr_in_edit_block441 = frozenset(
        [14, 20, 28, 43, 62, 84, 92, 93, 96, 97, 99, 107, 118, 120, 123, 124]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block445 = frozenset(
        [14, 20, 28, 43, 62, 84, 92, 93, 96, 97, 99, 107, 118, 120, 123, 124]
    )
    FOLLOW_DEDENT_in_edit_block449 = frozenset([1])
    FOLLOW_COLON_in_simple_block456 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_block458 = frozenset([49])
    FOLLOW_INDENT_in_simple_block460 = frozenset([43, 120])
    FOLLOW_simple_attr_in_simple_block462 = frozenset([20, 43, 120])
    FOLLOW_DEDENT_in_simple_block465 = frozenset([1])
    FOLLOW_core_attr_in_attr482 = frozenset([1])
    FOLLOW_simple_attr_in_attr486 = frozenset([1])
    FOLLOW_compound_attr_in_attr490 = frozenset([1])
    FOLLOW_name_in_simple_attr499 = frozenset(
        [
            11,
            15,
            16,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            73,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_COLON_in_simple_attr502 = frozenset([43, 120])
    FOLLOW_name_in_simple_attr504 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            73,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_simple_attr508 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_attr511 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr520 = frozenset([80])
    FOLLOW_ON_in_compound_attr522 = frozenset([43, 120])
    FOLLOW_name_in_compound_attr524 = frozenset([16, 73])
    FOLLOW_ROT_AROUND_in_compound_attr528 = frozenset([43, 120])
    FOLLOW_name_in_compound_attr530 = frozenset([16, 73])
    FOLLOW_PHYSICS_in_compound_attr534 = frozenset([16, 73])
    FOLLOW_simple_block_in_compound_attr538 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr542 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr559 = frozenset([8, 117])
    FOLLOW_AXIS_in_core_attr561 = frozenset([117])
    FOLLOW_TO_in_core_attr564 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr566 = frozenset([73])
    FOLLOW_CAM_TRANSLATE_in_core_attr574 = frozenset([117])
    FOLLOW_TO_in_core_attr576 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr578 = frozenset([73])
    FOLLOW_ROTATE_in_core_attr586 = frozenset(
        [
            8,
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_AXIS_in_core_attr588 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr591 = frozenset([73, 83])
    FOLLOW_ORDER_in_core_attr593 = frozenset([73])
    FOLLOW_SCALE_in_core_attr602 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr604 = frozenset([73])
    FOLLOW_LOOK_AT_in_core_attr612 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr614 = frozenset([73])
    FOLLOW_UP_AXIS_in_core_attr622 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr624 = frozenset([73])
    FOLLOW_SIZE_in_core_attr632 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr634 = frozenset([73])
    FOLLOW_SEMANTICS_in_core_attr642 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr644 = frozenset([73])
    FOLLOW_VISIBLE_in_core_attr652 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_core_attr654 = frozenset([73])
    FOLLOW_NEWLINE_in_core_attr660 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt670 = frozenset([16])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt672 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block679 = frozenset([73])
    FOLLOW_NEWLINE_in_inner_behavior_block681 = frozenset([49])
    FOLLOW_INDENT_in_inner_behavior_block683 = frozenset(
        [14, 43, 62, 84, 92, 93, 96, 97, 99, 107, 118, 120, 123, 124]
    )
    FOLLOW_attr_in_inner_behavior_block685 = frozenset(
        [14, 20, 43, 62, 84, 92, 93, 96, 97, 99, 107, 118, 120, 123, 124]
    )
    FOLLOW_DEDENT_in_inner_behavior_block688 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt699 = frozenset([16])
    FOLLOW_behavior_block_in_behavior_stmt701 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr709 = frozenset(
        [
            11,
            15,
            31,
            33,
            36,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            115,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_behavior_expr711 = frozenset([36, 115])
    FOLLOW_set_in_behavior_expr714 = frozenset([1])
    FOLLOW_COLON_in_behavior_block727 = frozenset([73])
    FOLLOW_NEWLINE_in_behavior_block729 = frozenset([49])
    FOLLOW_INDENT_in_behavior_block731 = frozenset(
        [
            11,
            15,
            19,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_aug_expr_stmt_in_behavior_block734 = frozenset(
        [
            11,
            15,
            19,
            20,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_edit_stmt_in_behavior_block738 = frozenset(
        [
            11,
            15,
            19,
            20,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_DEDENT_in_behavior_block742 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt752 = frozenset([5, 7])
    FOLLOW_set_in_expr_stmt754 = frozenset(
        [
            11,
            15,
            31,
            32,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_testlist_in_expr_stmt763 = frozenset([73])
    FOLLOW_fetch_expr_in_expr_stmt767 = frozenset([73])
    FOLLOW_NEWLINE_in_expr_stmt770 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt783 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_aug_expr_stmt793 = frozenset(
        [
            11,
            15,
            31,
            32,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            73,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt796 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt800 = frozenset([73])
    FOLLOW_NEWLINE_in_aug_expr_stmt804 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt814 = frozenset(
        [
            11,
            15,
            19,
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
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt827 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt831 = frozenset([73])
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
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_fetch_expr905 = frozenset([37])
    FOLLOW_FROM_in_fetch_expr907 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_fetch_expr909 = frozenset([1, 59, 67, 91])
    FOLLOW_MATCH_in_fetch_expr912 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_fetch_expr914 = frozenset([1, 59, 91])
    FOLLOW_LIMIT_in_fetch_expr919 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_fetch_expr921 = frozenset([1, 91])
    FOLLOW_RECURSIVE_in_fetch_expr925 = frozenset([1])
    FOLLOW_or_test_in_test943 = frozenset([1, 47])
    FOLLOW_IF_in_test946 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_or_test_in_test948 = frozenset([26])
    FOLLOW_ELSE_in_test950 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_test952 = frozenset([1])
    FOLLOW_or_test_in_test_nocond961 = frozenset([1])
    FOLLOW_and_test_in_or_test972 = frozenset([1, 82])
    FOLLOW_OR_in_or_test975 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_and_test_in_or_test977 = frozenset([1, 82])
    FOLLOW_not_test_in_and_test989 = frozenset([1, 4])
    FOLLOW_AND_in_and_test992 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_not_test_in_and_test994 = frozenset([1, 4])
    FOLLOW_NOT_in_not_test1006 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_not_test_in_not_test1008 = frozenset([1])
    FOLLOW_comparison_in_not_test1012 = frozenset([1])
    FOLLOW_expr_in_comparison1020 = frozenset([1, 27, 40, 41, 48, 53, 65, 66, 77, 78])
    FOLLOW_comp_op_in_comparison1023 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_expr_in_comparison1025 = frozenset([1, 27, 40, 41, 48, 53, 65, 66, 77, 78])
    FOLLOW_LT_in_comp_op1038 = frozenset([1])
    FOLLOW_GT_in_comp_op1042 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op1046 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op1050 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op1054 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op1058 = frozenset([1])
    FOLLOW_IN_in_comp_op1062 = frozenset([1])
    FOLLOW_NOT_in_comp_op1066 = frozenset([48])
    FOLLOW_IN_in_comp_op1068 = frozenset([1])
    FOLLOW_IS_in_comp_op1072 = frozenset([1])
    FOLLOW_IS_in_comp_op1076 = frozenset([77])
    FOLLOW_NOT_in_comp_op1078 = frozenset([1])
    FOLLOW_xor_expr_in_expr1092 = frozenset([1, 12])
    FOLLOW_BIT_OR_in_expr1095 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_xor_expr_in_expr1097 = frozenset([1, 12])
    FOLLOW_and_expr_in_xor_expr1109 = frozenset([1, 126])
    FOLLOW_XOR_in_xor_expr1112 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_and_expr_in_xor_expr1114 = frozenset([1, 126])
    FOLLOW_shift_expr_in_and_expr1126 = frozenset([1, 10])
    FOLLOW_BIT_AND_in_and_expr1129 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_shift_expr_in_and_expr1131 = frozenset([1, 10])
    FOLLOW_arith_expr_in_shift_expr1141 = frozenset([1, 64, 95])
    FOLLOW_set_in_shift_expr1144 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_arith_expr_in_shift_expr1152 = frozenset([1, 64, 95])
    FOLLOW_term_in_arith_expr1162 = frozenset([1, 69, 85])
    FOLLOW_set_in_arith_expr1165 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_term_in_arith_expr1173 = frozenset([1, 69, 85])
    FOLLOW_factor_in_term1189 = frozenset([1, 22, 44, 70, 71])
    FOLLOW_set_in_term1192 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_factor_in_term1208 = frozenset([1, 22, 44, 70, 71])
    FOLLOW_set_in_factor1222 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_factor_in_factor1234 = frozenset([1])
    FOLLOW_power_in_factor1238 = frozenset([1])
    FOLLOW_atom_expr_in_power1251 = frozenset([1, 87])
    FOLLOW_POWER_in_power1254 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_factor_in_power1256 = frozenset([1])
    FOLLOW_atom_in_atom_expr1267 = frozenset([1, 23, 55])
    FOLLOW_trailer_in_atom_expr1272 = frozenset([1, 23, 55])
    FOLLOW_LPAREN_in_atom1282 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_atom1284 = frozenset([94])
    FOLLOW_RPAREN_in_atom1286 = frozenset([1])
    FOLLOW_LBRACK_in_atom1292 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            90,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_testlist_comp_in_atom1295 = frozenset([90])
    FOLLOW_MINUS_in_atom1301 = frozenset([51])
    FOLLOW_INTEGER_in_atom1304 = frozenset([88])
    FOLLOW_RANGE_in_atom1307 = frozenset([51, 69])
    FOLLOW_MINUS_in_atom1310 = frozenset([51])
    FOLLOW_INTEGER_in_atom1313 = frozenset([90])
    FOLLOW_RBRACK_in_atom1317 = frozenset([1])
    FOLLOW_LT_in_atom1323 = frozenset(
        [
            11,
            15,
            31,
            33,
            40,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_vector_comp_in_atom1325 = frozenset([40])
    FOLLOW_GT_in_atom1328 = frozenset([1])
    FOLLOW_LBRACE_in_atom1334 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            89,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_dict_or_set_maker_in_atom1336 = frozenset([89])
    FOLLOW_RBRACE_in_atom1339 = frozenset([1])
    FOLLOW_name_in_atom1345 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom1349 = frozenset([1])
    FOLLOW_distribution_expr_in_atom1353 = frozenset([1])
    FOLLOW_INTEGER_in_atom1359 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom1363 = frozenset([1])
    FOLLOW_STRING_in_atom1367 = frozenset([1])
    FOLLOW_NONE_in_atom1371 = frozenset([1])
    FOLLOW_TRUE_in_atom1375 = frozenset([1])
    FOLLOW_FALSE_in_atom1379 = frozenset([1])
    FOLLOW_distribution_in_distribution_expr1408 = frozenset([63])
    FOLLOW_LPAREN_in_distribution_expr1410 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_arglist_in_distribution_expr1412 = frozenset([94])
    FOLLOW_RPAREN_in_distribution_expr1414 = frozenset([1])
    FOLLOW_test_in_testlist_comp1450 = frozenset([1, 17, 34])
    FOLLOW_comp_for_in_testlist_comp1454 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp1459 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_testlist_comp1461 = frozenset([1, 17])
    FOLLOW_expr_in_vector_comp1473 = frozenset([17])
    FOLLOW_COMMA_in_vector_comp1475 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_expr_in_vector_comp1477 = frozenset([17])
    FOLLOW_COMMA_in_vector_comp1479 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_expr_in_vector_comp1481 = frozenset([1])
    FOLLOW_LBRACK_in_trailer1497 = frozenset(
        [
            11,
            15,
            16,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_subscriptlist_in_trailer1499 = frozenset([90])
    FOLLOW_RBRACK_in_trailer1501 = frozenset([1])
    FOLLOW_DOT_in_trailer1505 = frozenset([43, 120])
    FOLLOW_name_in_trailer1507 = frozenset([1])
    FOLLOW_argument_in_arglist1520 = frozenset([1, 17])
    FOLLOW_COMMA_in_arglist1523 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_argument_in_arglist1525 = frozenset([1, 17])
    FOLLOW_test_in_argument1539 = frozenset([1, 5, 34])
    FOLLOW_comp_for_in_argument1542 = frozenset([1])
    FOLLOW_ASSIGN_in_argument1546 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_argument1548 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist1557 = frozenset([1, 17])
    FOLLOW_COMMA_in_subscriptlist1560 = frozenset(
        [
            11,
            15,
            16,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_subscript__in_subscriptlist1562 = frozenset([1, 17])
    FOLLOW_test_in_subscript_1574 = frozenset([1, 16])
    FOLLOW_COLON_in_subscript_1577 = frozenset(
        [
            1,
            11,
            15,
            16,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_subscript_1580 = frozenset([1, 16])
    FOLLOW_sliceop_in_subscript_1585 = frozenset([1])
    FOLLOW_COLON_in_subscript_1593 = frozenset(
        [
            1,
            11,
            15,
            16,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_subscript_1596 = frozenset([1, 16])
    FOLLOW_sliceop_in_subscript_1601 = frozenset([1])
    FOLLOW_COLON_in_sliceop1616 = frozenset(
        [
            1,
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_sliceop1618 = frozenset([1])
    FOLLOW_expr_in_exprlist1627 = frozenset([1, 17])
    FOLLOW_COMMA_in_exprlist1630 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_expr_in_exprlist1632 = frozenset([1, 17])
    FOLLOW_test_in_testlist1641 = frozenset([1, 17])
    FOLLOW_COMMA_in_testlist1644 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_testlist1646 = frozenset([1, 17])
    FOLLOW_test_in_dict_or_set_maker1656 = frozenset([1, 16, 17, 34])
    FOLLOW_COLON_in_dict_or_set_maker1660 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1662 = frozenset([1, 17, 34])
    FOLLOW_comp_for_in_dict_or_set_maker1665 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1670 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1672 = frozenset([16])
    FOLLOW_COLON_in_dict_or_set_maker1674 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1676 = frozenset([1, 17])
    FOLLOW_comp_for_in_dict_or_set_maker1691 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1696 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_in_dict_or_set_maker1698 = frozenset([1, 17])
    FOLLOW_comp_for_in_comp_iter1712 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter1716 = frozenset([1])
    FOLLOW_FOR_in_comp_for1724 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_exprlist_in_comp_for1726 = frozenset([48])
    FOLLOW_IN_in_comp_for1728 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_or_test_in_comp_for1730 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_for1732 = frozenset([1])
    FOLLOW_IF_in_comp_if1742 = frozenset(
        [
            11,
            15,
            31,
            33,
            43,
            51,
            54,
            55,
            61,
            63,
            65,
            69,
            74,
            76,
            77,
            85,
            101,
            103,
            113,
            119,
            120,
            121,
        ]
    )
    FOLLOW_test_nocond_in_comp_if1744 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_if1746 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
