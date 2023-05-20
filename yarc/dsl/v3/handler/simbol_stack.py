from typing import NamedTuple, Optional


class Variable(NamedTuple):
    name: str
    type_: type
    used: bool


class SymbolTable:
    def __init__(self, parent: Optional["SymbolTable"] = None):
        self._symbols: dict[str, Variable] = {}
        self.parent = parent

    def define(self, name: str, var_type: type, used: bool = False) -> None:
        self._symbols[name] = Variable(name, var_type, used)

    def lookup(self, name: str) -> Optional[Variable]:
        if name in self._symbols:
            var = self._symbols[name]
            self._symbols[name] = Variable(var.name, var.type_, True)
            return var
        elif self.parent is not None:
            return self.parent.lookup(name)
        else:
            return None


class SymbolStack:
    def __init__(self):
        self._stack = [SymbolTable()]

    def push(self) -> None:
        self._stack.append(SymbolTable(parent=self.top()))

    def pop(self) -> SymbolTable:
        return self._stack.pop()

    def top(self) -> SymbolTable:
        return self._stack[-1]

    def define(self, name: str, var_type: type, used: bool = False) -> None:
        self.top().define(name, var_type, used)

    def lookup(self, name: str) -> Optional[Variable]:
        return self.top().lookup(name)
