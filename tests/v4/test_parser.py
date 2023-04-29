import os

from antlr4 import CommonTokenStream, InputStream

from yarc.dsl.v4 import YarcLexer, YarcParser

parent_dir = os.path.dirname(os.path.abspath(__file__))
tests_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

input_file = os.path.join(tests_dir, "assets", "sample.txt")
with open(input_file) as f:
    input_str = f.read()

input_stream = InputStream(input_str)
lexer = YarcLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = YarcParser(stream)
tree = parser.scenario()
