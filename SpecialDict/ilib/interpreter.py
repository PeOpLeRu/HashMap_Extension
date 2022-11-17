from .parser import Parser
from .tokens import Token, TokenType

class InterpreterException(Exception):
    ...

class Interpreter():
    def __init__(self):
        self.parser = Parser()
        self.condition : list[Token] | None = None

    def init_interpreter(self, _key_condition : str):
        self.condition = self.parser.parse_condition(_key_condition)

    def check_condition(self, key : str) -> bool:
        if self.condition == None:
            raise InterpreterException("Interpreter condition is not initialization! Call init_interpreter()")

        if True in [elem.isalpha() for elem in key]:
            return False

        key : list[float] = self.parser.parse_key(key)

        if len(key) != len(self.condition):
            return False

        for i in range(0, len(key)):
            if not self._check_subcondition(key[i], self.condition[i].type, self.condition[i].value):
                return False
        
        return True

    def _check_subcondition(self, key_value : float, operator : TokenType, value : float) -> bool:
        match operator:
            case TokenType.GREATER:
                if key_value > value:
                    return True
                else:
                    return False
            case TokenType.GREATER_OR_EQUAL:
                if key_value >= value:
                    return True
                else:
                    return False
            case TokenType.EQUAL:
                if key_value == value:
                    return True
                else:
                    return False
            case TokenType.NOT_EQUAL:
                if key_value != value:
                    return True
                else:
                    return False
            case TokenType.LESS_OR_EQUAL:
                if key_value <= value:
                    return True
                else:
                    return False
            case TokenType.LESS:
                if key_value < value:
                    return True
                else:
                    return False