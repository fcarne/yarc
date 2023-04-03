# Generated from /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/parser/v3/yarc.g by ANTLR 4.9.2
from typing import TextIO

import sys
from io import StringIO

from antlr4 import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\3")
        buf.write("\f\b\1\4\2\t\2\3\2\6\2\7\n\2\r\2\16\2\b\3\2\3\2\2\2\3")
        buf.write("\3\3\3\2\2\2\f\2\3\3\2\2\2\3\6\3\2\2\2\5\7\4\62;\2\6\5")
        buf.write("\3\2\2\2\7\b\3\2\2\2\b\6\3\2\2\2\b\t\3\2\2\2\t\n\3\2\2")
        buf.write("\2\n\13\7a\2\2\13\4\3\2\2\2\4\2\b\2")
        return buf.getvalue()


class yarcLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    ID = 1

    channelNames = ["DEFAULT_TOKEN_CHANNEL", "HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = [
        "<INVALID>",
    ]

    symbolicNames = ["<INVALID>", "ID"]

    ruleNames = ["ID"]

    grammarFileName = "yarc.g"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache()
        )
        self._actions = None
        self._predicates = None
