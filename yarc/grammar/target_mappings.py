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


def translate_grammar(grammar: str, target_language: TargetLanguage) -> str:
    def replace_predicates(grammar: str) -> str:
        language_mapping = language_mappings[target_language]
        for python_predicate, target_predicate in language_mapping.items():
            grammar = grammar.replace(python_predicate, target_predicate)

        return grammar

    transformed_grammar = replace_predicates(grammar)

    transformed_grammar = re.sub(
        r"language=[a-zA-Z0-9]+;" f'language="{target_language.value}";',
        transformed_grammar,
    )

    transformed_grammar = re.sub(
        r"@members\s*{[^}]*}", r"/* TO DO: Import super class */", transformed_grammar
    )

    return transformed_grammar
