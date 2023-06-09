from typing import Optional, TextIO

import re
import sys

from antlr3 import InputStream, Lexer
from antlr3.tokens import CommonToken, Token

from yarc.compiler import YarcParser


class YarcLexerBase(Lexer):
    NEW_LINE_PATTERN = re.compile("[^\r\n\f]+")
    SPACES_PATTERN = re.compile("[\r\n\f]+")

    def __init__(self, input: InputStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.tokens: list[Token] = []
        self.indents: list[int] = []
        self.opened = 0

    def reset(self):
        self.tokens = []
        self.indents = []
        self.opened = 0
        super().reset()

    def emit(self, token: Optional[Token] = None) -> Token:
        t = super().emit(token)
        self.emitToken(t)
        return t

    def emitToken(self, token: Token) -> None:
        self._state.token = token
        self.tokens.append(token)

    def nextToken(self):
        # Check if the end-of-file is ahead and there are still some DEDENTS expected.
        if self.input.LA(1) == YarcParser.EOF and len(self.indents) != 0:
            # Remove any trailing EOF tokens from our buffer.
            self.tokens = [
                token for token in self.tokens if token.type != YarcParser.EOF
            ]

            # First emit an extra line break that serves as the end of the statement.
            self.emitToken(self.commonToken(YarcParser.NEWLINE, "\n"))

            # Now emit as much DEDENT tokens as needed.
            while len(self.indents) != 0:
                self.emitToken(self.createDedent())
                self.indents.pop()

            # Put the EOF back on the token stream.
            self.emitToken(self.commonToken(YarcParser.EOF, "<EOF>"))

        next_ = super().nextToken()
        return next_ if len(self.tokens) == 0 else self.tokens.pop(0)

    def createDedent(self):
        return self.commonToken(YarcParser.DEDENT, "")

    def commonToken(self, type_: int, text: str) -> CommonToken:
        stop = self.getCharIndex() - 1
        start = stop if text == "" else stop - len(text) + 1
        token = CommonToken(
            type=type_,
            text=text,
            channel=Lexer.DEFAULT_TOKEN_CHANNEL,
            start=start,
            stop=stop,
        )

        token.line = self._state.tokenStartLine
        token.charPositionInLine = self._state.tokenStartCharPositionInLine

        if type_ == YarcParser.INDENT:
            token.line += 1
            token.charPositionInLine = 0

        return token

    def getIndentationCount(self, whitespace: str) -> int:
        count = 0
        for c in whitespace:
            if c == "\t":
                count += 8 - count % 8
            else:
                count += 1
        return count

    def atStartOfInput(self):
        return self.getCharIndex() == 0

    def openBrace(self):
        self.opened += 1

    def closeBrace(self):
        self.opened -= 1

    def onNewLine(self):
        new_line = self.NEW_LINE_PATTERN.sub("", self.text)
        spaces = self.SPACES_PATTERN.sub("", self.text)

        # Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
        # satisfy the final newline needed by the single_put rule used by the REPL.
        next_ = self.input.LA(1)
        next_next = self.input.LA(2)

        if self.opened > 0 or (next_next != -1 and next_ in (10, 13, 35)):
            self.skip()
        else:
            self.emitToken(self.commonToken(YarcParser.NEWLINE, new_line))
            indent = self.getIndentationCount(spaces)
            previous = 0 if len(self.indents) == 0 else self.indents[-1]

            if indent == previous:
                self.skip()
            elif indent > previous:
                self.indents.append(indent)
                self.emitToken(self.commonToken(YarcParser.INDENT, spaces))
            else:
                while len(self.indents) > 0 and self.indents[-1] > indent:
                    self.emitToken(self.createDedent())
                    self.indents.pop()
