# $ANTLR 3.5.3 YarcLexer.g 2023-06-06 20:50:58

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
COLON = 14
COMBINE = 15
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
MATERIAL_ = 68
MINUS = 69
MOD = 70
MOVE_TO_CAM = 71
MUL = 72
NESTED_CODE = 73
NEWLINE = 74
NONE = 75
NON_ZERO_DIGIT = 76
NOT = 77
NOT_EQ = 78
OCT_DIGIT = 79
ON = 80
OPEN = 81
OR = 82
ORDER = 83
PHYSICS = 84
PIVOT = 85
PLUS = 86
POINT_FLOAT = 87
POWER = 88
RANGE = 89
RBRACE = 90
RBRACK = 91
RECURSIVE = 92
ROTATE = 93
ROT_AROUND = 94
RPAREN = 95
RSHIFT = 96
SCALE = 97
SCATTER = 98
SCENARIO = 99
SEMANTICS = 100
SEMI = 101
SETTINGS = 102
SETTING_ID = 103
SHAPE = 104
SHORT_STRING = 105
SIZE = 106
SKIP_ = 107
SNIPPET = 108
SPACES = 109
STAGE = 110
STEP = 111
STEREO = 112
STRING = 113
STRING_ESCAPE_SEQ = 114
TIME = 115
TIMELINE = 116
TO = 117
TRANSLATE = 118
TRUE = 119
UNDERSCORE = 120
UNKNOWN = 121
UP_AXIS = 122
VISIBLE = 123
WRITERS = 124
XOR = 125

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
    14: "COLON",
    15: "COMBINE",
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
    68: "MATERIAL_",
    69: "MINUS",
    70: "MOD",
    71: "MOVE_TO_CAM",
    72: "MUL",
    73: "NESTED_CODE",
    74: "NEWLINE",
    75: "NONE",
    76: "NON_ZERO_DIGIT",
    77: "NOT",
    78: "NOT_EQ",
    79: "OCT_DIGIT",
    80: "ON",
    81: "OPEN",
    82: "OR",
    83: "ORDER",
    84: "PHYSICS",
    85: "PIVOT",
    86: "PLUS",
    87: "POINT_FLOAT",
    88: "POWER",
    89: "RANGE",
    90: "RBRACE",
    91: "RBRACK",
    92: "RECURSIVE",
    93: "ROTATE",
    94: "ROT_AROUND",
    95: "RPAREN",
    96: "RSHIFT",
    97: "SCALE",
    98: "SCATTER",
    99: "SCENARIO",
    100: "SEMANTICS",
    101: "SEMI",
    102: "SETTINGS",
    103: "SETTING_ID",
    104: "SHAPE",
    105: "SHORT_STRING",
    106: "SIZE",
    107: "SKIP_",
    108: "SNIPPET",
    109: "SPACES",
    110: "STAGE",
    111: "STEP",
    112: "STEREO",
    113: "STRING",
    114: "STRING_ESCAPE_SEQ",
    115: "TIME",
    116: "TIMELINE",
    117: "TO",
    118: "TRANSLATE",
    119: "TRUE",
    120: "UNDERSCORE",
    121: "UNKNOWN",
    122: "UP_AXIS",
    123: "VISIBLE",
    124: "WRITERS",
    125: "XOR",
}
Token.registerTokenNamesMap(tokenNamesMap)


