from .lexer import Lexer
from .tokens import Token, TokenType

class ParserException(Exception):
    ...

class Parser:

    def __init__(self):
        self.current_token: Token | None = None
        self.lexer = Lexer()

    def init_parser(self, text: str) -> None:
        self.lexer.init_lexer(text)
        self.current_token = self.lexer.next()

    def parse_key(self, key : str) -> list[float]:
        res = []
    
        self.init_parser(key)
    
        while self.current_token.type != TokenType.EOL:
            token = self.current_token
            self._check_type(TokenType.NUMBER)
            res.append(float(token.value))

        return res

    def parse_condition(self, condition : str) -> list[Token]:
        res = []

        self.init_parser(condition)

        while self.current_token.type != TokenType.EOL:
            token_1 = self.current_token
            self._check_type([TokenType.GREATER, TokenType.LESS, TokenType.EQUAL, TokenType.NOT_EQUAL, TokenType.GREATER_OR_EQUAL, TokenType.LESS_OR_EQUAL])
            token_2 = self.current_token
            self._check_type(TokenType.NUMBER)
            res.append(Token(token_1.type, float(token_2.value)))

        return res

    def _check_type(self, type_: TokenType | list[TokenType]):
        if isinstance(type_, TokenType) and self.current_token.type == type_:
            self.current_token = self.lexer.next()
        elif isinstance(type_, list) and self.current_token.type in type_:
            self.current_token = self.lexer.next()
        else:
            raise ParserException(f"invalid token order. Expected {type_}, Received {self.current_token.type}")

        return