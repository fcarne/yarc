# $ANTLR 3.5.3 YarcParser.g 2023-05-14 18:42:34

import sys

import stringtemplate3
from antlr3 import (
    BaseRecognizer,
    EarlyExitException,
    NoViableAltException,
    ParserRuleReturnScope,
    RecognitionException,
    RecognizerSharedState,
    Token,
)

from yarc.dsl.v3.handler.handler import Attribute
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
MUL = 70
NESTED_CODE = 71
NEWLINE = 72
NONE = 73
NON_ZERO_DIGIT = 74
NOT = 75
NOT_EQ = 76
OCT_DIGIT = 77
ON = 78
OPEN = 79
OR = 80
ORDER = 81
PHYSICS = 82
PLUS = 83
POINT_FLOAT = 84
POWER = 85
RANGE = 86
RBRACE = 87
RBRACK = 88
RECURSIVE = 89
ROTATE = 90
ROT_AROUND = 91
RPAREN = 92
RSHIFT = 93
SCALE = 94
SCATTER = 95
SCENARIO = 96
SEMANTICS = 97
SEMI = 98
SETTINGS = 99
SETTING_ID = 100
SHAPE = 101
SHORT_STRING = 102
SIZE = 103
SKIP_ = 104
SNIPPET = 105
SPACES = 106
STAGE = 107
STEP = 108
STEREO = 109
STRING = 110
STRING_ESCAPE_SEQ = 111
TIME = 112
TIMELINE = 113
TO = 114
TRANSLATE = 115
TRUE = 116
UNDERSCORE = 117
UNKNOWN = 118
UP_AXIS = 119
VISIBLE = 120
WRITERS = 121
XOR = 122

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
    70: "MUL",
    71: "NESTED_CODE",
    72: "NEWLINE",
    73: "NONE",
    74: "NON_ZERO_DIGIT",
    75: "NOT",
    76: "NOT_EQ",
    77: "OCT_DIGIT",
    78: "ON",
    79: "OPEN",
    80: "OR",
    81: "ORDER",
    82: "PHYSICS",
    83: "PLUS",
    84: "POINT_FLOAT",
    85: "POWER",
    86: "RANGE",
    87: "RBRACE",
    88: "RBRACK",
    89: "RECURSIVE",
    90: "ROTATE",
    91: "ROT_AROUND",
    92: "RPAREN",
    93: "RSHIFT",
    94: "SCALE",
    95: "SCATTER",
    96: "SCENARIO",
    97: "SEMANTICS",
    98: "SEMI",
    99: "SETTINGS",
    100: "SETTING_ID",
    101: "SHAPE",
    102: "SHORT_STRING",
    103: "SIZE",
    104: "SKIP_",
    105: "SNIPPET",
    106: "SPACES",
    107: "STAGE",
    108: "STEP",
    109: "STEREO",
    110: "STRING",
    111: "STRING_ESCAPE_SEQ",
    112: "TIME",
    113: "TIMELINE",
    114: "TO",
    115: "TRANSLATE",
    116: "TRUE",
    117: "UNDERSCORE",
    118: "UNKNOWN",
    119: "UP_AXIS",
    120: "VISIBLE",
    121: "WRITERS",
    122: "XOR",
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
    # YarcParser.g:20:1: scenario : ( NEWLINE )* declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st);
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
                # YarcParser.g:20:10: ( ( NEWLINE )* declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )? -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st))
                # YarcParser.g:20:12: ( NEWLINE )* declaration ( NEWLINE )* ( settings )? ( stage )? ( writers )?
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

                # YarcParser.g:20:33: ( NEWLINE )*
                while True:  # loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if LA2_0 == NEWLINE:
                        alt2 = 1

                    if alt2 == 1:
                        # YarcParser.g:20:33: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_scenario64
                        )

                    else:
                        break  # loop2

                # YarcParser.g:20:42: ( settings )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if LA3_0 == SETTINGS:
                    alt3 = 1
                if alt3 == 1:
                    # YarcParser.g:20:42: settings
                    self._state.following.append(self.FOLLOW_settings_in_scenario67)
                    settings2 = self.settings()

                    self._state.following.pop()

                # YarcParser.g:20:52: ( stage )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == STAGE:
                    alt4 = 1
                if alt4 == 1:
                    # YarcParser.g:20:52: stage
                    self._state.following.append(self.FOLLOW_stage_in_scenario70)
                    stage3 = self.stage()

                    self._state.following.pop()

                # YarcParser.g:20:59: ( writers )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if LA5_0 == WRITERS:
                    alt5 = 1
                if alt5 == 1:
                    # YarcParser.g:20:59: writers
                    self._state.following.append(self.FOLLOW_writers_in_scenario73)
                    writers4 = self.writers()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 21:3: -> scenario(name=$declaration.scenario_namesettings=$settings.ststage=$stage.stwriters=$writers.st)
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
    # YarcParser.g:24:1: declaration returns [scenario_name] : SCENARIO ID ( COLON name )? NEWLINE ;
    def declaration(
        self,
    ):
        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        ID5 = None
        name6 = None

        try:
            try:
                # YarcParser.g:24:37: ( SCENARIO ID ( COLON name )? NEWLINE )
                # YarcParser.g:24:39: SCENARIO ID ( COLON name )? NEWLINE
                self.match(self.input, SCENARIO, self.FOLLOW_SCENARIO_in_declaration115)

                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_declaration117)

                # YarcParser.g:24:51: ( COLON name )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if LA6_0 == COLON:
                    alt6 = 1
                if alt6 == 1:
                    # YarcParser.g:24:52: COLON name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration120)

                    self._state.following.append(self.FOLLOW_name_in_declaration122)
                    name6 = self.name()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_declaration126)

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
    # YarcParser.g:28:1: settings : SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT -> settings(setting_list=$sets);
    def settings(
        self,
    ):
        retval = self.settings_return()
        retval.start = self.input.LT(1)

        list_sets = None
        sets = None
        try:
            try:
                # YarcParser.g:28:13: ( SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT -> settings(setting_list=$sets))
                # YarcParser.g:28:15: SETTINGS COLON NEWLINE INDENT (sets+= setting )+ DEDENT
                self.match(self.input, SETTINGS, self.FOLLOW_SETTINGS_in_settings149)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_settings151)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_settings153)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_settings155)

                # YarcParser.g:28:49: (sets+= setting )+
                cnt7 = 0
                while True:  # loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if LA7_0 == ID:
                        alt7 = 1

                    if alt7 == 1:
                        # YarcParser.g:28:49: sets+= setting
                        self._state.following.append(self.FOLLOW_setting_in_settings159)
                        sets = self.setting()

                        self._state.following.pop()
                        if list_sets is None:
                            list_sets = []
                        list_sets.append(sets.st)

                    else:
                        if cnt7 >= 1:
                            break  # loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_settings162)

                # TEMPLATE REWRITE
                # 28:67: -> settings(setting_list=$sets)
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
    # YarcParser.g:29:1: stage : STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st};
    def stage(
        self,
    ):
        retval = self.stage_return()
        retval.start = self.input.LT(1)

        stmts7 = None

        try:
            try:
                # YarcParser.g:29:13: ( STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st})
                # YarcParser.g:29:15: STAGE COLON NEWLINE INDENT stmts DEDENT
                self.match(self.input, STAGE, self.FOLLOW_STAGE_in_stage184)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_stage186)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stage188)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stage190)

                self._state.following.append(self.FOLLOW_stmts_in_stage192)
                stmts7 = self.stmts()

                self._state.following.pop()

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stage194)

                # TEMPLATE REWRITE
                # 29:55: -> {$stmts.st}
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
    # YarcParser.g:30:1: writers : WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | writer )+ DEDENT -> writers(stmts=$stmts_);
    def writers(
        self,
    ):
        retval = self.writers_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:30:13: ( WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | writer )+ DEDENT -> writers(stmts=$stmts_))
                # YarcParser.g:30:15: WRITERS COLON NEWLINE INDENT stmts_+= ( expr_stmt | writer )+ DEDENT
                self.match(self.input, WRITERS, self.FOLLOW_WRITERS_in_writers209)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writers211)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writers213)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writers215)

                # YarcParser.g:30:52: ( expr_stmt | writer )+
                cnt8 = 0
                while True:  # loop8
                    alt8 = 3
                    LA8_0 = self.input.LA(1)

                    if LA8_0 in {
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
                        alt8 = 1
                    elif LA8_0 == ID:
                        LA8_3 = self.input.LA(2)

                        if LA8_3 == COLON:
                            alt8 = 2
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

                    if alt8 == 1:
                        # YarcParser.g:30:53: expr_stmt
                        self._state.following.append(
                            self.FOLLOW_expr_stmt_in_writers220
                        )
                        stmts_ = self.expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt8 == 2:
                        # YarcParser.g:30:65: writer
                        self._state.following.append(self.FOLLOW_writer_in_writers224)
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

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writers228)

                # TEMPLATE REWRITE
                # 30:81: -> writers(stmts=$stmts_)
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
    # YarcParser.g:32:1: setting : ID ASSIGN test NEWLINE -> setting(setting=$ID.textvalue=$test.st);
    def setting(
        self,
    ):
        retval = self.setting_return()
        retval.start = self.input.LT(1)

        ID8 = None
        test9 = None

        try:
            try:
                # YarcParser.g:32:16: ( ID ASSIGN test NEWLINE -> setting(setting=$ID.textvalue=$test.st))
                # YarcParser.g:32:18: ID ASSIGN test NEWLINE
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_setting252)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_setting254)

                self._state.following.append(self.FOLLOW_test_in_setting256)
                test9 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_setting258)

                # TEMPLATE REWRITE
                # 32:41: -> setting(setting=$ID.textvalue=$test.st)
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
    # YarcParser.g:33:1: stmts :stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | edit_stmt | behavior_stmt )+ -> stage(stmts=$stmts_);
    def stmts(
        self,
    ):
        retval = self.stmts_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:33:16: (stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | edit_stmt | behavior_stmt )+ -> stage(stmts=$stmts_))
                # YarcParser.g:33:18: stmts_+= ( open_stmt )? stmts_+= ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                pass
                # YarcParser.g:33:26: ( open_stmt )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if LA9_0 == OPEN:
                    alt9 = 1
                if alt9 == 1:
                    # YarcParser.g:33:27: open_stmt
                    self._state.following.append(self.FOLLOW_open_stmt_in_stmts292)
                    stmts_ = self.open_stmt()

                    self._state.following.pop()
                    if list_stmts_ is None:
                        list_stmts_ = []
                    list_stmts_.append(stmts_.st)

                # YarcParser.g:33:47: ( aug_expr_stmt | edit_stmt | behavior_stmt )+
                cnt10 = 0
                while True:  # loop10
                    alt10 = 4
                    LA10 = self.input.LA(1)
                    if LA10 in {
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
                        alt10 = 1
                    elif LA10 in {EDIT}:
                        alt10 = 2
                    elif LA10 in {EVERY}:
                        alt10 = 3

                    if alt10 == 1:
                        # YarcParser.g:33:48: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_stmts299
                        )
                        stmts_ = self.aug_expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt10 == 2:
                        # YarcParser.g:33:64: edit_stmt
                        self._state.following.append(self.FOLLOW_edit_stmt_in_stmts303)
                        stmts_ = self.edit_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt10 == 3:
                        # YarcParser.g:33:76: behavior_stmt
                        self._state.following.append(
                            self.FOLLOW_behavior_stmt_in_stmts307
                        )
                        stmts_ = self.behavior_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt10 >= 1:
                            break  # loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1

                # TEMPLATE REWRITE
                # 33:92: -> stage(stmts=$stmts_)
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
    # YarcParser.g:34:1: writer : ID COLON NEWLINE INDENT (writer_params+= writer_param )+ DEDENT -> writer(writer_id=$ID.textwriter_params=$writer_params);
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
                # YarcParser.g:34:16: ( ID COLON NEWLINE INDENT (writer_params+= writer_param )+ DEDENT -> writer(writer_id=$ID.textwriter_params=$writer_params))
                # YarcParser.g:34:18: ID COLON NEWLINE INDENT (writer_params+= writer_param )+ DEDENT
                ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_writer333)

                self.match(self.input, COLON, self.FOLLOW_COLON_in_writer335)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer337)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_writer339)

                # YarcParser.g:34:55: (writer_params+= writer_param )+
                cnt11 = 0
                while True:  # loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if LA11_0 == ID:
                        alt11 = 1

                    if alt11 == 1:
                        # YarcParser.g:34:55: writer_params+= writer_param
                        self._state.following.append(
                            self.FOLLOW_writer_param_in_writer343
                        )
                        writer_params = self.writer_param()

                        self._state.following.pop()
                        if list_writer_params is None:
                            list_writer_params = []
                        list_writer_params.append(writer_params.st)

                    else:
                        if cnt11 >= 1:
                            break  # loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_writer346)

                # TEMPLATE REWRITE
                # 34:78: -> writer(writer_id=$ID.textwriter_params=$writer_params)
                retval.st = self.templateLib.getInstanceOf(
                    "writer",
                    attributes={
                        "writer_id": ID10.text,
                        "writer_params": list_writer_params,
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
    # YarcParser.g:35:1: writer_param : ID ASSIGN test NEWLINE -> writer_param(param=$ID.textvalue=$test.st);
    def writer_param(
        self,
    ):
        retval = self.writer_param_return()
        retval.start = self.input.LT(1)

        ID11 = None
        test12 = None

        try:
            try:
                # YarcParser.g:35:16: ( ID ASSIGN test NEWLINE -> writer_param(param=$ID.textvalue=$test.st))
                # YarcParser.g:35:18: ID ASSIGN test NEWLINE
                ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_writer_param370)

                self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_writer_param372)

                self._state.following.append(self.FOLLOW_test_in_writer_param374)
                test12 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_writer_param376)

                # TEMPLATE REWRITE
                # 35:41: -> writer_param(param=$ID.textvalue=$test.st)
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
    # YarcParser.g:39:1: open_stmt : OPEN test NEWLINE -> open_stmt(path=$test.st);
    def open_stmt(
        self,
    ):
        retval = self.open_stmt_return()
        retval.start = self.input.LT(1)

        test13 = None

        try:
            try:
                # YarcParser.g:39:11: ( OPEN test NEWLINE -> open_stmt(path=$test.st))
                # YarcParser.g:39:13: OPEN test NEWLINE
                self.match(self.input, OPEN, self.FOLLOW_OPEN_in_open_stmt402)

                self._state.following.append(self.FOLLOW_test_in_open_stmt404)
                test13 = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_open_stmt406)

                # TEMPLATE REWRITE
                # 39:31: -> open_stmt(path=$test.st)
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
    # YarcParser.g:40:1: edit_stmt : EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))) ;
    def edit_stmt(
        self,
    ):
        retval = self.edit_stmt_return()
        retval.start = self.input.LT(1)

        list_params = None
        list_values = None
        id = None
        edit_block14 = None
        params = None
        values = None
        try:
            try:
                # YarcParser.g:40:11: ( EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))) )
                # YarcParser.g:40:13: EDIT ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                self.match(self.input, EDIT, self.FOLLOW_EDIT_in_edit_stmt422)

                # YarcParser.g:40:18: ( TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT -> edit_timeline(params=$paramsvalues=$values)|id= name edit_block[$id.st] -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if LA13_0 == TIMELINE:
                    alt13 = 1
                elif LA13_0 in {ID, UNDERSCORE}:
                    alt13 = 2
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # YarcParser.g:40:19: TIMELINE COLON NEWLINE INDENT (params+= name values+= test NEWLINE )+ DEDENT
                    self.match(
                        self.input, TIMELINE, self.FOLLOW_TIMELINE_in_edit_stmt425
                    )

                    self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_stmt427)

                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_stmt429)

                    self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_stmt431)

                    # YarcParser.g:40:49: (params+= name values+= test NEWLINE )+
                    cnt12 = 0
                    while True:  # loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if LA12_0 in {ID, UNDERSCORE}:
                            alt12 = 1

                        if alt12 == 1:
                            # YarcParser.g:40:50: params+= name values+= test NEWLINE
                            self._state.following.append(
                                self.FOLLOW_name_in_edit_stmt436
                            )
                            params = self.name()

                            self._state.following.pop()
                            if list_params is None:
                                list_params = []
                            list_params.append(params.st)

                            self._state.following.append(
                                self.FOLLOW_test_in_edit_stmt440
                            )
                            values = self.test()

                            self._state.following.pop()
                            if list_values is None:
                                list_values = []
                            list_values.append(values.st)

                            self.match(
                                self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_stmt442
                            )

                        else:
                            if cnt12 >= 1:
                                break  # loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1

                    self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_stmt446)

                    # TEMPLATE REWRITE
                    # 40:93: -> edit_timeline(params=$paramsvalues=$values)
                    retval.st = self.templateLib.getInstanceOf(
                        "edit_timeline",
                        attributes={"params": list_params, "values": list_values},
                    )

                elif alt13 == 2:
                    # YarcParser.g:41:20: id= name edit_block[$id.st]
                    self._state.following.append(self.FOLLOW_name_in_edit_stmt484)
                    id = self.name()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_edit_block_in_edit_stmt486)
                    edit_block14 = self.edit_block(
                        ((id is not None) and [id.st] or [None])[0]
                    )

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 41:47: -> edit_stmt(id=$id.ststmts=self.handler.get_attrs(\"edit\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                    retval.st = self.templateLib.getInstanceOf(
                        "edit_stmt",
                        attributes={
                            "id": ((id is not None) and [id.st] or [None])[0],
                            "stmts": self.handler.get_attrs(
                                "edit",
                                (
                                    (edit_block14 is not None)
                                    and [edit_block14.attrs]
                                    or [None]
                                )[0],
                            ),
                            "behaviors": self.handler.get_behaviors(
                                (
                                    (edit_block14 is not None)
                                    and [edit_block14.attrs]
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
    # YarcParser.g:44:1: create_expr[id] : CREATE (count= test )? (prim= ( ( STEREO )? CAMERA | SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st))) ;
    def create_expr(self, id):
        retval = self.create_expr_return()
        retval.start = self.input.LT(1)

        prim = None
        count = None
        attrs = None
        file = None

        try:
            try:
                # YarcParser.g:44:16: ( CREATE (count= test )? (prim= ( ( STEREO )? CAMERA | SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st))) )
                # YarcParser.g:45:3: CREATE (count= test )? (prim= ( ( STEREO )? CAMERA | SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st)))
                self.match(self.input, CREATE, self.FOLLOW_CREATE_in_create_expr535)

                # YarcParser.g:45:15: (count= test )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if LA14_0 in {
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
                    alt14 = 1
                if alt14 == 1:
                    # YarcParser.g:45:15: count= test
                    self._state.following.append(self.FOLLOW_test_in_create_expr539)
                    count = self.test()

                    self._state.following.pop()

                # YarcParser.g:45:22: (prim= ( ( STEREO )? CAMERA | SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE ) -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| FROM file= test (attrs= edit_block[$id] | NEWLINE ) -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))| MATERIAL (attrs= simple_block | NEWLINE ) -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st)))
                alt20 = 3
                LA20 = self.input.LA(1)
                if LA20 in {CAMERA, LIGHT, SHAPE, STEREO}:
                    alt20 = 1
                elif LA20 in {FROM}:
                    alt20 = 2
                elif LA20 in {MATERIAL}:
                    alt20 = 3
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # YarcParser.g:46:5: prim= ( ( STEREO )? CAMERA | SHAPE | LIGHT ) (attrs= edit_block[$id] | NEWLINE )
                    pass
                    # YarcParser.g:46:10: ( ( STEREO )? CAMERA | SHAPE | LIGHT )
                    alt16 = 3
                    LA16 = self.input.LA(1)
                    if LA16 in {CAMERA, STEREO}:
                        alt16 = 1
                    elif LA16 in {SHAPE}:
                        alt16 = 2
                    elif LA16 in {LIGHT}:
                        alt16 = 3
                    else:
                        nvae = NoViableAltException("", 16, 0, self.input)

                        raise nvae

                    if alt16 == 1:
                        # YarcParser.g:46:11: ( STEREO )? CAMERA
                        pass
                        # YarcParser.g:46:11: ( STEREO )?
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if LA15_0 == STEREO:
                            alt15 = 1
                        if alt15 == 1:
                            # YarcParser.g:46:11: STEREO
                            prim = self.match(
                                self.input, STEREO, self.FOLLOW_STEREO_in_create_expr551
                            )

                        prim = self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_create_expr554
                        )

                    elif alt16 == 2:
                        # YarcParser.g:46:28: SHAPE
                        prim = self.match(
                            self.input, SHAPE, self.FOLLOW_SHAPE_in_create_expr558
                        )

                    elif alt16 == 3:
                        # YarcParser.g:46:36: LIGHT
                        prim = self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_create_expr562
                        )

                    # YarcParser.g:46:43: (attrs= edit_block[$id] | NEWLINE )
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
                        # YarcParser.g:46:44: attrs= edit_block[$id]
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr568
                        )
                        attrs = self.edit_block(id)

                        self._state.following.pop()

                    elif alt17 == 2:
                        # YarcParser.g:46:68: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr573
                        )

                    # TEMPLATE REWRITE
                    # 47:7: -> create_prim(id=$idprim=self.handler.map($prim)params=self.handler.get_params($prim, $attrs.attrs, $count.st)stmts=self.handler.get_attrs($prim, $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))
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

                elif alt20 == 2:
                    # YarcParser.g:52:7: FROM file= test (attrs= edit_block[$id] | NEWLINE )
                    self.match(self.input, FROM, self.FOLLOW_FROM_in_create_expr706)

                    self._state.following.append(self.FOLLOW_test_in_create_expr710)
                    file = self.test()

                    self._state.following.pop()

                    # YarcParser.g:52:22: (attrs= edit_block[$id] | NEWLINE )
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
                        # YarcParser.g:52:23: attrs= edit_block[$id]
                        self._state.following.append(
                            self.FOLLOW_edit_block_in_create_expr715
                        )
                        attrs = self.edit_block(id)

                        self._state.following.pop()

                    elif alt18 == 2:
                        # YarcParser.g:52:47: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr720
                        )

                    # TEMPLATE REWRITE
                    # 53:7: -> create_from(id=$idfile=$file.stparams=self.handler.get_params(\"from_file\", $attrs.attrs, $count.st)stmts=self.handler.get_attrs(\"from_file\", $attrs.attrs)behaviors=self.handler.get_behaviors($attrs.attrs))
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

                elif alt20 == 3:
                    # YarcParser.g:58:7: MATERIAL (attrs= simple_block | NEWLINE )
                    self.match(
                        self.input, MATERIAL, self.FOLLOW_MATERIAL_in_create_expr852
                    )

                    # YarcParser.g:58:16: (attrs= simple_block | NEWLINE )
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
                        # YarcParser.g:58:17: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_create_expr857
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt19 == 2:
                        # YarcParser.g:58:38: NEWLINE
                        self.match(
                            self.input, NEWLINE, self.FOLLOW_NEWLINE_in_create_expr861
                        )

                    # TEMPLATE REWRITE
                    # 59:7: -> create_material(id=$idparams=self.handler.get_params(\"material\", $attrs.attrs, $count.st))
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
    # YarcParser.g:64:1: instantiate_expr[id] : INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE ) -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params(\"instantiate\", $edit_block.attrs, $count.st)stmts=self.handler.get_attrs(\"instantiate\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs));
    def instantiate_expr(self, id):
        retval = self.instantiate_expr_return()
        retval.start = self.input.LT(1)

        count = None
        file = None
        edit_block15 = None

        try:
            try:
                # YarcParser.g:64:22: ( INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE ) -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params(\"instantiate\", $edit_block.attrs, $count.st)stmts=self.handler.get_attrs(\"instantiate\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                # YarcParser.g:64:24: INSTANTIATE count= ( test )? FROM file= test ( edit_block[$id] | NEWLINE )
                self.match(
                    self.input,
                    INSTANTIATE,
                    self.FOLLOW_INSTANTIATE_in_instantiate_expr923,
                )

                # YarcParser.g:64:42: ( test )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if LA21_0 in {
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
                    alt21 = 1
                if alt21 == 1:
                    # YarcParser.g:64:43: test
                    self._state.following.append(
                        self.FOLLOW_test_in_instantiate_expr928
                    )
                    count = self.test()

                    self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_instantiate_expr932)

                self._state.following.append(self.FOLLOW_test_in_instantiate_expr936)
                file = self.test()

                self._state.following.pop()

                # YarcParser.g:64:65: ( edit_block[$id] | NEWLINE )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if LA22_0 == COLON:
                    alt22 = 1
                elif LA22_0 == NEWLINE:
                    alt22 = 2
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # YarcParser.g:64:66: edit_block[$id]
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_instantiate_expr939
                    )
                    edit_block15 = self.edit_block(id)

                    self._state.following.pop()

                elif alt22 == 2:
                    # YarcParser.g:64:84: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_instantiate_expr944
                    )

                # TEMPLATE REWRITE
                # 65:3: -> instantiate_expr(id=$idfile=$file.stparams=self.handler.get_params(\"instantiate\", $edit_block.attrs, $count.st)stmts=self.handler.get_attrs(\"instantiate\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                retval.st = self.templateLib.getInstanceOf(
                    "instantiate_expr",
                    attributes={
                        "id": id,
                        "file": ((file is not None) and [file.st] or [None])[0],
                        "params": self.handler.get_params(
                            "instantiate",
                            (
                                (edit_block15 is not None)
                                and [edit_block15.attrs]
                                or [None]
                            )[0],
                            count.st,
                        ),
                        "stmts": self.handler.get_attrs(
                            "instantiate",
                            (
                                (edit_block15 is not None)
                                and [edit_block15.attrs]
                                or [None]
                            )[0],
                        ),
                        "behaviors": self.handler.get_behaviors(
                            (
                                (edit_block15 is not None)
                                and [edit_block15.attrs]
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
    # YarcParser.g:70:1: group_expr[id] : GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE ) -> group_expr(id=$idnames=$namesparams=self.handler.get_params(\"group\", $edit_block.attrs)stmts=self.handler.get_attrs(\"group\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs));
    def group_expr(self, id):
        retval = self.group_expr_return()
        retval.start = self.input.LT(1)

        list_names = None
        edit_block16 = None
        names = None
        try:
            try:
                # YarcParser.g:70:22: ( GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE ) -> group_expr(id=$idnames=$namesparams=self.handler.get_params(\"group\", $edit_block.attrs)stmts=self.handler.get_attrs(\"group\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs)))
                # YarcParser.g:70:24: GROUP LBRACK names+= name ( COMMA names+= name )* RBRACK ( edit_block[$id] | NEWLINE )
                self.match(self.input, GROUP, self.FOLLOW_GROUP_in_group_expr1083)

                self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_group_expr1085)

                self._state.following.append(self.FOLLOW_name_in_group_expr1089)
                names = self.name()

                self._state.following.pop()
                if list_names is None:
                    list_names = []
                list_names.append(names.st)

                # YarcParser.g:70:49: ( COMMA names+= name )*
                while True:  # loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if LA23_0 == COMMA:
                        alt23 = 1

                    if alt23 == 1:
                        # YarcParser.g:70:50: COMMA names+= name
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_group_expr1092
                        )

                        self._state.following.append(self.FOLLOW_name_in_group_expr1096)
                        names = self.name()

                        self._state.following.pop()
                        if list_names is None:
                            list_names = []
                        list_names.append(names.st)

                    else:
                        break  # loop23

                self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_group_expr1100)

                # YarcParser.g:70:77: ( edit_block[$id] | NEWLINE )
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
                    # YarcParser.g:70:78: edit_block[$id]
                    self._state.following.append(
                        self.FOLLOW_edit_block_in_group_expr1103
                    )
                    edit_block16 = self.edit_block(id)

                    self._state.following.pop()

                elif alt24 == 2:
                    # YarcParser.g:70:96: NEWLINE
                    self.match(
                        self.input, NEWLINE, self.FOLLOW_NEWLINE_in_group_expr1108
                    )

                # TEMPLATE REWRITE
                # 71:3: -> group_expr(id=$idnames=$namesparams=self.handler.get_params(\"group\", $edit_block.attrs)stmts=self.handler.get_attrs(\"group\", $edit_block.attrs)behaviors=self.handler.get_behaviors($edit_block.attrs))
                retval.st = self.templateLib.getInstanceOf(
                    "group_expr",
                    attributes={
                        "id": id,
                        "names": list_names,
                        "params": self.handler.get_params(
                            "group",
                            (
                                (edit_block16 is not None)
                                and [edit_block16.attrs]
                                or [None]
                            )[0],
                        ),
                        "stmts": self.handler.get_attrs(
                            "group",
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
    # YarcParser.g:76:1: get_expr[id] : GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE ) -> get_expr(id=$idfilter=$filter.stpath=$path.stparams=self.handler.get_params(\"get\", $simple_block.attrs));
    def get_expr(self, id):
        retval = self.get_expr_return()
        retval.start = self.input.LT(1)

        filter = None
        path = None
        simple_block17 = None

        try:
            try:
                # YarcParser.g:76:22: ( GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE ) -> get_expr(id=$idfilter=$filter.stpath=$path.stparams=self.handler.get_params(\"get\", $simple_block.attrs)))
                # YarcParser.g:76:24: GET (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )? path= test ( simple_block | NEWLINE )
                self.match(self.input, GET, self.FOLLOW_GET_in_get_expr1222)

                # YarcParser.g:76:28: (filter= ( CAMERA | LIGHT | MATERIAL | name ) AT )?
                alt26 = 2
                LA26 = self.input.LA(1)
                if LA26 in {CAMERA, LIGHT, MATERIAL}:
                    alt26 = 1
                elif LA26 in {ID}:
                    LA26_2 = self.input.LA(2)

                    if LA26_2 == AT:
                        alt26 = 1
                elif LA26 in {UNDERSCORE}:
                    LA26_3 = self.input.LA(2)

                    if LA26_3 == AT:
                        alt26 = 1
                if alt26 == 1:
                    # YarcParser.g:76:29: filter= ( CAMERA | LIGHT | MATERIAL | name ) AT
                    pass
                    # YarcParser.g:76:36: ( CAMERA | LIGHT | MATERIAL | name )
                    alt25 = 4
                    LA25 = self.input.LA(1)
                    if LA25 in {CAMERA}:
                        alt25 = 1
                    elif LA25 in {LIGHT}:
                        alt25 = 2
                    elif LA25 in {MATERIAL}:
                        alt25 = 3
                    elif LA25 in {ID, UNDERSCORE}:
                        alt25 = 4
                    else:
                        nvae = NoViableAltException("", 25, 0, self.input)

                        raise nvae

                    if alt25 == 1:
                        # YarcParser.g:76:37: CAMERA
                        filter = self.match(
                            self.input, CAMERA, self.FOLLOW_CAMERA_in_get_expr1228
                        )

                    elif alt25 == 2:
                        # YarcParser.g:76:46: LIGHT
                        filter = self.match(
                            self.input, LIGHT, self.FOLLOW_LIGHT_in_get_expr1232
                        )

                    elif alt25 == 3:
                        # YarcParser.g:76:54: MATERIAL
                        filter = self.match(
                            self.input, MATERIAL, self.FOLLOW_MATERIAL_in_get_expr1236
                        )

                    elif alt25 == 4:
                        # YarcParser.g:76:65: name
                        self._state.following.append(self.FOLLOW_name_in_get_expr1240)
                        filter = self.name()

                        self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_get_expr1243)

                self._state.following.append(self.FOLLOW_test_in_get_expr1249)
                path = self.test()

                self._state.following.pop()

                # YarcParser.g:76:86: ( simple_block | NEWLINE )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if LA27_0 == COLON:
                    alt27 = 1
                elif LA27_0 == NEWLINE:
                    alt27 = 2
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # YarcParser.g:76:87: simple_block
                    self._state.following.append(
                        self.FOLLOW_simple_block_in_get_expr1252
                    )
                    simple_block17 = self.simple_block()

                    self._state.following.pop()

                elif alt27 == 2:
                    # YarcParser.g:76:102: NEWLINE
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_get_expr1256)

                # TEMPLATE REWRITE
                # 77:3: -> get_expr(id=$idfilter=$filter.stpath=$path.stparams=self.handler.get_params(\"get\", $simple_block.attrs))
                retval.st = self.templateLib.getInstanceOf(
                    "get_expr",
                    attributes={
                        "id": id,
                        "filter": filter.st,
                        "path": ((path is not None) and [path.st] or [None])[0],
                        "params": self.handler.get_params(
                            "get",
                            (
                                (simple_block17 is not None)
                                and [simple_block17.attrs]
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
    # YarcParser.g:82:1: edit_block[id] returns [attrs] : COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT ;
    def edit_block(self, id):
        retval = self.edit_block_return()
        retval.start = self.input.LT(1)

        stmt_ = None

        retval.attrs = []
        try:
            try:
                # YarcParser.g:84:3: ( COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT )
                # YarcParser.g:84:5: COLON NEWLINE INDENT (stmt_= ( attr | inner_behavior_stmt[$id] ) )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_edit_block1348)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_edit_block1350)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_edit_block1352)

                # YarcParser.g:84:26: (stmt_= ( attr | inner_behavior_stmt[$id] ) )+
                cnt29 = 0
                while True:  # loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if LA29_0 in {
                        EVERY,
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
                        alt29 = 1

                    if alt29 == 1:
                        # YarcParser.g:84:27: stmt_= ( attr | inner_behavior_stmt[$id] )
                        pass
                        # YarcParser.g:84:33: ( attr | inner_behavior_stmt[$id] )
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if LA28_0 in {
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
                            alt28 = 1
                        elif LA28_0 == EVERY:
                            alt28 = 2
                        else:
                            nvae = NoViableAltException("", 28, 0, self.input)

                            raise nvae

                        if alt28 == 1:
                            # YarcParser.g:84:34: attr
                            self._state.following.append(
                                self.FOLLOW_attr_in_edit_block1358
                            )
                            stmt_ = self.attr()

                            self._state.following.pop()

                        elif alt28 == 2:
                            # YarcParser.g:84:41: inner_behavior_stmt[$id]
                            self._state.following.append(
                                self.FOLLOW_inner_behavior_stmt_in_edit_block1362
                            )
                            stmt_ = self.inner_behavior_stmt(id)

                            self._state.following.pop()

                        # action start
                        retval.attrs.append(stmt_.attr)
                        # action end

                    else:
                        if cnt29 >= 1:
                            break  # loop29

                        eee = EarlyExitException(29, self.input)
                        raise eee

                    cnt29 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_edit_block1370)

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
    # YarcParser.g:85:1: simple_block returns [attrs] : COLON NEWLINE INDENT ( simple_attr )+ DEDENT ;
    def simple_block(
        self,
    ):
        retval = self.simple_block_return()
        retval.start = self.input.LT(1)

        simple_attr18 = None

        retval.attrs = []
        try:
            try:
                # YarcParser.g:87:3: ( COLON NEWLINE INDENT ( simple_attr )+ DEDENT )
                # YarcParser.g:87:5: COLON NEWLINE INDENT ( simple_attr )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_block1389)

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_block1391)

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_simple_block1393)

                # YarcParser.g:87:26: ( simple_attr )+
                cnt30 = 0
                while True:  # loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if LA30_0 in {ID, UNDERSCORE}:
                        alt30 = 1

                    if alt30 == 1:
                        # YarcParser.g:87:27: simple_attr
                        self._state.following.append(
                            self.FOLLOW_simple_attr_in_simple_block1396
                        )
                        simple_attr18 = self.simple_attr()

                        self._state.following.pop()

                        # action start
                        retval.attrs.append(
                            (
                                (simple_attr18 is not None)
                                and [simple_attr18.attr]
                                or [None]
                            )[0]
                        )
                        # action end

                    else:
                        if cnt30 >= 1:
                            break  # loop30

                        eee = EarlyExitException(30, self.input)
                        raise eee

                    cnt30 += 1

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_simple_block1402)

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
    # YarcParser.g:89:1: attr returns [attr] : a= ( core_attr | simple_attr | compound_attr ) -> {$a.st};
    def attr(
        self,
    ):
        retval = self.attr_return()
        retval.start = self.input.LT(1)

        a = None

        try:
            try:
                # YarcParser.g:89:21: (a= ( core_attr | simple_attr | compound_attr ) -> {$a.st})
                # YarcParser.g:89:23: a= ( core_attr | simple_attr | compound_attr )
                pass
                # YarcParser.g:89:25: ( core_attr | simple_attr | compound_attr )
                alt31 = 3
                LA31 = self.input.LA(1)
                if LA31 in {
                    LOOK_AT,
                    ROTATE,
                    SCALE,
                    SEMANTICS,
                    SIZE,
                    TRANSLATE,
                    UP_AXIS,
                    VISIBLE,
                }:
                    alt31 = 1
                elif LA31 in {ID, UNDERSCORE}:
                    alt31 = 2
                elif LA31 in {PHYSICS, ROT_AROUND, SCATTER}:
                    alt31 = 3
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # YarcParser.g:89:26: core_attr
                    self._state.following.append(self.FOLLOW_core_attr_in_attr1417)
                    a = self.core_attr()

                    self._state.following.pop()

                elif alt31 == 2:
                    # YarcParser.g:89:38: simple_attr
                    self._state.following.append(self.FOLLOW_simple_attr_in_attr1421)
                    a = self.simple_attr()

                    self._state.following.pop()

                elif alt31 == 3:
                    # YarcParser.g:89:52: compound_attr
                    self._state.following.append(self.FOLLOW_compound_attr_in_attr1425)
                    a = self.compound_attr()

                    self._state.following.pop()

                # action start
                retval.attr = a.attr
                # action end

                # TEMPLATE REWRITE
                # 89:83: -> {$a.st}
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
    # YarcParser.g:90:1: simple_attr returns [attr] : name_= name ( COLON type= name )? value= test NEWLINE -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st);
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
                # YarcParser.g:92:3: (name_= name ( COLON type= name )? value= test NEWLINE -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st))
                # YarcParser.g:92:5: name_= name ( COLON type= name )? value= test NEWLINE
                self._state.following.append(self.FOLLOW_name_in_simple_attr1455)
                name_ = self.name()

                self._state.following.pop()

                # YarcParser.g:92:16: ( COLON type= name )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if LA32_0 == COLON:
                    alt32 = 1
                if alt32 == 1:
                    # YarcParser.g:92:17: COLON type= name
                    self.match(self.input, COLON, self.FOLLOW_COLON_in_simple_attr1458)

                    self._state.following.append(self.FOLLOW_name_in_simple_attr1462)
                    type = self.name()

                    self._state.following.pop()

                self._state.following.append(self.FOLLOW_test_in_simple_attr1468)
                value = self.test()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_simple_attr1470)

                # TEMPLATE REWRITE
                # 93:3: -> simple_attr(name=$name_.sttype=$type.stvalue=$value.st)
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
    # YarcParser.g:95:1: compound_attr returns [attr] : (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs))) ;
    def compound_attr(
        self,
    ):
        retval = self.compound_attr_return()
        retval.start = self.input.LT(1)

        name_ = None
        surface = None
        attrs = None
        center = None

        try:
            try:
                # YarcParser.g:97:3: ( (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs))) )
                # YarcParser.g:97:5: (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs)))
                pass
                # YarcParser.g:97:5: (name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE ) -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE ) -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))|name_= PHYSICS (attrs= simple_block | NEWLINE ) -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs)))
                alt36 = 3
                LA36 = self.input.LA(1)
                if LA36 in {SCATTER}:
                    alt36 = 1
                elif LA36 in {ROT_AROUND}:
                    alt36 = 2
                elif LA36 in {PHYSICS}:
                    alt36 = 3
                else:
                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae

                if alt36 == 1:
                    # YarcParser.g:97:7: name_= SCATTER ON surface= name (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input, SCATTER, self.FOLLOW_SCATTER_in_compound_attr1517
                    )

                    self.match(self.input, ON, self.FOLLOW_ON_in_compound_attr1519)

                    self._state.following.append(self.FOLLOW_name_in_compound_attr1523)
                    surface = self.name()

                    self._state.following.pop()

                    # YarcParser.g:97:37: (attrs= simple_block | NEWLINE )
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if LA33_0 == COLON:
                        alt33 = 1
                    elif LA33_0 == NEWLINE:
                        alt33 = 2
                    else:
                        nvae = NoViableAltException("", 33, 0, self.input)

                        raise nvae

                    if alt33 == 1:
                        # YarcParser.g:97:38: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr1528
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt33 == 2:
                        # YarcParser.g:97:59: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr1532,
                        )

                    # TEMPLATE REWRITE
                    # 98:7: -> scatter_expr(scatter_type=self.handler.map($name_)surface=$surface.stparams=self.handler.get_params($name_, $attrs.attrs))
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

                elif alt36 == 2:
                    # YarcParser.g:101:7: name_= ROT_AROUND center= name (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input,
                        ROT_AROUND,
                        self.FOLLOW_ROT_AROUND_in_compound_attr1616,
                    )

                    self._state.following.append(self.FOLLOW_name_in_compound_attr1620)
                    center = self.name()

                    self._state.following.pop()

                    # YarcParser.g:101:36: (attrs= simple_block | NEWLINE )
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if LA34_0 == COLON:
                        alt34 = 1
                    elif LA34_0 == NEWLINE:
                        alt34 = 2
                    else:
                        nvae = NoViableAltException("", 34, 0, self.input)

                        raise nvae

                    if alt34 == 1:
                        # YarcParser.g:101:37: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr1625
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt34 == 2:
                        # YarcParser.g:101:58: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr1629,
                        )

                    # TEMPLATE REWRITE
                    # 102:7: -> rot_around_expr(center=$center.stparams=self.handler.get_params($name_, $attrs.attrs))
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

                elif alt36 == 3:
                    # YarcParser.g:104:7: name_= PHYSICS (attrs= simple_block | NEWLINE )
                    name_ = self.match(
                        self.input, PHYSICS, self.FOLLOW_PHYSICS_in_compound_attr1686
                    )

                    # YarcParser.g:104:21: (attrs= simple_block | NEWLINE )
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
                        # YarcParser.g:104:22: attrs= simple_block
                        self._state.following.append(
                            self.FOLLOW_simple_block_in_compound_attr1691
                        )
                        attrs = self.simple_block()

                        self._state.following.pop()

                    elif alt35 == 2:
                        # YarcParser.g:104:43: NEWLINE
                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_compound_attr1695,
                        )

                    # TEMPLATE REWRITE
                    # 105:7: -> physics_expr(physics_attr=self.handler.map($name_)params=self.handler.get_params($name_, $attrs.attrs))
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
    # YarcParser.g:109:1: core_attr returns [attr] : ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test ( ORDER )? -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)) NEWLINE ;
    def core_attr(
        self,
    ):
        retval = self.core_attr_return()
        retval.start = self.input.LT(1)

        axis = None
        TRANSLATE19 = None
        ROTATE20 = None
        SCALE21 = None
        LOOK_AT22 = None
        UP_AXIS23 = None
        SIZE24 = None
        SEMANTICS25 = None
        VISIBLE26 = None
        value = None

        try:
            try:
                # YarcParser.g:111:3: ( ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test ( ORDER )? -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)) NEWLINE )
                # YarcParser.g:111:5: ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test ( ORDER )? -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st)) NEWLINE
                pass
                # YarcParser.g:111:5: ( TRANSLATE (axis= AXIS )? TO value= test -> translate_expr(type=namevalue=$value.st)| ROTATE (axis= AXIS )? value= test ( ORDER )? -> rotate_expr(type=namevalue=$value.st)| SCALE value= test -> scale_expr(value=$value.st)| LOOK_AT value= test -> look_at_expr(value=$value.st)| UP_AXIS value= test -> look_at_up_axis_expr(value=$value.st)| SIZE value= test -> size_expr(value=$value.st)| SEMANTICS value= test -> semantics_expr(value=$value.st)| VISIBLE value= test -> visible_expr(value=$value.st))
                alt40 = 8
                LA40 = self.input.LA(1)
                if LA40 in {TRANSLATE}:
                    alt40 = 1
                elif LA40 in {ROTATE}:
                    alt40 = 2
                elif LA40 in {SCALE}:
                    alt40 = 3
                elif LA40 in {LOOK_AT}:
                    alt40 = 4
                elif LA40 in {UP_AXIS}:
                    alt40 = 5
                elif LA40 in {SIZE}:
                    alt40 = 6
                elif LA40 in {SEMANTICS}:
                    alt40 = 7
                elif LA40 in {VISIBLE}:
                    alt40 = 8
                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae

                if alt40 == 1:
                    # YarcParser.g:111:7: TRANSLATE (axis= AXIS )? TO value= test
                    TRANSLATE19 = self.match(
                        self.input, TRANSLATE, self.FOLLOW_TRANSLATE_in_core_attr1766
                    )

                    # YarcParser.g:111:21: (axis= AXIS )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if LA37_0 == AXIS:
                        alt37 = 1
                    if alt37 == 1:
                        # YarcParser.g:111:21: axis= AXIS
                        axis = self.match(
                            self.input, AXIS, self.FOLLOW_AXIS_in_core_attr1770
                        )

                    self.match(self.input, TO, self.FOLLOW_TO_in_core_attr1773)

                    self._state.following.append(self.FOLLOW_test_in_core_attr1777)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(TRANSLATE19, axis)
                    # action end

                    # TEMPLATE REWRITE
                    # 111:87: -> translate_expr(type=namevalue=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "translate_expr",
                        attributes={
                            "type": name,
                            "value": ((value is not None) and [value.st] or [None])[0],
                        },
                    )

                elif alt40 == 2:
                    # YarcParser.g:112:7: ROTATE (axis= AXIS )? value= test ( ORDER )?
                    ROTATE20 = self.match(
                        self.input, ROTATE, self.FOLLOW_ROTATE_in_core_attr1801
                    )

                    # YarcParser.g:112:18: (axis= AXIS )?
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if LA38_0 == AXIS:
                        alt38 = 1
                    if alt38 == 1:
                        # YarcParser.g:112:18: axis= AXIS
                        axis = self.match(
                            self.input, AXIS, self.FOLLOW_AXIS_in_core_attr1805
                        )

                    self._state.following.append(self.FOLLOW_test_in_core_attr1810)
                    value = self.test()

                    self._state.following.pop()

                    # YarcParser.g:112:36: ( ORDER )?
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if LA39_0 == ORDER:
                        alt39 = 1
                    if alt39 == 1:
                        # YarcParser.g:112:36: ORDER
                        self.match(
                            self.input, ORDER, self.FOLLOW_ORDER_in_core_attr1812
                        )

                    # action start
                    name = self.handler.map(ROTATE20, axis)
                    # action end

                    # TEMPLATE REWRITE
                    # 112:85: -> rotate_expr(type=namevalue=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "rotate_expr",
                        attributes={
                            "type": name,
                            "value": ((value is not None) and [value.st] or [None])[0],
                        },
                    )

                elif alt40 == 3:
                    # YarcParser.g:113:7: SCALE value= test
                    SCALE21 = self.match(
                        self.input, SCALE, self.FOLLOW_SCALE_in_core_attr1837
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr1841)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SCALE21)
                    # action end

                    # TEMPLATE REWRITE
                    # 113:58: -> scale_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "scale_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt40 == 4:
                    # YarcParser.g:114:7: LOOK_AT value= test
                    LOOK_AT22 = self.match(
                        self.input, LOOK_AT, self.FOLLOW_LOOK_AT_in_core_attr1860
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr1864)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(LOOK_AT22)
                    # action end

                    # TEMPLATE REWRITE
                    # 114:62: -> look_at_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "look_at_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt40 == 5:
                    # YarcParser.g:115:7: UP_AXIS value= test
                    UP_AXIS23 = self.match(
                        self.input, UP_AXIS, self.FOLLOW_UP_AXIS_in_core_attr1883
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr1887)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(UP_AXIS23)
                    # action end

                    # TEMPLATE REWRITE
                    # 115:62: -> look_at_up_axis_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "look_at_up_axis_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt40 == 6:
                    # YarcParser.g:116:7: SIZE value= test
                    SIZE24 = self.match(
                        self.input, SIZE, self.FOLLOW_SIZE_in_core_attr1906
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr1910)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SIZE24)
                    # action end

                    # TEMPLATE REWRITE
                    # 116:56: -> size_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "size_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt40 == 7:
                    # YarcParser.g:117:7: SEMANTICS value= test
                    SEMANTICS25 = self.match(
                        self.input, SEMANTICS, self.FOLLOW_SEMANTICS_in_core_attr1929
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr1933)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(SEMANTICS25)
                    # action end

                    # TEMPLATE REWRITE
                    # 117:66: -> semantics_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "semantics_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                elif alt40 == 8:
                    # YarcParser.g:118:7: VISIBLE value= test
                    VISIBLE26 = self.match(
                        self.input, VISIBLE, self.FOLLOW_VISIBLE_in_core_attr1952
                    )

                    self._state.following.append(self.FOLLOW_test_in_core_attr1956)
                    value = self.test()

                    self._state.following.pop()

                    # action start
                    name = self.handler.map(VISIBLE26)
                    # action end

                    # TEMPLATE REWRITE
                    # 118:62: -> visible_expr(value=$value.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "visible_expr",
                        attributes={
                            "value": ((value is not None) and [value.st] or [None])[0]
                        },
                    )

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_core_attr1973)

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
    # YarcParser.g:121:1: inner_behavior_stmt[id] returns [attr] : behavior_expr inner_behavior_block -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st);
    def inner_behavior_stmt(self, id):
        retval = self.inner_behavior_stmt_return()
        retval.start = self.input.LT(1)

        behavior_expr27 = None
        inner_behavior_block28 = None

        try:
            try:
                # YarcParser.g:123:3: ( behavior_expr inner_behavior_block -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st))
                # YarcParser.g:123:5: behavior_expr inner_behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_inner_behavior_stmt1996
                )
                behavior_expr27 = self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_inner_behavior_block_in_inner_behavior_stmt1998
                )
                inner_behavior_block28 = self.inner_behavior_block()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 123:40: -> inner_behavior_stmt(behavior=$behavior_expr.stid=$idblock=$inner_behavior_block.st)
                retval.st = self.templateLib.getInstanceOf(
                    "inner_behavior_stmt",
                    attributes={
                        "behavior": (
                            (behavior_expr27 is not None)
                            and [behavior_expr27.st]
                            or [None]
                        )[0],
                        "id": id,
                        "block": (
                            (inner_behavior_block28 is not None)
                            and [inner_behavior_block28.st]
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
    # YarcParser.g:124:1: inner_behavior_block : COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT -> behavior_block(stmts=$stmts_);
    def inner_behavior_block(
        self,
    ):
        retval = self.inner_behavior_block_return()
        retval.start = self.input.LT(1)

        list_stmts_ = None
        stmts_ = None
        try:
            try:
                # YarcParser.g:124:22: ( COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT -> behavior_block(stmts=$stmts_))
                # YarcParser.g:124:24: COLON NEWLINE INDENT (stmts_+= attr )+ DEDENT
                self.match(
                    self.input, COLON, self.FOLLOW_COLON_in_inner_behavior_block2024
                )

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_inner_behavior_block2026
                )

                self.match(
                    self.input, INDENT, self.FOLLOW_INDENT_in_inner_behavior_block2028
                )

                # YarcParser.g:124:51: (stmts_+= attr )+
                cnt41 = 0
                while True:  # loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if LA41_0 in {
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
                        alt41 = 1

                    if alt41 == 1:
                        # YarcParser.g:124:51: stmts_+= attr
                        self._state.following.append(
                            self.FOLLOW_attr_in_inner_behavior_block2032
                        )
                        stmts_ = self.attr()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    else:
                        if cnt41 >= 1:
                            break  # loop41

                        eee = EarlyExitException(41, self.input)
                        raise eee

                    cnt41 += 1

                self.match(
                    self.input, DEDENT, self.FOLLOW_DEDENT_in_inner_behavior_block2035
                )

                # TEMPLATE REWRITE
                # 124:66: -> behavior_block(stmts=$stmts_)
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
    # YarcParser.g:127:1: behavior_stmt : behavior_expr behavior_block -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st);
    def behavior_stmt(
        self,
    ):
        retval = self.behavior_stmt_return()
        retval.start = self.input.LT(1)

        behavior_expr29 = None
        behavior_block30 = None

        try:
            try:
                # YarcParser.g:127:16: ( behavior_expr behavior_block -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st))
                # YarcParser.g:127:18: behavior_expr behavior_block
                self._state.following.append(
                    self.FOLLOW_behavior_expr_in_behavior_stmt2055
                )
                behavior_expr29 = self.behavior_expr()

                self._state.following.pop()

                self._state.following.append(
                    self.FOLLOW_behavior_block_in_behavior_stmt2057
                )
                behavior_block30 = self.behavior_block()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 127:47: -> behavior_stmt(behavior=$behavior_expr.stblock=$behavior_block.st)
                retval.st = self.templateLib.getInstanceOf(
                    "behavior_stmt",
                    attributes={
                        "behavior": (
                            (behavior_expr29 is not None)
                            and [behavior_expr29.st]
                            or [None]
                        )[0],
                        "block": (
                            (behavior_block30 is not None)
                            and [behavior_block30.st]
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
    # YarcParser.g:128:1: behavior_expr : EVERY (interval= test )? type= ( FRAMES | TIME ) -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type));
    def behavior_expr(
        self,
    ):
        retval = self.behavior_expr_return()
        retval.start = self.input.LT(1)

        type = None
        interval = None

        try:
            try:
                # YarcParser.g:128:16: ( EVERY (interval= test )? type= ( FRAMES | TIME ) -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type)))
                # YarcParser.g:128:18: EVERY (interval= test )? type= ( FRAMES | TIME )
                self.match(self.input, EVERY, self.FOLLOW_EVERY_in_behavior_expr2079)

                # YarcParser.g:128:32: (interval= test )?
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
                if alt42 == 1:
                    # YarcParser.g:128:32: interval= test
                    self._state.following.append(self.FOLLOW_test_in_behavior_expr2083)
                    interval = self.test()

                    self._state.following.pop()

                # YarcParser.g:128:44: ( FRAMES | TIME )
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if LA43_0 == FRAMES:
                    alt43 = 1
                elif LA43_0 == TIME:
                    alt43 = 2
                else:
                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # YarcParser.g:128:45: FRAMES
                    type = self.match(
                        self.input, FRAMES, self.FOLLOW_FRAMES_in_behavior_expr2089
                    )

                elif alt43 == 2:
                    # YarcParser.g:128:54: TIME
                    type = self.match(
                        self.input, TIME, self.FOLLOW_TIME_in_behavior_expr2093
                    )

                # TEMPLATE REWRITE
                # 128:60: -> behavior_expr(interval=$interval.stis_frame=self.handler.is_frame($type))
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
    # YarcParser.g:129:1: behavior_block : COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | edit_stmt )+ DEDENT -> behavior_block(stmts=$stmts_);
    def behavior_block(
        self,
    ):
        retval = self.behavior_block_return()
        retval.start = self.input.LT(1)

        stmts_ = None
        list_stmts_ = None

        try:
            try:
                # YarcParser.g:129:16: ( COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | edit_stmt )+ DEDENT -> behavior_block(stmts=$stmts_))
                # YarcParser.g:129:18: COLON NEWLINE INDENT stmts_+= ( aug_expr_stmt | edit_stmt )+ DEDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_behavior_block2115)

                self.match(
                    self.input, NEWLINE, self.FOLLOW_NEWLINE_in_behavior_block2117
                )

                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_behavior_block2119)

                # YarcParser.g:129:47: ( aug_expr_stmt | edit_stmt )+
                cnt44 = 0
                while True:  # loop44
                    alt44 = 3
                    LA44_0 = self.input.LA(1)

                    if LA44_0 in {
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
                        alt44 = 1
                    elif LA44_0 == EDIT:
                        alt44 = 2

                    if alt44 == 1:
                        # YarcParser.g:129:48: aug_expr_stmt
                        self._state.following.append(
                            self.FOLLOW_aug_expr_stmt_in_behavior_block2124
                        )
                        stmts_ = self.aug_expr_stmt()

                        self._state.following.pop()
                        if list_stmts_ is None:
                            list_stmts_ = []
                        list_stmts_.append(stmts_.st)

                    elif alt44 == 2:
                        # YarcParser.g:129:64: edit_stmt
                        self._state.following.append(
                            self.FOLLOW_edit_stmt_in_behavior_block2128
                        )
                        stmts_ = self.edit_stmt()

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

                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_behavior_block2132)

                # TEMPLATE REWRITE
                # 129:83: -> behavior_block(stmts=$stmts_)
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
    # YarcParser.g:132:1: expr_stmt : assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st);
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
                # YarcParser.g:132:11: (assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st))
                # YarcParser.g:132:13: assignable= testlist op= ( AUG_ASSIGN | ASSIGN ) value= ( testlist | fetch_expr ) NEWLINE
                self._state.following.append(self.FOLLOW_testlist_in_expr_stmt2153)
                assignable = self.testlist()

                self._state.following.pop()

                # YarcParser.g:132:36: ( AUG_ASSIGN | ASSIGN )
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if LA45_0 == AUG_ASSIGN:
                    alt45 = 1
                elif LA45_0 == ASSIGN:
                    alt45 = 2
                else:
                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae

                if alt45 == 1:
                    # YarcParser.g:132:37: AUG_ASSIGN
                    op = self.match(
                        self.input, AUG_ASSIGN, self.FOLLOW_AUG_ASSIGN_in_expr_stmt2158
                    )

                elif alt45 == 2:
                    # YarcParser.g:132:50: ASSIGN
                    op = self.match(
                        self.input, ASSIGN, self.FOLLOW_ASSIGN_in_expr_stmt2162
                    )

                # YarcParser.g:132:64: ( testlist | fetch_expr )
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if LA46_0 in {
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
                    alt46 = 1
                elif LA46_0 == FETCH:
                    alt46 = 2
                else:
                    nvae = NoViableAltException("", 46, 0, self.input)

                    raise nvae

                if alt46 == 1:
                    # YarcParser.g:132:65: testlist
                    self._state.following.append(self.FOLLOW_testlist_in_expr_stmt2168)
                    value = self.testlist()

                    self._state.following.pop()

                elif alt46 == 2:
                    # YarcParser.g:132:76: fetch_expr
                    self._state.following.append(
                        self.FOLLOW_fetch_expr_in_expr_stmt2172
                    )
                    value = self.fetch_expr()

                    self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expr_stmt2175)

                # TEMPLATE REWRITE
                # 133:3: -> expr_stmt(assignable=$assignable.stop=$op.textvalue=$value.st)
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
    # YarcParser.g:135:1: aug_expr_stmt : ( (id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) ) | model_expr[id] -> {$model_expr.st});
    def aug_expr_stmt(
        self,
    ):
        retval = self.aug_expr_stmt_return()
        retval.start = self.input.LT(1)

        op = None
        value = None
        id = None
        model_expr31 = None

        try:
            try:
                # YarcParser.g:135:14: ( (id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) ) | model_expr[id] -> {$model_expr.st})
                alt51 = 2
                LA51_0 = self.input.LA(1)

                if LA51_0 in {
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
                    alt51 = 1
                elif LA51_0 in {CREATE, GET, GROUP, INSTANTIATE}:
                    alt51 = 2
                else:
                    nvae = NoViableAltException("", 51, 0, self.input)

                    raise nvae

                if alt51 == 1:
                    # YarcParser.g:135:16: (id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) )
                    pass
                    # YarcParser.g:135:16: (id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) ) )
                    # YarcParser.g:136:5: id= testlist (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) )
                    self._state.following.append(
                        self.FOLLOW_testlist_in_aug_expr_stmt2213
                    )
                    id = self.testlist()

                    self._state.following.pop()

                    # YarcParser.g:136:17: (op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st}) )
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if LA50_0 == AUG_ASSIGN:
                        alt50 = 1
                    elif LA50_0 == ASSIGN:
                        alt50 = 2
                    else:
                        nvae = NoViableAltException("", 50, 0, self.input)

                        raise nvae

                    if alt50 == 1:
                        # YarcParser.g:137:7: op= AUG_ASSIGN value= ( testlist | fetch_expr ) NEWLINE
                        op = self.match(
                            self.input,
                            AUG_ASSIGN,
                            self.FOLLOW_AUG_ASSIGN_in_aug_expr_stmt2225,
                        )

                        # YarcParser.g:137:27: ( testlist | fetch_expr )
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if LA47_0 in {
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
                            alt47 = 1
                        elif LA47_0 == FETCH:
                            alt47 = 2
                        else:
                            nvae = NoViableAltException("", 47, 0, self.input)

                            raise nvae

                        if alt47 == 1:
                            # YarcParser.g:137:28: testlist
                            self._state.following.append(
                                self.FOLLOW_testlist_in_aug_expr_stmt2230
                            )
                            value = self.testlist()

                            self._state.following.pop()

                        elif alt47 == 2:
                            # YarcParser.g:137:39: fetch_expr
                            self._state.following.append(
                                self.FOLLOW_fetch_expr_in_aug_expr_stmt2234
                            )
                            value = self.fetch_expr()

                            self._state.following.pop()

                        self.match(
                            self.input,
                            NEWLINE,
                            self.FOLLOW_NEWLINE_in_aug_expr_stmt2237,
                        )

                        # TEMPLATE REWRITE
                        # 137:59: -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)
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

                    elif alt50 == 2:
                        # YarcParser.g:138:9: op= ASSIGN (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st})
                        op = self.match(
                            self.input, ASSIGN, self.FOLLOW_ASSIGN_in_aug_expr_stmt2269
                        )

                        # YarcParser.g:138:19: (value= ( testlist | fetch_expr ) NEWLINE -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)|value= ( model_expr[$id.st] ) -> {$value.st})
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if LA49_0 in {
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
                            alt49 = 1
                        elif LA49_0 in {CREATE, GET, GROUP, INSTANTIATE}:
                            alt49 = 2
                        else:
                            nvae = NoViableAltException("", 49, 0, self.input)

                            raise nvae

                        if alt49 == 1:
                            # YarcParser.g:139:9: value= ( testlist | fetch_expr ) NEWLINE
                            pass
                            # YarcParser.g:139:15: ( testlist | fetch_expr )
                            alt48 = 2
                            LA48_0 = self.input.LA(1)

                            if LA48_0 in {
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
                                alt48 = 1
                            elif LA48_0 == FETCH:
                                alt48 = 2
                            else:
                                nvae = NoViableAltException("", 48, 0, self.input)

                                raise nvae

                            if alt48 == 1:
                                # YarcParser.g:139:16: testlist
                                self._state.following.append(
                                    self.FOLLOW_testlist_in_aug_expr_stmt2284
                                )
                                value = self.testlist()

                                self._state.following.pop()

                            elif alt48 == 2:
                                # YarcParser.g:139:27: fetch_expr
                                self._state.following.append(
                                    self.FOLLOW_fetch_expr_in_aug_expr_stmt2288
                                )
                                value = self.fetch_expr()

                                self._state.following.pop()

                            self.match(
                                self.input,
                                NEWLINE,
                                self.FOLLOW_NEWLINE_in_aug_expr_stmt2291,
                            )

                            # TEMPLATE REWRITE
                            # 139:47: -> expr_stmt(assignable=$id.stop=$op.textvalue=$value.st)
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

                        elif alt49 == 2:
                            # YarcParser.g:140:11: value= ( model_expr[$id.st] )
                            pass
                            # YarcParser.g:140:17: ( model_expr[$id.st] )
                            # YarcParser.g:140:18: model_expr[$id.st]
                            self._state.following.append(
                                self.FOLLOW_model_expr_in_aug_expr_stmt2326
                            )
                            value = self.model_expr(
                                ((id is not None) and [id.st] or [None])[0]
                            )

                            self._state.following.pop()

                            # TEMPLATE REWRITE
                            # 140:38: -> {$value.st}
                            retval.st = value.st

                elif alt51 == 2:
                    # YarcParser.g:144:5: model_expr[id]
                    pass
                    # action start
                    id = self.handler.get_random_uid()
                    # action end

                    self._state.following.append(
                        self.FOLLOW_model_expr_in_aug_expr_stmt2360
                    )
                    model_expr31 = self.model_expr(id)

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 144:57: -> {$model_expr.st}
                    retval.st = (
                        (model_expr31 is not None) and [model_expr31.st] or [None]
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
    # YarcParser.g:147:1: model_expr[id] : expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] ) -> {expr_.st};
    def model_expr(self, id):
        retval = self.model_expr_return()
        retval.start = self.input.LT(1)

        expr_ = None

        try:
            try:
                # YarcParser.g:147:15: (expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] ) -> {expr_.st})
                # YarcParser.g:147:17: expr_= ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] )
                pass
                # YarcParser.g:147:23: ( create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id] )
                alt52 = 4
                LA52 = self.input.LA(1)
                if LA52 in {CREATE}:
                    alt52 = 1
                elif LA52 in {INSTANTIATE}:
                    alt52 = 2
                elif LA52 in {GET}:
                    alt52 = 3
                elif LA52 in {GROUP}:
                    alt52 = 4
                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # YarcParser.g:147:24: create_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_create_expr_in_model_expr2377
                    )
                    expr_ = self.create_expr(id)

                    self._state.following.pop()

                elif alt52 == 2:
                    # YarcParser.g:147:43: instantiate_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_instantiate_expr_in_model_expr2382
                    )
                    expr_ = self.instantiate_expr(id)

                    self._state.following.pop()

                elif alt52 == 3:
                    # YarcParser.g:147:67: get_expr[$id]
                    self._state.following.append(self.FOLLOW_get_expr_in_model_expr2387)
                    expr_ = self.get_expr(id)

                    self._state.following.pop()

                elif alt52 == 4:
                    # YarcParser.g:147:83: group_expr[$id]
                    self._state.following.append(
                        self.FOLLOW_group_expr_in_model_expr2392
                    )
                    expr_ = self.group_expr(id)

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 147:100: -> {expr_.st}
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
    # YarcParser.g:149:1: fetch_expr : FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )? -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE);
    def fetch_expr(
        self,
    ):
        retval = self.fetch_expr_return()
        retval.start = self.input.LT(1)

        RECURSIVE32 = None
        ext = None
        path = None
        filter = None
        limit = None

        try:
            try:
                # YarcParser.g:149:12: ( FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )? -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE))
                # YarcParser.g:149:14: FETCH ext= test FROM path= test ( MATCH filter= test )? ( LIMIT limit= test )? ( RECURSIVE )?
                self.match(self.input, FETCH, self.FOLLOW_FETCH_in_fetch_expr2406)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr2410)
                ext = self.test()

                self._state.following.pop()

                self.match(self.input, FROM, self.FOLLOW_FROM_in_fetch_expr2412)

                self._state.following.append(self.FOLLOW_test_in_fetch_expr2416)
                path = self.test()

                self._state.following.pop()

                # YarcParser.g:149:44: ( MATCH filter= test )?
                alt53 = 2
                LA53_0 = self.input.LA(1)

                if LA53_0 == MATCH:
                    alt53 = 1
                if alt53 == 1:
                    # YarcParser.g:149:45: MATCH filter= test
                    self.match(self.input, MATCH, self.FOLLOW_MATCH_in_fetch_expr2419)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr2423)
                    filter = self.test()

                    self._state.following.pop()

                # YarcParser.g:149:65: ( LIMIT limit= test )?
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if LA54_0 == LIMIT:
                    alt54 = 1
                if alt54 == 1:
                    # YarcParser.g:149:66: LIMIT limit= test
                    self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_fetch_expr2428)

                    self._state.following.append(self.FOLLOW_test_in_fetch_expr2432)
                    limit = self.test()

                    self._state.following.pop()

                # YarcParser.g:149:85: ( RECURSIVE )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if LA55_0 == RECURSIVE:
                    alt55 = 1
                if alt55 == 1:
                    # YarcParser.g:149:85: RECURSIVE
                    RECURSIVE32 = self.match(
                        self.input, RECURSIVE, self.FOLLOW_RECURSIVE_in_fetch_expr2436
                    )

                # TEMPLATE REWRITE
                # 150:3: -> fetch_expr(ext=$ext.stpath=$path.stfilter=$filter.stlimit=$limit.strecursive=$RECURSIVE)
                retval.st = self.templateLib.getInstanceOf(
                    "fetch_expr",
                    attributes={
                        "ext": ((ext is not None) and [ext.st] or [None])[0],
                        "path": ((path is not None) and [path.st] or [None])[0],
                        "filter": ((filter is not None) and [filter.st] or [None])[0],
                        "limit": ((limit is not None) and [limit.st] or [None])[0],
                        "recursive": RECURSIVE32,
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
    # YarcParser.g:153:1: test : expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st);
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
                # YarcParser.g:153:13: (expr_= or_test ( IF cond= or_test ELSE else_expr= test )? -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st))
                # YarcParser.g:153:15: expr_= or_test ( IF cond= or_test ELSE else_expr= test )?
                self._state.following.append(self.FOLLOW_or_test_in_test2487)
                expr_ = self.or_test()

                self._state.following.pop()

                # YarcParser.g:153:29: ( IF cond= or_test ELSE else_expr= test )?
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if LA56_0 == IF:
                    alt56 = 1
                if alt56 == 1:
                    # YarcParser.g:153:30: IF cond= or_test ELSE else_expr= test
                    self.match(self.input, IF, self.FOLLOW_IF_in_test2490)

                    self._state.following.append(self.FOLLOW_or_test_in_test2494)
                    cond = self.or_test()

                    self._state.following.pop()

                    self.match(self.input, ELSE, self.FOLLOW_ELSE_in_test2496)

                    self._state.following.append(self.FOLLOW_test_in_test2500)
                    else_expr = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 154:13: -> test(expr=$expr_.stcond=$cond.stelse_expr=$else_expr.st)
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
    # YarcParser.g:155:1: test_nocond : or_test -> test(expr=$or_test.st);
    def test_nocond(
        self,
    ):
        retval = self.test_nocond_return()
        retval.start = self.input.LT(1)

        or_test33 = None

        try:
            try:
                # YarcParser.g:155:13: ( or_test -> test(expr=$or_test.st))
                # YarcParser.g:155:15: or_test
                self._state.following.append(self.FOLLOW_or_test_in_test_nocond2542)
                or_test33 = self.or_test()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 155:23: -> test(expr=$or_test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "test",
                    attributes={
                        "expr": ((or_test33 is not None) and [or_test33.st] or [None])[
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
    # YarcParser.g:156:1: or_test :exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs);
    def or_test(
        self,
    ):
        retval = self.or_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:156:13: (exprs+= and_test ( OR exprs+= and_test )* -> or_test(exprs=$exprs))
                # YarcParser.g:156:15: exprs+= and_test ( OR exprs+= and_test )*
                self._state.following.append(self.FOLLOW_and_test_in_or_test2564)
                exprs = self.and_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:156:31: ( OR exprs+= and_test )*
                while True:  # loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if LA57_0 == OR:
                        alt57 = 1

                    if alt57 == 1:
                        # YarcParser.g:156:32: OR exprs+= and_test
                        self.match(self.input, OR, self.FOLLOW_OR_in_or_test2567)

                        self._state.following.append(
                            self.FOLLOW_and_test_in_or_test2571
                        )
                        exprs = self.and_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop57

                # TEMPLATE REWRITE
                # 156:53: -> or_test(exprs=$exprs)
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
    # YarcParser.g:157:1: and_test :exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs);
    def and_test(
        self,
    ):
        retval = self.and_test_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:157:13: (exprs+= not_test ( AND exprs+= not_test )* -> and_test(exprs=$exprs))
                # YarcParser.g:157:15: exprs+= not_test ( AND exprs+= not_test )*
                self._state.following.append(self.FOLLOW_not_test_in_and_test2594)
                exprs = self.not_test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:157:31: ( AND exprs+= not_test )*
                while True:  # loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if LA58_0 == AND:
                        alt58 = 1

                    if alt58 == 1:
                        # YarcParser.g:157:32: AND exprs+= not_test
                        self.match(self.input, AND, self.FOLLOW_AND_in_and_test2597)

                        self._state.following.append(
                            self.FOLLOW_not_test_in_and_test2601
                        )
                        exprs = self.not_test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop58

                # TEMPLATE REWRITE
                # 157:54: -> and_test(exprs=$exprs)
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
    # YarcParser.g:158:1: not_test : ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st});
    def not_test(
        self,
    ):
        retval = self.not_test_return()
        retval.start = self.input.LT(1)

        expr_ = None
        comparison34 = None

        try:
            try:
                # YarcParser.g:158:13: ( NOT expr_= not_test -> not_test(expr=$expr_.st)| comparison -> {$comparison.st})
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if LA59_0 == NOT:
                    alt59 = 1
                elif LA59_0 in {
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
                    alt59 = 2
                else:
                    nvae = NoViableAltException("", 59, 0, self.input)

                    raise nvae

                if alt59 == 1:
                    # YarcParser.g:158:15: NOT expr_= not_test
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_not_test2622)

                    self._state.following.append(self.FOLLOW_not_test_in_not_test2626)
                    expr_ = self.not_test()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 158:35: -> not_test(expr=$expr_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "not_test",
                        attributes={
                            "expr": ((expr_ is not None) and [expr_.st] or [None])[0]
                        },
                    )

                elif alt59 == 2:
                    # YarcParser.g:159:15: comparison
                    self._state.following.append(self.FOLLOW_comparison_in_not_test2652)
                    comparison34 = self.comparison()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 159:26: -> {$comparison.st}
                    retval.st = (
                        (comparison34 is not None) and [comparison34.st] or [None]
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
    # YarcParser.g:160:1: comparison :exprs+= expr ( comp_op exprs+= expr )* -> comparison(exprs=$exprsop=$comp_op.text);
    def comparison(
        self,
    ):
        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        comp_op35 = None
        exprs = None
        try:
            try:
                # YarcParser.g:160:13: (exprs+= expr ( comp_op exprs+= expr )* -> comparison(exprs=$exprsop=$comp_op.text))
                # YarcParser.g:160:15: exprs+= expr ( comp_op exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_comparison2666)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:160:27: ( comp_op exprs+= expr )*
                while True:  # loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if LA60_0 in {EQUALS, GT, GT_EQ, IN, IS, LT, LT_EQ, NOT, NOT_EQ}:
                        alt60 = 1

                    if alt60 == 1:
                        # YarcParser.g:160:28: comp_op exprs+= expr
                        self._state.following.append(
                            self.FOLLOW_comp_op_in_comparison2669
                        )
                        comp_op35 = self.comp_op()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_expr_in_comparison2673)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop60

                # TEMPLATE REWRITE
                # 160:50: -> comparison(exprs=$exprsop=$comp_op.text)
                retval.st = self.templateLib.getInstanceOf(
                    "comparison",
                    attributes={
                        "exprs": list_exprs,
                        "op": (
                            (comp_op35 is not None)
                            and [self.input.toString(comp_op35.start, comp_op35.stop)]
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
    # YarcParser.g:161:1: comp_op : ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT );
    def comp_op(
        self,
    ):
        retval = self.comp_op_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # YarcParser.g:161:13: ( LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT )
                alt61 = 10
                LA61 = self.input.LA(1)
                if LA61 in {LT}:
                    alt61 = 1
                elif LA61 in {GT}:
                    alt61 = 2
                elif LA61 in {EQUALS}:
                    alt61 = 3
                elif LA61 in {GT_EQ}:
                    alt61 = 4
                elif LA61 in {LT_EQ}:
                    alt61 = 5
                elif LA61 in {NOT_EQ}:
                    alt61 = 6
                elif LA61 in {IN}:
                    alt61 = 7
                elif LA61 in {NOT}:
                    alt61 = 8
                elif LA61 in {IS}:
                    LA61_9 = self.input.LA(2)

                    if LA61_9 == NOT:
                        alt61 = 10
                    elif LA61_9 in {
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
                        alt61 = 9
                    else:
                        nvae = NoViableAltException("", 61, 9, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 61, 0, self.input)

                    raise nvae

                if alt61 == 1:
                    # YarcParser.g:161:15: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_comp_op2700)

                elif alt61 == 2:
                    # YarcParser.g:161:20: GT
                    self.match(self.input, GT, self.FOLLOW_GT_in_comp_op2704)

                elif alt61 == 3:
                    # YarcParser.g:161:25: EQUALS
                    self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_comp_op2708)

                elif alt61 == 4:
                    # YarcParser.g:161:34: GT_EQ
                    self.match(self.input, GT_EQ, self.FOLLOW_GT_EQ_in_comp_op2712)

                elif alt61 == 5:
                    # YarcParser.g:161:42: LT_EQ
                    self.match(self.input, LT_EQ, self.FOLLOW_LT_EQ_in_comp_op2716)

                elif alt61 == 6:
                    # YarcParser.g:161:50: NOT_EQ
                    self.match(self.input, NOT_EQ, self.FOLLOW_NOT_EQ_in_comp_op2720)

                elif alt61 == 7:
                    # YarcParser.g:161:59: IN
                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op2724)

                elif alt61 == 8:
                    # YarcParser.g:161:64: NOT IN
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op2728)

                    self.match(self.input, IN, self.FOLLOW_IN_in_comp_op2730)

                elif alt61 == 9:
                    # YarcParser.g:161:73: IS
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op2734)

                elif alt61 == 10:
                    # YarcParser.g:161:78: IS NOT
                    self.match(self.input, IS, self.FOLLOW_IS_in_comp_op2738)

                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comp_op2740)

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
    # YarcParser.g:162:1: expr :exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs);
    def expr(
        self,
    ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:162:13: (exprs+= xor_expr ( BIT_OR exprs+= xor_expr )* -> expr(exprs=$exprs))
                # YarcParser.g:162:15: exprs+= xor_expr ( BIT_OR exprs+= xor_expr )*
                self._state.following.append(self.FOLLOW_xor_expr_in_expr2757)
                exprs = self.xor_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:162:31: ( BIT_OR exprs+= xor_expr )*
                while True:  # loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if LA62_0 == BIT_OR:
                        alt62 = 1

                    if alt62 == 1:
                        # YarcParser.g:162:32: BIT_OR exprs+= xor_expr
                        self.match(self.input, BIT_OR, self.FOLLOW_BIT_OR_in_expr2760)

                        self._state.following.append(self.FOLLOW_xor_expr_in_expr2764)
                        exprs = self.xor_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop62

                # TEMPLATE REWRITE
                # 162:57: -> expr(exprs=$exprs)
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
    # YarcParser.g:163:1: xor_expr :exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs);
    def xor_expr(
        self,
    ):
        retval = self.xor_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:163:13: (exprs+= and_expr ( XOR exprs+= and_expr )* -> xor_expr(exprs=$exprs))
                # YarcParser.g:163:15: exprs+= and_expr ( XOR exprs+= and_expr )*
                self._state.following.append(self.FOLLOW_and_expr_in_xor_expr2787)
                exprs = self.and_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:163:31: ( XOR exprs+= and_expr )*
                while True:  # loop63
                    alt63 = 2
                    LA63_0 = self.input.LA(1)

                    if LA63_0 == XOR:
                        alt63 = 1

                    if alt63 == 1:
                        # YarcParser.g:163:32: XOR exprs+= and_expr
                        self.match(self.input, XOR, self.FOLLOW_XOR_in_xor_expr2790)

                        self._state.following.append(
                            self.FOLLOW_and_expr_in_xor_expr2794
                        )
                        exprs = self.and_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop63

                # TEMPLATE REWRITE
                # 163:54: -> xor_expr(exprs=$exprs)
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
    # YarcParser.g:164:1: and_expr :exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs);
    def and_expr(
        self,
    ):
        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:164:13: (exprs+= shift_expr ( BIT_AND exprs+= shift_expr )* -> and_expr(exprs=$exprs))
                # YarcParser.g:164:15: exprs+= shift_expr ( BIT_AND exprs+= shift_expr )*
                self._state.following.append(self.FOLLOW_shift_expr_in_and_expr2817)
                exprs = self.shift_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:164:33: ( BIT_AND exprs+= shift_expr )*
                while True:  # loop64
                    alt64 = 2
                    LA64_0 = self.input.LA(1)

                    if LA64_0 == BIT_AND:
                        alt64 = 1

                    if alt64 == 1:
                        # YarcParser.g:164:34: BIT_AND exprs+= shift_expr
                        self.match(
                            self.input, BIT_AND, self.FOLLOW_BIT_AND_in_and_expr2820
                        )

                        self._state.following.append(
                            self.FOLLOW_shift_expr_in_and_expr2824
                        )
                        exprs = self.shift_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop64

                # TEMPLATE REWRITE
                # 164:62: -> and_expr(exprs=$exprs)
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
    # YarcParser.g:165:1: shift_expr :exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsop=$op);
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
                # YarcParser.g:165:13: (exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )* -> shift_expr(exprs=$exprsop=$op))
                # YarcParser.g:165:15: exprs+= arith_expr (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                self._state.following.append(self.FOLLOW_arith_expr_in_shift_expr2845)
                exprs = self.arith_expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:165:33: (op= ( LSHIFT | RSHIFT ) exprs+= arith_expr )*
                while True:  # loop66
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if LA66_0 in {LSHIFT, RSHIFT}:
                        alt66 = 1

                    if alt66 == 1:
                        # YarcParser.g:165:34: op= ( LSHIFT | RSHIFT ) exprs+= arith_expr
                        pass
                        # YarcParser.g:165:37: ( LSHIFT | RSHIFT )
                        alt65 = 2
                        LA65_0 = self.input.LA(1)

                        if LA65_0 == LSHIFT:
                            alt65 = 1
                        elif LA65_0 == RSHIFT:
                            alt65 = 2
                        else:
                            nvae = NoViableAltException("", 65, 0, self.input)

                            raise nvae

                        if alt65 == 1:
                            # YarcParser.g:165:38: LSHIFT
                            op = self.match(
                                self.input, LSHIFT, self.FOLLOW_LSHIFT_in_shift_expr2851
                            )

                        elif alt65 == 2:
                            # YarcParser.g:165:47: RSHIFT
                            op = self.match(
                                self.input, RSHIFT, self.FOLLOW_RSHIFT_in_shift_expr2855
                            )

                        self._state.following.append(
                            self.FOLLOW_arith_expr_in_shift_expr2860
                        )
                        exprs = self.arith_expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop66

                # TEMPLATE REWRITE
                # 165:75: -> shift_expr(exprs=$exprsop=$op)
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
    # YarcParser.g:166:1: arith_expr :terms+= term (op= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsop=$op);
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
                # YarcParser.g:166:13: (terms+= term (op= ( PLUS | MINUS ) terms+= term )* -> arith_expr(terms=$termsop=$op))
                # YarcParser.g:166:15: terms+= term (op= ( PLUS | MINUS ) terms+= term )*
                self._state.following.append(self.FOLLOW_term_in_arith_expr2886)
                terms = self.term()

                self._state.following.pop()
                if list_terms is None:
                    list_terms = []
                list_terms.append(terms.st)

                # YarcParser.g:166:27: (op= ( PLUS | MINUS ) terms+= term )*
                while True:  # loop68
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if LA68_0 in {MINUS, PLUS}:
                        alt68 = 1

                    if alt68 == 1:
                        # YarcParser.g:166:28: op= ( PLUS | MINUS ) terms+= term
                        pass
                        # YarcParser.g:166:31: ( PLUS | MINUS )
                        alt67 = 2
                        LA67_0 = self.input.LA(1)

                        if LA67_0 == PLUS:
                            alt67 = 1
                        elif LA67_0 == MINUS:
                            alt67 = 2
                        else:
                            nvae = NoViableAltException("", 67, 0, self.input)

                            raise nvae

                        if alt67 == 1:
                            # YarcParser.g:166:32: PLUS
                            op = self.match(
                                self.input, PLUS, self.FOLLOW_PLUS_in_arith_expr2892
                            )

                        elif alt67 == 2:
                            # YarcParser.g:166:39: MINUS
                            op = self.match(
                                self.input, MINUS, self.FOLLOW_MINUS_in_arith_expr2896
                            )

                        self._state.following.append(self.FOLLOW_term_in_arith_expr2901)
                        terms = self.term()

                        self._state.following.pop()
                        if list_terms is None:
                            list_terms = []
                        list_terms.append(terms.st)

                    else:
                        break  # loop68

                # TEMPLATE REWRITE
                # 166:60: -> arith_expr(terms=$termsop=$op)
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
    # YarcParser.g:167:1: term :factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsop=$op);
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
                # YarcParser.g:167:13: (factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )* -> term(factors=$factorsop=$op))
                # YarcParser.g:167:15: factors+= factor (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                self._state.following.append(self.FOLLOW_factor_in_term2933)
                factors = self.factor()

                self._state.following.pop()
                if list_factors is None:
                    list_factors = []
                list_factors.append(factors.st)

                # YarcParser.g:167:31: (op= ( MUL | DIV | MOD | IDIV ) factors+= factor )*
                while True:  # loop70
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if LA70_0 in {DIV, IDIV, MOD, MUL}:
                        alt70 = 1

                    if alt70 == 1:
                        # YarcParser.g:167:32: op= ( MUL | DIV | MOD | IDIV ) factors+= factor
                        pass
                        # YarcParser.g:167:35: ( MUL | DIV | MOD | IDIV )
                        alt69 = 4
                        LA69 = self.input.LA(1)
                        if LA69 in {MUL}:
                            alt69 = 1
                        elif LA69 in {DIV}:
                            alt69 = 2
                        elif LA69 in {MOD}:
                            alt69 = 3
                        elif LA69 in {IDIV}:
                            alt69 = 4
                        else:
                            nvae = NoViableAltException("", 69, 0, self.input)

                            raise nvae

                        if alt69 == 1:
                            # YarcParser.g:167:36: MUL
                            op = self.match(
                                self.input, MUL, self.FOLLOW_MUL_in_term2939
                            )

                        elif alt69 == 2:
                            # YarcParser.g:167:42: DIV
                            op = self.match(
                                self.input, DIV, self.FOLLOW_DIV_in_term2943
                            )

                        elif alt69 == 3:
                            # YarcParser.g:167:48: MOD
                            op = self.match(
                                self.input, MOD, self.FOLLOW_MOD_in_term2947
                            )

                        elif alt69 == 4:
                            # YarcParser.g:167:54: IDIV
                            op = self.match(
                                self.input, IDIV, self.FOLLOW_IDIV_in_term2951
                            )

                        self._state.following.append(self.FOLLOW_factor_in_term2956)
                        factors = self.factor()

                        self._state.following.pop()
                        if list_factors is None:
                            list_factors = []
                        list_factors.append(factors.st)

                    else:
                        break  # loop70

                # TEMPLATE REWRITE
                # 167:78: -> term(factors=$factorsop=$op)
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
    # YarcParser.g:168:1: factor : (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st});
    def factor(
        self,
    ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)

        prefix = None
        factor_ = None
        power36 = None

        try:
            try:
                # YarcParser.g:168:13: (prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor -> prefix_factor(factor=$factor_.stprefix=$prefix)| power -> {$power.st})
                alt72 = 2
                LA72_0 = self.input.LA(1)

                if LA72_0 in {BIT_NOT, MINUS, PLUS}:
                    alt72 = 1
                elif LA72_0 in {
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
                    alt72 = 2
                else:
                    nvae = NoViableAltException("", 72, 0, self.input)

                    raise nvae

                if alt72 == 1:
                    # YarcParser.g:168:15: prefix= ( PLUS | MINUS | BIT_NOT ) factor_= factor
                    pass
                    # YarcParser.g:168:22: ( PLUS | MINUS | BIT_NOT )
                    alt71 = 3
                    LA71 = self.input.LA(1)
                    if LA71 in {PLUS}:
                        alt71 = 1
                    elif LA71 in {MINUS}:
                        alt71 = 2
                    elif LA71 in {BIT_NOT}:
                        alt71 = 3
                    else:
                        nvae = NoViableAltException("", 71, 0, self.input)

                        raise nvae

                    if alt71 == 1:
                        # YarcParser.g:168:23: PLUS
                        prefix = self.match(
                            self.input, PLUS, self.FOLLOW_PLUS_in_factor2987
                        )

                    elif alt71 == 2:
                        # YarcParser.g:168:30: MINUS
                        prefix = self.match(
                            self.input, MINUS, self.FOLLOW_MINUS_in_factor2991
                        )

                    elif alt71 == 3:
                        # YarcParser.g:168:38: BIT_NOT
                        prefix = self.match(
                            self.input, BIT_NOT, self.FOLLOW_BIT_NOT_in_factor2995
                        )

                    self._state.following.append(self.FOLLOW_factor_in_factor3000)
                    factor_ = self.factor()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 168:62: -> prefix_factor(factor=$factor_.stprefix=$prefix)
                    retval.st = self.templateLib.getInstanceOf(
                        "prefix_factor",
                        attributes={
                            "factor": (
                                (factor_ is not None) and [factor_.st] or [None]
                            )[0],
                            "prefix": prefix,
                        },
                    )

                elif alt72 == 2:
                    # YarcParser.g:169:15: power
                    self._state.following.append(self.FOLLOW_power_in_factor3030)
                    power36 = self.power()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 169:21: -> {$power.st}
                    retval.st = ((power36 is not None) and [power36.st] or [None])[0]

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
    # YarcParser.g:170:1: power : atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st);
    def power(
        self,
    ):
        retval = self.power_return()
        retval.start = self.input.LT(1)

        atom_expr37 = None
        factor38 = None

        try:
            try:
                # YarcParser.g:170:13: ( atom_expr ( POWER factor )? -> power(atom=$atom_expr.stfactor=$factor.st))
                # YarcParser.g:170:15: atom_expr ( POWER factor )?
                self._state.following.append(self.FOLLOW_atom_expr_in_power3047)
                atom_expr37 = self.atom_expr()

                self._state.following.pop()

                # YarcParser.g:170:25: ( POWER factor )?
                alt73 = 2
                LA73_0 = self.input.LA(1)

                if LA73_0 == POWER:
                    alt73 = 1
                if alt73 == 1:
                    # YarcParser.g:170:26: POWER factor
                    self.match(self.input, POWER, self.FOLLOW_POWER_in_power3050)

                    self._state.following.append(self.FOLLOW_factor_in_power3052)
                    factor38 = self.factor()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 170:41: -> power(atom=$atom_expr.stfactor=$factor.st)
                retval.st = self.templateLib.getInstanceOf(
                    "power",
                    attributes={
                        "atom": (
                            (atom_expr37 is not None) and [atom_expr37.st] or [None]
                        )[0],
                        "factor": ((factor38 is not None) and [factor38.st] or [None])[
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
    # YarcParser.g:171:1: atom_expr : atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers);
    def atom_expr(
        self,
    ):
        retval = self.atom_expr_return()
        retval.start = self.input.LT(1)

        list_trailers = None
        atom39 = None
        trailers = None
        try:
            try:
                # YarcParser.g:171:13: ( atom (trailers+= trailer )* -> atom_expr(atom=$atom.sttrailers=$trailers))
                # YarcParser.g:171:15: atom (trailers+= trailer )*
                self._state.following.append(self.FOLLOW_atom_in_atom_expr3077)
                atom39 = self.atom()

                self._state.following.pop()

                # YarcParser.g:171:20: (trailers+= trailer )*
                while True:  # loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if LA74_0 in {DOT, LBRACK}:
                        alt74 = 1

                    if alt74 == 1:
                        # YarcParser.g:171:21: trailers+= trailer
                        self._state.following.append(
                            self.FOLLOW_trailer_in_atom_expr3082
                        )
                        trailers = self.trailer()

                        self._state.following.pop()
                        if list_trailers is None:
                            list_trailers = []
                        list_trailers.append(trailers.st)

                    else:
                        break  # loop74

                # TEMPLATE REWRITE
                # 171:41: -> atom_expr(atom=$atom.sttrailers=$trailers)
                retval.st = self.templateLib.getInstanceOf(
                    "atom_expr",
                    attributes={
                        "atom": ((atom39 is not None) and [atom39.st] or [None])[0],
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
    # YarcParser.g:172:1: atom : ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false() ;
    def atom(
        self,
    ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)

        SETTING_ID44 = None
        DISTRIBUTION45 = None
        INTEGER47 = None
        FLOAT_NUMBER48 = None
        STRING49 = None
        test_ = None
        testlist_comp40 = None
        vector_comp41 = None
        dict_or_set_maker42 = None
        name43 = None
        arglist46 = None

        try:
            try:
                # YarcParser.g:172:5: ( ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false() )
                # YarcParser.g:173:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false()
                pass
                # YarcParser.g:173:3: ( LPAREN test_= test RPAREN -> parenthesized_expr(expr=$test_.st)| LBRACK ( testlist_comp )? RBRACK -> list(list_comp=$testlist_comp.st)| LT ( vector_comp )? GT -> vector(values=$vector_comp.st)| LBRACE ( dict_or_set_maker )? RBRACE -> dict(dict_comp=$dict_or_set_maker.st)| LEN LPAREN test_= test RPAREN -> len(value=$test_.st)| name -> {$name.st}| SETTING_ID -> setting_id(id=$SETTING_ID.text)| DISTRIBUTION LPAREN arglist RPAREN -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)| INTEGER -> {$INTEGER.text}| FLOAT_NUMBER -> {$FLOAT_NUMBER.text}| STRING -> {$STRING.text}| NONE -> null(| TRUE -> true(| FALSE -> false()
                alt78 = 14
                LA78 = self.input.LA(1)
                if LA78 in {LPAREN}:
                    alt78 = 1
                elif LA78 in {LBRACK}:
                    alt78 = 2
                elif LA78 in {LT}:
                    alt78 = 3
                elif LA78 in {LBRACE}:
                    alt78 = 4
                elif LA78 in {LEN}:
                    alt78 = 5
                elif LA78 in {ID, UNDERSCORE}:
                    alt78 = 6
                elif LA78 in {SETTING_ID}:
                    alt78 = 7
                elif LA78 in {DISTRIBUTION}:
                    alt78 = 8
                elif LA78 in {INTEGER}:
                    alt78 = 9
                elif LA78 in {FLOAT_NUMBER}:
                    alt78 = 10
                elif LA78 in {STRING}:
                    alt78 = 11
                elif LA78 in {NONE}:
                    alt78 = 12
                elif LA78 in {TRUE}:
                    alt78 = 13
                elif LA78 in {FALSE}:
                    alt78 = 14
                else:
                    nvae = NoViableAltException("", 78, 0, self.input)

                    raise nvae

                if alt78 == 1:
                    # YarcParser.g:173:4: LPAREN test_= test RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom3107)

                    self._state.following.append(self.FOLLOW_test_in_atom3111)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom3113)

                    # TEMPLATE REWRITE
                    # 173:29: -> parenthesized_expr(expr=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "parenthesized_expr",
                        attributes={
                            "expr": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt78 == 2:
                    # YarcParser.g:174:5: LBRACK ( testlist_comp )? RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom3128)

                    # YarcParser.g:174:12: ( testlist_comp )?
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if LA75_0 in {
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
                        alt75 = 1
                    if alt75 == 1:
                        # YarcParser.g:174:12: testlist_comp
                        self._state.following.append(
                            self.FOLLOW_testlist_comp_in_atom3130
                        )
                        testlist_comp40 = self.testlist_comp()

                        self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom3133)

                    # TEMPLATE REWRITE
                    # 174:34: -> list(list_comp=$testlist_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list",
                        attributes={
                            "list_comp": (
                                (testlist_comp40 is not None)
                                and [testlist_comp40.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt78 == 3:
                    # YarcParser.g:175:5: LT ( vector_comp )? GT
                    self.match(self.input, LT, self.FOLLOW_LT_in_atom3148)

                    # YarcParser.g:175:8: ( vector_comp )?
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
                        PLUS,
                        SETTING_ID,
                        STRING,
                        TRUE,
                        UNDERSCORE,
                    }:
                        alt76 = 1
                    if alt76 == 1:
                        # YarcParser.g:175:8: vector_comp
                        self._state.following.append(
                            self.FOLLOW_vector_comp_in_atom3150
                        )
                        vector_comp41 = self.vector_comp()

                        self._state.following.pop()

                    self.match(self.input, GT, self.FOLLOW_GT_in_atom3153)

                    # TEMPLATE REWRITE
                    # 175:24: -> vector(values=$vector_comp.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "vector",
                        attributes={
                            "values": (
                                (vector_comp41 is not None)
                                and [vector_comp41.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt78 == 4:
                    # YarcParser.g:176:5: LBRACE ( dict_or_set_maker )? RBRACE
                    self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_atom3168)

                    # YarcParser.g:176:12: ( dict_or_set_maker )?
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if LA77_0 in {
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
                        alt77 = 1
                    if alt77 == 1:
                        # YarcParser.g:176:12: dict_or_set_maker
                        self._state.following.append(
                            self.FOLLOW_dict_or_set_maker_in_atom3170
                        )
                        dict_or_set_maker42 = self.dict_or_set_maker()

                        self._state.following.pop()

                    self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_atom3173)

                    # TEMPLATE REWRITE
                    # 176:38: -> dict(dict_comp=$dict_or_set_maker.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dict",
                        attributes={
                            "dict_comp": (
                                (dict_or_set_maker42 is not None)
                                and [dict_or_set_maker42.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt78 == 5:
                    # YarcParser.g:177:5: LEN LPAREN test_= test RPAREN
                    self.match(self.input, LEN, self.FOLLOW_LEN_in_atom3188)

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom3190)

                    self._state.following.append(self.FOLLOW_test_in_atom3194)
                    test_ = self.test()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom3196)

                    # TEMPLATE REWRITE
                    # 177:34: -> len(value=$test_.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "len",
                        attributes={
                            "value": ((test_ is not None) and [test_.st] or [None])[0]
                        },
                    )

                elif alt78 == 6:
                    # YarcParser.g:178:5: name
                    self._state.following.append(self.FOLLOW_name_in_atom3211)
                    name43 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 178:10: -> {$name.st}
                    retval.st = ((name43 is not None) and [name43.st] or [None])[0]

                elif alt78 == 7:
                    # YarcParser.g:179:5: SETTING_ID
                    SETTING_ID44 = self.match(
                        self.input, SETTING_ID, self.FOLLOW_SETTING_ID_in_atom3221
                    )

                    # TEMPLATE REWRITE
                    # 179:16: -> setting_id(id=$SETTING_ID.text)
                    retval.st = self.templateLib.getInstanceOf(
                        "setting_id", attributes={"id": SETTING_ID44.text}
                    )

                elif alt78 == 8:
                    # YarcParser.g:180:5: DISTRIBUTION LPAREN arglist RPAREN
                    DISTRIBUTION45 = self.match(
                        self.input, DISTRIBUTION, self.FOLLOW_DISTRIBUTION_in_atom3237
                    )

                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom3239)

                    self._state.following.append(self.FOLLOW_arglist_in_atom3241)
                    arglist46 = self.arglist()

                    self._state.following.pop()

                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom3243)

                    # TEMPLATE REWRITE
                    # 180:40: -> distribution(name=$DISTRIBUTION.textarglist=$arglist.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "distribution",
                        attributes={
                            "name": DISTRIBUTION45.text,
                            "arglist": (
                                (arglist46 is not None) and [arglist46.st] or [None]
                            )[0],
                        },
                    )

                elif alt78 == 9:
                    # YarcParser.g:181:5: INTEGER
                    INTEGER47 = self.match(
                        self.input, INTEGER, self.FOLLOW_INTEGER_in_atom3263
                    )

                    # TEMPLATE REWRITE
                    # 181:13: -> {$INTEGER.text}
                    retval.st = INTEGER47.text

                elif alt78 == 10:
                    # YarcParser.g:182:5: FLOAT_NUMBER
                    FLOAT_NUMBER48 = self.match(
                        self.input, FLOAT_NUMBER, self.FOLLOW_FLOAT_NUMBER_in_atom3273
                    )

                    # TEMPLATE REWRITE
                    # 182:18: -> {$FLOAT_NUMBER.text}
                    retval.st = FLOAT_NUMBER48.text

                elif alt78 == 11:
                    # YarcParser.g:183:5: STRING
                    STRING49 = self.match(
                        self.input, STRING, self.FOLLOW_STRING_in_atom3283
                    )

                    # TEMPLATE REWRITE
                    # 183:12: -> {$STRING.text}
                    retval.st = STRING49.text

                elif alt78 == 12:
                    # YarcParser.g:184:5: NONE
                    self.match(self.input, NONE, self.FOLLOW_NONE_in_atom3294)

                    # TEMPLATE REWRITE
                    # 184:10: -> null(
                    retval.st = self.templateLib.getInstanceOf("null")

                elif alt78 == 13:
                    # YarcParser.g:185:5: TRUE
                    self.match(self.input, TRUE, self.FOLLOW_TRUE_in_atom3306)

                    # TEMPLATE REWRITE
                    # 185:10: -> true(
                    retval.st = self.templateLib.getInstanceOf("true")

                elif alt78 == 14:
                    # YarcParser.g:186:5: FALSE
                    self.match(self.input, FALSE, self.FOLLOW_FALSE_in_atom3318)

                    # TEMPLATE REWRITE
                    # 186:11: -> false(
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
    # YarcParser.g:190:1: name : ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text});
    def name(
        self,
    ):
        retval = self.name_return()
        retval.start = self.input.LT(1)

        ID50 = None
        UNDERSCORE51 = None

        try:
            try:
                # YarcParser.g:190:5: ( ID -> {$ID.text}| UNDERSCORE -> {$UNDERSCORE.text})
                alt79 = 2
                LA79_0 = self.input.LA(1)

                if LA79_0 == ID:
                    alt79 = 1
                elif LA79_0 == UNDERSCORE:
                    alt79 = 2
                else:
                    nvae = NoViableAltException("", 79, 0, self.input)

                    raise nvae

                if alt79 == 1:
                    # YarcParser.g:191:3: ID
                    ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_name3338)

                    # TEMPLATE REWRITE
                    # 191:6: -> {$ID.text}
                    retval.st = ID50.text

                elif alt79 == 2:
                    # YarcParser.g:192:5: UNDERSCORE
                    UNDERSCORE51 = self.match(
                        self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_name3348
                    )

                    # TEMPLATE REWRITE
                    # 192:16: -> {$UNDERSCORE.text}
                    retval.st = UNDERSCORE51.text

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
    # YarcParser.g:203:1: testlist_comp :exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) ;
    def testlist_comp(
        self,
    ):
        retval = self.testlist_comp_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        to = None
        step = None
        comp_for52 = None
        exprs = None
        try:
            try:
                # YarcParser.g:203:15: (exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st)) )
                # YarcParser.g:203:17: exprs+= test ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                self._state.following.append(self.FOLLOW_test_in_testlist_comp3367)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:203:29: ( comp_for -> list_comp(expr=$exprs[0]for=$comp_for.st)| ( COMMA exprs+= test )* -> test_list(exprs=$exprs)| RANGE to= test ( STEP step= test )? -> range(from=$exprs[0]to=$to.ststep=$step.st))
                alt82 = 3
                LA82 = self.input.LA(1)
                if LA82 in {FOR}:
                    alt82 = 1
                elif LA82 in {COMMA, RBRACK}:
                    alt82 = 2
                elif LA82 in {RANGE}:
                    alt82 = 3
                else:
                    nvae = NoViableAltException("", 82, 0, self.input)

                    raise nvae

                if alt82 == 1:
                    # YarcParser.g:203:31: comp_for
                    self._state.following.append(
                        self.FOLLOW_comp_for_in_testlist_comp3371
                    )
                    comp_for52 = self.comp_for()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 203:40: -> list_comp(expr=$exprs[0]for=$comp_for.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "list_comp",
                        attributes={
                            "expr": list_exprs[0],
                            "for": (
                                (comp_for52 is not None) and [comp_for52.st] or [None]
                            )[0],
                        },
                    )

                elif alt82 == 2:
                    # YarcParser.g:204:24: ( COMMA exprs+= test )*
                    pass
                    # YarcParser.g:204:24: ( COMMA exprs+= test )*
                    while True:  # loop80
                        alt80 = 2
                        LA80_0 = self.input.LA(1)

                        if LA80_0 == COMMA:
                            alt80 = 1

                        if alt80 == 1:
                            # YarcParser.g:204:25: COMMA exprs+= test
                            self.match(
                                self.input,
                                COMMA,
                                self.FOLLOW_COMMA_in_testlist_comp3411,
                            )

                            self._state.following.append(
                                self.FOLLOW_test_in_testlist_comp3415
                            )
                            exprs = self.test()

                            self._state.following.pop()
                            if list_exprs is None:
                                list_exprs = []
                            list_exprs.append(exprs.st)

                        else:
                            break  # loop80

                    # TEMPLATE REWRITE
                    # 204:45: -> test_list(exprs=$exprs)
                    retval.st = self.templateLib.getInstanceOf(
                        "test_list", attributes={"exprs": list_exprs}
                    )

                elif alt82 == 3:
                    # YarcParser.g:205:24: RANGE to= test ( STEP step= test )?
                    self.match(
                        self.input, RANGE, self.FOLLOW_RANGE_in_testlist_comp3451
                    )

                    self._state.following.append(self.FOLLOW_test_in_testlist_comp3455)
                    to = self.test()

                    self._state.following.pop()

                    # YarcParser.g:205:38: ( STEP step= test )?
                    alt81 = 2
                    LA81_0 = self.input.LA(1)

                    if LA81_0 == STEP:
                        alt81 = 1
                    if alt81 == 1:
                        # YarcParser.g:205:39: STEP step= test
                        self.match(
                            self.input, STEP, self.FOLLOW_STEP_in_testlist_comp3458
                        )

                        self._state.following.append(
                            self.FOLLOW_test_in_testlist_comp3462
                        )
                        step = self.test()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 205:56: -> range(from=$exprs[0]to=$to.ststep=$step.st)
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
    # YarcParser.g:208:1: vector_comp : x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st);
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
                # YarcParser.g:208:15: (x= expr COMMA y= expr COMMA z= expr -> vector_comp(x=$x.sty=$y.stz=$z.st))
                # YarcParser.g:208:17: x= expr COMMA y= expr COMMA z= expr
                self._state.following.append(self.FOLLOW_expr_in_vector_comp3511)
                x = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp3513)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp3517)
                y = self.expr()

                self._state.following.pop()

                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vector_comp3519)

                self._state.following.append(self.FOLLOW_expr_in_vector_comp3523)
                z = self.expr()

                self._state.following.pop()

                # TEMPLATE REWRITE
                # 208:50: -> vector_comp(x=$x.sty=$y.stz=$z.st)
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
    # YarcParser.g:210:1: trailer : ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st));
    def trailer(
        self,
    ):
        retval = self.trailer_return()
        retval.start = self.input.LT(1)

        subscriptlist53 = None
        name54 = None

        try:
            try:
                # YarcParser.g:210:15: ( LBRACK subscriptlist RBRACK -> index(index=$subscriptlist.st)| DOT name -> dot_attr(attr=$name.st))
                alt83 = 2
                LA83_0 = self.input.LA(1)

                if LA83_0 == LBRACK:
                    alt83 = 1
                elif LA83_0 == DOT:
                    alt83 = 2
                else:
                    nvae = NoViableAltException("", 83, 0, self.input)

                    raise nvae

                if alt83 == 1:
                    # YarcParser.g:210:17: LBRACK subscriptlist RBRACK
                    self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_trailer3557)

                    self._state.following.append(
                        self.FOLLOW_subscriptlist_in_trailer3559
                    )
                    subscriptlist53 = self.subscriptlist()

                    self._state.following.pop()

                    self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_trailer3561)

                    # TEMPLATE REWRITE
                    # 210:45: -> index(index=$subscriptlist.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "index",
                        attributes={
                            "index": (
                                (subscriptlist53 is not None)
                                and [subscriptlist53.st]
                                or [None]
                            )[0]
                        },
                    )

                elif alt83 == 2:
                    # YarcParser.g:211:17: DOT name
                    self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer3589)

                    self._state.following.append(self.FOLLOW_name_in_trailer3591)
                    name54 = self.name()

                    self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 211:26: -> dot_attr(attr=$name.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "dot_attr",
                        attributes={
                            "attr": ((name54 is not None) and [name54.st] or [None])[0]
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
    # YarcParser.g:212:1: arglist :args+= argument ( COMMA args+= argument )* -> arg_list(args=$args);
    def arglist(
        self,
    ):
        retval = self.arglist_return()
        retval.start = self.input.LT(1)

        list_args = None
        args = None
        try:
            try:
                # YarcParser.g:212:15: (args+= argument ( COMMA args+= argument )* -> arg_list(args=$args))
                # YarcParser.g:212:17: args+= argument ( COMMA args+= argument )*
                self._state.following.append(self.FOLLOW_argument_in_arglist3615)
                args = self.argument()

                self._state.following.pop()
                if list_args is None:
                    list_args = []
                list_args.append(args.st)

                # YarcParser.g:212:32: ( COMMA args+= argument )*
                while True:  # loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if LA84_0 == COMMA:
                        alt84 = 1

                    if alt84 == 1:
                        # YarcParser.g:212:33: COMMA args+= argument
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arglist3618)

                        self._state.following.append(
                            self.FOLLOW_argument_in_arglist3622
                        )
                        args = self.argument()

                        self._state.following.pop()
                        if list_args is None:
                            list_args = []
                        list_args.append(args.st)

                    else:
                        break  # loop84

                # TEMPLATE REWRITE
                # 212:56: -> arg_list(args=$args)
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
    # YarcParser.g:213:1: argument : kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st);
    def argument(
        self,
    ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)

        kw_or_arg = None
        arg = None

        try:
            try:
                # YarcParser.g:213:15: (kw_or_arg= test ( ASSIGN arg= test )? -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st))
                # YarcParser.g:213:17: kw_or_arg= test ( ASSIGN arg= test )?
                self._state.following.append(self.FOLLOW_test_in_argument3647)
                kw_or_arg = self.test()

                self._state.following.pop()

                # YarcParser.g:213:32: ( ASSIGN arg= test )?
                alt85 = 2
                LA85_0 = self.input.LA(1)

                if LA85_0 == ASSIGN:
                    alt85 = 1
                if alt85 == 1:
                    # YarcParser.g:213:33: ASSIGN arg= test
                    self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_argument3650)

                    self._state.following.append(self.FOLLOW_test_in_argument3654)
                    arg = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 213:51: -> arg(kw_or_arg=$kw_or_arg.starg=$arg.st)
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
    # YarcParser.g:214:1: subscriptlist :subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs);
    def subscriptlist(
        self,
    ):
        retval = self.subscriptlist_return()
        retval.start = self.input.LT(1)

        list_subs = None
        subs = None
        try:
            try:
                # YarcParser.g:214:15: (subs+= subscript_ ( COMMA subs+= subscript_ )* -> subscript_list(subs=$subs))
                # YarcParser.g:214:17: subs+= subscript_ ( COMMA subs+= subscript_ )*
                self._state.following.append(
                    self.FOLLOW_subscript__in_subscriptlist3679
                )
                subs = self.subscript_()

                self._state.following.pop()
                if list_subs is None:
                    list_subs = []
                list_subs.append(subs.st)

                # YarcParser.g:214:34: ( COMMA subs+= subscript_ )*
                while True:  # loop86
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if LA86_0 == COMMA:
                        alt86 = 1

                    if alt86 == 1:
                        # YarcParser.g:214:35: COMMA subs+= subscript_
                        self.match(
                            self.input, COMMA, self.FOLLOW_COMMA_in_subscriptlist3682
                        )

                        self._state.following.append(
                            self.FOLLOW_subscript__in_subscriptlist3686
                        )
                        subs = self.subscript_()

                        self._state.following.pop()
                        if list_subs is None:
                            list_subs = []
                        list_subs.append(subs.st)

                    else:
                        break  # loop86

                # TEMPLATE REWRITE
                # 214:60: -> subscript_list(subs=$subs)
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
    # YarcParser.g:215:1: subscript_ : (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st));
    def subscript_(
        self,
    ):
        retval = self.subscript__return()
        retval.start = self.input.LT(1)

        to = None
        step = None
        COLON55 = None
        COLON56 = None
        from_ = None

        try:
            try:
                # YarcParser.g:215:15: (from_= test ( COLON to= ( test )? step= ( sliceop )? )? -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)| COLON to= ( test )? step= ( sliceop )? -> subscript(colon=$COLONto=$to.ststep=$step.st))
                alt92 = 2
                LA92_0 = self.input.LA(1)

                if LA92_0 in {
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
                    alt92 = 1
                elif LA92_0 == COLON:
                    alt92 = 2
                else:
                    nvae = NoViableAltException("", 92, 0, self.input)

                    raise nvae

                if alt92 == 1:
                    # YarcParser.g:215:17: from_= test ( COLON to= ( test )? step= ( sliceop )? )?
                    self._state.following.append(self.FOLLOW_test_in_subscript_3709)
                    from_ = self.test()

                    self._state.following.pop()

                    # YarcParser.g:215:28: ( COLON to= ( test )? step= ( sliceop )? )?
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if LA89_0 == COLON:
                        alt89 = 1
                    if alt89 == 1:
                        # YarcParser.g:215:29: COLON to= ( test )? step= ( sliceop )?
                        COLON55 = self.match(
                            self.input, COLON, self.FOLLOW_COLON_in_subscript_3712
                        )

                        # YarcParser.g:215:38: ( test )?
                        alt87 = 2
                        LA87_0 = self.input.LA(1)

                        if LA87_0 in {
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
                            alt87 = 1
                        if alt87 == 1:
                            # YarcParser.g:215:39: test
                            self._state.following.append(
                                self.FOLLOW_test_in_subscript_3717
                            )
                            to = self.test()

                            self._state.following.pop()

                        # YarcParser.g:215:51: ( sliceop )?
                        alt88 = 2
                        LA88_0 = self.input.LA(1)

                        if LA88_0 == COLON:
                            alt88 = 1
                        if alt88 == 1:
                            # YarcParser.g:215:52: sliceop
                            self._state.following.append(
                                self.FOLLOW_sliceop_in_subscript_3724
                            )
                            step = self.sliceop()

                            self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 215:64: -> subscript(from=$from_.stcolon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={
                            "from": ((from_ is not None) and [from_.st] or [None])[0],
                            "colon": COLON55,
                            "to": to.st,
                            "step": step.st,
                        },
                    )

                elif alt92 == 2:
                    # YarcParser.g:216:17: COLON to= ( test )? step= ( sliceop )?
                    COLON56 = self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_subscript_3770
                    )

                    # YarcParser.g:216:26: ( test )?
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if LA90_0 in {
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
                        alt90 = 1
                    if alt90 == 1:
                        # YarcParser.g:216:27: test
                        self._state.following.append(self.FOLLOW_test_in_subscript_3775)
                        to = self.test()

                        self._state.following.pop()

                    # YarcParser.g:216:39: ( sliceop )?
                    alt91 = 2
                    LA91_0 = self.input.LA(1)

                    if LA91_0 == COLON:
                        alt91 = 1
                    if alt91 == 1:
                        # YarcParser.g:216:40: sliceop
                        self._state.following.append(
                            self.FOLLOW_sliceop_in_subscript_3782
                        )
                        step = self.sliceop()

                        self._state.following.pop()

                    # TEMPLATE REWRITE
                    # 216:51: -> subscript(colon=$COLONto=$to.ststep=$step.st)
                    retval.st = self.templateLib.getInstanceOf(
                        "subscript",
                        attributes={"colon": COLON56, "to": to.st, "step": step.st},
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
    # YarcParser.g:217:1: sliceop : COLON ( test )? -> subscipt_step(step=$test.st);
    def sliceop(
        self,
    ):
        retval = self.sliceop_return()
        retval.start = self.input.LT(1)

        test57 = None

        try:
            try:
                # YarcParser.g:217:15: ( COLON ( test )? -> subscipt_step(step=$test.st))
                # YarcParser.g:217:17: COLON ( test )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_sliceop3817)

                # YarcParser.g:217:23: ( test )?
                alt93 = 2
                LA93_0 = self.input.LA(1)

                if LA93_0 in {
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
                    alt93 = 1
                if alt93 == 1:
                    # YarcParser.g:217:23: test
                    self._state.following.append(self.FOLLOW_test_in_sliceop3819)
                    test57 = self.test()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 217:29: -> subscipt_step(step=$test.st)
                retval.st = self.templateLib.getInstanceOf(
                    "subscipt_step",
                    attributes={
                        "step": ((test57 is not None) and [test57.st] or [None])[0]
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
    # YarcParser.g:219:1: exprlist :exprs+= expr ( COMMA exprs+= expr )* -> test_list(exprs=$exprs);
    def exprlist(
        self,
    ):
        retval = self.exprlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:219:10: (exprs+= expr ( COMMA exprs+= expr )* -> test_list(exprs=$exprs))
                # YarcParser.g:219:12: exprs+= expr ( COMMA exprs+= expr )*
                self._state.following.append(self.FOLLOW_expr_in_exprlist3839)
                exprs = self.expr()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:219:24: ( COMMA exprs+= expr )*
                while True:  # loop94
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if LA94_0 == COMMA:
                        alt94 = 1

                    if alt94 == 1:
                        # YarcParser.g:219:25: COMMA exprs+= expr
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_exprlist3842)

                        self._state.following.append(self.FOLLOW_expr_in_exprlist3846)
                        exprs = self.expr()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop94

                # TEMPLATE REWRITE
                # 219:45: -> test_list(exprs=$exprs)
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
    # YarcParser.g:220:1: testlist :exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs);
    def testlist(
        self,
    ):
        retval = self.testlist_return()
        retval.start = self.input.LT(1)

        list_exprs = None
        exprs = None
        try:
            try:
                # YarcParser.g:220:10: (exprs+= test ( COMMA exprs+= test )* -> test_list(exprs=$exprs))
                # YarcParser.g:220:12: exprs+= test ( COMMA exprs+= test )*
                self._state.following.append(self.FOLLOW_test_in_testlist3866)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:220:24: ( COMMA exprs+= test )*
                while True:  # loop95
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if LA95_0 == COMMA:
                        alt95 = 1

                    if alt95 == 1:
                        # YarcParser.g:220:25: COMMA exprs+= test
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_testlist3869)

                        self._state.following.append(self.FOLLOW_test_in_testlist3873)
                        exprs = self.test()

                        self._state.following.pop()
                        if list_exprs is None:
                            list_exprs = []
                        list_exprs.append(exprs.st)

                    else:
                        break  # loop95

                # TEMPLATE REWRITE
                # 220:45: -> test_list(exprs=$exprs)
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
    # YarcParser.g:221:1: dict_or_set_maker :exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs)) ;
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
                # YarcParser.g:221:18: (exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs)) )
                # YarcParser.g:222:3: exprs+= test ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs))
                self._state.following.append(self.FOLLOW_test_in_dict_or_set_maker3894)
                exprs = self.test()

                self._state.following.pop()
                if list_exprs is None:
                    list_exprs = []
                list_exprs.append(exprs.st)

                # YarcParser.g:222:15: ( COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* ) -> key_value_list(keys=$exprsvalues=$values)| (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* ) -> test_list(exprs=$exprs))
                alt100 = 2
                LA100_0 = self.input.LA(1)

                if LA100_0 == COLON:
                    alt100 = 1
                elif LA100_0 in {COMMA, FOR, RBRACE}:
                    alt100 = 2
                else:
                    nvae = NoViableAltException("", 100, 0, self.input)

                    raise nvae

                if alt100 == 1:
                    # YarcParser.g:222:17: COLON values+= test (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* )
                    self.match(
                        self.input, COLON, self.FOLLOW_COLON_in_dict_or_set_maker3898
                    )

                    self._state.following.append(
                        self.FOLLOW_test_in_dict_or_set_maker3902
                    )
                    values = self.test()

                    self._state.following.pop()
                    if list_values is None:
                        list_values = []
                    list_values.append(values.st)

                    # YarcParser.g:222:36: (for_= comp_for -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)| ( COMMA exprs+= test COLON values+= test )* )
                    alt97 = 2
                    LA97_0 = self.input.LA(1)

                    if LA97_0 == FOR:
                        alt97 = 1
                    elif LA97_0 in {COMMA, RBRACE}:
                        alt97 = 2
                    else:
                        nvae = NoViableAltException("", 97, 0, self.input)

                        raise nvae

                    if alt97 == 1:
                        # YarcParser.g:222:37: for_= comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker3907
                        )
                        for_ = self.comp_for()

                        self._state.following.pop()

                        # TEMPLATE REWRITE
                        # 222:51: -> dict_comp(key=$exprs[0]value=$values[0]for=$for_.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "dict_comp",
                            attributes={
                                "key": list_exprs[0],
                                "value": list_values[0],
                                "for": ((for_ is not None) and [for_.st] or [None])[0],
                            },
                        )

                    elif alt97 == 2:
                        # YarcParser.g:223:38: ( COMMA exprs+= test COLON values+= test )*
                        pass
                        # YarcParser.g:223:38: ( COMMA exprs+= test COLON values+= test )*
                        while True:  # loop96
                            alt96 = 2
                            LA96_0 = self.input.LA(1)

                            if LA96_0 == COMMA:
                                alt96 = 1

                            if alt96 == 1:
                                # YarcParser.g:223:39: COMMA exprs+= test COLON values+= test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker3966,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker3970
                                )
                                exprs = self.test()

                                self._state.following.pop()
                                if list_exprs is None:
                                    list_exprs = []
                                list_exprs.append(exprs.st)

                                self.match(
                                    self.input,
                                    COLON,
                                    self.FOLLOW_COLON_in_dict_or_set_maker3972,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker3976
                                )
                                values = self.test()

                                self._state.following.pop()
                                if list_values is None:
                                    list_values = []
                                list_values.append(values.st)

                            else:
                                break  # loop96

                    # TEMPLATE REWRITE
                    # 223:79: -> key_value_list(keys=$exprsvalues=$values)
                    retval.st = self.templateLib.getInstanceOf(
                        "key_value_list",
                        attributes={"keys": list_exprs, "values": list_values},
                    )

                elif alt100 == 2:
                    # YarcParser.g:224:17: (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* )
                    pass
                    # YarcParser.g:224:17: (for_= comp_for -> list_comp(expr=$exprs[0]for=$for_.st)| ( COMMA exprs+= test )* )
                    alt99 = 2
                    LA99_0 = self.input.LA(1)

                    if LA99_0 == FOR:
                        alt99 = 1
                    elif LA99_0 in {COMMA, RBRACE}:
                        alt99 = 2
                    else:
                        nvae = NoViableAltException("", 99, 0, self.input)

                        raise nvae

                    if alt99 == 1:
                        # YarcParser.g:224:18: for_= comp_for
                        self._state.following.append(
                            self.FOLLOW_comp_for_in_dict_or_set_maker4014
                        )
                        for_ = self.comp_for()

                        self._state.following.pop()

                        # TEMPLATE REWRITE
                        # 224:32: -> list_comp(expr=$exprs[0]for=$for_.st)
                        retval.st = self.templateLib.getInstanceOf(
                            "list_comp",
                            attributes={
                                "expr": list_exprs[0],
                                "for": ((for_ is not None) and [for_.st] or [None])[0],
                            },
                        )

                    elif alt99 == 2:
                        # YarcParser.g:225:19: ( COMMA exprs+= test )*
                        pass
                        # YarcParser.g:225:19: ( COMMA exprs+= test )*
                        while True:  # loop98
                            alt98 = 2
                            LA98_0 = self.input.LA(1)

                            if LA98_0 == COMMA:
                                alt98 = 1

                            if alt98 == 1:
                                # YarcParser.g:225:20: COMMA exprs+= test
                                self.match(
                                    self.input,
                                    COMMA,
                                    self.FOLLOW_COMMA_in_dict_or_set_maker4052,
                                )

                                self._state.following.append(
                                    self.FOLLOW_test_in_dict_or_set_maker4056
                                )
                                exprs = self.test()

                                self._state.following.pop()
                                if list_exprs is None:
                                    list_exprs = []
                                list_exprs.append(exprs.st)

                            else:
                                break  # loop98

                    # TEMPLATE REWRITE
                    # 225:42: -> test_list(exprs=$exprs)
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
    # YarcParser.g:229:1: comp_iter : comp= ( comp_for | comp_if ) -> {$comp.st};
    def comp_iter(
        self,
    ):
        retval = self.comp_iter_return()
        retval.start = self.input.LT(1)

        comp = None

        try:
            try:
                # YarcParser.g:229:11: (comp= ( comp_for | comp_if ) -> {$comp.st})
                # YarcParser.g:229:13: comp= ( comp_for | comp_if )
                pass
                # YarcParser.g:229:18: ( comp_for | comp_if )
                alt101 = 2
                LA101_0 = self.input.LA(1)

                if LA101_0 == FOR:
                    alt101 = 1
                elif LA101_0 == IF:
                    alt101 = 2
                else:
                    nvae = NoViableAltException("", 101, 0, self.input)

                    raise nvae

                if alt101 == 1:
                    # YarcParser.g:229:19: comp_for
                    self._state.following.append(self.FOLLOW_comp_for_in_comp_iter4097)
                    comp = self.comp_for()

                    self._state.following.pop()

                elif alt101 == 2:
                    # YarcParser.g:229:30: comp_if
                    self._state.following.append(self.FOLLOW_comp_if_in_comp_iter4101)
                    comp = self.comp_if()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 229:39: -> {$comp.st}
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
    # YarcParser.g:230:1: comp_for : FOR exprlist IN or_test ( comp_iter )? -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st);
    def comp_for(
        self,
    ):
        retval = self.comp_for_return()
        retval.start = self.input.LT(1)

        exprlist58 = None
        or_test59 = None
        comp_iter60 = None

        try:
            try:
                # YarcParser.g:230:11: ( FOR exprlist IN or_test ( comp_iter )? -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st))
                # YarcParser.g:230:13: FOR exprlist IN or_test ( comp_iter )?
                self.match(self.input, FOR, self.FOLLOW_FOR_in_comp_for4114)

                self._state.following.append(self.FOLLOW_exprlist_in_comp_for4116)
                exprlist58 = self.exprlist()

                self._state.following.pop()

                self.match(self.input, IN, self.FOLLOW_IN_in_comp_for4118)

                self._state.following.append(self.FOLLOW_or_test_in_comp_for4120)
                or_test59 = self.or_test()

                self._state.following.pop()

                # YarcParser.g:230:37: ( comp_iter )?
                alt102 = 2
                LA102_0 = self.input.LA(1)

                if LA102_0 in {FOR, IF}:
                    alt102 = 1
                if alt102 == 1:
                    # YarcParser.g:230:37: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_for4122)
                    comp_iter60 = self.comp_iter()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 230:48: -> comp_for(exprs=$exprlist.stseq=$or_test.stcomp_iter=$comp_iter.st)
                retval.st = self.templateLib.getInstanceOf(
                    "comp_for",
                    attributes={
                        "exprs": (
                            (exprlist58 is not None) and [exprlist58.st] or [None]
                        )[0],
                        "seq": ((or_test59 is not None) and [or_test59.st] or [None])[
                            0
                        ],
                        "comp_iter": (
                            (comp_iter60 is not None) and [comp_iter60.st] or [None]
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
    # YarcParser.g:231:1: comp_if : IF test_nocond ( comp_iter )? -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st);
    def comp_if(
        self,
    ):
        retval = self.comp_if_return()
        retval.start = self.input.LT(1)

        test_nocond61 = None
        comp_iter62 = None

        try:
            try:
                # YarcParser.g:231:11: ( IF test_nocond ( comp_iter )? -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st))
                # YarcParser.g:231:13: IF test_nocond ( comp_iter )?
                self.match(self.input, IF, self.FOLLOW_IF_in_comp_if4151)

                self._state.following.append(self.FOLLOW_test_nocond_in_comp_if4153)
                test_nocond61 = self.test_nocond()

                self._state.following.pop()

                # YarcParser.g:231:28: ( comp_iter )?
                alt103 = 2
                LA103_0 = self.input.LA(1)

                if LA103_0 in {FOR, IF}:
                    alt103 = 1
                if alt103 == 1:
                    # YarcParser.g:231:28: comp_iter
                    self._state.following.append(self.FOLLOW_comp_iter_in_comp_if4155)
                    comp_iter62 = self.comp_iter()

                    self._state.following.pop()

                # TEMPLATE REWRITE
                # 231:39: -> comp_if(cond=$test_nocond.stcomp_iter=$comp_iter.st)
                retval.st = self.templateLib.getInstanceOf(
                    "comp_if",
                    attributes={
                        "cond": (
                            (test_nocond61 is not None) and [test_nocond61.st] or [None]
                        )[0],
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

    # $ANTLR end "comp_if"

    FOLLOW_NEWLINE_in_scenario59 = frozenset([72, 96])
    FOLLOW_declaration_in_scenario62 = frozenset([1, 72, 99, 107, 121])
    FOLLOW_NEWLINE_in_scenario64 = frozenset([1, 72, 99, 107, 121])
    FOLLOW_settings_in_scenario67 = frozenset([1, 107, 121])
    FOLLOW_stage_in_scenario70 = frozenset([1, 121])
    FOLLOW_writers_in_scenario73 = frozenset([1])
    FOLLOW_SCENARIO_in_declaration115 = frozenset([43])
    FOLLOW_ID_in_declaration117 = frozenset([15, 72])
    FOLLOW_COLON_in_declaration120 = frozenset([43, 117])
    FOLLOW_name_in_declaration122 = frozenset([72])
    FOLLOW_NEWLINE_in_declaration126 = frozenset([1])
    FOLLOW_SETTINGS_in_settings149 = frozenset([15])
    FOLLOW_COLON_in_settings151 = frozenset([72])
    FOLLOW_NEWLINE_in_settings153 = frozenset([49])
    FOLLOW_INDENT_in_settings155 = frozenset([43])
    FOLLOW_setting_in_settings159 = frozenset([19, 43])
    FOLLOW_DEDENT_in_settings162 = frozenset([1])
    FOLLOW_STAGE_in_stage184 = frozenset([15])
    FOLLOW_COLON_in_stage186 = frozenset([72])
    FOLLOW_NEWLINE_in_stage188 = frozenset([49])
    FOLLOW_INDENT_in_stage190 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            79,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_stmts_in_stage192 = frozenset([19])
    FOLLOW_DEDENT_in_stage194 = frozenset([1])
    FOLLOW_WRITERS_in_writers209 = frozenset([15])
    FOLLOW_COLON_in_writers211 = frozenset([72])
    FOLLOW_NEWLINE_in_writers213 = frozenset([49])
    FOLLOW_INDENT_in_writers215 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_expr_stmt_in_writers220 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_writer_in_writers224 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_DEDENT_in_writers228 = frozenset([1])
    FOLLOW_ID_in_setting252 = frozenset([5])
    FOLLOW_ASSIGN_in_setting254 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_setting256 = frozenset([72])
    FOLLOW_NEWLINE_in_setting258 = frozenset([1])
    FOLLOW_open_stmt_in_stmts292 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_aug_expr_stmt_in_stmts299 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_edit_stmt_in_stmts303 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_behavior_stmt_in_stmts307 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_ID_in_writer333 = frozenset([15])
    FOLLOW_COLON_in_writer335 = frozenset([72])
    FOLLOW_NEWLINE_in_writer337 = frozenset([49])
    FOLLOW_INDENT_in_writer339 = frozenset([43])
    FOLLOW_writer_param_in_writer343 = frozenset([19, 43])
    FOLLOW_DEDENT_in_writer346 = frozenset([1])
    FOLLOW_ID_in_writer_param370 = frozenset([5])
    FOLLOW_ASSIGN_in_writer_param372 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_writer_param374 = frozenset([72])
    FOLLOW_NEWLINE_in_writer_param376 = frozenset([1])
    FOLLOW_OPEN_in_open_stmt402 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_open_stmt404 = frozenset([72])
    FOLLOW_NEWLINE_in_open_stmt406 = frozenset([1])
    FOLLOW_EDIT_in_edit_stmt422 = frozenset([43, 113, 117])
    FOLLOW_TIMELINE_in_edit_stmt425 = frozenset([15])
    FOLLOW_COLON_in_edit_stmt427 = frozenset([72])
    FOLLOW_NEWLINE_in_edit_stmt429 = frozenset([49])
    FOLLOW_INDENT_in_edit_stmt431 = frozenset([43, 117])
    FOLLOW_name_in_edit_stmt436 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_edit_stmt440 = frozenset([72])
    FOLLOW_NEWLINE_in_edit_stmt442 = frozenset([19, 43, 117])
    FOLLOW_DEDENT_in_edit_stmt446 = frozenset([1])
    FOLLOW_name_in_edit_stmt484 = frozenset([15])
    FOLLOW_edit_block_in_edit_stmt486 = frozenset([1])
    FOLLOW_CREATE_in_create_expr535 = frozenset(
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
            58,
            62,
            64,
            67,
            68,
            73,
            75,
            83,
            100,
            101,
            109,
            110,
            116,
            117,
        ]
    )
    FOLLOW_test_in_create_expr539 = frozenset([13, 37, 58, 67, 101, 109])
    FOLLOW_STEREO_in_create_expr551 = frozenset([13])
    FOLLOW_CAMERA_in_create_expr554 = frozenset([15, 72])
    FOLLOW_SHAPE_in_create_expr558 = frozenset([15, 72])
    FOLLOW_LIGHT_in_create_expr562 = frozenset([15, 72])
    FOLLOW_edit_block_in_create_expr568 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr573 = frozenset([1])
    FOLLOW_FROM_in_create_expr706 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_create_expr710 = frozenset([15, 72])
    FOLLOW_edit_block_in_create_expr715 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr720 = frozenset([1])
    FOLLOW_MATERIAL_in_create_expr852 = frozenset([15, 72])
    FOLLOW_simple_block_in_create_expr857 = frozenset([1])
    FOLLOW_NEWLINE_in_create_expr861 = frozenset([1])
    FOLLOW_INSTANTIATE_in_instantiate_expr923 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_test_in_instantiate_expr928 = frozenset([37])
    FOLLOW_FROM_in_instantiate_expr932 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_instantiate_expr936 = frozenset([15, 72])
    FOLLOW_edit_block_in_instantiate_expr939 = frozenset([1])
    FOLLOW_NEWLINE_in_instantiate_expr944 = frozenset([1])
    FOLLOW_GROUP_in_group_expr1083 = frozenset([55])
    FOLLOW_LBRACK_in_group_expr1085 = frozenset([43, 117])
    FOLLOW_name_in_group_expr1089 = frozenset([16, 88])
    FOLLOW_COMMA_in_group_expr1092 = frozenset([43, 117])
    FOLLOW_name_in_group_expr1096 = frozenset([16, 88])
    FOLLOW_RBRACK_in_group_expr1100 = frozenset([15, 72])
    FOLLOW_edit_block_in_group_expr1103 = frozenset([1])
    FOLLOW_NEWLINE_in_group_expr1108 = frozenset([1])
    FOLLOW_GET_in_get_expr1222 = frozenset(
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
            62,
            64,
            67,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_CAMERA_in_get_expr1228 = frozenset([6])
    FOLLOW_LIGHT_in_get_expr1232 = frozenset([6])
    FOLLOW_MATERIAL_in_get_expr1236 = frozenset([6])
    FOLLOW_name_in_get_expr1240 = frozenset([6])
    FOLLOW_AT_in_get_expr1243 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_get_expr1249 = frozenset([15, 72])
    FOLLOW_simple_block_in_get_expr1252 = frozenset([1])
    FOLLOW_NEWLINE_in_get_expr1256 = frozenset([1])
    FOLLOW_COLON_in_edit_block1348 = frozenset([72])
    FOLLOW_NEWLINE_in_edit_block1350 = frozenset([49])
    FOLLOW_INDENT_in_edit_block1352 = frozenset(
        [28, 43, 61, 82, 90, 91, 94, 95, 97, 103, 115, 117, 119, 120]
    )
    FOLLOW_attr_in_edit_block1358 = frozenset(
        [19, 28, 43, 61, 82, 90, 91, 94, 95, 97, 103, 115, 117, 119, 120]
    )
    FOLLOW_inner_behavior_stmt_in_edit_block1362 = frozenset(
        [19, 28, 43, 61, 82, 90, 91, 94, 95, 97, 103, 115, 117, 119, 120]
    )
    FOLLOW_DEDENT_in_edit_block1370 = frozenset([1])
    FOLLOW_COLON_in_simple_block1389 = frozenset([72])
    FOLLOW_NEWLINE_in_simple_block1391 = frozenset([49])
    FOLLOW_INDENT_in_simple_block1393 = frozenset([43, 117])
    FOLLOW_simple_attr_in_simple_block1396 = frozenset([19, 43, 117])
    FOLLOW_DEDENT_in_simple_block1402 = frozenset([1])
    FOLLOW_core_attr_in_attr1417 = frozenset([1])
    FOLLOW_simple_attr_in_attr1421 = frozenset([1])
    FOLLOW_compound_attr_in_attr1425 = frozenset([1])
    FOLLOW_name_in_simple_attr1455 = frozenset(
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
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_COLON_in_simple_attr1458 = frozenset([43, 117])
    FOLLOW_name_in_simple_attr1462 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_simple_attr1468 = frozenset([72])
    FOLLOW_NEWLINE_in_simple_attr1470 = frozenset([1])
    FOLLOW_SCATTER_in_compound_attr1517 = frozenset([78])
    FOLLOW_ON_in_compound_attr1519 = frozenset([43, 117])
    FOLLOW_name_in_compound_attr1523 = frozenset([15, 72])
    FOLLOW_simple_block_in_compound_attr1528 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr1532 = frozenset([1])
    FOLLOW_ROT_AROUND_in_compound_attr1616 = frozenset([43, 117])
    FOLLOW_name_in_compound_attr1620 = frozenset([15, 72])
    FOLLOW_simple_block_in_compound_attr1625 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr1629 = frozenset([1])
    FOLLOW_PHYSICS_in_compound_attr1686 = frozenset([15, 72])
    FOLLOW_simple_block_in_compound_attr1691 = frozenset([1])
    FOLLOW_NEWLINE_in_compound_attr1695 = frozenset([1])
    FOLLOW_TRANSLATE_in_core_attr1766 = frozenset([8, 114])
    FOLLOW_AXIS_in_core_attr1770 = frozenset([114])
    FOLLOW_TO_in_core_attr1773 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_core_attr1777 = frozenset([72])
    FOLLOW_ROTATE_in_core_attr1801 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_AXIS_in_core_attr1805 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_core_attr1810 = frozenset([72, 81])
    FOLLOW_ORDER_in_core_attr1812 = frozenset([72])
    FOLLOW_SCALE_in_core_attr1837 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_core_attr1841 = frozenset([72])
    FOLLOW_LOOK_AT_in_core_attr1860 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_core_attr1864 = frozenset([72])
    FOLLOW_UP_AXIS_in_core_attr1883 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_core_attr1887 = frozenset([72])
    FOLLOW_SIZE_in_core_attr1906 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_core_attr1910 = frozenset([72])
    FOLLOW_SEMANTICS_in_core_attr1929 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_core_attr1933 = frozenset([72])
    FOLLOW_VISIBLE_in_core_attr1952 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_core_attr1956 = frozenset([72])
    FOLLOW_NEWLINE_in_core_attr1973 = frozenset([1])
    FOLLOW_behavior_expr_in_inner_behavior_stmt1996 = frozenset([15])
    FOLLOW_inner_behavior_block_in_inner_behavior_stmt1998 = frozenset([1])
    FOLLOW_COLON_in_inner_behavior_block2024 = frozenset([72])
    FOLLOW_NEWLINE_in_inner_behavior_block2026 = frozenset([49])
    FOLLOW_INDENT_in_inner_behavior_block2028 = frozenset(
        [43, 61, 82, 90, 91, 94, 95, 97, 103, 115, 117, 119, 120]
    )
    FOLLOW_attr_in_inner_behavior_block2032 = frozenset(
        [19, 43, 61, 82, 90, 91, 94, 95, 97, 103, 115, 117, 119, 120]
    )
    FOLLOW_DEDENT_in_inner_behavior_block2035 = frozenset([1])
    FOLLOW_behavior_expr_in_behavior_stmt2055 = frozenset([15])
    FOLLOW_behavior_block_in_behavior_stmt2057 = frozenset([1])
    FOLLOW_EVERY_in_behavior_expr2079 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            112,
            116,
            117,
        ]
    )
    FOLLOW_test_in_behavior_expr2083 = frozenset([36, 112])
    FOLLOW_FRAMES_in_behavior_expr2089 = frozenset([1])
    FOLLOW_TIME_in_behavior_expr2093 = frozenset([1])
    FOLLOW_COLON_in_behavior_block2115 = frozenset([72])
    FOLLOW_NEWLINE_in_behavior_block2117 = frozenset([49])
    FOLLOW_INDENT_in_behavior_block2119 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_aug_expr_stmt_in_behavior_block2124 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_edit_stmt_in_behavior_block2128 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_DEDENT_in_behavior_block2132 = frozenset([1])
    FOLLOW_testlist_in_expr_stmt2153 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_expr_stmt2158 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_ASSIGN_in_expr_stmt2162 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_testlist_in_expr_stmt2168 = frozenset([72])
    FOLLOW_fetch_expr_in_expr_stmt2172 = frozenset([72])
    FOLLOW_NEWLINE_in_expr_stmt2175 = frozenset([1])
    FOLLOW_testlist_in_aug_expr_stmt2213 = frozenset([5, 7])
    FOLLOW_AUG_ASSIGN_in_aug_expr_stmt2225 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt2230 = frozenset([72])
    FOLLOW_fetch_expr_in_aug_expr_stmt2234 = frozenset([72])
    FOLLOW_NEWLINE_in_aug_expr_stmt2237 = frozenset([1])
    FOLLOW_ASSIGN_in_aug_expr_stmt2269 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_testlist_in_aug_expr_stmt2284 = frozenset([72])
    FOLLOW_fetch_expr_in_aug_expr_stmt2288 = frozenset([72])
    FOLLOW_NEWLINE_in_aug_expr_stmt2291 = frozenset([1])
    FOLLOW_model_expr_in_aug_expr_stmt2326 = frozenset([1])
    FOLLOW_model_expr_in_aug_expr_stmt2360 = frozenset([1])
    FOLLOW_create_expr_in_model_expr2377 = frozenset([1])
    FOLLOW_instantiate_expr_in_model_expr2382 = frozenset([1])
    FOLLOW_get_expr_in_model_expr2387 = frozenset([1])
    FOLLOW_group_expr_in_model_expr2392 = frozenset([1])
    FOLLOW_FETCH_in_fetch_expr2406 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_fetch_expr2410 = frozenset([37])
    FOLLOW_FROM_in_fetch_expr2412 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_fetch_expr2416 = frozenset([1, 59, 66, 89])
    FOLLOW_MATCH_in_fetch_expr2419 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_fetch_expr2423 = frozenset([1, 59, 89])
    FOLLOW_LIMIT_in_fetch_expr2428 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_fetch_expr2432 = frozenset([1, 89])
    FOLLOW_RECURSIVE_in_fetch_expr2436 = frozenset([1])
    FOLLOW_or_test_in_test2487 = frozenset([1, 47])
    FOLLOW_IF_in_test2490 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_or_test_in_test2494 = frozenset([26])
    FOLLOW_ELSE_in_test2496 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_test2500 = frozenset([1])
    FOLLOW_or_test_in_test_nocond2542 = frozenset([1])
    FOLLOW_and_test_in_or_test2564 = frozenset([1, 80])
    FOLLOW_OR_in_or_test2567 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_and_test_in_or_test2571 = frozenset([1, 80])
    FOLLOW_not_test_in_and_test2594 = frozenset([1, 4])
    FOLLOW_AND_in_and_test2597 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_not_test_in_and_test2601 = frozenset([1, 4])
    FOLLOW_NOT_in_not_test2622 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_not_test_in_not_test2626 = frozenset([1])
    FOLLOW_comparison_in_not_test2652 = frozenset([1])
    FOLLOW_expr_in_comparison2666 = frozenset([1, 27, 40, 41, 48, 53, 64, 65, 75, 76])
    FOLLOW_comp_op_in_comparison2669 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_expr_in_comparison2673 = frozenset([1, 27, 40, 41, 48, 53, 64, 65, 75, 76])
    FOLLOW_LT_in_comp_op2700 = frozenset([1])
    FOLLOW_GT_in_comp_op2704 = frozenset([1])
    FOLLOW_EQUALS_in_comp_op2708 = frozenset([1])
    FOLLOW_GT_EQ_in_comp_op2712 = frozenset([1])
    FOLLOW_LT_EQ_in_comp_op2716 = frozenset([1])
    FOLLOW_NOT_EQ_in_comp_op2720 = frozenset([1])
    FOLLOW_IN_in_comp_op2724 = frozenset([1])
    FOLLOW_NOT_in_comp_op2728 = frozenset([48])
    FOLLOW_IN_in_comp_op2730 = frozenset([1])
    FOLLOW_IS_in_comp_op2734 = frozenset([1])
    FOLLOW_IS_in_comp_op2738 = frozenset([75])
    FOLLOW_NOT_in_comp_op2740 = frozenset([1])
    FOLLOW_xor_expr_in_expr2757 = frozenset([1, 12])
    FOLLOW_BIT_OR_in_expr2760 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_xor_expr_in_expr2764 = frozenset([1, 12])
    FOLLOW_and_expr_in_xor_expr2787 = frozenset([1, 122])
    FOLLOW_XOR_in_xor_expr2790 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_and_expr_in_xor_expr2794 = frozenset([1, 122])
    FOLLOW_shift_expr_in_and_expr2817 = frozenset([1, 10])
    FOLLOW_BIT_AND_in_and_expr2820 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_shift_expr_in_and_expr2824 = frozenset([1, 10])
    FOLLOW_arith_expr_in_shift_expr2845 = frozenset([1, 63, 93])
    FOLLOW_LSHIFT_in_shift_expr2851 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_RSHIFT_in_shift_expr2855 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_arith_expr_in_shift_expr2860 = frozenset([1, 63, 93])
    FOLLOW_term_in_arith_expr2886 = frozenset([1, 68, 83])
    FOLLOW_PLUS_in_arith_expr2892 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_MINUS_in_arith_expr2896 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_term_in_arith_expr2901 = frozenset([1, 68, 83])
    FOLLOW_factor_in_term2933 = frozenset([1, 22, 44, 69, 70])
    FOLLOW_MUL_in_term2939 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_DIV_in_term2943 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_MOD_in_term2947 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_IDIV_in_term2951 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_factor_in_term2956 = frozenset([1, 22, 44, 69, 70])
    FOLLOW_PLUS_in_factor2987 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_MINUS_in_factor2991 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_BIT_NOT_in_factor2995 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_factor_in_factor3000 = frozenset([1])
    FOLLOW_power_in_factor3030 = frozenset([1])
    FOLLOW_atom_expr_in_power3047 = frozenset([1, 85])
    FOLLOW_POWER_in_power3050 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_factor_in_power3052 = frozenset([1])
    FOLLOW_atom_in_atom_expr3077 = frozenset([1, 23, 55])
    FOLLOW_trailer_in_atom_expr3082 = frozenset([1, 23, 55])
    FOLLOW_LPAREN_in_atom3107 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_atom3111 = frozenset([92])
    FOLLOW_RPAREN_in_atom3113 = frozenset([1])
    FOLLOW_LBRACK_in_atom3128 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            88,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_testlist_comp_in_atom3130 = frozenset([88])
    FOLLOW_RBRACK_in_atom3133 = frozenset([1])
    FOLLOW_LT_in_atom3148 = frozenset(
        [11, 21, 31, 33, 40, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_vector_comp_in_atom3150 = frozenset([40])
    FOLLOW_GT_in_atom3153 = frozenset([1])
    FOLLOW_LBRACE_in_atom3168 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            87,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_dict_or_set_maker_in_atom3170 = frozenset([87])
    FOLLOW_RBRACE_in_atom3173 = frozenset([1])
    FOLLOW_LEN_in_atom3188 = frozenset([62])
    FOLLOW_LPAREN_in_atom3190 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_atom3194 = frozenset([92])
    FOLLOW_RPAREN_in_atom3196 = frozenset([1])
    FOLLOW_name_in_atom3211 = frozenset([1])
    FOLLOW_SETTING_ID_in_atom3221 = frozenset([1])
    FOLLOW_DISTRIBUTION_in_atom3237 = frozenset([62])
    FOLLOW_LPAREN_in_atom3239 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_arglist_in_atom3241 = frozenset([92])
    FOLLOW_RPAREN_in_atom3243 = frozenset([1])
    FOLLOW_INTEGER_in_atom3263 = frozenset([1])
    FOLLOW_FLOAT_NUMBER_in_atom3273 = frozenset([1])
    FOLLOW_STRING_in_atom3283 = frozenset([1])
    FOLLOW_NONE_in_atom3294 = frozenset([1])
    FOLLOW_TRUE_in_atom3306 = frozenset([1])
    FOLLOW_FALSE_in_atom3318 = frozenset([1])
    FOLLOW_ID_in_name3338 = frozenset([1])
    FOLLOW_UNDERSCORE_in_name3348 = frozenset([1])
    FOLLOW_test_in_testlist_comp3367 = frozenset([1, 16, 34, 86])
    FOLLOW_comp_for_in_testlist_comp3371 = frozenset([1])
    FOLLOW_COMMA_in_testlist_comp3411 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_testlist_comp3415 = frozenset([1, 16])
    FOLLOW_RANGE_in_testlist_comp3451 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_testlist_comp3455 = frozenset([1, 108])
    FOLLOW_STEP_in_testlist_comp3458 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_testlist_comp3462 = frozenset([1])
    FOLLOW_expr_in_vector_comp3511 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp3513 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_expr_in_vector_comp3517 = frozenset([16])
    FOLLOW_COMMA_in_vector_comp3519 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_expr_in_vector_comp3523 = frozenset([1])
    FOLLOW_LBRACK_in_trailer3557 = frozenset(
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
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_subscriptlist_in_trailer3559 = frozenset([88])
    FOLLOW_RBRACK_in_trailer3561 = frozenset([1])
    FOLLOW_DOT_in_trailer3589 = frozenset([43, 117])
    FOLLOW_name_in_trailer3591 = frozenset([1])
    FOLLOW_argument_in_arglist3615 = frozenset([1, 16])
    FOLLOW_COMMA_in_arglist3618 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_argument_in_arglist3622 = frozenset([1, 16])
    FOLLOW_test_in_argument3647 = frozenset([1, 5])
    FOLLOW_ASSIGN_in_argument3650 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_argument3654 = frozenset([1])
    FOLLOW_subscript__in_subscriptlist3679 = frozenset([1, 16])
    FOLLOW_COMMA_in_subscriptlist3682 = frozenset(
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
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_subscript__in_subscriptlist3686 = frozenset([1, 16])
    FOLLOW_test_in_subscript_3709 = frozenset([1, 15])
    FOLLOW_COLON_in_subscript_3712 = frozenset(
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
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_test_in_subscript_3717 = frozenset([1, 15])
    FOLLOW_sliceop_in_subscript_3724 = frozenset([1])
    FOLLOW_COLON_in_subscript_3770 = frozenset(
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
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_test_in_subscript_3775 = frozenset([1, 15])
    FOLLOW_sliceop_in_subscript_3782 = frozenset([1])
    FOLLOW_COLON_in_sliceop3817 = frozenset(
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
            62,
            64,
            68,
            73,
            75,
            83,
            100,
            110,
            116,
            117,
        ]
    )
    FOLLOW_test_in_sliceop3819 = frozenset([1])
    FOLLOW_expr_in_exprlist3839 = frozenset([1, 16])
    FOLLOW_COMMA_in_exprlist3842 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_expr_in_exprlist3846 = frozenset([1, 16])
    FOLLOW_test_in_testlist3866 = frozenset([1, 16])
    FOLLOW_COMMA_in_testlist3869 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_testlist3873 = frozenset([1, 16])
    FOLLOW_test_in_dict_or_set_maker3894 = frozenset([1, 15, 16, 34])
    FOLLOW_COLON_in_dict_or_set_maker3898 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_dict_or_set_maker3902 = frozenset([1, 16, 34])
    FOLLOW_comp_for_in_dict_or_set_maker3907 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker3966 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_dict_or_set_maker3970 = frozenset([15])
    FOLLOW_COLON_in_dict_or_set_maker3972 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_dict_or_set_maker3976 = frozenset([1, 16])
    FOLLOW_comp_for_in_dict_or_set_maker4014 = frozenset([1])
    FOLLOW_COMMA_in_dict_or_set_maker4052 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_in_dict_or_set_maker4056 = frozenset([1, 16])
    FOLLOW_comp_for_in_comp_iter4097 = frozenset([1])
    FOLLOW_comp_if_in_comp_iter4101 = frozenset([1])
    FOLLOW_FOR_in_comp_for4114 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 83, 100, 110, 116, 117]
    )
    FOLLOW_exprlist_in_comp_for4116 = frozenset([48])
    FOLLOW_IN_in_comp_for4118 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_or_test_in_comp_for4120 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_for4122 = frozenset([1])
    FOLLOW_IF_in_comp_if4151 = frozenset(
        [11, 21, 31, 33, 43, 51, 54, 55, 56, 62, 64, 68, 73, 75, 83, 100, 110, 116, 117]
    )
    FOLLOW_test_nocond_in_comp_if4153 = frozenset([1, 34, 47])
    FOLLOW_comp_iter_in_comp_if4155 = frozenset([1])


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain

    main = ParserMain("YarcParserLexer", YarcParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
