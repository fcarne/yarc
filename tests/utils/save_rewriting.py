import sys
from pathlib import Path

from antlr3 import ANTLRFileStream, CommonTokenStream

from yarc.compiler.YarcLexer import YarcLexer
from yarc.compiler.YarcParser import YarcParser

TESTS_DIR = Path(__file__).resolve().parent.parent
resources_dir = TESTS_DIR / "resources"

input_file = resources_dir / sys.argv[1]
file_input = ANTLRFileStream(input_file)
lexer = YarcLexer(file_input)
stream = CommonTokenStream(lexer)
parser = YarcParser(stream)

script = parser.scenario(handler_kwargs={"warnings": False})

print(script)
