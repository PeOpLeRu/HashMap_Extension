from ilib.specialDict import *
from ilib.interpreter import *
from ilib.parser import *
from ilib.lexer import *
from ilib.tokens import *
import pytest

class TestSpecialDict:

    def testSpecialDict(self):
        sd = SpecialDict()
        sd["0"] = 0
        sd["1"] = 1
        sd["2"] = 2
        sd["3"] = 3
        sd["2, 3"] = 23
        sd["2, 7"] = 27
        sd["5, 7"] = 57
        sd["5, 10"] = 510
        sd["5, 7, 2"] = 572
        sd["5, 10, 4"] = 5104
        sd["1, 1, 1, 1"] = 1111
        sd["1, 1, 2, 3"] = 1123
        sd["value4"] = 4
        sd["a_str"] = "str_value"

        assert sd.iloc[0] == 0
        assert sd.iloc[1] == 1
        assert sd.iloc[2] == 1111
        assert sd.iloc[3] == 1123
        assert sd.iloc[4] == 2
        assert sd.iloc[5] == 23
        assert sd.iloc[7] == 3
        assert sd.iloc[8] == 510
        assert sd.iloc[12] == "str_value"

        print(sd.iloc[13])

        print(sd)
        
        with pytest.raises(SpecialDictException):
            sd.iloc[14]

        assert sd.ploc['<>2, <>3'].ploc['<>3, <10']["5, 7"] == 57
        assert sd.ploc['>=2, >1'].ploc['<=5, ==10']["5, 10"] == 510
        assert sd.ploc['>3, >=4'].ploc['>1, <=7']["5, 7"] == 57
        assert sd.ploc["==5, >=10"]["5, 10"] == 510

        with pytest.raises(LexerException):
            sd.ploc[">>="]

        with pytest.raises(ParserException):
            sd.ploc["2>"]

        with pytest.raises(InterpreterException):
            interpreter = Interpreter()
            interpreter.check_condition(">2")

    def testToken(self):
        assert TokenType.GREATER == Token(TokenType.GREATER, None).type
        token = Token(TokenType.NUMBER, 123)
        print(token)

test = TestSpecialDict()
test.testSpecialDict()
test.testToken()