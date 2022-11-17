from .tokens import Token, TokenType

class LexerException(Exception):
    ...

class Lexer:
    def __init__(self):
        self.pos = 0
        self.text = ""
        self.current_char = ""

        self.ops = ['>', '<', '=']

    def init_lexer(self, text: str):
        self.pos = 0
        self.text = text
        self.current_char = self.text[self.pos]

    def forward(self):
        self.pos += 1
        if self.pos == len(self.text):
            self.current_char = ""
        else:
            self.current_char = self.text[self.pos]

    def next(self) -> Token:
        while self.current_char != "":
            if self.current_char not in self.ops and not self.current_char.isdigit():
                self.skip()
                continue
            if self.current_char.isdigit():
                return Token(TokenType.NUMBER, self._number())
            if self.current_char in self.ops:
                return Token(self._operator(), None)
            
        return Token(TokenType.EOL, "")

    def skip(self):
        while self.current_char != "" and self.current_char not in self.ops and not self.current_char.isdigit():
            self.forward()

    def _number(self) -> str:
        result = []

        while self.current_char != "" and \
                (self.current_char.isdigit() or 
                self.current_char == '.'):
            result.append(self.current_char)
            self.forward()

        return "".join(result)

    def _operator(self) -> TokenType:
        res = []

        while self.current_char != "" and self.current_char in self.ops:
            res.append(self.current_char)
            self.forward()

        res = "".join(res)

        match res:
            case ">=":
                return TokenType.GREATER_OR_EQUAL
            case ">":
                return TokenType.GREATER
            case "==":
                return TokenType.EQUAL
            case "<>":
                return TokenType.NOT_EQUAL
            case "<":
                return TokenType.LESS
            case "<=":
                return TokenType.LESS_OR_EQUAL

        raise LexerException("Undefined operator")