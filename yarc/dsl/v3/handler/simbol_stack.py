from typing import Optional


class SymbolTable:
    def __init__(self, parent: Optional["SymbolTable"] = None) -> None:
        self._symbols: dict[str, type] = {}
        self.parent = parent

    def define(self, name: str, var_type: type) -> None:
        self._symbols[name] = var_type

    def lookup(self, name: str) -> Optional[type]:
        if name in self._symbols:
            return self._symbols[name]
        elif self.parent is not None:
            return self.parent.lookup(name)
        else:
            return None


class SymbolStack:
    def __init__(self) -> None:
        self._stack = [SymbolTable()]

    def push(self) -> None:
        self._stack.append(SymbolTable(parent=self.top()))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> SymbolTable:
        return self._stack[-1]

    def define(self, name: str, var_type: type) -> None:
        self.top().define(name, var_type)

    def lookup(self, name: str) -> Optional[type]:
        return self.top().lookup(name)
