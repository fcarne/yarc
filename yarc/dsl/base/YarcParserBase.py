from antlr3 import Parser


class Python3ParserBase(Parser):
    def CannotBePlusMinus(self) -> bool:
        return True

    def CannotBeDotLpEq(self) -> bool:
        return True
