import os
from pathlib import Path

import pytest
from antlr3 import ANTLRStringStream, Token

from yarc.compiler.YarcLexer import YarcLexer

TESTS_DIR = Path(__file__).resolve().parent
resources_dir = TESTS_DIR / "resources"
tokens_dir = TESTS_DIR / "tokens"


def read_file(filename):
    with open(filename) as file:
        return file.read()


def read_expected_tokens(filename):
    with open(filename) as file:
        return [int(token.strip()) for token in file.readlines()]


@pytest.mark.parametrize("filename", os.listdir(resources_dir))
def test_lexer(filename):
    content = read_file(os.path.join(resources_dir, filename))

    tokens_filename = os.path.join(
        tokens_dir, os.path.splitext(filename)[0] + ".tokens"
    )
    expected_tokens = read_expected_tokens(tokens_filename)

    input_stream = ANTLRStringStream(content)
    lexer = YarcLexer(input_stream)

    read: Token
    for read, expected in zip(lexer, expected_tokens):
        assert read.type == expected, f"Actual: {read}, expected: {expected}"
