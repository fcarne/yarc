import re
from enum import Enum


class TargetLanguage(Enum):
    JAVA = "Java"
    CPP = "Cpp"
    CSHARP = "CSharp"
    PYTHON2 = "Python2"
    PYTHON3 = "Python3"
    JAVASCRIPT = "JavaScript"
    RUBY = "Ruby"


# Dictionary mapping target languages to their corresponding mappings
language_mappings = {
    TargetLanguage.JAVA: {
        "self": "this",
        "not": "!",
        "[]": "new ArrayList<>()",
        "{}": "new HashMap<>()",
        "append": "add",
        "comment_start": "//",
    },
    TargetLanguage.CPP: {
        "self": "this",
        "not": "!",
        "[]": "std::vector<>()",
        "{}": "std::map<>()",
        "append": "push_back",
        "comment_start": "//",
    },
    TargetLanguage.CSHARP: {
        "self": "this",
        "not": "!",
        "[]": "new List<>()",
        "{}": "new Dictionary<>()",
        "append": "Add",
        "comment_start": "//",
    },
    TargetLanguage.PYTHON2: {
        "self": "self",
        "not": "not",
        "[]": "[]",
        "{}": "{}",
        "append": "append",
        "comment_start": "#",
    },
    TargetLanguage.PYTHON3: {
        "self": "self",
        "not": "not",
        "[]": "[]",
        "{}": "{}",
        "append": "append",
        "comment_start": "#",
    },
    TargetLanguage.JAVASCRIPT: {
        "self": "this",
        "not": "!",
        "[]": "[]",
        "{}": "{}",
        "append": "push",
        "comment_start": "//",
    },
    TargetLanguage.RUBY: {
        "self": "self",
        "not": "!",
        "[]": "[]",
        "{}": "{}",
        "append": "push",
        "comment_start": "#",
    },
}


def translate(grammar: str, target_language: TargetLanguage) -> str:
    def replace_predicates(grammar: str) -> str:
        language_mapping = language_mappings[target_language]
        for python_predicate, target_predicate in language_mapping.items():
            regex = r"(\b)(" + re.escape(python_predicate) + r")(\b)"
            grammar = re.sub(regex, r"\1" + target_predicate, grammar)

        return grammar

    transformed_grammar = replace_predicates(grammar)

    transformed_grammar = re.sub(
        r"language\s*=\s*[a-zA-Z0-9]+\s*;",
        f"language = {target_language.value};",
        transformed_grammar,
    )

    transformed_grammar = re.sub(
        r"@header\s*\{.*?\}",
        r"@header {\n/* TO DO: Import super class */\n}",
        transformed_grammar,
        flags=re.DOTALL,
    )

    return transformed_grammar
