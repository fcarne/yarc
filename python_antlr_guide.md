# Using ANTLR 3 with Python 3 🐍
In this guide we will look at how to setup a project using ANTLR 3 and Python 3.

## Setup ⚙️
If you are developing a project in Python you should be familiar with some of the best practices needed to simplify code writing. 

We do not go into much details, as a refresher we will list all of the necessary steps.

First of all, you should create a virtual environment in which to store all the dependecies needed for your project. To do that, hop into your preferred terminal and write:
```bash
python -m venv <path/to/venv>
```

Now you should `activate` your environment with the following command:
```bash
source <path/to/venv>/bin/activate
```
if you are on Linux, or this one: 
```bash
<path/to/venv>\Scripts\Activate.ps1
```
if you are on Windows. 

> **⚠️** With **Powershell** you may need to enable the execution of scripts, more [here](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows).

Now, you should install all the dependencies needed for your project. ANTLR 3 official support ended when Python 2 was still a thing, but a Python 3 compatible version can be found [on GitHub](https://github.com/fcarne/antlr3-python3-runtime) (give it a **⭐** if you found it useful).

To install the dependency from GitHub you can run the following command if you are using `pip`:
```bash
pip install git+https://github.com/fcarne/antlr3-python3-runtime.git
```
or, if you are using `poetry`:
```bash
poetry add git+https://github.com/fcarne/antlr3-python3-runtime.git
```

> **ℹ️** Don't know what `poetry` is? [Check it out](https://python-poetry.org), it is a tool to simplify packaging and dependency management.

If you also need String Template 3 for text generation and rewriting, you can install from the following repository:
```bash
https://github.com/fcarne/stringtemplate3-python3-runtime.git
```

While not necessary, you can also setup a `git` repository and some `pre-commit` hooks. Those will run everytime you commit and can be useful to format your code, perform static type-checking (yes, types exists even in Python), or remove unused imports (more in the following section) using `autoflake`. 

To simplify some of these steps you can use `cookiecutter`, a tool for creating Python projects from templates, aka recipes. For a simple Python package, you can use the following recipe: [python-package-template](https://github.com/TezRomacH/python-package-template) 

## Developing the grammar 📝
You can write your grammar specification as you would usually do. Just remember some things:
1. Set `language = Python3` in the `options` tag of your lexer and parser specifications.
2. In the `@header` tags use `from` statements if needed.
3. Semantic actions (the ones between `{...}`) expect Python code, use `self` and not `this`.

Once you are finished preparing your grammar, generate lexer and parser. Beware that antlrworks adds the following line:
```python
from antlr3.compat import frozenset, set
```
which will cause a runtime error because those modules do not exist. You can safely remove this import (or setup a pre-commit hook to remove unused imports) since the generated code doesn't actually use neither of them.

Being written for Python, the library has some minor differences with respect to the Java one (e.g., deprecates the `getCharPositionInLine()` method in favor of the `charPositionInLine` property).

## Using the generated parser 🚀
Now that you have your lexer and parser you need to use them in your code, or even better, you need to test them before using them.

To test your lexer you first need to instantiate it:
```python
from antlr3 import ANTLRStringStream

with open(filename) as f:
    content = f.read()

input_stream = ANTLRStringStream(content) # read from a string
lexer = MyLexer(input_stream)
```
To read the token stream from the lexer, you can use the following statements:
```python
for token in lexer:
    print(token.type, token.text)
```
Yes, the `Lexer` class is iterable.

To instantiate the parser, you can do the following:
```python
from antlr3 import ANTLRFileStream, CommonTokenStream

input_stream = ANTLRFileStream(filename) # read from a file
lexer = MyLexer(input_stream)
token_stream = CommonTokenStream(lexer) # create the token stream from the lexer
parser = MyParser(token_stream)
```

To start parsing, you simply call the needed parser rule:
```python
parser.script(...) # In MyParser.g there is the rule script: ...
```

If you used template rewriting, you must call `toString()` on the result of the parser method to apply the rewriting.

> **ℹ️** More examples on how to instantiate lexer and parser [here](https://theantlrguy.atlassian.net/wiki/spaces/ANTLR3/pages/2687339/Antlr3PythonTarget#Antlr3PythonTarget-Examples)

## Conclusions 🐍
In this guide we looked at how to setup a project and use the generated lexer and parser in our code using ANTLR 3 and Python 3. It is actually fairly easy and effectively the same as using the library in Java, the main issue derives from the scarcity of documentation online. 

You can also use ANTLR 4 that comes with the official PiPy package `antlr4-python3-runtime`.

## Useful resources 🌐
- [Python package API](https://www.antlr3.org/api/Python/index.html)
- [Official ANTLR 3 Docs](https://theantlrguy.atlassian.net/wiki/spaces/ANTLR3/pages/2687117/Python+runtime)
- [StringTemplate 3 and Python](https://theantlrguy.atlassian.net/wiki/spaces/ST/pages/1409045/Python+notes)
