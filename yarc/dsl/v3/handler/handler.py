import stringtemplate3
from antlr3 import Parser


class Handler:
    def set_template(self, parser: Parser, template_path: str):
        parser.templateLib = stringtemplate3.StringTemplateGroupLoader(
            file=template_path, lexer="angle-bracket"
        )
