import os

from antlr3 import *

from yarc.dsl.v3.YarcLexer import YarcLexer
from yarc.dsl.v3.YarcParser import YarcParser

parent_dir = os.path.dirname(os.path.abspath(__file__))
tests_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

input_file = os.path.join(tests_dir, "assets", "sample.txt")
with open(input_file) as f:
    input_str = f.read()

input_stream = ANTLRStringStream(input_str)
lexer = YarcLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = YarcParser(stream)
tree = parser.scenario()
