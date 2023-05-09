# $ANTLR 3.5.1 /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g 2023-05-09 10:40:54

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


class YarcParser(Parser):
    grammarFileName = "/media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g"
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:1: scenario : declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st);
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
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:10: ( declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:12: declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )?
                self._state.following.append(self.FOLLOW_declaration_in_scenario44)
                declaration1 = self.declaration()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:24: ( NEWLINE )*
                while True:  # loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if LA1_0 == NEWLINE:
                        alt1 = 1

                    if alt1 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:24: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario46
                        )

                    else:
                        break  # loop1

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:33: ( settings )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if LA2_0 == SETTINGS:
                    alt2 = 1
                if alt2 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:33: settings
                    self._state.following.append(self.FOLLOW_settings_in_scenario49)
                    settings2 = self.settings()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:43: ( stage )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if LA3_0 == STAGE:
                    alt3 = 1
                if alt3 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:43: stage
                    self._state.following.append(self.FOLLOW_stage_in_scenario52)
                    stage3 = self.stage()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:50: ( writers )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == WRITERS:
                    alt4 = 1
                if alt4 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:9:50: writers
                    self._state.following.append(self.FOLLOW_writers_in_scenario55)
                    writers4 = self.writers()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 10:3: -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:1: declaration returns [scenario_name] : SCENARIO ID ( COLON name )? NEWLINE ;
    def declaration(
        self,
    ):
        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        ID5 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:37: ( SCENARIO ID ( COLON name )? NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:39: SCENARIO ID ( COLON name )? NEWLINE
                self.match(self.input, SCENARIO, self.FOLLOW_SCENARIO_in_declaration97)

                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_declaration99)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:51: ( COLON name )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if LA5_0 == COLON:
                    alt5 = 1
                if alt5 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:13:52: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration102)

                    self._state.following.append(self.FOLLOW_name_in_declaration104)
                    self.name()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_declaration108)

                # action start
                retval.scenario_name = ID5.text
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:14:1: settings : SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT -> settings(setting_list=$sets);
    def settings(
        self,
    ):
        retval = self.settings_return()
        retval.start = self.input.LT(1)

        list_sets = None
        sets = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:14:13: ( SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT -> settings(setting_list=$sets))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:14:15: SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT
                self.match(self.input, SETTINGS, self.FOLLOW_SETTINGS_in_settings120)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_settings122)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_settings124)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_settings126)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:14:49: (sets+= setting )+
                cnt6 = 0
                while True:  # loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if LA6_0 == ID:
                        alt6 = 1

                    if alt6 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:14:49: sets+= setting
                        self._state.following.append(self.FOLLOW_setting_in_settings130)
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

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_settings133)

                # TEMPLATE REWRITE
                # 14:67: -> settings(setting_list=$sets)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:15:1: stage : STAGE COLON NEWLINE INDENT stmts DEDENT ;
    def stage(
        self,
    ):
        retval = self.stage_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:15:13: ( STAGE COLON NEWLINE INDENT stmts DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:15:15: STAGE COLON NEWLINE INDENT stmts DEDENT
                self.match(self.input, STAGE, self.FOLLOW_STAGE_in_stage155)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_stage157)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stage159)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stage161)

                self._state.following.append(self.FOLLOW_stmts_in_stage163)
                self.stmts()

                self._state.following.pop()

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stage165)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:1: writers : WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT ;
    def writers(
        self,
    ):
        retval = self.writers_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:13: ( WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:15: WRITERS COLON NEWLINE INDENT ( expr_stmt | writer )+ DEDENT
                self.match(self.input, WRITERS, self.FOLLOW_WRITERS_in_writers176)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writers178)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writers180)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writers182)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:44: ( expr_stmt | writer )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:45: expr_stmt
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers185
                        )
                        self.expr_stmt()

                        self._state.following.pop()

                    elif alt7 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:16:57: writer
                        self._state.following.append(self.FOLLOW_writer_in_writers189)
                        self.writer()

                        self._state.following.pop()

                    else:
                        if cnt7 >= 1:
                            break  # loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writers193)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:18:1: setting : ID ASSIGN test NEWLINE -> setting(setting=$ID.textvalue=$test.st);
    def setting(
        self,
    ):
        retval = self.setting_return()
        retval.start = self.input.LT(1)

        ID6 = None
        test7 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:18:16: ( ID ASSIGN test NEWLINE -> setting(setting=$ID.textvalue=$test.st))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:18:18: ID ASSIGN test NEWLINE
                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_setting208)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_setting210)

                self._state.following.append(self.FOLLOW_test_in_setting212)
                test7 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_setting214)

                # TEMPLATE REWRITE
                # 18:41: -> setting(setting=$ID.textvalue=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "setting",
                    attributes={
                        "setting": ID6.text,
                        "value": ((test7 is not None) and [test7.st] or [None])[0],
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:1: stmts : ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+ ;
    def stmts(
        self,
    ):
        retval = self.stmts_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:16: ( ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+ )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:18: ( open_stmt )? ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:18: ( open_stmt )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if LA8_0 == OPEN:
                    alt8 = 1
                if alt8 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:18: open_stmt
                    self._state.following.append(self.FOLLOW_open_stmt_in_stmts245)
                    self.open_stmt()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:29: ( aug_expr_stmt | edit_stmt | behavior_stmt )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:30: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts249
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt9 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:46: edit_stmt
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts253)
                        self.edit_stmt()

                        self._state.following.pop()

                    elif alt9 == 3:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:19:58: behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_behavior_stmt_in_stmts257
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:20:1: writer : ID COLON NEWLINE INDENT ( writer_setting )+ DEDENT ;
    def writer(
        self,
    ):
        retval = self.writer_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:20:16: ( ID COLON NEWLINE INDENT ( writer_setting )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:20:18: ID COLON NEWLINE INDENT ( writer_setting )+ DEDENT
                self.match(self.input, ID, self.FOLLOW_ID_in_writer274)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writer276)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer278)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writer280)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:20:42: ( writer_setting )+
                cnt10 = 0
                while True:  # loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if LA10_0 == ID:
                        alt10 = 1

                    if alt10 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:20:42: writer_setting
                        self._state.following.append(
                            self.FOLLOW_writer_setting_in_writer282
                        )
                        self.writer_setting()

                        self._state.following.pop()

                    else:
                        if cnt10 >= 1:
                            break  # loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writer285)

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "writer"

    class writer_setting_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.st = None

        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None

        __str__ = toString

    # $ANTLR start "writer_setting"
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:21:1: writer_setting : ID ASSIGN test NEWLINE ;
    def writer_setting(
        self,
    ):
        retval = self.writer_setting_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:21:16: ( ID ASSIGN test NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:21:18: ID ASSIGN test NEWLINE
                self.match(self.input, ID, self.FOLLOW_ID_in_writer_setting292)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_writer_setting294)

                self._state.following.append(self.FOLLOW_test_in_writer_setting296)
                self.test()

                self._state.following.pop()

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer_setting298
                )

                retval.stop = self.input.LT(-1)

            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "writer_setting"

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:24:1: open_stmt : OPEN test NEWLINE ;
    def open_stmt(
        self,
    ):
        retval = self.open_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:24:11: ( OPEN test NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:24:13: OPEN test NEWLINE
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_open_stmt309)

                self._state.following.append(self.FOLLOW_test_in_open_stmt311)
                self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_open_stmt313)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:1: edit_stmt : EDIT ( TIMELINE | name ) edit_block ;
    def edit_stmt(
        self,
    ):
        retval = self.edit_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:11: ( EDIT ( TIMELINE | name ) edit_block )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:13: EDIT ( TIMELINE | name ) edit_block
                self.match(self.input, EDIT, self.FOLLOW_EDIT_in_edit_stmt320)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:18: ( TIMELINE | name )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:19: TIMELINE
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt323
                    )

                elif alt11 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:25:30: name
                    self._state.following.append(self.FOLLOW_name_in_edit_stmt327)
                    self.name()

                    self._state.following.pop()

                self._state.following.append(self.FOLLOW_edit_block_in_edit_stmt330)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:27:1: create_expr : CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) ;
    def create_expr(
        self,
    ):
        retval = self.create_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:27:12: ( CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:28:3: CREATE ( test )? ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr339)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:28:10: ( test )?
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:28:10: test
                    self._state.following.append(self.FOLLOW_test_in_create_expr341)
                    self.test()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:28:16: ( ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE ) | MATERIAL ( simple_block ) )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test ) ( edit_block | NEWLINE )
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:5: ( ( STEREO )? CAMERA | shapes | light_type LIGHT | FROM test )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:6: ( STEREO )? CAMERA
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:6: ( STEREO )?
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if LA13_0 == STEREO:
                            alt13 = 1
                        if alt13 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:6: STEREO
                            self.match(
                                self.input, STEREO, self.FOLLOW_STEREO_in_create_expr351
                            )

                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr354
                        )

                    elif alt14 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:23: shapes
                        self._state.following.append(
                            self.FOLLOW_shapes_in_create_expr358
                        )
                        self.shapes()

                        self._state.following.pop()

                    elif alt14 == 3:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:32: light_type LIGHT
                        self._state.following.append(
                            self.FOLLOW_light_type_in_create_expr362
                        )
                        self.light_type()

                        self._state.following.pop()

                        self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr364
                        )

                    elif alt14 == 4:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:51: FROM test
                        self.match(self.input, FROM, self.FOLLOW_FROM_in_create_expr368)

                        self._state.following.append(self.FOLLOW_test_in_create_expr370)
                        self.test()

                        self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:62: ( edit_block | NEWLINE )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:63: edit_block
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr374
                        )
                        self.edit_block()

                        self._state.following.pop()

                    elif alt15 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:29:76: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr378
                        )

                elif alt16 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:30:7: MATERIAL ( simple_block )
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr387
                    )

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:30:16: ( simple_block )
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:30:17: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_create_expr390
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:1: shapes : ( SHAPES | SHAPES_OR_LIGHTS );
    def shapes(
        self,
    ):
        retval = self.shapes_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:34:12: ( SHAPES | SHAPES_OR_LIGHTS )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:1: light_type : ( LIGHT_TYPE | SHAPES_OR_LIGHTS );
    def light_type(
        self,
    ):
        retval = self.light_type_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:35:12: ( LIGHT_TYPE | SHAPES_OR_LIGHTS )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:37:1: instantiate_expr : INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) ;
    def instantiate_expr(
        self,
    ):
        retval = self.instantiate_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:37:18: ( INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:37:20: INSTANTIATE ( test )? FROM test ( edit_block | NEWLINE )
                self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr431,
                )

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:37:32: ( test )?
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:37:33: test
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr434
                    )
                    self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr438)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr440)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:37:50: ( edit_block | NEWLINE )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:37:51: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr443
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt18 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:37:64: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instantiate_expr447
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:1: group_expr : GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) ;
    def group_expr(
        self,
    ):
        retval = self.group_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:18: ( GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:20: GROUP LBRACK name ( COMMA name )* RBRACK ( edit_block | NEWLINE )
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_expr461)

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr463)

                self._state.following.append(self.FOLLOW_name_in_group_expr465)
                self.name()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:38: ( COMMA name )*
                while True:  # loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if LA19_0 == COMMA:
                        alt19 = 1

                    if alt19 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:39: COMMA name
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_group_expr468
                        )

                        self._state.following.append(self.FOLLOW_name_in_group_expr470)
                        self.name()

                        self._state.following.pop()

                    else:
                        break  # loop19

                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_group_expr474)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:59: ( edit_block | NEWLINE )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:60: edit_block
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr477
                    )
                    self.edit_block()

                    self._state.following.pop()

                elif alt20 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:38:73: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_group_expr481
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:1: get_expr : GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) ;
    def get_expr(
        self,
    ):
        retval = self.get_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:18: ( GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:20: GET ( ( CAMERA | LIGHT | MATERIAL | name ) AT )? test ( simple_block | NEWLINE )
                self.match(self.input, GET, self.FOLLOW_GET_in_get_expr497)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:24: ( ( CAMERA | LIGHT | MATERIAL | name ) AT )?
                alt22 = 2
                LA22 = self.input.LA(1)
                if LA22 in {CAMERA, LIGHT, MATERIAL}:
                    alt22 = 1
                elif LA22 in {ID}:
                    LA22_2 = self.input.LA(2)

                    if LA22_2 == AT:
                        alt22 = 1
                elif LA22 in {UNDERSCORE}:
                    LA22_3 = self.input.LA(2)

                    if LA22_3 == AT:
                        alt22 = 1
                if alt22 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:25: ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:25: ( CAMERA | LIGHT | MATERIAL | name )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:26: CAMERA
                        self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr501
                        )

                    elif alt21 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:35: LIGHT
                        self.match(self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr505)

                    elif alt21 == 3:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:43: MATERIAL
                        self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr509
                        )

                    elif alt21 == 4:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:54: name
                        self._state.following.append(self.FOLLOW_name_in_get_expr513)
                        self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr516)

                self._state.following.append(self.FOLLOW_test_in_get_expr520)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:70: ( simple_block | NEWLINE )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:71: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr523
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt23 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:39:86: NEWLINE
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr527)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:1: edit_block : COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT ;
    def edit_block(
        self,
    ):
        retval = self.edit_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:14: ( COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:16: COLON NEWLINE INDENT ( attr | inner_behavior_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block538)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block540)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block542)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:37: ( attr | inner_behavior_stmt )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:38: attr
                        self._state.following.append(self.FOLLOW_attr_in_edit_block545)
                        self.attr()

                        self._state.following.pop()

                    elif alt24 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:41:45: inner_behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_inner_behavior_stmt_in_edit_block549
                        )
                        self.inner_behavior_stmt()

                        self._state.following.pop()

                    else:
                        if cnt24 >= 1:
                            break  # loop24

                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_block553)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:1: simple_block : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        retval = self.simple_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:14: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:16: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block560)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block562)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block564)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:37: ( simple_attr )+
                cnt25 = 0
                while True:  # loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if LA25_0 in {ID, UNDERSCORE}:
                        alt25 = 1

                    if alt25 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:42:37: simple_attr
                        self._state.following.append(
                            self.FOLLOW_simple_attr_in_simple_block566
                        )
                        self.simple_attr()

                        self._state.following.pop()

                    else:
                        if cnt25 >= 1:
                            break  # loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_simple_block569)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:1: attr : ( core_attr | simple_attr | compound_attr );
    def attr(
        self,
    ):
        retval = self.attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:15: ( core_attr | simple_attr | compound_attr )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:17: core_attr
                    self._state.following.append(self.FOLLOW_core_attr_in_attr586)
                    self.core_attr()

                    self._state.following.pop()

                elif alt26 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:29: simple_attr
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr590)
                    self.simple_attr()

                    self._state.following.pop()

                elif alt26 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:44:43: compound_attr
                    self._state.following.append(self.FOLLOW_compound_attr_in_attr594)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:45:1: simple_attr : name ( COLON name )? ( test )? NEWLINE ;
    def simple_attr(
        self,
    ):
        retval = self.simple_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:45:15: ( name ( COLON name )? ( test )? NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:45:17: name ( COLON name )? ( test )? NEWLINE
                self._state.following.append(self.FOLLOW_name_in_simple_attr603)
                self.name()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:45:22: ( COLON name )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if LA27_0 == COLON:
                    alt27 = 1
                if alt27 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:45:23: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr606)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr608)
                    self.name()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:45:36: ( test )?
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:45:36: test
                    self._state.following.append(self.FOLLOW_test_in_simple_attr612)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_attr615)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:1: compound_attr : ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) ;
    def compound_attr(
        self,
    ):
        retval = self.compound_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:15: ( ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS ) ( simple_block | NEWLINE )
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:17: ( SCATTER ON name | ROT_AROUND name | PHYSICS )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:18: SCATTER ON name
                    self.match(
                        self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr624
                    )

                    self.match(self.input, ON, self.FOLLOW_ON_in_compound_attr626)

                    self._state.following.append(self.FOLLOW_name_in_compound_attr628)
                    self.name()

                    self._state.following.pop()

                elif alt29 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:36: ROT_AROUND name
                    self.match(
                        self.input,
                        ROT_AROUND,
                        self.FOLLOW_ROT_AROUND_in_compound_attr632,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr634)
                    self.name()

                    self._state.following.pop()

                elif alt29 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:54: PHYSICS
                    self.match(
                        self.input, PHYSICS, self.FOLLOW_PHYSICS_in_compound_attr638
                    )

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:63: ( simple_block | NEWLINE )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:64: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_compound_attr642
                    )
                    self.simple_block()

                    self._state.following.pop()

                elif alt30 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:47:79: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_compound_attr646
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:49:1: core_attr : ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE ;
    def core_attr(
        self,
    ):
        retval = self.core_attr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:49:10: ( ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:50:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test ) NEWLINE
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:50:3: ( TRANSLATE ( AXIS )? TO test | CAM_TRANSLATE TO test | ROTATE ( AXIS )? test ( ORDER )? | SCALE test | LOOK_AT test | UP_AXIS test | SIZE test | SEMANTICS test | VISIBLE test )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:51:5: TRANSLATE ( AXIS )? TO test
                    self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr663
                    )

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:51:15: ( AXIS )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if LA31_0 == AXIS:
                        alt31 = 1
                    if alt31 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:51:15: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr665)

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr668)

                    self._state.following.append(self.FOLLOW_test_in_core_attr670)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:52:7: CAM_TRANSLATE TO test
                    self.match(
                        self.input,
                        CAM_TRANSLATE,
                        self.FOLLOW_CAM_TRANSLATE_in_core_attr678,
                    )

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr680)

                    self._state.following.append(self.FOLLOW_test_in_core_attr682)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:53:7: ROTATE ( AXIS )? test ( ORDER )?
                    self.match(self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr690)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:53:14: ( AXIS )?
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if LA32_0 == AXIS:
                        alt32 = 1
                    if alt32 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:53:14: AXIS
                        self.match(self.input, AXIS, self.FOLLOW_AXIS_in_core_attr692)

                    self._state.following.append(self.FOLLOW_test_in_core_attr695)
                    self.test()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:53:25: ( ORDER )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if LA33_0 == ORDER:
                        alt33 = 1
                    if alt33 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:53:25: ORDER
                        self.match(self.input, ORDER, self.FOLLOW_ORDER_in_core_attr697)

                elif alt34 == 4:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:54:7: SCALE test
                    self.match(self.input, SCALE, self.FOLLOW_SCALE_in_core_attr706)

                    self._state.following.append(self.FOLLOW_test_in_core_attr708)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 5:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:55:7: LOOK_AT test
                    self.match(self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr716)

                    self._state.following.append(self.FOLLOW_test_in_core_attr718)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 6:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:56:7: UP_AXIS test
                    self.match(self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr726)

                    self._state.following.append(self.FOLLOW_test_in_core_attr728)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 7:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:57:7: SIZE test
                    self.match(self.input, SIZE, self.FOLLOW_SIZE_in_core_attr736)

                    self._state.following.append(self.FOLLOW_test_in_core_attr738)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 8:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:58:7: SEMANTICS test
                    self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr746
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr748)
                    self.test()

                    self._state.following.pop()

                elif alt34 == 9:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:59:7: VISIBLE test
                    self.match(self.input, VISIBLE, self.FOLLOW_VISIBLE_in_core_attr756)

                    self._state.following.append(self.FOLLOW_test_in_core_attr758)
                    self.test()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_core_attr764)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:63:1: inner_behavior_stmt : behavior_expr inner_behavior_block ;
    def inner_behavior_stmt(
        self,
    ):
        retval = self.inner_behavior_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:63:22: ( behavior_expr inner_behavior_block )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:63:24: behavior_expr inner_behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_inner_behavior_stmt774
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_inner_behavior_block_in_inner_behavior_stmt776
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:64:1: inner_behavior_block : COLON NEWLINE INDENT ( attr )+ DEDENT ;
    def inner_behavior_block(
        self,
    ):
        retval = self.inner_behavior_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:64:22: ( COLON NEWLINE INDENT ( attr )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:64:24: COLON NEWLINE INDENT ( attr )+ DEDENT
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block783
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block785
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block787
                )

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:64:45: ( attr )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:64:45: attr
                        self._state.following.append(
                            self.FOLLOW_attr_in_inner_behavior_block789
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
                    self.input, DEDENT, self.FOLLOW_DEDENT_in_inner_behavior_block792
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:67:1: behavior_stmt : behavior_expr behavior_block ;
    def behavior_stmt(
        self,
    ):
        retval = self.behavior_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:67:16: ( behavior_expr behavior_block )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:67:18: behavior_expr behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_behavior_stmt803
                )
                self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_behavior_block_in_behavior_stmt805
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:68:1: behavior_expr : EVERY ( test )? ( FRAMES | TIME ) ;
    def behavior_expr(
        self,
    ):
        retval = self.behavior_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:68:16: ( EVERY ( test )? ( FRAMES | TIME ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:68:18: EVERY ( test )? ( FRAMES | TIME )
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr813)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:68:24: ( test )?
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:68:24: test
                    self._state.following.append(self.FOLLOW_test_in_behavior_expr815)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:1: behavior_block : COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT ;
    def behavior_block(
        self,
    ):
        retval = self.behavior_block_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:16: ( COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:18: COLON NEWLINE INDENT ( aug_expr_stmt | edit_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block831)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block833
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block835)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:39: ( aug_expr_stmt | edit_stmt )+
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:40: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block838
                        )
                        self.aug_expr_stmt()

                        self._state.following.pop()

                    elif alt37 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:69:56: edit_stmt
                        self._state.following.append(
                            self.FOLLOW_edit_stmt_in_behavior_block842
                        )
                        self.edit_stmt()

                        self._state.following.pop()

                    else:
                        if cnt37 >= 1:
                            break  # loop37

                        eee = EarlyExitException(37, self.input)
                        raise eee

                    cnt37 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_behavior_block846)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:72:1: expr_stmt : testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE ;
    def expr_stmt(
        self,
    ):
        retval = self.expr_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:72:11: ( testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:72:13: testlist ( AUG_ASSIGN | ASSIGN ) ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt856)
                self.testlist()

                self._state.following.pop()

                if self.input.LA(1) in {ASSIGN, AUG_ASSIGN}:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:72:44: ( testlist | fetch_expr )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:72:45: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt867)
                    self.testlist()

                    self._state.following.pop()

                elif alt38 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:72:56: fetch_expr
                    self._state.following.append(self.FOLLOW_fetch_expr_in_expr_stmt871)
                    self.fetch_expr()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expr_stmt874)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:74:1: aug_expr_stmt : ( ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr );
    def aug_expr_stmt(
        self,
    ):
        retval = self.aug_expr_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:74:14: ( ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) ) | create_expr | instantiate_expr | get_expr | group_expr )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:74:16: ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:74:16: ( testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) ) )
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:75:5: testlist ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt887
                    )
                    self.testlist()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:75:14: ( AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE | ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr ) )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:76:7: AUG_ASSIGN ( testlist | fetch_expr )? NEWLINE
                        self.match(
                            self.input,
                            AUG_ASSIGN,
                            self.FOLLOW_AUG_ASSIGN_in_aug_expr_stmt897,
                        )

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:76:18: ( testlist | fetch_expr )?
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
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:76:19: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt900
                            )
                            self.testlist()

                            self._state.following.pop()

                        elif alt39 == 2:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:76:30: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt904
                            )
                            self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_aug_expr_stmt908
                        )

                    elif alt42 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:77:9: ASSIGN ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
                        self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt918
                        )

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:77:16: ( ( testlist | fetch_expr ) NEWLINE | create_expr | instantiate_expr | get_expr | group_expr )
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
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:78:9: ( testlist | fetch_expr ) NEWLINE
                            pass
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:78:9: ( testlist | fetch_expr )
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
                                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:78:10: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt931
                                )
                                self.testlist()

                                self._state.following.pop()

                            elif alt40 == 2:
                                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:78:21: fetch_expr
                                self._state.following.append(
                                    self.FOLLOW_fetch_expr_in_aug_expr_stmt935
                                )
                                self.fetch_expr()

                                self._state.following.pop()

                            self.match(
                                self.input,
                                NEWLINE,
                                self.FOLLOW_NEWLINE_in_aug_expr_stmt938,
                            )

                        elif alt41 == 2:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:79:11: create_expr
                            self._state.following.append(
                                self.FOLLOW_create_expr_in_aug_expr_stmt950
                            )
                            self.create_expr()

                            self._state.following.pop()

                        elif alt41 == 3:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:79:25: instantiate_expr
                            self._state.following.append(
                                self.FOLLOW_instantiate_expr_in_aug_expr_stmt954
                            )
                            self.instantiate_expr()

                            self._state.following.pop()

                        elif alt41 == 4:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:79:44: get_expr
                            self._state.following.append(
                                self.FOLLOW_get_expr_in_aug_expr_stmt958
                            )
                            self.get_expr()

                            self._state.following.pop()

                        elif alt41 == 5:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:79:55: group_expr
                            self._state.following.append(
                                self.FOLLOW_group_expr_in_aug_expr_stmt962
                            )
                            self.group_expr()

                            self._state.following.pop()

                elif alt43 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:5: create_expr
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_aug_expr_stmt986
                    )
                    self.create_expr()

                    self._state.following.pop()

                elif alt43 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:19: instantiate_expr
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_aug_expr_stmt990
                    )
                    self.instantiate_expr()

                    self._state.following.pop()

                elif alt43 == 4:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:38: get_expr
                    self._state.following.append(
                        self.FOLLOW_get_expr_in_aug_expr_stmt994
                    )
                    self.get_expr()

                    self._state.following.pop()

                elif alt43 == 5:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:83:49: group_expr
                    self._state.following.append(
                        self.FOLLOW_group_expr_in_aug_expr_stmt998
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:1: fetch_expr : FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )? ;
    def fetch_expr(
        self,
    ):
        retval = self.fetch_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:12: ( FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:14: FETCH test FROM test ( MATCH test )? ( LIMIT test )? ( RECURSIVE )?
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr1007)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr1009)
                self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr1011)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr1013)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:35: ( MATCH test )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if LA44_0 == MATCH:
                    alt44 = 1
                if alt44 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:36: MATCH test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr1016)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr1018)
                    self.test()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:49: ( LIMIT test )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 == LIMIT:
                    alt45 = 1
                if alt45 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:50: LIMIT test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr1023)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr1025)
                    self.test()

                    self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:63: ( RECURSIVE )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 == RECURSIVE:
                    alt46 = 1
                if alt46 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:86:63: RECURSIVE
                    self.match(
                        self.input, RECURSIVE, self.FOLLOW_RECURSIVE_in_fetch_expr1029
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:1: test : expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st);
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
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:13: (expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:15: expr_= or_test ( IF cond= or_test ELSE else_expr= test )?
                self._state.following.append(self.FOLLOW_or_test_in_test1049)
                expr_ = self.or_test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:29: ( IF cond= or_test ELSE else_expr= test )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if LA47_0 == IF:
                    alt47 = 1
                if alt47 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:89:30: IF cond= or_test ELSE else_expr= test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test1052)

                    self._state.following.append(self.FOLLOW_or_test_in_test1056)
                    cond = self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test1058)

                    self._state.following.append(self.FOLLOW_test_in_test1062)
                    else_expr = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 90:13: -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:91:1: test_nocond : or_test -> test(expr=$or_test.st);
    def test_nocond(
        self,
    ):
        retval = self.test_nocond_return()
        retval.start = self.input.LT(1)

        or_test8 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:91:13: ( or_test -> test(expr=$or_test.st))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:91:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond1104)
                or_test8 = self.or_test()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 91:23: -> test(expr=$or_test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "test",
                    attributes={
                        "expr": ((or_test8 is not None) and [or_test8.st] or [None])[0]
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:1: or_test :exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs);
    def or_test(
        self,
    ):
        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:13: (exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:15: exprs+= and_test ( OR exprs+= and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test1126)
                exprs = self.and_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:31: ( OR exprs+= and_test )*
                while True:  # loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if LA48_0 == OR:
                        alt48 = 1

                    if alt48 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:92:32: OR exprs+= and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test1129)

                        self._state.following.append(
                            self.FOLLOW_and_test_in_or_test1133
                        )
                        exprs = self.and_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop48

                # TEMPLATE REWRITE
                # 92:53: -> or_test(exprs=$exprs)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:1: and_test :exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs);
    def and_test(
        self,
    ):
        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:13: (exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:15: exprs+= not_test ( AND exprs+= not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test1156)
                exprs = self.not_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:31: ( AND exprs+= not_test )*
                while True:  # loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if LA49_0 == AND:
                        alt49 = 1

                    if alt49 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:93:32: AND exprs+= not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test1159)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test1163
                        )
                        exprs = self.not_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop49

                # TEMPLATE REWRITE
                # 93:54: -> and_test(exprs=$exprs)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:94:1: not_test : ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st});
    def not_test(
        self,
    ):
        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        expr_ = None
        comparison9 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:94:13: ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st})
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:94:15: NOT expr_= not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test1184)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test1188)
                    expr_ = self.not_test()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 94:35: -> not_test(expr=$expr_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "not_test",
                        attributes={
                            "expr": ((expr_ is not None) and [expr_.st] or [None])[0]
                        },
                    )

                elif alt50 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:95:15: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test1214)
                    comparison9 = self.comparison()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 95:26: -> {$comparison.st}
                    retval.st = (
                        (comparison9 is not None) and [comparison9.st] or [None]
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:1: comparison :exprs+= expr ( comp_op exprs+= expr )* -> comparison(exprs=$exprsop=$comp_op.text);
    def comparison(
        self,
    ):
        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        comp_op10 = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:13: (exprs+= expr ( comp_op exprs+= expr )* -> comparison(exprs=$exprsop=$comp_op.text))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:15: exprs+= expr ( comp_op exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison1228)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:27: ( comp_op exprs+= expr )*
                while True:  # loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if LA51_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt51 = 1

                    if alt51 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:96:28: comp_op exprs+= expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison1231
                        )
                        comp_op10 = self.comp_op()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_expr_in_comparison1235)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop51

                # TEMPLATE REWRITE
                # 96:50: -> comparison(exprs=$exprsop=$comp_op.text)
                retval.st = self.templateLib.getInstanceOf(
                    "comparison",
                    attributes={
                        "exprs": list_exprs,
                        "op": (
                            (comp_op10 is not None)
                            and [self.input.toString(comp_op10.start, comp_op10.stop)]
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:1: comp_op : ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT );
    def comp_op(
        self,
    ):
        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:13: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
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
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:15: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_comp_op1262)

                elif alt52 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:20: GT
                    self.match(self.input, GT, self.FOLLOW_GT_in_comp_op1266)

                elif alt52 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:25: EQUALS
                    self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op1270)

                elif alt52 == 4:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:34: GT_EQ
                    self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op1274)

                elif alt52 == 5:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:42: LT_EQ
                    self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op1278)

                elif alt52 == 6:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:50: NOT_EQ
                    self.match(self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op1282)

                elif alt52 == 7:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:59: IN
                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1286)

                elif alt52 == 8:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:64: NOT IN
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1290)

                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op1292)

                elif alt52 == 9:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:73: IS
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1296)

                elif alt52 == 10:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:97:78: IS NOT
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op1300)

                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op1302)

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:1: expr :exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs);
    def expr(
        self,
    ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:13: (exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:15: exprs+= xor_expr ( BIT_OR exprs+= xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr1319)
                exprs = self.xor_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:31: ( BIT_OR exprs+= xor_expr )*
                while True:  # loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if LA53_0 == BIT_OR:
                        alt53 = 1

                    if alt53 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:98:32: BIT_OR exprs+= xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr1322)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr1326)
                        exprs = self.xor_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop53

                # TEMPLATE REWRITE
                # 98:57: -> expr(exprs=$exprs)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:1: xor_expr :exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs);
    def xor_expr(
        self,
    ):
        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:13: (exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:15: exprs+= and_expr ( XOR exprs+= and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr1349)
                exprs = self.and_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:31: ( XOR exprs+= and_expr )*
                while True:  # loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if LA54_0 == XOR:
                        alt54 = 1

                    if alt54 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:99:32: XOR exprs+= and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr1352)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr1356
                        )
                        exprs = self.and_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop54

                # TEMPLATE REWRITE
                # 99:54: -> xor_expr(exprs=$exprs)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:1: and_expr :exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs);
    def and_expr(
        self,
    ):
        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:13: (exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:15: exprs+= shift_expr ( BIT_AND exprs+= shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr1379)
                exprs = self.shift_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:33: ( BIT_AND exprs+= shift_expr )*
                while True:  # loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if LA55_0 == BIT_AND:
                        alt55 = 1

                    if alt55 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:100:34: BIT_AND exprs+= shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr1382
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr1386
                        )
                        exprs = self.shift_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop55

                # TEMPLATE REWRITE
                # 100:62: -> and_expr(exprs=$exprs)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:1: shift_expr :exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsop=$op);
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
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:13: (exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsop=$op))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:15: exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr1407)
                exprs = self.arith_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:33: (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                while True:  # loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if LA57_0 in {LSHIFT, RSHIFT}:
                        alt57 = 1

                    if alt57 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:34: op= ( LSHIFT | RSHIFT ) exprs+= arith_expr
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:37: ( LSHIFT | RSHIFT )
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if LA56_0 == LSHIFT:
                            alt56 = 1
                        elif LA56_0 == RSHIFT:
                            alt56 = 2
                        else:
                            nvae = NoViableAltException("", 56, 0, self.input)

                            raise nvae

                        if alt56 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:38: LSHIFT
                            op = self.match(
                                self.input, LSHIFT, self.FOLLOW_LSHIFT_in_shift_expr1413
                            )

                        elif alt56 == 2:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:101:47: RSHIFT
                            op = self.match(
                                self.input, RSHIFT, self.FOLLOW_RSHIFT_in_shift_expr1417
                            )

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr1422
                        )
                        exprs = self.arith_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop57

                # TEMPLATE REWRITE
                # 101:75: -> shift_expr(exprs=$exprsop=$op)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:1: arith_expr :terms+= term (op= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsop=$op);
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
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:13: (terms+= term (op= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsop=$op))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:15: terms+= term (op= ( PLUS | MINUS ) terms+= term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr1448)
                terms = self.term()

                self._state.following.pop()
                if list_terms is None:
                    list_terms = []
                list_terms.append(terms.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:27: (op= ( PLUS | MINUS ) terms+= term )*
                while True:  # loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if LA59_0 in {MINUS, PLUS}:
                        alt59 = 1

                    if alt59 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:28: op= ( PLUS | MINUS ) terms+= term
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:31: ( PLUS | MINUS )
                        alt58 = 2
                        LA58_0 = self.input.LA(1)

                        if LA58_0 == PLUS:
                            alt58 = 1
                        elif LA58_0 == MINUS:
                            alt58 = 2
                        else:
                            nvae = NoViableAltException("", 58, 0, self.input)

                            raise nvae

                        if alt58 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:32: PLUS
                            op = self.match(
                                self.input, PLUS, self.FOLLOW_PLUS_in_arith_expr1454
                            )

                        elif alt58 == 2:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:102:39: MINUS
                            op = self.match(
                                self.input, MINUS, self.FOLLOW_MINUS_in_arith_expr1458
                            )

                        self._state.following.append(self.FOLLOW_term_in_arith_expr1463)
                        terms = self.term()

                        self._state.following.pop()
                        if list_terms is None:
                            list_terms = []
                        list_terms.append(terms.st)

                    else:
                        break  # loop59

                # TEMPLATE REWRITE
                # 102:60: -> arith_expr(terms=$termsop=$op)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:1: term :factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsop=$op);
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
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:13: (factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsop=$op))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:15: factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                self._state.following.append(self.FOLLOW_factor_in_term1495)
                factors = self.factor()

                self._state.following.pop()
                if list_factors is None:
                    list_factors = []
                list_factors.append(factors.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:31: (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                while True:  # loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if LA61_0 in {DIV, IDIV, MOD, MUL}:
                        alt61 = 1

                    if alt61 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:32: op= ( MUL | DIV | MOD | IDIV ) factors+= factor
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:35: ( MUL | DIV | MOD | IDIV )
                        alt60 = 4
                        LA60 = self.input.LA(1)
                        if LA60 in {MUL}:
                            alt60 = 1
                        elif LA60 in {DIV}:
                            alt60 = 2
                        elif LA60 in {MOD}:
                            alt60 = 3
                        elif LA60 in {IDIV}:
                            alt60 = 4
                        else:
                            nvae = NoViableAltException("", 60, 0, self.input)

                            raise nvae

                        if alt60 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:36: MUL
                            op = self.match(
                                self.input, MUL, self.FOLLOW_MUL_in_term1501
                            )

                        elif alt60 == 2:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:42: DIV
                            op = self.match(
                                self.input, DIV, self.FOLLOW_DIV_in_term1505
                            )

                        elif alt60 == 3:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:48: MOD
                            op = self.match(
                                self.input, MOD, self.FOLLOW_MOD_in_term1509
                            )

                        elif alt60 == 4:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:103:54: IDIV
                            op = self.match(
                                self.input, IDIV, self.FOLLOW_IDIV_in_term1513
                            )

                        self._state.following.append(self.FOLLOW_factor_in_term1518)
                        factors = self.factor()

                        self._state.following.pop()
                        if list_factors is None:
                            list_factors = []
                        list_factors.append(factors.st)

                    else:
                        break  # loop61

                # TEMPLATE REWRITE
                # 103:78: -> term(factors=$factorsop=$op)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:1: factor : (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st});
    def factor(
        self,
    ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)

        prefix = None
        factor_ = None
        power11 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:13: (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st})
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if LA63_0 in {BIT_NOT, MINUS, PLUS}:
                    alt63 = 1
                elif LA63_0 in {
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
                    alt63 = 2
                else:
                    nvae = NoViableAltException("", 63, 0, self.input)

                    raise nvae

                if alt63 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:15: prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:22: ( PLUS | MINUS | BIT_NOT )
                    alt62 = 3
                    LA62 = self.input.LA(1)
                    if LA62 in {PLUS}:
                        alt62 = 1
                    elif LA62 in {MINUS}:
                        alt62 = 2
                    elif LA62 in {BIT_NOT}:
                        alt62 = 3
                    else:
                        nvae = NoViableAltException("", 62, 0, self.input)

                        raise nvae

                    if alt62 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:23: PLUS
                        prefix = self.match(
                            self.input, PLUS, self.FOLLOW_PLUS_in_factor1549
                        )

                    elif alt62 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:30: MINUS
                        prefix = self.match(
                            self.input, MINUS, self.FOLLOW_MINUS_in_factor1553
                        )

                    elif alt62 == 3:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:104:38: BIT_NOT
                        prefix = self.match(
                            self.input, BIT_NOT, self.FOLLOW_BIT_NOT_in_factor1557
                        )

                    self._state.following.append(self.FOLLOW_factor_in_factor1562)
                    factor_ = self.factor()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 104:62: -> prefix_factor(factor=$factor_.stprefix=$prefix)
                    retval.st = self.templateLib.getInstanceOf(
                        "prefix_factor",
                        attributes={
                            "factor": (
                                (factor_ is not None) and [factor_.st] or [None]
                            )[0],
                            "prefix": prefix,
                        },
                    )

                elif alt63 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:105:15: power
                    self._state.following.append(self.FOLLOW_power_in_factor1592)
                    power11 = self.power()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 105:21: -> {$power.st}
                    retval.st = ((power11 is not None) and [power11.st] or [None])[0]

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:106:1: power : atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st);
    def power(
        self,
    ):
        retval = self.power_return()
        retval.start = self.input.LT(1)

        atom_expr12 = None
        factor13 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:106:13: ( atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:106:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power1609)
                atom_expr12 = self.atom_expr()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:106:25: ( POWER factor )?
                alt64 = 2
                LA64_0 = self.input.LA(1)

                if LA64_0 == POWER:
                    alt64 = 1
                if alt64 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:106:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power1612)

                    self._state.following.append(self.FOLLOW_factor_in_power1614)
                    factor13 = self.factor()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 106:41: -> power(atom=$atom_expr.stfactor=$factor.st)
                retval.st = self.templateLib.getInstanceOf(
                    "power",
                    attributes={
                        "atom": (
                            (atom_expr12 is not None) and [atom_expr12.st] or [None]
                        )[0],
                        "factor": ((factor13 is not None) and [factor13.st] or [None])[
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:107:1: atom_expr : atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers);
    def atom_expr(
        self,
    ):
        retval = self.atom_expr_return()
        retval.start = self.input.LT(1)

        list_trailers = None
        atom14 = None
        trailers = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:107:13: ( atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:107:15: atom (trailers+= trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr1639)
                atom14 = self.atom()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:107:20: (trailers+= trailer )*
                while True:  # loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if LA65_0 in {DOT, LBRACK}:
                        alt65 = 1

                    if alt65 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:107:21: trailers+= trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr1644
                        )
                        trailers = self.trailer()

                        self._state.following.pop()
                        if list_trailers is None:
                            list_trailers = []
                        list_trailers.append(trailers.st)

                    else:
                        break  # loop65

                # TEMPLATE REWRITE
                # 107:41: -> atom_expr(atom=$atom.sttrailers=$trailers)
                retval.st = self.templateLib.getInstanceOf(
                    "atom_expr",
                    attributes={
                        "atom": ((atom14 is not None) and [atom14.st] or [None])[0],
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:108:1: atom : ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false() ;
    def atom(
        self,
    ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)

        SETTING_ID19 = None
        DISTRIBUTION20 = None
        INTEGER22 = None
        FLOAT_NUMBER23 = None
        STRING24 = None
        test_ = None
        testlist_comp15 = None
        vector_comp16 = None
        dict_or_set_maker17 = None
        name18 = None
        arglist21 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:108:5: ( ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false() )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:109:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false()
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:109:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false()
                alt69 = 14
                LA69 = self.input.LA(1)
                if LA69 in {LPAREN}:
                    alt69 = 1
                elif LA69 in {LBRACK}:
                    alt69 = 2
                elif LA69 in {LT}:
                    alt69 = 3
                elif LA69 in {LBRACE}:
                    alt69 = 4
                elif LA69 in {LEN}:
                    alt69 = 5
                elif LA69 in {ID, UNDERSCORE}:
                    alt69 = 6
                elif LA69 in {SETTING_ID}:
                    alt69 = 7
                elif LA69 in {DISTRIBUTION}:
                    alt69 = 8
                elif LA69 in {INTEGER}:
                    alt69 = 9
                elif LA69 in {FLOAT_NUMBER}:
                    alt69 = 10
                elif LA69 in {STRING}:
                    alt69 = 11
                elif LA69 in {NONE}:
                    alt69 = 12
                elif LA69 in {TRUE}:
                    alt69 = 13
                elif LA69 in {FALSE}:
                    alt69 = 14
                else:
                    nvae = NoViableAltException("", 69, 0, self.input)

                    raise nvae

                if alt69 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:109:4: LPAREN test_= test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1669)

                    self._state.following.append(self.FOLLOW_test_in_atom1673)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1675)

                    # TEMPLATE REWRITE
                    # 109:29: -> parenthesized_expr(expr=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "parenthesized_expr",
                        attributes={
                            "expr": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt69 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:110:5: LBRACK ( testlist_comp )? RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom1690)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:110:12: ( testlist_comp )?
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
                        NOT,
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt66 = 1
                    if alt66 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:110:12: testlist_comp
                        self._state.following.append(
                            self.FOLLOW_testlist_comp_in_atom1692
                        )
                        testlist_comp15 = self.testlist_comp()

                        self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom1695)

                    # TEMPLATE REWRITE
                    # 110:34: -> list(list_comp=$testlist_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list",
                        attributes={
                            "list_comp": (
                                (testlist_comp15 is not None)
                                and [testlist_comp15.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt69 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:111:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom1710)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:111:8: ( vector_comp )?
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
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt67 = 1
                    if alt67 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:111:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom1712
                        )
                        vector_comp16 = self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom1715)

                    # TEMPLATE REWRITE
                    # 111:24: -> vector(values=$vector_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "vector",
                        attributes={
                            "values": (
                                (vector_comp16 is not None)
                                and [vector_comp16.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt69 == 4:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:112:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom1730)

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:112:12: ( dict_or_set_maker )?
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:112:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom1732
                        )
                        dict_or_set_maker17 = self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom1735)

                    # TEMPLATE REWRITE
                    # 112:38: -> dict(dict_comp=$dict_or_set_maker.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dict",
                        attributes={
                            "dict_comp": (
                                (dict_or_set_maker17 is not None)
                                and [dict_or_set_maker17.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt69 == 5:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:113:5: LEN LPAREN test_= test RPAREN
                    self.match(self.input, LEN, self.FOLLOW_LEN_in_atom1750)

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1752)

                    self._state.following.append(self.FOLLOW_test_in_atom1756)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1758)

                    # TEMPLATE REWRITE
                    # 113:34: -> len(value=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "len",
                        attributes={
                            "value": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt69 == 6:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:114:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom1773)
                    name18 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 114:10: -> {$name.st}
                    retval.st = ((name18 is not None) and [name18.st] or [None])[0]

                elif alt69 == 7:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:115:5: SETTING_ID
                    SETTING_ID19 = self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom1783
                    )

                    # TEMPLATE REWRITE
                    # 115:16: -> setting_id(id=$SETTING_ID.text)
                    retval.st = self.templateLib.getInstanceOf(
                        "setting_id", attributes={"id": SETTING_ID19.text}
                    )

                elif alt69 == 8:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:116:5: DISTRIBUTION LPAREN arglist RPAREN
                    DISTRIBUTION20 = self.match(
                        self.input, DISTRIBUTION, self.FOLLOW_DISTRIBUTION_in_atom1799
                    )

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom1801)

                    self._state.following.append(self.FOLLOW_arglist_in_atom1803)
                    arglist21 = self.arglist()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom1805)

                    # TEMPLATE REWRITE
                    # 116:40: -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "distribution",
                        attributes={
                            "name": DISTRIBUTION20.text,
                            "arglist": (
                                (arglist21 is not None) and [arglist21.st] or [None]
                            )[0],
                        },
                    )

                elif alt69 == 9:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:117:5: INTEGER
                    INTEGER22 = self.match(
                        self.input, INTEGER, self.FOLLOW_INTEGER_in_atom1825
                    )

                    # TEMPLATE REWRITE
                    # 117:13: -> {$INTEGER.text}
                    retval.st = INTEGER22.text

                elif alt69 == 10:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:118:5: FLOAT_NUMBER
                    FLOAT_NUMBER23 = self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom1835
                    )

                    # TEMPLATE REWRITE
                    # 118:18: -> {$FLOAT_NUMBER.text}
                    retval.st = FLOAT_NUMBER23.text

                elif alt69 == 11:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:119:5: STRING
                    STRING24 = self.match(
                        self.input, STRING, self.FOLLOW_STRING_in_atom1845
                    )

                    # TEMPLATE REWRITE
                    # 119:12: -> {$STRING.text}
                    retval.st = STRING24.text

                elif alt69 == 12:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:120:5: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom1855)

                    # TEMPLATE REWRITE
                    # 120:10: -> null(
                    retval.st = self.templateLib.getInstanceOf("null")

                elif alt69 == 13:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:121:5: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom1867)

                    # TEMPLATE REWRITE
                    # 121:10: -> true(
                    retval.st = self.templateLib.getInstanceOf("true")

                elif alt69 == 14:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:122:5: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom1879)

                    # TEMPLATE REWRITE
                    # 122:11: -> false(
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:126:1: name : ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text});
    def name(
        self,
    ):
        retval = self.name_return()
        retval.start = self.input.LT(1)

        ID25 = None
        UNDERSCORE26 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:126:5: ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text})
                alt70 = 2
                LA70_0 = self.input.LA(1)

                if LA70_0 == ID:
                    alt70 = 1
                elif LA70_0 == UNDERSCORE:
                    alt70 = 2
                else:
                    nvae = NoViableAltException("", 70, 0, self.input)

                    raise nvae

                if alt70 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:127:3: ID
                    ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_name1899)

                    # TEMPLATE REWRITE
                    # 127:6: -> {$ID.text}
                    retval.st = ID25.text

                elif alt70 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:128:5: UNDERSCORE
                    UNDERSCORE26 = self.match(
                        self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_name1909
                    )

                    # TEMPLATE REWRITE
                    # 128:16: -> {$UNDERSCORE.text}
                    retval.st = UNDERSCORE26.text

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:139:1: testlist_comp :exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) ;
    def testlist_comp(
        self,
    ):
        retval = self.testlist_comp_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        to = None
        step = None
        comp_for27 = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:139:15: (exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:139:17: exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                self._state.following.append(self.FOLLOW_test_in_testlist_comp1928)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:139:29: ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                alt73 = 3
                LA73 = self.input.LA(1)
                if LA73 in {FOR}:
                    alt73 = 1
                elif LA73 in {COMMA, RBRACK}:
                    alt73 = 2
                elif LA73 in {RANGE}:
                    alt73 = 3
                else:
                    nvae = NoViableAltException("", 73, 0, self.input)

                    raise nvae

                if alt73 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:139:31: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp1932
                    )
                    comp_for27 = self.comp_for()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 139:40: -> list_comp(expr=$exprs[0]for=$comp_for.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list_comp",
                        attributes={
                            "expr": list_exprs[0],
                            "for": (
                                (comp_for27 is not None) and [comp_for27.st] or [None]
                            )[0],
                        },
                    )

                elif alt73 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:24: ( COMMA exprs+= test )*
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:24: ( COMMA exprs+= test )*
                    while True:  # loop71
                        alt71 = 2
                        LA71_0 = self.input.LA(1)

                        if LA71_0 == COMMA:
                            alt71 = 1

                        if alt71 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:140:25: COMMA exprs+= test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp1972,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp1976
                            )
                            exprs = self.test()

                            self._state.following.pop()
                            if list_exprs is None:
                                list_exprs = []
                            list_exprs.append(exprs.st)

                        else:
                            break  # loop71

                    # TEMPLATE REWRITE
                    # 140:45: -> test_list(exprs=$exprs)
                    retval.st = self.templateLib.getInstanceOf(
                        "test_list", attributes={"exprs": list_exprs}
                    )

                elif alt73 == 3:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:24: RANGE to= test ( STEP step= test )?
                    self.match(
                        self.input, RANGE, self.FOLLOW_RANGE_in_testlist_comp2012
                    )

                    self._state.following.append(self.FOLLOW_test_in_testlist_comp2016)
                    to = self.test()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:38: ( STEP step= test )?
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if LA72_0 == STEP:
                        alt72 = 1
                    if alt72 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:141:39: STEP step= test
                        self.match(
                            self.input, STEP, self.FOLLOW_STEP_in_testlist_comp2019
                        )

                        self._state.following.append(
                            self.FOLLOW_test_in_testlist_comp2023
                        )
                        step = self.test()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 141:56: -> range(from=$exprs[0]to=$to.ststep=$step.st)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:144:1: vector_comp : x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st);
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
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:144:15: (x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:144:17: x= expr COMMA y= expr COMMA z= expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp2072)
                x = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp2074)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp2078)
                y = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp2080)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp2084)
                z = self.expr()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 144:50: -> vector_comp(x=$x.sty=$y.stz=$z.st)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:146:1: trailer : ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st));
    def trailer(
        self,
    ):
        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        subscriptlist28 = None
        name29 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:146:15: ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st))
                alt74 = 2
                LA74_0 = self.input.LA(1)

                if LA74_0 == LBRACK:
                    alt74 = 1
                elif LA74_0 == DOT:
                    alt74 = 2
                else:
                    nvae = NoViableAltException("", 74, 0, self.input)

                    raise nvae

                if alt74 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:146:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer2118)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer2120
                    )
                    subscriptlist28 = self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer2122)

                    # TEMPLATE REWRITE
                    # 146:45: -> index(index=$subscriptlist.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "index",
                        attributes={
                            "index": (
                                (subscriptlist28 is not None)
                                and [subscriptlist28.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt74 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:147:17: DOT name
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer2150)

                    self._state.following.append(self.FOLLOW_name_in_trailer2152)
                    name29 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 147:26: -> dot_attr(attr=$name.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dot_attr",
                        attributes={
                            "attr": ((name29 is not None) and [name29.st] or [None])[0]
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:148:1: arglist :args+= argument ( COMMA args+= argument )* -> arg_list(args=$args);
    def arglist(
        self,
    ):
        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        list_args = None
        args = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:148:15: (args+= argument ( COMMA args+= argument )* -> arg_list(args=$args))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:148:17: args+= argument ( COMMA args+= argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist2176)
                args = self.argument()

                self._state.following.pop()
                if list_args is None:
                    list_args = []
                list_args.append(args.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:148:32: ( COMMA args+= argument )*
                while True:  # loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if LA75_0 == COMMA:
                        alt75 = 1

                    if alt75 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:148:33: COMMA args+= argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist2179)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist2183
                        )
                        args = self.argument()

                        self._state.following.pop()
                        if list_args is None:
                            list_args = []
                        list_args.append(args.st)

                    else:
                        break  # loop75

                # TEMPLATE REWRITE
                # 148:56: -> arg_list(args=$args)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:149:1: argument : kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st);
    def argument(
        self,
    ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)

        kw_or_arg = None
        arg = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:149:15: (kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:149:17: kw_or_arg= test ( ASSIGN arg= test )?
                self._state.following.append(self.FOLLOW_test_in_argument2208)
                kw_or_arg = self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:149:32: ( ASSIGN arg= test )?
                alt76 = 2
                LA76_0 = self.input.LA(1)

                if LA76_0 == ASSIGN:
                    alt76 = 1
                if alt76 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:149:33: ASSIGN arg= test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument2211)

                    self._state.following.append(self.FOLLOW_test_in_argument2215)
                    arg = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 149:51: -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:150:1: subscriptlist :subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs);
    def subscriptlist(
        self,
    ):
        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        list_subs = None
        subs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:150:15: (subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:150:17: subs+= subscript_ ( COMMA subs+= subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist2240
                )
                subs = self.subscript_()

                self._state.following.pop()
                if list_subs is None:
                    list_subs = []
                list_subs.append(subs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:150:34: ( COMMA subs+= subscript_ )*
                while True:  # loop77
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if LA77_0 == COMMA:
                        alt77 = 1

                    if alt77 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:150:35: COMMA subs+= subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist2243
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist2247
                        )
                        subs = self.subscript_()

                        self._state.following.pop()
                        if list_subs is None:
                            list_subs = []
                        list_subs.append(subs.st)

                    else:
                        break  # loop77

                # TEMPLATE REWRITE
                # 150:60: -> subscript_list(subs=$subs)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:1: subscript_ : (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st));
    def subscript_(
        self,
    ):
        retval = self.subscript__return()
        retval.start = self.input.LT(1)

        to = None
        step = None
        COLON30 = None
        COLON31 = None
        from_ = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:15: (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st))
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
                elif LA83_0 == COLON:
                    alt83 = 2
                else:
                    nvae = NoViableAltException("", 83, 0, self.input)

                    raise nvae

                if alt83 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:17: from_= test ( COLON to= ( test )? step= ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_2270)
                    from_ = self.test()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:28: ( COLON to= ( test )? step= ( sliceop )? )?
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if LA80_0 == COLON:
                        alt80 = 1
                    if alt80 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:29: COLON to= ( test )? step= ( sliceop )?
                        COLON30 = self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_2273
                        )

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:38: ( test )?
                        alt78 = 2
                        LA78_0 = self.input.LA(1)

                        if LA78_0 in {
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
                            alt78 = 1
                        if alt78 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:39: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_2278
                            )
                            to = self.test()

                            self._state.following.pop()

                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:51: ( sliceop )?
                        alt79 = 2
                        LA79_0 = self.input.LA(1)

                        if LA79_0 == COLON:
                            alt79 = 1
                        if alt79 == 1:
                            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:151:52: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_2285
                            )
                            step = self.sliceop()

                            self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 151:64: -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={
                            "from": ((from_ is not None) and [from_.st] or [None])[0],
                            "colon": COLON30,
                            "to": to.st,
                            "step": step.st,
                        },
                    )

                elif alt83 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:152:17: COLON to= ( test )? step= ( sliceop )?
                    COLON31 = self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_subscript_2331
                    )

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:152:26: ( test )?
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
                    if alt81 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:152:27: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_2336)
                        to = self.test()

                        self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:152:39: ( sliceop )?
                    alt82 = 2
                    LA82_0 = self.input.LA(1)

                    if LA82_0 == COLON:
                        alt82 = 1
                    if alt82 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:152:40: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_2343
                        )
                        step = self.sliceop()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 152:51: -> subscript(colon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={"colon": COLON31, "to": to.st, "step": step.st},
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:153:1: sliceop : COLON ( test )? -> subscipt_step(step=$test.st);
    def sliceop(
        self,
    ):
        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        test32 = None

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:153:15: ( COLON ( test )? -> subscipt_step(step=$test.st))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:153:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop2378)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:153:23: ( test )?
                alt84 = 2
                LA84_0 = self.input.LA(1)

                if LA84_0 in {
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
                    alt84 = 1
                if alt84 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:153:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop2380)
                    test32 = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 153:29: -> subscipt_step(step=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "subscipt_step",
                    attributes={
                        "step": ((test32 is not None) and [test32.st] or [None])[0]
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:155:1: exprlist :exprs+= expr ( COMMA exprs+= expr )* -> test_list(exprs=$exprs);
    def exprlist(
        self,
    ):
        retval = self.exprlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:155:10: (exprs+= expr ( COMMA exprs+= expr )* -> test_list(exprs=$exprs))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:155:12: exprs+= expr ( COMMA exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_exprlist2400)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:155:24: ( COMMA exprs+= expr )*
                while True:  # loop85
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if LA85_0 == COMMA:
                        alt85 = 1

                    if alt85 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:155:25: COMMA exprs+= expr
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist2403)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist2407)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop85

                # TEMPLATE REWRITE
                # 155:45: -> test_list(exprs=$exprs)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:156:1: testlist :exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs);
    def testlist(
        self,
    ):
        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:156:10: (exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs))
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:156:12: exprs+= test ( COMMA exprs+= test )*
                self._state.following.append(self.FOLLOW_test_in_testlist2427)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:156:24: ( COMMA exprs+= test )*
                while True:  # loop86
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if LA86_0 == COMMA:
                        alt86 = 1

                    if alt86 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:156:25: COMMA exprs+= test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist2430)

                        self._state.following.append(self.FOLLOW_test_in_testlist2434)
                        exprs = self.test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop86

                # TEMPLATE REWRITE
                # 156:45: -> test_list(exprs=$exprs)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:157:1: dict_or_set_maker : test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) ;
    def dict_or_set_maker(
        self,
    ):
        retval = self.dict_or_set_maker_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:157:18: ( test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:158:3: test ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker2453)
                self.test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:158:8: ( COLON test ( comp_for | ( COMMA test COLON test )* ) | ( comp_for | ( COMMA test )* ) )
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if LA91_0 == COLON:
                    alt91 = 1
                elif LA91_0 in {COMMA, FOR, RBRACE}:
                    alt91 = 2
                else:
                    nvae = NoViableAltException("", 91, 0, self.input)

                    raise nvae

                if alt91 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:158:10: COLON test ( comp_for | ( COMMA test COLON test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker2457
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker2459
                    )
                    self.test()

                    self._state.following.pop()

                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:158:21: ( comp_for | ( COMMA test COLON test )* )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:158:22: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker2462
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt88 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:158:33: ( COMMA test COLON test )*
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:158:33: ( COMMA test COLON test )*
                        while True:  # loop87
                            alt87 = 2
                            LA87_0 = self.input.LA(1)

                            if LA87_0 == COMMA:
                                alt87 = 1

                            if alt87 == 1:
                                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:158:34: COMMA test COLON test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker2467,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker2469
                                )
                                self.test()

                                self._state.following.pop()

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker2471,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker2473
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop87

                elif alt91 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:159:10: ( comp_for | ( COMMA test )* )
                    pass
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:159:10: ( comp_for | ( COMMA test )* )
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
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:159:11: comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker2488
                        )
                        self.comp_for()

                        self._state.following.pop()

                    elif alt90 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:159:22: ( COMMA test )*
                        pass
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:159:22: ( COMMA test )*
                        while True:  # loop89
                            alt89 = 2
                            LA89_0 = self.input.LA(1)

                            if LA89_0 == COMMA:
                                alt89 = 1

                            if alt89 == 1:
                                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:159:23: COMMA test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker2493,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker2495
                                )
                                self.test()

                                self._state.following.pop()

                            else:
                                break  # loop89

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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:162:1: comp_iter : ( comp_for | comp_if );
    def comp_iter(
        self,
    ):
        retval = self.comp_iter_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:162:11: ( comp_for | comp_if )
                alt92 = 2
                LA92_0 = self.input.LA(1)

                if LA92_0 == FOR:
                    alt92 = 1
                elif LA92_0 == IF:
                    alt92 = 2
                else:
                    nvae = NoViableAltException("", 92, 0, self.input)

                    raise nvae

                if alt92 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:162:13: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter2509)
                    self.comp_for()

                    self._state.following.pop()

                elif alt92 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:162:24: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter2513)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:163:1: comp_for : FOR exprlist IN or_test ( comp_iter )? ;
    def comp_for(
        self,
    ):
        retval = self.comp_for_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:163:11: ( FOR exprlist IN or_test ( comp_iter )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:163:13: FOR exprlist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for2521)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for2523)
                self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for2525)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for2527)
                self.or_test()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:163:37: ( comp_iter )?
                alt93 = 2
                LA93_0 = self.input.LA(1)

                if LA93_0 in {FOR, IF}:
                    alt93 = 1
                if alt93 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:163:37: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for2529)
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
    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:164:1: comp_if : IF test_nocond ( comp_iter )? ;
    def comp_if(
        self,
    ):
        retval = self.comp_if_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:164:11: ( IF test_nocond ( comp_iter )? )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:164:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if2539)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if2541)
                self.test_nocond()

                self._state.following.pop()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:164:28: ( comp_iter )?
                alt94 = 2
                LA94_0 = self.input.LA(1)

                if LA94_0 in {FOR, IF}:
                    alt94 = 1
                if alt94 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcParser.g:164:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if2543)
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

    FOLLOW_declaration_in_scenario44 = frozenset([1, 73, 100, 109, 123])
    FOLLOW_NEWLINE_in_scenario46 = frozenset([1, 73, 100, 109, 123])
    FOLLOW_settings_in_scenario49 = frozenset([1, 109, 123])
    FOLLOW_stage_in_scenario52 = frozenset([1, 123])
    FOLLOW_writers_in_scenario55 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration97 = frozenset([43])
    FOLLOW_ID_in_declaration99 = frozenset([15, 73])
    FOLLOW_COLON_in_declaration102 = frozenset([43, 119])
    FOLLOW_name_in_declaration104 = frozenset([73])
    FOLLOW_NEWLINE_in_declaration108 = frozenset([1])
    FOLLOW_SETTINGS_in_settings120 = frozenset([15])
    FOLLOW_COLON_in_settings122 = frozenset([73])
    FOLLOW_NEWLINE_in_settings124 = frozenset([49])
    FOLLOW_INDENT_in_settings126 = frozenset([43])
    FOLLOW_setting_in_settings130 = frozenset([19, 43])
    FOLLOW_DEDENT_in_settings133 = frozenset([1])
    FOLLOW_STAGE_in_stage155 = frozenset([15])
    FOLLOW_COLON_in_stage157 = frozenset([73])
    FOLLOW_NEWLINE_in_stage159 = frozenset([49])
    FOLLOW_INDENT_in_stage161 = frozenset(
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
    FOLLOW_stmts_in_stage163 = frozenset([19])
    FOLLOW_DEDENT_in_stage165 = frozenset([1])
    FOLLOW_WRITERS_in_writers176 = frozenset([15])
    FOLLOW_COLON_in_writers178 = frozenset([73])
    FOLLOW_NEWLINE_in_writers180 = frozenset([49])
    FOLLOW_INDENT_in_writers182 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_stmt_in_writers185 = frozenset(
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
    FOLLOW_writer_in_writers189 = frozenset(
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
    FOLLOW_DEDENT_in_writers193 = frozenset([1])
    FOLLOW_ID_in_setting208 = frozenset([5])
    FOLLOW_ASSIGN_in_setting210 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_setting212 = frozenset([73])
    FOLLOW_NEWLINE_in_setting214 = frozenset([1])
    FOLLOW_open_stmt_in_stmts245 = frozenset(
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
    FOLLOW_aug_expr_stmt_in_stmts249 = frozenset(
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
    FOLLOW_edit_stmt_in_stmts253 = frozenset(
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
    FOLLOW_behavior_stmt_in_stmts257 = frozenset(
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
    FOLLOW_ID_in_writer274 = frozenset([15])
    FOLLOW_COLON_in_writer276 = frozenset([73])
    FOLLOW_NEWLINE_in_writer278 = frozenset([49])
    FOLLOW_INDENT_in_writer280 = frozenset([43])
    FOLLOW_writer_setting_in_writer282 = frozenset([19, 43])
    FOLLOW_DEDENT_in_writer285 = frozenset([1])
    FOLLOW_ID_in_writer_setting292 = frozenset([5])
    FOLLOW_ASSIGN_in_writer_setting294 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_writer_setting296 = frozenset([73])
    FOLLOW_NEWLINE_in_writer_setting298 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt309 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_open_stmt311 = frozenset([73])
    FOLLOW_NEWLINE_in_open_stmt313 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt320 = frozenset([43, 115, 119])
    FOLLOW_TIMELINE_in_edit_stmt323 = frozenset([15])
    FOLLOW_name_in_edit_stmt327 = frozenset([15])
    FOLLOW_edit_block_in_edit_stmt330 = frozenset([1])
    FOLLOW_CREATE_in_create_expr339 = frozenset(
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
    FOLLOW_test_in_create_expr341 = frozenset([13, 37, 59, 68, 102, 103, 111])
    FOLLOW_STEREO_in_create_expr351 = frozenset([13])
    FOLLOW_CAMERA_in_create_expr354 = frozenset([15, 73])
    FOLLOW_shapes_in_create_expr358 = frozenset([15, 73])
    FOLLOW_light_type_in_create_expr362 = frozenset([58])
    FOLLOW_LIGHT_in_create_expr364 = frozenset([15, 73])
    FOLLOW_FROM_in_create_expr368 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_create_expr370 = frozenset([15, 73])
    FOLLOW_edit_block_in_create_expr374 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr378 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr387 = frozenset([15])
    FOLLOW_simple_block_in_create_expr390 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr431 = frozenset(
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
    FOLLOW_test_in_instantiate_expr434 = frozenset([37])
    FOLLOW_FROM_in_instantiate_expr438 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_instantiate_expr440 = frozenset([15, 73])
    FOLLOW_edit_block_in_instantiate_expr443 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr447 = frozenset([1])
    FOLLOW_GROUP_in_group_expr461 = frozenset([55])
    FOLLOW_LBRACK_in_group_expr463 = frozenset([43, 119])
    FOLLOW_name_in_group_expr465 = frozenset([16, 89])
    FOLLOW_COMMA_in_group_expr468 = frozenset([43, 119])
    FOLLOW_name_in_group_expr470 = frozenset([16, 89])
    FOLLOW_RBRACK_in_group_expr474 = frozenset([15, 73])
    FOLLOW_edit_block_in_group_expr477 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr481 = frozenset([1])
    FOLLOW_GET_in_get_expr497 = frozenset(
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
    FOLLOW_CAMERA_in_get_expr501 = frozenset([6])
    FOLLOW_LIGHT_in_get_expr505 = frozenset([6])
    FOLLOW_MATERIAL_in_get_expr509 = frozenset([6])
    FOLLOW_name_in_get_expr513 = frozenset([6])
    FOLLOW_AT_in_get_expr516 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_get_expr520 = frozenset([15, 73])
    FOLLOW_simple_block_in_get_expr523 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr527 = frozenset([1])
    FOLLOW_COLON_in_edit_block538 = frozenset([73])
    FOLLOW_NEWLINE_in_edit_block540 = frozenset([49])
    FOLLOW_INDENT_in_edit_block542 = frozenset(
        [14, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_attr_in_edit_block545 = frozenset(
        [14, 19, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block549 = frozenset(
        [14, 19, 28, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_DEDENT_in_edit_block553 = frozenset([1])
    FOLLOW_COLON_in_simple_block560 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_block562 = frozenset([49])
    FOLLOW_INDENT_in_simple_block564 = frozenset([43, 119])
    FOLLOW_simple_attr_in_simple_block566 = frozenset([19, 43, 119])
    FOLLOW_DEDENT_in_simple_block569 = frozenset([1])
    FOLLOW_core_attr_in_attr586 = frozenset([1])
    FOLLOW_simple_attr_in_attr590 = frozenset([1])
    FOLLOW_compound_attr_in_attr594 = frozenset([1])
    FOLLOW_name_in_simple_attr603 = frozenset(
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
    FOLLOW_COLON_in_simple_attr606 = frozenset([43, 119])
    FOLLOW_name_in_simple_attr608 = frozenset(
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
    FOLLOW_test_in_simple_attr612 = frozenset([73])
    FOLLOW_NEWLINE_in_simple_attr615 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr624 = frozenset([79])
    FOLLOW_ON_in_compound_attr626 = frozenset([43, 119])
    FOLLOW_name_in_compound_attr628 = frozenset([15, 73])
    FOLLOW_ROT_AROUND_in_compound_attr632 = frozenset([43, 119])
    FOLLOW_name_in_compound_attr634 = frozenset([15, 73])
    FOLLOW_PHYSICS_in_compound_attr638 = frozenset([15, 73])
    FOLLOW_simple_block_in_compound_attr642 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr646 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr663 = frozenset([8, 116])
    FOLLOW_AXIS_in_core_attr665 = frozenset([116])
    FOLLOW_TO_in_core_attr668 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr670 = frozenset([73])
    FOLLOW_CAM_TRANSLATE_in_core_attr678 = frozenset([116])
    FOLLOW_TO_in_core_attr680 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr682 = frozenset([73])
    FOLLOW_ROTATE_in_core_attr690 = frozenset(
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
    FOLLOW_AXIS_in_core_attr692 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr695 = frozenset([73, 82])
    FOLLOW_ORDER_in_core_attr697 = frozenset([73])
    FOLLOW_SCALE_in_core_attr706 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr708 = frozenset([73])
    FOLLOW_LOOK_AT_in_core_attr716 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr718 = frozenset([73])
    FOLLOW_UP_AXIS_in_core_attr726 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr728 = frozenset([73])
    FOLLOW_SIZE_in_core_attr736 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr738 = frozenset([73])
    FOLLOW_SEMANTICS_in_core_attr746 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr748 = frozenset([73])
    FOLLOW_VISIBLE_in_core_attr756 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_core_attr758 = frozenset([73])
    FOLLOW_NEWLINE_in_core_attr764 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt774 = frozenset([15])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt776 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block783 = frozenset([73])
    FOLLOW_NEWLINE_in_inner_behavior_block785 = frozenset([49])
    FOLLOW_INDENT_in_inner_behavior_block787 = frozenset(
        [14, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_attr_in_inner_behavior_block789 = frozenset(
        [14, 19, 43, 62, 83, 91, 92, 95, 96, 98, 105, 117, 119, 121, 122]
    )
    FOLLOW_DEDENT_in_inner_behavior_block792 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt803 = frozenset([15])
    FOLLOW_behavior_block_in_behavior_stmt805 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr813 = frozenset(
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
    FOLLOW_test_in_behavior_expr815 = frozenset([36, 114])
    FOLLOW_set_in_behavior_expr818 = frozenset([1])
    FOLLOW_COLON_in_behavior_block831 = frozenset([73])
    FOLLOW_NEWLINE_in_behavior_block833 = frozenset([49])
    FOLLOW_INDENT_in_behavior_block835 = frozenset(
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
    FOLLOW_aug_expr_stmt_in_behavior_block838 = frozenset(
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
    FOLLOW_edit_stmt_in_behavior_block842 = frozenset(
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
    FOLLOW_DEDENT_in_behavior_block846 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt856 = frozenset([5, 7])
    FOLLOW_set_in_expr_stmt858 = frozenset(
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
    FOLLOW_testlist_in_expr_stmt867 = frozenset([73])
    FOLLOW_fetch_expr_in_expr_stmt871 = frozenset([73])
    FOLLOW_NEWLINE_in_expr_stmt874 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt887 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_aug_expr_stmt897 = frozenset(
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
    FOLLOW_testlist_in_aug_expr_stmt900 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt904 = frozenset([73])
    FOLLOW_NEWLINE_in_aug_expr_stmt908 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt918 = frozenset(
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
    FOLLOW_testlist_in_aug_expr_stmt931 = frozenset([73])
    FOLLOW_fetch_expr_in_aug_expr_stmt935 = frozenset([73])
    FOLLOW_NEWLINE_in_aug_expr_stmt938 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt950 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt954 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt958 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt962 = frozenset([1])
    FOLLOW_create_expr_in_aug_expr_stmt986 = frozenset([1])
    FOLLOW_instantiate_expr_in_aug_expr_stmt990 = frozenset([1])
    FOLLOW_get_expr_in_aug_expr_stmt994 = frozenset([1])
    FOLLOW_group_expr_in_aug_expr_stmt998 = frozenset([1])
    FOLLOW_FETCH_in_fetch_expr1007 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_fetch_expr1009 = frozenset([37])
    FOLLOW_FROM_in_fetch_expr1011 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_fetch_expr1013 = frozenset([1, 60, 67, 90])
    FOLLOW_MATCH_in_fetch_expr1016 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_fetch_expr1018 = frozenset([1, 60, 90])
    FOLLOW_LIMIT_in_fetch_expr1023 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_fetch_expr1025 = frozenset([1, 90])
    FOLLOW_RECURSIVE_in_fetch_expr1029 = frozenset([1])
    FOLLOW_or_test_in_test1049 = frozenset([1, 47])
    FOLLOW_IF_in_test1052 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_or_test_in_test1056 = frozenset([26])
    FOLLOW_ELSE_in_test1058 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_test1062 = frozenset([1])
    FOLLOW_or_test_in_test_nocond1104 = frozenset([1])
    FOLLOW_and_test_in_or_test1126 = frozenset([1, 81])
    FOLLOW_OR_in_or_test1129 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_and_test_in_or_test1133 = frozenset([1, 81])
    FOLLOW_not_test_in_and_test1156 = frozenset([1, 4])
    FOLLOW_AND_in_and_test1159 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_not_test_in_and_test1163 = frozenset([1, 4])
    FOLLOW_NOT_in_not_test1184 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_not_test_in_not_test1188 = frozenset([1])
    FOLLOW_comparison_in_not_test1214 = frozenset([1])
    FOLLOW_expr_in_comparison1228 = frozenset([1, 27, 40, 41, 48, 53, 65, 66, 76, 77])
    FOLLOW_comp_op_in_comparison1231 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_in_comparison1235 = frozenset([1, 27, 40, 41, 48, 53, 65, 66, 76, 77])
    FOLLOW_LT_in_comp_op1262 = frozenset([1])
    FOLLOW_GT_in_comp_op1266 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op1270 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op1274 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op1278 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op1282 = frozenset([1])
    FOLLOW_IN_in_comp_op1286 = frozenset([1])
    FOLLOW_NOT_in_comp_op1290 = frozenset([48])
    FOLLOW_IN_in_comp_op1292 = frozenset([1])
    FOLLOW_IS_in_comp_op1296 = frozenset([1])
    FOLLOW_IS_in_comp_op1300 = frozenset([76])
    FOLLOW_NOT_in_comp_op1302 = frozenset([1])
    FOLLOW_xor_expr_in_expr1319 = frozenset([1, 12])
    FOLLOW_BIT_OR_in_expr1322 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_xor_expr_in_expr1326 = frozenset([1, 12])
    FOLLOW_and_expr_in_xor_expr1349 = frozenset([1, 124])
    FOLLOW_XOR_in_xor_expr1352 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_and_expr_in_xor_expr1356 = frozenset([1, 124])
    FOLLOW_shift_expr_in_and_expr1379 = frozenset([1, 10])
    FOLLOW_BIT_AND_in_and_expr1382 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_shift_expr_in_and_expr1386 = frozenset([1, 10])
    FOLLOW_arith_expr_in_shift_expr1407 = frozenset([1, 64, 94])
    FOLLOW_LSHIFT_in_shift_expr1413 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_RSHIFT_in_shift_expr1417 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_arith_expr_in_shift_expr1422 = frozenset([1, 64, 94])
    FOLLOW_term_in_arith_expr1448 = frozenset([1, 69, 84])
    FOLLOW_PLUS_in_arith_expr1454 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_MINUS_in_arith_expr1458 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_term_in_arith_expr1463 = frozenset([1, 69, 84])
    FOLLOW_factor_in_term1495 = frozenset([1, 22, 44, 70, 71])
    FOLLOW_MUL_in_term1501 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_DIV_in_term1505 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_MOD_in_term1509 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_IDIV_in_term1513 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_factor_in_term1518 = frozenset([1, 22, 44, 70, 71])
    FOLLOW_PLUS_in_factor1549 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_MINUS_in_factor1553 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_BIT_NOT_in_factor1557 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_factor_in_factor1562 = frozenset([1])
    FOLLOW_power_in_factor1592 = frozenset([1])
    FOLLOW_atom_expr_in_power1609 = frozenset([1, 86])
    FOLLOW_POWER_in_power1612 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_factor_in_power1614 = frozenset([1])
    FOLLOW_atom_in_atom_expr1639 = frozenset([1, 23, 55])
    FOLLOW_trailer_in_atom_expr1644 = frozenset([1, 23, 55])
    FOLLOW_LPAREN_in_atom1669 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_atom1673 = frozenset([93])
    FOLLOW_RPAREN_in_atom1675 = frozenset([1])
    FOLLOW_LBRACK_in_atom1690 = frozenset(
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
    FOLLOW_testlist_comp_in_atom1692 = frozenset([89])
    FOLLOW_RBRACK_in_atom1695 = frozenset([1])
    FOLLOW_LT_in_atom1710 = frozenset(
        [11, 21, 31, 33, 40, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_vector_comp_in_atom1712 = frozenset([40])
    FOLLOW_GT_in_atom1715 = frozenset([1])
    FOLLOW_LBRACE_in_atom1730 = frozenset(
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
    FOLLOW_dict_or_set_maker_in_atom1732 = frozenset([88])
    FOLLOW_RBRACE_in_atom1735 = frozenset([1])
    FOLLOW_LEN_in_atom1750 = frozenset([63])
    FOLLOW_LPAREN_in_atom1752 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_atom1756 = frozenset([93])
    FOLLOW_RPAREN_in_atom1758 = frozenset([1])
    FOLLOW_name_in_atom1773 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom1783 = frozenset([1])
    FOLLOW_DISTRIBUTION_in_atom1799 = frozenset([63])
    FOLLOW_LPAREN_in_atom1801 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_arglist_in_atom1803 = frozenset([93])
    FOLLOW_RPAREN_in_atom1805 = frozenset([1])
    FOLLOW_INTEGER_in_atom1825 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom1835 = frozenset([1])
    FOLLOW_STRING_in_atom1845 = frozenset([1])
    FOLLOW_NONE_in_atom1855 = frozenset([1])
    FOLLOW_TRUE_in_atom1867 = frozenset([1])
    FOLLOW_FALSE_in_atom1879 = frozenset([1])
    FOLLOW_ID_in_name1899 = frozenset([1])
    FOLLOW_UNDERSCORE_in_name1909 = frozenset([1])
    FOLLOW_test_in_testlist_comp1928 = frozenset([1, 16, 34, 87])
    FOLLOW_comp_for_in_testlist_comp1932 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp1972 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_testlist_comp1976 = frozenset([1, 16])
    FOLLOW_RANGE_in_testlist_comp2012 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_testlist_comp2016 = frozenset([1, 110])
    FOLLOW_STEP_in_testlist_comp2019 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_testlist_comp2023 = frozenset([1])
    FOLLOW_expr_in_vector_comp2072 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp2074 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_in_vector_comp2078 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp2080 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_in_vector_comp2084 = frozenset([1])
    FOLLOW_LBRACK_in_trailer2118 = frozenset(
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
    FOLLOW_subscriptlist_in_trailer2120 = frozenset([89])
    FOLLOW_RBRACK_in_trailer2122 = frozenset([1])
    FOLLOW_DOT_in_trailer2150 = frozenset([43, 119])
    FOLLOW_name_in_trailer2152 = frozenset([1])
    FOLLOW_argument_in_arglist2176 = frozenset([1, 16])
    FOLLOW_COMMA_in_arglist2179 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_argument_in_arglist2183 = frozenset([1, 16])
    FOLLOW_test_in_argument2208 = frozenset([1, 5])
    FOLLOW_ASSIGN_in_argument2211 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_argument2215 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist2240 = frozenset([1, 16])
    FOLLOW_COMMA_in_subscriptlist2243 = frozenset(
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
    FOLLOW_subscript__in_subscriptlist2247 = frozenset([1, 16])
    FOLLOW_test_in_subscript_2270 = frozenset([1, 15])
    FOLLOW_COLON_in_subscript_2273 = frozenset(
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
    FOLLOW_test_in_subscript_2278 = frozenset([1, 15])
    FOLLOW_sliceop_in_subscript_2285 = frozenset([1])
    FOLLOW_COLON_in_subscript_2331 = frozenset(
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
    FOLLOW_test_in_subscript_2336 = frozenset([1, 15])
    FOLLOW_sliceop_in_subscript_2343 = frozenset([1])
    FOLLOW_COLON_in_sliceop2378 = frozenset(
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
    FOLLOW_test_in_sliceop2380 = frozenset([1])
    FOLLOW_expr_in_exprlist2400 = frozenset([1, 16])
    FOLLOW_COMMA_in_exprlist2403 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_expr_in_exprlist2407 = frozenset([1, 16])
    FOLLOW_test_in_testlist2427 = frozenset([1, 16])
    FOLLOW_COMMA_in_testlist2430 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_testlist2434 = frozenset([1, 16])
    FOLLOW_test_in_dict_or_set_maker2453 = frozenset([1, 15, 16, 34])
    FOLLOW_COLON_in_dict_or_set_maker2457 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_dict_or_set_maker2459 = frozenset([1, 16, 34])
    FOLLOW_comp_for_in_dict_or_set_maker2462 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker2467 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_dict_or_set_maker2469 = frozenset([15])
    FOLLOW_COLON_in_dict_or_set_maker2471 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_dict_or_set_maker2473 = frozenset([1, 16])
    FOLLOW_comp_for_in_dict_or_set_maker2488 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker2493 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_in_dict_or_set_maker2495 = frozenset([1, 16])
    FOLLOW_comp_for_in_comp_iter2509 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter2513 = frozenset([1])
    FOLLOW_FOR_in_comp_for2521 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 84, 101, 112, 118, 119]
    )
    FOLLOW_exprlist_in_comp_for2523 = frozenset([48])
    FOLLOW_IN_in_comp_for2525 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_or_test_in_comp_for2527 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_for2529 = frozenset([1])
    FOLLOW_IF_in_comp_if2539 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 63, 65, 69, 74, 76, 84, 101, 112, 118, 119]
    )
    FOLLOW_test_nocond_in_comp_if2541 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_if2543 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
