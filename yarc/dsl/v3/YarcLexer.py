# $ANTLR 3.5.1 C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g 2023-04-26 00:01:59

import sys

from antlr3 import *
from antlr3.compat import frozenset, set

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


class YarcLexer(YarcLexerBase):
    grammarFileName = "C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa17 = self.DFA17(
            self,
            17,
            eot=self.DFA17_eot,
            eof=self.DFA17_eof,
            min=self.DFA17_min,
            max=self.DFA17_max,
            accept=self.DFA17_accept,
            special=self.DFA17_special,
            transition=self.DFA17_transition,
        )

        self.dfa27 = self.DFA27(
            self,
            27,
            eot=self.DFA27_eot,
            eof=self.DFA27_eof,
            min=self.DFA27_min,
            max=self.DFA27_max,
            accept=self.DFA27_accept,
            special=self.DFA27_special,
            transition=self.DFA27_transition,
        )

        self.dfa28 = self.DFA28(
            self,
            28,
            eot=self.DFA28_eot,
            eof=self.DFA28_eof,
            min=self.DFA28_min,
            max=self.DFA28_max,
            accept=self.DFA28_accept,
            special=self.DFA28_special,
            transition=self.DFA28_transition,
        )

        self.dfa38 = self.DFA38(
            self,
            38,
            eot=self.DFA38_eot,
            eof=self.DFA38_eof,
            min=self.DFA38_min,
            max=self.DFA38_max,
            accept=self.DFA38_accept,
            special=self.DFA38_special,
            transition=self.DFA38_transition,
        )

    # $ANTLR start "SCENARIO"
    def mSCENARIO(
        self,
    ):
        try:
            _type = SCENARIO
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:22:10: ( 'scenario' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:22:12: 'scenario'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:23:10: ( 'settings' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:23:12: 'settings'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:24:10: ( 'stage' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:24:12: 'stage'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:25:10: ( 'writers' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:25:12: 'writers'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:28:10: ( 'plane' | 'cube' | 'sphere' | 'cylinder' | 'cone' | 'torus' | 'disk' )
            alt1 = 7
            LA1 = self.input.LA(1)
            if LA1 == 112:
                alt1 = 1
            elif LA1 == 99:
                LA1 = self.input.LA(2)
                if LA1 == 117:
                    alt1 = 2
                elif LA1 == 121:
                    alt1 = 4
                elif LA1 == 111:
                    alt1 = 5
                else:
                    nvae = NoViableAltException("", 1, 2, self.input)

                    raise nvae

            elif LA1 == 115:
                alt1 = 3
            elif LA1 == 116:
                alt1 = 6
            elif LA1 == 100:
                alt1 = 7
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae

            if alt1 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:28:12: 'plane'
                pass
                self.match("plane")

            elif alt1 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:28:22: 'cube'
                pass
                self.match("cube")

            elif alt1 == 3:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:28:31: 'sphere'
                pass
                self.match("sphere")

            elif alt1 == 4:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:28:42: 'cylinder'
                pass
                self.match("cylinder")

            elif alt1 == 5:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:28:55: 'cone'
                pass
                self.match("cone")

            elif alt1 == 6:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:28:64: 'torus'
                pass
                self.match("torus")

            elif alt1 == 7:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:28:74: 'disk'
                pass
                self.match("disk")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SHAPES"

    # $ANTLR start "CAMERA"
    def mCAMERA(
        self,
    ):
        try:
            _type = CAMERA
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:29:10: ( 'camera' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:29:12: 'camera'
            pass
            self.match("camera")

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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:30:10: ( 'light' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:30:12: 'light'
            pass
            self.match("light")

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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:31:10: ( 'stereo' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:31:12: 'stereo'
            pass
            self.match("stereo")

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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:32:10: ( 'material' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:32:12: 'material'
            pass
            self.match("material")

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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:33:10: ( 'timeline' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:33:12: 'timeline'
            pass
            self.match("timeline")

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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:36:13: ( 'open' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:36:15: 'open'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:37:13: ( 'create' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:37:15: 'create'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:38:13: ( 'group' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:38:15: 'group'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:39:13: ( 'instantiate' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:39:15: 'instantiate'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:40:13: ( 'get' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:40:15: 'get'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:41:13: ( 'edit' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:41:15: 'edit'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:44:7: ( 'fetch' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:44:9: 'fetch'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:45:7: ( 'match' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:45:9: 'match'
            pass
            self.match("match")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MATCH"

    # $ANTLR start "TRANSLATE"
    def mTRANSLATE(
        self,
    ):
        try:
            _type = TRANSLATE
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:48:15: ( 'translate' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:48:17: 'translate'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:49:15: ( 'camera_translate' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:49:17: 'camera_translate'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:50:15: ( 'rotate' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:50:17: 'rotate'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:51:15: ( 'scale' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:51:17: 'scale'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:52:15: ( 'semantics' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:52:17: 'semantics'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:53:15: ( 'visible' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:53:17: 'visible'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:54:15: ( 'size' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:54:17: 'size'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:55:15: ( 'look_at' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:55:17: 'look_at'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:56:15: ( 'up_axis' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:56:17: 'up_axis'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:57:15: ( 'x' | 'y' | 'z' | 'X' | 'Y' | 'Z' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:58:15: ( AXIS AXIS AXIS )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:58:17: AXIS AXIS AXIS
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:61:14: ( 'scatter' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:61:16: 'scatter'
            pass
            self.match("scatter")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SCATTER"

    # $ANTLR start "SCATTER_TYPE"
    def mSCATTER_TYPE(
        self,
    ):
        try:
            _type = SCATTER_TYPE
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:62:14: ( '2d' | '3d' )
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
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:62:16: '2d'
                pass
                self.match("2d")

            elif alt2 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:62:23: '3d'
                pass
                self.match("3d")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SCATTER_TYPE"

    # $ANTLR start "AROUND"
    def mAROUND(
        self,
    ):
        try:
            _type = AROUND
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:63:14: ( 'around' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:63:16: 'around'
            pass
            self.match("around")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AROUND"

    # $ANTLR start "TEXTURE"
    def mTEXTURE(
        self,
    ):
        try:
            _type = TEXTURE
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:64:14: ( 'texture' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:64:16: 'texture'
            pass
            self.match("texture")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TEXTURE"

    # $ANTLR start "EVERY"
    def mEVERY(
        self,
    ):
        try:
            _type = EVERY
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:67:8: ( 'every' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:67:10: 'every'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:68:8: ( 'frame' ( 's' )? )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:68:10: 'frame' ( 's' )?
            pass
            self.match("frame")

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:68:18: ( 's' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if LA3_0 == 115:
                alt3 = 1
            if alt3 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:68:18: 's'
                pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:69:8: ( 'sec' ( 'ond' ( 's' )? )? )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:69:10: 'sec' ( 'ond' ( 's' )? )?
            pass
            self.match("sec")

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:69:16: ( 'ond' ( 's' )? )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if LA5_0 == 111:
                alt5 = 1
            if alt5 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:69:17: 'ond' ( 's' )?
                pass
                self.match("ond")

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:69:23: ( 's' )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if LA4_0 == 115:
                    alt4 = 1
                if alt4 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:69:23: 's'
                    pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:72:13: ( 'Uniform' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:72:15: 'Uniform'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:73:13: ( 'Normal' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:73:15: 'Normal'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:74:13: ( 'Choice' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:74:15: 'Choice'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:75:13: ( 'Sequence' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:75:15: 'Sequence'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:76:13: ( 'LogUniform' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:76:15: 'LogUniform'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:79:9: ( NESTED_CODE )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:79:11: NESTED_CODE
            pass
            self.mNESTED_CODE()

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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:81:21: ( LBRACE LBRACE ( options {k=2; greedy=false; } : NESTED_CODE | . )* RBRACE RBRACE )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:82:3: LBRACE LBRACE ( options {k=2; greedy=false; } : NESTED_CODE | . )* RBRACE RBRACE
            pass
            self.mLBRACE()

            self.mLBRACE()

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:83:5: ( options {k=2; greedy=false; } : NESTED_CODE | . )*
            while True:  # loop6
                alt6 = 3
                LA6_0 = self.input.LA(1)

                if LA6_0 == 125:
                    alt6 = 3
                elif LA6_0 == 123:
                    alt6 = 1
                elif (0 <= LA6_0 <= 122) or LA6_0 == 124 or (126 <= LA6_0 <= 65535):
                    alt6 = 2

                if alt6 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:83:37: NESTED_CODE
                    pass
                    self.mNESTED_CODE()

                elif alt6 == 2:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:83:51: .
                    pass
                    self.matchAny()

                else:
                    break  # loop6

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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:88:4: ( 'to' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:88:6: 'to'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:89:4: ( 'on' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:89:6: 'on'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:90:4: ( 'at' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:90:6: 'at'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:97:12: ( 'and' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:97:14: 'and'
            pass
            self.match("and")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND"

    # $ANTLR start "DEF"
    def mDEF(
        self,
    ):
        try:
            _type = DEF
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:98:12: ( 'def' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:98:14: 'def'
            pass
            self.match("def")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEF"

    # $ANTLR start "ELSE"
    def mELSE(
        self,
    ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:99:12: ( 'else' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:99:14: 'else'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:100:12: ( 'false' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:100:14: 'false'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:101:12: ( 'for' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:101:14: 'for'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:102:12: ( 'from' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:102:14: 'from'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:103:12: ( 'if' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:103:14: 'if'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:104:12: ( 'in' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:104:14: 'in'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:105:12: ( 'is' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:105:14: 'is'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:106:12: ( 'none' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:106:14: 'none'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:107:12: ( 'not' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:107:14: 'not'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:108:12: ( 'or' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:108:14: 'or'
            pass
            self.match("or")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"

    # $ANTLR start "RETURN"
    def mRETURN(
        self,
    ):
        try:
            _type = RETURN
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:109:12: ( 'return' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:109:14: 'return'
            pass
            self.match("return")

            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RETURN"

    # $ANTLR start "TRUE"
    def mTRUE(
        self,
    ):
        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:110:12: ( 'true' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:110:14: 'true'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:111:12: ( '_' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:111:14: '_'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:114:10: ( '.' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:114:12: '.'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:115:10: ( '..' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:115:12: '..'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:116:10: ( '...' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:116:12: '...'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:117:10: ( ',' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:117:12: ','
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:118:10: ( ':' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:118:12: ':'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:119:10: ( ';' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:119:12: ';'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:121:9: ( '=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:121:11: '='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:122:9: ( '|' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:122:11: '|'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:123:9: ( '^' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:123:11: '^'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:124:9: ( '&' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:124:11: '&'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:125:9: ( '~' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:125:11: '~'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:126:9: ( '<<' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:126:11: '<<'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:127:9: ( '>>' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:127:11: '>>'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:128:9: ( '+' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:128:11: '+'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:129:9: ( '-' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:129:11: '-'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:130:8: ( '*' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:130:10: '*'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:131:9: ( '/' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:131:11: '/'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:132:9: ( '%' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:132:11: '%'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:133:9: ( '//' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:133:11: '//'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:134:9: ( '**' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:134:11: '**'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:136:8: ( '(' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:136:10: '('
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:137:8: ( ')' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:137:10: ')'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:138:8: ( '[' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:138:10: '['
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:139:8: ( ']' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:139:10: ']'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:140:8: ( '{' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:140:10: '{'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:141:8: ( '}' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:141:10: '}'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:143:8: ( '<' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:143:10: '<'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:144:8: ( '>' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:144:10: '>'
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:145:8: ( '==' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:145:10: '=='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:146:8: ( '>=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:146:10: '>='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:147:8: ( '<=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:147:10: '<='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:148:8: ( '!=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:148:10: '!='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:150:15: ( '+=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:150:17: '+='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:151:15: ( '-=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:151:17: '-='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:152:15: ( '*=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:152:17: '*='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:153:15: ( '/=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:153:17: '/='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:154:15: ( '%=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:154:17: '%='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:155:15: ( '&=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:155:17: '&='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:156:15: ( '|=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:156:17: '|='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:157:15: ( '^=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:157:17: '^='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:158:15: ( '<<=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:158:17: '<<='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:159:15: ( '>>=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:159:17: '>>='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:160:15: ( '**=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:160:17: '**='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:161:15: ( '//=' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:161:17: '//='
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:164:12: ( ID_START ( ID_CONTINUE )* )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:164:14: ID_START ( ID_CONTINUE )*
            pass
            self.mID_START()

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:164:23: ( ID_CONTINUE )*
            while True:  # loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (
                    (48 <= LA7_0 <= 57)
                    or (65 <= LA7_0 <= 90)
                    or LA7_0 == 95
                    or (97 <= LA7_0 <= 122)
                ):
                    alt7 = 1

                if alt7 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                    pass
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
                    break  # loop7

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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:165:12: ( '$' ID )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:165:14: '$' ID
            pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:168:7: ( ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:169:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )? SHORT_STRING
            pass
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:169:3: ( ( 'u' | 'U' ) | ( ( 'f' | 'F' )? ( 'r' | 'R' ) ) | ( ( 'r' | 'R' )? ( 'f' | 'F' ) ) )?
            alt10 = 4
            LA10 = self.input.LA(1)
            if LA10 == 85 or LA10 == 117:
                alt10 = 1
            elif LA10 == 70 or LA10 == 102:
                LA10_2 = self.input.LA(2)

                if LA10_2 == 82 or LA10_2 == 114:
                    alt10 = 2
                elif LA10_2 == 34 or LA10_2 == 39:
                    alt10 = 3
            elif LA10 == 82 or LA10 == 114:
                LA10_3 = self.input.LA(2)

                if LA10_3 == 34 or LA10_3 == 39:
                    alt10 = 2
                elif LA10_3 == 70 or LA10_3 == 102:
                    alt10 = 3
            if alt10 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:169:5: ( 'u' | 'U' )
                pass
                if self.input.LA(1) == 85 or self.input.LA(1) == 117:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            elif alt10 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:170:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:170:5: ( ( 'f' | 'F' )? ( 'r' | 'R' ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:170:7: ( 'f' | 'F' )? ( 'r' | 'R' )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:170:7: ( 'f' | 'F' )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if LA8_0 == 70 or LA8_0 == 102:
                    alt8 = 1
                if alt8 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                    pass
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

            elif alt10 == 3:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:171:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:171:5: ( ( 'r' | 'R' )? ( 'f' | 'F' ) )
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:171:7: ( 'r' | 'R' )? ( 'f' | 'F' )
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:171:7: ( 'r' | 'R' )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if LA9_0 == 82 or LA9_0 == 114:
                    alt9 = 1
                if alt9 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                    pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:176:9: ( NON_ZERO_DIGIT ( DIGIT )* | ( '0' )+ | '0' ( 'o' | 'O' ) ( OCT_DIGIT )+ | '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ | '0' ( 'b' | 'B' ) ( BIN_DIGIT )+ )
            alt16 = 5
            LA16_0 = self.input.LA(1)

            if 49 <= LA16_0 <= 57:
                alt16 = 1
            elif LA16_0 == 48:
                LA16 = self.input.LA(2)
                if LA16 == 79 or LA16 == 111:
                    alt16 = 3
                elif LA16 == 88 or LA16 == 120:
                    alt16 = 4
                elif LA16 == 66 or LA16 == 98:
                    alt16 = 5
                else:
                    alt16 = 2

            else:
                nvae = NoViableAltException("", 16, 0, self.input)

                raise nvae

            if alt16 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:177:3: NON_ZERO_DIGIT ( DIGIT )*
                pass
                self.mNON_ZERO_DIGIT()

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:177:18: ( DIGIT )*
                while True:  # loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if 48 <= LA11_0 <= 57:
                        alt11 = 1

                    if alt11 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                        pass
                        if 48 <= self.input.LA(1) <= 57:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        break  # loop11

            elif alt16 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:177:27: ( '0' )+
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:177:27: ( '0' )+
                cnt12 = 0
                while True:  # loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if LA12_0 == 48:
                        alt12 = 1

                    if alt12 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:177:27: '0'
                        pass
                        self.match(48)

                    else:
                        if cnt12 >= 1:
                            break  # loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1

            elif alt16 == 3:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:178:5: '0' ( 'o' | 'O' ) ( OCT_DIGIT )+
                pass
                self.match(48)

                if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:178:21: ( OCT_DIGIT )+
                cnt13 = 0
                while True:  # loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if 48 <= LA13_0 <= 55:
                        alt13 = 1

                    if alt13 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                        pass
                        if 48 <= self.input.LA(1) <= 55:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        if cnt13 >= 1:
                            break  # loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1

            elif alt16 == 4:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:179:5: '0' ( 'x' | 'X' ) ( HEX_DIGIT )+
                pass
                self.match(48)

                if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:179:21: ( HEX_DIGIT )+
                cnt14 = 0
                while True:  # loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (
                        (48 <= LA14_0 <= 57)
                        or (65 <= LA14_0 <= 70)
                        or (97 <= LA14_0 <= 102)
                    ):
                        alt14 = 1

                    if alt14 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                        pass
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
                        if cnt14 >= 1:
                            break  # loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1

            elif alt16 == 5:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:180:5: '0' ( 'b' | 'B' ) ( BIN_DIGIT )+
                pass
                self.match(48)

                if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:180:21: ( BIN_DIGIT )+
                cnt15 = 0
                while True:  # loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if 48 <= LA15_0 <= 49:
                        alt15 = 1

                    if alt15 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                        pass
                        if 48 <= self.input.LA(1) <= 49:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse

                    else:
                        if cnt15 >= 1:
                            break  # loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1

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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:183:14: ( POINT_FLOAT | EXPONENT_FLOAT )
            alt17 = 2
            alt17 = self.dfa17.predict(self.input)
            if alt17 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:183:16: POINT_FLOAT
                pass
                self.mPOINT_FLOAT()

            elif alt17 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:183:30: EXPONENT_FLOAT
                pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:186:8: ( ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? ) )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:187:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            pass
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:187:3: ( ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )? )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) ( SPACES )?
            pass
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:3: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt19 = 3
            LA19 = self.input.LA(1)
            if LA19 == 13:
                LA19_1 = self.input.LA(2)

                if LA19_1 == 10:
                    alt19 = 1
                else:
                    alt19 = 2

            elif LA19 == 10:
                alt19 = 1
            elif LA19 == 12:
                alt19 = 3
            else:
                nvae = NoViableAltException("", 19, 0, self.input)

                raise nvae

            if alt19 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:5: ( '\\r' )? '\\n'
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:5: ( '\\r' )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if LA18_0 == 13:
                    alt18 = 1
                if alt18 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:5: '\\r'
                    pass
                    self.match(13)

                self.match(10)

            elif alt19 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:18: '\\r'
                pass
                self.match(13)

            elif alt19 == 3:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:25: '\\f'
                pass
                self.match(12)

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:31: ( SPACES )?
            alt20 = 2
            LA20_0 = self.input.LA(1)

            if LA20_0 == 9 or LA20_0 == 32:
                alt20 = 1
            if alt20 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:188:31: SPACES
                pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:193:9: ( ( SPACES | COMMENT | LINE_JOINING ) )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:193:11: ( SPACES | COMMENT | LINE_JOINING )
            pass
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:193:11: ( SPACES | COMMENT | LINE_JOINING )
            alt21 = 3
            LA21 = self.input.LA(1)
            if LA21 == 9 or LA21 == 32:
                alt21 = 1
            elif LA21 == 35:
                alt21 = 2
            elif LA21 == 92:
                alt21 = 3
            else:
                nvae = NoViableAltException("", 21, 0, self.input)

                raise nvae

            if alt21 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:193:13: SPACES
                pass
                self.mSPACES()

            elif alt21 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:193:22: COMMENT
                pass
                self.mCOMMENT()

            elif alt21 == 3:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:193:32: LINE_JOINING
                pass
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

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:194:9: ( . )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:194:11: .
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:197:22: ( '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\'' | '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"' )
            alt24 = 2
            LA24_0 = self.input.LA(1)

            if LA24_0 == 39:
                alt24 = 1
            elif LA24_0 == 34:
                alt24 = 2
            else:
                nvae = NoViableAltException("", 24, 0, self.input)

                raise nvae

            if alt24 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:198:3: '\\'' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )* '\\''
                pass
                self.match(39)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:198:8: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' ) )*
                while True:  # loop22
                    alt22 = 3
                    LA22_0 = self.input.LA(1)

                    if LA22_0 == 92:
                        alt22 = 1
                    elif (
                        (0 <= LA22_0 <= 9)
                        or LA22_0 == 11
                        or (14 <= LA22_0 <= 38)
                        or (40 <= LA22_0 <= 91)
                        or (93 <= LA22_0 <= 65535)
                    ):
                        alt22 = 2

                    if alt22 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:198:9: STRING_ESCAPE_SEQ
                        pass
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt22 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:198:29: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\\'' )
                        pass
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
                        break  # loop22

                self.match(39)

            elif alt24 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:199:5: '\"' ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )* '\"'
                pass
                self.match(34)

                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:199:9: ( STRING_ESCAPE_SEQ |~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' ) )*
                while True:  # loop23
                    alt23 = 3
                    LA23_0 = self.input.LA(1)

                    if LA23_0 == 92:
                        alt23 = 1
                    elif (
                        (0 <= LA23_0 <= 9)
                        or LA23_0 == 11
                        or (14 <= LA23_0 <= 33)
                        or (35 <= LA23_0 <= 91)
                        or (93 <= LA23_0 <= 65535)
                    ):
                        alt23 = 2

                    if alt23 == 1:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:199:10: STRING_ESCAPE_SEQ
                        pass
                        self.mSTRING_ESCAPE_SEQ()

                    elif alt23 == 2:
                        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:199:30: ~ ( '\\\\' | '\\r' | '\\n' | '\\f' | '\"' )
                        pass
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
                        break  # loop23

                self.match(34)

        finally:
            pass

    # $ANTLR end "SHORT_STRING"

    # $ANTLR start "STRING_ESCAPE_SEQ"
    def mSTRING_ESCAPE_SEQ(
        self,
    ):
        try:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:201:28: ( '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' ) | '\\\\' NEWLINE )
            alt25 = 2
            LA25_0 = self.input.LA(1)

            if LA25_0 == 92:
                LA25_1 = self.input.LA(2)

                if (
                    (0 <= LA25_1 <= 8)
                    or LA25_1 == 11
                    or (14 <= LA25_1 <= 31)
                    or (33 <= LA25_1 <= 65535)
                ):
                    alt25 = 1
                elif LA25_1 == 10 or (12 <= LA25_1 <= 13):
                    alt25 = 2
                else:
                    nvae = NoViableAltException("", 25, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 25, 0, self.input)

                raise nvae

            if alt25 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:201:30: '\\\\' ~ ( '\\t' | ' ' | '\\r' | '\\n' | '\\f' )
                pass
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

            elif alt25 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:201:72: '\\\\' NEWLINE
                pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:203:25: ( '1' .. '9' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:204:25: ( '0' .. '9' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:205:25: ( '0' .. '7' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:206:25: ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:207:25: ( '0' | '1' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:209:25: ( ( INT_PART )? FRACTION | INT_PART '.' )
            alt27 = 2
            alt27 = self.dfa27.predict(self.input)
            if alt27 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:209:27: ( INT_PART )? FRACTION
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:209:27: ( INT_PART )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if 48 <= LA26_0 <= 57:
                    alt26 = 1
                if alt26 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:209:27: INT_PART
                    pass
                    self.mINT_PART()

                self.mFRACTION()

            elif alt27 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:209:48: INT_PART '.'
                pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:210:25: ( ( INT_PART | POINT_FLOAT ) EXPONENT )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:210:27: ( INT_PART | POINT_FLOAT ) EXPONENT
            pass
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:210:27: ( INT_PART | POINT_FLOAT )
            alt28 = 2
            alt28 = self.dfa28.predict(self.input)
            if alt28 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:210:29: INT_PART
                pass
                self.mINT_PART()

            elif alt28 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:210:40: POINT_FLOAT
                pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:211:25: ( ( DIGIT )+ )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:211:27: ( DIGIT )+
            pass
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:211:27: ( DIGIT )+
            cnt29 = 0
            while True:  # loop29
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if 48 <= LA29_0 <= 57:
                    alt29 = 1

                if alt29 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                    pass
                    if 48 <= self.input.LA(1) <= 57:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt29 >= 1:
                        break  # loop29

                    eee = EarlyExitException(29, self.input)
                    raise eee

                cnt29 += 1

        finally:
            pass

    # $ANTLR end "INT_PART"

    # $ANTLR start "FRACTION"
    def mFRACTION(
        self,
    ):
        try:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:212:25: ( '.' ( DIGIT )+ )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:212:27: '.' ( DIGIT )+
            pass
            self.match(46)

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:212:31: ( DIGIT )+
            cnt30 = 0
            while True:  # loop30
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if 48 <= LA30_0 <= 57:
                    alt30 = 1

                if alt30 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                    pass
                    if 48 <= self.input.LA(1) <= 57:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                else:
                    if cnt30 >= 1:
                        break  # loop30

                    eee = EarlyExitException(30, self.input)
                    raise eee

                cnt30 += 1

        finally:
            pass

    # $ANTLR end "FRACTION"

    # $ANTLR start "EXPONENT"
    def mEXPONENT(
        self,
    ):
        try:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:213:25: ( ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+ )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:213:27: ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+
            pass
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:213:39: ( '+' | '-' )?
            alt31 = 2
            LA31_0 = self.input.LA(1)

            if LA31_0 == 43 or LA31_0 == 45:
                alt31 = 1
            if alt31 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                pass
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:213:52: ( DIGIT )+
            cnt32 = 0
            while True:  # loop32
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if 48 <= LA32_0 <= 57:
                    alt32 = 1

                if alt32 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                    pass
                    if 48 <= self.input.LA(1) <= 57:
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

    # $ANTLR end "EXPONENT"

    # $ANTLR start "ID_START"
    def mID_START(
        self,
    ):
        try:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:215:22: ( UNDERSCORE | LETTER )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:216:22: ( ID_START | DIGIT )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:217:22: ( 'a' .. 'z' | 'A' .. 'Z' )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
            pass
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
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:219:23: ( ( ' ' | '\\t' )+ )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:219:25: ( ' ' | '\\t' )+
            pass
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:219:25: ( ' ' | '\\t' )+
            cnt33 = 0
            while True:  # loop33
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if LA33_0 == 9 or LA33_0 == 32:
                    alt33 = 1

                if alt33 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                    pass
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
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

    # $ANTLR end "SPACES"

    # $ANTLR start "COMMENT"
    def mCOMMENT(
        self,
    ):
        try:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:220:23: ( '#' (~ ( '\\r' | '\\n' | '\\f' ) )* )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:220:25: '#' (~ ( '\\r' | '\\n' | '\\f' ) )*
            pass
            self.match(35)

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:220:29: (~ ( '\\r' | '\\n' | '\\f' ) )*
            while True:  # loop34
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (0 <= LA34_0 <= 9) or LA34_0 == 11 or (14 <= LA34_0 <= 65535):
                    alt34 = 1

                if alt34 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:
                    pass
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
                    break  # loop34

        finally:
            pass

    # $ANTLR end "COMMENT"

    # $ANTLR start "LINE_JOINING"
    def mLINE_JOINING(
        self,
    ):
        try:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:23: ( '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' ) )
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:25: '\\\\' ( SPACES )? ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            pass
            self.match(92)

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:30: ( SPACES )?
            alt35 = 2
            LA35_0 = self.input.LA(1)

            if LA35_0 == 9 or LA35_0 == 32:
                alt35 = 1
            if alt35 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:30: SPACES
                pass
                self.mSPACES()

            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:38: ( ( '\\r' )? '\\n' | '\\r' | '\\f' )
            alt37 = 3
            LA37 = self.input.LA(1)
            if LA37 == 13:
                LA37_1 = self.input.LA(2)

                if LA37_1 == 10:
                    alt37 = 1
                else:
                    alt37 = 2

            elif LA37 == 10:
                alt37 = 1
            elif LA37 == 12:
                alt37 = 3
            else:
                nvae = NoViableAltException("", 37, 0, self.input)

                raise nvae

            if alt37 == 1:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:40: ( '\\r' )? '\\n'
                pass
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:40: ( '\\r' )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if LA36_0 == 13:
                    alt36 = 1
                if alt36 == 1:
                    # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:40: '\\r'
                    pass
                    self.match(13)

                self.match(10)

            elif alt37 == 2:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:53: '\\r'
                pass
                self.match(13)

            elif alt37 == 3:
                # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:221:60: '\\f'
                pass
                self.match(12)

        finally:
            pass

    # $ANTLR end "LINE_JOINING"

    def mTokens(self):
        # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:8: ( SCENARIO | SETTINGS | STAGE | WRITERS | SHAPES | CAMERA | LIGHT | STEREO | MATERIAL | TIMELINE | OPEN | CREATE | GROUP | INSTANTIATE | GET | EDIT | FETCH | MATCH | TRANSLATE | CAM_TRANSLATE | ROTATE | SCALE | SEMANTICS | VISIBLE | SIZE | LOOK_AT | UP_AXIS | AXIS | ORDER | SCATTER | SCATTER_TYPE | AROUND | TEXTURE | EVERY | FRAMES | TIME | UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM | SNIPPET | TO | ON | AT | AND | DEF | ELSE | FALSE | FOR | FROM | IF | IN | IS | NONE | NOT | OR | RETURN | TRUE | UNDERSCORE | DOT | RANGE | ELLIPSIS | COMMA | COLON | SEMI | ASSIGN | BIT_OR | XOR | BIT_AND | BIT_NOT | LSHIFT | RSHIFT | PLUS | MINUS | MUL | DIV | MOD | IDIV | POWER | LPAREN | RPAREN | LBRACK | RBRACK | LBRACE | RBRACE | LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | ADD_ASSIGN | SUB_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN | LSHIFT_ASSIGN | RSHIFT_ASSIGN | POWER_ASSIGN | IDIV_ASSIGN | ID | SETTING_ID | STRING | INTEGER | FLOAT_NUMBER | NEWLINE | SKIP_ | UNKNOWN )
        alt38 = 112
        alt38 = self.dfa38.predict(self.input)
        if alt38 == 1:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:10: SCENARIO
            pass
            self.mSCENARIO()

        elif alt38 == 2:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:19: SETTINGS
            pass
            self.mSETTINGS()

        elif alt38 == 3:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:28: STAGE
            pass
            self.mSTAGE()

        elif alt38 == 4:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:34: WRITERS
            pass
            self.mWRITERS()

        elif alt38 == 5:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:42: SHAPES
            pass
            self.mSHAPES()

        elif alt38 == 6:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:49: CAMERA
            pass
            self.mCAMERA()

        elif alt38 == 7:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:56: LIGHT
            pass
            self.mLIGHT()

        elif alt38 == 8:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:62: STEREO
            pass
            self.mSTEREO()

        elif alt38 == 9:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:69: MATERIAL
            pass
            self.mMATERIAL()

        elif alt38 == 10:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:78: TIMELINE
            pass
            self.mTIMELINE()

        elif alt38 == 11:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:87: OPEN
            pass
            self.mOPEN()

        elif alt38 == 12:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:92: CREATE
            pass
            self.mCREATE()

        elif alt38 == 13:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:99: GROUP
            pass
            self.mGROUP()

        elif alt38 == 14:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:105: INSTANTIATE
            pass
            self.mINSTANTIATE()

        elif alt38 == 15:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:117: GET
            pass
            self.mGET()

        elif alt38 == 16:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:121: EDIT
            pass
            self.mEDIT()

        elif alt38 == 17:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:126: FETCH
            pass
            self.mFETCH()

        elif alt38 == 18:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:132: MATCH
            pass
            self.mMATCH()

        elif alt38 == 19:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:138: TRANSLATE
            pass
            self.mTRANSLATE()

        elif alt38 == 20:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:148: CAM_TRANSLATE
            pass
            self.mCAM_TRANSLATE()

        elif alt38 == 21:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:162: ROTATE
            pass
            self.mROTATE()

        elif alt38 == 22:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:169: SCALE
            pass
            self.mSCALE()

        elif alt38 == 23:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:175: SEMANTICS
            pass
            self.mSEMANTICS()

        elif alt38 == 24:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:185: VISIBLE
            pass
            self.mVISIBLE()

        elif alt38 == 25:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:193: SIZE
            pass
            self.mSIZE()

        elif alt38 == 26:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:198: LOOK_AT
            pass
            self.mLOOK_AT()

        elif alt38 == 27:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:206: UP_AXIS
            pass
            self.mUP_AXIS()

        elif alt38 == 28:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:214: AXIS
            pass
            self.mAXIS()

        elif alt38 == 29:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:219: ORDER
            pass
            self.mORDER()

        elif alt38 == 30:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:225: SCATTER
            pass
            self.mSCATTER()

        elif alt38 == 31:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:233: SCATTER_TYPE
            pass
            self.mSCATTER_TYPE()

        elif alt38 == 32:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:246: AROUND
            pass
            self.mAROUND()

        elif alt38 == 33:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:253: TEXTURE
            pass
            self.mTEXTURE()

        elif alt38 == 34:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:261: EVERY
            pass
            self.mEVERY()

        elif alt38 == 35:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:267: FRAMES
            pass
            self.mFRAMES()

        elif alt38 == 36:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:274: TIME
            pass
            self.mTIME()

        elif alt38 == 37:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:279: UNIFORM
            pass
            self.mUNIFORM()

        elif alt38 == 38:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:287: NORMAL
            pass
            self.mNORMAL()

        elif alt38 == 39:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:294: CHOICE
            pass
            self.mCHOICE()

        elif alt38 == 40:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:301: SEQUENCE
            pass
            self.mSEQUENCE()

        elif alt38 == 41:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:310: LOG_UNIFORM
            pass
            self.mLOG_UNIFORM()

        elif alt38 == 42:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:322: SNIPPET
            pass
            self.mSNIPPET()

        elif alt38 == 43:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:330: TO
            pass
            self.mTO()

        elif alt38 == 44:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:333: ON
            pass
            self.mON()

        elif alt38 == 45:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:336: AT
            pass
            self.mAT()

        elif alt38 == 46:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:339: AND
            pass
            self.mAND()

        elif alt38 == 47:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:343: DEF
            pass
            self.mDEF()

        elif alt38 == 48:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:347: ELSE
            pass
            self.mELSE()

        elif alt38 == 49:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:352: FALSE
            pass
            self.mFALSE()

        elif alt38 == 50:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:358: FOR
            pass
            self.mFOR()

        elif alt38 == 51:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:362: FROM
            pass
            self.mFROM()

        elif alt38 == 52:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:367: IF
            pass
            self.mIF()

        elif alt38 == 53:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:370: IN
            pass
            self.mIN()

        elif alt38 == 54:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:373: IS
            pass
            self.mIS()

        elif alt38 == 55:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:376: NONE
            pass
            self.mNONE()

        elif alt38 == 56:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:381: NOT
            pass
            self.mNOT()

        elif alt38 == 57:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:385: OR
            pass
            self.mOR()

        elif alt38 == 58:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:388: RETURN
            pass
            self.mRETURN()

        elif alt38 == 59:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:395: TRUE
            pass
            self.mTRUE()

        elif alt38 == 60:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:400: UNDERSCORE
            pass
            self.mUNDERSCORE()

        elif alt38 == 61:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:411: DOT
            pass
            self.mDOT()

        elif alt38 == 62:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:415: RANGE
            pass
            self.mRANGE()

        elif alt38 == 63:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:421: ELLIPSIS
            pass
            self.mELLIPSIS()

        elif alt38 == 64:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:430: COMMA
            pass
            self.mCOMMA()

        elif alt38 == 65:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:436: COLON
            pass
            self.mCOLON()

        elif alt38 == 66:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:442: SEMI
            pass
            self.mSEMI()

        elif alt38 == 67:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:447: ASSIGN
            pass
            self.mASSIGN()

        elif alt38 == 68:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:454: BIT_OR
            pass
            self.mBIT_OR()

        elif alt38 == 69:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:461: XOR
            pass
            self.mXOR()

        elif alt38 == 70:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:465: BIT_AND
            pass
            self.mBIT_AND()

        elif alt38 == 71:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:473: BIT_NOT
            pass
            self.mBIT_NOT()

        elif alt38 == 72:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:481: LSHIFT
            pass
            self.mLSHIFT()

        elif alt38 == 73:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:488: RSHIFT
            pass
            self.mRSHIFT()

        elif alt38 == 74:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:495: PLUS
            pass
            self.mPLUS()

        elif alt38 == 75:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:500: MINUS
            pass
            self.mMINUS()

        elif alt38 == 76:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:506: MUL
            pass
            self.mMUL()

        elif alt38 == 77:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:510: DIV
            pass
            self.mDIV()

        elif alt38 == 78:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:514: MOD
            pass
            self.mMOD()

        elif alt38 == 79:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:518: IDIV
            pass
            self.mIDIV()

        elif alt38 == 80:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:523: POWER
            pass
            self.mPOWER()

        elif alt38 == 81:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:529: LPAREN
            pass
            self.mLPAREN()

        elif alt38 == 82:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:536: RPAREN
            pass
            self.mRPAREN()

        elif alt38 == 83:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:543: LBRACK
            pass
            self.mLBRACK()

        elif alt38 == 84:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:550: RBRACK
            pass
            self.mRBRACK()

        elif alt38 == 85:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:557: LBRACE
            pass
            self.mLBRACE()

        elif alt38 == 86:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:564: RBRACE
            pass
            self.mRBRACE()

        elif alt38 == 87:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:571: LT
            pass
            self.mLT()

        elif alt38 == 88:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:574: GT
            pass
            self.mGT()

        elif alt38 == 89:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:577: EQUALS
            pass
            self.mEQUALS()

        elif alt38 == 90:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:584: GT_EQ
            pass
            self.mGT_EQ()

        elif alt38 == 91:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:590: LT_EQ
            pass
            self.mLT_EQ()

        elif alt38 == 92:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:596: NOT_EQ
            pass
            self.mNOT_EQ()

        elif alt38 == 93:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:603: ADD_ASSIGN
            pass
            self.mADD_ASSIGN()

        elif alt38 == 94:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:614: SUB_ASSIGN
            pass
            self.mSUB_ASSIGN()

        elif alt38 == 95:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:625: MULT_ASSIGN
            pass
            self.mMULT_ASSIGN()

        elif alt38 == 96:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:637: DIV_ASSIGN
            pass
            self.mDIV_ASSIGN()

        elif alt38 == 97:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:648: MOD_ASSIGN
            pass
            self.mMOD_ASSIGN()

        elif alt38 == 98:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:659: AND_ASSIGN
            pass
            self.mAND_ASSIGN()

        elif alt38 == 99:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:670: OR_ASSIGN
            pass
            self.mOR_ASSIGN()

        elif alt38 == 100:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:680: XOR_ASSIGN
            pass
            self.mXOR_ASSIGN()

        elif alt38 == 101:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:691: LSHIFT_ASSIGN
            pass
            self.mLSHIFT_ASSIGN()

        elif alt38 == 102:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:705: RSHIFT_ASSIGN
            pass
            self.mRSHIFT_ASSIGN()

        elif alt38 == 103:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:719: POWER_ASSIGN
            pass
            self.mPOWER_ASSIGN()

        elif alt38 == 104:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:732: IDIV_ASSIGN
            pass
            self.mIDIV_ASSIGN()

        elif alt38 == 105:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:744: ID
            pass
            self.mID()

        elif alt38 == 106:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:747: SETTING_ID
            pass
            self.mSETTING_ID()

        elif alt38 == 107:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:758: STRING
            pass
            self.mSTRING()

        elif alt38 == 108:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:765: INTEGER
            pass
            self.mINTEGER()

        elif alt38 == 109:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:773: FLOAT_NUMBER
            pass
            self.mFLOAT_NUMBER()

        elif alt38 == 110:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:786: NEWLINE
            pass
            self.mNEWLINE()

        elif alt38 == 111:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:794: SKIP_
            pass
            self.mSKIP_()

        elif alt38 == 112:
            # C:\\Users\\feder\\Desktop\\University\\Magistrale\\Secondo_Anno\\1_Linguaggi\\Progetto\\yarc\\yarc\\dsl\\v3\\YarcLexer.g:1:800: UNKNOWN
            pass
            self.mUNKNOWN()

    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack("\3\uffff\1\6\1\uffff\1\6\1\uffff")

    DFA17_eof = DFA.unpack("\7\uffff")

    DFA17_min = DFA.unpack("\2\56\2\60\1\uffff\1\60\1\uffff")

    DFA17_max = DFA.unpack("\1\71\1\145\1\71\1\145\1\uffff\1\145\1\uffff")

    DFA17_accept = DFA.unpack("\4\uffff\1\2\1\uffff\1\1")

    DFA17_special = DFA.unpack("\7\uffff")

    DFA17_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack("\12\5"),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
        DFA.unpack("\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass

    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack("\3\uffff\1\4\1\uffff")

    DFA27_eof = DFA.unpack("\5\uffff")

    DFA27_min = DFA.unpack("\2\56\1\uffff\1\60\1\uffff")

    DFA27_max = DFA.unpack("\2\71\1\uffff\1\71\1\uffff")

    DFA27_accept = DFA.unpack("\2\uffff\1\1\1\uffff\1\2")

    DFA27_special = DFA.unpack("\5\uffff")

    DFA27_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1"),
        DFA.unpack(""),
        DFA.unpack("\12\2"),
        DFA.unpack(""),
    ]

    # class definition for DFA #27

    class DFA27(DFA):
        pass

    # lookup tables for DFA #28

    DFA28_eot = DFA.unpack("\4\uffff")

    DFA28_eof = DFA.unpack("\4\uffff")

    DFA28_min = DFA.unpack("\2\56\2\uffff")

    DFA28_max = DFA.unpack("\1\71\1\145\2\uffff")

    DFA28_accept = DFA.unpack("\2\uffff\1\2\1\1")

    DFA28_special = DFA.unpack("\4\uffff")

    DFA28_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\2\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(""),
        DFA.unpack(""),
    ]

    # class definition for DFA #28

    class DFA28(DFA):
        pass

    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        "\1\uffff\20\107\1\156\2\161\6\107\1\174\1\107\1\177\1\u0081\3\uffff"
        "\1\u0086\1\u0088\1\u008a\1\u008c\1\uffff\1\u0090\1\u0093\1\u0095"
        "\1\u0097\1\u009a\1\u009d\1\u009f\5\uffff\1\101\1\107\1\101\1\107"
        "\1\uffff\2\101\2\161\5\uffff\1\101\1\uffff\5\107\1\uffff\7\107"
        "\1\u00bb\11\107\1\u00c6\1\u00c7\2\107\1\u00cb\1\u00cc\1\u00cd\10"
        "\107\1\uffff\5\107\1\uffff\1\107\2\uffff\1\161\1\uffff\1\107\1"
        "\u00dc\6\107\2\uffff\1\107\1\uffff\1\u00e6\15\uffff\1\u00e8\2\uffff"
        "\1\u00ea\6\uffff\1\u00ec\2\uffff\1\u00ee\13\uffff\1\161\2\uffff"
        "\4\107\1\u00f5\14\107\1\uffff\5\107\1\u0107\4\107\2\uffff\1\107"
        "\1\u010e\1\107\3\uffff\7\107\1\u0117\4\107\1\u011c\1\107\1\uffff"
        "\1\u011e\6\107\1\u0125\12\uffff\6\107\1\uffff\3\107\1\u012f\2\107"
        "\1\u0132\1\107\1\u0132\5\107\1\u0139\1\107\1\u0132\1\uffff\4\107"
        "\1\u013f\1\107\1\uffff\1\107\1\u0142\1\107\1\u0144\2\107\1\u0147"
        "\1\107\1\uffff\4\107\1\uffff\1\107\1\uffff\5\107\1\u0153\1\uffff"
        "\1\107\1\u0155\4\107\1\u015a\2\107\1\uffff\1\107\1\u0132\1\uffff"
        "\3\107\1\u0132\2\107\1\uffff\1\107\1\u0164\2\107\1\u0167\1\uffff"
        "\1\u0168\1\107\1\uffff\1\u016a\1\uffff\1\u016b\1\u016d\1\uffff"
        "\1\u016e\12\107\1\uffff\1\107\1\uffff\3\107\1\u00f5\1\uffff\1\u017e"
        "\1\u0132\2\107\1\u0182\1\u0183\3\107\1\uffff\2\107\2\uffff\1\107"
        "\2\uffff\1\u016d\2\uffff\1\u018a\1\u018b\2\107\1\u018e\1\107\1"
        "\u0190\1\u0191\3\107\1\u0195\2\107\1\u00f5\1\uffff\1\u0198\2\107"
        "\2\uffff\2\107\1\u019d\1\u019e\2\107\2\uffff\1\u01a1\1\u01a2\1"
        "\uffff\1\u01a3\2\uffff\2\107\1\u01a6\1\uffff\1\u01a7\1\107\1\uffff"
        "\1\u0132\1\107\1\u01aa\1\107\2\uffff\1\u01ac\1\107\3\uffff\1\u01ae"
        "\1\107\2\uffff\1\u01b0\1\107\1\uffff\1\u01b2\1\uffff\1\107\1\uffff"
        "\1\107\1\uffff\1\107\1\uffff\1\107\1\u01b7\1\107\1\u01b9\1\uffff"
        "\1\107\1\uffff\3\107\1\u01be\1\uffff"
    )

    DFA38_eof = DFA.unpack("\u01bf\uffff")

    DFA38_min = DFA.unpack(
        "\1\0\1\143\1\162\1\154\1\141\2\145\1\151\1\141\1\156\1\145\1\146"
        "\1\144\2\42\1\151\1\42\1\60\2\56\1\156\1\42\1\157\1\150\1\145\1"
        "\157\1\173\1\157\1\60\1\56\3\uffff\4\75\1\uffff\1\74\3\75\1\52"
        "\1\57\1\75\5\uffff\1\75\1\42\1\101\1\42\1\uffff\2\0\2\56\5\uffff"
        "\1\11\1\uffff\1\141\1\143\1\141\1\150\1\172\1\uffff\1\151\1\141"
        "\1\142\1\154\1\156\1\155\1\145\1\60\1\155\1\141\1\170\1\163\1\146"
        "\1\147\1\157\1\164\1\145\2\60\1\157\1\164\3\60\1\151\1\145\1\163"
        "\1\164\1\42\1\154\1\162\1\42\1\uffff\2\164\1\42\1\163\1\137\1\uffff"
        "\1\130\2\uffff\1\56\1\uffff\1\157\1\60\1\144\1\151\1\162\1\157"
        "\1\161\1\147\2\uffff\1\156\1\uffff\1\56\15\uffff\1\75\2\uffff\1"
        "\75\6\uffff\1\75\2\uffff\1\75\13\uffff\1\56\2\uffff\1\156\1\154"
        "\1\164\1\141\1\60\1\147\1\162\2\145\1\164\1\156\1\145\1\151\2\145"
        "\1\141\1\165\1\uffff\1\145\1\156\1\145\1\164\1\153\1\60\1\150\1"
        "\153\1\143\1\156\2\uffff\1\165\1\60\1\164\3\uffff\1\164\1\162\1"
        "\145\1\143\2\155\1\163\1\60\1\141\1\165\1\151\1\141\1\60\1\165"
        "\1\uffff\1\60\1\146\1\155\1\151\1\165\1\125\1\145\1\60\12\uffff"
        "\1\141\1\145\1\164\1\151\2\156\1\uffff\2\145\1\162\1\60\2\145\1"
        "\60\1\156\1\60\1\162\1\164\1\163\1\154\1\163\1\60\1\165\1\60\1"
        "\uffff\1\164\1\137\1\162\1\150\1\60\1\160\1\uffff\1\141\1\60\1"
        "\171\1\60\1\150\1\145\1\60\1\145\1\uffff\1\164\1\162\1\142\1\170"
        "\1\uffff\1\156\1\uffff\1\157\1\141\1\143\1\145\1\156\1\60\1\uffff"
        "\1\162\1\60\1\145\1\156\1\164\1\144\1\60\1\157\1\145\1\uffff\1"
        "\162\1\60\1\uffff\1\144\1\141\1\145\1\60\1\151\1\154\1\uffff\1"
        "\162\1\60\1\141\1\151\1\60\1\uffff\1\60\1\156\1\uffff\1\60\1\uffff"
        "\2\60\1\uffff\1\60\1\145\1\156\1\154\1\151\1\144\1\162\1\154\1"
        "\145\1\156\1\151\1\uffff\1\151\1\uffff\1\162\1\147\1\151\1\60\1"
        "\uffff\2\60\1\163\1\145\2\60\1\156\1\141\1\145\1\uffff\1\164\1"
        "\141\2\uffff\1\164\2\uffff\1\60\2\uffff\2\60\1\145\1\163\1\60\1"
        "\155\2\60\1\143\1\146\1\157\1\60\1\163\1\143\1\60\1\uffff\1\60"
        "\1\162\1\164\2\uffff\1\145\1\164\2\60\1\154\1\151\2\uffff\2\60"
        "\1\uffff\1\60\2\uffff\1\145\1\157\1\60\1\uffff\1\60\1\163\1\uffff"
        "\1\60\1\162\1\60\1\145\2\uffff\1\60\1\141\3\uffff\1\60\1\162\2"
        "\uffff\1\60\1\141\1\uffff\1\60\1\uffff\1\164\1\uffff\1\155\1\uffff"
        "\1\156\1\uffff\1\145\1\60\1\163\1\60\1\uffff\1\154\1\uffff\1\141"
        "\1\164\1\145\1\60\1\uffff"
    )

    DFA38_max = DFA.unpack(
        "\1\uffff\1\164\1\162\1\154\1\171\1\162\1\151\1\157\1\141\2\162"
        "\1\163\1\166\1\162\1\157\1\151\1\160\1\172\2\145\1\164\1\156\1"
        "\157\1\150\1\145\1\157\1\173\1\157\1\172\1\71\3\uffff\4\75\1\uffff"
        "\1\75\1\76\5\75\5\uffff\1\75\1\162\1\172\1\146\1\uffff\2\uffff"
        "\2\145\5\uffff\1\40\1\uffff\1\145\1\164\1\145\1\150\1\172\1\uffff"
        "\1\151\1\141\1\142\1\154\1\156\1\155\1\145\1\172\1\155\1\165\1"
        "\170\1\163\1\146\1\147\1\157\1\164\1\145\2\172\1\157\1\164\3\172"
        "\1\151\1\145\1\163\1\164\1\157\1\154\1\162\1\47\1\uffff\2\164\1"
        "\47\1\163\1\137\1\uffff\1\172\2\uffff\1\145\1\uffff\1\157\1\172"
        "\1\144\1\151\1\162\1\157\1\161\1\147\2\uffff\1\164\1\uffff\1\56"
        "\15\uffff\1\75\2\uffff\1\75\6\uffff\1\75\2\uffff\1\75\13\uffff"
        "\1\145\2\uffff\1\156\2\164\1\141\1\172\1\147\1\162\2\145\1\164"
        "\1\156\1\145\1\151\2\145\1\141\1\165\1\uffff\1\145\1\156\1\145"
        "\1\164\1\153\1\172\1\150\1\153\1\145\1\156\2\uffff\1\165\1\172"
        "\1\164\3\uffff\1\164\1\162\1\145\1\143\2\155\1\163\1\172\1\141"
        "\1\165\1\151\1\141\1\172\1\165\1\uffff\1\172\1\146\1\155\1\151"
        "\1\165\1\125\1\145\1\172\12\uffff\1\141\1\145\1\164\1\151\2\156"
        "\1\uffff\2\145\1\162\1\172\2\145\1\172\1\156\1\172\1\162\1\164"
        "\1\163\1\154\1\163\1\172\1\165\1\172\1\uffff\1\164\1\137\1\162"
        "\1\150\1\172\1\160\1\uffff\1\141\1\172\1\171\1\172\1\150\1\145"
        "\1\172\1\145\1\uffff\1\164\1\162\1\142\1\170\1\uffff\1\156\1\uffff"
        "\1\157\1\141\1\143\1\145\1\156\1\172\1\uffff\1\162\1\172\1\145"
        "\1\156\1\164\1\144\1\172\1\157\1\145\1\uffff\1\162\1\172\1\uffff"
        "\1\144\1\141\1\145\1\172\1\151\1\154\1\uffff\1\162\1\172\1\141"
        "\1\151\1\172\1\uffff\1\172\1\156\1\uffff\1\172\1\uffff\2\172\1"
        "\uffff\1\172\1\145\1\156\1\154\1\151\1\144\1\162\1\154\1\145\1"
        "\156\1\151\1\uffff\1\151\1\uffff\1\162\1\147\1\151\1\172\1\uffff"
        "\2\172\1\163\1\145\2\172\1\156\1\141\1\145\1\uffff\1\164\1\141"
        "\2\uffff\1\164\2\uffff\1\172\2\uffff\2\172\1\145\1\163\1\172\1"
        "\155\2\172\1\143\1\146\1\157\1\172\1\163\1\143\1\172\1\uffff\1"
        "\172\1\162\1\164\2\uffff\1\145\1\164\2\172\1\154\1\151\2\uffff"
        "\2\172\1\uffff\1\172\2\uffff\1\145\1\157\1\172\1\uffff\1\172\1"
        "\163\1\uffff\1\172\1\162\1\172\1\145\2\uffff\1\172\1\141\3\uffff"
        "\1\172\1\162\2\uffff\1\172\1\141\1\uffff\1\172\1\uffff\1\164\1"
        "\uffff\1\155\1\uffff\1\156\1\uffff\1\145\1\172\1\163\1\172\1\uffff"
        "\1\154\1\uffff\1\141\1\164\1\145\1\172\1\uffff"
    )

    DFA38_accept = DFA.unpack(
        "\36\uffff\1\100\1\101\1\102\4\uffff\1\107\7\uffff\1\121\1\122\1"
        "\123\1\124\1\126\4\uffff\1\151\4\uffff\3\156\2\157\1\uffff\1\160"
        "\5\uffff\1\151\40\uffff\1\153\5\uffff\1\34\1\uffff\1\37\1\154\1"
        "\uffff\1\155\10\uffff\1\125\1\52\1\uffff\1\74\1\uffff\1\75\1\100"
        "\1\101\1\102\1\131\1\103\1\143\1\104\1\144\1\105\1\142\1\106\1"
        "\107\1\uffff\1\133\1\127\1\uffff\1\132\1\130\1\135\1\112\1\136"
        "\1\113\1\uffff\1\137\1\114\1\uffff\1\140\1\115\1\141\1\116\1\121"
        "\1\122\1\123\1\124\1\126\1\134\1\152\1\uffff\1\156\1\157\21\uffff"
        "\1\53\12\uffff\1\54\1\71\3\uffff\1\65\1\64\1\66\16\uffff\1\55\10"
        "\uffff\1\77\1\76\1\145\1\110\1\146\1\111\1\147\1\120\1\150\1\117"
        "\6\uffff\1\44\21\uffff\1\57\6\uffff\1\17\10\uffff\1\62\4\uffff"
        "\1\35\1\uffff\1\56\6\uffff\1\70\11\uffff\1\31\2\uffff\1\5\6\uffff"
        "\1\73\5\uffff\1\13\2\uffff\1\20\1\uffff\1\60\2\uffff\1\63\13\uffff"
        "\1\67\1\uffff\1\26\4\uffff\1\3\11\uffff\1\7\2\uffff\1\22\1\15\1"
        "\uffff\1\42\1\21\1\uffff\1\43\1\61\17\uffff\1\10\3\uffff\1\6\1"
        "\14\6\uffff\1\25\1\72\2\uffff\1\40\1\uffff\1\46\1\47\3\uffff\1"
        "\36\2\uffff\1\4\4\uffff\1\41\1\32\2\uffff\1\30\1\33\1\45\2\uffff"
        "\1\1\1\2\2\uffff\1\12\1\uffff\1\11\1\uffff\1\50\1\uffff\1\27\1"
        "\uffff\1\23\4\uffff\1\51\1\uffff\1\16\4\uffff\1\24"
    )

    DFA38_special = DFA.unpack("\1\1\66\uffff\1\0\1\2\u0186\uffff")

    DFA38_transition = [
        DFA.unpack(
            "\11\101\1\76\1\74\1\101\1\75\1\73\22\101\1\76\1\62\1"
            "\70\1\77\1\64\1\54\1\44\1\67\1\55\1\56\1\52\1\50\1\36\1\51\1\35"
            "\1\53\1\72\1\71\1\22\1\23\6\71\1\37\1\40\1\46\1\41\1\47\2\101\2"
            "\66\1\27\2\66\1\63\5\66\1\31\1\66\1\26\3\66\1\65\1\30\1\66\1\25"
            "\2\66\3\21\1\57\1\100\1\60\1\43\1\34\1\101\1\24\1\66\1\4\1\6\1"
            "\14\1\15\1\12\1\66\1\13\2\66\1\7\1\10\1\33\1\11\1\3\1\66\1\16\1"
            "\1\1\5\1\20\1\17\1\2\3\21\1\32\1\42\1\61\1\45\uff81\101"
        ),
        DFA.unpack("\1\102\1\uffff\1\103\3\uffff\1\106\6\uffff\1\105\3" "\uffff\1\104"),
        DFA.unpack("\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack(
            "\1\115\15\uffff\1\114\2\uffff\1\116\2\uffff\1\112\3" "\uffff\1\113"
        ),
        DFA.unpack("\1\122\3\uffff\1\120\5\uffff\1\117\2\uffff\1\121"),
        DFA.unpack("\1\124\3\uffff\1\123"),
        DFA.unpack("\1\125\5\uffff\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\131\1\uffff\1\130\1\uffff\1\132"),
        DFA.unpack("\1\134\14\uffff\1\133"),
        DFA.unpack("\1\136\7\uffff\1\135\4\uffff\1\137"),
        DFA.unpack("\1\140\7\uffff\1\142\11\uffff\1\141"),
        DFA.unpack(
            "\1\150\4\uffff\1\150\52\uffff\1\147\16\uffff\1\145"
            "\3\uffff\1\143\11\uffff\1\146\2\uffff\1\144"
        ),
        DFA.unpack(
            "\1\150\4\uffff\1\150\36\uffff\1\153\36\uffff\1\152" "\1\153\10\uffff\1\151"
        ),
        DFA.unpack("\1\154"),
        DFA.unpack("\1\150\4\uffff\1\150\110\uffff\1\155"),
        DFA.unpack(
            "\12\107\7\uffff\27\107\3\157\4\uffff\1\107\1\uffff" "\27\107\3\157"
        ),
        DFA.unpack("\1\163\1\uffff\12\162\13\uffff\1\163\36\uffff\1\160" "\1\163"),
        DFA.unpack("\1\163\1\uffff\12\162\13\uffff\1\163\36\uffff\1\160" "\1\163"),
        DFA.unpack("\1\166\3\uffff\1\164\1\uffff\1\165"),
        DFA.unpack("\1\150\4\uffff\1\150\106\uffff\1\167"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0080\1\uffff\12\163"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\1\u0087"),
        DFA.unpack("\1\u0089"),
        DFA.unpack("\1\u008b"),
        DFA.unpack(""),
        DFA.unpack("\1\u008e\1\u008f"),
        DFA.unpack("\1\u0092\1\u0091"),
        DFA.unpack("\1\u0094"),
        DFA.unpack("\1\u0096"),
        DFA.unpack("\1\u0098\22\uffff\1\u0099"),
        DFA.unpack("\1\u009b\15\uffff\1\u009c"),
        DFA.unpack("\1\u009e"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00a5"),
        DFA.unpack("\1\150\4\uffff\1\150\52\uffff\1\147\37\uffff\1\147"),
        DFA.unpack("\32\u00a6\4\uffff\1\u00a6\1\uffff\32\u00a6"),
        DFA.unpack("\1\150\4\uffff\1\150\36\uffff\1\153\37\uffff\1\153"),
        DFA.unpack(""),
        DFA.unpack("\12\150\1\uffff\1\150\2\uffff\ufff2\150"),
        DFA.unpack("\12\150\1\uffff\1\150\2\uffff\ufff2\150"),
        DFA.unpack("\1\163\1\uffff\12\162\13\uffff\1\163\37\uffff\1\163"),
        DFA.unpack("\1\163\1\uffff\1\u00a7\11\163\13\uffff\1\163\37\uffff" "\1\163"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\2\u00a9\1\uffff\2\u00a9\22\uffff\1\u00a9"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ab\3\uffff\1\u00aa"),
        DFA.unpack("\1\u00ae\11\uffff\1\u00ad\6\uffff\1\u00ac"),
        DFA.unpack("\1\u00af\3\uffff\1\u00b0"),
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
        DFA.unpack(
            "\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\21\107" "\1\u00ba\10\107"
        ),
        DFA.unpack("\1\u00bc"),
        DFA.unpack("\1\u00bd\23\uffff\1\u00be"),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\1\u00c0"),
        DFA.unpack("\1\u00c1"),
        DFA.unpack("\1\u00c2"),
        DFA.unpack("\1\u00c3"),
        DFA.unpack("\1\u00c4"),
        DFA.unpack("\1\u00c5"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\1\u00c9"),
        DFA.unpack(
            "\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\22\107" "\1\u00ca\7\107"
        ),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u00ce"),
        DFA.unpack("\1\u00cf"),
        DFA.unpack("\1\u00d0"),
        DFA.unpack("\1\u00d1"),
        DFA.unpack("\1\150\4\uffff\1\150\71\uffff\1\u00d2\15\uffff\1\u00d3"),
        DFA.unpack("\1\u00d4"),
        DFA.unpack("\1\u00d5"),
        DFA.unpack("\1\150\4\uffff\1\150"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d6"),
        DFA.unpack("\1\u00d7"),
        DFA.unpack("\1\150\4\uffff\1\150"),
        DFA.unpack("\1\u00d8"),
        DFA.unpack("\1\u00d9"),
        DFA.unpack(""),
        DFA.unpack("\3\u00da\35\uffff\3\u00da"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\163\1\uffff\12\162\13\uffff\1\163\37\uffff\1\163"),
        DFA.unpack(""),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u00dd"),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\1\u00df"),
        DFA.unpack("\1\u00e0"),
        DFA.unpack("\1\u00e1"),
        DFA.unpack("\1\u00e2"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00e3\5\uffff\1\u00e4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e5"),
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
        DFA.unpack("\1\u00e7"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00e9"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00eb"),
        DFA.unpack(""),
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
        DFA.unpack("\1\163\1\uffff\1\u00a7\11\163\13\uffff\1\163\37\uffff" "\1\163"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00ef"),
        DFA.unpack("\1\u00f0\7\uffff\1\u00f1"),
        DFA.unpack("\1\u00f2"),
        DFA.unpack("\1\u00f3"),
        DFA.unpack(
            "\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\16\107" "\1\u00f4\13\107"
        ),
        DFA.unpack("\1\u00f6"),
        DFA.unpack("\1\u00f7"),
        DFA.unpack("\1\u00f8"),
        DFA.unpack("\1\u00f9"),
        DFA.unpack("\1\u00fa"),
        DFA.unpack("\1\u00fb"),
        DFA.unpack("\1\u00fc"),
        DFA.unpack("\1\u00fd"),
        DFA.unpack("\1\u00fe"),
        DFA.unpack("\1\u00ff"),
        DFA.unpack("\1\u0100"),
        DFA.unpack("\1\u0101"),
        DFA.unpack(""),
        DFA.unpack("\1\u0102"),
        DFA.unpack("\1\u0103"),
        DFA.unpack("\1\u0104"),
        DFA.unpack("\1\u0105"),
        DFA.unpack("\1\u0106"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0108"),
        DFA.unpack("\1\u0109"),
        DFA.unpack("\1\u010b\1\uffff\1\u010a"),
        DFA.unpack("\1\u010c"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u010d"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u010f"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0110"),
        DFA.unpack("\1\u0111"),
        DFA.unpack("\1\u0112"),
        DFA.unpack("\1\u0113"),
        DFA.unpack("\1\u0114"),
        DFA.unpack("\1\u0115"),
        DFA.unpack("\1\u0116"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0118"),
        DFA.unpack("\1\u0119"),
        DFA.unpack("\1\u011a"),
        DFA.unpack("\1\u011b"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u011d"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u011f"),
        DFA.unpack("\1\u0120"),
        DFA.unpack("\1\u0121"),
        DFA.unpack("\1\u0122"),
        DFA.unpack("\1\u0123"),
        DFA.unpack("\1\u0124"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
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
        DFA.unpack("\1\u0126"),
        DFA.unpack("\1\u0127"),
        DFA.unpack("\1\u0128"),
        DFA.unpack("\1\u0129"),
        DFA.unpack("\1\u012a"),
        DFA.unpack("\1\u012b"),
        DFA.unpack(""),
        DFA.unpack("\1\u012c"),
        DFA.unpack("\1\u012d"),
        DFA.unpack("\1\u012e"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0130"),
        DFA.unpack("\1\u0131"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0133"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0134"),
        DFA.unpack("\1\u0135"),
        DFA.unpack("\1\u0136"),
        DFA.unpack("\1\u0137"),
        DFA.unpack("\1\u0138"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u013a"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\1\u013b"),
        DFA.unpack("\1\u013c"),
        DFA.unpack("\1\u013d"),
        DFA.unpack("\1\u013e"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0140"),
        DFA.unpack(""),
        DFA.unpack("\1\u0141"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0143"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0145"),
        DFA.unpack("\1\u0146"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0148"),
        DFA.unpack(""),
        DFA.unpack("\1\u0149"),
        DFA.unpack("\1\u014a"),
        DFA.unpack("\1\u014b"),
        DFA.unpack("\1\u014c"),
        DFA.unpack(""),
        DFA.unpack("\1\u014d"),
        DFA.unpack(""),
        DFA.unpack("\1\u014e"),
        DFA.unpack("\1\u014f"),
        DFA.unpack("\1\u0150"),
        DFA.unpack("\1\u0151"),
        DFA.unpack("\1\u0152"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\1\u0154"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0156"),
        DFA.unpack("\1\u0157"),
        DFA.unpack("\1\u0158"),
        DFA.unpack("\1\u0159"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u015b"),
        DFA.unpack("\1\u015c"),
        DFA.unpack(""),
        DFA.unpack("\1\u015d"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\1\u015e"),
        DFA.unpack("\1\u015f"),
        DFA.unpack("\1\u0160"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0161"),
        DFA.unpack("\1\u0162"),
        DFA.unpack(""),
        DFA.unpack("\1\u0163"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0165"),
        DFA.unpack("\1\u0166"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0169"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(
            "\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\22\107" "\1\u016c\7\107"
        ),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u016f"),
        DFA.unpack("\1\u0170"),
        DFA.unpack("\1\u0171"),
        DFA.unpack("\1\u0172"),
        DFA.unpack("\1\u0173"),
        DFA.unpack("\1\u0174"),
        DFA.unpack("\1\u0175"),
        DFA.unpack("\1\u0176"),
        DFA.unpack("\1\u0177"),
        DFA.unpack("\1\u0178"),
        DFA.unpack(""),
        DFA.unpack("\1\u0179"),
        DFA.unpack(""),
        DFA.unpack("\1\u017a"),
        DFA.unpack("\1\u017b"),
        DFA.unpack("\1\u017c"),
        DFA.unpack(
            "\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\22\107" "\1\u017d\7\107"
        ),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u017f"),
        DFA.unpack("\1\u0180"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\u0181\1\uffff\32\107"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0184"),
        DFA.unpack("\1\u0185"),
        DFA.unpack("\1\u0186"),
        DFA.unpack(""),
        DFA.unpack("\1\u0187"),
        DFA.unpack("\1\u0188"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0189"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u018c"),
        DFA.unpack("\1\u018d"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u018f"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0192"),
        DFA.unpack("\1\u0193"),
        DFA.unpack("\1\u0194"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0196"),
        DFA.unpack("\1\u0197"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u0199"),
        DFA.unpack("\1\u019a"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u019b"),
        DFA.unpack("\1\u019c"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u019f"),
        DFA.unpack("\1\u01a0"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u01a4"),
        DFA.unpack("\1\u01a5"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u01a8"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u01a9"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u01ab"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u01ad"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u01af"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u01b1"),
        DFA.unpack(""),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b3"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b4"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b5"),
        DFA.unpack(""),
        DFA.unpack("\1\u01b6"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack("\1\u01b8"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
        DFA.unpack("\1\u01ba"),
        DFA.unpack(""),
        DFA.unpack("\1\u01bb"),
        DFA.unpack("\1\u01bc"),
        DFA.unpack("\1\u01bd"),
        DFA.unpack("\12\107\7\uffff\32\107\4\uffff\1\107\1\uffff\32\107"),
        DFA.unpack(""),
    ]

    # class definition for DFA #38

    class DFA38(DFA):
        pass

        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0:
                LA38_55 = input.LA(1)

                s = -1
                if (0 <= LA38_55 <= 9) or LA38_55 == 11 or (14 <= LA38_55 <= 65535):
                    s = 104

                else:
                    s = 65

                if s >= 0:
                    return s
            elif s == 1:
                LA38_0 = input.LA(1)

                s = -1
                if LA38_0 == 115:
                    s = 1

                elif LA38_0 == 119:
                    s = 2

                elif LA38_0 == 112:
                    s = 3

                elif LA38_0 == 99:
                    s = 4

                elif LA38_0 == 116:
                    s = 5

                elif LA38_0 == 100:
                    s = 6

                elif LA38_0 == 108:
                    s = 7

                elif LA38_0 == 109:
                    s = 8

                elif LA38_0 == 111:
                    s = 9

                elif LA38_0 == 103:
                    s = 10

                elif LA38_0 == 105:
                    s = 11

                elif LA38_0 == 101:
                    s = 12

                elif LA38_0 == 102:
                    s = 13

                elif LA38_0 == 114:
                    s = 14

                elif LA38_0 == 118:
                    s = 15

                elif LA38_0 == 117:
                    s = 16

                elif (88 <= LA38_0 <= 90) or (120 <= LA38_0 <= 122):
                    s = 17

                elif LA38_0 == 50:
                    s = 18

                elif LA38_0 == 51:
                    s = 19

                elif LA38_0 == 97:
                    s = 20

                elif LA38_0 == 85:
                    s = 21

                elif LA38_0 == 78:
                    s = 22

                elif LA38_0 == 67:
                    s = 23

                elif LA38_0 == 83:
                    s = 24

                elif LA38_0 == 76:
                    s = 25

                elif LA38_0 == 123:
                    s = 26

                elif LA38_0 == 110:
                    s = 27

                elif LA38_0 == 95:
                    s = 28

                elif LA38_0 == 46:
                    s = 29

                elif LA38_0 == 44:
                    s = 30

                elif LA38_0 == 58:
                    s = 31

                elif LA38_0 == 59:
                    s = 32

                elif LA38_0 == 61:
                    s = 33

                elif LA38_0 == 124:
                    s = 34

                elif LA38_0 == 94:
                    s = 35

                elif LA38_0 == 38:
                    s = 36

                elif LA38_0 == 126:
                    s = 37

                elif LA38_0 == 60:
                    s = 38

                elif LA38_0 == 62:
                    s = 39

                elif LA38_0 == 43:
                    s = 40

                elif LA38_0 == 45:
                    s = 41

                elif LA38_0 == 42:
                    s = 42

                elif LA38_0 == 47:
                    s = 43

                elif LA38_0 == 37:
                    s = 44

                elif LA38_0 == 40:
                    s = 45

                elif LA38_0 == 41:
                    s = 46

                elif LA38_0 == 91:
                    s = 47

                elif LA38_0 == 93:
                    s = 48

                elif LA38_0 == 125:
                    s = 49

                elif LA38_0 == 33:
                    s = 50

                elif LA38_0 == 70:
                    s = 51

                elif LA38_0 == 36:
                    s = 52

                elif LA38_0 == 82:
                    s = 53

                elif (
                    (65 <= LA38_0 <= 66)
                    or (68 <= LA38_0 <= 69)
                    or (71 <= LA38_0 <= 75)
                    or LA38_0 == 77
                    or (79 <= LA38_0 <= 81)
                    or LA38_0 == 84
                    or (86 <= LA38_0 <= 87)
                    or LA38_0 == 98
                    or LA38_0 == 104
                    or (106 <= LA38_0 <= 107)
                    or LA38_0 == 113
                ):
                    s = 54

                elif LA38_0 == 39:
                    s = 55

                elif LA38_0 == 34:
                    s = 56

                elif LA38_0 == 49 or (52 <= LA38_0 <= 57):
                    s = 57

                elif LA38_0 == 48:
                    s = 58

                elif LA38_0 == 13:
                    s = 59

                elif LA38_0 == 10:
                    s = 60

                elif LA38_0 == 12:
                    s = 61

                elif LA38_0 == 9 or LA38_0 == 32:
                    s = 62

                elif LA38_0 == 35:
                    s = 63

                elif LA38_0 == 92:
                    s = 64

                elif (
                    (0 <= LA38_0 <= 8)
                    or LA38_0 == 11
                    or (14 <= LA38_0 <= 31)
                    or (63 <= LA38_0 <= 64)
                    or LA38_0 == 96
                    or (127 <= LA38_0 <= 65535)
                ):
                    s = 65

                if s >= 0:
                    return s
            elif s == 2:
                LA38_56 = input.LA(1)

                s = -1
                if (0 <= LA38_56 <= 9) or LA38_56 == 11 or (14 <= LA38_56 <= 65535):
                    s = 104

                else:
                    s = 65

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 38, _s, input)
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
