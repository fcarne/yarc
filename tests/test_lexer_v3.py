import os

from antlr3 import ANTLRStringStream

from yarc.parser.YarcLexer import YarcLexer

tests_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(tests_dir, "resources", "sample.txt")
with open(input_file) as f:
    input_str = f.read()

input_stream = ANTLRStringStream(input_str)
lexer = YarcLexer(input_stream)

for token in lexer:
    print(token)
