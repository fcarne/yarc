# $ANTLR 3.5.1 /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g 2023-05-09 00:48:04

import sys

from antlr3 import (
    DEFAULT_CHANNEL,
    DFA,
    BaseRecognizer,
    EarlyExitException,
    MismatchedSetException,
    NoViableAltException,
    RecognizerSharedState,
    Token,
)

if __name__ is not None and "." in __name__:
    from .YarcLexerBase import YarcLexerBase
else:
    from YarcLexerBase import YarcLexerBase


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


class YarcLexer(YarcLexerBase):
    grammarFileName = "/media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa23 = self.DFA23(
            self,
            23,
            eot=self.DFA23_eot,
            eof=self.DFA23_eof,
            min=self.DFA23_min,
            max=self.DFA23_max,
            accept=self.DFA23_accept,
            special=self.DFA23_special,
            transition=self.DFA23_transition,
        )

        self.dfa33 = self.DFA33(
            self,
            33,
            eot=self.DFA33_eot,
            eof=self.DFA33_eof,
            min=self.DFA33_min,
            max=self.DFA33_max,
            accept=self.DFA33_accept,
            special=self.DFA33_special,
            transition=self.DFA33_transition,
        )

        self.dfa34 = self.DFA34(
            self,
            34,
            eot=self.DFA34_eot,
            eof=self.DFA34_eof,
            min=self.DFA34_min,
            max=self.DFA34_max,
            accept=self.DFA34_accept,
            special=self.DFA34_special,
            transition=self.DFA34_transition,
        )

        self.dfa44 = self.DFA44(
            self,
            44,
            eot=self.DFA44_eot,
            eof=self.DFA44_eof,
            min=self.DFA44_min,
            max=self.DFA44_max,
            accept=self.DFA44_accept,
            special=self.DFA44_special,
            transition=self.DFA44_transition,
        )

    # $ANTLR start "SCENARIO"
    def mSCENARIO(
        self,
    ):
        try:
            _type = SCENARIO
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:22:10: ( 'scenario' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:22:12: 'scenario'
            self.match("scenario")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SCENARIO"

    # $ANTLR start "SETTINGS"
    def mSETTINGS(
        self,
    ):
        try:
            _type = SETTINGS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:23:10: ( 'settings' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:23:12: 'settings'
            self.match("settings")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SETTINGS"

    # $ANTLR start "STAGE"
    def mSTAGE(
        self,
    ):
        try:
            _type = STAGE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:24:10: ( 'stage' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:24:12: 'stage'
            self.match("stage")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STAGE"

    # $ANTLR start "WRITERS"
    def mWRITERS(
        self,
    ):
        try:
            _type = WRITERS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:25:10: ( 'writers' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:25:12: 'writers'
            self.match("writers")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WRITERS"

    # $ANTLR start "SHAPES"
    def mSHAPES(
        self,
    ):
        try:
            _type = SHAPES
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:28:18: ( 'Plane' | 'Cube' | 'Cone' | 'Torus' )
            alt1 = 4
            LA1 = self.input.LA(1)
            if LA1 in {80}:
                alt1 = 1
            elif LA1 in {67}:
                LA1_2 = self.input.LA(2)

                if LA1_2 == 117:
                    alt1 = 2
                elif LA1_2 == 111:
                    alt1 = 3
                else:
                    nvae = NoViableAltException("", 1, 2, self.input)

                    raise nvae

            elif LA1 in {84}:
                alt1 = 4
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae

            if alt1 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:28:20: 'Plane'
                self.match("Plane")

            elif alt1 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:28:30: 'Cube'
                self.match("Cube")

            elif alt1 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:28:39: 'Cone'
                self.match("Cone")

            elif alt1 == 4:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:28:48: 'Torus'
                self.match("Torus")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHAPES"

    # $ANTLR start "SHAPES_OR_LIGHTS"
    def mSHAPES_OR_LIGHTS(
        self,
    ):
        try:
            _type = SHAPES_OR_LIGHTS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:29:18: ( 'Sphere' | 'Cylinder' | 'Disk' )
            alt2 = 3
            LA2 = self.input.LA(1)
            if LA2 in {83}:
                alt2 = 1
            elif LA2 in {67}:
                alt2 = 2
            elif LA2 in {68}:
                alt2 = 3
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae

            if alt2 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:29:20: 'Sphere'
                self.match("Sphere")

            elif alt2 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:29:31: 'Cylinder'
                self.match("Cylinder")

            elif alt2 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:29:44: 'Disk'
                self.match("Disk")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHAPES_OR_LIGHTS"

    # $ANTLR start "CAMERA"
    def mCAMERA(
        self,
    ):
        try:
            _type = CAMERA
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:30:18: ( 'Camera' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:30:20: 'Camera'
            self.match("Camera")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CAMERA"

    # $ANTLR start "LIGHT"
    def mLIGHT(
        self,
    ):
        try:
            _type = LIGHT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:31:18: ( 'Light' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:31:20: 'Light'
            self.match("Light")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LIGHT"

    # $ANTLR start "LIGHT_TYPE"
    def mLIGHT_TYPE(
        self,
    ):
        try:
            _type = LIGHT_TYPE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:32:18: ( 'Rect' | 'Dome' | 'Distant' )
            alt3 = 3
            LA3_0 = self.input.LA(1)

            if LA3_0 == 82:
                alt3 = 1
            elif LA3_0 == 68:
                LA3_2 = self.input.LA(2)

                if LA3_2 == 111:
                    alt3 = 2
                elif LA3_2 == 105:
                    alt3 = 3
                else:
                    nvae = NoViableAltException("", 3, 2, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae

            if alt3 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:32:20: 'Rect'
                self.match("Rect")

            elif alt3 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:32:29: 'Dome'
                self.match("Dome")

            elif alt3 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:32:38: 'Distant'
                self.match("Distant")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LIGHT_TYPE"

    # $ANTLR start "STEREO"
    def mSTEREO(
        self,
    ):
        try:
            _type = STEREO
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:33:18: ( 'Stereo' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:33:20: 'Stereo'
            self.match("Stereo")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STEREO"

    # $ANTLR start "MATERIAL"
    def mMATERIAL(
        self,
    ):
        try:
            _type = MATERIAL
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:34:18: ( 'Material' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:34:20: 'Material'
            self.match("Material")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MATERIAL"

    # $ANTLR start "TIMELINE"
    def mTIMELINE(
        self,
    ):
        try:
            _type = TIMELINE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:35:18: ( 'Timeline' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:35:20: 'Timeline'
            self.match("Timeline")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TIMELINE"

    # $ANTLR start "OPEN"
    def mOPEN(
        self,
    ):
        try:
            _type = OPEN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:38:13: ( 'open' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:38:15: 'open'
            self.match("open")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OPEN"

    # $ANTLR start "CREATE"
    def mCREATE(
        self,
    ):
        try:
            _type = CREATE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:39:13: ( 'create' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:39:15: 'create'
            self.match("create")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CREATE"

    # $ANTLR start "GROUP"
    def mGROUP(
        self,
    ):
        try:
            _type = GROUP
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:40:13: ( 'group' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:40:15: 'group'
            self.match("group")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GROUP"

    # $ANTLR start "INSTANTIATE"
    def mINSTANTIATE(
        self,
    ):
        try:
            _type = INSTANTIATE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:41:13: ( 'instantiate' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:41:15: 'instantiate'
            self.match("instantiate")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INSTANTIATE"

    # $ANTLR start "GET"
    def mGET(
        self,
    ):
        try:
            _type = GET
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:42:13: ( 'get' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:42:15: 'get'
            self.match("get")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GET"

    # $ANTLR start "EDIT"
    def mEDIT(
        self,
    ):
        try:
            _type = EDIT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:43:13: ( 'edit' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:43:15: 'edit'
            self.match("edit")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EDIT"

    # $ANTLR start "FETCH"
    def mFETCH(
        self,
    ):
        try:
            _type = FETCH
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:47:11: ( 'fetch' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:47:13: 'fetch'
            self.match("fetch")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FETCH"

    # $ANTLR start "MATCH"
    def mMATCH(
        self,
    ):
        try:
            _type = MATCH
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:48:11: ( 'match' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:48:13: 'match'
            self.match("match")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MATCH"

    # $ANTLR start "LIMIT"
    def mLIMIT(
        self,
    ):
        try:
            _type = LIMIT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:49:11: ( 'limit' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:49:13: 'limit'
            self.match("limit")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LIMIT"

    # $ANTLR start "RECURSIVE"
    def mRECURSIVE(
        self,
    ):
        try:
            _type = RECURSIVE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:50:11: ( 'recursive' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:50:13: 'recursive'
            self.match("recursive")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RECURSIVE"

    # $ANTLR start "TRANSLATE"
    def mTRANSLATE(
        self,
    ):
        try:
            _type = TRANSLATE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:53:15: ( 'translate' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:53:17: 'translate'
            self.match("translate")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRANSLATE"

    # $ANTLR start "CAM_TRANSLATE"
    def mCAM_TRANSLATE(
        self,
    ):
        try:
            _type = CAM_TRANSLATE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:54:15: ( 'camera_translate' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:54:17: 'camera_translate'
            self.match("camera_translate")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CAM_TRANSLATE"

    # $ANTLR start "ROTATE"
    def mROTATE(
        self,
    ):
        try:
            _type = ROTATE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:55:15: ( 'rotate' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:55:17: 'rotate'
            self.match("rotate")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROTATE"

    # $ANTLR start "SCALE"
    def mSCALE(
        self,
    ):
        try:
            _type = SCALE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:56:15: ( 'scale' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:56:17: 'scale'
            self.match("scale")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SCALE"

    # $ANTLR start "SEMANTICS"
    def mSEMANTICS(
        self,
    ):
        try:
            _type = SEMANTICS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:57:15: ( 'semantics' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:57:17: 'semantics'
            self.match("semantics")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMANTICS"

    # $ANTLR start "VISIBLE"
    def mVISIBLE(
        self,
    ):
        try:
            _type = VISIBLE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:58:15: ( 'visible' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:58:17: 'visible'
            self.match("visible")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VISIBLE"

    # $ANTLR start "SIZE"
    def mSIZE(
        self,
    ):
        try:
            _type = SIZE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:59:15: ( 'size' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:59:17: 'size'
            self.match("size")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SIZE"

    # $ANTLR start "LOOK_AT"
    def mLOOK_AT(
        self,
    ):
        try:
            _type = LOOK_AT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:60:15: ( 'look_at' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:60:17: 'look_at'
            self.match("look_at")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOOK_AT"

    # $ANTLR start "UP_AXIS"
    def mUP_AXIS(
        self,
    ):
        try:
            _type = UP_AXIS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:61:15: ( 'up_axis' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:61:17: 'up_axis'
            self.match("up_axis")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UP_AXIS"

    # $ANTLR start "AXIS"
    def mAXIS(
        self,
    ):
        try:
            _type = AXIS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:62:15: ( 'x' | 'y' | 'z' | 'X' | 'Y' | 'Z' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if self.input.LA(1) in {88, 89, 90, 120, 121, 122}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AXIS"

    # $ANTLR start "ORDER"
    def mORDER(
        self,
    ):
        try:
            _type = ORDER
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:63:15: ( AXIS AXIS AXIS )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:63:17: AXIS AXIS AXIS
            self.mAXIS()

            self.mAXIS()

            self.mAXIS()

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ORDER"

    # $ANTLR start "SCATTER"
    def mSCATTER(
        self,
    ):
        try:
            _type = SCATTER
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:66:12: ( 'scatter_' ( '2d' | '3d' ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:66:14: 'scatter_' ( '2d' | '3d' )
            self.match("scatter_")

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:66:25: ( '2d' | '3d' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if LA4_0 == 50:
                alt4 = 1
            elif LA4_0 == 51:
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:66:26: '2d'
                self.match("2d")

            elif alt4 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:66:33: '3d'
                self.match("3d")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SCATTER"

    # $ANTLR start "ROT_AROUND"
    def mROT_AROUND(
        self,
    ):
        try:
            _type = ROT_AROUND
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:67:12: ( 'rotate_around' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:67:14: 'rotate_around'
            self.match("rotate_around")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROT_AROUND"

    # $ANTLR start "PHYSICS"
    def mPHYSICS(
        self,
    ):
        try:
            _type = PHYSICS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:68:12: ( 'collider' | 'kinematics' | 'rigid_body' | 'physics_material' )
            alt5 = 4
            LA5 = self.input.LA(1)
            if LA5 in {99}:
                alt5 = 1
            elif LA5 in {107}:
                alt5 = 2
            elif LA5 in {114}:
                alt5 = 3
            elif LA5 in {112}:
                alt5 = 4
            else:
                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae

            if alt5 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:68:14: 'collider'
                self.match("collider")

            elif alt5 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:68:27: 'kinematics'
                self.match("kinematics")

            elif alt5 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:68:42: 'rigid_body'
                self.match("rigid_body")

            elif alt5 == 4:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:68:57: 'physics_material'
                self.match("physics_material")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PHYSICS"

    # $ANTLR start "EVERY"
    def mEVERY(
        self,
    ):
        try:
            _type = EVERY
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:71:8: ( 'every' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:71:10: 'every'
            self.match("every")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EVERY"

    # $ANTLR start "FRAMES"
    def mFRAMES(
        self,
    ):
        try:
            _type = FRAMES
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:72:8: ( 'frame' ( 's' )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:72:10: 'frame' ( 's' )?
            self.match("frame")

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:72:18: ( 's' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if LA6_0 == 115:
                alt6 = 1
            if alt6 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:72:18: 's'
                self.match(115)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FRAMES"

    # $ANTLR start "TIME"
    def mTIME(
        self,
    ):
        try:
            _type = TIME
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:73:8: ( 'sec' ( 'ond' ( 's' )? )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:73:10: 'sec' ( 'ond' ( 's' )? )?
            self.match("sec")

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:73:16: ( 'ond' ( 's' )? )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if LA8_0 == 111:
                alt8 = 1
            if alt8 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:73:17: 'ond' ( 's' )?
                self.match("ond")

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:73:23: ( 's' )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if LA7_0 == 115:
                    alt7 = 1
                if alt7 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:73:23: 's'
                    self.match(115)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TIME"

    # $ANTLR start "DISTRIBUTION"
    def mDISTRIBUTION(
        self,
    ):
        try:
            _type = DISTRIBUTION
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:76:14: ( 'Uniform' | 'Normal' | 'Choice' | 'Sequence' | 'LogUniform' )
            alt9 = 5
            LA9 = self.input.LA(1)
            if LA9 in {85}:
                alt9 = 1
            elif LA9 in {78}:
                alt9 = 2
            elif LA9 in {67}:
                alt9 = 3
            elif LA9 in {83}:
                alt9 = 4
            elif LA9 in {76}:
                alt9 = 5
            else:
                nvae = NoViableAltException("", 9, 0, self.input)

                raise nvae

            if alt9 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:76:16: 'Uniform'
                self.match("Uniform")

            elif alt9 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:76:28: 'Normal'
                self.match("Normal")

            elif alt9 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:76:39: 'Choice'
                self.match("Choice")

            elif alt9 == 4:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:76:50: 'Sequence'
                self.match("Sequence")

            elif alt9 == 5:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:76:63: 'LogUniform'
                self.match("LogUniform")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DISTRIBUTION"

    # $ANTLR start "SNIPPET"
    def mSNIPPET(
        self,
    ):
        try:
            _type = SNIPPET
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:79:9: ( NESTED_CODE ( NEWLINE )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:79:11: NESTED_CODE ( NEWLINE )?
            self.mNESTED_CODE()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:79:23: ( NEWLINE )?
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if LA10_0 in {10, 12, 13}:
                alt10 = 1
            if alt10 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:79:23: NEWLINE
                self.mNEWLINE()

            # action start
            print("FOUND SNIPPET CODE!")
            # action end

            # action start
            self.skip()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SNIPPET"

    # $ANTLR start "NESTED_CODE"
    def mNESTED_CODE(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:81:21: ( LBRACE LBRACE ( options {k=2; greedy=false; } : NESTED_CODE | . )* RBRACE RBRACE )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:82:3: LBRACE LBRACE ( options {k=2; greedy=false; } : NESTED_CODE | . )* RBRACE RBRACE
            self.mLBRACE()

            self.mLBRACE()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:83:5: ( options {k=2; greedy=false; } : NESTED_CODE | . )*
            while True:  # loop11
                alt11 = 3
                LA11_0 = self.input.LA(1)

                if LA11_0 == 125:
                    alt11 = 3
                elif LA11_0 == 123:
                    alt11 = 1
                elif (
                    (0 <= LA11_0 <= 122) or (126 <= LA11_0 <= 65535) or LA11_0 in {124}
                ):
                    alt11 = 2

                if alt11 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:83:37: NESTED_CODE
                    self.mNESTED_CODE()

                elif alt11 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:83:51: .
                    self.matchAny()

                else:
                    break  # loop11

            self.mRBRACE()

            self.mRBRACE()

        finally:
            pass

    # $ANTLR end "NESTED_CODE"

    # $ANTLR start "TO"
    def mTO(
        self,
    ):
        try:
            _type = TO
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:88:4: ( 'to' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:88:6: 'to'
            self.match("to")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TO"

    # $ANTLR start "ON"
    def mON(
        self,
    ):
        try:
            _type = ON
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:89:4: ( 'on' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:89:6: 'on'
            self.match("on")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ON"

    # $ANTLR start "AT"
    def mAT(
        self,
    ):
        try:
            _type = AT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:90:4: ( 'at' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:90:6: 'at'
            self.match("at")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT"

    # $ANTLR start "AND"
    def mAND(
        self,
    ):
        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:97:12: ( 'and' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:97:14: 'and'
            self.match("and")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND"

    # $ANTLR start "ELSE"
    def mELSE(
        self,
    ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:98:12: ( 'else' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:98:14: 'else'
            self.match("else")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELSE"

    # $ANTLR start "FALSE"
    def mFALSE(
        self,
    ):
        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:99:12: ( 'false' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:99:14: 'false'
            self.match("false")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FALSE"

    # $ANTLR start "FOR"
    def mFOR(
        self,
    ):
        try:
            _type = FOR
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:100:12: ( 'for' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:100:14: 'for'
            self.match("for")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FOR"

    # $ANTLR start "FROM"
    def mFROM(
        self,
    ):
        try:
            _type = FROM
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:101:12: ( 'from' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:101:14: 'from'
            self.match("from")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FROM"

    # $ANTLR start "IF"
    def mIF(
        self,
    ):
        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:102:12: ( 'if' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:102:14: 'if'
            self.match("if")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IF"

    # $ANTLR start "IN"
    def mIN(
        self,
    ):
        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:103:12: ( 'in' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:103:14: 'in'
            self.match("in")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IN"

    # $ANTLR start "IS"
    def mIS(
        self,
    ):
        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:104:12: ( 'is' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:104:14: 'is'
            self.match("is")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IS"

    # $ANTLR start "LEN"
    def mLEN(
        self,
    ):
        try:
            _type = LEN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:105:12: ( 'len' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:105:14: 'len'
            self.match("len")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LEN"

    # $ANTLR start "NONE"
    def mNONE(
        self,
    ):
        try:
            _type = NONE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:106:12: ( 'none' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:106:14: 'none'
            self.match("none")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NONE"

    # $ANTLR start "NOT"
    def mNOT(
        self,
    ):
        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:107:12: ( 'not' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:107:14: 'not'
            self.match("not")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT"

    # $ANTLR start "OR"
    def mOR(
        self,
    ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:108:12: ( 'or' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:108:14: 'or'
            self.match("or")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"

    # $ANTLR start "STEP"
    def mSTEP(
        self,
    ):
        try:
            _type = STEP
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:109:12: ( 'step' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:109:14: 'step'
            self.match("step")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STEP"

    # $ANTLR start "TRUE"
    def mTRUE(
        self,
    ):
        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:110:12: ( 'true' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:110:14: 'true'
            self.match("true")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRUE"

    # $ANTLR start "UNDERSCORE"
    def mUNDERSCORE(
        self,
    ):
        try:
            _type = UNDERSCORE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:111:12: ( '_' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:111:14: '_'
            self.match(95)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNDERSCORE"

    # $ANTLR start "DOT"
    def mDOT(
        self,
    ):
        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:114:10: ( '.' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:114:12: '.'
            self.match(46)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"

    # $ANTLR start "RANGE"
    def mRANGE(
        self,
    ):
        try:
            _type = RANGE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:115:10: ( '..' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:115:12: '..'
            self.match("..")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RANGE"

    # $ANTLR start "ELLIPSIS"
    def mELLIPSIS(
        self,
    ):
        try:
            _type = ELLIPSIS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:116:10: ( '...' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:116:12: '...'
            self.match("...")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELLIPSIS"

    # $ANTLR start "COMMA"
    def mCOMMA(
        self,
    ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:117:10: ( ',' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:117:12: ','
            self.match(44)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"

    # $ANTLR start "COLON"
    def mCOLON(
        self,
    ):
        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:118:10: ( ':' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:118:12: ':'
            self.match(58)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COLON"

    # $ANTLR start "SEMI"
    def mSEMI(
        self,
    ):
        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:119:10: ( ';' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:119:12: ';'
            self.match(59)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMI"

    # $ANTLR start "ASSIGN"
    def mASSIGN(
        self,
    ):
        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:121:9: ( '=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:121:11: '='
            self.match(61)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ASSIGN"

    # $ANTLR start "BIT_OR"
    def mBIT_OR(
        self,
    ):
        try:
            _type = BIT_OR
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:122:9: ( '|' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:122:11: '|'
            self.match(124)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BIT_OR"

    # $ANTLR start "XOR"
    def mXOR(
        self,
    ):
        try:
            _type = XOR
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:123:9: ( '^' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:123:11: '^'
            self.match(94)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "XOR"

    # $ANTLR start "BIT_AND"
    def mBIT_AND(
        self,
    ):
        try:
            _type = BIT_AND
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:124:9: ( '&' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:124:11: '&'
            self.match(38)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BIT_AND"

    # $ANTLR start "BIT_NOT"
    def mBIT_NOT(
        self,
    ):
        try:
            _type = BIT_NOT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:125:9: ( '~' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:125:11: '~'
            self.match(126)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BIT_NOT"

    # $ANTLR start "LSHIFT"
    def mLSHIFT(
        self,
    ):
        try:
            _type = LSHIFT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:126:9: ( '<<' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:126:11: '<<'
            self.match("<<")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LSHIFT"

    # $ANTLR start "RSHIFT"
    def mRSHIFT(
        self,
    ):
        try:
            _type = RSHIFT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:127:9: ( '>>' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:127:11: '>>'
            self.match(">>")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RSHIFT"

    # $ANTLR start "PLUS"
    def mPLUS(
        self,
    ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:128:9: ( '+' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:128:11: '+'
            self.match(43)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"

    # $ANTLR start "MINUS"
    def mMINUS(
        self,
    ):
        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:129:9: ( '-' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:129:11: '-'
            self.match(45)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS"

    # $ANTLR start "MUL"
    def mMUL(
        self,
    ):
        try:
            _type = MUL
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:130:8: ( '*' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:130:10: '*'
            self.match(42)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MUL"

    # $ANTLR start "DIV"
    def mDIV(
        self,
    ):
        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:131:9: ( '/' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:131:11: '/'
            self.match(47)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIV"

    # $ANTLR start "MOD"
    def mMOD(
        self,
    ):
        try:
            _type = MOD
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:132:9: ( '%' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:132:11: '%'
            self.match(37)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOD"

    # $ANTLR start "IDIV"
    def mIDIV(
        self,
    ):
        try:
            _type = IDIV
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:133:9: ( '//' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:133:11: '//'
            self.match("//")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IDIV"

    # $ANTLR start "POWER"
    def mPOWER(
        self,
    ):
        try:
            _type = POWER
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:134:9: ( '**' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:134:11: '**'
            self.match("**")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "POWER"

    # $ANTLR start "LPAREN"
    def mLPAREN(
        self,
    ):
        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:136:8: ( '(' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:136:10: '('
            self.match(40)

            # action start
            self.openBrace()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LPAREN"

    # $ANTLR start "RPAREN"
    def mRPAREN(
        self,
    ):
        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:137:8: ( ')' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:137:10: ')'
            self.match(41)

            # action start
            self.closeBrace()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RPAREN"

    # $ANTLR start "LBRACK"
    def mLBRACK(
        self,
    ):
        try:
            _type = LBRACK
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:138:8: ( '[' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:138:10: '['
            self.match(91)

            # action start
            self.openBrace()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LBRACK"

    # $ANTLR start "RBRACK"
    def mRBRACK(
        self,
    ):
        try:
            _type = RBRACK
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:139:8: ( ']' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:139:10: ']'
            self.match(93)

            # action start
            self.closeBrace()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RBRACK"

    # $ANTLR start "LBRACE"
    def mLBRACE(
        self,
    ):
        try:
            _type = LBRACE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:140:8: ( '{' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:140:10: '{'
            self.match(123)

            # action start
            self.openBrace()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LBRACE"

    # $ANTLR start "RBRACE"
    def mRBRACE(
        self,
    ):
        try:
            _type = RBRACE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:141:8: ( '}' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:141:10: '}'
            self.match(125)

            # action start
            self.closeBrace()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RBRACE"

    # $ANTLR start "LT"
    def mLT(
        self,
    ):
        try:
            _type = LT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:143:8: ( '<' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:143:10: '<'
            self.match(60)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LT"

    # $ANTLR start "GT"
    def mGT(
        self,
    ):
        try:
            _type = GT
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:144:8: ( '>' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:144:10: '>'
            self.match(62)

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GT"

    # $ANTLR start "EQUALS"
    def mEQUALS(
        self,
    ):
        try:
            _type = EQUALS
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:145:8: ( '==' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:145:10: '=='
            self.match("==")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQUALS"

    # $ANTLR start "GT_EQ"
    def mGT_EQ(
        self,
    ):
        try:
            _type = GT_EQ
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:146:8: ( '>=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:146:10: '>='
            self.match(">=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GT_EQ"

    # $ANTLR start "LT_EQ"
    def mLT_EQ(
        self,
    ):
        try:
            _type = LT_EQ
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:147:8: ( '<=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:147:10: '<='
            self.match("<=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LT_EQ"

    # $ANTLR start "NOT_EQ"
    def mNOT_EQ(
        self,
    ):
        try:
            _type = NOT_EQ
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:148:8: ( '!=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:148:10: '!='
            self.match("!=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT_EQ"

    # $ANTLR start "AUG_ASSIGN"
    def mAUG_ASSIGN(
        self,
    ):
        try:
            _type = AUG_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:11: ( '+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=' | '**=' | '//=' )
            alt12 = 12
            LA12 = self.input.LA(1)
            if LA12 in {43}:
                alt12 = 1
            elif LA12 in {45}:
                alt12 = 2
            elif LA12 in {42}:
                LA12_3 = self.input.LA(2)

                if LA12_3 == 61:
                    alt12 = 3
                elif LA12_3 == 42:
                    alt12 = 11
                else:
                    nvae = NoViableAltException("", 12, 3, self.input)

                    raise nvae

            elif LA12 in {47}:
                LA12_4 = self.input.LA(2)

                if LA12_4 == 61:
                    alt12 = 4
                elif LA12_4 == 47:
                    alt12 = 12
                else:
                    nvae = NoViableAltException("", 12, 4, self.input)

                    raise nvae

            elif LA12 in {37}:
                alt12 = 5
            elif LA12 in {38}:
                alt12 = 6
            elif LA12 in {124}:
                alt12 = 7
            elif LA12 in {94}:
                alt12 = 8
            elif LA12 in {60}:
                alt12 = 9
            elif LA12 in {62}:
                alt12 = 10
            else:
                nvae = NoViableAltException("", 12, 0, self.input)

                raise nvae

            if alt12 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:13: '+='
                self.match("+=")

            elif alt12 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:20: '-='
                self.match("-=")

            elif alt12 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:27: '*='
                self.match("*=")

            elif alt12 == 4:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:33: '/='
                self.match("/=")

            elif alt12 == 5:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:40: '%='
                self.match("%=")

            elif alt12 == 6:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:47: '&='
                self.match("&=")

            elif alt12 == 7:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:54: '|='
                self.match("|=")

            elif alt12 == 8:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:61: '^='
                self.match("^=")

            elif alt12 == 9:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:68: '<<='
                self.match("<<=")

            elif alt12 == 10:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:76: '>>='
                self.match(">>=")

            elif alt12 == 11:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:84: '**='
                self.match("**=")

            elif alt12 == 12:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:92: '//='
                self.match("//=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AUG_ASSIGN"

    # $ANTLR start "ID"
    def mID(
        self,
    ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:153:12: ( ID_START ( ID_CONTINUE )* )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:153:14: ID_START ( ID_CONTINUE )*
            self.mID_START()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:153:23: ( ID_CONTINUE )*
            while True:  # loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (
                    (48 <= LA13_0 <= 57)
                    or (65 <= LA13_0 <= 90)
                    or (97 <= LA13_0 <= 122)
                    or LA13_0 in {95}
                ):
                    alt13 = 1

                if alt13 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (
                        (48 <= self.input.LA(1) <= 57)
                        or (65 <= self.input.LA(1) <= 90)
                        or (97 <= self.input.LA(1) <= 122)
                        or self.input.LA(1) in {95}
                    ):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    break  # loop13

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"

    # $ANTLR start "SETTING_ID"
    def mSETTING_ID(
        self,
    ):
        try:
            _type = SETTING_ID
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:154:12: ( '$' ID )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:154:14: '$' ID
            self.match(36)

            self.mID()

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SETTING_ID"

    # $ANTLR start "STRING"
    def mSTRING(
        self,
    ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:157:7: ( ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:158:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:158:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )?
            alt16 = 4
            LA16 = self.input.LA(1)
            if LA16 in {85, 117}:
                alt16 = 1
            elif LA16 in {70, 102}:
                LA16_2 = self.input.LA(2)

                if LA16_2 in {82, 114}:
                    alt16 = 2
                elif LA16_2 in {34, 39}:
                    alt16 = 3
            elif LA16 in {82, 114}:
                LA16_3 = self.input.LA(2)

                if LA16_3 in {34, 39}:
                    alt16 = 2
                elif LA16_3 in {70, 102}:
                    alt16 = 3
            if alt16 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:158:5: ( 'u' | 'U' )
                if self.input.LA(1) in {85, 117}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt16 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:159:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:159:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:159:7: ( 'f' | 'F' )? ( 'r' | 'R' )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:159:7: ( 'f' | 'F' )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if LA14_0 in {70, 102}:
                    alt14 = 1
                if alt14 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if self.input.LA(1) in {70, 102}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                if self.input.LA(1) in {82, 114}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt16 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:7: ( 'r' | 'R' )? ( 'f' | 'F' )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:7: ( 'r' | 'R' )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if LA15_0 in {82, 114}:
                    alt15 = 1
                if alt15 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if self.input.LA(1) in {82, 114}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                if self.input.LA(1) in {70, 102}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            self.mSHORT_STRING()

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"

    # $ANTLR start "INTEGER"
    def mINTEGER(
        self,
    ):
        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:165:9: ( NON_ZERO_DIGIT ( DIGIT )* | ( '0' )+ | '0' ( 'o' | 'O' ) ( OCT_DIGIT )+ | '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ | '0' ( 'b' | 'B' ) ( BIN_DIGIT )+ )
            alt22 = 5
            LA22_0 = self.input.LA(1)

            if (49 <= LA22_0 <= 57) or LA22_0 in {}:
                alt22 = 1
            elif LA22_0 == 48:
                LA22 = self.input.LA(2)
                if LA22 in {79, 111}:
                    alt22 = 3
                elif LA22 in {88, 120}:
                    alt22 = 4
                elif LA22 in {66, 98}:
                    alt22 = 5
                else:
                    alt22 = 2

            else:
                nvae = NoViableAltException("", 22, 0, self.input)

                raise nvae

            if alt22 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:166:3: NON_ZERO_DIGIT ( DIGIT )*
                self.mNON_ZERO_DIGIT()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:166:18: ( DIGIT )*
                while True:  # loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (48 <= LA17_0 <= 57) or LA17_0 in {}:
                        alt17 = 1

                    if alt17 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop17

            elif alt22 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:166:27: ( '0' )+
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:166:27: ( '0' )+
                cnt18 = 0
                while True:  # loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if LA18_0 == 48:
                        alt18 = 1

                    if alt18 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:166:27: '0'
                        self.match(48)

                    else:
                        if cnt18 >= 1:
                            break  # loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1

            elif alt22 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:167:5: '0' ( 'o' | 'O' ) ( OCT_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {79, 111}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:167:21: ( OCT_DIGIT )+
                cnt19 = 0
                while True:  # loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (48 <= LA19_0 <= 55) or LA19_0 in {}:
                        alt19 = 1

                    if alt19 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if (48 <= self.input.LA(1) <= 55) or self.input.LA(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        if cnt19 >= 1:
                            break  # loop19

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1

            elif alt22 == 4:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:168:5: '0' ( 'x' | 'X' ) ( HEX_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {88, 120}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:168:21: ( HEX_DIGIT )+
                cnt20 = 0
                while True:  # loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (
                        (48 <= LA20_0 <= 57)
                        or (65 <= LA20_0 <= 70)
                        or (97 <= LA20_0 <= 102)
                        or LA20_0 in {}
                    ):
                        alt20 = 1

                    if alt20 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if (
                            (48 <= self.input.LA(1) <= 57)
                            or (65 <= self.input.LA(1) <= 70)
                            or (97 <= self.input.LA(1) <= 102)
                            or self.input.LA(1) in {}
                        ):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        if cnt20 >= 1:
                            break  # loop20

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1

            elif alt22 == 5:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:169:5: '0' ( 'b' | 'B' ) ( BIN_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {66, 98}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:169:21: ( BIN_DIGIT )+
                cnt21 = 0
                while True:  # loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if LA21_0 in {48, 49}:
                        alt21 = 1

                    if alt21 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if self.input.LA(1) in {48, 49}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        if cnt21 >= 1:
                            break  # loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INTEGER"

    # $ANTLR start "FLOAT_NUMBER"
    def mFLOAT_NUMBER(
        self,
    ):
        try:
            _type = FLOAT_NUMBER
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:172:14: ( POINT_FLOAT | EXPONENT_FLOAT )
            alt23 = 2
            alt23 = self.dfa23.predict(self.input)
            if alt23 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:172:16: POINT_FLOAT
                self.mPOINT_FLOAT()

            elif alt23 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:172:30: EXPONENT_FLOAT
                self.mEXPONENT_FLOAT()

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT_NUMBER"

    # $ANTLR start "NEWLINE"
    def mNEWLINE(
        self,
    ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:175:8: ( ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:176:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:176:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )?
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt25 = 3
            LA25 = self.input.LA(1)
            if LA25 in {13}:
                LA25_1 = self.input.LA(2)

                if LA25_1 == 10:
                    alt25 = 1
                else:
                    alt25 = 2

            elif LA25 in {10}:
                alt25 = 1
            elif LA25 in {12}:
                alt25 = 3
            else:
                nvae = NoViableAltException("", 25, 0, self.input)

                raise nvae

            if alt25 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:5: ( '\\r' )? '\\n'
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:5: ( '\\r' )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if LA24_0 == 13:
                    alt24 = 1
                if alt24 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:5: '\\r'
                    self.match(13)

                self.match(10)

            elif alt25 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:18: '\\r'
                self.match(13)

            elif alt25 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:25: '\\f'
                self.match(12)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:31: ( SPACES )?
            alt26 = 2
            LA26_0 = self.input.LA(1)

            if LA26_0 in {9, 32}:
                alt26 = 1
            if alt26 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:31: SPACES
                self.mSPACES()

            # action start
            self.onNewLine()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"

    # $ANTLR start "SKIP_"
    def mSKIP_(
        self,
    ):
        try:
            _type = SKIP_
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:182:9: ( ( SPACES | COMMENT | LINE_JOINING ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:182:11: ( SPACES | COMMENT | LINE_JOINING )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:182:11: ( SPACES | COMMENT | LINE_JOINING )
            alt27 = 3
            LA27 = self.input.LA(1)
            if LA27 in {9, 32}:
                alt27 = 1
            elif LA27 in {35}:
                alt27 = 2
            elif LA27 in {92}:
                alt27 = 3
            else:
                nvae = NoViableAltException("", 27, 0, self.input)

                raise nvae

            if alt27 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:182:13: SPACES
                self.mSPACES()

            elif alt27 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:182:22: COMMENT
                self.mCOMMENT()

            elif alt27 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:182:32: LINE_JOINING
                self.mLINE_JOINING()

            # action start
            self.skip()
            # action end

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SKIP_"

    # $ANTLR start "UNKNOWN"
    def mUNKNOWN(
        self,
    ):
        try:
            _type = UNKNOWN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:183:9: ( . )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:183:11: .
            self.matchAny()

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNKNOWN"

    # $ANTLR start "SHORT_STRING"
    def mSHORT_STRING(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:186:22: ( '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\'' | '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"' )
            alt30 = 2
            LA30_0 = self.input.LA(1)

            if LA30_0 == 39:
                alt30 = 1
            elif LA30_0 == 34:
                alt30 = 2
            else:
                nvae = NoViableAltException("", 30, 0, self.input)

                raise nvae

            if alt30 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:187:3: '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\''
                self.match(39)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:187:8: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )*
                while True:  # loop28
                    alt28 = 3
                    LA28_0 = self.input.LA(1)

                    if LA28_0 == 92:
                        alt28 = 1
                    elif (
                        (0 <= LA28_0 <= 9)
                        or (14 <= LA28_0 <= 38)
                        or (40 <= LA28_0 <= 91)
                        or (93 <= LA28_0 <= 65535)
                        or LA28_0 in {11}
                    ):
                        alt28 = 2

                    if alt28 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:187:9: STRING_ESCAPE_SEQ
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt28 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:187:29: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' )
                        if (
                            (0 <= self.input.LA(1) <= 9)
                            or (14 <= self.input.LA(1) <= 38)
                            or (40 <= self.input.LA(1) <= 91)
                            or (93 <= self.input.LA(1) <= 65535)
                            or self.input.LA(1) in {11}
                        ):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop28

                self.match(39)

            elif alt30 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:188:5: '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"'
                self.match(34)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:188:9: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )*
                while True:  # loop29
                    alt29 = 3
                    LA29_0 = self.input.LA(1)

                    if LA29_0 == 92:
                        alt29 = 1
                    elif (
                        (0 <= LA29_0 <= 9)
                        or (14 <= LA29_0 <= 33)
                        or (35 <= LA29_0 <= 91)
                        or (93 <= LA29_0 <= 65535)
                        or LA29_0 in {11}
                    ):
                        alt29 = 2

                    if alt29 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:188:10: STRING_ESCAPE_SEQ
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt29 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:188:30: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' )
                        if (
                            (0 <= self.input.LA(1) <= 9)
                            or (14 <= self.input.LA(1) <= 33)
                            or (35 <= self.input.LA(1) <= 91)
                            or (93 <= self.input.LA(1) <= 65535)
                            or self.input.LA(1) in {11}
                        ):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop29

                self.match(34)

        finally:
            pass

    # $ANTLR end "SHORT_STRING"

    # $ANTLR start "STRING_ESCAPE_SEQ"
    def mSTRING_ESCAPE_SEQ(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:28: ( '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' ) | '\\\\' NEWLINE )
            alt31 = 2
            LA31_0 = self.input.LA(1)

            if LA31_0 == 92:
                LA31_1 = self.input.LA(2)

                if (
                    (0 <= LA31_1 <= 8)
                    or (14 <= LA31_1 <= 31)
                    or (33 <= LA31_1 <= 65535)
                    or LA31_1 in {11}
                ):
                    alt31 = 1
                elif LA31_1 in {10, 12, 13}:
                    alt31 = 2
                else:
                    nvae = NoViableAltException("", 31, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 31, 0, self.input)

                raise nvae

            if alt31 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:30: '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' )
                self.match(92)

                if (
                    (0 <= self.input.LA(1) <= 8)
                    or (14 <= self.input.LA(1) <= 31)
                    or (33 <= self.input.LA(1) <= 65535)
                    or self.input.LA(1) in {11}
                ):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt31 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:72: '\\\\' NEWLINE
                self.match(92)

                self.mNEWLINE()

        finally:
            pass

    # $ANTLR end "STRING_ESCAPE_SEQ"

    # $ANTLR start "NON_ZERO_DIGIT"
    def mNON_ZERO_DIGIT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:192:25: ( '1' .. '9' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (49 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

        finally:
            pass

    # $ANTLR end "NON_ZERO_DIGIT"

    # $ANTLR start "DIGIT"
    def mDIGIT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:193:25: ( '0' .. '9' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

        finally:
            pass

    # $ANTLR end "DIGIT"

    # $ANTLR start "OCT_DIGIT"
    def mOCT_DIGIT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:194:25: ( '0' .. '7' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (48 <= self.input.LA(1) <= 55) or self.input.LA(1) in {}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

        finally:
            pass

    # $ANTLR end "OCT_DIGIT"

    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:195:25: ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (
                (48 <= self.input.LA(1) <= 57)
                or (65 <= self.input.LA(1) <= 70)
                or (97 <= self.input.LA(1) <= 102)
                or self.input.LA(1) in {}
            ):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

        finally:
            pass

    # $ANTLR end "HEX_DIGIT"

    # $ANTLR start "BIN_DIGIT"
    def mBIN_DIGIT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:196:25: ( '0' | '1' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if self.input.LA(1) in {48, 49}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

        finally:
            pass

    # $ANTLR end "BIN_DIGIT"

    # $ANTLR start "POINT_FLOAT"
    def mPOINT_FLOAT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:198:25: ( ( INT_PART )? FRACTION | INT_PART '.' )
            alt33 = 2
            alt33 = self.dfa33.predict(self.input)
            if alt33 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:198:27: ( INT_PART )? FRACTION
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:198:27: ( INT_PART )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (48 <= LA32_0 <= 57) or LA32_0 in {}:
                    alt32 = 1
                if alt32 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:198:27: INT_PART
                    self.mINT_PART()

                self.mFRACTION()

            elif alt33 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:198:48: INT_PART '.'
                self.mINT_PART()

                self.match(46)

        finally:
            pass

    # $ANTLR end "POINT_FLOAT"

    # $ANTLR start "EXPONENT_FLOAT"
    def mEXPONENT_FLOAT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:199:25: ( ( INT_PART | POINT_FLOAT ) EXPONENT )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:199:27: ( INT_PART | POINT_FLOAT ) EXPONENT
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:199:27: ( INT_PART | POINT_FLOAT )
            alt34 = 2
            alt34 = self.dfa34.predict(self.input)
            if alt34 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:199:29: INT_PART
                self.mINT_PART()

            elif alt34 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:199:40: POINT_FLOAT
                self.mPOINT_FLOAT()

            self.mEXPONENT()

        finally:
            pass

    # $ANTLR end "EXPONENT_FLOAT"

    # $ANTLR start "INT_PART"
    def mINT_PART(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:25: ( ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:27: ( DIGIT )+
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:27: ( DIGIT )+
            cnt35 = 0
            while True:  # loop35
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (48 <= LA35_0 <= 57) or LA35_0 in {}:
                    alt35 = 1

                if alt35 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt35 >= 1:
                        break  # loop35

                    eee = EarlyExitException(35, self.input)
                    raise eee

                cnt35 += 1

        finally:
            pass

    # $ANTLR end "INT_PART"

    # $ANTLR start "FRACTION"
    def mFRACTION(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:25: ( '.' ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:27: '.' ( DIGIT )+
            self.match(46)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:31: ( DIGIT )+
            cnt36 = 0
            while True:  # loop36
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (48 <= LA36_0 <= 57) or LA36_0 in {}:
                    alt36 = 1

                if alt36 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt36 >= 1:
                        break  # loop36

                    eee = EarlyExitException(36, self.input)
                    raise eee

                cnt36 += 1

        finally:
            pass

    # $ANTLR end "FRACTION"

    # $ANTLR start "EXPONENT"
    def mEXPONENT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:202:25: ( ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:202:27: ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+
            if self.input.LA(1) in {69, 101}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:202:39: ( '+' | '-' )?
            alt37 = 2
            LA37_0 = self.input.LA(1)

            if LA37_0 in {43, 45}:
                alt37 = 1
            if alt37 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                if self.input.LA(1) in {43, 45}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:202:52: ( DIGIT )+
            cnt38 = 0
            while True:  # loop38
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (48 <= LA38_0 <= 57) or LA38_0 in {}:
                    alt38 = 1

                if alt38 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt38 >= 1:
                        break  # loop38

                    eee = EarlyExitException(38, self.input)
                    raise eee

                cnt38 += 1

        finally:
            pass

    # $ANTLR end "EXPONENT"

    # $ANTLR start "ID_START"
    def mID_START(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:204:22: ( UNDERSCORE | LETTER )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (
                (65 <= self.input.LA(1) <= 90)
                or (97 <= self.input.LA(1) <= 122)
                or self.input.LA(1) in {95}
            ):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

        finally:
            pass

    # $ANTLR end "ID_START"

    # $ANTLR start "ID_CONTINUE"
    def mID_CONTINUE(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:205:22: ( ID_START | DIGIT )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (
                (48 <= self.input.LA(1) <= 57)
                or (65 <= self.input.LA(1) <= 90)
                or (97 <= self.input.LA(1) <= 122)
                or self.input.LA(1) in {95}
            ):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

        finally:
            pass

    # $ANTLR end "ID_CONTINUE"

    # $ANTLR start "LETTER"
    def mLETTER(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:206:22: ( 'a' .. 'z' | 'A' .. 'Z' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (
                (65 <= self.input.LA(1) <= 90)
                or (97 <= self.input.LA(1) <= 122)
                or self.input.LA(1) in {}
            ):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

        finally:
            pass

    # $ANTLR end "LETTER"

    # $ANTLR start "SPACES"
    def mSPACES(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:208:23: ( ( ' ' | '\\t' )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:208:25: ( ' ' | '\\t' )+
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:208:25: ( ' ' | '\\t' )+
            cnt39 = 0
            while True:  # loop39
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if LA39_0 in {9, 32}:
                    alt39 = 1

                if alt39 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if self.input.LA(1) in {9, 32}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt39 >= 1:
                        break  # loop39

                    eee = EarlyExitException(39, self.input)
                    raise eee

                cnt39 += 1

        finally:
            pass

    # $ANTLR end "SPACES"

    # $ANTLR start "COMMENT"
    def mCOMMENT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:209:23: ( '#' (~ ( '\\r' | '\\n' | '\\f' ) )* )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:209:25: '#' (~ ( '\\r' | '\\n' | '\\f' ) )*
            self.match(35)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:209:29: (~ ( '\\r' | '\\n' | '\\f' ) )*
            while True:  # loop40
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (0 <= LA40_0 <= 9) or (14 <= LA40_0 <= 65535) or LA40_0 in {11}:
                    alt40 = 1

                if alt40 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (
                        (0 <= self.input.LA(1) <= 9)
                        or (14 <= self.input.LA(1) <= 65535)
                        or self.input.LA(1) in {11}
                    ):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    break  # loop40

        finally:
            pass

    # $ANTLR end "COMMENT"

    # $ANTLR start "LINE_JOINING"
    def mLINE_JOINING(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:23: ( '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:25: '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            self.match(92)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:30: ( SPACES )?
            alt41 = 2
            LA41_0 = self.input.LA(1)

            if LA41_0 in {9, 32}:
                alt41 = 1
            if alt41 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:30: SPACES
                self.mSPACES()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:38: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt43 = 3
            LA43 = self.input.LA(1)
            if LA43 in {13}:
                LA43_1 = self.input.LA(2)

                if LA43_1 == 10:
                    alt43 = 1
                else:
                    alt43 = 2

            elif LA43 in {10}:
                alt43 = 1
            elif LA43 in {12}:
                alt43 = 3
            else:
                nvae = NoViableAltException("", 43, 0, self.input)

                raise nvae

            if alt43 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:40: ( '\\r' )? '\\n'
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:40: ( '\\r' )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if LA42_0 == 13:
                    alt42 = 1
                if alt42 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:40: '\\r'
                    self.match(13)

                self.match(10)

            elif alt43 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:53: '\\r'
                self.match(13)

            elif alt43 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:60: '\\f'
                self.match(12)

        finally:
            pass

    # $ANTLR end "LINE_JOINING"

    def mTokens(self):
        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:8: ( SCENARIO | SETTINGS | STAGE | WRITERS | SHAPES | SHAPES_OR_LIGHTS | CAMERA | LIGHT | LIGHT_TYPE | STEREO | MATERIAL | TIMELINE | OPEN | CREATE | GROUP | INSTANTIATE | GET | EDIT | FETCH | MATCH | LIMIT | RECURSIVE | TRANSLATE | CAM_TRANSLATE | ROTATE | SCALE | SEMANTICS | VISIBLE | SIZE | LOOK_AT | UP_AXIS | AXIS | ORDER | SCATTER | ROT_AROUND | PHYSICS | EVERY | FRAMES | TIME | DISTRIBUTION | SNIPPET | TO | ON | AT | AND | ELSE | FALSE | FOR | FROM | IF | IN | IS | LEN | NONE | NOT | OR | STEP | TRUE | UNDERSCORE | DOT | RANGE | ELLIPSIS | COMMA | COLON | SEMI | ASSIGN | BIT_OR | XOR | BIT_AND | BIT_NOT | LSHIFT | RSHIFT | PLUS | MINUS | MUL | DIV | MOD | IDIV | POWER | LPAREN | RPAREN | LBRACK | RBRACK | LBRACE | RBRACE | LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | AUG_ASSIGN | ID | SETTING_ID | STRING | INTEGER | FLOAT_NUMBER | NEWLINE | SKIP_ | UNKNOWN )
        alt44 = 100
        alt44 = self.dfa44.predict(self.input)
        if alt44 == 1:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:10: SCENARIO
            self.mSCENARIO()

        elif alt44 == 2:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:19: SETTINGS
            self.mSETTINGS()

        elif alt44 == 3:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:28: STAGE
            self.mSTAGE()

        elif alt44 == 4:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:34: WRITERS
            self.mWRITERS()

        elif alt44 == 5:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:42: SHAPES
            self.mSHAPES()

        elif alt44 == 6:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:49: SHAPES_OR_LIGHTS
            self.mSHAPES_OR_LIGHTS()

        elif alt44 == 7:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:66: CAMERA
            self.mCAMERA()

        elif alt44 == 8:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:73: LIGHT
            self.mLIGHT()

        elif alt44 == 9:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:79: LIGHT_TYPE
            self.mLIGHT_TYPE()

        elif alt44 == 10:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:90: STEREO
            self.mSTEREO()

        elif alt44 == 11:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:97: MATERIAL
            self.mMATERIAL()

        elif alt44 == 12:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:106: TIMELINE
            self.mTIMELINE()

        elif alt44 == 13:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:115: OPEN
            self.mOPEN()

        elif alt44 == 14:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:120: CREATE
            self.mCREATE()

        elif alt44 == 15:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:127: GROUP
            self.mGROUP()

        elif alt44 == 16:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:133: INSTANTIATE
            self.mINSTANTIATE()

        elif alt44 == 17:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:145: GET
            self.mGET()

        elif alt44 == 18:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:149: EDIT
            self.mEDIT()

        elif alt44 == 19:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:154: FETCH
            self.mFETCH()

        elif alt44 == 20:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:160: MATCH
            self.mMATCH()

        elif alt44 == 21:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:166: LIMIT
            self.mLIMIT()

        elif alt44 == 22:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:172: RECURSIVE
            self.mRECURSIVE()

        elif alt44 == 23:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:182: TRANSLATE
            self.mTRANSLATE()

        elif alt44 == 24:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:192: CAM_TRANSLATE
            self.mCAM_TRANSLATE()

        elif alt44 == 25:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:206: ROTATE
            self.mROTATE()

        elif alt44 == 26:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:213: SCALE
            self.mSCALE()

        elif alt44 == 27:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:219: SEMANTICS
            self.mSEMANTICS()

        elif alt44 == 28:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:229: VISIBLE
            self.mVISIBLE()

        elif alt44 == 29:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:237: SIZE
            self.mSIZE()

        elif alt44 == 30:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:242: LOOK_AT
            self.mLOOK_AT()

        elif alt44 == 31:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:250: UP_AXIS
            self.mUP_AXIS()

        elif alt44 == 32:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:258: AXIS
            self.mAXIS()

        elif alt44 == 33:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:263: ORDER
            self.mORDER()

        elif alt44 == 34:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:269: SCATTER
            self.mSCATTER()

        elif alt44 == 35:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:277: ROT_AROUND
            self.mROT_AROUND()

        elif alt44 == 36:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:288: PHYSICS
            self.mPHYSICS()

        elif alt44 == 37:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:296: EVERY
            self.mEVERY()

        elif alt44 == 38:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:302: FRAMES
            self.mFRAMES()

        elif alt44 == 39:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:309: TIME
            self.mTIME()

        elif alt44 == 40:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:314: DISTRIBUTION
            self.mDISTRIBUTION()

        elif alt44 == 41:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:327: SNIPPET
            self.mSNIPPET()

        elif alt44 == 42:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:335: TO
            self.mTO()

        elif alt44 == 43:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:338: ON
            self.mON()

        elif alt44 == 44:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:341: AT
            self.mAT()

        elif alt44 == 45:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:344: AND
            self.mAND()

        elif alt44 == 46:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:348: ELSE
            self.mELSE()

        elif alt44 == 47:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:353: FALSE
            self.mFALSE()

        elif alt44 == 48:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:359: FOR
            self.mFOR()

        elif alt44 == 49:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:363: FROM
            self.mFROM()

        elif alt44 == 50:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:368: IF
            self.mIF()

        elif alt44 == 51:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:371: IN
            self.mIN()

        elif alt44 == 52:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:374: IS
            self.mIS()

        elif alt44 == 53:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:377: LEN
            self.mLEN()

        elif alt44 == 54:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:381: NONE
            self.mNONE()

        elif alt44 == 55:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:386: NOT
            self.mNOT()

        elif alt44 == 56:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:390: OR
            self.mOR()

        elif alt44 == 57:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:393: STEP
            self.mSTEP()

        elif alt44 == 58:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:398: TRUE
            self.mTRUE()

        elif alt44 == 59:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:403: UNDERSCORE
            self.mUNDERSCORE()

        elif alt44 == 60:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:414: DOT
            self.mDOT()

        elif alt44 == 61:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:418: RANGE
            self.mRANGE()

        elif alt44 == 62:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:424: ELLIPSIS
            self.mELLIPSIS()

        elif alt44 == 63:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:433: COMMA
            self.mCOMMA()

        elif alt44 == 64:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:439: COLON
            self.mCOLON()

        elif alt44 == 65:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:445: SEMI
            self.mSEMI()

        elif alt44 == 66:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:450: ASSIGN
            self.mASSIGN()

        elif alt44 == 67:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:457: BIT_OR
            self.mBIT_OR()

        elif alt44 == 68:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:464: XOR
            self.mXOR()

        elif alt44 == 69:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:468: BIT_AND
            self.mBIT_AND()

        elif alt44 == 70:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:476: BIT_NOT
            self.mBIT_NOT()

        elif alt44 == 71:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:484: LSHIFT
            self.mLSHIFT()

        elif alt44 == 72:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:491: RSHIFT
            self.mRSHIFT()

        elif alt44 == 73:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:498: PLUS
            self.mPLUS()

        elif alt44 == 74:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:503: MINUS
            self.mMINUS()

        elif alt44 == 75:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:509: MUL
            self.mMUL()

        elif alt44 == 76:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:513: DIV
            self.mDIV()

        elif alt44 == 77:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:517: MOD
            self.mMOD()

        elif alt44 == 78:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:521: IDIV
            self.mIDIV()

        elif alt44 == 79:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:526: POWER
            self.mPOWER()

        elif alt44 == 80:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:532: LPAREN
            self.mLPAREN()

        elif alt44 == 81:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:539: RPAREN
            self.mRPAREN()

        elif alt44 == 82:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:546: LBRACK
            self.mLBRACK()

        elif alt44 == 83:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:553: RBRACK
            self.mRBRACK()

        elif alt44 == 84:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:560: LBRACE
            self.mLBRACE()

        elif alt44 == 85:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:567: RBRACE
            self.mRBRACE()

        elif alt44 == 86:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:574: LT
            self.mLT()

        elif alt44 == 87:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:577: GT
            self.mGT()

        elif alt44 == 88:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:580: EQUALS
            self.mEQUALS()

        elif alt44 == 89:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:587: GT_EQ
            self.mGT_EQ()

        elif alt44 == 90:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:593: LT_EQ
            self.mLT_EQ()

        elif alt44 == 91:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:599: NOT_EQ
            self.mNOT_EQ()

        elif alt44 == 92:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:606: AUG_ASSIGN
            self.mAUG_ASSIGN()

        elif alt44 == 93:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:617: ID
            self.mID()

        elif alt44 == 94:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:620: SETTING_ID
            self.mSETTING_ID()

        elif alt44 == 95:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:631: STRING
            self.mSTRING()

        elif alt44 == 96:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:638: INTEGER
            self.mINTEGER()

        elif alt44 == 97:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:646: FLOAT_NUMBER
            self.mFLOAT_NUMBER()

        elif alt44 == 98:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:659: NEWLINE
            self.mNEWLINE()

        elif alt44 == 99:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:667: SKIP_
            self.mSKIP_()

        elif alt44 == 100:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:673: UNKNOWN
            self.mUNKNOWN()

    # lookup tables for DFA #23

    DFA23_eot = DFA.unpack("\3\uffff\1\6\1\uffff\1\6\1\uffff")

    DFA23_eof = DFA.unpack("\7\uffff")

    DFA23_min = DFA.unpack("\2\56\2\60\1\uffff\1\60\1\uffff")

    DFA23_max = DFA.unpack("\1\71\1\145\1\71\1\145\1\uffff\1\145\1\uffff")

    DFA23_accept = DFA.unpack("\4\uffff\1\2\1\uffff\1\1")

    DFA23_special = DFA.unpack("\7\uffff")

    DFA23_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack("\12\5"),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
    ]

    # class definition for DFA #23

    class DFA23(DFA):
        pass

    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack("\3\uffff\1\4\1\uffff")

    DFA33_eof = DFA.unpack("\5\uffff")

    DFA33_min = DFA.unpack("\2\56\1\uffff\1\60\1\uffff")

    DFA33_max = DFA.unpack("\2\71\1\uffff\1\71\1\uffff")

    DFA33_accept = DFA.unpack("\2\uffff\1\1\1\uffff\1\2")

    DFA33_special = DFA.unpack("\5\uffff")

    DFA33_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1"),
        DFA.unpack(""),
        DFA.unpack("\12\2"),
        DFA.unpack(""),
    ]

    # class definition for DFA #33

    class DFA33(DFA):
        pass

    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack("\4\uffff")

    DFA34_eof = DFA.unpack("\4\uffff")

    DFA34_min = DFA.unpack("\2\56\2\uffff")

    DFA34_max = DFA.unpack("\1\71\1\145\2\uffff")

    DFA34_accept = DFA.unpack("\2\uffff\1\2\1\1")

    DFA34_special = DFA.unpack("\4\uffff")

    DFA34_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\2\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(""),
        DFA.unpack(""),
    ]

    # class definition for DFA #34

    class DFA34(DFA):
        pass

    # lookup tables for DFA #44

    DFA44_eot = DFA.unpack(
        "\1\uffff\26\110\1\173\4\110\1\u0081\2\110\1\u0086\1\u0088\3\uffff"
        "\1\u008e\1\u0090\1\u0091\1\u0092\1\uffff\1\u0096\1\u0099\1\u009a"
        "\1\u009b\1\u009d\1\u009f\1\u00a0\5\uffff\1\103\1\110\1\103\1\uffff"
        "\2\103\2\u00a8\5\uffff\1\103\1\uffff\4\110\1\uffff\22\110\1\uffff"
        "\2\110\1\u00c8\1\u00c9\5\110\1\u00d0\1\u00d1\1\u00d2\20\110\1\u00e4"
        "\2\110\1\uffff\5\110\2\uffff\1\u00ec\2\110\1\uffff\1\u00f1\14\uffff"
        "\1\u00f2\2\uffff\1\u00f3\4\uffff\1\u00f4\1\uffff\1\u00f5\12\uffff"
        "\2\u00a8\2\uffff\4\110\1\u00fc\26\110\2\uffff\4\110\1\u0118\1\110"
        "\3\uffff\7\110\1\u0121\3\110\1\u0125\5\110\1\uffff\2\110\1\u012d"
        "\4\110\1\uffff\1\u0132\1\110\1\u0134\6\uffff\6\110\1\uffff\1\110"
        "\1\u013c\1\u013d\2\110\2\u0140\10\110\1\u0149\1\110\1\u014b\2\110"
        "\1\u014b\1\110\1\u014f\4\110\1\uffff\1\110\1\u0155\1\110\1\u0157"
        "\2\110\1\u015a\1\110\1\uffff\3\110\1\uffff\4\110\1\u0163\2\110\1"
        "\uffff\4\110\1\uffff\1\u016a\1\uffff\1\110\1\u016c\4\110\1\u0171"
        "\2\uffff\1\110\1\u0140\1\uffff\3\110\1\u0140\4\110\1\uffff\1\110"
        "\1\uffff\1\u017b\2\110\1\uffff\3\110\1\u0181\1\110\1\uffff\1\u0183"
        "\1\uffff\1\u0184\1\u0186\1\uffff\1\u0187\1\u0188\1\u0189\5\110\1"
        "\uffff\6\110\1\uffff\1\110\1\uffff\3\110\1\u00fc\1\uffff\2\110\1"
        "\u019c\1\u019d\1\110\1\u0149\1\u019f\2\110\1\uffff\2\110\1\u01a4"
        "\2\110\1\uffff\1\110\2\uffff\1\u0186\4\uffff\2\110\1\u01ab\7\110"
        "\1\u019d\4\110\1\u00fc\1\u01b7\1\110\2\uffff\1\110\1\uffff\1\110"
        "\1\u014b\2\110\1\uffff\3\110\1\u01c0\2\110\1\uffff\2\110\1\u01c5"
        "\1\u01c6\2\110\1\u019d\1\u01c9\1\110\1\u01cc\1\110\1\uffff\1\u0149"
        "\1\u01ce\1\u019d\1\110\1\u01d0\1\110\1\u01d2\1\110\1\uffff\4\110"
        "\2\uffff\2\110\1\uffff\2\110\1\uffff\1\u01dc\1\uffff\1\110\1\uffff"
        "\1\110\1\uffff\1\110\1\u01e0\2\110\1\u01e3\2\110\2\u01e6\1\uffff"
        "\1\u019d\2\110\1\uffff\1\110\1\u01d2\1\uffff\1\u01d2\1\110\1\uffff"
        "\1\110\1\u01ec\3\110\1\uffff\3\110\1\u01f3\2\110\1\uffff\3\110\1"
        "\u01f9\1\u01d2\1\uffff"
    )

    DFA44_eof = DFA.unpack("\u01fa\uffff")

    DFA44_min = DFA.unpack(
        "\1\0\1\143\1\162\1\154\1\141\1\151\1\145\2\151\1\42\1\141\1\156"
        "\1\141\1\145\1\146\1\144\1\42\1\141\1\145\1\42\1\157\1\151\1\42"
        "\1\60\1\151\1\150\1\42\1\157\1\173\1\156\1\157\1\60\1\56\3\uffff"
        "\4\75\1\uffff\1\74\3\75\1\52\1\57\1\75\5\uffff\1\75\1\42\1\101\1"
        "\uffff\2\0\2\56\5\uffff\1\11\1\uffff\1\141\1\143\1\141\1\172\1\uffff"
        "\1\151\1\141\1\142\1\156\1\154\1\155\1\157\1\162\1\155\1\150\1\145"
        "\1\161\1\163\1\155\2\147\1\143\1\42\1\uffff\1\164\1\145\2\60\1\145"
        "\1\155\1\154\1\157\1\164\3\60\1\151\1\145\1\163\1\164\1\42\1\154"
        "\1\162\1\42\1\164\1\155\1\157\1\156\1\143\1\164\1\147\1\141\1\60"
        "\1\163\1\137\1\uffff\1\130\1\156\1\171\1\151\1\162\2\uffff\1\60"
        "\1\144\1\156\1\uffff\1\56\14\uffff\1\75\2\uffff\1\75\4\uffff\1\75"
        "\1\uffff\1\75\12\uffff\2\56\2\uffff\1\156\1\154\1\164\1\141\1\60"
        "\1\147\1\160\1\145\1\164\1\156\2\145\1\151\1\145\1\151\1\165\2\145"
        "\1\162\1\165\1\153\1\145\1\150\1\125\1\164\1\145\1\156\2\uffff\1"
        "\141\1\145\1\154\1\165\1\60\1\164\3\uffff\1\164\1\162\1\145\1\143"
        "\2\155\1\163\1\60\1\143\1\151\1\153\1\60\1\165\1\141\1\151\1\156"
        "\1\145\1\uffff\1\151\1\141\1\60\1\145\1\163\1\146\1\155\1\uffff"
        "\1\60\1\145\1\60\6\uffff\1\141\1\145\1\164\1\151\2\156\1\uffff\1"
        "\145\2\60\2\145\2\60\1\156\1\162\1\143\1\163\1\154\1\162\2\145\1"
        "\60\1\141\1\60\1\164\1\156\1\60\1\162\1\60\1\164\1\162\1\151\1\160"
        "\1\uffff\1\141\1\60\1\171\1\60\1\150\1\145\1\60\1\145\1\uffff\1"
        "\150\1\164\1\137\1\uffff\1\162\1\164\1\144\1\163\1\60\1\142\1\170"
        "\1\uffff\1\155\1\151\1\157\1\141\1\uffff\1\60\1\uffff\1\162\1\60"
        "\1\145\1\156\1\164\1\144\1\60\2\uffff\1\162\1\60\1\uffff\1\144\1"
        "\141\1\145\1\60\1\151\1\145\1\157\1\156\1\uffff\1\156\1\uffff\1"
        "\60\2\151\1\uffff\1\145\1\141\1\144\1\60\1\156\1\uffff\1\60\1\uffff"
        "\2\60\1\uffff\3\60\1\141\1\163\1\145\1\137\1\154\1\uffff\1\154\1"
        "\151\1\141\1\143\1\162\1\154\1\uffff\1\151\1\uffff\1\162\1\147\1"
        "\151\1\60\1\uffff\1\163\1\145\2\60\1\156\2\60\1\143\1\164\1\uffff"
        "\1\146\1\141\1\60\1\137\1\145\1\uffff\1\164\2\uffff\1\60\4\uffff"
        "\1\164\1\151\1\60\1\142\1\141\1\145\1\163\1\164\1\163\1\155\1\60"
        "\1\157\1\137\1\163\1\143\2\60\1\162\2\uffff\1\145\1\uffff\1\145"
        "\1\60\1\157\1\154\1\uffff\1\164\1\162\1\151\1\60\1\166\1\141\1\uffff"
        "\1\157\1\164\2\60\1\151\1\137\2\60\1\62\1\60\1\163\1\uffff\3\60"
        "\1\162\1\60\1\162\1\60\1\141\1\uffff\1\145\1\162\1\144\1\145\2\uffff"
        "\1\143\1\155\1\uffff\2\144\1\uffff\1\60\1\uffff\1\155\1\uffff\1"
        "\141\1\uffff\1\164\1\60\1\157\1\171\1\60\1\163\1\141\2\60\1\uffff"
        "\1\60\1\156\1\145\1\uffff\1\165\1\60\1\uffff\1\60\1\164\1\uffff"
        "\1\163\1\60\1\156\1\145\1\154\1\uffff\1\144\1\162\1\141\1\60\1\151"
        "\1\164\1\uffff\1\141\1\145\1\154\2\60\1\uffff"
    )

    DFA44_max = DFA.unpack(
        "\1\uffff\1\164\1\162\1\154\1\171\1\157\1\164\2\157\1\146\1\141\3"
        "\162\1\163\1\166\1\162\1\141\2\157\1\162\1\151\1\160\1\172\1\151"
        "\1\150\1\156\1\157\1\173\1\164\1\157\1\172\1\71\3\uffff\4\75\1\uffff"
        "\1\75\1\76\5\75\5\uffff\1\75\1\162\1\172\1\uffff\2\uffff\2\145\5"
        "\uffff\1\40\1\uffff\1\145\1\164\1\145\1\172\1\uffff\1\151\1\141"
        "\1\142\1\156\1\154\1\155\1\157\1\162\1\155\1\150\1\145\1\161\1\163"
        "\1\155\2\147\1\143\1\47\1\uffff\1\164\1\145\2\172\1\145\1\155\1"
        "\154\1\157\1\164\3\172\1\151\1\145\1\163\1\164\1\157\1\154\1\162"
        "\1\47\1\164\1\155\1\157\1\156\1\143\1\164\1\147\1\165\1\172\1\163"
        "\1\137\1\uffff\1\172\1\156\1\171\1\151\1\162\2\uffff\1\172\1\144"
        "\1\164\1\uffff\1\56\14\uffff\1\75\2\uffff\1\75\4\uffff\1\75\1\uffff"
        "\1\75\12\uffff\2\145\2\uffff\1\156\2\164\1\141\1\172\1\147\1\160"
        "\1\145\1\164\1\156\2\145\1\151\1\145\1\151\1\165\2\145\1\162\1\165"
        "\1\164\1\145\1\150\1\125\1\164\1\145\1\156\2\uffff\1\141\1\145\1"
        "\154\1\165\1\172\1\164\3\uffff\1\164\1\162\1\145\1\143\2\155\1\163"
        "\1\172\1\143\1\151\1\153\1\172\1\165\1\141\1\151\1\156\1\145\1\uffff"
        "\1\151\1\141\1\172\1\145\1\163\1\146\1\155\1\uffff\1\172\1\145\1"
        "\172\6\uffff\1\141\1\145\1\164\1\151\2\156\1\uffff\1\145\2\172\2"
        "\145\2\172\1\156\1\162\1\143\1\163\1\154\1\162\2\145\1\172\1\141"
        "\1\172\1\164\1\156\1\172\1\162\1\172\1\164\1\162\1\151\1\160\1\uffff"
        "\1\141\1\172\1\171\1\172\1\150\1\145\1\172\1\145\1\uffff\1\150\1"
        "\164\1\137\1\uffff\1\162\1\164\1\144\1\163\1\172\1\142\1\170\1\uffff"
        "\1\155\1\151\1\157\1\141\1\uffff\1\172\1\uffff\1\162\1\172\1\145"
        "\1\156\1\164\1\144\1\172\2\uffff\1\162\1\172\1\uffff\1\144\1\141"
        "\1\145\1\172\1\151\1\145\1\157\1\156\1\uffff\1\156\1\uffff\1\172"
        "\2\151\1\uffff\1\145\1\141\1\144\1\172\1\156\1\uffff\1\172\1\uffff"
        "\2\172\1\uffff\3\172\1\141\1\163\1\145\1\137\1\154\1\uffff\1\154"
        "\1\151\1\141\1\143\1\162\1\154\1\uffff\1\151\1\uffff\1\162\1\147"
        "\1\151\1\172\1\uffff\1\163\1\145\2\172\1\156\2\172\1\143\1\164\1"
        "\uffff\1\146\1\141\1\172\1\137\1\145\1\uffff\1\164\2\uffff\1\172"
        "\4\uffff\1\164\1\151\1\172\1\142\1\141\1\145\1\163\1\164\1\163\1"
        "\155\1\172\1\157\1\137\1\163\1\143\2\172\1\162\2\uffff\1\145\1\uffff"
        "\1\145\1\172\1\157\1\154\1\uffff\1\164\1\162\1\151\1\172\1\166\1"
        "\141\1\uffff\1\157\1\164\2\172\1\151\1\137\2\172\1\63\1\172\1\163"
        "\1\uffff\3\172\1\162\1\172\1\162\1\172\1\141\1\uffff\1\145\1\162"
        "\1\144\1\145\2\uffff\1\143\1\155\1\uffff\2\144\1\uffff\1\172\1\uffff"
        "\1\155\1\uffff\1\141\1\uffff\1\164\1\172\1\157\1\171\1\172\1\163"
        "\1\141\2\172\1\uffff\1\172\1\156\1\145\1\uffff\1\165\1\172\1\uffff"
        "\1\172\1\164\1\uffff\1\163\1\172\1\156\1\145\1\154\1\uffff\1\144"
        "\1\162\1\141\1\172\1\151\1\164\1\uffff\1\141\1\145\1\154\2\172\1"
        "\uffff"
    )

    DFA44_accept = DFA.unpack(
        "\41\uffff\1\77\1\100\1\101\4\uffff\1\106\7\uffff\1\120\1\121\1\122"
        "\1\123\1\125\3\uffff\1\135\4\uffff\3\142\2\143\1\uffff\1\144\4\uffff"
        "\1\135\22\uffff\1\137\37\uffff\1\40\5\uffff\1\124\1\51\3\uffff\1"
        "\73\1\uffff\1\74\1\141\1\77\1\100\1\101\1\130\1\102\1\134\1\103"
        "\1\104\1\105\1\106\1\uffff\1\132\1\126\1\uffff\1\131\1\127\1\111"
        "\1\112\1\uffff\1\113\1\uffff\1\114\1\115\1\120\1\121\1\122\1\123"
        "\1\125\1\133\1\136\1\140\2\uffff\1\142\1\143\33\uffff\1\53\1\70"
        "\6\uffff\1\63\1\62\1\64\21\uffff\1\52\7\uffff\1\54\3\uffff\1\76"
        "\1\75\1\107\1\110\1\117\1\116\6\uffff\1\47\33\uffff\1\21\10\uffff"
        "\1\60\3\uffff\1\65\7\uffff\1\41\4\uffff\1\55\1\uffff\1\67\7\uffff"
        "\1\71\1\35\2\uffff\1\5\10\uffff\1\6\1\uffff\1\11\3\uffff\1\15\5"
        "\uffff\1\22\1\uffff\1\56\2\uffff\1\61\10\uffff\1\72\6\uffff\1\66"
        "\1\uffff\1\32\4\uffff\1\3\11\uffff\1\10\5\uffff\1\17\1\uffff\1\45"
        "\1\23\1\uffff\1\46\1\57\1\24\1\25\22\uffff\1\7\1\50\1\uffff\1\12"
        "\4\uffff\1\16\6\uffff\1\31\13\uffff\1\4\10\uffff\1\36\4\uffff\1"
        "\34\1\37\2\uffff\1\1\2\uffff\1\2\1\uffff\1\14\1\uffff\1\13\1\uffff"
        "\1\44\11\uffff\1\33\3\uffff\1\26\2\uffff\1\27\2\uffff\1\42\5\uffff"
        "\1\20\6\uffff\1\43\5\uffff\1\30"
    )

    DFA44_special = DFA.unpack("\1\0\70\uffff\1\1\1\2\u01bf\uffff")

    DFA44_transition = [
        DFA.unpack(
            "\11\103\1\100\1\76\1\103\1\77\1\75\22\103\1\100\1\65"
            "\1\72\1\101\1\67\1\57\1\47\1\71\1\60\1\61\1\55\1\53\1\41\1\54\1"
            "\40\1\56\1\74\11\73\1\42\1\43\1\51\1\44\1\52\2\103\2\70\1\4\1\7"
            "\1\70\1\66\5\70\1\10\1\12\1\33\1\70\1\3\1\70\1\11\1\6\1\5\1\32\2"
            "\70\3\27\1\62\1\102\1\63\1\46\1\37\1\103\1\35\1\70\1\14\1\70\1\17"
            "\1\20\1\15\1\70\1\16\1\70\1\30\1\22\1\21\1\36\1\13\1\31\1\70\1\23"
            "\1\1\1\24\1\26\1\25\1\2\3\27\1\34\1\45\1\64\1\50\uff81\103"
        ),
        DFA.unpack("\1\104\1\uffff\1\105\3\uffff\1\107\12\uffff\1\106"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\116\6\uffff\1\117\6\uffff\1\114\5\uffff\1\113\3\uffff" "\1\115"),
        DFA.unpack("\1\121\5\uffff\1\120"),
        DFA.unpack("\1\124\12\uffff\1\122\3\uffff\1\123"),
        DFA.unpack("\1\125\5\uffff\1\126"),
        DFA.unpack("\1\127\5\uffff\1\130"),
        DFA.unpack("\1\133\4\uffff\1\133\36\uffff\1\132\36\uffff\1\131\1" "\132"),
        DFA.unpack("\1\134"),
        DFA.unpack("\1\136\1\uffff\1\135\1\uffff\1\137"),
        DFA.unpack("\1\141\15\uffff\1\142\2\uffff\1\140"),
        DFA.unpack("\1\144\14\uffff\1\143"),
        DFA.unpack("\1\146\7\uffff\1\145\4\uffff\1\147"),
        DFA.unpack("\1\150\7\uffff\1\152\11\uffff\1\151"),
        DFA.unpack(
            "\1\133\4\uffff\1\133\52\uffff\1\157\16\uffff\1\155\3"
            "\uffff\1\153\11\uffff\1\156\2\uffff\1\154"
        ),
        DFA.unpack("\1\160"),
        DFA.unpack("\1\163\3\uffff\1\161\5\uffff\1\162"),
        DFA.unpack(
            "\1\133\4\uffff\1\133\36\uffff\1\132\36\uffff\1\164\1"
            "\132\2\uffff\1\166\5\uffff\1\165"
        ),
        DFA.unpack("\1\170\2\uffff\1\167"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\133\4\uffff\1\133\110\uffff\1\172"),
        DFA.unpack(
            "\12\110\7\uffff\27\110\3\174\4\uffff\1\110\1\uffff\27" "\110\3\174"
        ),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\133\4\uffff\1\133\106\uffff\1\177"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0082"),
        DFA.unpack("\1\u0084\5\uffff\1\u0083"),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0087\1\uffff\12\u0089"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u008f"),
        DFA.unpack(""),
        DFA.unpack("\1\u0094\1\u0095"),
        DFA.unpack("\1\u0098\1\u0097"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u009c\22\uffff\1\u008f"),
        DFA.unpack("\1\u009e\15\uffff\1\u008f"),
        DFA.unpack("\1\u008f"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00a6"),
        DFA.unpack("\1\133\4\uffff\1\133\52\uffff\1\157\37\uffff\1\157"),
        DFA.unpack("\32\u00a7\4\uffff\1\u00a7\1\uffff\32\u00a7"),
        DFA.unpack(""),
        DFA.unpack("\12\133\1\uffff\1\133\2\uffff\ufff2\133"),
        DFA.unpack("\12\133\1\uffff\1\133\2\uffff\ufff2\133"),
        DFA.unpack("\1\u0089\1\uffff\12\u00a9\13\uffff\1\u0089\37\uffff" "\1\u0089"),
        DFA.unpack(
            "\1\u0089\1\uffff\1\u00aa\11\u0089\13\uffff\1\u0089\37" "\uffff\1\u0089"
        ),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\2\u00ac\1\uffff\2\u00ac\22\uffff\1\u00ac"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ae\3\uffff\1\u00ad"),
        DFA.unpack("\1\u00b1\11\uffff\1\u00b0\6\uffff\1\u00af"),
        DFA.unpack("\1\u00b2\3\uffff\1\u00b3"),
        DFA.unpack("\1\u00b4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b5"),
        DFA.unpack("\1\u00b6"),
        DFA.unpack("\1\u00b7"),
        DFA.unpack("\1\u00b8"),
        DFA.unpack("\1\u00b9"),
        DFA.unpack("\1\u00ba"),
        DFA.unpack("\1\u00bb"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\1\u00be"),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\1\u00c0"),
        DFA.unpack("\1\u00c1"),
        DFA.unpack("\1\u00c2"),
        DFA.unpack("\1\u00c3"),
        DFA.unpack("\1\u00c4"),
        DFA.unpack("\1\u00c5"),
        DFA.unpack("\1\133\4\uffff\1\133"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c6"),
        DFA.unpack("\1\u00c7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00ca"),
        DFA.unpack("\1\u00cb"),
        DFA.unpack("\1\u00cc"),
        DFA.unpack("\1\u00cd"),
        DFA.unpack("\1\u00ce"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u00cf\7\110"
        ),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00d3"),
        DFA.unpack("\1\u00d4"),
        DFA.unpack("\1\u00d5"),
        DFA.unpack("\1\u00d6"),
        DFA.unpack("\1\133\4\uffff\1\133\71\uffff\1\u00d7\15\uffff\1\u00d8"),
        DFA.unpack("\1\u00d9"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\133\4\uffff\1\133"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack("\1\u00dd"),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\1\u00df"),
        DFA.unpack("\1\u00e0"),
        DFA.unpack("\1\u00e1"),
        DFA.unpack("\1\u00e2\23\uffff\1\u00e3"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00e5"),
        DFA.unpack("\1\u00e6"),
        DFA.unpack(""),
        DFA.unpack("\3\u00e7\35\uffff\3\u00e7"),
        DFA.unpack("\1\u00e8"),
        DFA.unpack("\1\u00e9"),
        DFA.unpack("\1\u00ea"),
        DFA.unpack("\1\u00eb"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00ed"),
        DFA.unpack("\1\u00ee\5\uffff\1\u00ef"),
        DFA.unpack(""),
        DFA.unpack("\1\u00f0"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008f"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008f"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008f"),
        DFA.unpack(""),
        DFA.unpack("\1\u008f"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0089\1\uffff\12\u00a9\13\uffff\1\u0089\37\uffff" "\1\u0089"),
        DFA.unpack(
            "\1\u0089\1\uffff\1\u00aa\11\u0089\13\uffff\1\u0089\37" "\uffff\1\u0089"
        ),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f6"),
        DFA.unpack("\1\u00f7\7\uffff\1\u00f8"),
        DFA.unpack("\1\u00f9"),
        DFA.unpack("\1\u00fa"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\16\110" "\1\u00fb\13\110"
        ),
        DFA.unpack("\1\u00fd"),
        DFA.unpack("\1\u00fe"),
        DFA.unpack("\1\u00ff"),
        DFA.unpack("\1\u0100"),
        DFA.unpack("\1\u0101"),
        DFA.unpack("\1\u0102"),
        DFA.unpack("\1\u0103"),
        DFA.unpack("\1\u0104"),
        DFA.unpack("\1\u0105"),
        DFA.unpack("\1\u0106"),
        DFA.unpack("\1\u0107"),
        DFA.unpack("\1\u0108"),
        DFA.unpack("\1\u0109"),
        DFA.unpack("\1\u010a"),
        DFA.unpack("\1\u010b"),
        DFA.unpack("\1\u010c\10\uffff\1\u010d"),
        DFA.unpack("\1\u010e"),
        DFA.unpack("\1\u010f"),
        DFA.unpack("\1\u0110"),
        DFA.unpack("\1\u0111"),
        DFA.unpack("\1\u0112"),
        DFA.unpack("\1\u0113"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0114"),
        DFA.unpack("\1\u0115"),
        DFA.unpack("\1\u0116"),
        DFA.unpack("\1\u0117"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0119"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u011a"),
        DFA.unpack("\1\u011b"),
        DFA.unpack("\1\u011c"),
        DFA.unpack("\1\u011d"),
        DFA.unpack("\1\u011e"),
        DFA.unpack("\1\u011f"),
        DFA.unpack("\1\u0120"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0122"),
        DFA.unpack("\1\u0123"),
        DFA.unpack("\1\u0124"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0126"),
        DFA.unpack("\1\u0127"),
        DFA.unpack("\1\u0128"),
        DFA.unpack("\1\u0129"),
        DFA.unpack("\1\u012a"),
        DFA.unpack(""),
        DFA.unpack("\1\u012b"),
        DFA.unpack("\1\u012c"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u012e"),
        DFA.unpack("\1\u012f"),
        DFA.unpack("\1\u0130"),
        DFA.unpack("\1\u0131"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0133"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0135"),
        DFA.unpack("\1\u0136"),
        DFA.unpack("\1\u0137"),
        DFA.unpack("\1\u0138"),
        DFA.unpack("\1\u0139"),
        DFA.unpack("\1\u013a"),
        DFA.unpack(""),
        DFA.unpack("\1\u013b"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u013e"),
        DFA.unpack("\1\u013f"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\1\u0142"),
        DFA.unpack("\1\u0143"),
        DFA.unpack("\1\u0144"),
        DFA.unpack("\1\u0145"),
        DFA.unpack("\1\u0146"),
        DFA.unpack("\1\u0147"),
        DFA.unpack("\1\u0148"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u014a"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u014c"),
        DFA.unpack("\1\u014d"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u014e"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0150"),
        DFA.unpack("\1\u0151"),
        DFA.unpack("\1\u0152"),
        DFA.unpack("\1\u0153"),
        DFA.unpack(""),
        DFA.unpack("\1\u0154"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0156"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0158"),
        DFA.unpack("\1\u0159"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u015b"),
        DFA.unpack(""),
        DFA.unpack("\1\u015c"),
        DFA.unpack("\1\u015d"),
        DFA.unpack("\1\u015e"),
        DFA.unpack(""),
        DFA.unpack("\1\u015f"),
        DFA.unpack("\1\u0160"),
        DFA.unpack("\1\u0161"),
        DFA.unpack("\1\u0162"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0164"),
        DFA.unpack("\1\u0165"),
        DFA.unpack(""),
        DFA.unpack("\1\u0166"),
        DFA.unpack("\1\u0167"),
        DFA.unpack("\1\u0168"),
        DFA.unpack("\1\u0169"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u016b"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u016d"),
        DFA.unpack("\1\u016e"),
        DFA.unpack("\1\u016f"),
        DFA.unpack("\1\u0170"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0172"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u0173"),
        DFA.unpack("\1\u0174"),
        DFA.unpack("\1\u0175"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0176"),
        DFA.unpack("\1\u0177"),
        DFA.unpack("\1\u0178"),
        DFA.unpack("\1\u0179"),
        DFA.unpack(""),
        DFA.unpack("\1\u017a"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u017c"),
        DFA.unpack("\1\u017d"),
        DFA.unpack(""),
        DFA.unpack("\1\u017e"),
        DFA.unpack("\1\u017f"),
        DFA.unpack("\1\u0180"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0182"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u0185\7\110"
        ),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u018a"),
        DFA.unpack("\1\u018b"),
        DFA.unpack("\1\u018c"),
        DFA.unpack("\1\u018d"),
        DFA.unpack("\1\u018e"),
        DFA.unpack(""),
        DFA.unpack("\1\u018f"),
        DFA.unpack("\1\u0190"),
        DFA.unpack("\1\u0191"),
        DFA.unpack("\1\u0192"),
        DFA.unpack("\1\u0193"),
        DFA.unpack("\1\u0194"),
        DFA.unpack(""),
        DFA.unpack("\1\u0195"),
        DFA.unpack(""),
        DFA.unpack("\1\u0196"),
        DFA.unpack("\1\u0197"),
        DFA.unpack("\1\u0198"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u0199\7\110"
        ),
        DFA.unpack(""),
        DFA.unpack("\1\u019a"),
        DFA.unpack("\1\u019b"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u019e"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01a0"),
        DFA.unpack("\1\u01a1"),
        DFA.unpack(""),
        DFA.unpack("\1\u01a2"),
        DFA.unpack("\1\u01a3"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01a5"),
        DFA.unpack("\1\u01a6"),
        DFA.unpack(""),
        DFA.unpack("\1\u01a7"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01a8"),
        DFA.unpack("\1\u01a9"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\u01aa\1\uffff\32\110"),
        DFA.unpack("\1\u01ac"),
        DFA.unpack("\1\u01ad"),
        DFA.unpack("\1\u01ae"),
        DFA.unpack("\1\u01af"),
        DFA.unpack("\1\u01b0"),
        DFA.unpack("\1\u01b1"),
        DFA.unpack("\1\u01b2"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01b3"),
        DFA.unpack("\1\u01b4"),
        DFA.unpack("\1\u01b5"),
        DFA.unpack("\1\u01b6"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01b8"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01b9"),
        DFA.unpack(""),
        DFA.unpack("\1\u01ba"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01bb"),
        DFA.unpack("\1\u01bc"),
        DFA.unpack(""),
        DFA.unpack("\1\u01bd"),
        DFA.unpack("\1\u01be"),
        DFA.unpack("\1\u01bf"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01c1"),
        DFA.unpack("\1\u01c2"),
        DFA.unpack(""),
        DFA.unpack("\1\u01c3"),
        DFA.unpack("\1\u01c4"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01c7"),
        DFA.unpack("\1\u01c8"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01ca\1\u01cb"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01cd"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01cf"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d1"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d3"),
        DFA.unpack(""),
        DFA.unpack("\1\u01d4"),
        DFA.unpack("\1\u01d5"),
        DFA.unpack("\1\u01d6"),
        DFA.unpack("\1\u01d7"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01d8"),
        DFA.unpack("\1\u01d9"),
        DFA.unpack(""),
        DFA.unpack("\1\u01da"),
        DFA.unpack("\1\u01db"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u01dd"),
        DFA.unpack(""),
        DFA.unpack("\1\u01de"),
        DFA.unpack(""),
        DFA.unpack("\1\u01df"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e1"),
        DFA.unpack("\1\u01e2"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e4"),
        DFA.unpack("\1\u01e5"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e7"),
        DFA.unpack("\1\u01e8"),
        DFA.unpack(""),
        DFA.unpack("\1\u01e9"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01ea"),
        DFA.unpack(""),
        DFA.unpack("\1\u01eb"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01ed"),
        DFA.unpack("\1\u01ee"),
        DFA.unpack("\1\u01ef"),
        DFA.unpack(""),
        DFA.unpack("\1\u01f0"),
        DFA.unpack("\1\u01f1"),
        DFA.unpack("\1\u01f2"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01f4"),
        DFA.unpack("\1\u01f5"),
        DFA.unpack(""),
        DFA.unpack("\1\u01f6"),
        DFA.unpack("\1\u01f7"),
        DFA.unpack("\1\u01f8"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
    ]

    # class definition for DFA #44

    class DFA44(DFA):
        pass

        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self_.recognizer

            _s = s

            if s == 0:
                LA44_0 = input.LA(1)

                s = -1
                if LA44_0 == 115:
                    s = 1

                elif LA44_0 == 119:
                    s = 2

                elif LA44_0 == 80:
                    s = 3

                elif LA44_0 == 67:
                    s = 4

                elif LA44_0 == 84:
                    s = 5

                elif LA44_0 == 83:
                    s = 6

                elif LA44_0 == 68:
                    s = 7

                elif LA44_0 == 76:
                    s = 8

                elif LA44_0 == 82:
                    s = 9

                elif LA44_0 == 77:
                    s = 10

                elif LA44_0 == 111:
                    s = 11

                elif LA44_0 == 99:
                    s = 12

                elif LA44_0 == 103:
                    s = 13

                elif LA44_0 == 105:
                    s = 14

                elif LA44_0 == 101:
                    s = 15

                elif LA44_0 == 102:
                    s = 16

                elif LA44_0 == 109:
                    s = 17

                elif LA44_0 == 108:
                    s = 18

                elif LA44_0 == 114:
                    s = 19

                elif LA44_0 == 116:
                    s = 20

                elif LA44_0 == 118:
                    s = 21

                elif LA44_0 == 117:
                    s = 22

                elif LA44_0 in {88, 89, 90, 120, 121, 122}:
                    s = 23

                elif LA44_0 == 107:
                    s = 24

                elif LA44_0 == 112:
                    s = 25

                elif LA44_0 == 85:
                    s = 26

                elif LA44_0 == 78:
                    s = 27

                elif LA44_0 == 123:
                    s = 28

                elif LA44_0 == 97:
                    s = 29

                elif LA44_0 == 110:
                    s = 30

                elif LA44_0 == 95:
                    s = 31

                elif LA44_0 == 46:
                    s = 32

                elif LA44_0 == 44:
                    s = 33

                elif LA44_0 == 58:
                    s = 34

                elif LA44_0 == 59:
                    s = 35

                elif LA44_0 == 61:
                    s = 36

                elif LA44_0 == 124:
                    s = 37

                elif LA44_0 == 94:
                    s = 38

                elif LA44_0 == 38:
                    s = 39

                elif LA44_0 == 126:
                    s = 40

                elif LA44_0 == 60:
                    s = 41

                elif LA44_0 == 62:
                    s = 42

                elif LA44_0 == 43:
                    s = 43

                elif LA44_0 == 45:
                    s = 44

                elif LA44_0 == 42:
                    s = 45

                elif LA44_0 == 47:
                    s = 46

                elif LA44_0 == 37:
                    s = 47

                elif LA44_0 == 40:
                    s = 48

                elif LA44_0 == 41:
                    s = 49

                elif LA44_0 == 91:
                    s = 50

                elif LA44_0 == 93:
                    s = 51

                elif LA44_0 == 125:
                    s = 52

                elif LA44_0 == 33:
                    s = 53

                elif LA44_0 == 70:
                    s = 54

                elif LA44_0 == 36:
                    s = 55

                elif (71 <= LA44_0 <= 75) or LA44_0 in {
                    65,
                    66,
                    69,
                    79,
                    81,
                    86,
                    87,
                    98,
                    100,
                    104,
                    106,
                    113,
                }:
                    s = 56

                elif LA44_0 == 39:
                    s = 57

                elif LA44_0 == 34:
                    s = 58

                elif (49 <= LA44_0 <= 57) or LA44_0 in {}:
                    s = 59

                elif LA44_0 == 48:
                    s = 60

                elif LA44_0 == 13:
                    s = 61

                elif LA44_0 == 10:
                    s = 62

                elif LA44_0 == 12:
                    s = 63

                elif LA44_0 in {9, 32}:
                    s = 64

                elif LA44_0 == 35:
                    s = 65

                elif LA44_0 == 92:
                    s = 66

                elif (
                    (0 <= LA44_0 <= 8)
                    or (14 <= LA44_0 <= 31)
                    or (127 <= LA44_0 <= 65535)
                    or LA44_0 in {11, 63, 64, 96}
                ):
                    s = 67

                if s >= 0:
                    return s
            elif s == 1:
                LA44_57 = input.LA(1)

                s = -1
                if (0 <= LA44_57 <= 9) or (14 <= LA44_57 <= 65535) or LA44_57 in {11}:
                    s = 91

                else:
                    s = 67

                if s >= 0:
                    return s
            elif s == 2:
                LA44_58 = input.LA(1)

                s = -1
                if (0 <= LA44_58 <= 9) or (14 <= LA44_58 <= 65535) or LA44_58 in {11}:
                    s = 91

                else:
                    s = 67

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 44, _s, input)
            self_.error(nvae)
            raise nvae


def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain

    main = LexerMain(YarcLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == "__main__":
    main(sys.argv)
