# $ANTLR 3.5.1 C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g 2023-05-07 22:41:48

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:1: expr_stmt : testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE ;
    def expr_stmt(
        self,
    ):
        retval = self.expr_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:11: ( testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:13: testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt761)
                self.testlist()

                self._state.following.pop()

                if self.input.LA(1) in {ASSIGN, AUG_ASSIGN}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:44: ( testlist | fetch_expr )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if LA38_0 in {
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
                    alt38 = 1
                elif LA38_0 == FETCH:
                    alt38 = 2
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae

                if alt38 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:70:45: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt772)
                    self.testlist()

                    self._state.following.pop()

                elif alt38 == 2:
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:1: aug_expr_stmt : ( ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr );
    def aug_expr_stmt(
        self,
    ):
        retval = self.aug_expr_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:14: ( ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr )
                alt43 = 5
                LA43 = self.input.LA(1)
                if LA43 in {
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:16: ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:72:16: ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:5: testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt792
                    )
                    self.testlist()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:73:14: ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:7: AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE
                        self.match(
                            self.input,
                            AUG_ASSIGN,
                            self.FOLLOW_AUG_ASSIGN_in_aug_expr_stmt802,
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:18: ( testlist | fetch_expr )?
                        alt39 = 3
                        LA39_0 = self.input.LA(1)

                        if LA39_0 in {
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
                            alt39 = 1
                        elif LA39_0 == FETCH:
                            alt39 = 2
                        if alt39 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:19: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt805
                            )
                            self.testlist()

                            self._state.following.pop()

                        elif alt39 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:74:30: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt809
                            )
                            self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_aug_expr_stmt813
                        )

                    elif alt42 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:9: ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt823
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:75:16: ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        alt41 = 5
                        LA41 = self.input.LA(1)
                        if LA41 in {
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
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:9: ( testlist | fetch_expr ) NEWLINE
                            pass
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:9: ( testlist | fetch_expr )
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
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:76:10: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt836
                                )
                                self.testlist()

                                self._state.following.pop()

                            elif alt40 == 2:
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

                        elif alt41 == 2:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:11: create_expr
                            self._state.following.append(
                                self.FOLLOW_create_expr_in_aug_expr_stmt855
                            )
                            self.create_expr()

                            self._state.following.pop()

                        elif alt41 == 3:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:25: instantiate_expr
                            self._state.following.append(
                                self.FOLLOW_instantiate_expr_in_aug_expr_stmt859
                            )
                            self.instantiate_expr()

                            self._state.following.pop()

                        elif alt41 == 4:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:44: get_expr
                            self._state.following.append(
                                self.FOLLOW_get_expr_in_aug_expr_stmt863
                            )
                            self.get_expr()

                            self._state.following.pop()

                        elif alt41 == 5:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:77:55: group_expr
                            self._state.following.append(
                                self.FOLLOW_group_expr_in_aug_expr_stmt867
                            )
                            self.group_expr()

                            self._state.following.pop()

                elif alt43 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:5: create_expr
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_aug_expr_stmt891
                    )
                    self.create_expr()

                    self._state.following.pop()

                elif alt43 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:19: instantiate_expr
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_aug_expr_stmt895
                    )
                    self.instantiate_expr()

                    self._state.following.pop()

                elif alt43 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:81:38: get_expr
                    self._state.following.append(
                        self.FOLLOW_get_expr_in_aug_expr_stmt899
                    )
                    self.get_expr()

                    self._state.following.pop()

                elif alt43 == 5:
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
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if LA44_0 == MATCH:
                    alt44 = 1
                if alt44 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:36: MATCH test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr921)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr923)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:49: ( LIMIT test )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 == LIMIT:
                    alt45 = 1
                if alt45 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:50: LIMIT test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr928)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr930)
                    self.test()

                    self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:84:63: ( RECURSIVE )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 == RECURSIVE:
                    alt46 = 1
                if alt46 == 1:
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:87:1: test : or_test ( IF or_test ELSE test )? ;
    def test(
        self,
    ):
        retval = self.test_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:87:13: ( or_test ( IF or_test ELSE test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:87:15: or_test ( IF or_test ELSE test )?
                self._state.following.append(self.FOLLOW_or_test_in_test952)
                self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:87:23: ( IF or_test ELSE test )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if LA47_0 == IF:
                    alt47 = 1
                if alt47 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:87:24: IF or_test ELSE test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test955)

                    self._state.following.append(self.FOLLOW_or_test_in_test957)
                    self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test959)

                    self._state.following.append(self.FOLLOW_test_in_test961)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:88:1: test_nocond : or_test ;
    def test_nocond(
        self,
    ):
        retval = self.test_nocond_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:88:13: ( or_test )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:88:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond970)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:1: or_test : and_test ( OR and_test )* ;
    def or_test(
        self,
    ):
        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:13: ( and_test ( OR and_test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:15: and_test ( OR and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test981)
                self.and_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:24: ( OR and_test )*
                while True:  # loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if LA48_0 == OR:
                        alt48 = 1

                    if alt48 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:89:25: OR and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test984)

                        self._state.following.append(self.FOLLOW_and_test_in_or_test986)
                        self.and_test()

                        self._state.following.pop()

                    else:
                        break  # loop48

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:90:1: and_test : not_test ( AND not_test )* ;
    def and_test(
        self,
    ):
        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:90:13: ( not_test ( AND not_test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:90:15: not_test ( AND not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test998)
                self.not_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:90:24: ( AND not_test )*
                while True:  # loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if LA49_0 == AND:
                        alt49 = 1

                    if alt49 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:90:25: AND not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test1001)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test1003
                        )
                        self.not_test()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:91:1: not_test : ( NOT not_test | comparison );
    def not_test(
        self,
    ):
        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:91:13: ( NOT not_test | comparison )
                alt50 = 2
                LA50_0 = self.input.LA(1)

                if LA50_0 == NOT:
                    alt50 = 1
                elif LA50_0 in {
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
                    alt50 = 2
                else:
                    nvae = NoViableAltException("", 50, 0, self.input)

                    raise nvae

                if alt50 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:91:15: NOT not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1015)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1017)
                    self.not_test()

                    self._state.following.pop()

                elif alt50 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:91:30: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test1021)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:92:1: comparison : expr ( comp_op expr )* ;
    def comparison(
        self,
    ):
        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:92:13: ( expr ( comp_op expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:92:15: expr ( comp_op expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison1029)
                self.expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:92:20: ( comp_op expr )*
                while True:  # loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if LA51_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt51 = 1

                    if alt51 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:92:21: comp_op expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison1032
                        )
                        self.comp_op()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_expr_in_comparison1034)
                        self.expr()

                        self._state.following.pop()

                    else:
                        break  # loop51

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:1: comp_op : ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT );
    def comp_op(
        self,
    ):
        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:13: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
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
                        alt52 = 9
                    else:
                        nvae = NoViableAltException("", 52, 9, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:15: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_comp_op1047)

                elif alt52 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:20: GT
                    self.match(self.input, GT, self.FOLLOW_GT_in_comp_op1051)

                elif alt52 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:25: EQUALS
                    self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op1055)

                elif alt52 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:34: GT_EQ
                    self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op1059)

                elif alt52 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:42: LT_EQ
                    self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op1063)

                elif alt52 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:50: NOT_EQ
                    self.match(self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op1067)

                elif alt52 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:59: IN
                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1071)

                elif alt52 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:64: NOT IN
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1075)

                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1077)

                elif alt52 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:73: IS
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1081)

                elif alt52 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:93:78: IS NOT
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1085)

                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1087)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:1: expr : xor_expr ( BIT_OR xor_expr )* ;
    def expr(
        self,
    ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:13: ( xor_expr ( BIT_OR xor_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:15: xor_expr ( BIT_OR xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr1101)
                self.xor_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:24: ( BIT_OR xor_expr )*
                while True:  # loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if LA53_0 == BIT_OR:
                        alt53 = 1

                    if alt53 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:94:25: BIT_OR xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr1104)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr1106)
                        self.xor_expr()

                        self._state.following.pop()

                    else:
                        break  # loop53

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:95:1: xor_expr : and_expr ( XOR and_expr )* ;
    def xor_expr(
        self,
    ):
        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:95:13: ( and_expr ( XOR and_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:95:15: and_expr ( XOR and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1118)
                self.and_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:95:24: ( XOR and_expr )*
                while True:  # loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if LA54_0 == XOR:
                        alt54 = 1

                    if alt54 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:95:25: XOR and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr1121)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr1123
                        )
                        self.and_expr()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:96:1: and_expr : shift_expr ( BIT_AND shift_expr )* ;
    def and_expr(
        self,
    ):
        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:96:13: ( shift_expr ( BIT_AND shift_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:96:15: shift_expr ( BIT_AND shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1135)
                self.shift_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:96:26: ( BIT_AND shift_expr )*
                while True:  # loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if LA55_0 == BIT_AND:
                        alt55 = 1

                    if alt55 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:96:27: BIT_AND shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr1138
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr1140
                        )
                        self.shift_expr()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:97:1: shift_expr : arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* ;
    def shift_expr(
        self,
    ):
        retval = self.shift_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:97:13: ( arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:97:15: arith_expr ( ( LSHIFT | RSHIFT ) arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1150)
                self.arith_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:97:26: ( ( LSHIFT | RSHIFT ) arith_expr )*
                while True:  # loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if LA56_0 in {LSHIFT, RSHIFT}:
                        alt56 = 1

                    if alt56 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:97:27: ( LSHIFT | RSHIFT ) arith_expr
                        if self.input.LA(1) in {LSHIFT, RSHIFT}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr1161
                        )
                        self.arith_expr()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:1: arith_expr : term ( ( PLUS | MINUS ) term )* ;
    def arith_expr(
        self,
    ):
        retval = self.arith_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:13: ( term ( ( PLUS | MINUS ) term )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:15: term ( ( PLUS | MINUS ) term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr1171)
                self.term()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:20: ( ( PLUS | MINUS ) term )*
                while True:  # loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if LA57_0 in {MINUS, PLUS}:
                        alt57 = 1

                    if alt57 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:98:21: ( PLUS | MINUS ) term
                        if self.input.LA(1) in {MINUS, PLUS}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_term_in_arith_expr1182)
                        self.term()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:99:1: term : factor ( ( MUL | DIV | MOD | IDIV ) factor )* ;
    def term(
        self,
    ):
        retval = self.term_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:99:13: ( factor ( ( MUL | DIV | MOD | IDIV ) factor )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:99:15: factor ( ( MUL | DIV | MOD | IDIV ) factor )*
                self._state.following.append(self.FOLLOW_factor_in_term1198)
                self.factor()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:99:22: ( ( MUL | DIV | MOD | IDIV ) factor )*
                while True:  # loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if LA58_0 in {DIV, IDIV, MOD, MUL}:
                        alt58 = 1

                    if alt58 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:99:23: ( MUL | DIV | MOD | IDIV ) factor
                        if self.input.LA(1) in {DIV, IDIV, MOD, MUL}:
                            self.input.consume()
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse

                        self._state.following.append(self.FOLLOW_factor_in_term1217)
                        self.factor()

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:1: factor : ( ( PLUS | MINUS | BIT_NOT ) factor | power );
    def factor(
        self,
    ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:13: ( ( PLUS | MINUS | BIT_NOT ) factor | power )
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if LA59_0 in {BIT_NOT, MINUS, PLUS}:
                    alt59 = 1
                elif LA59_0 in {
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
                    alt59 = 2
                else:
                    nvae = NoViableAltException("", 59, 0, self.input)

                    raise nvae

                if alt59 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:15: ( PLUS | MINUS | BIT_NOT ) factor
                    if self.input.LA(1) in {BIT_NOT, MINUS, PLUS}:
                        self.input.consume()
                        self._state.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        raise mse

                    self._state.following.append(self.FOLLOW_factor_in_factor1243)
                    self.factor()

                    self._state.following.pop()

                elif alt59 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:100:49: power
                    self._state.following.append(self.FOLLOW_power_in_factor1247)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:1: power : atom_expr ( POWER factor )? ;
    def power(
        self,
    ):
        retval = self.power_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:13: ( atom_expr ( POWER factor )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power1260)
                self.atom_expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:25: ( POWER factor )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if LA60_0 == POWER:
                    alt60 = 1
                if alt60 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:101:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power1263)

                    self._state.following.append(self.FOLLOW_factor_in_power1265)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:1: atom_expr : atom ( trailer )* ;
    def atom_expr(
        self,
    ):
        retval = self.atom_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:13: ( atom ( trailer )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:15: atom ( trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr1276)
                self.atom()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:20: ( trailer )*
                while True:  # loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if LA61_0 in {DOT, LBRACK}:
                        alt61 = 1

                    if alt61 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:102:23: trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr1281
                        )
                        self.trailer()

                        self._state.following.pop()

                    else:
                        break  # loop61

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:1: atom : ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | LEN LPAREN test RPAREN | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE );
    def atom(
        self,
    ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:103:5: ( LPAREN test RPAREN | LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK | LT ( vector_comp )? GT | LBRACE ( dict_or_set_maker )? RBRACE | LEN LPAREN test RPAREN | name | SETTING_ID | distribution_expr | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE )
                alt68 = 14
                LA68 = self.input.LA(1)
                if LA68 in {LPAREN}:
                    alt68 = 1
                elif LA68 in {LBRACK}:
                    alt68 = 2
                elif LA68 in {LT}:
                    alt68 = 3
                elif LA68 in {LBRACE}:
                    alt68 = 4
                elif LA68 in {LEN}:
                    alt68 = 5
                elif LA68 in {ID, UNDERSCORE}:
                    alt68 = 6
                elif LA68 in {SETTING_ID}:
                    alt68 = 7
                elif LA68 in {DISTRIBUTION}:
                    alt68 = 8
                elif LA68 in {INTEGER}:
                    alt68 = 9
                elif LA68 in {FLOAT_NUMBER}:
                    alt68 = 10
                elif LA68 in {STRING}:
                    alt68 = 11
                elif LA68 in {NONE}:
                    alt68 = 12
                elif LA68 in {TRUE}:
                    alt68 = 13
                elif LA68 in {FALSE}:
                    alt68 = 14
                else:
                    nvae = NoViableAltException("", 68, 0, self.input)

                    raise nvae

                if alt68 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:104:3: LPAREN test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1291)

                    self._state.following.append(self.FOLLOW_test_in_atom1293)
                    self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1295)

                elif alt68 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:5: LBRACK ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) ) RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom1301)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:12: ( ( testlist_comp )? | ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER ) )
                    alt65 = 2
                    LA65 = self.input.LA(1)
                    if LA65 in {
                        BIT_NOT,
                        DISTRIBUTION,
                        FALSE,
                        FLOAT_NUMBER,
                        ID,
                        LBRACE,
                        LBRACK,
                        LEN,
                        LPAREN,
                        LT,
                        NONE,
                        NOT,
                        PLUS,
                        RBRACK,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt65 = 1
                    elif LA65 in {MINUS}:
                        LA65_2 = self.input.LA(2)

                        if LA65_2 in {
                            BIT_NOT,
                            DISTRIBUTION,
                            FALSE,
                            FLOAT_NUMBER,
                            ID,
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:13: ( testlist_comp )?
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:13: ( testlist_comp )?
                        alt62 = 2
                        LA62_0 = self.input.LA(1)

                        if LA62_0 in {
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
                            alt62 = 1
                        if alt62 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:13: testlist_comp
                            self._state.following.append(
                                self.FOLLOW_testlist_comp_in_atom1304
                            )
                            self.testlist_comp()

                            self._state.following.pop()

                    elif alt65 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:30: ( ( MINUS )? INTEGER ) RANGE ( ( MINUS )? INTEGER )
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:30: ( ( MINUS )? INTEGER )
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:31: ( MINUS )? INTEGER
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:31: ( MINUS )?
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if LA63_0 == MINUS:
                            alt63 = 1
                        if alt63 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:31: MINUS
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1310)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1313)

                        self.match(self.input, RANGE, self.FOLLOW_RANGE_in_atom1316)

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:53: ( ( MINUS )? INTEGER )
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:54: ( MINUS )? INTEGER
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:54: ( MINUS )?
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if LA64_0 == MINUS:
                            alt64 = 1
                        if alt64 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:105:54: MINUS
                            self.match(self.input, MINUS, self.FOLLOW_MINUS_in_atom1319)

                        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1322)

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom1326)

                elif alt68 == 3:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom1332)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:8: ( vector_comp )?
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if LA66_0 in {
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
                        alt66 = 1
                    if alt66 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:106:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom1334
                        )
                        self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom1337)

                elif alt68 == 4:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom1343)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:12: ( dict_or_set_maker )?
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if LA67_0 in {
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
                        alt67 = 1
                    if alt67 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:107:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom1345
                        )
                        self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom1348)

                elif alt68 == 5:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:108:5: LEN LPAREN test RPAREN
                    self.match(self.input, LEN, self.FOLLOW_LEN_in_atom1354)

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1356)

                    self._state.following.append(self.FOLLOW_test_in_atom1358)
                    self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1360)

                elif alt68 == 6:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom1366)
                    self.name()

                    self._state.following.pop()

                elif alt68 == 7:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:12: SETTING_ID
                    self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom1370
                    )

                elif alt68 == 8:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:109:25: distribution_expr
                    self._state.following.append(
                        self.FOLLOW_distribution_expr_in_atom1374
                    )
                    self.distribution_expr()

                    self._state.following.pop()

                elif alt68 == 9:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:5: INTEGER
                    self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1380)

                elif alt68 == 10:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:15: FLOAT_NUMBER
                    self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom1384
                    )

                elif alt68 == 11:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:30: STRING
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_atom1388)

                elif alt68 == 12:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:39: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom1392)

                elif alt68 == 13:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:46: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom1396)

                elif alt68 == 14:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:110:53: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom1400)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:1: name : ( ID | UNDERSCORE );
    def name(
        self,
    ):
        retval = self.name_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:113:5: ( ID | UNDERSCORE )
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:126:1: distribution_expr : DISTRIBUTION LPAREN arglist RPAREN ;
    def distribution_expr(
        self,
    ):
        retval = self.distribution_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:126:19: ( DISTRIBUTION LPAREN arglist RPAREN )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:126:21: DISTRIBUTION LPAREN arglist RPAREN
                self.match(
                    self.input,
                    DISTRIBUTION,
                    self.FOLLOW_DISTRIBUTION_in_distribution_expr1429,
                )

                self.match(
                    self.input, LPAREN, self.FOLLOW_LPAREN_in_distribution_expr1431
                )

                self._state.following.append(
                    self.FOLLOW_arglist_in_distribution_expr1433
                )
                self.arglist()

                self._state.following.pop()

                self.match(
                    self.input, RPAREN, self.FOLLOW_RPAREN_in_distribution_expr1435
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "distribution_expr"

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:1: testlist_comp : test ( comp_for | ( COMMA test )* ) ;
    def testlist_comp(
        self,
    ):
        retval = self.testlist_comp_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:15: ( test ( comp_for | ( COMMA test )* ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:17: test ( comp_for | ( COMMA test )* )
                self._state.following.append(self.FOLLOW_test_in_testlist_comp1443)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:22: ( comp_for | ( COMMA test )* )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:24: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp1447
                    )
                    self.comp_for()

                    self._state.following.pop()

                elif alt70 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:35: ( COMMA test )*
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:35: ( COMMA test )*
                    while True:  # loop69
                        alt69 = 2
                        LA69_0 = self.input.LA(1)

                        if LA69_0 == COMMA:
                            alt69 = 1

                        if alt69 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:128:36: COMMA test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp1452,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp1454
                            )
                            self.test()

                            self._state.following.pop()

                        else:
                            break  # loop69

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:129:1: vector_comp : expr COMMA expr COMMA expr ;
    def vector_comp(
        self,
    ):
        retval = self.vector_comp_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:129:15: ( expr COMMA expr COMMA expr )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:129:17: expr COMMA expr COMMA expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp1466)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1468)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1470)
                self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp1472)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp1474)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:131:1: trailer : ( LBRACK subscriptlist RBRACK | DOT ( name | AXIS ) );
    def trailer(
        self,
    ):
        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:131:15: ( LBRACK subscriptlist RBRACK | DOT ( name | AXIS ) )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:131:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer1490)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer1492
                    )
                    self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer1494)

                elif alt72 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:131:47: DOT ( name | AXIS )
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer1498)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:131:51: ( name | AXIS )
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if LA71_0 in {ID, UNDERSCORE}:
                        alt71 = 1
                    elif LA71_0 == AXIS:
                        alt71 = 2
                    else:
                        nvae = NoViableAltException("", 71, 0, self.input)

                        raise nvae

                    if alt71 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:131:52: name
                        self._state.following.append(self.FOLLOW_name_in_trailer1501)
                        self.name()

                        self._state.following.pop()

                    elif alt71 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:131:60: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_trailer1506)

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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:132:1: arglist : argument ( COMMA argument )* ;
    def arglist(
        self,
    ):
        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:132:15: ( argument ( COMMA argument )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:132:17: argument ( COMMA argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist1520)
                self.argument()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:132:26: ( COMMA argument )*
                while True:  # loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if LA73_0 == COMMA:
                        alt73 = 1

                    if alt73 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:132:27: COMMA argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist1523)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist1525
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:133:1: argument : test ( comp_for | ASSIGN test )? ;
    def argument(
        self,
    ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:133:15: ( test ( comp_for | ASSIGN test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:133:17: test ( comp_for | ASSIGN test )?
                self._state.following.append(self.FOLLOW_test_in_argument1539)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:133:22: ( comp_for | ASSIGN test )?
                alt74 = 3
                LA74_0 = self.input.LA(1)

                if LA74_0 == FOR:
                    alt74 = 1
                elif LA74_0 == ASSIGN:
                    alt74 = 2
                if alt74 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:133:23: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_argument1542)
                    self.comp_for()

                    self._state.following.pop()

                elif alt74 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:133:34: ASSIGN test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument1546)

                    self._state.following.append(self.FOLLOW_test_in_argument1548)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:134:1: subscriptlist : subscript_ ( COMMA subscript_ )* ;
    def subscriptlist(
        self,
    ):
        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:134:15: ( subscript_ ( COMMA subscript_ )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:134:17: subscript_ ( COMMA subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist1557
                )
                self.subscript_()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:134:28: ( COMMA subscript_ )*
                while True:  # loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if LA75_0 == COMMA:
                        alt75 = 1

                    if alt75 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:134:29: COMMA subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist1560
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist1562
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:1: subscript_ : ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? );
    def subscript_(
        self,
    ):
        retval = self.subscript__return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:15: ( test ( COLON ( test )? ( sliceop )? )? | COLON ( test )? ( sliceop )? )
                alt81 = 2
                LA81_0 = self.input.LA(1)

                if LA81_0 in {
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
                    alt81 = 1
                elif LA81_0 == COLON:
                    alt81 = 2
                else:
                    nvae = NoViableAltException("", 81, 0, self.input)

                    raise nvae

                if alt81 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:17: test ( COLON ( test )? ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_1574)
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:22: ( COLON ( test )? ( sliceop )? )?
                    alt78 = 2
                    LA78_0 = self.input.LA(1)

                    if LA78_0 == COLON:
                        alt78 = 1
                    if alt78 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:23: COLON ( test )? ( sliceop )?
                        self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_1577
                        )

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:29: ( test )?
                        alt76 = 2
                        LA76_0 = self.input.LA(1)

                        if LA76_0 in {
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
                            alt76 = 1
                        if alt76 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:30: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_1580
                            )
                            self.test()

                            self._state.following.pop()

                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:37: ( sliceop )?
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if LA77_0 == COLON:
                            alt77 = 1
                        if alt77 == 1:
                            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:38: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_1585
                            )
                            self.sliceop()

                            self._state.following.pop()

                elif alt81 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:52: COLON ( test )? ( sliceop )?
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_subscript_1593)

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:58: ( test )?
                    alt79 = 2
                    LA79_0 = self.input.LA(1)

                    if LA79_0 in {
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
                        alt79 = 1
                    if alt79 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:59: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_1596)
                        self.test()

                        self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:66: ( sliceop )?
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if LA80_0 == COLON:
                        alt80 = 1
                    if alt80 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:135:67: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_1601
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:136:1: sliceop : COLON ( test )? ;
    def sliceop(
        self,
    ):
        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:136:15: ( COLON ( test )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:136:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop1616)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:136:23: ( test )?
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if LA82_0 in {
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
                    alt82 = 1
                if alt82 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:136:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop1618)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:1: exprlist : expr ( COMMA expr )* ;
    def exprlist(
        self,
    ):
        retval = self.exprlist_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:10: ( expr ( COMMA expr )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:12: expr ( COMMA expr )*
                self._state.following.append(self.FOLLOW_expr_in_exprlist1627)
                self.expr()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:17: ( COMMA expr )*
                while True:  # loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if LA83_0 == COMMA:
                        alt83 = 1

                    if alt83 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:138:18: COMMA expr
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist1630)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist1632)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:1: testlist : test ( COMMA test )* ;
    def testlist(
        self,
    ):
        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:10: ( test ( COMMA test )* )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:12: test ( COMMA test )*
                self._state.following.append(self.FOLLOW_test_in_testlist1641)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:17: ( COMMA test )*
                while True:  # loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if LA84_0 == COMMA:
                        alt84 = 1

                    if alt84 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:139:18: COMMA test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist1644)

                        self._state.following.append(self.FOLLOW_test_in_testlist1646)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:140:1: dict_or_set_maker : test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) ;
    def dict_or_set_maker(
        self,
    ):
        retval = self.dict_or_set_maker_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:140:18: ( test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:3: test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker1656)
                self.test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:8: ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:10: COLON test ( comp_for | ( COMMA test COLON test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker1660
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker1662
                    )
                    self.test()

                    self._state.following.pop()

                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:21: ( comp_for | ( COMMA test COLON test )* )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:22: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1665
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt86 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:33: ( COMMA test COLON test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:33: ( COMMA test COLON test )*
                        while True:  # loop85
                            alt85 = 2
                            LA85_0 = self.input.LA(1)

                            if LA85_0 == COMMA:
                                alt85 = 1

                            if alt85 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:141:34: COMMA test COLON test
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
                                break  # loop85

                elif alt89 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:10: ( comp_for | ( COMMA test )* )
                    pass
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:10: ( comp_for | ( COMMA test )* )
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
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:11: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker1691
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt88 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:22: ( COMMA test )*
                        pass
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:22: ( COMMA test )*
                        while True:  # loop87
                            alt87 = 2
                            LA87_0 = self.input.LA(1)

                            if LA87_0 == COMMA:
                                alt87 = 1

                            if alt87 == 1:
                                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:142:23: COMMA test
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:1: comp_iter : ( comp_for | comp_if );
    def comp_iter(
        self,
    ):
        retval = self.comp_iter_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:11: ( comp_for | comp_if )
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
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:13: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter1712)
                    self.comp_for()

                    self._state.following.pop()

                elif alt90 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:145:24: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter1716)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:1: comp_for : FOR exprlist IN or_test ( comp_iter )? ;
    def comp_for(
        self,
    ):
        retval = self.comp_for_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:11: ( FOR exprlist IN or_test ( comp_iter )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:13: FOR exprlist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for1724)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for1726)
                self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for1728)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for1730)
                self.or_test()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:37: ( comp_iter )?
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if LA91_0 in {FOR, IF}:
                    alt91 = 1
                if alt91 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:146:37: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for1732)
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
    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:1: comp_if : IF test_nocond ( comp_iter )? ;
    def comp_if(
        self,
    ):
        retval = self.comp_if_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:11: ( IF test_nocond ( comp_iter )? )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if1742)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if1744)
                self.test_nocond()

                self._state.following.pop()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:28: ( comp_iter )?
                alt92 = 2
                LA92_0 = self.input.LA(1)

                if LA92_0 in {FOR, IF}:
                    alt92 = 1
                if alt92 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcParser.g:147:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if1746)
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

    FOLLOW_declaration_in_scenario44 = frozenset([1, 73, 100, 109, 122])
    FOLLOW_NEWLINE_in_scenario46 = frozenset([1, 73, 100, 109, 122])
    FOLLOW_settings_in_scenario49 = frozenset([1, 109, 122])
    FOLLOW_stage_in_scenario52 = frozenset([1, 122])
    FOLLOW_writers_in_scenario55 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration65 = frozenset([43, 118])
    FOLLOW_name_in_declaration67 = frozenset([15, 73])
    FOLLOW_COLON_in_declaration70 = frozenset([43, 118])
    FOLLOW_name_in_declaration72 = frozenset([73])
    FOLLOW_NEWLINE_in_declaration76 = frozenset([1])
    FOLLOW_SETTINGS_in_settings86 = frozenset([15])
    FOLLOW_COLON_in_settings88 = frozenset([73])
    FOLLOW_NEWLINE_in_settings90 = frozenset([49])
    FOLLOW_INDENT_in_settings92 = frozenset([43])
    FOLLOW_option_in_settings94 = frozenset([19, 43])
    FOLLOW_DEDENT_in_settings97 = frozenset([1])
    FOLLOW_STAGE_in_stage110 = frozenset([15])
    FOLLOW_COLON_in_stage112 = frozenset([73])
    FOLLOW_NEWLINE_in_stage114 = frozenset([49])
    FOLLOW_INDENT_in_stage116 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_stmts_in_stage118 = frozenset([19])
    FOLLOW_DEDENT_in_stage120 = frozenset([1])
    FOLLOW_WRITERS_in_writers131 = frozenset([15])
    FOLLOW_COLON_in_writers133 = frozenset([73])
    FOLLOW_NEWLINE_in_writers135 = frozenset([49])
    FOLLOW_INDENT_in_writers137 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_stmt_in_writers140 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_writer_in_writers144 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_DEDENT_in_writers148 = frozenset([1])
    FOLLOW_ID_in_option156 = frozenset([5])
    FOLLOW_ASSIGN_in_option158 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_option160 = frozenset([73])
    FOLLOW_NEWLINE_in_option162 = frozenset([1])
    FOLLOW_open_stmt_in_stmts170 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_aug_expr_stmt_in_stmts174 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_edit_stmt_in_stmts178 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_behavior_stmt_in_stmts182 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_ID_in_writer191 = frozenset([15])
    FOLLOW_COLON_in_writer193 = frozenset([73])
    FOLLOW_NEWLINE_in_writer195 = frozenset([49])
    FOLLOW_INDENT_in_writer197 = frozenset([43])
    FOLLOW_option_in_writer199 = frozenset([19, 43])
    FOLLOW_DEDENT_in_writer202 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt214 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_open_stmt216 = frozenset([73])
    FOLLOW_NEWLINE_in_open_stmt218 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt225 = frozenset([43, 114, 118])
    FOLLOW_TIMELINE_in_edit_stmt228 = frozenset([15])
    FOLLOW_name_in_edit_stmt232 = frozenset([15])
    FOLLOW_edit_block_in_edit_stmt235 = frozenset([1])
    FOLLOW_CREATE_in_create_expr244 = frozenset(
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
            110,
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_create_expr246 = frozenset([13, 37, 59, 68, 102, 103, 110])
    FOLLOW_STEREO_in_create_expr256 = frozenset([13])
    FOLLOW_CAMERA_in_create_expr259 = frozenset([15, 73])
    FOLLOW_shapes_in_create_expr263 = frozenset([15, 73])
    FOLLOW_light_type_in_create_expr267 = frozenset([58])
    FOLLOW_LIGHT_in_create_expr269 = frozenset([15, 73])
    FOLLOW_FROM_in_create_expr273 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_create_expr275 = frozenset([15, 73])
    FOLLOW_edit_block_in_create_expr279 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr283 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr292 = frozenset([15])
    FOLLOW_simple_block_in_create_expr295 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr336 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_instantiate_expr339 = frozenset([37])
    FOLLOW_FROM_in_instantiate_expr343 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_instantiate_expr345 = frozenset([15, 73])
    FOLLOW_edit_block_in_instantiate_expr348 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr352 = frozenset([1])
    FOLLOW_GROUP_in_group_expr366 = frozenset([55])
    FOLLOW_LBRACK_in_group_expr368 = frozenset([43, 118])
    FOLLOW_name_in_group_expr370 = frozenset([16, 89])
    FOLLOW_COMMA_in_group_expr373 = frozenset([43, 118])
    FOLLOW_name_in_group_expr375 = frozenset([16, 89])
    FOLLOW_RBRACK_in_group_expr379 = frozenset([15, 73])
    FOLLOW_edit_block_in_group_expr382 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr386 = frozenset([1])
    FOLLOW_GET_in_get_expr402 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_CAMERA_in_get_expr406 = frozenset([6])
    FOLLOW_LIGHT_in_get_expr410 = frozenset([6])
    FOLLOW_MATERIAL_in_get_expr414 = frozenset([6])
    FOLLOW_name_in_get_expr418 = frozenset([6])
    FOLLOW_AT_in_get_expr421 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_get_expr425 = frozenset([15, 73])
    FOLLOW_simple_block_in_get_expr428 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr432 = frozenset([1])
    FOLLOW_COLON_in_edit_block443 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_block445 = frozenset([49])
    FOLLOW_INDENT_in_edit_block447 = frozenset(
        [14, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 116, 118, 120, 121]
    )
    FOLLOW_attr_in_edit_block450 = frozenset(
        [14, 19, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 116, 118, 120, 121]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block454 = frozenset(
        [14, 19, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 116, 118, 120, 121]
    )
    FOLLOW_DEDENT_in_edit_block458 = frozenset([1])
    FOLLOW_COLON_in_simple_block465 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_block467 = frozenset([49])
    FOLLOW_INDENT_in_simple_block469 = frozenset([43, 118])
    FOLLOW_simple_attr_in_simple_block471 = frozenset([19, 43, 118])
    FOLLOW_DEDENT_in_simple_block474 = frozenset([1])
    FOLLOW_core_attr_in_attr491 = frozenset([1])
    FOLLOW_simple_attr_in_attr495 = frozenset([1])
    FOLLOW_compound_attr_in_attr499 = frozenset([1])
    FOLLOW_name_in_simple_attr508 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_COLON_in_simple_attr511 = frozenset([43, 118])
    FOLLOW_name_in_simple_attr513 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_simple_attr517 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_attr520 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr529 = frozenset([79])
    FOLLOW_ON_in_compound_attr531 = frozenset([43, 118])
    FOLLOW_name_in_compound_attr533 = frozenset([15, 73])
    FOLLOW_ROT_AROUND_in_compound_attr537 = frozenset([43, 118])
    FOLLOW_name_in_compound_attr539 = frozenset([15, 73])
    FOLLOW_PHYSICS_in_compound_attr543 = frozenset([15, 73])
    FOLLOW_simple_block_in_compound_attr547 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr551 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr568 = frozenset([8, 115])
    FOLLOW_AXIS_in_core_attr570 = frozenset([115])
    FOLLOW_TO_in_core_attr573 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr575 = frozenset([73])
    FOLLOW_CAM_TRANSLATE_in_core_attr583 = frozenset([115])
    FOLLOW_TO_in_core_attr585 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr587 = frozenset([73])
    FOLLOW_ROTATE_in_core_attr595 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_AXIS_in_core_attr597 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr600 = frozenset([73, 82])
    FOLLOW_ORDER_in_core_attr602 = frozenset([73])
    FOLLOW_SCALE_in_core_attr611 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr613 = frozenset([73])
    FOLLOW_LOOK_AT_in_core_attr621 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr623 = frozenset([73])
    FOLLOW_UP_AXIS_in_core_attr631 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr633 = frozenset([73])
    FOLLOW_SIZE_in_core_attr641 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr643 = frozenset([73])
    FOLLOW_SEMANTICS_in_core_attr651 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr653 = frozenset([73])
    FOLLOW_VISIBLE_in_core_attr661 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_core_attr663 = frozenset([73])
    FOLLOW_NEWLINE_in_core_attr669 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt679 = frozenset([15])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt681 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block688 = frozenset([73])
    FOLLOW_NEWLINE_in_inner_behavior_block690 = frozenset([49])
    FOLLOW_INDENT_in_inner_behavior_block692 = frozenset(
        [14, 43, 62, 83, 91, 92, 95, 96, 98, 105, 116, 118, 120, 121]
    )
    FOLLOW_attr_in_inner_behavior_block694 = frozenset(
        [14, 19, 43, 62, 83, 91, 92, 95, 96, 98, 105, 116, 118, 120, 121]
    )
    FOLLOW_DEDENT_in_inner_behavior_block697 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt708 = frozenset([15])
    FOLLOW_behavior_block_in_behavior_stmt710 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr718 = frozenset(
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
            111,
            113,
            117,
            118,
        ]
    )
    FOLLOW_test_in_behavior_expr720 = frozenset([36, 113])
    FOLLOW_set_in_behavior_expr723 = frozenset([1])
    FOLLOW_COLON_in_behavior_block736 = frozenset([73])
    FOLLOW_NEWLINE_in_behavior_block738 = frozenset([49])
    FOLLOW_INDENT_in_behavior_block740 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_aug_expr_stmt_in_behavior_block743 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_edit_stmt_in_behavior_block747 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_DEDENT_in_behavior_block751 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt761 = frozenset([5, 7])
    FOLLOW_set_in_expr_stmt763 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_testlist_in_expr_stmt772 = frozenset([73])
    FOLLOW_fetch_expr_in_expr_stmt776 = frozenset([73])
    FOLLOW_NEWLINE_in_expr_stmt779 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt792 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_aug_expr_stmt802 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt805 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt809 = frozenset([73])
    FOLLOW_NEWLINE_in_aug_expr_stmt813 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt823 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt836 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt840 = frozenset([73])
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
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_fetch_expr914 = frozenset([37])
    FOLLOW_FROM_in_fetch_expr916 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_fetch_expr918 = frozenset([1, 60, 67, 90])
    FOLLOW_MATCH_in_fetch_expr921 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_fetch_expr923 = frozenset([1, 60, 90])
    FOLLOW_LIMIT_in_fetch_expr928 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_fetch_expr930 = frozenset([1, 90])
    FOLLOW_RECURSIVE_in_fetch_expr934 = frozenset([1])
    FOLLOW_or_test_in_test952 = frozenset([1, 47])
    FOLLOW_IF_in_test955 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_or_test_in_test957 = frozenset([26])
    FOLLOW_ELSE_in_test959 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_test961 = frozenset([1])
    FOLLOW_or_test_in_test_nocond970 = frozenset([1])
    FOLLOW_and_test_in_or_test981 = frozenset([1, 81])
    FOLLOW_OR_in_or_test984 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_and_test_in_or_test986 = frozenset([1, 81])
    FOLLOW_not_test_in_and_test998 = frozenset([1, 4])
    FOLLOW_AND_in_and_test1001 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_not_test_in_and_test1003 = frozenset([1, 4])
    FOLLOW_NOT_in_not_test1015 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_not_test_in_not_test1017 = frozenset([1])
    FOLLOW_comparison_in_not_test1021 = frozenset([1])
    FOLLOW_expr_in_comparison1029 = frozenset([1, 27, 40, 41, 48, 53, 65, 66, 76, 77])
    FOLLOW_comp_op_in_comparison1032 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_in_comparison1034 = frozenset([1, 27, 40, 41, 48, 53, 65, 66, 76, 77])
    FOLLOW_LT_in_comp_op1047 = frozenset([1])
    FOLLOW_GT_in_comp_op1051 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op1055 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op1059 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op1063 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op1067 = frozenset([1])
    FOLLOW_IN_in_comp_op1071 = frozenset([1])
    FOLLOW_NOT_in_comp_op1075 = frozenset([48])
    FOLLOW_IN_in_comp_op1077 = frozenset([1])
    FOLLOW_IS_in_comp_op1081 = frozenset([1])
    FOLLOW_IS_in_comp_op1085 = frozenset([76])
    FOLLOW_NOT_in_comp_op1087 = frozenset([1])
    FOLLOW_xor_expr_in_expr1101 = frozenset([1, 12])
    FOLLOW_BIT_OR_in_expr1104 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_xor_expr_in_expr1106 = frozenset([1, 12])
    FOLLOW_and_expr_in_xor_expr1118 = frozenset([1, 123])
    FOLLOW_XOR_in_xor_expr1121 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_and_expr_in_xor_expr1123 = frozenset([1, 123])
    FOLLOW_shift_expr_in_and_expr1135 = frozenset([1, 10])
    FOLLOW_BIT_AND_in_and_expr1138 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_shift_expr_in_and_expr1140 = frozenset([1, 10])
    FOLLOW_arith_expr_in_shift_expr1150 = frozenset([1, 64, 94])
    FOLLOW_set_in_shift_expr1153 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_arith_expr_in_shift_expr1161 = frozenset([1, 64, 94])
    FOLLOW_term_in_arith_expr1171 = frozenset([1, 69, 84])
    FOLLOW_set_in_arith_expr1174 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_term_in_arith_expr1182 = frozenset([1, 69, 84])
    FOLLOW_factor_in_term1198 = frozenset([1, 22, 44, 70, 71])
    FOLLOW_set_in_term1201 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_factor_in_term1217 = frozenset([1, 22, 44, 70, 71])
    FOLLOW_set_in_factor1231 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_factor_in_factor1243 = frozenset([1])
    FOLLOW_power_in_factor1247 = frozenset([1])
    FOLLOW_atom_expr_in_power1260 = frozenset([1, 86])
    FOLLOW_POWER_in_power1263 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_factor_in_power1265 = frozenset([1])
    FOLLOW_atom_in_atom_expr1276 = frozenset([1, 23, 55])
    FOLLOW_trailer_in_atom_expr1281 = frozenset([1, 23, 55])
    FOLLOW_LPAREN_in_atom1291 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_atom1293 = frozenset([93])
    FOLLOW_RPAREN_in_atom1295 = frozenset([1])
    FOLLOW_LBRACK_in_atom1301 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_testlist_comp_in_atom1304 = frozenset([89])
    FOLLOW_MINUS_in_atom1310 = frozenset([51])
    FOLLOW_INTEGER_in_atom1313 = frozenset([87])
    FOLLOW_RANGE_in_atom1316 = frozenset([51, 69])
    FOLLOW_MINUS_in_atom1319 = frozenset([51])
    FOLLOW_INTEGER_in_atom1322 = frozenset([89])
    FOLLOW_RBRACK_in_atom1326 = frozenset([1])
    FOLLOW_LT_in_atom1332 = frozenset(
        [11, 21, 31, 33, 40, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_vector_comp_in_atom1334 = frozenset([40])
    FOLLOW_GT_in_atom1337 = frozenset([1])
    FOLLOW_LBRACE_in_atom1343 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_dict_or_set_maker_in_atom1345 = frozenset([88])
    FOLLOW_RBRACE_in_atom1348 = frozenset([1])
    FOLLOW_LEN_in_atom1354 = frozenset([63])
    FOLLOW_LPAREN_in_atom1356 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_atom1358 = frozenset([93])
    FOLLOW_RPAREN_in_atom1360 = frozenset([1])
    FOLLOW_name_in_atom1366 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom1370 = frozenset([1])
    FOLLOW_distribution_expr_in_atom1374 = frozenset([1])
    FOLLOW_INTEGER_in_atom1380 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom1384 = frozenset([1])
    FOLLOW_STRING_in_atom1388 = frozenset([1])
    FOLLOW_NONE_in_atom1392 = frozenset([1])
    FOLLOW_TRUE_in_atom1396 = frozenset([1])
    FOLLOW_FALSE_in_atom1400 = frozenset([1])
    FOLLOW_DISTRIBUTION_in_distribution_expr1429 = frozenset([63])
    FOLLOW_LPAREN_in_distribution_expr1431 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_arglist_in_distribution_expr1433 = frozenset([93])
    FOLLOW_RPAREN_in_distribution_expr1435 = frozenset([1])
    FOLLOW_test_in_testlist_comp1443 = frozenset([1, 16, 34])
    FOLLOW_comp_for_in_testlist_comp1447 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp1452 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_testlist_comp1454 = frozenset([1, 16])
    FOLLOW_expr_in_vector_comp1466 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp1468 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_in_vector_comp1470 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp1472 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_in_vector_comp1474 = frozenset([1])
    FOLLOW_LBRACK_in_trailer1490 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_subscriptlist_in_trailer1492 = frozenset([89])
    FOLLOW_RBRACK_in_trailer1494 = frozenset([1])
    FOLLOW_DOT_in_trailer1498 = frozenset([8, 43, 118])
    FOLLOW_name_in_trailer1501 = frozenset([1])
    FOLLOW_AXIS_in_trailer1506 = frozenset([1])
    FOLLOW_argument_in_arglist1520 = frozenset([1, 16])
    FOLLOW_COMMA_in_arglist1523 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_argument_in_arglist1525 = frozenset([1, 16])
    FOLLOW_test_in_argument1539 = frozenset([1, 5, 34])
    FOLLOW_comp_for_in_argument1542 = frozenset([1])
    FOLLOW_ASSIGN_in_argument1546 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_argument1548 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist1557 = frozenset([1, 16])
    FOLLOW_COMMA_in_subscriptlist1560 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_subscript__in_subscriptlist1562 = frozenset([1, 16])
    FOLLOW_test_in_subscript_1574 = frozenset([1, 15])
    FOLLOW_COLON_in_subscript_1577 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_subscript_1580 = frozenset([1, 15])
    FOLLOW_sliceop_in_subscript_1585 = frozenset([1])
    FOLLOW_COLON_in_subscript_1593 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_subscript_1596 = frozenset([1, 15])
    FOLLOW_sliceop_in_subscript_1601 = frozenset([1])
    FOLLOW_COLON_in_sliceop1616 = frozenset(
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
            111,
            117,
            118,
        ]
    )
    FOLLOW_test_in_sliceop1618 = frozenset([1])
    FOLLOW_expr_in_exprlist1627 = frozenset([1, 16])
    FOLLOW_COMMA_in_exprlist1630 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_expr_in_exprlist1632 = frozenset([1, 16])
    FOLLOW_test_in_testlist1641 = frozenset([1, 16])
    FOLLOW_COMMA_in_testlist1644 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_testlist1646 = frozenset([1, 16])
    FOLLOW_test_in_dict_or_set_maker1656 = frozenset([1, 15, 16, 34])
    FOLLOW_COLON_in_dict_or_set_maker1660 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_dict_or_set_maker1662 = frozenset([1, 16, 34])
    FOLLOW_comp_for_in_dict_or_set_maker1665 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1670 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_dict_or_set_maker1672 = frozenset([15])
    FOLLOW_COLON_in_dict_or_set_maker1674 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_dict_or_set_maker1676 = frozenset([1, 16])
    FOLLOW_comp_for_in_dict_or_set_maker1691 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker1696 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_test_in_dict_or_set_maker1698 = frozenset([1, 16])
    FOLLOW_comp_for_in_comp_iter1712 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter1716 = frozenset([1])
    FOLLOW_FOR_in_comp_for1724 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 111, 117, 118]
    )
    FOLLOW_exprlist_in_comp_for1726 = frozenset([48])
    FOLLOW_IN_in_comp_for1728 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
    )
    FOLLOW_or_test_in_comp_for1730 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_for1732 = frozenset([1])
    FOLLOW_IF_in_comp_if1742 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 111, 117, 118]
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
