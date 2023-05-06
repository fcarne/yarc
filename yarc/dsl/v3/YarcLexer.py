# $ANTLR 3.5.1 /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g 2023-05-06 18:03:50

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


class YarcLexer(YarcLexerBase):
    grammarFileName = "/media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa22 = self.DFA22(
            self,
            22,
            eot=self.DFA22_eot,
            eof=self.DFA22_eof,
            min=self.DFA22_min,
            max=self.DFA22_max,
            accept=self.DFA22_accept,
            special=self.DFA22_special,
            transition=self.DFA22_transition,
        )

        self.dfa32 = self.DFA32(
            self,
            32,
            eot=self.DFA32_eot,
            eof=self.DFA32_eof,
            min=self.DFA32_min,
            max=self.DFA32_max,
            accept=self.DFA32_accept,
            special=self.DFA32_special,
            transition=self.DFA32_transition,
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

        self.dfa43 = self.DFA43(
            self,
            43,
            eot=self.DFA43_eot,
            eof=self.DFA43_eof,
            min=self.DFA43_min,
            max=self.DFA43_max,
            accept=self.DFA43_accept,
            special=self.DFA43_special,
            transition=self.DFA43_transition,
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

    # $ANTLR start "UNIFORM"
    def mUNIFORM(
        self,
    ):
        try:
            _type = UNIFORM
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:76:13: ( 'Uniform' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:76:15: 'Uniform'
            self.match("Uniform")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNIFORM"

    # $ANTLR start "NORMAL"
    def mNORMAL(
        self,
    ):
        try:
            _type = NORMAL
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:77:13: ( 'Normal' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:77:15: 'Normal'
            self.match("Normal")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NORMAL"

    # $ANTLR start "CHOICE"
    def mCHOICE(
        self,
    ):
        try:
            _type = CHOICE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:78:13: ( 'Choice' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:78:15: 'Choice'
            self.match("Choice")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHOICE"

    # $ANTLR start "SEQUENCE"
    def mSEQUENCE(
        self,
    ):
        try:
            _type = SEQUENCE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:79:13: ( 'Sequence' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:79:15: 'Sequence'
            self.match("Sequence")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEQUENCE"

    # $ANTLR start "LOG_UNIFORM"
    def mLOG_UNIFORM(
        self,
    ):
        try:
            _type = LOG_UNIFORM
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:80:13: ( 'LogUniform' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:80:15: 'LogUniform'
            self.match("LogUniform")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LOG_UNIFORM"

    # $ANTLR start "SNIPPET"
    def mSNIPPET(
        self,
    ):
        try:
            _type = SNIPPET
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:83:9: ( NESTED_CODE ( NEWLINE )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:83:11: NESTED_CODE ( NEWLINE )?
            self.mNESTED_CODE()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:83:23: ( NEWLINE )?
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if LA9_0 in {10, 12, 13}:
                alt9 = 1
            if alt9 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:83:23: NEWLINE
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:85:21: ( LBRACE LBRACE ( options {k=2; greedy=false; } : NESTED_CODE | . )* RBRACE RBRACE )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:86:3: LBRACE LBRACE ( options {k=2; greedy=false; } : NESTED_CODE | . )* RBRACE RBRACE
            self.mLBRACE()

            self.mLBRACE()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:87:5: ( options {k=2; greedy=false; } : NESTED_CODE | . )*
            while True:  # loop10
                alt10 = 3
                LA10_0 = self.input.LA(1)

                if LA10_0 == 125:
                    alt10 = 3
                elif LA10_0 == 123:
                    alt10 = 1
                elif (
                    (0 <= LA10_0 <= 122) or (126 <= LA10_0 <= 65535) or LA10_0 in {124}
                ):
                    alt10 = 2

                if alt10 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:87:37: NESTED_CODE
                    self.mNESTED_CODE()

                elif alt10 == 2:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:87:51: .
                    self.matchAny()

                else:
                    break  # loop10

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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:92:4: ( 'to' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:92:6: 'to'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:93:4: ( 'on' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:93:6: 'on'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:94:4: ( 'at' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:94:6: 'at'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:101:12: ( 'and' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:101:14: 'and'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:102:12: ( 'else' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:102:14: 'else'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:103:12: ( 'false' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:103:14: 'false'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:104:12: ( 'for' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:104:14: 'for'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:105:12: ( 'from' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:105:14: 'from'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:106:12: ( 'if' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:106:14: 'if'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:107:12: ( 'in' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:107:14: 'in'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:108:12: ( 'is' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:108:14: 'is'
            self.match("is")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IS"

    # $ANTLR start "NONE"
    def mNONE(
        self,
    ):
        try:
            _type = NONE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:109:12: ( 'none' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:109:14: 'none'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:110:12: ( 'not' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:110:14: 'not'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:111:12: ( 'or' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:111:14: 'or'
            self.match("or")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"

    # $ANTLR start "TRUE"
    def mTRUE(
        self,
    ):
        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:112:12: ( 'true' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:112:14: 'true'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:113:12: ( '_' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:113:14: '_'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:116:10: ( '.' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:116:12: '.'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:117:10: ( '..' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:117:12: '..'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:118:10: ( '...' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:118:12: '...'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:119:10: ( ',' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:119:12: ','
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:120:10: ( ':' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:120:12: ':'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:121:10: ( ';' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:121:12: ';'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:123:9: ( '=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:123:11: '='
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:124:9: ( '|' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:124:11: '|'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:125:9: ( '^' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:125:11: '^'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:126:9: ( '&' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:126:11: '&'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:127:9: ( '~' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:127:11: '~'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:128:9: ( '<<' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:128:11: '<<'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:129:9: ( '>>' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:129:11: '>>'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:130:9: ( '+' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:130:11: '+'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:131:9: ( '-' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:131:11: '-'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:132:8: ( '*' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:132:10: '*'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:133:9: ( '/' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:133:11: '/'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:134:9: ( '%' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:134:11: '%'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:135:9: ( '//' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:135:11: '//'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:136:9: ( '**' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:136:11: '**'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:138:8: ( '(' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:138:10: '('
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:139:8: ( ')' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:139:10: ')'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:140:8: ( '[' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:140:10: '['
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:141:8: ( ']' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:141:10: ']'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:142:8: ( '{' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:142:10: '{'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:143:8: ( '}' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:143:10: '}'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:145:8: ( '<' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:145:10: '<'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:146:8: ( '>' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:146:10: '>'
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:147:8: ( '==' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:147:10: '=='
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:148:8: ( '>=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:148:10: '>='
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:149:8: ( '<=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:149:10: '<='
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:8: ( '!=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:150:10: '!='
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:11: ( '+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=' | '**=' | '//=' )
            alt11 = 12
            LA11 = self.input.LA(1)
            if LA11 in {43}:
                alt11 = 1
            elif LA11 in {45}:
                alt11 = 2
            elif LA11 in {42}:
                LA11_3 = self.input.LA(2)

                if LA11_3 == 61:
                    alt11 = 3
                elif LA11_3 == 42:
                    alt11 = 11
                else:
                    nvae = NoViableAltException("", 11, 3, self.input)

                    raise nvae

            elif LA11 in {47}:
                LA11_4 = self.input.LA(2)

                if LA11_4 == 61:
                    alt11 = 4
                elif LA11_4 == 47:
                    alt11 = 12
                else:
                    nvae = NoViableAltException("", 11, 4, self.input)

                    raise nvae

            elif LA11 in {37}:
                alt11 = 5
            elif LA11 in {38}:
                alt11 = 6
            elif LA11 in {124}:
                alt11 = 7
            elif LA11 in {94}:
                alt11 = 8
            elif LA11 in {60}:
                alt11 = 9
            elif LA11 in {62}:
                alt11 = 10
            else:
                nvae = NoViableAltException("", 11, 0, self.input)

                raise nvae

            if alt11 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:13: '+='
                self.match("+=")

            elif alt11 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:20: '-='
                self.match("-=")

            elif alt11 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:27: '*='
                self.match("*=")

            elif alt11 == 4:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:33: '/='
                self.match("/=")

            elif alt11 == 5:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:40: '%='
                self.match("%=")

            elif alt11 == 6:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:47: '&='
                self.match("&=")

            elif alt11 == 7:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:54: '|='
                self.match("|=")

            elif alt11 == 8:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:61: '^='
                self.match("^=")

            elif alt11 == 9:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:68: '<<='
                self.match("<<=")

            elif alt11 == 10:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:76: '>>='
                self.match(">>=")

            elif alt11 == 11:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:84: '**='
                self.match("**=")

            elif alt11 == 12:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:92: '//='
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:155:12: ( ID_START ( ID_CONTINUE )* )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:155:14: ID_START ( ID_CONTINUE )*
            self.mID_START()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:155:23: ( ID_CONTINUE )*
            while True:  # loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (
                    (48 <= LA12_0 <= 57)
                    or (65 <= LA12_0 <= 90)
                    or (97 <= LA12_0 <= 122)
                    or LA12_0 in {95}
                ):
                    alt12 = 1

                if alt12 == 1:
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
                    break  # loop12

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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:156:12: ( '$' ID )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:156:14: '$' ID
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:159:7: ( ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )?
            alt15 = 4
            LA15 = self.input.LA(1)
            if LA15 in {85, 117}:
                alt15 = 1
            elif LA15 in {70, 102}:
                LA15_2 = self.input.LA(2)

                if LA15_2 in {82, 114}:
                    alt15 = 2
                elif LA15_2 in {34, 39}:
                    alt15 = 3
            elif LA15 in {82, 114}:
                LA15_3 = self.input.LA(2)

                if LA15_3 in {34, 39}:
                    alt15 = 2
                elif LA15_3 in {70, 102}:
                    alt15 = 3
            if alt15 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:5: ( 'u' | 'U' )
                if self.input.LA(1) in {85, 117}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt15 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:161:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:161:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:161:7: ( 'f' | 'F' )? ( 'r' | 'R' )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:161:7: ( 'f' | 'F' )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if LA13_0 in {70, 102}:
                    alt13 = 1
                if alt13 == 1:
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

            elif alt15 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:162:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:162:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:162:7: ( 'r' | 'R' )? ( 'f' | 'F' )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:162:7: ( 'r' | 'R' )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if LA14_0 in {82, 114}:
                    alt14 = 1
                if alt14 == 1:
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:167:9: ( NON_ZERO_DIGIT ( DIGIT )* | ( '0' )+ | '0' ( 'o' | 'O' ) ( OCT_DIGIT )+ | '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ | '0' ( 'b' | 'B' ) ( BIN_DIGIT )+ )
            alt21 = 5
            LA21_0 = self.input.LA(1)

            if (49 <= LA21_0 <= 57) or LA21_0 in {}:
                alt21 = 1
            elif LA21_0 == 48:
                LA21 = self.input.LA(2)
                if LA21 in {79, 111}:
                    alt21 = 3
                elif LA21 in {88, 120}:
                    alt21 = 4
                elif LA21 in {66, 98}:
                    alt21 = 5
                else:
                    alt21 = 2

            else:
                nvae = NoViableAltException("", 21, 0, self.input)

                raise nvae

            if alt21 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:168:3: NON_ZERO_DIGIT ( DIGIT )*
                self.mNON_ZERO_DIGIT()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:168:18: ( DIGIT )*
                while True:  # loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (48 <= LA16_0 <= 57) or LA16_0 in {}:
                        alt16 = 1

                    if alt16 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop16

            elif alt21 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:168:27: ( '0' )+
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:168:27: ( '0' )+
                cnt17 = 0
                while True:  # loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if LA17_0 == 48:
                        alt17 = 1

                    if alt17 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:168:27: '0'
                        self.match(48)

                    else:
                        if cnt17 >= 1:
                            break  # loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1

            elif alt21 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:169:5: '0' ( 'o' | 'O' ) ( OCT_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {79, 111}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:169:21: ( OCT_DIGIT )+
                cnt18 = 0
                while True:  # loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (48 <= LA18_0 <= 55) or LA18_0 in {}:
                        alt18 = 1

                    if alt18 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if (48 <= self.input.LA(1) <= 55) or self.input.LA(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        if cnt18 >= 1:
                            break  # loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1

            elif alt21 == 4:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:170:5: '0' ( 'x' | 'X' ) ( HEX_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {88, 120}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:170:21: ( HEX_DIGIT )+
                cnt19 = 0
                while True:  # loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (
                        (48 <= LA19_0 <= 57)
                        or (65 <= LA19_0 <= 70)
                        or (97 <= LA19_0 <= 102)
                        or LA19_0 in {}
                    ):
                        alt19 = 1

                    if alt19 == 1:
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
                        if cnt19 >= 1:
                            break  # loop19

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1

            elif alt21 == 5:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:171:5: '0' ( 'b' | 'B' ) ( BIN_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {66, 98}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:171:21: ( BIN_DIGIT )+
                cnt20 = 0
                while True:  # loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if LA20_0 in {48, 49}:
                        alt20 = 1

                    if alt20 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if self.input.LA(1) in {48, 49}:
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:174:14: ( POINT_FLOAT | EXPONENT_FLOAT )
            alt22 = 2
            alt22 = self.dfa22.predict(self.input)
            if alt22 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:174:16: POINT_FLOAT
                self.mPOINT_FLOAT()

            elif alt22 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:174:30: EXPONENT_FLOAT
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:177:8: ( ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:178:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:178:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )?
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt24 = 3
            LA24 = self.input.LA(1)
            if LA24 in {13}:
                LA24_1 = self.input.LA(2)

                if LA24_1 == 10:
                    alt24 = 1
                else:
                    alt24 = 2

            elif LA24 in {10}:
                alt24 = 1
            elif LA24 in {12}:
                alt24 = 3
            else:
                nvae = NoViableAltException("", 24, 0, self.input)

                raise nvae

            if alt24 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:5: ( '\\r' )? '\\n'
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:5: ( '\\r' )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if LA23_0 == 13:
                    alt23 = 1
                if alt23 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:5: '\\r'
                    self.match(13)

                self.match(10)

            elif alt24 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:18: '\\r'
                self.match(13)

            elif alt24 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:25: '\\f'
                self.match(12)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:31: ( SPACES )?
            alt25 = 2
            LA25_0 = self.input.LA(1)

            if LA25_0 in {9, 32}:
                alt25 = 1
            if alt25 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:31: SPACES
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:184:9: ( ( SPACES | COMMENT | LINE_JOINING ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:184:11: ( SPACES | COMMENT | LINE_JOINING )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:184:11: ( SPACES | COMMENT | LINE_JOINING )
            alt26 = 3
            LA26 = self.input.LA(1)
            if LA26 in {9, 32}:
                alt26 = 1
            elif LA26 in {35}:
                alt26 = 2
            elif LA26 in {92}:
                alt26 = 3
            else:
                nvae = NoViableAltException("", 26, 0, self.input)

                raise nvae

            if alt26 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:184:13: SPACES
                self.mSPACES()

            elif alt26 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:184:22: COMMENT
                self.mCOMMENT()

            elif alt26 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:184:32: LINE_JOINING
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:185:9: ( . )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:185:11: .
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:188:22: ( '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\'' | '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"' )
            alt29 = 2
            LA29_0 = self.input.LA(1)

            if LA29_0 == 39:
                alt29 = 1
            elif LA29_0 == 34:
                alt29 = 2
            else:
                nvae = NoViableAltException("", 29, 0, self.input)

                raise nvae

            if alt29 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:189:3: '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\''
                self.match(39)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:189:8: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )*
                while True:  # loop27
                    alt27 = 3
                    LA27_0 = self.input.LA(1)

                    if LA27_0 == 92:
                        alt27 = 1
                    elif (
                        (0 <= LA27_0 <= 9)
                        or (14 <= LA27_0 <= 38)
                        or (40 <= LA27_0 <= 91)
                        or (93 <= LA27_0 <= 65535)
                        or LA27_0 in {11}
                    ):
                        alt27 = 2

                    if alt27 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:189:9: STRING_ESCAPE_SEQ
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt27 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:189:29: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' )
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
                        break  # loop27

                self.match(39)

            elif alt29 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:5: '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"'
                self.match(34)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:9: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )*
                while True:  # loop28
                    alt28 = 3
                    LA28_0 = self.input.LA(1)

                    if LA28_0 == 92:
                        alt28 = 1
                    elif (
                        (0 <= LA28_0 <= 9)
                        or (14 <= LA28_0 <= 33)
                        or (35 <= LA28_0 <= 91)
                        or (93 <= LA28_0 <= 65535)
                        or LA28_0 in {11}
                    ):
                        alt28 = 2

                    if alt28 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:10: STRING_ESCAPE_SEQ
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt28 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:30: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' )
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
                        break  # loop28

                self.match(34)

        finally:
            pass

    # $ANTLR end "SHORT_STRING"

    # $ANTLR start "STRING_ESCAPE_SEQ"
    def mSTRING_ESCAPE_SEQ(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:192:28: ( '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' ) | '\\\\' NEWLINE )
            alt30 = 2
            LA30_0 = self.input.LA(1)

            if LA30_0 == 92:
                LA30_1 = self.input.LA(2)

                if (
                    (0 <= LA30_1 <= 8)
                    or (14 <= LA30_1 <= 31)
                    or (33 <= LA30_1 <= 65535)
                    or LA30_1 in {11}
                ):
                    alt30 = 1
                elif LA30_1 in {10, 12, 13}:
                    alt30 = 2
                else:
                    nvae = NoViableAltException("", 30, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 30, 0, self.input)

                raise nvae

            if alt30 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:192:30: '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' )
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

            elif alt30 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:192:72: '\\\\' NEWLINE
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:194:25: ( '1' .. '9' )
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:195:25: ( '0' .. '9' )
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:196:25: ( '0' .. '7' )
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:197:25: ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:198:25: ( '0' | '1' )
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:25: ( ( INT_PART )? FRACTION | INT_PART '.' )
            alt32 = 2
            alt32 = self.dfa32.predict(self.input)
            if alt32 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:27: ( INT_PART )? FRACTION
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:27: ( INT_PART )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (48 <= LA31_0 <= 57) or LA31_0 in {}:
                    alt31 = 1
                if alt31 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:27: INT_PART
                    self.mINT_PART()

                self.mFRACTION()

            elif alt32 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:48: INT_PART '.'
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:25: ( ( INT_PART | POINT_FLOAT ) EXPONENT )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:27: ( INT_PART | POINT_FLOAT ) EXPONENT
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:27: ( INT_PART | POINT_FLOAT )
            alt33 = 2
            alt33 = self.dfa33.predict(self.input)
            if alt33 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:29: INT_PART
                self.mINT_PART()

            elif alt33 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:40: POINT_FLOAT
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:202:25: ( ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:202:27: ( DIGIT )+
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:202:27: ( DIGIT )+
            cnt34 = 0
            while True:  # loop34
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (48 <= LA34_0 <= 57) or LA34_0 in {}:
                    alt34 = 1

                if alt34 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt34 >= 1:
                        break  # loop34

                    eee = EarlyExitException(34, self.input)
                    raise eee

                cnt34 += 1

        finally:
            pass

    # $ANTLR end "INT_PART"

    # $ANTLR start "FRACTION"
    def mFRACTION(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:203:25: ( '.' ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:203:27: '.' ( DIGIT )+
            self.match(46)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:203:31: ( DIGIT )+
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

    # $ANTLR end "FRACTION"

    # $ANTLR start "EXPONENT"
    def mEXPONENT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:204:25: ( ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:204:27: ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+
            if self.input.LA(1) in {69, 101}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:204:39: ( '+' | '-' )?
            alt36 = 2
            LA36_0 = self.input.LA(1)

            if LA36_0 in {43, 45}:
                alt36 = 1
            if alt36 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                if self.input.LA(1) in {43, 45}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:204:52: ( DIGIT )+
            cnt37 = 0
            while True:  # loop37
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (48 <= LA37_0 <= 57) or LA37_0 in {}:
                    alt37 = 1

                if alt37 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt37 >= 1:
                        break  # loop37

                    eee = EarlyExitException(37, self.input)
                    raise eee

                cnt37 += 1

        finally:
            pass

    # $ANTLR end "EXPONENT"

    # $ANTLR start "ID_START"
    def mID_START(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:206:22: ( UNDERSCORE | LETTER )
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:207:22: ( ID_START | DIGIT )
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:208:22: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:23: ( ( ' ' | '\\t' )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:25: ( ' ' | '\\t' )+
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:210:25: ( ' ' | '\\t' )+
            cnt38 = 0
            while True:  # loop38
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if LA38_0 in {9, 32}:
                    alt38 = 1

                if alt38 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if self.input.LA(1) in {9, 32}:
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

    # $ANTLR end "SPACES"

    # $ANTLR start "COMMENT"
    def mCOMMENT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:211:23: ( '#' (~ ( '\\r' | '\\n' | '\\f' ) )* )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:211:25: '#' (~ ( '\\r' | '\\n' | '\\f' ) )*
            self.match(35)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:211:29: (~ ( '\\r' | '\\n' | '\\f' ) )*
            while True:  # loop39
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (0 <= LA39_0 <= 9) or (14 <= LA39_0 <= 65535) or LA39_0 in {11}:
                    alt39 = 1

                if alt39 == 1:
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
                    break  # loop39

        finally:
            pass

    # $ANTLR end "COMMENT"

    # $ANTLR start "LINE_JOINING"
    def mLINE_JOINING(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:23: ( '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:25: '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            self.match(92)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:30: ( SPACES )?
            alt40 = 2
            LA40_0 = self.input.LA(1)

            if LA40_0 in {9, 32}:
                alt40 = 1
            if alt40 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:30: SPACES
                self.mSPACES()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:38: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt42 = 3
            LA42 = self.input.LA(1)
            if LA42 in {13}:
                LA42_1 = self.input.LA(2)

                if LA42_1 == 10:
                    alt42 = 1
                else:
                    alt42 = 2

            elif LA42 in {10}:
                alt42 = 1
            elif LA42 in {12}:
                alt42 = 3
            else:
                nvae = NoViableAltException("", 42, 0, self.input)

                raise nvae

            if alt42 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:40: ( '\\r' )? '\\n'
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:40: ( '\\r' )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if LA41_0 == 13:
                    alt41 = 1
                if alt41 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:40: '\\r'
                    self.match(13)

                self.match(10)

            elif alt42 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:53: '\\r'
                self.match(13)

            elif alt42 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:60: '\\f'
                self.match(12)

        finally:
            pass

    # $ANTLR end "LINE_JOINING"

    def mTokens(self):
        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:8: ( SCENARIO | SETTINGS | STAGE | WRITERS | SHAPES | SHAPES_OR_LIGHTS | CAMERA | LIGHT | LIGHT_TYPE | STEREO | MATERIAL | TIMELINE | OPEN | CREATE | GROUP | INSTANTIATE | GET | EDIT | FETCH | MATCH | LIMIT | RECURSIVE | TRANSLATE | CAM_TRANSLATE | ROTATE | SCALE | SEMANTICS | VISIBLE | SIZE | LOOK_AT | UP_AXIS | AXIS | ORDER | SCATTER | ROT_AROUND | PHYSICS | EVERY | FRAMES | TIME | UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM | SNIPPET | TO | ON | AT | AND | ELSE | FALSE | FOR | FROM | IF | IN | IS | NONE | NOT | OR | TRUE | UNDERSCORE | DOT | RANGE | ELLIPSIS | COMMA | COLON | SEMI | ASSIGN | BIT_OR | XOR | BIT_AND | BIT_NOT | LSHIFT | RSHIFT | PLUS | MINUS | MUL | DIV | MOD | IDIV | POWER | LPAREN | RPAREN | LBRACK | RBRACK | LBRACE | RBRACE | LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | AUG_ASSIGN | ID | SETTING_ID | STRING | INTEGER | FLOAT_NUMBER | NEWLINE | SKIP_ | UNKNOWN )
        alt43 = 102
        alt43 = self.dfa43.predict(self.input)
        if alt43 == 1:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:10: SCENARIO
            self.mSCENARIO()

        elif alt43 == 2:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:19: SETTINGS
            self.mSETTINGS()

        elif alt43 == 3:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:28: STAGE
            self.mSTAGE()

        elif alt43 == 4:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:34: WRITERS
            self.mWRITERS()

        elif alt43 == 5:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:42: SHAPES
            self.mSHAPES()

        elif alt43 == 6:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:49: SHAPES_OR_LIGHTS
            self.mSHAPES_OR_LIGHTS()

        elif alt43 == 7:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:66: CAMERA
            self.mCAMERA()

        elif alt43 == 8:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:73: LIGHT
            self.mLIGHT()

        elif alt43 == 9:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:79: LIGHT_TYPE
            self.mLIGHT_TYPE()

        elif alt43 == 10:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:90: STEREO
            self.mSTEREO()

        elif alt43 == 11:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:97: MATERIAL
            self.mMATERIAL()

        elif alt43 == 12:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:106: TIMELINE
            self.mTIMELINE()

        elif alt43 == 13:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:115: OPEN
            self.mOPEN()

        elif alt43 == 14:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:120: CREATE
            self.mCREATE()

        elif alt43 == 15:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:127: GROUP
            self.mGROUP()

        elif alt43 == 16:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:133: INSTANTIATE
            self.mINSTANTIATE()

        elif alt43 == 17:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:145: GET
            self.mGET()

        elif alt43 == 18:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:149: EDIT
            self.mEDIT()

        elif alt43 == 19:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:154: FETCH
            self.mFETCH()

        elif alt43 == 20:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:160: MATCH
            self.mMATCH()

        elif alt43 == 21:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:166: LIMIT
            self.mLIMIT()

        elif alt43 == 22:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:172: RECURSIVE
            self.mRECURSIVE()

        elif alt43 == 23:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:182: TRANSLATE
            self.mTRANSLATE()

        elif alt43 == 24:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:192: CAM_TRANSLATE
            self.mCAM_TRANSLATE()

        elif alt43 == 25:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:206: ROTATE
            self.mROTATE()

        elif alt43 == 26:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:213: SCALE
            self.mSCALE()

        elif alt43 == 27:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:219: SEMANTICS
            self.mSEMANTICS()

        elif alt43 == 28:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:229: VISIBLE
            self.mVISIBLE()

        elif alt43 == 29:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:237: SIZE
            self.mSIZE()

        elif alt43 == 30:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:242: LOOK_AT
            self.mLOOK_AT()

        elif alt43 == 31:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:250: UP_AXIS
            self.mUP_AXIS()

        elif alt43 == 32:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:258: AXIS
            self.mAXIS()

        elif alt43 == 33:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:263: ORDER
            self.mORDER()

        elif alt43 == 34:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:269: SCATTER
            self.mSCATTER()

        elif alt43 == 35:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:277: ROT_AROUND
            self.mROT_AROUND()

        elif alt43 == 36:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:288: PHYSICS
            self.mPHYSICS()

        elif alt43 == 37:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:296: EVERY
            self.mEVERY()

        elif alt43 == 38:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:302: FRAMES
            self.mFRAMES()

        elif alt43 == 39:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:309: TIME
            self.mTIME()

        elif alt43 == 40:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:314: UNIFORM
            self.mUNIFORM()

        elif alt43 == 41:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:322: NORMAL
            self.mNORMAL()

        elif alt43 == 42:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:329: CHOICE
            self.mCHOICE()

        elif alt43 == 43:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:336: SEQUENCE
            self.mSEQUENCE()

        elif alt43 == 44:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:345: LOG_UNIFORM
            self.mLOG_UNIFORM()

        elif alt43 == 45:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:357: SNIPPET
            self.mSNIPPET()

        elif alt43 == 46:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:365: TO
            self.mTO()

        elif alt43 == 47:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:368: ON
            self.mON()

        elif alt43 == 48:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:371: AT
            self.mAT()

        elif alt43 == 49:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:374: AND
            self.mAND()

        elif alt43 == 50:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:378: ELSE
            self.mELSE()

        elif alt43 == 51:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:383: FALSE
            self.mFALSE()

        elif alt43 == 52:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:389: FOR
            self.mFOR()

        elif alt43 == 53:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:393: FROM
            self.mFROM()

        elif alt43 == 54:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:398: IF
            self.mIF()

        elif alt43 == 55:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:401: IN
            self.mIN()

        elif alt43 == 56:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:404: IS
            self.mIS()

        elif alt43 == 57:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:407: NONE
            self.mNONE()

        elif alt43 == 58:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:412: NOT
            self.mNOT()

        elif alt43 == 59:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:416: OR
            self.mOR()

        elif alt43 == 60:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:419: TRUE
            self.mTRUE()

        elif alt43 == 61:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:424: UNDERSCORE
            self.mUNDERSCORE()

        elif alt43 == 62:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:435: DOT
            self.mDOT()

        elif alt43 == 63:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:439: RANGE
            self.mRANGE()

        elif alt43 == 64:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:445: ELLIPSIS
            self.mELLIPSIS()

        elif alt43 == 65:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:454: COMMA
            self.mCOMMA()

        elif alt43 == 66:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:460: COLON
            self.mCOLON()

        elif alt43 == 67:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:466: SEMI
            self.mSEMI()

        elif alt43 == 68:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:471: ASSIGN
            self.mASSIGN()

        elif alt43 == 69:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:478: BIT_OR
            self.mBIT_OR()

        elif alt43 == 70:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:485: XOR
            self.mXOR()

        elif alt43 == 71:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:489: BIT_AND
            self.mBIT_AND()

        elif alt43 == 72:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:497: BIT_NOT
            self.mBIT_NOT()

        elif alt43 == 73:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:505: LSHIFT
            self.mLSHIFT()

        elif alt43 == 74:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:512: RSHIFT
            self.mRSHIFT()

        elif alt43 == 75:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:519: PLUS
            self.mPLUS()

        elif alt43 == 76:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:524: MINUS
            self.mMINUS()

        elif alt43 == 77:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:530: MUL
            self.mMUL()

        elif alt43 == 78:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:534: DIV
            self.mDIV()

        elif alt43 == 79:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:538: MOD
            self.mMOD()

        elif alt43 == 80:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:542: IDIV
            self.mIDIV()

        elif alt43 == 81:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:547: POWER
            self.mPOWER()

        elif alt43 == 82:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:553: LPAREN
            self.mLPAREN()

        elif alt43 == 83:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:560: RPAREN
            self.mRPAREN()

        elif alt43 == 84:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:567: LBRACK
            self.mLBRACK()

        elif alt43 == 85:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:574: RBRACK
            self.mRBRACK()

        elif alt43 == 86:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:581: LBRACE
            self.mLBRACE()

        elif alt43 == 87:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:588: RBRACE
            self.mRBRACE()

        elif alt43 == 88:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:595: LT
            self.mLT()

        elif alt43 == 89:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:598: GT
            self.mGT()

        elif alt43 == 90:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:601: EQUALS
            self.mEQUALS()

        elif alt43 == 91:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:608: GT_EQ
            self.mGT_EQ()

        elif alt43 == 92:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:614: LT_EQ
            self.mLT_EQ()

        elif alt43 == 93:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:620: NOT_EQ
            self.mNOT_EQ()

        elif alt43 == 94:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:627: AUG_ASSIGN
            self.mAUG_ASSIGN()

        elif alt43 == 95:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:638: ID
            self.mID()

        elif alt43 == 96:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:641: SETTING_ID
            self.mSETTING_ID()

        elif alt43 == 97:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:652: STRING
            self.mSTRING()

        elif alt43 == 98:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:659: INTEGER
            self.mINTEGER()

        elif alt43 == 99:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:667: FLOAT_NUMBER
            self.mFLOAT_NUMBER()

        elif alt43 == 100:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:680: NEWLINE
            self.mNEWLINE()

        elif alt43 == 101:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:688: SKIP_
            self.mSKIP_()

        elif alt43 == 102:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:694: UNKNOWN
            self.mUNKNOWN()

    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack("\3\uffff\1\6\1\uffff\1\6\1\uffff")

    DFA22_eof = DFA.unpack("\7\uffff")

    DFA22_min = DFA.unpack("\2\56\2\60\1\uffff\1\60\1\uffff")

    DFA22_max = DFA.unpack("\1\71\1\145\1\71\1\145\1\uffff\1\145\1\uffff")

    DFA22_accept = DFA.unpack("\4\uffff\1\2\1\uffff\1\1")

    DFA22_special = DFA.unpack("\7\uffff")

    DFA22_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack("\12\5"),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
    ]

    # class definition for DFA #22

    class DFA22(DFA):
        pass

    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack("\3\uffff\1\4\1\uffff")

    DFA32_eof = DFA.unpack("\5\uffff")

    DFA32_min = DFA.unpack("\2\56\1\uffff\1\60\1\uffff")

    DFA32_max = DFA.unpack("\2\71\1\uffff\1\71\1\uffff")

    DFA32_accept = DFA.unpack("\2\uffff\1\1\1\uffff\1\2")

    DFA32_special = DFA.unpack("\5\uffff")

    DFA32_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1"),
        DFA.unpack(""),
        DFA.unpack("\12\2"),
        DFA.unpack(""),
    ]

    # class definition for DFA #32

    class DFA32(DFA):
        pass

    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack("\4\uffff")

    DFA33_eof = DFA.unpack("\4\uffff")

    DFA33_min = DFA.unpack("\2\56\2\uffff")

    DFA33_max = DFA.unpack("\1\71\1\145\2\uffff")

    DFA33_accept = DFA.unpack("\2\uffff\1\2\1\1")

    DFA33_special = DFA.unpack("\4\uffff")

    DFA33_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\2\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(""),
        DFA.unpack(""),
    ]

    # class definition for DFA #33

    class DFA33(DFA):
        pass

    # lookup tables for DFA #43

    DFA43_eot = DFA.unpack(
        "\1\uffff\26\110\1\172\4\110\1\u0080\2\110\1\u0085\1\u0087\3\uffff"
        "\1\u008d\1\u008f\1\u0090\1\u0091\1\uffff\1\u0095\1\u0098\1\u0099"
        "\1\u009a\1\u009c\1\u009e\1\u009f\5\uffff\1\103\1\110\1\103\1\uffff"
        "\2\103\2\u00a7\5\uffff\1\103\1\uffff\4\110\1\uffff\22\110\1\uffff"
        "\2\110\1\u00c6\1\u00c7\5\110\1\u00ce\1\u00cf\1\u00d0\17\110\1\u00e1"
        "\2\110\1\uffff\5\110\2\uffff\1\u00e9\2\110\1\uffff\1\u00ee\14\uffff"
        "\1\u00ef\2\uffff\1\u00f0\4\uffff\1\u00f1\1\uffff\1\u00f2\12\uffff"
        "\2\u00a7\2\uffff\4\110\1\u00f9\25\110\2\uffff\4\110\1\u0114\1\110"
        "\3\uffff\7\110\1\u011d\10\110\1\uffff\2\110\1\u0128\4\110\1\uffff"
        "\1\u012d\1\110\1\u012f\6\uffff\6\110\1\uffff\1\110\1\u0137\2\110"
        "\2\u013a\10\110\1\u0143\1\110\1\u0145\2\110\1\u0145\1\110\1\u0149"
        "\4\110\1\uffff\1\110\1\u014f\1\110\1\u0151\2\110\1\u0154\1\110\1"
        "\uffff\7\110\1\u015d\2\110\1\uffff\4\110\1\uffff\1\u0164\1\uffff"
        "\1\110\1\u0166\4\110\1\u016b\1\uffff\1\110\1\u013a\1\uffff\3\110"
        "\1\u013a\4\110\1\uffff\1\110\1\uffff\1\u0175\2\110\1\uffff\3\110"
        "\1\u017b\1\110\1\uffff\1\u017d\1\uffff\1\u017e\1\u0180\1\uffff\1"
        "\u0181\1\u0182\1\u0183\5\110\1\uffff\6\110\1\uffff\1\110\1\uffff"
        "\3\110\1\u00f9\1\uffff\2\110\1\u0196\1\u0197\1\110\1\u0143\1\u0199"
        "\2\110\1\uffff\2\110\1\u019e\2\110\1\uffff\1\110\2\uffff\1\u0180"
        "\4\uffff\2\110\1\u01a5\7\110\1\u01ad\4\110\1\u00f9\1\u01b2\1\110"
        "\2\uffff\1\110\1\uffff\1\110\1\u0145\2\110\1\uffff\3\110\1\u01bb"
        "\2\110\1\uffff\2\110\1\u01c0\1\u01c1\2\110\1\u01c4\1\uffff\1\u01c5"
        "\1\110\1\u01c8\1\110\1\uffff\1\u0143\1\u01ca\1\u01cb\1\110\1\u01cd"
        "\1\110\1\u01cf\1\110\1\uffff\4\110\2\uffff\2\110\2\uffff\2\110\1"
        "\uffff\1\u01d9\2\uffff\1\110\1\uffff\1\110\1\uffff\1\110\1\u01dd"
        "\2\110\1\u01e0\2\110\2\u01e3\1\uffff\1\u01e4\2\110\1\uffff\1\110"
        "\1\u01cf\1\uffff\1\u01cf\1\110\2\uffff\1\110\1\u01ea\3\110\1\uffff"
        "\3\110\1\u01f1\2\110\1\uffff\3\110\1\u01f7\1\u01cf\1\uffff"
    )

    DFA43_eof = DFA.unpack("\u01f8\uffff")

    DFA43_min = DFA.unpack(
        "\1\0\1\143\1\162\1\154\1\141\1\151\1\145\2\151\1\42\1\141\1\156"
        "\1\141\1\145\1\146\1\144\1\42\1\141\1\151\1\42\1\157\1\151\1\42"
        "\1\60\1\151\1\150\1\42\1\157\1\173\1\156\1\157\1\60\1\56\3\uffff"
        "\4\75\1\uffff\1\74\3\75\1\52\1\57\1\75\5\uffff\1\75\1\42\1\101\1"
        "\uffff\2\0\2\56\5\uffff\1\11\1\uffff\1\141\1\143\1\141\1\172\1\uffff"
        "\1\151\1\141\1\142\1\156\1\154\1\155\1\157\1\162\1\155\1\150\1\145"
        "\1\161\1\163\1\155\2\147\1\143\1\42\1\uffff\1\164\1\145\2\60\1\145"
        "\1\155\1\154\1\157\1\164\3\60\1\151\1\145\1\163\1\164\1\42\1\154"
        "\1\162\1\42\1\164\1\155\1\157\1\143\1\164\1\147\1\141\1\60\1\163"
        "\1\137\1\uffff\1\130\1\156\1\171\1\151\1\162\2\uffff\1\60\1\144"
        "\1\156\1\uffff\1\56\14\uffff\1\75\2\uffff\1\75\4\uffff\1\75\1\uffff"
        "\1\75\12\uffff\2\56\2\uffff\1\156\1\154\1\164\1\141\1\60\1\147\1"
        "\145\1\164\1\156\2\145\1\151\1\145\1\151\1\165\2\145\1\162\1\165"
        "\1\153\1\145\1\150\1\125\1\164\1\145\1\156\2\uffff\1\141\1\145\1"
        "\154\1\165\1\60\1\164\3\uffff\1\164\1\162\1\145\1\143\2\155\1\163"
        "\1\60\1\143\1\151\1\153\1\165\1\141\1\151\1\156\1\145\1\uffff\1"
        "\151\1\141\1\60\1\145\1\163\1\146\1\155\1\uffff\1\60\1\145\1\60"
        "\6\uffff\1\141\1\145\1\164\1\151\2\156\1\uffff\1\145\1\60\2\145"
        "\2\60\1\156\1\162\1\143\1\163\1\154\1\162\2\145\1\60\1\141\1\60"
        "\1\164\1\156\1\60\1\162\1\60\1\164\1\162\1\151\1\160\1\uffff\1\141"
        "\1\60\1\171\1\60\1\150\1\145\1\60\1\145\1\uffff\1\150\1\164\1\137"
        "\1\162\1\164\1\144\1\163\1\60\1\142\1\170\1\uffff\1\155\1\151\1"
        "\157\1\141\1\uffff\1\60\1\uffff\1\162\1\60\1\145\1\156\1\164\1\144"
        "\1\60\1\uffff\1\162\1\60\1\uffff\1\144\1\141\1\145\1\60\1\151\1"
        "\145\1\157\1\156\1\uffff\1\156\1\uffff\1\60\2\151\1\uffff\1\145"
        "\1\141\1\144\1\60\1\156\1\uffff\1\60\1\uffff\2\60\1\uffff\3\60\1"
        "\141\1\163\1\145\1\137\1\154\1\uffff\1\154\1\151\1\141\1\143\1\162"
        "\1\154\1\uffff\1\151\1\uffff\1\162\1\147\1\151\1\60\1\uffff\1\163"
        "\1\145\2\60\1\156\2\60\1\143\1\164\1\uffff\1\146\1\141\1\60\1\137"
        "\1\145\1\uffff\1\164\2\uffff\1\60\4\uffff\1\164\1\151\1\60\1\142"
        "\1\141\1\145\1\163\1\164\1\163\1\155\1\60\1\157\1\137\1\163\1\143"
        "\2\60\1\162\2\uffff\1\145\1\uffff\1\145\1\60\1\157\1\154\1\uffff"
        "\1\164\1\162\1\151\1\60\1\166\1\141\1\uffff\1\157\1\164\2\60\1\151"
        "\1\137\1\60\1\uffff\1\60\1\62\1\60\1\163\1\uffff\3\60\1\162\1\60"
        "\1\162\1\60\1\141\1\uffff\1\145\1\162\1\144\1\145\2\uffff\1\143"
        "\1\155\2\uffff\2\144\1\uffff\1\60\2\uffff\1\155\1\uffff\1\141\1"
        "\uffff\1\164\1\60\1\157\1\171\1\60\1\163\1\141\2\60\1\uffff\1\60"
        "\1\156\1\145\1\uffff\1\165\1\60\1\uffff\1\60\1\164\2\uffff\1\163"
        "\1\60\1\156\1\145\1\154\1\uffff\1\144\1\162\1\141\1\60\1\151\1\164"
        "\1\uffff\1\141\1\145\1\154\2\60\1\uffff"
    )

    DFA43_max = DFA.unpack(
        "\1\uffff\1\164\1\162\1\154\1\171\1\157\1\164\2\157\1\146\1\141\3"
        "\162\1\163\1\166\1\162\1\141\2\157\1\162\1\151\1\160\1\172\1\151"
        "\1\150\1\156\1\157\1\173\1\164\1\157\1\172\1\71\3\uffff\4\75\1\uffff"
        "\1\75\1\76\5\75\5\uffff\1\75\1\162\1\172\1\uffff\2\uffff\2\145\5"
        "\uffff\1\40\1\uffff\1\145\1\164\1\141\1\172\1\uffff\1\151\1\141"
        "\1\142\1\156\1\154\1\155\1\157\1\162\1\155\1\150\1\145\1\161\1\163"
        "\1\155\2\147\1\143\1\47\1\uffff\1\164\1\145\2\172\1\145\1\155\1"
        "\154\1\157\1\164\3\172\1\151\1\145\1\163\1\164\1\157\1\154\1\162"
        "\1\47\1\164\1\155\1\157\1\143\1\164\1\147\1\165\1\172\1\163\1\137"
        "\1\uffff\1\172\1\156\1\171\1\151\1\162\2\uffff\1\172\1\144\1\164"
        "\1\uffff\1\56\14\uffff\1\75\2\uffff\1\75\4\uffff\1\75\1\uffff\1"
        "\75\12\uffff\2\145\2\uffff\1\156\2\164\1\141\1\172\1\147\1\145\1"
        "\164\1\156\2\145\1\151\1\145\1\151\1\165\2\145\1\162\1\165\1\164"
        "\1\145\1\150\1\125\1\164\1\145\1\156\2\uffff\1\141\1\145\1\154\1"
        "\165\1\172\1\164\3\uffff\1\164\1\162\1\145\1\143\2\155\1\163\1\172"
        "\1\143\1\151\1\153\1\165\1\141\1\151\1\156\1\145\1\uffff\1\151\1"
        "\141\1\172\1\145\1\163\1\146\1\155\1\uffff\1\172\1\145\1\172\6\uffff"
        "\1\141\1\145\1\164\1\151\2\156\1\uffff\1\145\1\172\2\145\2\172\1"
        "\156\1\162\1\143\1\163\1\154\1\162\2\145\1\172\1\141\1\172\1\164"
        "\1\156\1\172\1\162\1\172\1\164\1\162\1\151\1\160\1\uffff\1\141\1"
        "\172\1\171\1\172\1\150\1\145\1\172\1\145\1\uffff\1\150\1\164\1\137"
        "\1\162\1\164\1\144\1\163\1\172\1\142\1\170\1\uffff\1\155\1\151\1"
        "\157\1\141\1\uffff\1\172\1\uffff\1\162\1\172\1\145\1\156\1\164\1"
        "\144\1\172\1\uffff\1\162\1\172\1\uffff\1\144\1\141\1\145\1\172\1"
        "\151\1\145\1\157\1\156\1\uffff\1\156\1\uffff\1\172\2\151\1\uffff"
        "\1\145\1\141\1\144\1\172\1\156\1\uffff\1\172\1\uffff\2\172\1\uffff"
        "\3\172\1\141\1\163\1\145\1\137\1\154\1\uffff\1\154\1\151\1\141\1"
        "\143\1\162\1\154\1\uffff\1\151\1\uffff\1\162\1\147\1\151\1\172\1"
        "\uffff\1\163\1\145\2\172\1\156\2\172\1\143\1\164\1\uffff\1\146\1"
        "\141\1\172\1\137\1\145\1\uffff\1\164\2\uffff\1\172\4\uffff\1\164"
        "\1\151\1\172\1\142\1\141\1\145\1\163\1\164\1\163\1\155\1\172\1\157"
        "\1\137\1\163\1\143\2\172\1\162\2\uffff\1\145\1\uffff\1\145\1\172"
        "\1\157\1\154\1\uffff\1\164\1\162\1\151\1\172\1\166\1\141\1\uffff"
        "\1\157\1\164\2\172\1\151\1\137\1\172\1\uffff\1\172\1\63\1\172\1"
        "\163\1\uffff\3\172\1\162\1\172\1\162\1\172\1\141\1\uffff\1\145\1"
        "\162\1\144\1\145\2\uffff\1\143\1\155\2\uffff\2\144\1\uffff\1\172"
        "\2\uffff\1\155\1\uffff\1\141\1\uffff\1\164\1\172\1\157\1\171\1\172"
        "\1\163\1\141\2\172\1\uffff\1\172\1\156\1\145\1\uffff\1\165\1\172"
        "\1\uffff\1\172\1\164\2\uffff\1\163\1\172\1\156\1\145\1\154\1\uffff"
        "\1\144\1\162\1\141\1\172\1\151\1\164\1\uffff\1\141\1\145\1\154\2"
        "\172\1\uffff"
    )

    DFA43_accept = DFA.unpack(
        "\41\uffff\1\101\1\102\1\103\4\uffff\1\110\7\uffff\1\122\1\123\1"
        "\124\1\125\1\127\3\uffff\1\137\4\uffff\3\144\2\145\1\uffff\1\146"
        "\4\uffff\1\137\22\uffff\1\141\36\uffff\1\40\5\uffff\1\126\1\55\3"
        "\uffff\1\75\1\uffff\1\76\1\143\1\101\1\102\1\103\1\132\1\104\1\136"
        "\1\105\1\106\1\107\1\110\1\uffff\1\134\1\130\1\uffff\1\133\1\131"
        "\1\113\1\114\1\uffff\1\115\1\uffff\1\116\1\117\1\122\1\123\1\124"
        "\1\125\1\127\1\135\1\140\1\142\2\uffff\1\144\1\145\32\uffff\1\57"
        "\1\73\6\uffff\1\67\1\66\1\70\20\uffff\1\56\7\uffff\1\60\3\uffff"
        "\1\100\1\77\1\111\1\112\1\121\1\120\6\uffff\1\47\32\uffff\1\21\10"
        "\uffff\1\64\12\uffff\1\41\4\uffff\1\61\1\uffff\1\72\7\uffff\1\35"
        "\2\uffff\1\5\10\uffff\1\6\1\uffff\1\11\3\uffff\1\15\5\uffff\1\22"
        "\1\uffff\1\62\2\uffff\1\65\10\uffff\1\74\6\uffff\1\71\1\uffff\1"
        "\32\4\uffff\1\3\11\uffff\1\10\5\uffff\1\17\1\uffff\1\45\1\23\1\uffff"
        "\1\46\1\63\1\24\1\25\22\uffff\1\7\1\52\1\uffff\1\12\4\uffff\1\16"
        "\6\uffff\1\31\7\uffff\1\51\4\uffff\1\4\10\uffff\1\36\4\uffff\1\34"
        "\1\37\2\uffff\1\50\1\1\2\uffff\1\2\1\uffff\1\14\1\53\1\uffff\1\13"
        "\1\uffff\1\44\11\uffff\1\33\3\uffff\1\26\2\uffff\1\27\2\uffff\1"
        "\42\1\54\5\uffff\1\20\6\uffff\1\43\5\uffff\1\30"
    )

    DFA43_special = DFA.unpack("\1\0\70\uffff\1\1\1\2\u01bd\uffff")

    DFA43_transition = [
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
        DFA.unpack("\1\161\5\uffff\1\162"),
        DFA.unpack(
            "\1\133\4\uffff\1\133\36\uffff\1\132\36\uffff\1\163\1"
            "\132\2\uffff\1\165\5\uffff\1\164"
        ),
        DFA.unpack("\1\167\2\uffff\1\166"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\133\4\uffff\1\133\110\uffff\1\171"),
        DFA.unpack(
            "\12\110\7\uffff\27\110\3\173\4\uffff\1\110\1\uffff\27" "\110\3\173"
        ),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\133\4\uffff\1\133\106\uffff\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack("\1\u0081"),
        DFA.unpack("\1\u0083\5\uffff\1\u0082"),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0086\1\uffff\12\u0088"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008c"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u008e"),
        DFA.unpack(""),
        DFA.unpack("\1\u0093\1\u0094"),
        DFA.unpack("\1\u0097\1\u0096"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u009b\22\uffff\1\u008e"),
        DFA.unpack("\1\u009d\15\uffff\1\u008e"),
        DFA.unpack("\1\u008e"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00a5"),
        DFA.unpack("\1\133\4\uffff\1\133\52\uffff\1\157\37\uffff\1\157"),
        DFA.unpack("\32\u00a6\4\uffff\1\u00a6\1\uffff\32\u00a6"),
        DFA.unpack(""),
        DFA.unpack("\12\133\1\uffff\1\133\2\uffff\ufff2\133"),
        DFA.unpack("\12\133\1\uffff\1\133\2\uffff\ufff2\133"),
        DFA.unpack("\1\u0088\1\uffff\12\u00a8\13\uffff\1\u0088\37\uffff" "\1\u0088"),
        DFA.unpack(
            "\1\u0088\1\uffff\1\u00a9\11\u0088\13\uffff\1\u0088\37" "\uffff\1\u0088"
        ),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\2\u00ab\1\uffff\2\u00ab\22\uffff\1\u00ab"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ad\3\uffff\1\u00ac"),
        DFA.unpack("\1\u00b0\11\uffff\1\u00af\6\uffff\1\u00ae"),
        DFA.unpack("\1\u00b1"),
        DFA.unpack("\1\u00b2"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b3"),
        DFA.unpack("\1\u00b4"),
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
        DFA.unpack("\1\133\4\uffff\1\133"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c4"),
        DFA.unpack("\1\u00c5"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\1\u00c9"),
        DFA.unpack("\1\u00ca"),
        DFA.unpack("\1\u00cb"),
        DFA.unpack("\1\u00cc"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u00cd\7\110"
        ),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00d1"),
        DFA.unpack("\1\u00d2"),
        DFA.unpack("\1\u00d3"),
        DFA.unpack("\1\u00d4"),
        DFA.unpack("\1\133\4\uffff\1\133\71\uffff\1\u00d5\15\uffff\1\u00d6"),
        DFA.unpack("\1\u00d7"),
        DFA.unpack("\1\u00d8"),
        DFA.unpack("\1\133\4\uffff\1\133"),
        DFA.unpack("\1\u00d9"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack("\1\u00dd"),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\1\u00df\23\uffff\1\u00e0"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00e2"),
        DFA.unpack("\1\u00e3"),
        DFA.unpack(""),
        DFA.unpack("\3\u00e4\35\uffff\3\u00e4"),
        DFA.unpack("\1\u00e5"),
        DFA.unpack("\1\u00e6"),
        DFA.unpack("\1\u00e7"),
        DFA.unpack("\1\u00e8"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00ea"),
        DFA.unpack("\1\u00eb\5\uffff\1\u00ec"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ed"),
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
        DFA.unpack("\1\u008e"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008e"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u008e"),
        DFA.unpack(""),
        DFA.unpack("\1\u008e"),
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
        DFA.unpack("\1\u0088\1\uffff\12\u00a8\13\uffff\1\u0088\37\uffff" "\1\u0088"),
        DFA.unpack(
            "\1\u0088\1\uffff\1\u00a9\11\u0088\13\uffff\1\u0088\37" "\uffff\1\u0088"
        ),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f3"),
        DFA.unpack("\1\u00f4\7\uffff\1\u00f5"),
        DFA.unpack("\1\u00f6"),
        DFA.unpack("\1\u00f7"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\16\110" "\1\u00f8\13\110"
        ),
        DFA.unpack("\1\u00fa"),
        DFA.unpack("\1\u00fb"),
        DFA.unpack("\1\u00fc"),
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
        DFA.unpack("\1\u0108\10\uffff\1\u0109"),
        DFA.unpack("\1\u010a"),
        DFA.unpack("\1\u010b"),
        DFA.unpack("\1\u010c"),
        DFA.unpack("\1\u010d"),
        DFA.unpack("\1\u010e"),
        DFA.unpack("\1\u010f"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0110"),
        DFA.unpack("\1\u0111"),
        DFA.unpack("\1\u0112"),
        DFA.unpack("\1\u0113"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0115"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0116"),
        DFA.unpack("\1\u0117"),
        DFA.unpack("\1\u0118"),
        DFA.unpack("\1\u0119"),
        DFA.unpack("\1\u011a"),
        DFA.unpack("\1\u011b"),
        DFA.unpack("\1\u011c"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u011e"),
        DFA.unpack("\1\u011f"),
        DFA.unpack("\1\u0120"),
        DFA.unpack("\1\u0121"),
        DFA.unpack("\1\u0122"),
        DFA.unpack("\1\u0123"),
        DFA.unpack("\1\u0124"),
        DFA.unpack("\1\u0125"),
        DFA.unpack(""),
        DFA.unpack("\1\u0126"),
        DFA.unpack("\1\u0127"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0129"),
        DFA.unpack("\1\u012a"),
        DFA.unpack("\1\u012b"),
        DFA.unpack("\1\u012c"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u012e"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0130"),
        DFA.unpack("\1\u0131"),
        DFA.unpack("\1\u0132"),
        DFA.unpack("\1\u0133"),
        DFA.unpack("\1\u0134"),
        DFA.unpack("\1\u0135"),
        DFA.unpack(""),
        DFA.unpack("\1\u0136"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0138"),
        DFA.unpack("\1\u0139"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u013b"),
        DFA.unpack("\1\u013c"),
        DFA.unpack("\1\u013d"),
        DFA.unpack("\1\u013e"),
        DFA.unpack("\1\u013f"),
        DFA.unpack("\1\u0140"),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\1\u0142"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0144"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0146"),
        DFA.unpack("\1\u0147"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0148"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u014a"),
        DFA.unpack("\1\u014b"),
        DFA.unpack("\1\u014c"),
        DFA.unpack("\1\u014d"),
        DFA.unpack(""),
        DFA.unpack("\1\u014e"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0150"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0152"),
        DFA.unpack("\1\u0153"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0155"),
        DFA.unpack(""),
        DFA.unpack("\1\u0156"),
        DFA.unpack("\1\u0157"),
        DFA.unpack("\1\u0158"),
        DFA.unpack("\1\u0159"),
        DFA.unpack("\1\u015a"),
        DFA.unpack("\1\u015b"),
        DFA.unpack("\1\u015c"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u015e"),
        DFA.unpack("\1\u015f"),
        DFA.unpack(""),
        DFA.unpack("\1\u0160"),
        DFA.unpack("\1\u0161"),
        DFA.unpack("\1\u0162"),
        DFA.unpack("\1\u0163"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u0165"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0167"),
        DFA.unpack("\1\u0168"),
        DFA.unpack("\1\u0169"),
        DFA.unpack("\1\u016a"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u016c"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u016d"),
        DFA.unpack("\1\u016e"),
        DFA.unpack("\1\u016f"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0170"),
        DFA.unpack("\1\u0171"),
        DFA.unpack("\1\u0172"),
        DFA.unpack("\1\u0173"),
        DFA.unpack(""),
        DFA.unpack("\1\u0174"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0176"),
        DFA.unpack("\1\u0177"),
        DFA.unpack(""),
        DFA.unpack("\1\u0178"),
        DFA.unpack("\1\u0179"),
        DFA.unpack("\1\u017a"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u017c"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u017f\7\110"
        ),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0184"),
        DFA.unpack("\1\u0185"),
        DFA.unpack("\1\u0186"),
        DFA.unpack("\1\u0187"),
        DFA.unpack("\1\u0188"),
        DFA.unpack(""),
        DFA.unpack("\1\u0189"),
        DFA.unpack("\1\u018a"),
        DFA.unpack("\1\u018b"),
        DFA.unpack("\1\u018c"),
        DFA.unpack("\1\u018d"),
        DFA.unpack("\1\u018e"),
        DFA.unpack(""),
        DFA.unpack("\1\u018f"),
        DFA.unpack(""),
        DFA.unpack("\1\u0190"),
        DFA.unpack("\1\u0191"),
        DFA.unpack("\1\u0192"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u0193\7\110"
        ),
        DFA.unpack(""),
        DFA.unpack("\1\u0194"),
        DFA.unpack("\1\u0195"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0198"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u019a"),
        DFA.unpack("\1\u019b"),
        DFA.unpack(""),
        DFA.unpack("\1\u019c"),
        DFA.unpack("\1\u019d"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u019f"),
        DFA.unpack("\1\u01a0"),
        DFA.unpack(""),
        DFA.unpack("\1\u01a1"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01a2"),
        DFA.unpack("\1\u01a3"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\u01a4\1\uffff\32\110"),
        DFA.unpack("\1\u01a6"),
        DFA.unpack("\1\u01a7"),
        DFA.unpack("\1\u01a8"),
        DFA.unpack("\1\u01a9"),
        DFA.unpack("\1\u01aa"),
        DFA.unpack("\1\u01ab"),
        DFA.unpack("\1\u01ac"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01ae"),
        DFA.unpack("\1\u01af"),
        DFA.unpack("\1\u01b0"),
        DFA.unpack("\1\u01b1"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01b3"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01b4"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b5"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01b6"),
        DFA.unpack("\1\u01b7"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b8"),
        DFA.unpack("\1\u01b9"),
        DFA.unpack("\1\u01ba"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01bc"),
        DFA.unpack("\1\u01bd"),
        DFA.unpack(""),
        DFA.unpack("\1\u01be"),
        DFA.unpack("\1\u01bf"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01c2"),
        DFA.unpack("\1\u01c3"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01c6\1\u01c7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01c9"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01cc"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01ce"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d0"),
        DFA.unpack(""),
        DFA.unpack("\1\u01d1"),
        DFA.unpack("\1\u01d2"),
        DFA.unpack("\1\u01d3"),
        DFA.unpack("\1\u01d4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01d5"),
        DFA.unpack("\1\u01d6"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01d7"),
        DFA.unpack("\1\u01d8"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01da"),
        DFA.unpack(""),
        DFA.unpack("\1\u01db"),
        DFA.unpack(""),
        DFA.unpack("\1\u01dc"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01de"),
        DFA.unpack("\1\u01df"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e1"),
        DFA.unpack("\1\u01e2"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e5"),
        DFA.unpack("\1\u01e6"),
        DFA.unpack(""),
        DFA.unpack("\1\u01e7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e8"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01e9"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01eb"),
        DFA.unpack("\1\u01ec"),
        DFA.unpack("\1\u01ed"),
        DFA.unpack(""),
        DFA.unpack("\1\u01ee"),
        DFA.unpack("\1\u01ef"),
        DFA.unpack("\1\u01f0"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01f2"),
        DFA.unpack("\1\u01f3"),
        DFA.unpack(""),
        DFA.unpack("\1\u01f4"),
        DFA.unpack("\1\u01f5"),
        DFA.unpack("\1\u01f6"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
    ]

    # class definition for DFA #43

    class DFA43(DFA):
        pass

        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self_.recognizer

            _s = s

            if s == 0:
                LA43_0 = input.LA(1)

                s = -1
                if LA43_0 == 115:
                    s = 1

                elif LA43_0 == 119:
                    s = 2

                elif LA43_0 == 80:
                    s = 3

                elif LA43_0 == 67:
                    s = 4

                elif LA43_0 == 84:
                    s = 5

                elif LA43_0 == 83:
                    s = 6

                elif LA43_0 == 68:
                    s = 7

                elif LA43_0 == 76:
                    s = 8

                elif LA43_0 == 82:
                    s = 9

                elif LA43_0 == 77:
                    s = 10

                elif LA43_0 == 111:
                    s = 11

                elif LA43_0 == 99:
                    s = 12

                elif LA43_0 == 103:
                    s = 13

                elif LA43_0 == 105:
                    s = 14

                elif LA43_0 == 101:
                    s = 15

                elif LA43_0 == 102:
                    s = 16

                elif LA43_0 == 109:
                    s = 17

                elif LA43_0 == 108:
                    s = 18

                elif LA43_0 == 114:
                    s = 19

                elif LA43_0 == 116:
                    s = 20

                elif LA43_0 == 118:
                    s = 21

                elif LA43_0 == 117:
                    s = 22

                elif LA43_0 in {88, 89, 90, 120, 121, 122}:
                    s = 23

                elif LA43_0 == 107:
                    s = 24

                elif LA43_0 == 112:
                    s = 25

                elif LA43_0 == 85:
                    s = 26

                elif LA43_0 == 78:
                    s = 27

                elif LA43_0 == 123:
                    s = 28

                elif LA43_0 == 97:
                    s = 29

                elif LA43_0 == 110:
                    s = 30

                elif LA43_0 == 95:
                    s = 31

                elif LA43_0 == 46:
                    s = 32

                elif LA43_0 == 44:
                    s = 33

                elif LA43_0 == 58:
                    s = 34

                elif LA43_0 == 59:
                    s = 35

                elif LA43_0 == 61:
                    s = 36

                elif LA43_0 == 124:
                    s = 37

                elif LA43_0 == 94:
                    s = 38

                elif LA43_0 == 38:
                    s = 39

                elif LA43_0 == 126:
                    s = 40

                elif LA43_0 == 60:
                    s = 41

                elif LA43_0 == 62:
                    s = 42

                elif LA43_0 == 43:
                    s = 43

                elif LA43_0 == 45:
                    s = 44

                elif LA43_0 == 42:
                    s = 45

                elif LA43_0 == 47:
                    s = 46

                elif LA43_0 == 37:
                    s = 47

                elif LA43_0 == 40:
                    s = 48

                elif LA43_0 == 41:
                    s = 49

                elif LA43_0 == 91:
                    s = 50

                elif LA43_0 == 93:
                    s = 51

                elif LA43_0 == 125:
                    s = 52

                elif LA43_0 == 33:
                    s = 53

                elif LA43_0 == 70:
                    s = 54

                elif LA43_0 == 36:
                    s = 55

                elif (71 <= LA43_0 <= 75) or LA43_0 in {
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

                elif LA43_0 == 39:
                    s = 57

                elif LA43_0 == 34:
                    s = 58

                elif (49 <= LA43_0 <= 57) or LA43_0 in {}:
                    s = 59

                elif LA43_0 == 48:
                    s = 60

                elif LA43_0 == 13:
                    s = 61

                elif LA43_0 == 10:
                    s = 62

                elif LA43_0 == 12:
                    s = 63

                elif LA43_0 in {9, 32}:
                    s = 64

                elif LA43_0 == 35:
                    s = 65

                elif LA43_0 == 92:
                    s = 66

                elif (
                    (0 <= LA43_0 <= 8)
                    or (14 <= LA43_0 <= 31)
                    or (127 <= LA43_0 <= 65535)
                    or LA43_0 in {11, 63, 64, 96}
                ):
                    s = 67

                if s >= 0:
                    return s
            elif s == 1:
                LA43_57 = input.LA(1)

                s = -1
                if (0 <= LA43_57 <= 9) or (14 <= LA43_57 <= 65535) or LA43_57 in {11}:
                    s = 91

                else:
                    s = 67

                if s >= 0:
                    return s
            elif s == 2:
                LA43_58 = input.LA(1)

                s = -1
                if (0 <= LA43_58 <= 9) or (14 <= LA43_58 <= 65535) or LA43_58 in {11}:
                    s = 91

                else:
                    s = 67

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 43, _s, input)
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
