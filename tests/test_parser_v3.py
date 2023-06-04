import os

from antlr3 import ANTLRFileStream, CommonTokenStream

from yarc.compiler.YarcLexer import YarcLexer
from yarc.compiler.YarcParser import YarcParser

tests_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(tests_dir, "resources", "sample.txt")
with open(input_file) as f:
    input_str = f.read()

file_input = ANTLRFileStream(input_file)
# input_stream = ANTLRStringStream(input_str)
lexer = YarcLexer(file_input)
stream = CommonTokenStream(lexer)
parser = YarcParser(stream)


script = parser.scenario(handler_kwargs={"warnings": True})

print(script)

print("ERRORS:")
for k, v in parser.handler.error_dict.items():
    print(f"{k}: {v}")

print("WARNINGS:")
print(parser.handler.warning_dict)
