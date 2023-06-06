import os
import re
from pathlib import Path

import pytest
from antlr3 import ANTLRFileStream, CommonTokenStream

from yarc.compiler.YarcLexer import YarcLexer
from yarc.compiler.YarcParser import YarcParser

TESTS_DIR = Path(__file__).resolve().parent
resources_dir = TESTS_DIR / "resources"
rewrite_dir = TESTS_DIR / "rewrite"


def read_expected_rewriting(filename):
    with open(filename) as file:
        return file.read().strip()


def sanitize(s):
    s = s.strip()
    s = re.sub(r"'seed': \d+", r"'seed: 1", s)
    s = re.sub(r"rep.set_global_seed\(\d+\)", r"rep.set_global_seed\(1\)", s)
    return s


@pytest.mark.parametrize("filename", os.listdir(resources_dir))
def test_parser(filename):
    rewriting_filename = os.path.join(
        rewrite_dir, os.path.splitext(filename)[0] + ".txt"
    )
    expected = read_expected_rewriting(rewriting_filename)

    lexer = YarcLexer(ANTLRFileStream(resources_dir / filename))
    stream = CommonTokenStream(lexer)
    parser = YarcParser(stream)

    script = parser.scenario(handler_kwargs={"warnings": False})

    assert sanitize(script.toString()) == sanitize(expected)
