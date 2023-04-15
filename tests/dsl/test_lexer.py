import os

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.InputStream import InputStream

from yarc.dsl.v4 import YarcLexer


def test_lexer():
    class MyErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            raise ValueError(f"Syntax error at line {line}:{column} {msg}")

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

    input_file = os.path.join(tests_dir, "assets\\lexer_test.txt")
    with open(input_file) as f:
        input_str = f.read()

    input_stream = InputStream(input_str)
    lexer = YarcLexer(input_stream)

    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())

    for i in range(100):
        token = lexer.nextToken()
        token_type = lexer.symbolicNames[token.type - 1]

        print(token, token_type)

        if token_type == "EOF":
            break
