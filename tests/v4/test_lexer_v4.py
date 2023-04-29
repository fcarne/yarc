import os

from antlr4 import Token
from antlr4.error.ErrorListener import ErrorListener
from antlr4.InputStream import InputStream

from yarc.dsl.v4.YarcLexer import YarcLexer
from yarc.dsl.v4.YarcParser import YarcParser


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError(f"Syntax error at line {line}:{column} {msg}")


parent_dir = os.path.dirname(os.path.abspath(__file__))
tests_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

input_file = os.path.join(tests_dir, "assets", "sample.txt")
with open(input_file) as f:
    input_str = f.read()

input_stream = InputStream(input_str)
lexer = YarcLexer(input_stream)

lexer.removeErrorListeners()
lexer.addErrorListener(MyErrorListener())

while True:
    token: Token = lexer.nextToken()
    token_type = (
        lexer.symbolicNames[token.type] if token.type != YarcParser.EOF else "EOF"
    )

    print(token, token_type)

    if token_type == "EOF":
        break
