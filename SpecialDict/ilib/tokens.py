from enum import Enum, auto

class TokenType(Enum):
    NUMBER = auto()

    EQUAL = auto()
    NOT_EQUAL = auto()

    GREATER = auto()
    GREATER_OR_EQUAL = auto()

    LESS = auto()
    LESS_OR_EQUAL = auto()

    EOL = auto()

class Token:

    def __init__(self, _type : TokenType, _value : str | None) -> None:
        self.type : TokenType = _type
        self.value : int | None = _value

    def __str__(self) -> str:
        return f"Token ({self.type}, {self.value})"