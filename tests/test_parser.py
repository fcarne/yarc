import os

from antlr4 import *

from yarc.dsl.v4 import YarcLexer, YarcParser

tests_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(tests_dir, "assets", "sample_alt.txt")
with open(input_file) as f:
    input_str = f.read()

input_stream = InputStream(input_str)
lexer = YarcLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = YarcParser(stream)
tree = parser.scene()