class YarcLexer(YarcLexerBase):
    grammarFileName = "YarcLexer.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa20 = self.DFA20(
            self,
            20,
            eot=self.DFA20_eot,
            eof=self.DFA20_eof,
            min=self.DFA20_min,
            max=self.DFA20_max,
            accept=self.DFA20_accept,
            special=self.DFA20_special,
            transition=self.DFA20_transition,
        )

        self.dfa30 = self.DFA30(
            self,
            30,
            eot=self.DFA30_eot,
            eof=self.DFA30_eof,
            min=self.DFA30_min,
            max=self.DFA30_max,
            accept=self.DFA30_accept,
            special=self.DFA30_special,
            transition=self.DFA30_transition,
        )

        self.dfa31 = self.DFA31(
            self,
            31,
            eot=self.DFA31_eot,
            eof=self.DFA31_eof,
            min=self.DFA31_min,
            max=self.DFA31_max,
            accept=self.DFA31_accept,
            special=self.DFA31_special,
            transition=self.DFA31_transition,
        )

        self.dfa41 = self.DFA41(
            self,
            41,
            eot=self.DFA41_eot,
            eof=self.DFA41_eof,
            min=self.DFA41_min,
            max=self.DFA41_max,
            accept=self.DFA41_accept,
            special=self.DFA41_special,
            transition=self.DFA41_transition,
        )

    # $ANTLR start "SCENARIO"
    def mSCENARIO(
        self,
    ):
        try:
            _type = SCENARIO
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:21:10: ( 'scenario' )
            # YarcLexer.g:21:12: 'scenario'
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

            # YarcLexer.g:22:10: ( 'settings' )
            # YarcLexer.g:22:12: 'settings'
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

            # YarcLexer.g:23:10: ( 'stage' )
            # YarcLexer.g:23:12: 'stage'
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

            # YarcLexer.g:24:10: ( 'writers' )
            # YarcLexer.g:24:12: 'writers'
            self.match("writers")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WRITERS"

    # $ANTLR start "SHAPE"
    def mSHAPE(
        self,
    ):
        try:
            _type = SHAPE
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:27:18: ( 'Plane' | 'Cube' | 'Cone' | 'Torus' | 'Sphere' | 'Cylinder' | 'Disk' )
            alt1 = 7
            LA1 = self.input.LA(1)
            if LA1 in {80}:
                alt1 = 1
            elif LA1 in {67}:
                LA1 = self.input.LA(2)
                if LA1 in {117}:
                    alt1 = 2
                elif LA1 in {111}:
                    alt1 = 3
                elif LA1 in {121}:
                    alt1 = 6
                else:
                    nvae = NoViableAltException("", 1, 2, self.input)

                    raise nvae

            elif LA1 in {84}:
                alt1 = 4
            elif LA1 in {83}:
                alt1 = 5
            elif LA1 in {68}:
                alt1 = 7
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae

            if alt1 == 1:
                # YarcLexer.g:27:20: 'Plane'
                self.match("Plane")

            elif alt1 == 2:
                # YarcLexer.g:27:30: 'Cube'
                self.match("Cube")

            elif alt1 == 3:
                # YarcLexer.g:27:39: 'Cone'
                self.match("Cone")

            elif alt1 == 4:
                # YarcLexer.g:27:48: 'Torus'
                self.match("Torus")

            elif alt1 == 5:
                # YarcLexer.g:27:58: 'Sphere'
                self.match("Sphere")

            elif alt1 == 6:
                # YarcLexer.g:27:69: 'Cylinder'
                self.match("Cylinder")

            elif alt1 == 7:
                # YarcLexer.g:27:82: 'Disk'
                self.match("Disk")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHAPE"

    # $ANTLR start "CAMERA"
    def mCAMERA(
        self,
    ):
        try:
            _type = CAMERA
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:28:18: ( 'Camera' )
            # YarcLexer.g:28:20: 'Camera'
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

            # YarcLexer.g:29:18: ( 'Light' )
            # YarcLexer.g:29:20: 'Light'
            self.match("Light")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LIGHT"

    # $ANTLR start "STEREO"
    def mSTEREO(
        self,
    ):
        try:
            _type = STEREO
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:30:18: ( 'Stereo' )
            # YarcLexer.g:30:20: 'Stereo'
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

            # YarcLexer.g:31:18: ( 'Material' )
            # YarcLexer.g:31:20: 'Material'
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

            # YarcLexer.g:32:18: ( 'Timeline' )
            # YarcLexer.g:32:20: 'Timeline'
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

            # YarcLexer.g:35:13: ( 'open' )
            # YarcLexer.g:35:15: 'open'
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

            # YarcLexer.g:36:13: ( 'create' )
            # YarcLexer.g:36:15: 'create'
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

            # YarcLexer.g:37:13: ( 'group' )
            # YarcLexer.g:37:15: 'group'
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

            # YarcLexer.g:38:13: ( 'instantiate' )
            # YarcLexer.g:38:15: 'instantiate'
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

            # YarcLexer.g:39:13: ( 'get' )
            # YarcLexer.g:39:15: 'get'
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

            # YarcLexer.g:40:13: ( 'edit' )
            # YarcLexer.g:40:15: 'edit'
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

            # YarcLexer.g:44:11: ( 'fetch' )
            # YarcLexer.g:44:13: 'fetch'
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

            # YarcLexer.g:45:11: ( 'match' )
            # YarcLexer.g:45:13: 'match'
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

            # YarcLexer.g:46:11: ( 'limit' )
            # YarcLexer.g:46:13: 'limit'
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

            # YarcLexer.g:47:11: ( 'recursive' )
            # YarcLexer.g:47:13: 'recursive'
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

            # YarcLexer.g:50:15: ( 'translate' )
            # YarcLexer.g:50:17: 'translate'
            self.match("translate")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRANSLATE"

    # $ANTLR start "ROTATE"
    def mROTATE(
        self,
    ):
        try:
            _type = ROTATE
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:51:15: ( 'rotate' )
            # YarcLexer.g:51:17: 'rotate'
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

            # YarcLexer.g:52:15: ( 'scale' )
            # YarcLexer.g:52:17: 'scale'
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

            # YarcLexer.g:53:15: ( 'semantics' )
            # YarcLexer.g:53:17: 'semantics'
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

            # YarcLexer.g:54:15: ( 'visible' )
            # YarcLexer.g:54:17: 'visible'
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

            # YarcLexer.g:55:15: ( 'size' )
            # YarcLexer.g:55:17: 'size'
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

            # YarcLexer.g:56:15: ( 'look_at' )
            # YarcLexer.g:56:17: 'look_at'
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

            # YarcLexer.g:57:15: ( 'up_axis' )
            # YarcLexer.g:57:17: 'up_axis'
            self.match("up_axis")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UP_AXIS"

    # $ANTLR start "PIVOT"
    def mPIVOT(
        self,
    ):
        try:
            _type = PIVOT
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:58:15: ( 'pivot' )
            # YarcLexer.g:58:17: 'pivot'
            self.match("pivot")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PIVOT"

    # $ANTLR start "MATERIAL_"
    def mMATERIAL_(
        self,
    ):
        try:
            _type = MATERIAL_
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:59:15: ( 'material' )
            # YarcLexer.g:59:17: 'material'
            self.match("material")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MATERIAL_"

    # $ANTLR start "AXIS"
    def mAXIS(
        self,
    ):
        try:
            _type = AXIS
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:60:15: ( 'x' | 'y' | 'z' | 'X' | 'Y' | 'Z' )
            # YarcLexer.g:
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

            # YarcLexer.g:61:15: ( AXIS AXIS AXIS )
            # YarcLexer.g:61:17: AXIS AXIS AXIS
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

            # YarcLexer.g:64:13: ( 'scatter_' ( '2d' | '3d' ) )
            # YarcLexer.g:64:15: 'scatter_' ( '2d' | '3d' )
            self.match("scatter_")

            # YarcLexer.g:64:26: ( '2d' | '3d' )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if LA2_0 == 50:
                alt2 = 1
            elif LA2_0 == 51:
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae

            if alt2 == 1:
                # YarcLexer.g:64:27: '2d'
                self.match("2d")

            elif alt2 == 2:
                # YarcLexer.g:64:34: '3d'
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

            # YarcLexer.g:65:13: ( 'rotate_around' )
            # YarcLexer.g:65:15: 'rotate_around'
            self.match("rotate_around")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROT_AROUND"

    # $ANTLR start "MOVE_TO_CAM"
    def mMOVE_TO_CAM(
        self,
    ):
        try:
            _type = MOVE_TO_CAM
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:66:13: ( 'move_to_camera' )
            # YarcLexer.g:66:15: 'move_to_camera'
            self.match("move_to_camera")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOVE_TO_CAM"

    # $ANTLR start "PHYSICS"
    def mPHYSICS(
        self,
    ):
        try:
            _type = PHYSICS
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:67:13: ( 'collider' | 'kinematics' | 'rigid_body' | 'physics_material' )
            alt3 = 4
            LA3 = self.input.LA(1)
            if LA3 in {99}:
                alt3 = 1
            elif LA3 in {107}:
                alt3 = 2
            elif LA3 in {114}:
                alt3 = 3
            elif LA3 in {112}:
                alt3 = 4
            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae

            if alt3 == 1:
                # YarcLexer.g:67:15: 'collider'
                self.match("collider")

            elif alt3 == 2:
                # YarcLexer.g:67:28: 'kinematics'
                self.match("kinematics")

            elif alt3 == 3:
                # YarcLexer.g:67:43: 'rigid_body'
                self.match("rigid_body")

            elif alt3 == 4:
                # YarcLexer.g:67:58: 'physics_material'
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

            # YarcLexer.g:70:8: ( 'every' )
            # YarcLexer.g:70:10: 'every'
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

            # YarcLexer.g:71:8: ( 'frame' ( 's' )? )
            # YarcLexer.g:71:10: 'frame' ( 's' )?
            self.match("frame")

            # YarcLexer.g:71:18: ( 's' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if LA4_0 == 115:
                alt4 = 1
            if alt4 == 1:
                # YarcLexer.g:71:18: 's'
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

            # YarcLexer.g:72:8: ( 'sec' ( 'ond' ( 's' )? )? )
            # YarcLexer.g:72:10: 'sec' ( 'ond' ( 's' )? )?
            self.match("sec")

            # YarcLexer.g:72:16: ( 'ond' ( 's' )? )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if LA6_0 == 111:
                alt6 = 1
            if alt6 == 1:
                # YarcLexer.g:72:17: 'ond' ( 's' )?
                self.match("ond")

                # YarcLexer.g:72:23: ( 's' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if LA5_0 == 115:
                    alt5 = 1
                if alt5 == 1:
                    # YarcLexer.g:72:23: 's'
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

            # YarcLexer.g:75:14: ( 'Uniform' | 'Normal' | 'Choice' | 'Sequence' | 'LogUniform' )
            alt7 = 5
            LA7 = self.input.LA(1)
            if LA7 in {85}:
                alt7 = 1
            elif LA7 in {78}:
                alt7 = 2
            elif LA7 in {67}:
                alt7 = 3
            elif LA7 in {83}:
                alt7 = 4
            elif LA7 in {76}:
                alt7 = 5
            else:
                nvae = NoViableAltException("", 7, 0, self.input)

                raise nvae

            if alt7 == 1:
                # YarcLexer.g:75:16: 'Uniform'
                self.match("Uniform")

            elif alt7 == 2:
                # YarcLexer.g:75:28: 'Normal'
                self.match("Normal")

            elif alt7 == 3:
                # YarcLexer.g:75:39: 'Choice'
                self.match("Choice")

            elif alt7 == 4:
                # YarcLexer.g:75:50: 'Sequence'
                self.match("Sequence")

            elif alt7 == 5:
                # YarcLexer.g:75:63: 'LogUniform'
                self.match("LogUniform")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DISTRIBUTION"

    # $ANTLR start "COMBINE"
    def mCOMBINE(
        self,
    ):
        try:
            _type = COMBINE
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:76:9: ( 'Combine' )
            # YarcLexer.g:76:11: 'Combine'
            self.match("Combine")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMBINE"

    # $ANTLR start "SNIPPET"
    def mSNIPPET(
        self,
    ):
        try:
            _type = SNIPPET
            _channel = DEFAULT_CHANNEL

            # YarcLexer.g:78:9: ( NESTED_CODE )
            # YarcLexer.g:78:11: NESTED_CODE
            self.mNESTED_CODE()

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
            # YarcLexer.g:80:21: ( LBRACE LBRACE ( options {k=2; greedy=false; } : NESTED_CODE | . )* RBRACE RBRACE )
            # YarcLexer.g:81:3: LBRACE LBRACE ( options {k=2; greedy=false; } : NESTED_CODE | . )* RBRACE RBRACE
            self.mLBRACE()

            self.mLBRACE()

            # YarcLexer.g:82:5: ( options {k=2; greedy=false; } : NESTED_CODE | . )*
            while True:  # loop8
                alt8 = 3
                LA8_0 = self.input.LA(1)

                if LA8_0 == 125:
                    alt8 = 3
                elif LA8_0 == 123:
                    alt8 = 1
                elif (0 <= LA8_0 <= 122) or (126 <= LA8_0 <= 65535) or LA8_0 in {124}:
                    alt8 = 2

                if alt8 == 1:
                    # YarcLexer.g:82:37: NESTED_CODE
                    self.mNESTED_CODE()

                elif alt8 == 2:
                    # YarcLexer.g:82:51: .
                    self.matchAny()

                else:
                    break  # loop8

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

            # YarcLexer.g:87:4: ( 'to' )
            # YarcLexer.g:87:6: 'to'
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

            # YarcLexer.g:88:4: ( 'on' )
            # YarcLexer.g:88:6: 'on'
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

            # YarcLexer.g:89:4: ( 'at' )
            # YarcLexer.g:89:6: 'at'
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

            # YarcLexer.g:97:12: ( 'and' )
            # YarcLexer.g:97:14: 'and'
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

            # YarcLexer.g:98:12: ( 'else' )
            # YarcLexer.g:98:14: 'else'
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

            # YarcLexer.g:99:12: ( 'false' )
            # YarcLexer.g:99:14: 'false'
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

            # YarcLexer.g:100:12: ( 'for' )
            # YarcLexer.g:100:14: 'for'
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

            # YarcLexer.g:101:12: ( 'from' )
            # YarcLexer.g:101:14: 'from'
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

            # YarcLexer.g:102:12: ( 'if' )
            # YarcLexer.g:102:14: 'if'
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

            # YarcLexer.g:103:12: ( 'in' )
            # YarcLexer.g:103:14: 'in'
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

            # YarcLexer.g:104:12: ( 'is' )
            # YarcLexer.g:104:14: 'is'
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

            # YarcLexer.g:105:12: ( 'len' )
            # YarcLexer.g:105:14: 'len'
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

            # YarcLexer.g:106:12: ( 'none' )
            # YarcLexer.g:106:14: 'none'
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

            # YarcLexer.g:107:12: ( 'not' )
            # YarcLexer.g:107:14: 'not'
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

            # YarcLexer.g:108:12: ( 'or' )
            # YarcLexer.g:108:14: 'or'
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

            # YarcLexer.g:109:12: ( 'step' )
            # YarcLexer.g:109:14: 'step'
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

            # YarcLexer.g:110:12: ( 'true' )
            # YarcLexer.g:110:14: 'true'
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

            # YarcLexer.g:111:12: ( '_' )
            # YarcLexer.g:111:14: '_'
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

            # YarcLexer.g:114:10: ( '.' )
            # YarcLexer.g:114:12: '.'
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

            # YarcLexer.g:115:10: ( '..' )
            # YarcLexer.g:115:12: '..'
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

            # YarcLexer.g:116:10: ( '...' )
            # YarcLexer.g:116:12: '...'
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

            # YarcLexer.g:117:10: ( ',' )
            # YarcLexer.g:117:12: ','
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

            # YarcLexer.g:118:10: ( ':' )
            # YarcLexer.g:118:12: ':'
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

            # YarcLexer.g:119:10: ( ';' )
            # YarcLexer.g:119:12: ';'
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

            # YarcLexer.g:121:9: ( '=' )
            # YarcLexer.g:121:11: '='
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

            # YarcLexer.g:122:9: ( '|' )
            # YarcLexer.g:122:11: '|'
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

            # YarcLexer.g:123:9: ( '^' )
            # YarcLexer.g:123:11: '^'
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

            # YarcLexer.g:124:9: ( '&' )
            # YarcLexer.g:124:11: '&'
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

            # YarcLexer.g:125:9: ( '~' )
            # YarcLexer.g:125:11: '~'
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

            # YarcLexer.g:126:9: ( '<<' )
            # YarcLexer.g:126:11: '<<'
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

            # YarcLexer.g:127:9: ( '>>' )
            # YarcLexer.g:127:11: '>>'
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

            # YarcLexer.g:128:9: ( '+' )
            # YarcLexer.g:128:11: '+'
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

            # YarcLexer.g:129:9: ( '-' )
            # YarcLexer.g:129:11: '-'
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

            # YarcLexer.g:130:8: ( '*' )
            # YarcLexer.g:130:10: '*'
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

            # YarcLexer.g:131:9: ( '/' )
            # YarcLexer.g:131:11: '/'
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

            # YarcLexer.g:132:9: ( '%' )
            # YarcLexer.g:132:11: '%'
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

            # YarcLexer.g:133:9: ( '//' )
            # YarcLexer.g:133:11: '//'
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

            # YarcLexer.g:134:9: ( '**' )
            # YarcLexer.g:134:11: '**'
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

            # YarcLexer.g:136:8: ( '(' )
            # YarcLexer.g:136:10: '('
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

            # YarcLexer.g:137:8: ( ')' )
            # YarcLexer.g:137:10: ')'
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

            # YarcLexer.g:138:8: ( '[' )
            # YarcLexer.g:138:10: '['
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

            # YarcLexer.g:139:8: ( ']' )
            # YarcLexer.g:139:10: ']'
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

            # YarcLexer.g:140:8: ( '{' )
            # YarcLexer.g:140:10: '{'
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

            # YarcLexer.g:141:8: ( '}' )
            # YarcLexer.g:141:10: '}'
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

            # YarcLexer.g:143:8: ( '<' )
            # YarcLexer.g:143:10: '<'
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

            # YarcLexer.g:144:8: ( '>' )
            # YarcLexer.g:144:10: '>'
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

            # YarcLexer.g:145:8: ( '==' )
            # YarcLexer.g:145:10: '=='
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

            # YarcLexer.g:146:8: ( '>=' )
            # YarcLexer.g:146:10: '>='
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

            # YarcLexer.g:147:8: ( '<=' )
            # YarcLexer.g:147:10: '<='
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

            # YarcLexer.g:148:8: ( '!=' )
            # YarcLexer.g:148:10: '!='
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

            # YarcLexer.g:150:11: ( '+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=' | '**=' | '//=' )
            alt9 = 12
            LA9 = self.input.LA(1)
            if LA9 in {43}:
                alt9 = 1
            elif LA9 in {45}:
                alt9 = 2
            elif LA9 in {42}:
                LA9_3 = self.input.LA(2)

                if LA9_3 == 61:
                    alt9 = 3
                elif LA9_3 == 42:
                    alt9 = 11
                else:
                    nvae = NoViableAltException("", 9, 3, self.input)

                    raise nvae

            elif LA9 in {47}:
                LA9_4 = self.input.LA(2)

                if LA9_4 == 61:
                    alt9 = 4
                elif LA9_4 == 47:
                    alt9 = 12
                else:
                    nvae = NoViableAltException("", 9, 4, self.input)

                    raise nvae

            elif LA9 in {37}:
                alt9 = 5
            elif LA9 in {38}:
                alt9 = 6
            elif LA9 in {124}:
                alt9 = 7
            elif LA9 in {94}:
                alt9 = 8
            elif LA9 in {60}:
                alt9 = 9
            elif LA9 in {62}:
                alt9 = 10
            else:
                nvae = NoViableAltException("", 9, 0, self.input)

                raise nvae

            if alt9 == 1:
                # YarcLexer.g:150:13: '+='
                self.match("+=")

            elif alt9 == 2:
                # YarcLexer.g:150:20: '-='
                self.match("-=")

            elif alt9 == 3:
                # YarcLexer.g:150:27: '*='
                self.match("*=")

            elif alt9 == 4:
                # YarcLexer.g:150:33: '/='
                self.match("/=")

            elif alt9 == 5:
                # YarcLexer.g:150:40: '%='
                self.match("%=")

            elif alt9 == 6:
                # YarcLexer.g:150:47: '&='
                self.match("&=")

            elif alt9 == 7:
                # YarcLexer.g:150:54: '|='
                self.match("|=")

            elif alt9 == 8:
                # YarcLexer.g:150:61: '^='
                self.match("^=")

            elif alt9 == 9:
                # YarcLexer.g:150:68: '<<='
                self.match("<<=")

            elif alt9 == 10:
                # YarcLexer.g:150:76: '>>='
                self.match(">>=")

            elif alt9 == 11:
                # YarcLexer.g:150:84: '**='
                self.match("**=")

            elif alt9 == 12:
                # YarcLexer.g:150:92: '//='
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

            # YarcLexer.g:153:12: ( ID_START ( ID_CONTINUE )* )
            # YarcLexer.g:153:14: ID_START ( ID_CONTINUE )*
            self.mID_START()

            # YarcLexer.g:153:23: ( ID_CONTINUE )*
            while True:  # loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (
                    (48 <= LA10_0 <= 57)
                    or (65 <= LA10_0 <= 90)
                    or (97 <= LA10_0 <= 122)
                    or LA10_0 in {95}
                ):
                    alt10 = 1

                if alt10 == 1:
                    # YarcLexer.g:
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
                    break  # loop10

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

            # YarcLexer.g:154:12: ( '$' ID )
            # YarcLexer.g:154:14: '$' ID
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

            # YarcLexer.g:157:7: ( ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING )
            # YarcLexer.g:158:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING
            # YarcLexer.g:158:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )?
            alt13 = 4
            LA13 = self.input.LA(1)
            if LA13 in {85, 117}:
                alt13 = 1
            elif LA13 in {70, 102}:
                LA13_2 = self.input.LA(2)

                if LA13_2 in {82, 114}:
                    alt13 = 2
                elif LA13_2 in {34, 39}:
                    alt13 = 3
            elif LA13 in {82, 114}:
                LA13_3 = self.input.LA(2)

                if LA13_3 in {34, 39}:
                    alt13 = 2
                elif LA13_3 in {70, 102}:
                    alt13 = 3
            if alt13 == 1:
                # YarcLexer.g:158:5: ( 'u' | 'U' )
                if self.input.LA(1) in {85, 117}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt13 == 2:
                # YarcLexer.g:159:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                pass
                # YarcLexer.g:159:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                # YarcLexer.g:159:7: ( 'f' | 'F' )? ( 'r' | 'R' )
                # YarcLexer.g:159:7: ( 'f' | 'F' )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if LA11_0 in {70, 102}:
                    alt11 = 1
                if alt11 == 1:
                    # YarcLexer.g:
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

            elif alt13 == 3:
                # YarcLexer.g:160:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                pass
                # YarcLexer.g:160:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                # YarcLexer.g:160:7: ( 'r' | 'R' )? ( 'f' | 'F' )
                # YarcLexer.g:160:7: ( 'r' | 'R' )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if LA12_0 in {82, 114}:
                    alt12 = 1
                if alt12 == 1:
                    # YarcLexer.g:
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

            # YarcLexer.g:165:9: ( NON_ZERO_DIGIT ( DIGIT )* | ( '0' )+ | '0' ( 'o' | 'O' ) ( OCT_DIGIT )+ | '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ | '0' ( 'b' | 'B' ) ( BIN_DIGIT )+ )
            alt19 = 5
            LA19_0 = self.input.LA(1)

            if (49 <= LA19_0 <= 57) or LA19_0 in {}:
                alt19 = 1
            elif LA19_0 == 48:
                LA19 = self.input.LA(2)
                if LA19 in {79, 111}:
                    alt19 = 3
                elif LA19 in {88, 120}:
                    alt19 = 4
                elif LA19 in {66, 98}:
                    alt19 = 5
                else:
                    alt19 = 2

            else:
                nvae = NoViableAltException("", 19, 0, self.input)

                raise nvae

            if alt19 == 1:
                # YarcLexer.g:166:3: NON_ZERO_DIGIT ( DIGIT )*
                self.mNON_ZERO_DIGIT()

                # YarcLexer.g:166:18: ( DIGIT )*
                while True:  # loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (48 <= LA14_0 <= 57) or LA14_0 in {}:
                        alt14 = 1

                    if alt14 == 1:
                        # YarcLexer.g:
                        if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop14

            elif alt19 == 2:
                # YarcLexer.g:166:27: ( '0' )+
                pass
                # YarcLexer.g:166:27: ( '0' )+
                cnt15 = 0
                while True:  # loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if LA15_0 == 48:
                        alt15 = 1

                    if alt15 == 1:
                        # YarcLexer.g:166:27: '0'
                        self.match(48)

                    else:
                        if cnt15 >= 1:
                            break  # loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1

            elif alt19 == 3:
                # YarcLexer.g:167:5: '0' ( 'o' | 'O' ) ( OCT_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {79, 111}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # YarcLexer.g:167:21: ( OCT_DIGIT )+
                cnt16 = 0
                while True:  # loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (48 <= LA16_0 <= 55) or LA16_0 in {}:
                        alt16 = 1

                    if alt16 == 1:
                        # YarcLexer.g:
                        if (48 <= self.input.LA(1) <= 55) or self.input.LA(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        if cnt16 >= 1:
                            break  # loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1

            elif alt19 == 4:
                # YarcLexer.g:168:5: '0' ( 'x' | 'X' ) ( HEX_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {88, 120}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # YarcLexer.g:168:21: ( HEX_DIGIT )+
                cnt17 = 0
                while True:  # loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (
                        (48 <= LA17_0 <= 57)
                        or (65 <= LA17_0 <= 70)
                        or (97 <= LA17_0 <= 102)
                        or LA17_0 in {}
                    ):
                        alt17 = 1

                    if alt17 == 1:
                        # YarcLexer.g:
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
                        if cnt17 >= 1:
                            break  # loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1

            elif alt19 == 5:
                # YarcLexer.g:169:5: '0' ( 'b' | 'B' ) ( BIN_DIGIT )+
                self.match(48)

                if self.input.LA(1) in {66, 98}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # YarcLexer.g:169:21: ( BIN_DIGIT )+
                cnt18 = 0
                while True:  # loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if LA18_0 in {48, 49}:
                        alt18 = 1

                    if alt18 == 1:
                        # YarcLexer.g:
                        if self.input.LA(1) in {48, 49}:
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

            # YarcLexer.g:172:14: ( POINT_FLOAT | EXPONENT_FLOAT )
            alt20 = 2
            alt20 = self.dfa20.predict(self.input)
            if alt20 == 1:
                # YarcLexer.g:172:16: POINT_FLOAT
                self.mPOINT_FLOAT()

            elif alt20 == 2:
                # YarcLexer.g:172:30: EXPONENT_FLOAT
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

            # YarcLexer.g:175:8: ( ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? ) )
            # YarcLexer.g:176:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # YarcLexer.g:176:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # YarcLexer.g:177:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )?
            # YarcLexer.g:177:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt22 = 3
            LA22 = self.input.LA(1)
            if LA22 in {13}:
                LA22_1 = self.input.LA(2)

                if LA22_1 == 10:
                    alt22 = 1
                else:
                    alt22 = 2

            elif LA22 in {10}:
                alt22 = 1
            elif LA22 in {12}:
                alt22 = 3
            else:
                nvae = NoViableAltException("", 22, 0, self.input)

                raise nvae

            if alt22 == 1:
                # YarcLexer.g:177:5: ( '\\r' )? '\\n'
                pass
                # YarcLexer.g:177:5: ( '\\r' )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if LA21_0 == 13:
                    alt21 = 1
                if alt21 == 1:
                    # YarcLexer.g:177:5: '\\r'
                    self.match(13)

                self.match(10)

            elif alt22 == 2:
                # YarcLexer.g:177:18: '\\r'
                self.match(13)

            elif alt22 == 3:
                # YarcLexer.g:177:25: '\\f'
                self.match(12)

            # YarcLexer.g:177:31: ( SPACES )?
            alt23 = 2
            LA23_0 = self.input.LA(1)

            if LA23_0 in {9, 32}:
                alt23 = 1
            if alt23 == 1:
                # YarcLexer.g:177:31: SPACES
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

            # YarcLexer.g:182:9: ( ( SPACES | COMMENT | LINE_JOINING ) )
            # YarcLexer.g:182:11: ( SPACES | COMMENT | LINE_JOINING )
            # YarcLexer.g:182:11: ( SPACES | COMMENT | LINE_JOINING )
            alt24 = 3
            LA24 = self.input.LA(1)
            if LA24 in {9, 32}:
                alt24 = 1
            elif LA24 in {35}:
                alt24 = 2
            elif LA24 in {92}:
                alt24 = 3
            else:
                nvae = NoViableAltException("", 24, 0, self.input)

                raise nvae

            if alt24 == 1:
                # YarcLexer.g:182:13: SPACES
                self.mSPACES()

            elif alt24 == 2:
                # YarcLexer.g:182:22: COMMENT
                self.mCOMMENT()

            elif alt24 == 3:
                # YarcLexer.g:182:32: LINE_JOINING
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

            # YarcLexer.g:183:9: ( . )
            # YarcLexer.g:183:11: .
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
            # YarcLexer.g:186:22: ( '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\'' | '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"' )
            alt27 = 2
            LA27_0 = self.input.LA(1)

            if LA27_0 == 39:
                alt27 = 1
            elif LA27_0 == 34:
                alt27 = 2
            else:
                nvae = NoViableAltException("", 27, 0, self.input)

                raise nvae

            if alt27 == 1:
                # YarcLexer.g:187:3: '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\''
                self.match(39)

                # YarcLexer.g:187:8: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )*
                while True:  # loop25
                    alt25 = 3
                    LA25_0 = self.input.LA(1)

                    if LA25_0 == 92:
                        alt25 = 1
                    elif (
                        (0 <= LA25_0 <= 9)
                        or (14 <= LA25_0 <= 38)
                        or (40 <= LA25_0 <= 91)
                        or (93 <= LA25_0 <= 65535)
                        or LA25_0 in {11}
                    ):
                        alt25 = 2

                    if alt25 == 1:
                        # YarcLexer.g:187:9: STRING_ESCAPE_SEQ
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt25 == 2:
                        # YarcLexer.g:187:29: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' )
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
                        break  # loop25

                self.match(39)

            elif alt27 == 2:
                # YarcLexer.g:188:5: '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"'
                self.match(34)

                # YarcLexer.g:188:9: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )*
                while True:  # loop26
                    alt26 = 3
                    LA26_0 = self.input.LA(1)

                    if LA26_0 == 92:
                        alt26 = 1
                    elif (
                        (0 <= LA26_0 <= 9)
                        or (14 <= LA26_0 <= 33)
                        or (35 <= LA26_0 <= 91)
                        or (93 <= LA26_0 <= 65535)
                        or LA26_0 in {11}
                    ):
                        alt26 = 2

                    if alt26 == 1:
                        # YarcLexer.g:188:10: STRING_ESCAPE_SEQ
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt26 == 2:
                        # YarcLexer.g:188:30: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' )
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
                        break  # loop26

                self.match(34)

        finally:
            pass

    # $ANTLR end "SHORT_STRING"

    # $ANTLR start "STRING_ESCAPE_SEQ"
    def mSTRING_ESCAPE_SEQ(
        self,
    ):
        try:
            # YarcLexer.g:190:28: ( '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' ) | '\\\\' NEWLINE )
            alt28 = 2
            LA28_0 = self.input.LA(1)

            if LA28_0 == 92:
                LA28_1 = self.input.LA(2)

                if (
                    (0 <= LA28_1 <= 8)
                    or (14 <= LA28_1 <= 31)
                    or (33 <= LA28_1 <= 65535)
                    or LA28_1 in {11}
                ):
                    alt28 = 1
                elif LA28_1 in {10, 12, 13}:
                    alt28 = 2
                else:
                    nvae = NoViableAltException("", 28, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 28, 0, self.input)

                raise nvae

            if alt28 == 1:
                # YarcLexer.g:190:30: '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' )
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

            elif alt28 == 2:
                # YarcLexer.g:190:72: '\\\\' NEWLINE
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
            # YarcLexer.g:192:25: ( '1' .. '9' )
            # YarcLexer.g:
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
            # YarcLexer.g:193:25: ( '0' .. '9' )
            # YarcLexer.g:
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
            # YarcLexer.g:194:25: ( '0' .. '7' )
            # YarcLexer.g:
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
            # YarcLexer.g:195:25: ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )
            # YarcLexer.g:
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
            # YarcLexer.g:196:25: ( '0' | '1' )
            # YarcLexer.g:
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
            # YarcLexer.g:198:25: ( ( INT_PART )? FRACTION | INT_PART '.' )
            alt30 = 2
            alt30 = self.dfa30.predict(self.input)
            if alt30 == 1:
                # YarcLexer.g:198:27: ( INT_PART )? FRACTION
                pass
                # YarcLexer.g:198:27: ( INT_PART )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (48 <= LA29_0 <= 57) or LA29_0 in {}:
                    alt29 = 1
                if alt29 == 1:
                    # YarcLexer.g:198:27: INT_PART
                    self.mINT_PART()

                self.mFRACTION()

            elif alt30 == 2:
                # YarcLexer.g:198:48: INT_PART '.'
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
            # YarcLexer.g:199:25: ( ( INT_PART | POINT_FLOAT ) EXPONENT )
            # YarcLexer.g:199:27: ( INT_PART | POINT_FLOAT ) EXPONENT
            pass
            # YarcLexer.g:199:27: ( INT_PART | POINT_FLOAT )
            alt31 = 2
            alt31 = self.dfa31.predict(self.input)
            if alt31 == 1:
                # YarcLexer.g:199:29: INT_PART
                self.mINT_PART()

            elif alt31 == 2:
                # YarcLexer.g:199:40: POINT_FLOAT
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
            # YarcLexer.g:200:25: ( ( DIGIT )+ )
            # YarcLexer.g:200:27: ( DIGIT )+
            pass
            # YarcLexer.g:200:27: ( DIGIT )+
            cnt32 = 0
            while True:  # loop32
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (48 <= LA32_0 <= 57) or LA32_0 in {}:
                    alt32 = 1

                if alt32 == 1:
                    # YarcLexer.g:
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt32 >= 1:
                        break  # loop32

                    eee = EarlyExitException(32, self.input)
                    raise eee

                cnt32 += 1

        finally:
            pass

    # $ANTLR end "INT_PART"

    # $ANTLR start "FRACTION"
    def mFRACTION(
        self,
    ):
        try:
            # YarcLexer.g:201:25: ( '.' ( DIGIT )+ )
            # YarcLexer.g:201:27: '.' ( DIGIT )+
            self.match(46)

            # YarcLexer.g:201:31: ( DIGIT )+
            cnt33 = 0
            while True:  # loop33
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (48 <= LA33_0 <= 57) or LA33_0 in {}:
                    alt33 = 1

                if alt33 == 1:
                    # YarcLexer.g:
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt33 >= 1:
                        break  # loop33

                    eee = EarlyExitException(33, self.input)
                    raise eee

                cnt33 += 1

        finally:
            pass

    # $ANTLR end "FRACTION"

    # $ANTLR start "EXPONENT"
    def mEXPONENT(
        self,
    ):
        try:
            # YarcLexer.g:202:25: ( ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+ )
            # YarcLexer.g:202:27: ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+
            if self.input.LA(1) in {69, 101}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # YarcLexer.g:202:39: ( '+' | '-' )?
            alt34 = 2
            LA34_0 = self.input.LA(1)

            if LA34_0 in {43, 45}:
                alt34 = 1
            if alt34 == 1:
                # YarcLexer.g:
                if self.input.LA(1) in {43, 45}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            # YarcLexer.g:202:52: ( DIGIT )+
            cnt35 = 0
            while True:  # loop35
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (48 <= LA35_0 <= 57) or LA35_0 in {}:
                    alt35 = 1

                if alt35 == 1:
                    # YarcLexer.g:
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

    # $ANTLR end "EXPONENT"

    # $ANTLR start "ID_START"
    def mID_START(
        self,
    ):
        try:
            # YarcLexer.g:204:22: ( UNDERSCORE | LETTER )
            # YarcLexer.g:
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
            # YarcLexer.g:205:22: ( ID_START | DIGIT )
            # YarcLexer.g:
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
            # YarcLexer.g:206:22: ( 'a' .. 'z' | 'A' .. 'Z' )
            # YarcLexer.g:
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
            # YarcLexer.g:208:23: ( ( ' ' | '\\t' )+ )
            # YarcLexer.g:208:25: ( ' ' | '\\t' )+
            pass
            # YarcLexer.g:208:25: ( ' ' | '\\t' )+
            cnt36 = 0
            while True:  # loop36
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if LA36_0 in {9, 32}:
                    alt36 = 1

                if alt36 == 1:
                    # YarcLexer.g:
                    if self.input.LA(1) in {9, 32}:
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

    # $ANTLR end "SPACES"

    # $ANTLR start "COMMENT"
    def mCOMMENT(
        self,
    ):
        try:
            # YarcLexer.g:209:23: ( '#' (~ ( '\\r' | '\\n' | '\\f' ) )* )
            # YarcLexer.g:209:25: '#' (~ ( '\\r' | '\\n' | '\\f' ) )*
            self.match(35)

            # YarcLexer.g:209:29: (~ ( '\\r' | '\\n' | '\\f' ) )*
            while True:  # loop37
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (0 <= LA37_0 <= 9) or (14 <= LA37_0 <= 65535) or LA37_0 in {11}:
                    alt37 = 1

                if alt37 == 1:
                    # YarcLexer.g:
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
                    break  # loop37

        finally:
            pass

    # $ANTLR end "COMMENT"

    # $ANTLR start "LINE_JOINING"
    def mLINE_JOINING(
        self,
    ):
        try:
            # YarcLexer.g:210:23: ( '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) )
            # YarcLexer.g:210:25: '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            self.match(92)

            # YarcLexer.g:210:30: ( SPACES )?
            alt38 = 2
            LA38_0 = self.input.LA(1)

            if LA38_0 in {9, 32}:
                alt38 = 1
            if alt38 == 1:
                # YarcLexer.g:210:30: SPACES
                self.mSPACES()

            # YarcLexer.g:210:38: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt40 = 3
            LA40 = self.input.LA(1)
            if LA40 in {13}:
                LA40_1 = self.input.LA(2)

                if LA40_1 == 10:
                    alt40 = 1
                else:
                    alt40 = 2

            elif LA40 in {10}:
                alt40 = 1
            elif LA40 in {12}:
                alt40 = 3
            else:
                nvae = NoViableAltException("", 40, 0, self.input)

                raise nvae

            if alt40 == 1:
                # YarcLexer.g:210:40: ( '\\r' )? '\\n'
                pass
                # YarcLexer.g:210:40: ( '\\r' )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if LA39_0 == 13:
                    alt39 = 1
                if alt39 == 1:
                    # YarcLexer.g:210:40: '\\r'
                    self.match(13)

                self.match(10)

            elif alt40 == 2:
                # YarcLexer.g:210:53: '\\r'
                self.match(13)

            elif alt40 == 3:
                # YarcLexer.g:210:60: '\\f'
                self.match(12)

        finally:
            pass

    # $ANTLR end "LINE_JOINING"

    def mTokens(self):
        # YarcLexer.g:1:8: ( SCENARIO | SETTINGS | STAGE | WRITERS | SHAPE | CAMERA | LIGHT | STEREO | MATERIAL | TIMELINE | OPEN | CREATE | GROUP | INSTANTIATE | GET | EDIT | FETCH | MATCH | LIMIT | RECURSIVE | TRANSLATE | ROTATE | SCALE | SEMANTICS | VISIBLE | SIZE | LOOK_AT | UP_AXIS | PIVOT | MATERIAL_ | AXIS | ORDER | SCATTER | ROT_AROUND | MOVE_TO_CAM | PHYSICS | EVERY | FRAMES | TIME | DISTRIBUTION | COMBINE | SNIPPET | TO | ON | AT | AND | ELSE | FALSE | FOR | FROM | IF | IN | IS | LEN | NONE | NOT | OR | STEP | TRUE | UNDERSCORE | DOT | RANGE | ELLIPSIS | COMMA | COLON | SEMI | ASSIGN | BIT_OR | XOR | BIT_AND | BIT_NOT | LSHIFT | RSHIFT | PLUS | MINUS | MUL | DIV | MOD | IDIV | POWER | LPAREN | RPAREN | LBRACK | RBRACK | LBRACE | RBRACE | LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | AUG_ASSIGN | ID | SETTING_ID | STRING | INTEGER | FLOAT_NUMBER | NEWLINE | SKIP_ | UNKNOWN )
        alt41 = 101
        alt41 = self.dfa41.predict(self.input)
        if alt41 == 1:
            # YarcLexer.g:1:10: SCENARIO
            self.mSCENARIO()

        elif alt41 == 2:
            # YarcLexer.g:1:19: SETTINGS
            self.mSETTINGS()

        elif alt41 == 3:
            # YarcLexer.g:1:28: STAGE
            self.mSTAGE()

        elif alt41 == 4:
            # YarcLexer.g:1:34: WRITERS
            self.mWRITERS()

        elif alt41 == 5:
            # YarcLexer.g:1:42: SHAPE
            self.mSHAPE()

        elif alt41 == 6:
            # YarcLexer.g:1:48: CAMERA
            self.mCAMERA()

        elif alt41 == 7:
            # YarcLexer.g:1:55: LIGHT
            self.mLIGHT()

        elif alt41 == 8:
            # YarcLexer.g:1:61: STEREO
            self.mSTEREO()

        elif alt41 == 9:
            # YarcLexer.g:1:68: MATERIAL
            self.mMATERIAL()

        elif alt41 == 10:
            # YarcLexer.g:1:77: TIMELINE
            self.mTIMELINE()

        elif alt41 == 11:
            # YarcLexer.g:1:86: OPEN
            self.mOPEN()

        elif alt41 == 12:
            # YarcLexer.g:1:91: CREATE
            self.mCREATE()

        elif alt41 == 13:
            # YarcLexer.g:1:98: GROUP
            self.mGROUP()

        elif alt41 == 14:
            # YarcLexer.g:1:104: INSTANTIATE
            self.mINSTANTIATE()

        elif alt41 == 15:
            # YarcLexer.g:1:116: GET
            self.mGET()

        elif alt41 == 16:
            # YarcLexer.g:1:120: EDIT
            self.mEDIT()

        elif alt41 == 17:
            # YarcLexer.g:1:125: FETCH
            self.mFETCH()

        elif alt41 == 18:
            # YarcLexer.g:1:131: MATCH
            self.mMATCH()

        elif alt41 == 19:
            # YarcLexer.g:1:137: LIMIT
            self.mLIMIT()

        elif alt41 == 20:
            # YarcLexer.g:1:143: RECURSIVE
            self.mRECURSIVE()

        elif alt41 == 21:
            # YarcLexer.g:1:153: TRANSLATE
            self.mTRANSLATE()

        elif alt41 == 22:
            # YarcLexer.g:1:163: ROTATE
            self.mROTATE()

        elif alt41 == 23:
            # YarcLexer.g:1:170: SCALE
            self.mSCALE()

        elif alt41 == 24:
            # YarcLexer.g:1:176: SEMANTICS
            self.mSEMANTICS()

        elif alt41 == 25:
            # YarcLexer.g:1:186: VISIBLE
            self.mVISIBLE()

        elif alt41 == 26:
            # YarcLexer.g:1:194: SIZE
            self.mSIZE()

        elif alt41 == 27:
            # YarcLexer.g:1:199: LOOK_AT
            self.mLOOK_AT()

        elif alt41 == 28:
            # YarcLexer.g:1:207: UP_AXIS
            self.mUP_AXIS()

        elif alt41 == 29:
            # YarcLexer.g:1:215: PIVOT
            self.mPIVOT()

        elif alt41 == 30:
            # YarcLexer.g:1:221: MATERIAL_
            self.mMATERIAL_()

        elif alt41 == 31:
            # YarcLexer.g:1:231: AXIS
            self.mAXIS()

        elif alt41 == 32:
            # YarcLexer.g:1:236: ORDER
            self.mORDER()

        elif alt41 == 33:
            # YarcLexer.g:1:242: SCATTER
            self.mSCATTER()

        elif alt41 == 34:
            # YarcLexer.g:1:250: ROT_AROUND
            self.mROT_AROUND()

        elif alt41 == 35:
            # YarcLexer.g:1:261: MOVE_TO_CAM
            self.mMOVE_TO_CAM()

        elif alt41 == 36:
            # YarcLexer.g:1:273: PHYSICS
            self.mPHYSICS()

        elif alt41 == 37:
            # YarcLexer.g:1:281: EVERY
            self.mEVERY()

        elif alt41 == 38:
            # YarcLexer.g:1:287: FRAMES
            self.mFRAMES()

        elif alt41 == 39:
            # YarcLexer.g:1:294: TIME
            self.mTIME()

        elif alt41 == 40:
            # YarcLexer.g:1:299: DISTRIBUTION
            self.mDISTRIBUTION()

        elif alt41 == 41:
            # YarcLexer.g:1:312: COMBINE
            self.mCOMBINE()

        elif alt41 == 42:
            # YarcLexer.g:1:320: SNIPPET
            self.mSNIPPET()

        elif alt41 == 43:
            # YarcLexer.g:1:328: TO
            self.mTO()

        elif alt41 == 44:
            # YarcLexer.g:1:331: ON
            self.mON()

        elif alt41 == 45:
            # YarcLexer.g:1:334: AT
            self.mAT()

        elif alt41 == 46:
            # YarcLexer.g:1:337: AND
            self.mAND()

        elif alt41 == 47:
            # YarcLexer.g:1:341: ELSE
            self.mELSE()

        elif alt41 == 48:
            # YarcLexer.g:1:346: FALSE
            self.mFALSE()

        elif alt41 == 49:
            # YarcLexer.g:1:352: FOR
            self.mFOR()

        elif alt41 == 50:
            # YarcLexer.g:1:356: FROM
            self.mFROM()

        elif alt41 == 51:
            # YarcLexer.g:1:361: IF
            self.mIF()

        elif alt41 == 52:
            # YarcLexer.g:1:364: IN
            self.mIN()

        elif alt41 == 53:
            # YarcLexer.g:1:367: IS
            self.mIS()

        elif alt41 == 54:
            # YarcLexer.g:1:370: LEN
            self.mLEN()

        elif alt41 == 55:
            # YarcLexer.g:1:374: NONE
            self.mNONE()

        elif alt41 == 56:
            # YarcLexer.g:1:379: NOT
            self.mNOT()

        elif alt41 == 57:
            # YarcLexer.g:1:383: OR
            self.mOR()

        elif alt41 == 58:
            # YarcLexer.g:1:386: STEP
            self.mSTEP()

        elif alt41 == 59:
            # YarcLexer.g:1:391: TRUE
            self.mTRUE()

        elif alt41 == 60:
            # YarcLexer.g:1:396: UNDERSCORE
            self.mUNDERSCORE()

        elif alt41 == 61:
            # YarcLexer.g:1:407: DOT
            self.mDOT()

        elif alt41 == 62:
            # YarcLexer.g:1:411: RANGE
            self.mRANGE()

        elif alt41 == 63:
            # YarcLexer.g:1:417: ELLIPSIS
            self.mELLIPSIS()

        elif alt41 == 64:
            # YarcLexer.g:1:426: COMMA
            self.mCOMMA()

        elif alt41 == 65:
            # YarcLexer.g:1:432: COLON
            self.mCOLON()

        elif alt41 == 66:
            # YarcLexer.g:1:438: SEMI
            self.mSEMI()

        elif alt41 == 67:
            # YarcLexer.g:1:443: ASSIGN
            self.mASSIGN()

        elif alt41 == 68:
            # YarcLexer.g:1:450: BIT_OR
            self.mBIT_OR()

        elif alt41 == 69:
            # YarcLexer.g:1:457: XOR
            self.mXOR()

        elif alt41 == 70:
            # YarcLexer.g:1:461: BIT_AND
            self.mBIT_AND()

        elif alt41 == 71:
            # YarcLexer.g:1:469: BIT_NOT
            self.mBIT_NOT()

        elif alt41 == 72:
            # YarcLexer.g:1:477: LSHIFT
            self.mLSHIFT()

        elif alt41 == 73:
            # YarcLexer.g:1:484: RSHIFT
            self.mRSHIFT()

        elif alt41 == 74:
            # YarcLexer.g:1:491: PLUS
            self.mPLUS()

        elif alt41 == 75:
            # YarcLexer.g:1:496: MINUS
            self.mMINUS()

        elif alt41 == 76:
            # YarcLexer.g:1:502: MUL
            self.mMUL()

        elif alt41 == 77:
            # YarcLexer.g:1:506: DIV
            self.mDIV()

        elif alt41 == 78:
            # YarcLexer.g:1:510: MOD
            self.mMOD()

        elif alt41 == 79:
            # YarcLexer.g:1:514: IDIV
            self.mIDIV()

        elif alt41 == 80:
            # YarcLexer.g:1:519: POWER
            self.mPOWER()

        elif alt41 == 81:
            # YarcLexer.g:1:525: LPAREN
            self.mLPAREN()

        elif alt41 == 82:
            # YarcLexer.g:1:532: RPAREN
            self.mRPAREN()

        elif alt41 == 83:
            # YarcLexer.g:1:539: LBRACK
            self.mLBRACK()

        elif alt41 == 84:
            # YarcLexer.g:1:546: RBRACK
            self.mRBRACK()

        elif alt41 == 85:
            # YarcLexer.g:1:553: LBRACE
            self.mLBRACE()

        elif alt41 == 86:
            # YarcLexer.g:1:560: RBRACE
            self.mRBRACE()

        elif alt41 == 87:
            # YarcLexer.g:1:567: LT
            self.mLT()

        elif alt41 == 88:
            # YarcLexer.g:1:570: GT
            self.mGT()

        elif alt41 == 89:
            # YarcLexer.g:1:573: EQUALS
            self.mEQUALS()

        elif alt41 == 90:
            # YarcLexer.g:1:580: GT_EQ
            self.mGT_EQ()

        elif alt41 == 91:
            # YarcLexer.g:1:586: LT_EQ
            self.mLT_EQ()

        elif alt41 == 92:
            # YarcLexer.g:1:592: NOT_EQ
            self.mNOT_EQ()

        elif alt41 == 93:
            # YarcLexer.g:1:599: AUG_ASSIGN
            self.mAUG_ASSIGN()

        elif alt41 == 94:
            # YarcLexer.g:1:610: ID
            self.mID()

        elif alt41 == 95:
            # YarcLexer.g:1:613: SETTING_ID
            self.mSETTING_ID()

        elif alt41 == 96:
            # YarcLexer.g:1:624: STRING
            self.mSTRING()

        elif alt41 == 97:
            # YarcLexer.g:1:631: INTEGER
            self.mINTEGER()

        elif alt41 == 98:
            # YarcLexer.g:1:639: FLOAT_NUMBER
            self.mFLOAT_NUMBER()

        elif alt41 == 99:
            # YarcLexer.g:1:652: NEWLINE
            self.mNEWLINE()

        elif alt41 == 100:
            # YarcLexer.g:1:660: SKIP_
            self.mSKIP_()

        elif alt41 == 101:
            # YarcLexer.g:1:666: UNKNOWN
            self.mUNKNOWN()

    # lookup tables for DFA #20

    DFA20_eot = DFA.unpack("\3\uffff\1\6\1\uffff\1\6\1\uffff")

    DFA20_eof = DFA.unpack("\7\uffff")

    DFA20_min = DFA.unpack("\2\56\2\60\1\uffff\1\60\1\uffff")

    DFA20_max = DFA.unpack("\1\71\1\145\1\71\1\145\1\uffff\1\145\1\uffff")

    DFA20_accept = DFA.unpack("\4\uffff\1\2\1\uffff\1\1")

    DFA20_special = DFA.unpack("\7\uffff")

    DFA20_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack("\12\5"),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
    ]

    # class definition for DFA #20

    class DFA20(DFA):
        pass

    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack("\3\uffff\1\4\1\uffff")

    DFA30_eof = DFA.unpack("\5\uffff")

    DFA30_min = DFA.unpack("\2\56\1\uffff\1\60\1\uffff")

    DFA30_max = DFA.unpack("\2\71\1\uffff\1\71\1\uffff")

    DFA30_accept = DFA.unpack("\2\uffff\1\1\1\uffff\1\2")

    DFA30_special = DFA.unpack("\5\uffff")

    DFA30_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1"),
        DFA.unpack(""),
        DFA.unpack("\12\2"),
        DFA.unpack(""),
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass

    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack("\4\uffff")

    DFA31_eof = DFA.unpack("\4\uffff")

    DFA31_min = DFA.unpack("\2\56\2\uffff")

    DFA31_max = DFA.unpack("\1\71\1\145\2\uffff")

    DFA31_accept = DFA.unpack("\2\uffff\1\2\1\1")

    DFA31_special = DFA.unpack("\4\uffff")

    DFA31_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\2\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(""),
        DFA.unpack(""),
    ]

    # class definition for DFA #31

    class DFA31(DFA):
        pass

    # lookup tables for DFA #41

    DFA41_eot = DFA.unpack(
        "\1\uffff\26\110\1\173\3\110\1\u0080\2\110\1\u0085\1\u0087\3\uffff"
        "\1\u008d\1\u008f\1\u0090\1\u0091\1\uffff\1\u0095\1\u0098\1\u0099"
        "\1\u009a\1\u009c\1\u009e\1\u009f\5\uffff\1\103\1\110\1\103\1\110"
        "\1\uffff\2\103\2\u00a7\5\uffff\1\103\1\uffff\4\110\1\uffff\21\110"
        "\1\u00c6\1\u00c7\4\110\1\u00cd\1\u00ce\1\u00cf\10\110\1\uffff\12"
        "\110\1\u00e2\4\110\1\uffff\4\110\2\uffff\1\u00eb\2\110\1\uffff\1"
        "\u00f0\14\uffff\1\u00f1\2\uffff\1\u00f2\4\uffff\1\u00f3\1\uffff"
        "\1\u00f4\12\uffff\2\u00a7\2\uffff\4\110\1\u00fb\25\110\2\uffff\3"
        "\110\1\u0114\1\110\3\uffff\7\110\1\u011d\4\110\1\u0123\5\110\1\uffff"
        "\4\110\1\u012d\3\110\1\uffff\1\u0131\1\110\1\u0133\6\uffff\6\110"
        "\1\uffff\1\110\1\u013b\1\u013c\2\110\2\u013f\11\110\1\u013f\3\110"
        "\1\u014c\3\110\1\uffff\1\110\1\u0151\1\110\1\u0153\2\110\1\u0156"
        "\1\110\1\uffff\5\110\1\uffff\4\110\1\u0161\4\110\1\uffff\3\110\1"
        "\uffff\1\u0169\1\uffff\1\110\1\u016b\4\110\1\u0170\2\uffff\1\110"
        "\1\u013f\1\uffff\4\110\1\u013f\4\110\1\u017a\2\110\1\uffff\2\110"
        "\1\u017f\1\110\1\uffff\1\u0181\1\uffff\1\u0182\1\u0184\1\uffff\1"
        "\u0185\1\u0186\2\110\1\u0189\5\110\1\uffff\2\110\1\u0191\4\110\1"
        "\uffff\1\110\1\uffff\3\110\1\u00fb\1\uffff\3\110\1\u019e\1\u019f"
        "\1\110\1\u013f\1\u01a1\1\110\1\uffff\2\110\1\u01a5\1\110\1\uffff"
        "\1\110\2\uffff\1\u0184\3\uffff\2\110\1\uffff\2\110\1\u01ad\4\110"
        "\1\uffff\3\110\1\u019f\4\110\1\u00fb\1\u01b9\1\u01ba\1\110\2\uffff"
        "\1\110\1\uffff\3\110\1\uffff\4\110\1\u01c4\2\110\1\uffff\2\110\1"
        "\u01c9\1\u01ca\2\110\1\u019f\1\u01cd\1\110\1\u01d0\1\110\2\uffff"
        "\1\u013f\1\u01d2\1\u019f\1\110\1\u01d4\1\u01d5\1\110\1\u01d7\1\110"
        "\1\uffff\4\110\2\uffff\2\110\1\uffff\2\110\1\uffff\1\u01e1\1\uffff"
        "\1\110\2\uffff\1\110\1\uffff\1\110\1\u01e5\2\110\1\u01e8\2\110\2"
        "\u01eb\1\uffff\1\u019f\2\110\1\uffff\1\110\1\u01d5\1\uffff\1\110"
        "\1\u01d5\1\uffff\1\u01f0\3\110\1\uffff\4\110\1\u01f8\1\110\1\u01fa"
        "\1\uffff\1\110\1\uffff\1\110\1\u01d5"
    )

    DFA41_eof = DFA.unpack("\u01fd\uffff")

    DFA41_min = DFA.unpack(
        "\1\0\1\143\1\162\1\154\1\141\1\151\1\145\2\151\1\141\1\156\1\157"
        "\1\145\1\146\1\144\1\42\1\141\1\145\1\42\1\157\1\151\1\42\1\150"
        "\1\60\1\151\1\42\1\157\1\173\1\156\1\157\1\60\1\56\3\uffff\4\75"
        "\1\uffff\1\74\3\75\1\52\1\57\1\75\5\uffff\1\75\1\42\1\101\1\42\1"
        "\uffff\2\0\2\56\5\uffff\1\11\1\uffff\1\141\1\143\1\141\1\172\1\uffff"
        "\1\151\1\141\1\142\1\155\1\154\1\155\1\157\1\162\1\155\1\150\1\145"
        "\1\161\1\163\2\147\1\164\1\145\2\60\1\145\1\154\1\157\1\164\3\60"
        "\1\151\1\145\1\163\1\164\1\42\1\154\1\162\1\42\1\uffff\1\164\1\166"
        "\1\155\1\157\1\156\1\143\1\164\1\147\1\42\1\141\1\60\1\163\1\137"
        "\1\166\1\171\1\uffff\1\130\1\156\1\151\1\162\2\uffff\1\60\1\144"
        "\1\156\1\uffff\1\56\14\uffff\1\75\2\uffff\1\75\4\uffff\1\75\1\uffff"
        "\1\75\12\uffff\2\56\2\uffff\1\156\1\154\1\164\1\141\1\60\1\147\1"
        "\160\1\145\1\164\1\156\2\145\1\142\1\151\1\145\1\151\1\165\2\145"
        "\1\162\1\165\1\153\1\150\1\125\1\145\1\156\2\uffff\1\141\1\154\1"
        "\165\1\60\1\164\3\uffff\1\164\1\162\1\145\1\143\2\155\1\163\1\60"
        "\1\143\1\145\1\151\1\153\1\60\1\165\1\141\1\151\1\156\1\145\1\uffff"
        "\1\151\1\141\1\157\1\163\1\60\1\145\1\146\1\155\1\uffff\1\60\1\145"
        "\1\60\6\uffff\1\141\1\145\1\164\1\151\2\156\1\uffff\1\145\2\60\2"
        "\145\2\60\1\151\1\156\1\162\1\143\1\163\1\154\1\162\2\145\1\60\1"
        "\164\1\156\1\162\1\60\1\164\1\151\1\160\1\uffff\1\141\1\60\1\171"
        "\1\60\1\150\1\145\1\60\1\145\1\uffff\1\150\1\162\1\137\1\164\1\137"
        "\1\uffff\1\162\1\164\1\144\1\163\1\60\1\142\1\170\1\164\1\151\1"
        "\uffff\1\155\1\157\1\141\1\uffff\1\60\1\uffff\1\162\1\60\1\145\1"
        "\156\1\164\1\144\1\60\2\uffff\1\162\1\60\1\uffff\1\156\1\144\1\141"
        "\1\145\1\60\1\151\1\145\1\157\1\156\1\60\2\151\1\uffff\1\145\1\144"
        "\1\60\1\156\1\uffff\1\60\1\uffff\2\60\1\uffff\2\60\1\151\1\164\1"
        "\60\1\141\1\163\1\145\1\137\1\154\1\uffff\1\154\1\151\1\60\1\143"
        "\1\141\1\162\1\154\1\uffff\1\151\1\uffff\1\162\1\147\1\151\1\60"
        "\1\uffff\1\163\2\145\2\60\1\156\2\60\1\143\1\uffff\1\146\1\141\1"
        "\60\1\145\1\uffff\1\164\2\uffff\1\60\3\uffff\1\141\1\157\1\uffff"
        "\1\164\1\151\1\60\1\142\1\141\1\145\1\163\1\uffff\1\163\1\164\1"
        "\155\1\60\1\157\1\137\1\163\1\143\3\60\1\162\2\uffff\1\145\1\uffff"
        "\1\145\1\157\1\154\1\uffff\1\162\1\151\1\154\1\137\1\60\1\166\1"
        "\141\1\uffff\1\157\1\164\2\60\1\137\1\151\2\60\1\62\1\60\1\163\2"
        "\uffff\3\60\1\162\2\60\1\141\1\60\1\143\1\uffff\1\145\1\162\1\144"
        "\1\145\2\uffff\1\155\1\143\1\uffff\2\144\1\uffff\1\60\1\uffff\1"
        "\155\2\uffff\1\164\1\uffff\1\141\1\60\1\157\1\171\1\60\1\141\1\163"
        "\2\60\1\uffff\1\60\1\145\1\155\1\uffff\1\165\1\60\1\uffff\1\164"
        "\1\60\1\uffff\1\60\1\145\1\156\1\145\1\uffff\1\162\1\144\1\162\1"
        "\141\1\60\1\151\1\60\1\uffff\1\141\1\uffff\1\154\1\60"
    )

    DFA41_max = DFA.unpack(
        "\1\uffff\1\164\1\162\1\154\1\171\1\157\1\164\1\151\1\157\1\141\3"
        "\162\1\163\1\166\1\162\3\157\1\162\1\151\1\160\1\151\1\172\1\151"
        "\1\156\1\157\1\173\1\164\1\157\1\172\1\71\3\uffff\4\75\1\uffff\1"
        "\75\1\76\5\75\5\uffff\1\75\1\162\1\172\1\146\1\uffff\2\uffff\2\145"
        "\5\uffff\1\40\1\uffff\1\145\1\164\1\145\1\172\1\uffff\1\151\1\141"
        "\1\142\1\156\1\154\1\155\1\157\1\162\1\155\1\150\1\145\1\161\1\163"
        "\2\147\1\164\1\145\2\172\1\145\1\154\1\157\1\164\3\172\1\151\1\145"
        "\1\163\1\164\1\157\1\154\1\162\1\47\1\uffff\1\164\1\166\1\155\1"
        "\157\1\156\1\143\1\164\1\147\1\47\1\165\1\172\1\163\1\137\1\166"
        "\1\171\1\uffff\1\172\1\156\1\151\1\162\2\uffff\1\172\1\144\1\164"
        "\1\uffff\1\56\14\uffff\1\75\2\uffff\1\75\4\uffff\1\75\1\uffff\1"
        "\75\12\uffff\2\145\2\uffff\1\156\2\164\1\141\1\172\1\147\1\160\1"
        "\145\1\164\1\156\2\145\1\142\1\151\1\145\1\151\1\165\2\145\1\162"
        "\1\165\1\153\1\150\1\125\1\145\1\156\2\uffff\1\141\1\154\1\165\1"
        "\172\1\164\3\uffff\1\164\1\162\1\145\1\143\2\155\1\163\1\172\2\145"
        "\1\151\1\153\1\172\1\165\1\141\1\151\1\156\1\145\1\uffff\1\151\1"
        "\141\1\157\1\163\1\172\1\145\1\146\1\155\1\uffff\1\172\1\145\1\172"
        "\6\uffff\1\141\1\145\1\164\1\151\2\156\1\uffff\1\145\2\172\2\145"
        "\2\172\1\151\1\156\1\162\1\143\1\163\1\154\1\162\2\145\1\172\1\164"
        "\1\156\1\162\1\172\1\164\1\151\1\160\1\uffff\1\141\1\172\1\171\1"
        "\172\1\150\1\145\1\172\1\145\1\uffff\1\150\1\162\1\137\1\164\1\137"
        "\1\uffff\1\162\1\164\1\144\1\163\1\172\1\142\1\170\1\164\1\151\1"
        "\uffff\1\155\1\157\1\141\1\uffff\1\172\1\uffff\1\162\1\172\1\145"
        "\1\156\1\164\1\144\1\172\2\uffff\1\162\1\172\1\uffff\1\156\1\144"
        "\1\141\1\145\1\172\1\151\1\145\1\157\1\156\1\172\2\151\1\uffff\1"
        "\145\1\144\1\172\1\156\1\uffff\1\172\1\uffff\2\172\1\uffff\2\172"
        "\1\151\1\164\1\172\1\141\1\163\1\145\1\137\1\154\1\uffff\1\154\1"
        "\151\1\172\1\143\1\141\1\162\1\154\1\uffff\1\151\1\uffff\1\162\1"
        "\147\1\151\1\172\1\uffff\1\163\2\145\2\172\1\156\2\172\1\143\1\uffff"
        "\1\146\1\141\1\172\1\145\1\uffff\1\164\2\uffff\1\172\3\uffff\1\141"
        "\1\157\1\uffff\1\164\1\151\1\172\1\142\1\141\1\145\1\163\1\uffff"
        "\1\163\1\164\1\155\1\172\1\157\1\137\1\163\1\143\3\172\1\162\2\uffff"
        "\1\145\1\uffff\1\145\1\157\1\154\1\uffff\1\162\1\151\1\154\1\137"
        "\1\172\1\166\1\141\1\uffff\1\157\1\164\2\172\1\137\1\151\2\172\1"
        "\63\1\172\1\163\2\uffff\3\172\1\162\2\172\1\141\1\172\1\143\1\uffff"
        "\1\145\1\162\1\144\1\145\2\uffff\1\155\1\143\1\uffff\2\144\1\uffff"
        "\1\172\1\uffff\1\155\2\uffff\1\164\1\uffff\1\141\1\172\1\157\1\171"
        "\1\172\1\141\1\163\2\172\1\uffff\1\172\1\145\1\155\1\uffff\1\165"
        "\1\172\1\uffff\1\164\1\172\1\uffff\1\172\1\145\1\156\1\145\1\uffff"
        "\1\162\1\144\1\162\1\141\1\172\1\151\1\172\1\uffff\1\141\1\uffff"
        "\1\154\1\172"
    )

    DFA41_accept = DFA.unpack(
        "\40\uffff\1\100\1\101\1\102\4\uffff\1\107\7\uffff\1\121\1\122\1"
        "\123\1\124\1\126\4\uffff\1\136\4\uffff\3\143\2\144\1\uffff\1\145"
        "\4\uffff\1\136\42\uffff\1\140\17\uffff\1\37\4\uffff\1\125\1\52\3"
        "\uffff\1\74\1\uffff\1\75\1\142\1\100\1\101\1\102\1\131\1\103\1\135"
        "\1\104\1\105\1\106\1\107\1\uffff\1\133\1\127\1\uffff\1\132\1\130"
        "\1\112\1\113\1\uffff\1\114\1\uffff\1\115\1\116\1\121\1\122\1\123"
        "\1\124\1\126\1\134\1\137\1\141\2\uffff\1\143\1\144\32\uffff\1\54"
        "\1\71\5\uffff\1\64\1\63\1\65\22\uffff\1\53\10\uffff\1\55\3\uffff"
        "\1\77\1\76\1\110\1\111\1\120\1\117\6\uffff\1\47\30\uffff\1\17\10"
        "\uffff\1\61\5\uffff\1\66\11\uffff\1\40\3\uffff\1\56\1\uffff\1\70"
        "\7\uffff\1\72\1\32\2\uffff\1\5\14\uffff\1\13\4\uffff\1\20\1\uffff"
        "\1\57\2\uffff\1\62\12\uffff\1\73\7\uffff\1\67\1\uffff\1\27\4\uffff"
        "\1\3\11\uffff\1\7\4\uffff\1\15\1\uffff\1\45\1\21\1\uffff\1\46\1"
        "\60\1\22\2\uffff\1\23\7\uffff\1\35\14\uffff\1\6\1\50\1\uffff\1\10"
        "\3\uffff\1\14\7\uffff\1\26\13\uffff\1\4\1\51\11\uffff\1\33\4\uffff"
        "\1\31\1\34\2\uffff\1\1\2\uffff\1\2\1\uffff\1\12\1\uffff\1\11\1\44"
        "\1\uffff\1\36\11\uffff\1\30\3\uffff\1\24\2\uffff\1\25\2\uffff\1"
        "\41\4\uffff\1\16\7\uffff\1\42\1\uffff\1\43\2\uffff"
    )

    DFA41_special = DFA.unpack("\1\2\70\uffff\1\0\1\1\u01c2\uffff")

    DFA41_transition = [
        DFA.unpack(
            "\11\103\1\100\1\76\1\103\1\77\1\75\22\103\1\100\1\64"
            "\1\72\1\101\1\66\1\56\1\46\1\71\1\57\1\60\1\54\1\52\1\40\1\53\1"
            "\37\1\55\1\74\11\73\1\41\1\42\1\50\1\43\1\51\2\103\2\70\1\4\1\7"
            "\1\70\1\65\5\70\1\10\1\11\1\32\1\70\1\3\1\70\1\67\1\6\1\5\1\31\2"
            "\70\3\27\1\61\1\102\1\62\1\45\1\36\1\103\1\34\1\70\1\13\1\70\1\16"
            "\1\17\1\14\1\70\1\15\1\70\1\30\1\21\1\20\1\35\1\12\1\26\1\70\1\22"
            "\1\1\1\23\1\25\1\24\1\2\3\27\1\33\1\44\1\63\1\47\uff81\103"
        ),
        DFA.unpack("\1\104\1\uffff\1\105\3\uffff\1\107\12\uffff\1\106"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\116\6\uffff\1\117\6\uffff\1\114\5\uffff\1\113\3\uffff" "\1\115"),
        DFA.unpack("\1\121\5\uffff\1\120"),
        DFA.unpack("\1\124\12\uffff\1\122\3\uffff\1\123"),
        DFA.unpack("\1\125"),
        DFA.unpack("\1\126\5\uffff\1\127"),
        DFA.unpack("\1\130"),
        DFA.unpack("\1\132\1\uffff\1\131\1\uffff\1\133"),
        DFA.unpack("\1\135\2\uffff\1\134"),
        DFA.unpack("\1\137\14\uffff\1\136"),
        DFA.unpack("\1\141\7\uffff\1\140\4\uffff\1\142"),
        DFA.unpack("\1\143\7\uffff\1\145\11\uffff\1\144"),
        DFA.unpack(
            "\1\153\4\uffff\1\153\52\uffff\1\152\16\uffff\1\150\3"
            "\uffff\1\146\11\uffff\1\151\2\uffff\1\147"
        ),
        DFA.unpack("\1\154\15\uffff\1\155"),
        DFA.unpack("\1\160\3\uffff\1\156\5\uffff\1\157"),
        DFA.unpack(
            "\1\153\4\uffff\1\153\36\uffff\1\164\36\uffff\1\161\1"
            "\164\2\uffff\1\163\5\uffff\1\162"
        ),
        DFA.unpack("\1\166\2\uffff\1\165"),
        DFA.unpack("\1\167"),
        DFA.unpack("\1\153\4\uffff\1\153\110\uffff\1\170"),
        DFA.unpack("\1\172\1\171"),
        DFA.unpack(
            "\12\110\7\uffff\27\110\3\174\4\uffff\1\110\1\uffff\27" "\110\3\174"
        ),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\153\4\uffff\1\153\106\uffff\1\176"),
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
        DFA.unpack("\1\153\4\uffff\1\153\52\uffff\1\152\37\uffff\1\152"),
        DFA.unpack("\32\u00a6\4\uffff\1\u00a6\1\uffff\32\u00a6"),
        DFA.unpack("\1\153\4\uffff\1\153\36\uffff\1\164\37\uffff\1\164"),
        DFA.unpack(""),
        DFA.unpack("\12\153\1\uffff\1\153\2\uffff\ufff2\153"),
        DFA.unpack("\12\153\1\uffff\1\153\2\uffff\ufff2\153"),
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
        DFA.unpack("\1\u00b1\3\uffff\1\u00b2"),
        DFA.unpack("\1\u00b3"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b4"),
        DFA.unpack("\1\u00b5"),
        DFA.unpack("\1\u00b6"),
        DFA.unpack("\1\u00b8\1\u00b7"),
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
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\1\u00c9"),
        DFA.unpack("\1\u00ca"),
        DFA.unpack("\1\u00cb"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u00cc\7\110"
        ),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00d0"),
        DFA.unpack("\1\u00d1"),
        DFA.unpack("\1\u00d2"),
        DFA.unpack("\1\u00d3"),
        DFA.unpack("\1\153\4\uffff\1\153\71\uffff\1\u00d4\15\uffff\1\u00d5"),
        DFA.unpack("\1\u00d6"),
        DFA.unpack("\1\u00d7"),
        DFA.unpack("\1\153\4\uffff\1\153"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d8"),
        DFA.unpack("\1\u00d9"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack("\1\u00dd"),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\1\u00df"),
        DFA.unpack("\1\153\4\uffff\1\153"),
        DFA.unpack("\1\u00e0\23\uffff\1\u00e1"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00e3"),
        DFA.unpack("\1\u00e4"),
        DFA.unpack("\1\u00e5"),
        DFA.unpack("\1\u00e6"),
        DFA.unpack(""),
        DFA.unpack("\3\u00e7\35\uffff\3\u00e7"),
        DFA.unpack("\1\u00e8"),
        DFA.unpack("\1\u00e9"),
        DFA.unpack("\1\u00ea"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00ec"),
        DFA.unpack("\1\u00ed\5\uffff\1\u00ee"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ef"),
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
        DFA.unpack("\1\u00f5"),
        DFA.unpack("\1\u00f6\7\uffff\1\u00f7"),
        DFA.unpack("\1\u00f8"),
        DFA.unpack("\1\u00f9"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\16\110" "\1\u00fa\13\110"
        ),
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
        DFA.unpack("\1\u0108"),
        DFA.unpack("\1\u0109"),
        DFA.unpack("\1\u010a"),
        DFA.unpack("\1\u010b"),
        DFA.unpack("\1\u010c"),
        DFA.unpack("\1\u010d"),
        DFA.unpack("\1\u010e"),
        DFA.unpack("\1\u010f"),
        DFA.unpack("\1\u0110"),
        DFA.unpack(""),
        DFA.unpack(""),
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
        DFA.unpack("\1\u011e\1\uffff\1\u011f"),
        DFA.unpack("\1\u0120"),
        DFA.unpack("\1\u0121"),
        DFA.unpack("\1\u0122"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0124"),
        DFA.unpack("\1\u0125"),
        DFA.unpack("\1\u0126"),
        DFA.unpack("\1\u0127"),
        DFA.unpack("\1\u0128"),
        DFA.unpack(""),
        DFA.unpack("\1\u0129"),
        DFA.unpack("\1\u012a"),
        DFA.unpack("\1\u012b"),
        DFA.unpack("\1\u012c"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u012e"),
        DFA.unpack("\1\u012f"),
        DFA.unpack("\1\u0130"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0132"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0134"),
        DFA.unpack("\1\u0135"),
        DFA.unpack("\1\u0136"),
        DFA.unpack("\1\u0137"),
        DFA.unpack("\1\u0138"),
        DFA.unpack("\1\u0139"),
        DFA.unpack(""),
        DFA.unpack("\1\u013a"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u013d"),
        DFA.unpack("\1\u013e"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0140"),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\1\u0142"),
        DFA.unpack("\1\u0143"),
        DFA.unpack("\1\u0144"),
        DFA.unpack("\1\u0145"),
        DFA.unpack("\1\u0146"),
        DFA.unpack("\1\u0147"),
        DFA.unpack("\1\u0148"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0149"),
        DFA.unpack("\1\u014a"),
        DFA.unpack("\1\u014b"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u014d"),
        DFA.unpack("\1\u014e"),
        DFA.unpack("\1\u014f"),
        DFA.unpack(""),
        DFA.unpack("\1\u0150"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0152"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0154"),
        DFA.unpack("\1\u0155"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0157"),
        DFA.unpack(""),
        DFA.unpack("\1\u0158"),
        DFA.unpack("\1\u0159"),
        DFA.unpack("\1\u015a"),
        DFA.unpack("\1\u015b"),
        DFA.unpack("\1\u015c"),
        DFA.unpack(""),
        DFA.unpack("\1\u015d"),
        DFA.unpack("\1\u015e"),
        DFA.unpack("\1\u015f"),
        DFA.unpack("\1\u0160"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0162"),
        DFA.unpack("\1\u0163"),
        DFA.unpack("\1\u0164"),
        DFA.unpack("\1\u0165"),
        DFA.unpack(""),
        DFA.unpack("\1\u0166"),
        DFA.unpack("\1\u0167"),
        DFA.unpack("\1\u0168"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u016a"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u016c"),
        DFA.unpack("\1\u016d"),
        DFA.unpack("\1\u016e"),
        DFA.unpack("\1\u016f"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0171"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u0172"),
        DFA.unpack("\1\u0173"),
        DFA.unpack("\1\u0174"),
        DFA.unpack("\1\u0175"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0176"),
        DFA.unpack("\1\u0177"),
        DFA.unpack("\1\u0178"),
        DFA.unpack("\1\u0179"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u017b"),
        DFA.unpack("\1\u017c"),
        DFA.unpack(""),
        DFA.unpack("\1\u017d"),
        DFA.unpack("\1\u017e"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0180"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u0183\7\110"
        ),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0187"),
        DFA.unpack("\1\u0188"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u018a"),
        DFA.unpack("\1\u018b"),
        DFA.unpack("\1\u018c"),
        DFA.unpack("\1\u018d"),
        DFA.unpack("\1\u018e"),
        DFA.unpack(""),
        DFA.unpack("\1\u018f"),
        DFA.unpack("\1\u0190"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0192"),
        DFA.unpack("\1\u0193"),
        DFA.unpack("\1\u0194"),
        DFA.unpack("\1\u0195"),
        DFA.unpack(""),
        DFA.unpack("\1\u0196"),
        DFA.unpack(""),
        DFA.unpack("\1\u0197"),
        DFA.unpack("\1\u0198"),
        DFA.unpack("\1\u0199"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u019a\7\110"
        ),
        DFA.unpack(""),
        DFA.unpack("\1\u019b"),
        DFA.unpack("\1\u019c"),
        DFA.unpack("\1\u019d"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01a0"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01a2"),
        DFA.unpack(""),
        DFA.unpack("\1\u01a3"),
        DFA.unpack("\1\u01a4"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01a6"),
        DFA.unpack(""),
        DFA.unpack("\1\u01a7"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01a8"),
        DFA.unpack("\1\u01a9"),
        DFA.unpack(""),
        DFA.unpack("\1\u01aa"),
        DFA.unpack("\1\u01ab"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\u01ac\1\uffff\32\110"),
        DFA.unpack("\1\u01ae"),
        DFA.unpack("\1\u01af"),
        DFA.unpack("\1\u01b0"),
        DFA.unpack("\1\u01b1"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b2"),
        DFA.unpack("\1\u01b3"),
        DFA.unpack("\1\u01b4"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01b5"),
        DFA.unpack("\1\u01b6"),
        DFA.unpack("\1\u01b7"),
        DFA.unpack("\1\u01b8"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01bb"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01bc"),
        DFA.unpack(""),
        DFA.unpack("\1\u01bd"),
        DFA.unpack("\1\u01be"),
        DFA.unpack("\1\u01bf"),
        DFA.unpack(""),
        DFA.unpack("\1\u01c0"),
        DFA.unpack("\1\u01c1"),
        DFA.unpack("\1\u01c2"),
        DFA.unpack("\1\u01c3"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01c5"),
        DFA.unpack("\1\u01c6"),
        DFA.unpack(""),
        DFA.unpack("\1\u01c7"),
        DFA.unpack("\1\u01c8"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01cb"),
        DFA.unpack("\1\u01cc"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01ce\1\u01cf"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d1"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d3"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d6"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d8"),
        DFA.unpack(""),
        DFA.unpack("\1\u01d9"),
        DFA.unpack("\1\u01da"),
        DFA.unpack("\1\u01db"),
        DFA.unpack("\1\u01dc"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01dd"),
        DFA.unpack("\1\u01de"),
        DFA.unpack(""),
        DFA.unpack("\1\u01df"),
        DFA.unpack("\1\u01e0"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u01e2"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01e3"),
        DFA.unpack(""),
        DFA.unpack("\1\u01e4"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e6"),
        DFA.unpack("\1\u01e7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e9"),
        DFA.unpack("\1\u01ea"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01ec"),
        DFA.unpack("\1\u01ed"),
        DFA.unpack(""),
        DFA.unpack("\1\u01ee"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u01ef"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01f1"),
        DFA.unpack("\1\u01f2"),
        DFA.unpack("\1\u01f3"),
        DFA.unpack(""),
        DFA.unpack("\1\u01f4"),
        DFA.unpack("\1\u01f5"),
        DFA.unpack("\1\u01f6"),
        DFA.unpack("\1\u01f7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01f9"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u01fb"),
        DFA.unpack(""),
        DFA.unpack("\1\u01fc"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
    ]

    # class definition for DFA #41

    class DFA41(DFA):
        pass

        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0:
                LA41_57 = input.LA(1)

                s = -1
                if (0 <= LA41_57 <= 9) or (14 <= LA41_57 <= 65535) or LA41_57 in {11}:
                    s = 107

                else:
                    s = 67

                if s >= 0:
                    return s
            elif s == 1:
                LA41_58 = input.LA(1)

                s = -1
                if (0 <= LA41_58 <= 9) or (14 <= LA41_58 <= 65535) or LA41_58 in {11}:
                    s = 107

                else:
                    s = 67

                if s >= 0:
                    return s
            elif s == 2:
                LA41_0 = input.LA(1)

                s = -1
                if LA41_0 == 115:
                    s = 1

                elif LA41_0 == 119:
                    s = 2

                elif LA41_0 == 80:
                    s = 3

                elif LA41_0 == 67:
                    s = 4

                elif LA41_0 == 84:
                    s = 5

                elif LA41_0 == 83:
                    s = 6

                elif LA41_0 == 68:
                    s = 7

                elif LA41_0 == 76:
                    s = 8

                elif LA41_0 == 77:
                    s = 9

                elif LA41_0 == 111:
                    s = 10

                elif LA41_0 == 99:
                    s = 11

                elif LA41_0 == 103:
                    s = 12

                elif LA41_0 == 105:
                    s = 13

                elif LA41_0 == 101:
                    s = 14

                elif LA41_0 == 102:
                    s = 15

                elif LA41_0 == 109:
                    s = 16

                elif LA41_0 == 108:
                    s = 17

                elif LA41_0 == 114:
                    s = 18

                elif LA41_0 == 116:
                    s = 19

                elif LA41_0 == 118:
                    s = 20

                elif LA41_0 == 117:
                    s = 21

                elif LA41_0 == 112:
                    s = 22

                elif LA41_0 in {88, 89, 90, 120, 121, 122}:
                    s = 23

                elif LA41_0 == 107:
                    s = 24

                elif LA41_0 == 85:
                    s = 25

                elif LA41_0 == 78:
                    s = 26

                elif LA41_0 == 123:
                    s = 27

                elif LA41_0 == 97:
                    s = 28

                elif LA41_0 == 110:
                    s = 29

                elif LA41_0 == 95:
                    s = 30

                elif LA41_0 == 46:
                    s = 31

                elif LA41_0 == 44:
                    s = 32

                elif LA41_0 == 58:
                    s = 33

                elif LA41_0 == 59:
                    s = 34

                elif LA41_0 == 61:
                    s = 35

                elif LA41_0 == 124:
                    s = 36

                elif LA41_0 == 94:
                    s = 37

                elif LA41_0 == 38:
                    s = 38

                elif LA41_0 == 126:
                    s = 39

                elif LA41_0 == 60:
                    s = 40

                elif LA41_0 == 62:
                    s = 41

                elif LA41_0 == 43:
                    s = 42

                elif LA41_0 == 45:
                    s = 43

                elif LA41_0 == 42:
                    s = 44

                elif LA41_0 == 47:
                    s = 45

                elif LA41_0 == 37:
                    s = 46

                elif LA41_0 == 40:
                    s = 47

                elif LA41_0 == 41:
                    s = 48

                elif LA41_0 == 91:
                    s = 49

                elif LA41_0 == 93:
                    s = 50

                elif LA41_0 == 125:
                    s = 51

                elif LA41_0 == 33:
                    s = 52

                elif LA41_0 == 70:
                    s = 53

                elif LA41_0 == 36:
                    s = 54

                elif LA41_0 == 82:
                    s = 55

                elif (71 <= LA41_0 <= 75) or LA41_0 in {
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

                elif LA41_0 == 39:
                    s = 57

                elif LA41_0 == 34:
                    s = 58

                elif (49 <= LA41_0 <= 57) or LA41_0 in {}:
                    s = 59

                elif LA41_0 == 48:
                    s = 60

                elif LA41_0 == 13:
                    s = 61

                elif LA41_0 == 10:
                    s = 62

                elif LA41_0 == 12:
                    s = 63

                elif LA41_0 in {9, 32}:
                    s = 64

                elif LA41_0 == 35:
                    s = 65

                elif LA41_0 == 92:
                    s = 66

                elif (
                    (0 <= LA41_0 <= 8)
                    or (14 <= LA41_0 <= 31)
                    or (127 <= LA41_0 <= 65535)
                    or LA41_0 in {11, 63, 64, 96}
                ):
                    s = 67

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 41, _s, input)
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
