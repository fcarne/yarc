# $ANTLR 3.5.1 /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g 2023-05-06 17:52:51

import sys

from antlr3 import (
    DEFAULT_CHANNEL,
    DFA,
    BaseRecognizer,
    EarlyExitException,
    MismatchedSetException,
    NoViableAltException,
    RecognizerSharedState,
)

if __name__ is not None and "." in __name__:
    from .YarcLexerBase import YarcLexerBase
else:
    from YarcLexerBase import YarcLexerBase


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


class YarcLexer(YarcLexerBase):
    grammarFileName = "/media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa21 = self.DFA21(
            self,
            21,
            eot=self.DFA21_eot,
            eof=self.DFA21_eof,
            min=self.DFA21_min,
            max=self.DFA21_max,
            accept=self.DFA21_accept,
            special=self.DFA21_special,
            transition=self.DFA21_transition,
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

        self.dfa42 = self.DFA42(
            self,
            42,
            eot=self.DFA42_eot,
            eof=self.DFA42_eof,
            min=self.DFA42_min,
            max=self.DFA42_max,
            accept=self.DFA42_accept,
            special=self.DFA42_special,
            transition=self.DFA42_transition,
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
            if LA1 == 80:
                alt1 = 1
            elif LA1 == 67:
                LA1_2 = self.input.LA(2)

                if LA1_2 == 117:
                    alt1 = 2
                elif LA1_2 == 111:
                    alt1 = 3
                else:
                    nvae = NoViableAltException("", 1, 2, self.input)

                    raise nvae

            elif LA1 == 84:
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
            if LA2 == 83:
                alt2 = 1
            elif LA2 == 67:
                alt2 = 2
            elif LA2 == 68:
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
            if (88 <= self.input.LA(1) <= 90) or (120 <= self.input.LA(1) <= 122):
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
            if LA5 == 99:
                alt5 = 1
            elif LA5 == 107:
                alt5 = 2
            elif LA5 == 114:
                alt5 = 3
            elif LA5 == 112:
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

            if LA9_0 == 10 or (12 <= LA9_0 <= 13):
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
                elif (0 <= LA10_0 <= 122) or LA10_0 == 124 or (126 <= LA10_0 <= 65535):
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

    # $ANTLR start "ADD_ASSIGN"
    def mADD_ASSIGN(
        self,
    ):
        try:
            _type = ADD_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:15: ( '+=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:152:17: '+='
            self.match("+=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ADD_ASSIGN"

    # $ANTLR start "SUB_ASSIGN"
    def mSUB_ASSIGN(
        self,
    ):
        try:
            _type = SUB_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:153:15: ( '-=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:153:17: '-='
            self.match("-=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SUB_ASSIGN"

    # $ANTLR start "MULT_ASSIGN"
    def mMULT_ASSIGN(
        self,
    ):
        try:
            _type = MULT_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:154:15: ( '*=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:154:17: '*='
            self.match("*=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MULT_ASSIGN"

    # $ANTLR start "DIV_ASSIGN"
    def mDIV_ASSIGN(
        self,
    ):
        try:
            _type = DIV_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:155:15: ( '/=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:155:17: '/='
            self.match("/=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIV_ASSIGN"

    # $ANTLR start "MOD_ASSIGN"
    def mMOD_ASSIGN(
        self,
    ):
        try:
            _type = MOD_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:156:15: ( '%=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:156:17: '%='
            self.match("%=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOD_ASSIGN"

    # $ANTLR start "AND_ASSIGN"
    def mAND_ASSIGN(
        self,
    ):
        try:
            _type = AND_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:157:15: ( '&=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:157:17: '&='
            self.match("&=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND_ASSIGN"

    # $ANTLR start "OR_ASSIGN"
    def mOR_ASSIGN(
        self,
    ):
        try:
            _type = OR_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:158:15: ( '|=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:158:17: '|='
            self.match("|=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR_ASSIGN"

    # $ANTLR start "XOR_ASSIGN"
    def mXOR_ASSIGN(
        self,
    ):
        try:
            _type = XOR_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:159:15: ( '^=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:159:17: '^='
            self.match("^=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "XOR_ASSIGN"

    # $ANTLR start "LSHIFT_ASSIGN"
    def mLSHIFT_ASSIGN(
        self,
    ):
        try:
            _type = LSHIFT_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:15: ( '<<=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:160:17: '<<='
            self.match("<<=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LSHIFT_ASSIGN"

    # $ANTLR start "RSHIFT_ASSIGN"
    def mRSHIFT_ASSIGN(
        self,
    ):
        try:
            _type = RSHIFT_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:161:15: ( '>>=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:161:17: '>>='
            self.match(">>=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RSHIFT_ASSIGN"

    # $ANTLR start "POWER_ASSIGN"
    def mPOWER_ASSIGN(
        self,
    ):
        try:
            _type = POWER_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:162:15: ( '**=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:162:17: '**='
            self.match("**=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "POWER_ASSIGN"

    # $ANTLR start "IDIV_ASSIGN"
    def mIDIV_ASSIGN(
        self,
    ):
        try:
            _type = IDIV_ASSIGN
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:163:15: ( '//=' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:163:17: '//='
            self.match("//=")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IDIV_ASSIGN"

    # $ANTLR start "ID"
    def mID(
        self,
    ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:166:12: ( ID_START ( ID_CONTINUE )* )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:166:14: ID_START ( ID_CONTINUE )*
            self.mID_START()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:166:23: ( ID_CONTINUE )*
            while True:  # loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (
                    (48 <= LA11_0 <= 57)
                    or (65 <= LA11_0 <= 90)
                    or LA11_0 == 95
                    or (97 <= LA11_0 <= 122)
                ):
                    alt11 = 1

                if alt11 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (
                        (48 <= self.input.LA(1) <= 57)
                        or (65 <= self.input.LA(1) <= 90)
                        or self.input.LA(1) == 95
                        or (97 <= self.input.LA(1) <= 122)
                    ):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    break  # loop11

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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:167:12: ( '$' ID )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:167:14: '$' ID
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:170:7: ( ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:171:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:171:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )?
            alt14 = 4
            LA14 = self.input.LA(1)
            if LA14 == 85 or LA14 == 117:
                alt14 = 1
            elif LA14 == 70 or LA14 == 102:
                LA14_2 = self.input.LA(2)

                if LA14_2 == 82 or LA14_2 == 114:
                    alt14 = 2
                elif LA14_2 == 34 or LA14_2 == 39:
                    alt14 = 3
            elif LA14 == 82 or LA14 == 114:
                LA14_3 = self.input.LA(2)

                if LA14_3 == 34 or LA14_3 == 39:
                    alt14 = 2
                elif LA14_3 == 70 or LA14_3 == 102:
                    alt14 = 3
            if alt14 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:171:5: ( 'u' | 'U' )
                if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt14 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:172:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:172:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:172:7: ( 'f' | 'F' )? ( 'r' | 'R' )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:172:7: ( 'f' | 'F' )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if LA12_0 == 70 or LA12_0 == 102:
                    alt12 = 1
                if alt12 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if self.input.LA(1) == 70 or self.input.LA(1) == 102:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt14 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:173:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:173:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:173:7: ( 'r' | 'R' )? ( 'f' | 'F' )
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:173:7: ( 'r' | 'R' )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if LA13_0 == 82 or LA13_0 == 114:
                    alt13 = 1
                if alt13 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if self.input.LA(1) == 82 or self.input.LA(1) == 114:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                if self.input.LA(1) == 70 or self.input.LA(1) == 102:
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:178:9: ( NON_ZERO_DIGIT ( DIGIT )* | ( '0' )+ | '0' ( 'o' | 'O' ) ( OCT_DIGIT )+ | '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ | '0' ( 'b' | 'B' ) ( BIN_DIGIT )+ )
            alt20 = 5
            LA20_0 = self.input.LA(1)

            if 49 <= LA20_0 <= 57:
                alt20 = 1
            elif LA20_0 == 48:
                LA20 = self.input.LA(2)
                if LA20 == 79 or LA20 == 111:
                    alt20 = 3
                elif LA20 == 88 or LA20 == 120:
                    alt20 = 4
                elif LA20 == 66 or LA20 == 98:
                    alt20 = 5
                else:
                    alt20 = 2

            else:
                nvae = NoViableAltException("", 20, 0, self.input)

                raise nvae

            if alt20 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:3: NON_ZERO_DIGIT ( DIGIT )*
                self.mNON_ZERO_DIGIT()

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:18: ( DIGIT )*
                while True:  # loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if 48 <= LA15_0 <= 57:
                        alt15 = 1

                    if alt15 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if 48 <= self.input.LA(1) <= 57:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop15

            elif alt20 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:27: ( '0' )+
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:27: ( '0' )+
                cnt16 = 0
                while True:  # loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if LA16_0 == 48:
                        alt16 = 1

                    if alt16 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:179:27: '0'
                        self.match(48)

                    else:
                        if cnt16 >= 1:
                            break  # loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1

            elif alt20 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:180:5: '0' ( 'o' | 'O' ) ( OCT_DIGIT )+
                self.match(48)

                if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:180:21: ( OCT_DIGIT )+
                cnt17 = 0
                while True:  # loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if 48 <= LA17_0 <= 55:
                        alt17 = 1

                    if alt17 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if 48 <= self.input.LA(1) <= 55:
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

            elif alt20 == 4:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:181:5: '0' ( 'x' | 'X' ) ( HEX_DIGIT )+
                self.match(48)

                if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:181:21: ( HEX_DIGIT )+
                cnt18 = 0
                while True:  # loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (
                        (48 <= LA18_0 <= 57)
                        or (65 <= LA18_0 <= 70)
                        or (97 <= LA18_0 <= 102)
                    ):
                        alt18 = 1

                    if alt18 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if (
                            (48 <= self.input.LA(1) <= 57)
                            or (65 <= self.input.LA(1) <= 70)
                            or (97 <= self.input.LA(1) <= 102)
                        ):
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

            elif alt20 == 5:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:182:5: '0' ( 'b' | 'B' ) ( BIN_DIGIT )+
                self.match(48)

                if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:182:21: ( BIN_DIGIT )+
                cnt19 = 0
                while True:  # loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if 48 <= LA19_0 <= 49:
                        alt19 = 1

                    if alt19 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                        if 48 <= self.input.LA(1) <= 49:
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:185:14: ( POINT_FLOAT | EXPONENT_FLOAT )
            alt21 = 2
            alt21 = self.dfa21.predict(self.input)
            if alt21 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:185:16: POINT_FLOAT
                self.mPOINT_FLOAT()

            elif alt21 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:185:30: EXPONENT_FLOAT
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:188:8: ( ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:189:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:189:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )?
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt23 = 3
            LA23 = self.input.LA(1)
            if LA23 == 13:
                LA23_1 = self.input.LA(2)

                if LA23_1 == 10:
                    alt23 = 1
                else:
                    alt23 = 2

            elif LA23 == 10:
                alt23 = 1
            elif LA23 == 12:
                alt23 = 3
            else:
                nvae = NoViableAltException("", 23, 0, self.input)

                raise nvae

            if alt23 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:5: ( '\\r' )? '\\n'
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:5: ( '\\r' )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if LA22_0 == 13:
                    alt22 = 1
                if alt22 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:5: '\\r'
                    self.match(13)

                self.match(10)

            elif alt23 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:18: '\\r'
                self.match(13)

            elif alt23 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:25: '\\f'
                self.match(12)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:31: ( SPACES )?
            alt24 = 2
            LA24_0 = self.input.LA(1)

            if LA24_0 == 9 or LA24_0 == 32:
                alt24 = 1
            if alt24 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:190:31: SPACES
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:195:9: ( ( SPACES | COMMENT | LINE_JOINING ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:195:11: ( SPACES | COMMENT | LINE_JOINING )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:195:11: ( SPACES | COMMENT | LINE_JOINING )
            alt25 = 3
            LA25 = self.input.LA(1)
            if LA25 == 9 or LA25 == 32:
                alt25 = 1
            elif LA25 == 35:
                alt25 = 2
            elif LA25 == 92:
                alt25 = 3
            else:
                nvae = NoViableAltException("", 25, 0, self.input)

                raise nvae

            if alt25 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:195:13: SPACES
                self.mSPACES()

            elif alt25 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:195:22: COMMENT
                self.mCOMMENT()

            elif alt25 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:195:32: LINE_JOINING
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

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:196:9: ( . )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:196:11: .
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:199:22: ( '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\'' | '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"' )
            alt28 = 2
            LA28_0 = self.input.LA(1)

            if LA28_0 == 39:
                alt28 = 1
            elif LA28_0 == 34:
                alt28 = 2
            else:
                nvae = NoViableAltException("", 28, 0, self.input)

                raise nvae

            if alt28 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:3: '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\''
                self.match(39)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:8: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )*
                while True:  # loop26
                    alt26 = 3
                    LA26_0 = self.input.LA(1)

                    if LA26_0 == 92:
                        alt26 = 1
                    elif (
                        (0 <= LA26_0 <= 9)
                        or LA26_0 == 11
                        or (14 <= LA26_0 <= 38)
                        or (40 <= LA26_0 <= 91)
                        or (93 <= LA26_0 <= 65535)
                    ):
                        alt26 = 2

                    if alt26 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:9: STRING_ESCAPE_SEQ
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt26 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:200:29: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' )
                        if (
                            (0 <= self.input.LA(1) <= 9)
                            or self.input.LA(1) == 11
                            or (14 <= self.input.LA(1) <= 38)
                            or (40 <= self.input.LA(1) <= 91)
                            or (93 <= self.input.LA(1) <= 65535)
                        ):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop26

                self.match(39)

            elif alt28 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:5: '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"'
                self.match(34)

                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:9: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )*
                while True:  # loop27
                    alt27 = 3
                    LA27_0 = self.input.LA(1)

                    if LA27_0 == 92:
                        alt27 = 1
                    elif (
                        (0 <= LA27_0 <= 9)
                        or LA27_0 == 11
                        or (14 <= LA27_0 <= 33)
                        or (35 <= LA27_0 <= 91)
                        or (93 <= LA27_0 <= 65535)
                    ):
                        alt27 = 2

                    if alt27 == 1:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:10: STRING_ESCAPE_SEQ
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt27 == 2:
                        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:201:30: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' )
                        if (
                            (0 <= self.input.LA(1) <= 9)
                            or self.input.LA(1) == 11
                            or (14 <= self.input.LA(1) <= 33)
                            or (35 <= self.input.LA(1) <= 91)
                            or (93 <= self.input.LA(1) <= 65535)
                        ):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop27

                self.match(34)

        finally:
            pass

    # $ANTLR end "SHORT_STRING"

    # $ANTLR start "STRING_ESCAPE_SEQ"
    def mSTRING_ESCAPE_SEQ(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:203:28: ( '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' ) | '\\\\' NEWLINE )
            alt29 = 2
            LA29_0 = self.input.LA(1)

            if LA29_0 == 92:
                LA29_1 = self.input.LA(2)

                if (
                    (0 <= LA29_1 <= 8)
                    or LA29_1 == 11
                    or (14 <= LA29_1 <= 31)
                    or (33 <= LA29_1 <= 65535)
                ):
                    alt29 = 1
                elif LA29_1 == 10 or (12 <= LA29_1 <= 13):
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 29, 0, self.input)

                raise nvae

            if alt29 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:203:30: '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' )
                self.match(92)

                if (
                    (0 <= self.input.LA(1) <= 8)
                    or self.input.LA(1) == 11
                    or (14 <= self.input.LA(1) <= 31)
                    or (33 <= self.input.LA(1) <= 65535)
                ):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt29 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:203:72: '\\\\' NEWLINE
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:205:25: ( '1' .. '9' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if 49 <= self.input.LA(1) <= 57:
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:206:25: ( '0' .. '9' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if 48 <= self.input.LA(1) <= 57:
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:207:25: ( '0' .. '7' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if 48 <= self.input.LA(1) <= 55:
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:208:25: ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (
                (48 <= self.input.LA(1) <= 57)
                or (65 <= self.input.LA(1) <= 70)
                or (97 <= self.input.LA(1) <= 102)
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:209:25: ( '0' | '1' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if 48 <= self.input.LA(1) <= 49:
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:211:25: ( ( INT_PART )? FRACTION | INT_PART '.' )
            alt31 = 2
            alt31 = self.dfa31.predict(self.input)
            if alt31 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:211:27: ( INT_PART )? FRACTION
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:211:27: ( INT_PART )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if 48 <= LA30_0 <= 57:
                    alt30 = 1
                if alt30 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:211:27: INT_PART
                    self.mINT_PART()

                self.mFRACTION()

            elif alt31 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:211:48: INT_PART '.'
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:25: ( ( INT_PART | POINT_FLOAT ) EXPONENT )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:27: ( INT_PART | POINT_FLOAT ) EXPONENT
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:27: ( INT_PART | POINT_FLOAT )
            alt32 = 2
            alt32 = self.dfa32.predict(self.input)
            if alt32 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:29: INT_PART
                self.mINT_PART()

            elif alt32 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:212:40: POINT_FLOAT
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:213:25: ( ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:213:27: ( DIGIT )+
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:213:27: ( DIGIT )+
            cnt33 = 0
            while True:  # loop33
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if 48 <= LA33_0 <= 57:
                    alt33 = 1

                if alt33 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if 48 <= self.input.LA(1) <= 57:
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

    # $ANTLR end "INT_PART"

    # $ANTLR start "FRACTION"
    def mFRACTION(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:214:25: ( '.' ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:214:27: '.' ( DIGIT )+
            self.match(46)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:214:31: ( DIGIT )+
            cnt34 = 0
            while True:  # loop34
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if 48 <= LA34_0 <= 57:
                    alt34 = 1

                if alt34 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if 48 <= self.input.LA(1) <= 57:
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

    # $ANTLR end "FRACTION"

    # $ANTLR start "EXPONENT"
    def mEXPONENT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:215:25: ( ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:215:27: ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:215:39: ( '+' | '-' )?
            alt35 = 2
            LA35_0 = self.input.LA(1)

            if LA35_0 == 43 or LA35_0 == 45:
                alt35 = 1
            if alt35 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:215:52: ( DIGIT )+
            cnt36 = 0
            while True:  # loop36
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if 48 <= LA36_0 <= 57:
                    alt36 = 1

                if alt36 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if 48 <= self.input.LA(1) <= 57:
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

    # $ANTLR end "EXPONENT"

    # $ANTLR start "ID_START"
    def mID_START(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:217:22: ( UNDERSCORE | LETTER )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (
                (65 <= self.input.LA(1) <= 90)
                or self.input.LA(1) == 95
                or (97 <= self.input.LA(1) <= 122)
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:218:22: ( ID_START | DIGIT )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (
                (48 <= self.input.LA(1) <= 57)
                or (65 <= self.input.LA(1) <= 90)
                or self.input.LA(1) == 95
                or (97 <= self.input.LA(1) <= 122)
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:219:22: ( 'a' .. 'z' | 'A' .. 'Z' )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
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
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:221:23: ( ( ' ' | '\\t' )+ )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:221:25: ( ' ' | '\\t' )+
            pass
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:221:25: ( ' ' | '\\t' )+
            cnt37 = 0
            while True:  # loop37
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if LA37_0 == 9 or LA37_0 == 32:
                    alt37 = 1

                if alt37 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
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

    # $ANTLR end "SPACES"

    # $ANTLR start "COMMENT"
    def mCOMMENT(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:222:23: ( '#' (~ ( '\\r' | '\\n' | '\\f' ) )* )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:222:25: '#' (~ ( '\\r' | '\\n' | '\\f' ) )*
            self.match(35)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:222:29: (~ ( '\\r' | '\\n' | '\\f' ) )*
            while True:  # loop38
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (0 <= LA38_0 <= 9) or LA38_0 == 11 or (14 <= LA38_0 <= 65535):
                    alt38 = 1

                if alt38 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:
                    if (
                        (0 <= self.input.LA(1) <= 9)
                        or self.input.LA(1) == 11
                        or (14 <= self.input.LA(1) <= 65535)
                    ):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    break  # loop38

        finally:
            pass

    # $ANTLR end "COMMENT"

    # $ANTLR start "LINE_JOINING"
    def mLINE_JOINING(
        self,
    ):
        try:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:23: ( '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) )
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:25: '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            self.match(92)

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:30: ( SPACES )?
            alt39 = 2
            LA39_0 = self.input.LA(1)

            if LA39_0 == 9 or LA39_0 == 32:
                alt39 = 1
            if alt39 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:30: SPACES
                self.mSPACES()

            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:38: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt41 = 3
            LA41 = self.input.LA(1)
            if LA41 == 13:
                LA41_1 = self.input.LA(2)

                if LA41_1 == 10:
                    alt41 = 1
                else:
                    alt41 = 2

            elif LA41 == 10:
                alt41 = 1
            elif LA41 == 12:
                alt41 = 3
            else:
                nvae = NoViableAltException("", 41, 0, self.input)

                raise nvae

            if alt41 == 1:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:40: ( '\\r' )? '\\n'
                pass
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:40: ( '\\r' )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if LA40_0 == 13:
                    alt40 = 1
                if alt40 == 1:
                    # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:40: '\\r'
                    self.match(13)

                self.match(10)

            elif alt41 == 2:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:53: '\\r'
                self.match(13)

            elif alt41 == 3:
                # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:223:60: '\\f'
                self.match(12)

        finally:
            pass

    # $ANTLR end "LINE_JOINING"

    def mTokens(self):
        # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:8: ( SCENARIO | SETTINGS | STAGE | WRITERS | SHAPES | SHAPES_OR_LIGHTS | CAMERA | LIGHT | LIGHT_TYPE | STEREO | MATERIAL | TIMELINE | OPEN | CREATE | GROUP | INSTANTIATE | GET | EDIT | FETCH | MATCH | LIMIT | RECURSIVE | TRANSLATE | CAM_TRANSLATE | ROTATE | SCALE | SEMANTICS | VISIBLE | SIZE | LOOK_AT | UP_AXIS | AXIS | ORDER | SCATTER | ROT_AROUND | PHYSICS | EVERY | FRAMES | TIME | UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM | SNIPPET | TO | ON | AT | AND | ELSE | FALSE | FOR | FROM | IF | IN | IS | NONE | NOT | OR | TRUE | UNDERSCORE | DOT | RANGE | ELLIPSIS | COMMA | COLON | SEMI | ASSIGN | BIT_OR | XOR | BIT_AND | BIT_NOT | LSHIFT | RSHIFT | PLUS | MINUS | MUL | DIV | MOD | IDIV | POWER | LPAREN | RPAREN | LBRACK | RBRACK | LBRACE | RBRACE | LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | ADD_ASSIGN | SUB_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | POWER_ASSIGN | IDIV_ASSIGN | ID | SETTING_ID | STRING | INTEGER | FLOAT_NUMBER | NEWLINE | SKIP_ | UNKNOWN )
        alt42 = 113
        alt42 = self.dfa42.predict(self.input)
        if alt42 == 1:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:10: SCENARIO
            self.mSCENARIO()

        elif alt42 == 2:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:19: SETTINGS
            self.mSETTINGS()

        elif alt42 == 3:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:28: STAGE
            self.mSTAGE()

        elif alt42 == 4:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:34: WRITERS
            self.mWRITERS()

        elif alt42 == 5:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:42: SHAPES
            self.mSHAPES()

        elif alt42 == 6:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:49: SHAPES_OR_LIGHTS
            self.mSHAPES_OR_LIGHTS()

        elif alt42 == 7:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:66: CAMERA
            self.mCAMERA()

        elif alt42 == 8:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:73: LIGHT
            self.mLIGHT()

        elif alt42 == 9:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:79: LIGHT_TYPE
            self.mLIGHT_TYPE()

        elif alt42 == 10:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:90: STEREO
            self.mSTEREO()

        elif alt42 == 11:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:97: MATERIAL
            self.mMATERIAL()

        elif alt42 == 12:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:106: TIMELINE
            self.mTIMELINE()

        elif alt42 == 13:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:115: OPEN
            self.mOPEN()

        elif alt42 == 14:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:120: CREATE
            self.mCREATE()

        elif alt42 == 15:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:127: GROUP
            self.mGROUP()

        elif alt42 == 16:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:133: INSTANTIATE
            self.mINSTANTIATE()

        elif alt42 == 17:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:145: GET
            self.mGET()

        elif alt42 == 18:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:149: EDIT
            self.mEDIT()

        elif alt42 == 19:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:154: FETCH
            self.mFETCH()

        elif alt42 == 20:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:160: MATCH
            self.mMATCH()

        elif alt42 == 21:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:166: LIMIT
            self.mLIMIT()

        elif alt42 == 22:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:172: RECURSIVE
            self.mRECURSIVE()

        elif alt42 == 23:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:182: TRANSLATE
            self.mTRANSLATE()

        elif alt42 == 24:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:192: CAM_TRANSLATE
            self.mCAM_TRANSLATE()

        elif alt42 == 25:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:206: ROTATE
            self.mROTATE()

        elif alt42 == 26:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:213: SCALE
            self.mSCALE()

        elif alt42 == 27:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:219: SEMANTICS
            self.mSEMANTICS()

        elif alt42 == 28:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:229: VISIBLE
            self.mVISIBLE()

        elif alt42 == 29:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:237: SIZE
            self.mSIZE()

        elif alt42 == 30:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:242: LOOK_AT
            self.mLOOK_AT()

        elif alt42 == 31:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:250: UP_AXIS
            self.mUP_AXIS()

        elif alt42 == 32:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:258: AXIS
            self.mAXIS()

        elif alt42 == 33:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:263: ORDER
            self.mORDER()

        elif alt42 == 34:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:269: SCATTER
            self.mSCATTER()

        elif alt42 == 35:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:277: ROT_AROUND
            self.mROT_AROUND()

        elif alt42 == 36:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:288: PHYSICS
            self.mPHYSICS()

        elif alt42 == 37:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:296: EVERY
            self.mEVERY()

        elif alt42 == 38:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:302: FRAMES
            self.mFRAMES()

        elif alt42 == 39:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:309: TIME
            self.mTIME()

        elif alt42 == 40:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:314: UNIFORM
            self.mUNIFORM()

        elif alt42 == 41:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:322: NORMAL
            self.mNORMAL()

        elif alt42 == 42:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:329: CHOICE
            self.mCHOICE()

        elif alt42 == 43:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:336: SEQUENCE
            self.mSEQUENCE()

        elif alt42 == 44:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:345: LOG_UNIFORM
            self.mLOG_UNIFORM()

        elif alt42 == 45:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:357: SNIPPET
            self.mSNIPPET()

        elif alt42 == 46:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:365: TO
            self.mTO()

        elif alt42 == 47:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:368: ON
            self.mON()

        elif alt42 == 48:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:371: AT
            self.mAT()

        elif alt42 == 49:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:374: AND
            self.mAND()

        elif alt42 == 50:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:378: ELSE
            self.mELSE()

        elif alt42 == 51:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:383: FALSE
            self.mFALSE()

        elif alt42 == 52:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:389: FOR
            self.mFOR()

        elif alt42 == 53:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:393: FROM
            self.mFROM()

        elif alt42 == 54:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:398: IF
            self.mIF()

        elif alt42 == 55:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:401: IN
            self.mIN()

        elif alt42 == 56:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:404: IS
            self.mIS()

        elif alt42 == 57:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:407: NONE
            self.mNONE()

        elif alt42 == 58:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:412: NOT
            self.mNOT()

        elif alt42 == 59:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:416: OR
            self.mOR()

        elif alt42 == 60:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:419: TRUE
            self.mTRUE()

        elif alt42 == 61:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:424: UNDERSCORE
            self.mUNDERSCORE()

        elif alt42 == 62:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:435: DOT
            self.mDOT()

        elif alt42 == 63:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:439: RANGE
            self.mRANGE()

        elif alt42 == 64:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:445: ELLIPSIS
            self.mELLIPSIS()

        elif alt42 == 65:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:454: COMMA
            self.mCOMMA()

        elif alt42 == 66:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:460: COLON
            self.mCOLON()

        elif alt42 == 67:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:466: SEMI
            self.mSEMI()

        elif alt42 == 68:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:471: ASSIGN
            self.mASSIGN()

        elif alt42 == 69:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:478: BIT_OR
            self.mBIT_OR()

        elif alt42 == 70:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:485: XOR
            self.mXOR()

        elif alt42 == 71:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:489: BIT_AND
            self.mBIT_AND()

        elif alt42 == 72:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:497: BIT_NOT
            self.mBIT_NOT()

        elif alt42 == 73:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:505: LSHIFT
            self.mLSHIFT()

        elif alt42 == 74:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:512: RSHIFT
            self.mRSHIFT()

        elif alt42 == 75:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:519: PLUS
            self.mPLUS()

        elif alt42 == 76:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:524: MINUS
            self.mMINUS()

        elif alt42 == 77:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:530: MUL
            self.mMUL()

        elif alt42 == 78:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:534: DIV
            self.mDIV()

        elif alt42 == 79:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:538: MOD
            self.mMOD()

        elif alt42 == 80:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:542: IDIV
            self.mIDIV()

        elif alt42 == 81:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:547: POWER
            self.mPOWER()

        elif alt42 == 82:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:553: LPAREN
            self.mLPAREN()

        elif alt42 == 83:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:560: RPAREN
            self.mRPAREN()

        elif alt42 == 84:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:567: LBRACK
            self.mLBRACK()

        elif alt42 == 85:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:574: RBRACK
            self.mRBRACK()

        elif alt42 == 86:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:581: LBRACE
            self.mLBRACE()

        elif alt42 == 87:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:588: RBRACE
            self.mRBRACE()

        elif alt42 == 88:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:595: LT
            self.mLT()

        elif alt42 == 89:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:598: GT
            self.mGT()

        elif alt42 == 90:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:601: EQUALS
            self.mEQUALS()

        elif alt42 == 91:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:608: GT_EQ
            self.mGT_EQ()

        elif alt42 == 92:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:614: LT_EQ
            self.mLT_EQ()

        elif alt42 == 93:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:620: NOT_EQ
            self.mNOT_EQ()

        elif alt42 == 94:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:627: ADD_ASSIGN
            self.mADD_ASSIGN()

        elif alt42 == 95:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:638: SUB_ASSIGN
            self.mSUB_ASSIGN()

        elif alt42 == 96:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:649: MULT_ASSIGN
            self.mMULT_ASSIGN()

        elif alt42 == 97:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:661: DIV_ASSIGN
            self.mDIV_ASSIGN()

        elif alt42 == 98:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:672: MOD_ASSIGN
            self.mMOD_ASSIGN()

        elif alt42 == 99:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:683: AND_ASSIGN
            self.mAND_ASSIGN()

        elif alt42 == 100:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:694: OR_ASSIGN
            self.mOR_ASSIGN()

        elif alt42 == 101:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:704: XOR_ASSIGN
            self.mXOR_ASSIGN()

        elif alt42 == 102:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:715: LSHIFT_ASSIGN
            self.mLSHIFT_ASSIGN()

        elif alt42 == 103:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:729: RSHIFT_ASSIGN
            self.mRSHIFT_ASSIGN()

        elif alt42 == 104:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:743: POWER_ASSIGN
            self.mPOWER_ASSIGN()

        elif alt42 == 105:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:756: IDIV_ASSIGN
            self.mIDIV_ASSIGN()

        elif alt42 == 106:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:768: ID
            self.mID()

        elif alt42 == 107:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:771: SETTING_ID
            self.mSETTING_ID()

        elif alt42 == 108:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:782: STRING
            self.mSTRING()

        elif alt42 == 109:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:789: INTEGER
            self.mINTEGER()

        elif alt42 == 110:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:797: FLOAT_NUMBER
            self.mFLOAT_NUMBER()

        elif alt42 == 111:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:810: NEWLINE
            self.mNEWLINE()

        elif alt42 == 112:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:818: SKIP_
            self.mSKIP_()

        elif alt42 == 113:
            # /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v3/YarcLexer.g:1:824: UNKNOWN
            self.mUNKNOWN()

    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack("\3\uffff\1\6\1\uffff\1\6\1\uffff")

    DFA21_eof = DFA.unpack("\7\uffff")

    DFA21_min = DFA.unpack("\2\56\2\60\1\uffff\1\60\1\uffff")

    DFA21_max = DFA.unpack("\1\71\1\145\1\71\1\145\1\uffff\1\145\1\uffff")

    DFA21_accept = DFA.unpack("\4\uffff\1\2\1\uffff\1\1")

    DFA21_special = DFA.unpack("\7\uffff")

    DFA21_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack("\12\5"),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
    ]

    # class definition for DFA #21

    class DFA21(DFA):
        pass

    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack("\3\uffff\1\4\1\uffff")

    DFA31_eof = DFA.unpack("\5\uffff")

    DFA31_min = DFA.unpack("\2\56\1\uffff\1\60\1\uffff")

    DFA31_max = DFA.unpack("\2\71\1\uffff\1\71\1\uffff")

    DFA31_accept = DFA.unpack("\2\uffff\1\1\1\uffff\1\2")

    DFA31_special = DFA.unpack("\5\uffff")

    DFA31_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1"),
        DFA.unpack(""),
        DFA.unpack("\12\2"),
        DFA.unpack(""),
    ]

    # class definition for DFA #31

    class DFA31(DFA):
        pass

    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack("\4\uffff")

    DFA32_eof = DFA.unpack("\4\uffff")

    DFA32_min = DFA.unpack("\2\56\2\uffff")

    DFA32_max = DFA.unpack("\1\71\1\145\2\uffff")

    DFA32_accept = DFA.unpack("\2\uffff\1\2\1\1")

    DFA32_special = DFA.unpack("\4\uffff")

    DFA32_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\2\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(""),
        DFA.unpack(""),
    ]

    # class definition for DFA #32

    class DFA32(DFA):
        pass

    # lookup tables for DFA #42

    DFA42_eot = DFA.unpack(
        "\1\uffff\26\110\1\172\4\110\1\u0080\2\110\1\u0085\1\u0087\3\uffff"
        "\1\u008d\1\u008f\1\u0091\1\u0093\1\uffff\1\u0097\1\u009a\1\u009c"
        "\1\u009e\1\u00a1\1\u00a4\1\u00a6\5\uffff\1\103\1\110\1\103\1\uffff"
        "\2\103\2\u00ae\5\uffff\1\103\1\uffff\4\110\1\uffff\22\110\1\uffff"
        "\2\110\1\u00cd\1\u00ce\5\110\1\u00d5\1\u00d6\1\u00d7\17\110\1\u00e8"
        "\2\110\1\uffff\5\110\2\uffff\1\u00f0\2\110\1\uffff\1\u00f5\16\uffff"
        "\1\u00f7\2\uffff\1\u00f9\6\uffff\1\u00fb\2\uffff\1\u00fd\14\uffff"
        "\2\u00ae\2\uffff\4\110\1\u0104\25\110\2\uffff\4\110\1\u011f\1\110"
        "\3\uffff\7\110\1\u0128\10\110\1\uffff\2\110\1\u0133\4\110\1\uffff"
        "\1\u0138\1\110\1\u013a\12\uffff\6\110\1\uffff\1\110\1\u0142\2\110"
        "\2\u0145\10\110\1\u014e\1\110\1\u0150\2\110\1\u0150\1\110\1\u0154"
        "\4\110\1\uffff\1\110\1\u015a\1\110\1\u015c\2\110\1\u015f\1\110"
        "\1\uffff\7\110\1\u0168\2\110\1\uffff\4\110\1\uffff\1\u016f\1\uffff"
        "\1\110\1\u0171\4\110\1\u0176\1\uffff\1\110\1\u0145\1\uffff\3\110"
        "\1\u0145\4\110\1\uffff\1\110\1\uffff\1\u0180\2\110\1\uffff\3\110"
        "\1\u0186\1\110\1\uffff\1\u0188\1\uffff\1\u0189\1\u018b\1\uffff"
        "\1\u018c\1\u018d\1\u018e\5\110\1\uffff\6\110\1\uffff\1\110\1\uffff"
        "\3\110\1\u0104\1\uffff\2\110\1\u01a1\1\u01a2\1\110\1\u014e\1\u01a4"
        "\2\110\1\uffff\2\110\1\u01a9\2\110\1\uffff\1\110\2\uffff\1\u018b"
        "\4\uffff\2\110\1\u01b0\7\110\1\u01b8\4\110\1\u0104\1\u01bd\1\110"
        "\2\uffff\1\110\1\uffff\1\110\1\u0150\2\110\1\uffff\3\110\1\u01c6"
        "\2\110\1\uffff\2\110\1\u01cb\1\u01cc\2\110\1\u01cf\1\uffff\1\u01d0"
        "\1\110\1\u01d3\1\110\1\uffff\1\u014e\1\u01d5\1\u01d6\1\110\1\u01d8"
        "\1\110\1\u01da\1\110\1\uffff\4\110\2\uffff\2\110\2\uffff\2\110"
        "\1\uffff\1\u01e4\2\uffff\1\110\1\uffff\1\110\1\uffff\1\110\1\u01e8"
        "\2\110\1\u01eb\2\110\2\u01ee\1\uffff\1\u01ef\2\110\1\uffff\1\110"
        "\1\u01da\1\uffff\1\u01da\1\110\2\uffff\1\110\1\u01f5\3\110\1\uffff"
        "\3\110\1\u01fc\2\110\1\uffff\3\110\1\u0202\1\u01da\1\uffff"
    )

    DFA42_eof = DFA.unpack("\u0203\uffff")

    DFA42_min = DFA.unpack(
        "\1\0\1\143\1\162\1\154\1\141\1\151\1\145\2\151\1\42\1\141\1\156"
        "\1\141\1\145\1\146\1\144\1\42\1\141\1\151\1\42\1\157\1\151\1\42"
        "\1\60\1\151\1\150\1\42\1\157\1\173\1\156\1\157\1\60\1\56\3\uffff"
        "\4\75\1\uffff\1\74\3\75\1\52\1\57\1\75\5\uffff\1\75\1\42\1\101"
        "\1\uffff\2\0\2\56\5\uffff\1\11\1\uffff\1\141\1\143\1\141\1\172"
        "\1\uffff\1\151\1\141\1\142\1\156\1\154\1\155\1\157\1\162\1\155"
        "\1\150\1\145\1\161\1\163\1\155\2\147\1\143\1\42\1\uffff\1\164\1"
        "\145\2\60\1\145\1\155\1\154\1\157\1\164\3\60\1\151\1\145\1\163"
        "\1\164\1\42\1\154\1\162\1\42\1\164\1\155\1\157\1\143\1\164\1\147"
        "\1\141\1\60\1\163\1\137\1\uffff\1\130\1\156\1\171\1\151\1\162\2"
        "\uffff\1\60\1\144\1\156\1\uffff\1\56\16\uffff\1\75\2\uffff\1\75"
        "\6\uffff\1\75\2\uffff\1\75\14\uffff\2\56\2\uffff\1\156\1\154\1"
        "\164\1\141\1\60\1\147\1\145\1\164\1\156\2\145\1\151\1\145\1\151"
        "\1\165\2\145\1\162\1\165\1\153\1\145\1\150\1\125\1\164\1\145\1"
        "\156\2\uffff\1\141\1\145\1\154\1\165\1\60\1\164\3\uffff\1\164\1"
        "\162\1\145\1\143\2\155\1\163\1\60\1\143\1\151\1\153\1\165\1\141"
        "\1\151\1\156\1\145\1\uffff\1\151\1\141\1\60\1\145\1\163\1\146\1"
        "\155\1\uffff\1\60\1\145\1\60\12\uffff\1\141\1\145\1\164\1\151\2"
        "\156\1\uffff\1\145\1\60\2\145\2\60\1\156\1\162\1\143\1\163\1\154"
        "\1\162\2\145\1\60\1\141\1\60\1\164\1\156\1\60\1\162\1\60\1\164"
        "\1\162\1\151\1\160\1\uffff\1\141\1\60\1\171\1\60\1\150\1\145\1"
        "\60\1\145\1\uffff\1\150\1\164\1\137\1\162\1\164\1\144\1\163\1\60"
        "\1\142\1\170\1\uffff\1\155\1\151\1\157\1\141\1\uffff\1\60\1\uffff"
        "\1\162\1\60\1\145\1\156\1\164\1\144\1\60\1\uffff\1\162\1\60\1\uffff"
        "\1\144\1\141\1\145\1\60\1\151\1\145\1\157\1\156\1\uffff\1\156\1"
        "\uffff\1\60\2\151\1\uffff\1\145\1\141\1\144\1\60\1\156\1\uffff"
        "\1\60\1\uffff\2\60\1\uffff\3\60\1\141\1\163\1\145\1\137\1\154\1"
        "\uffff\1\154\1\151\1\141\1\143\1\162\1\154\1\uffff\1\151\1\uffff"
        "\1\162\1\147\1\151\1\60\1\uffff\1\163\1\145\2\60\1\156\2\60\1\143"
        "\1\164\1\uffff\1\146\1\141\1\60\1\137\1\145\1\uffff\1\164\2\uffff"
        "\1\60\4\uffff\1\164\1\151\1\60\1\142\1\141\1\145\1\163\1\164\1"
        "\163\1\155\1\60\1\157\1\137\1\163\1\143\2\60\1\162\2\uffff\1\145"
        "\1\uffff\1\145\1\60\1\157\1\154\1\uffff\1\164\1\162\1\151\1\60"
        "\1\166\1\141\1\uffff\1\157\1\164\2\60\1\151\1\137\1\60\1\uffff"
        "\1\60\1\62\1\60\1\163\1\uffff\3\60\1\162\1\60\1\162\1\60\1\141"
        "\1\uffff\1\145\1\162\1\144\1\145\2\uffff\1\143\1\155\2\uffff\2"
        "\144\1\uffff\1\60\2\uffff\1\155\1\uffff\1\141\1\uffff\1\164\1\60"
        "\1\157\1\171\1\60\1\163\1\141\2\60\1\uffff\1\60\1\156\1\145\1\uffff"
        "\1\165\1\60\1\uffff\1\60\1\164\2\uffff\1\163\1\60\1\156\1\145\1"
        "\154\1\uffff\1\144\1\162\1\141\1\60\1\151\1\164\1\uffff\1\141\1"
        "\145\1\154\2\60\1\uffff"
    )

    DFA42_max = DFA.unpack(
        "\1\uffff\1\164\1\162\1\154\1\171\1\157\1\164\2\157\1\146\1\141"
        "\3\162\1\163\1\166\1\162\1\141\2\157\1\162\1\151\1\160\1\172\1"
        "\151\1\150\1\156\1\157\1\173\1\164\1\157\1\172\1\71\3\uffff\4\75"
        "\1\uffff\1\75\1\76\5\75\5\uffff\1\75\1\162\1\172\1\uffff\2\uffff"
        "\2\145\5\uffff\1\40\1\uffff\1\145\1\164\1\141\1\172\1\uffff\1\151"
        "\1\141\1\142\1\156\1\154\1\155\1\157\1\162\1\155\1\150\1\145\1"
        "\161\1\163\1\155\2\147\1\143\1\47\1\uffff\1\164\1\145\2\172\1\145"
        "\1\155\1\154\1\157\1\164\3\172\1\151\1\145\1\163\1\164\1\157\1"
        "\154\1\162\1\47\1\164\1\155\1\157\1\143\1\164\1\147\1\165\1\172"
        "\1\163\1\137\1\uffff\1\172\1\156\1\171\1\151\1\162\2\uffff\1\172"
        "\1\144\1\164\1\uffff\1\56\16\uffff\1\75\2\uffff\1\75\6\uffff\1"
        "\75\2\uffff\1\75\14\uffff\2\145\2\uffff\1\156\2\164\1\141\1\172"
        "\1\147\1\145\1\164\1\156\2\145\1\151\1\145\1\151\1\165\2\145\1"
        "\162\1\165\1\164\1\145\1\150\1\125\1\164\1\145\1\156\2\uffff\1"
        "\141\1\145\1\154\1\165\1\172\1\164\3\uffff\1\164\1\162\1\145\1"
        "\143\2\155\1\163\1\172\1\143\1\151\1\153\1\165\1\141\1\151\1\156"
        "\1\145\1\uffff\1\151\1\141\1\172\1\145\1\163\1\146\1\155\1\uffff"
        "\1\172\1\145\1\172\12\uffff\1\141\1\145\1\164\1\151\2\156\1\uffff"
        "\1\145\1\172\2\145\2\172\1\156\1\162\1\143\1\163\1\154\1\162\2"
        "\145\1\172\1\141\1\172\1\164\1\156\1\172\1\162\1\172\1\164\1\162"
        "\1\151\1\160\1\uffff\1\141\1\172\1\171\1\172\1\150\1\145\1\172"
        "\1\145\1\uffff\1\150\1\164\1\137\1\162\1\164\1\144\1\163\1\172"
        "\1\142\1\170\1\uffff\1\155\1\151\1\157\1\141\1\uffff\1\172\1\uffff"
        "\1\162\1\172\1\145\1\156\1\164\1\144\1\172\1\uffff\1\162\1\172"
        "\1\uffff\1\144\1\141\1\145\1\172\1\151\1\145\1\157\1\156\1\uffff"
        "\1\156\1\uffff\1\172\2\151\1\uffff\1\145\1\141\1\144\1\172\1\156"
        "\1\uffff\1\172\1\uffff\2\172\1\uffff\3\172\1\141\1\163\1\145\1"
        "\137\1\154\1\uffff\1\154\1\151\1\141\1\143\1\162\1\154\1\uffff"
        "\1\151\1\uffff\1\162\1\147\1\151\1\172\1\uffff\1\163\1\145\2\172"
        "\1\156\2\172\1\143\1\164\1\uffff\1\146\1\141\1\172\1\137\1\145"
        "\1\uffff\1\164\2\uffff\1\172\4\uffff\1\164\1\151\1\172\1\142\1"
        "\141\1\145\1\163\1\164\1\163\1\155\1\172\1\157\1\137\1\163\1\143"
        "\2\172\1\162\2\uffff\1\145\1\uffff\1\145\1\172\1\157\1\154\1\uffff"
        "\1\164\1\162\1\151\1\172\1\166\1\141\1\uffff\1\157\1\164\2\172"
        "\1\151\1\137\1\172\1\uffff\1\172\1\63\1\172\1\163\1\uffff\3\172"
        "\1\162\1\172\1\162\1\172\1\141\1\uffff\1\145\1\162\1\144\1\145"
        "\2\uffff\1\143\1\155\2\uffff\2\144\1\uffff\1\172\2\uffff\1\155"
        "\1\uffff\1\141\1\uffff\1\164\1\172\1\157\1\171\1\172\1\163\1\141"
        "\2\172\1\uffff\1\172\1\156\1\145\1\uffff\1\165\1\172\1\uffff\1"
        "\172\1\164\2\uffff\1\163\1\172\1\156\1\145\1\154\1\uffff\1\144"
        "\1\162\1\141\1\172\1\151\1\164\1\uffff\1\141\1\145\1\154\2\172"
        "\1\uffff"
    )

    DFA42_accept = DFA.unpack(
        "\41\uffff\1\101\1\102\1\103\4\uffff\1\110\7\uffff\1\122\1\123\1"
        "\124\1\125\1\127\3\uffff\1\152\4\uffff\3\157\2\160\1\uffff\1\161"
        "\4\uffff\1\152\22\uffff\1\154\36\uffff\1\40\5\uffff\1\126\1\55"
        "\3\uffff\1\75\1\uffff\1\76\1\156\1\101\1\102\1\103\1\132\1\104"
        "\1\144\1\105\1\145\1\106\1\143\1\107\1\110\1\uffff\1\134\1\130"
        "\1\uffff\1\133\1\131\1\136\1\113\1\137\1\114\1\uffff\1\140\1\115"
        "\1\uffff\1\141\1\116\1\142\1\117\1\122\1\123\1\124\1\125\1\127"
        "\1\135\1\153\1\155\2\uffff\1\157\1\160\32\uffff\1\57\1\73\6\uffff"
        "\1\67\1\66\1\70\20\uffff\1\56\7\uffff\1\60\3\uffff\1\100\1\77\1"
        "\146\1\111\1\147\1\112\1\150\1\121\1\151\1\120\6\uffff\1\47\32"
        "\uffff\1\21\10\uffff\1\64\12\uffff\1\41\4\uffff\1\61\1\uffff\1"
        "\72\7\uffff\1\35\2\uffff\1\5\10\uffff\1\6\1\uffff\1\11\3\uffff"
        "\1\15\5\uffff\1\22\1\uffff\1\62\2\uffff\1\65\10\uffff\1\74\6\uffff"
        "\1\71\1\uffff\1\32\4\uffff\1\3\11\uffff\1\10\5\uffff\1\17\1\uffff"
        "\1\45\1\23\1\uffff\1\46\1\63\1\24\1\25\22\uffff\1\7\1\52\1\uffff"
        "\1\12\4\uffff\1\16\6\uffff\1\31\7\uffff\1\51\4\uffff\1\4\10\uffff"
        "\1\36\4\uffff\1\34\1\37\2\uffff\1\50\1\1\2\uffff\1\2\1\uffff\1"
        "\14\1\53\1\uffff\1\13\1\uffff\1\44\11\uffff\1\33\3\uffff\1\26\2"
        "\uffff\1\27\2\uffff\1\42\1\54\5\uffff\1\20\6\uffff\1\43\5\uffff"
        "\1\30"
    )

    DFA42_special = DFA.unpack("\1\0\70\uffff\1\1\1\2\u01c8\uffff")

    DFA42_transition = [
        DFA.unpack(
            "\11\103\1\100\1\76\1\103\1\77\1\75\22\103\1\100\1\65"
            "\1\72\1\101\1\67\1\57\1\47\1\71\1\60\1\61\1\55\1\53\1\41\1\54\1"
            "\40\1\56\1\74\11\73\1\42\1\43\1\51\1\44\1\52\2\103\2\70\1\4\1\7"
            "\1\70\1\66\5\70\1\10\1\12\1\33\1\70\1\3\1\70\1\11\1\6\1\5\1\32"
            "\2\70\3\27\1\62\1\102\1\63\1\46\1\37\1\103\1\35\1\70\1\14\1\70"
            "\1\17\1\20\1\15\1\70\1\16\1\70\1\30\1\22\1\21\1\36\1\13\1\31\1"
            "\70\1\23\1\1\1\24\1\26\1\25\1\2\3\27\1\34\1\45\1\64\1\50\uff81"
            "\103"
        ),
        DFA.unpack("\1\104\1\uffff\1\105\3\uffff\1\107\12\uffff\1\106"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\116\6\uffff\1\117\6\uffff\1\114\5\uffff\1\113\3" "\uffff\1\115"),
        DFA.unpack("\1\121\5\uffff\1\120"),
        DFA.unpack("\1\124\12\uffff\1\122\3\uffff\1\123"),
        DFA.unpack("\1\125\5\uffff\1\126"),
        DFA.unpack("\1\127\5\uffff\1\130"),
        DFA.unpack("\1\133\4\uffff\1\133\36\uffff\1\132\36\uffff\1\131" "\1\132"),
        DFA.unpack("\1\134"),
        DFA.unpack("\1\136\1\uffff\1\135\1\uffff\1\137"),
        DFA.unpack("\1\141\15\uffff\1\142\2\uffff\1\140"),
        DFA.unpack("\1\144\14\uffff\1\143"),
        DFA.unpack("\1\146\7\uffff\1\145\4\uffff\1\147"),
        DFA.unpack("\1\150\7\uffff\1\152\11\uffff\1\151"),
        DFA.unpack(
            "\1\133\4\uffff\1\133\52\uffff\1\157\16\uffff\1\155"
            "\3\uffff\1\153\11\uffff\1\156\2\uffff\1\154"
        ),
        DFA.unpack("\1\160"),
        DFA.unpack("\1\161\5\uffff\1\162"),
        DFA.unpack(
            "\1\133\4\uffff\1\133\36\uffff\1\132\36\uffff\1\163"
            "\1\132\2\uffff\1\165\5\uffff\1\164"
        ),
        DFA.unpack("\1\167\2\uffff\1\166"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\133\4\uffff\1\133\110\uffff\1\171"),
        DFA.unpack(
            "\12\110\7\uffff\27\110\3\173\4\uffff\1\110\1\uffff" "\27\110\3\173"
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
        DFA.unpack("\1\u0090"),
        DFA.unpack("\1\u0092"),
        DFA.unpack(""),
        DFA.unpack("\1\u0095\1\u0096"),
        DFA.unpack("\1\u0099\1\u0098"),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\1\u009d"),
        DFA.unpack("\1\u009f\22\uffff\1\u00a0"),
        DFA.unpack("\1\u00a2\15\uffff\1\u00a3"),
        DFA.unpack("\1\u00a5"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00ac"),
        DFA.unpack("\1\133\4\uffff\1\133\52\uffff\1\157\37\uffff\1\157"),
        DFA.unpack("\32\u00ad\4\uffff\1\u00ad\1\uffff\32\u00ad"),
        DFA.unpack(""),
        DFA.unpack("\12\133\1\uffff\1\133\2\uffff\ufff2\133"),
        DFA.unpack("\12\133\1\uffff\1\133\2\uffff\ufff2\133"),
        DFA.unpack("\1\u0088\1\uffff\12\u00af\13\uffff\1\u0088\37\uffff" "\1\u0088"),
        DFA.unpack(
            "\1\u0088\1\uffff\1\u00b0\11\u0088\13\uffff\1\u0088" "\37\uffff\1\u0088"
        ),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\2\u00b2\1\uffff\2\u00b2\22\uffff\1\u00b2"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b4\3\uffff\1\u00b3"),
        DFA.unpack("\1\u00b7\11\uffff\1\u00b6\6\uffff\1\u00b5"),
        DFA.unpack("\1\u00b8"),
        DFA.unpack("\1\u00b9"),
        DFA.unpack(""),
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
        DFA.unpack("\1\u00c6"),
        DFA.unpack("\1\u00c7"),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\1\u00c9"),
        DFA.unpack("\1\u00ca"),
        DFA.unpack("\1\133\4\uffff\1\133"),
        DFA.unpack(""),
        DFA.unpack("\1\u00cb"),
        DFA.unpack("\1\u00cc"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00cf"),
        DFA.unpack("\1\u00d0"),
        DFA.unpack("\1\u00d1"),
        DFA.unpack("\1\u00d2"),
        DFA.unpack("\1\u00d3"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u00d4\7\110"
        ),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00d8"),
        DFA.unpack("\1\u00d9"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\133\4\uffff\1\133\71\uffff\1\u00dc\15\uffff\1\u00dd"),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\1\u00df"),
        DFA.unpack("\1\133\4\uffff\1\133"),
        DFA.unpack("\1\u00e0"),
        DFA.unpack("\1\u00e1"),
        DFA.unpack("\1\u00e2"),
        DFA.unpack("\1\u00e3"),
        DFA.unpack("\1\u00e4"),
        DFA.unpack("\1\u00e5"),
        DFA.unpack("\1\u00e6\23\uffff\1\u00e7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00e9"),
        DFA.unpack("\1\u00ea"),
        DFA.unpack(""),
        DFA.unpack("\3\u00eb\35\uffff\3\u00eb"),
        DFA.unpack("\1\u00ec"),
        DFA.unpack("\1\u00ed"),
        DFA.unpack("\1\u00ee"),
        DFA.unpack("\1\u00ef"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u00f1"),
        DFA.unpack("\1\u00f2\5\uffff\1\u00f3"),
        DFA.unpack(""),
        DFA.unpack("\1\u00f4"),
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
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f6"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00f8"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00fa"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00fc"),
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
        DFA.unpack("\1\u0088\1\uffff\12\u00af\13\uffff\1\u0088\37\uffff" "\1\u0088"),
        DFA.unpack(
            "\1\u0088\1\uffff\1\u00b0\11\u0088\13\uffff\1\u0088" "\37\uffff\1\u0088"
        ),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00fe"),
        DFA.unpack("\1\u00ff\7\uffff\1\u0100"),
        DFA.unpack("\1\u0101"),
        DFA.unpack("\1\u0102"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\16\110" "\1\u0103\13\110"
        ),
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
        DFA.unpack("\1\u0111"),
        DFA.unpack("\1\u0112"),
        DFA.unpack("\1\u0113\10\uffff\1\u0114"),
        DFA.unpack("\1\u0115"),
        DFA.unpack("\1\u0116"),
        DFA.unpack("\1\u0117"),
        DFA.unpack("\1\u0118"),
        DFA.unpack("\1\u0119"),
        DFA.unpack("\1\u011a"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u011b"),
        DFA.unpack("\1\u011c"),
        DFA.unpack("\1\u011d"),
        DFA.unpack("\1\u011e"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0120"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0121"),
        DFA.unpack("\1\u0122"),
        DFA.unpack("\1\u0123"),
        DFA.unpack("\1\u0124"),
        DFA.unpack("\1\u0125"),
        DFA.unpack("\1\u0126"),
        DFA.unpack("\1\u0127"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0129"),
        DFA.unpack("\1\u012a"),
        DFA.unpack("\1\u012b"),
        DFA.unpack("\1\u012c"),
        DFA.unpack("\1\u012d"),
        DFA.unpack("\1\u012e"),
        DFA.unpack("\1\u012f"),
        DFA.unpack("\1\u0130"),
        DFA.unpack(""),
        DFA.unpack("\1\u0131"),
        DFA.unpack("\1\u0132"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0134"),
        DFA.unpack("\1\u0135"),
        DFA.unpack("\1\u0136"),
        DFA.unpack("\1\u0137"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0139"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
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
        DFA.unpack("\1\u013b"),
        DFA.unpack("\1\u013c"),
        DFA.unpack("\1\u013d"),
        DFA.unpack("\1\u013e"),
        DFA.unpack("\1\u013f"),
        DFA.unpack("\1\u0140"),
        DFA.unpack(""),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0143"),
        DFA.unpack("\1\u0144"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0146"),
        DFA.unpack("\1\u0147"),
        DFA.unpack("\1\u0148"),
        DFA.unpack("\1\u0149"),
        DFA.unpack("\1\u014a"),
        DFA.unpack("\1\u014b"),
        DFA.unpack("\1\u014c"),
        DFA.unpack("\1\u014d"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u014f"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0151"),
        DFA.unpack("\1\u0152"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0153"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0155"),
        DFA.unpack("\1\u0156"),
        DFA.unpack("\1\u0157"),
        DFA.unpack("\1\u0158"),
        DFA.unpack(""),
        DFA.unpack("\1\u0159"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u015b"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u015d"),
        DFA.unpack("\1\u015e"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0160"),
        DFA.unpack(""),
        DFA.unpack("\1\u0161"),
        DFA.unpack("\1\u0162"),
        DFA.unpack("\1\u0163"),
        DFA.unpack("\1\u0164"),
        DFA.unpack("\1\u0165"),
        DFA.unpack("\1\u0166"),
        DFA.unpack("\1\u0167"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0169"),
        DFA.unpack("\1\u016a"),
        DFA.unpack(""),
        DFA.unpack("\1\u016b"),
        DFA.unpack("\1\u016c"),
        DFA.unpack("\1\u016d"),
        DFA.unpack("\1\u016e"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u0170"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0172"),
        DFA.unpack("\1\u0173"),
        DFA.unpack("\1\u0174"),
        DFA.unpack("\1\u0175"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u0177"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\1\u0178"),
        DFA.unpack("\1\u0179"),
        DFA.unpack("\1\u017a"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u017b"),
        DFA.unpack("\1\u017c"),
        DFA.unpack("\1\u017d"),
        DFA.unpack("\1\u017e"),
        DFA.unpack(""),
        DFA.unpack("\1\u017f"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0181"),
        DFA.unpack("\1\u0182"),
        DFA.unpack(""),
        DFA.unpack("\1\u0183"),
        DFA.unpack("\1\u0184"),
        DFA.unpack("\1\u0185"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u0187"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u018a\7\110"
        ),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u018f"),
        DFA.unpack("\1\u0190"),
        DFA.unpack("\1\u0191"),
        DFA.unpack("\1\u0192"),
        DFA.unpack("\1\u0193"),
        DFA.unpack(""),
        DFA.unpack("\1\u0194"),
        DFA.unpack("\1\u0195"),
        DFA.unpack("\1\u0196"),
        DFA.unpack("\1\u0197"),
        DFA.unpack("\1\u0198"),
        DFA.unpack("\1\u0199"),
        DFA.unpack(""),
        DFA.unpack("\1\u019a"),
        DFA.unpack(""),
        DFA.unpack("\1\u019b"),
        DFA.unpack("\1\u019c"),
        DFA.unpack("\1\u019d"),
        DFA.unpack(
            "\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\22\110" "\1\u019e\7\110"
        ),
        DFA.unpack(""),
        DFA.unpack("\1\u019f"),
        DFA.unpack("\1\u01a0"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01a3"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01a5"),
        DFA.unpack("\1\u01a6"),
        DFA.unpack(""),
        DFA.unpack("\1\u01a7"),
        DFA.unpack("\1\u01a8"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01aa"),
        DFA.unpack("\1\u01ab"),
        DFA.unpack(""),
        DFA.unpack("\1\u01ac"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01ad"),
        DFA.unpack("\1\u01ae"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\u01af\1\uffff\32\110"),
        DFA.unpack("\1\u01b1"),
        DFA.unpack("\1\u01b2"),
        DFA.unpack("\1\u01b3"),
        DFA.unpack("\1\u01b4"),
        DFA.unpack("\1\u01b5"),
        DFA.unpack("\1\u01b6"),
        DFA.unpack("\1\u01b7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01b9"),
        DFA.unpack("\1\u01ba"),
        DFA.unpack("\1\u01bb"),
        DFA.unpack("\1\u01bc"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01be"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01bf"),
        DFA.unpack(""),
        DFA.unpack("\1\u01c0"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01c1"),
        DFA.unpack("\1\u01c2"),
        DFA.unpack(""),
        DFA.unpack("\1\u01c3"),
        DFA.unpack("\1\u01c4"),
        DFA.unpack("\1\u01c5"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01c7"),
        DFA.unpack("\1\u01c8"),
        DFA.unpack(""),
        DFA.unpack("\1\u01c9"),
        DFA.unpack("\1\u01ca"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01cd"),
        DFA.unpack("\1\u01ce"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d1\1\u01d2"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d4"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01d9"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01db"),
        DFA.unpack(""),
        DFA.unpack("\1\u01dc"),
        DFA.unpack("\1\u01dd"),
        DFA.unpack("\1\u01de"),
        DFA.unpack("\1\u01df"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01e0"),
        DFA.unpack("\1\u01e1"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01e2"),
        DFA.unpack("\1\u01e3"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01e5"),
        DFA.unpack(""),
        DFA.unpack("\1\u01e6"),
        DFA.unpack(""),
        DFA.unpack("\1\u01e7"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01e9"),
        DFA.unpack("\1\u01ea"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01ec"),
        DFA.unpack("\1\u01ed"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01f0"),
        DFA.unpack("\1\u01f1"),
        DFA.unpack(""),
        DFA.unpack("\1\u01f2"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01f3"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01f4"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01f6"),
        DFA.unpack("\1\u01f7"),
        DFA.unpack("\1\u01f8"),
        DFA.unpack(""),
        DFA.unpack("\1\u01f9"),
        DFA.unpack("\1\u01fa"),
        DFA.unpack("\1\u01fb"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\1\u01fd"),
        DFA.unpack("\1\u01fe"),
        DFA.unpack(""),
        DFA.unpack("\1\u01ff"),
        DFA.unpack("\1\u0200"),
        DFA.unpack("\1\u0201"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack("\12\110\7\uffff\32\110\4\uffff\1\110\1\uffff\32\110"),
        DFA.unpack(""),
    ]

    # class definition for DFA #42

    class DFA42(DFA):
        pass

        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self_.recognizer

            _s = s

            if s == 0:
                LA42_0 = input.LA(1)

                s = -1
                if LA42_0 == 115:
                    s = 1

                elif LA42_0 == 119:
                    s = 2

                elif LA42_0 == 80:
                    s = 3

                elif LA42_0 == 67:
                    s = 4

                elif LA42_0 == 84:
                    s = 5

                elif LA42_0 == 83:
                    s = 6

                elif LA42_0 == 68:
                    s = 7

                elif LA42_0 == 76:
                    s = 8

                elif LA42_0 == 82:
                    s = 9

                elif LA42_0 == 77:
                    s = 10

                elif LA42_0 == 111:
                    s = 11

                elif LA42_0 == 99:
                    s = 12

                elif LA42_0 == 103:
                    s = 13

                elif LA42_0 == 105:
                    s = 14

                elif LA42_0 == 101:
                    s = 15

                elif LA42_0 == 102:
                    s = 16

                elif LA42_0 == 109:
                    s = 17

                elif LA42_0 == 108:
                    s = 18

                elif LA42_0 == 114:
                    s = 19

                elif LA42_0 == 116:
                    s = 20

                elif LA42_0 == 118:
                    s = 21

                elif LA42_0 == 117:
                    s = 22

                elif (88 <= LA42_0 <= 90) or (120 <= LA42_0 <= 122):
                    s = 23

                elif LA42_0 == 107:
                    s = 24

                elif LA42_0 == 112:
                    s = 25

                elif LA42_0 == 85:
                    s = 26

                elif LA42_0 == 78:
                    s = 27

                elif LA42_0 == 123:
                    s = 28

                elif LA42_0 == 97:
                    s = 29

                elif LA42_0 == 110:
                    s = 30

                elif LA42_0 == 95:
                    s = 31

                elif LA42_0 == 46:
                    s = 32

                elif LA42_0 == 44:
                    s = 33

                elif LA42_0 == 58:
                    s = 34

                elif LA42_0 == 59:
                    s = 35

                elif LA42_0 == 61:
                    s = 36

                elif LA42_0 == 124:
                    s = 37

                elif LA42_0 == 94:
                    s = 38

                elif LA42_0 == 38:
                    s = 39

                elif LA42_0 == 126:
                    s = 40

                elif LA42_0 == 60:
                    s = 41

                elif LA42_0 == 62:
                    s = 42

                elif LA42_0 == 43:
                    s = 43

                elif LA42_0 == 45:
                    s = 44

                elif LA42_0 == 42:
                    s = 45

                elif LA42_0 == 47:
                    s = 46

                elif LA42_0 == 37:
                    s = 47

                elif LA42_0 == 40:
                    s = 48

                elif LA42_0 == 41:
                    s = 49

                elif LA42_0 == 91:
                    s = 50

                elif LA42_0 == 93:
                    s = 51

                elif LA42_0 == 125:
                    s = 52

                elif LA42_0 == 33:
                    s = 53

                elif LA42_0 == 70:
                    s = 54

                elif LA42_0 == 36:
                    s = 55

                elif (
                    (65 <= LA42_0 <= 66)
                    or LA42_0 == 69
                    or (71 <= LA42_0 <= 75)
                    or LA42_0 == 79
                    or LA42_0 == 81
                    or (86 <= LA42_0 <= 87)
                    or LA42_0 == 98
                    or LA42_0 == 100
                    or LA42_0 == 104
                    or LA42_0 == 106
                    or LA42_0 == 113
                ):
                    s = 56

                elif LA42_0 == 39:
                    s = 57

                elif LA42_0 == 34:
                    s = 58

                elif 49 <= LA42_0 <= 57:
                    s = 59

                elif LA42_0 == 48:
                    s = 60

                elif LA42_0 == 13:
                    s = 61

                elif LA42_0 == 10:
                    s = 62

                elif LA42_0 == 12:
                    s = 63

                elif LA42_0 == 9 or LA42_0 == 32:
                    s = 64

                elif LA42_0 == 35:
                    s = 65

                elif LA42_0 == 92:
                    s = 66

                elif (
                    (0 <= LA42_0 <= 8)
                    or LA42_0 == 11
                    or (14 <= LA42_0 <= 31)
                    or (63 <= LA42_0 <= 64)
                    or LA42_0 == 96
                    or (127 <= LA42_0 <= 65535)
                ):
                    s = 67

                if s >= 0:
                    return s
            elif s == 1:
                LA42_57 = input.LA(1)

                s = -1
                if (0 <= LA42_57 <= 9) or LA42_57 == 11 or (14 <= LA42_57 <= 65535):
                    s = 91

                else:
                    s = 67

                if s >= 0:
                    return s
            elif s == 2:
                LA42_58 = input.LA(1)

                s = -1
                if (0 <= LA42_58 <= 9) or LA42_58 == 11 or (14 <= LA42_58 <= 65535):
                    s = 91

                else:
                    s = 67

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 42, _s, input)
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
