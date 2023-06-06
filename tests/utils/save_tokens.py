import sys
from pathlib import Path

from antlr3 import ANTLRStringStream, Token

from yarc.compiler.YarcLexer import YarcLexer

TESTS_DIR = Path(__file__).resolve().parent.parent
resources_dir = TESTS_DIR / "resources"

input_file = resources_dir / sys.argv[1]
with open(input_file) as f:
    input_str = f.read()

input_stream = ANTLRStringStream(input_str)
lexer = YarcLexer(input_stream)

token: Token
for token in lexer:
    print(token.type)
