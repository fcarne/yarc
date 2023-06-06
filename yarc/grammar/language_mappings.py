import re
from enum import Enum


class Language(Enum):
    JAVA = "Java"
    CPP = "Cpp"
    CSHARP = "CSharp"
    PYTHON2 = "Python2"
    PYTHON3 = "Python3"
    JAVASCRIPT = "JavaScript"
    RUBY = "Ruby"


# Dictionary mapping target languages to their corresponding mappings
language_mappings = {
    Language.JAVA: {
        "self": "this",
        "not": "!",
        "[]": "new ArrayList<>()",
        "{}": "new HashMap<>()",
        "append": "add",
        "comment_start": "//",
    },
    Language.CPP: {
        "self": "this",
        "not": "!",
        "[]": "std::vector<>()",
        "{}": "std::map<>()",
        "append": "push_back",
        "comment_start": "//",
    },
    Language.CSHARP: {
        "self": "this",
        "not": "!",
        "[]": "new List<>()",
        "{}": "new Dictionary<>()",
        "append": "Add",
        "comment_start": "//",
    },
    Language.PYTHON2: {
        "self": "self",
        "not": "not",
        "[]": "[]",
        "{}": "{}",
        "append": "append",
        "comment_start": "#",
    },
    Language.PYTHON3: {
        "self": "self",
        "not": "not",
        "[]": "[]",
        "{}": "{}",
        "append": "append",
        "comment_start": "#",
    },
    Language.JAVASCRIPT: {
        "self": "this",
        "not": "!",
        "[]": "[]",
        "{}": "{}",
        "append": "push",
        "comment_start": "//",
    },
    Language.RUBY: {
        "self": "self",
        "not": "!",
        "[]": "[]",
        "{}": "{}",
        "append": "push",
        "comment_start": "#",
    },
}


def translate(grammar: str, language: Language) -> str:
    def replace_predicates(grammar: str) -> str:
        language_mapping = language_mappings[language]
        for python_predicate, target_predicate in language_mapping.items():
            regex = r"(\b)(" + re.escape(python_predicate) + r")(\b)"
            grammar = re.sub(regex, r"\1" + target_predicate, grammar)

        return grammar

    grammar = replace_predicates(grammar)

    grammar = re.sub(
        r"language\s*=\s*[a-zA-Z0-9]+\s*;",
        f"language = {language.value};",
        grammar,
    )

    grammar = re.sub(
        r"@header\s*\{.*?\}",
        r"@header {\n/* TO DO: Import super class */\n}",
        grammar,
        flags=re.DOTALL,
    )

    return grammar
