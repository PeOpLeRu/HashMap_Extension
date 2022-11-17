from .interpreter import Interpreter

class SpecialDictException(Exception):
    ...

class SpecialDict(dict):

    def __init__(self):
        super().__init__()
        self.iloc = _Iloc(self)
        self.ploc = _Ploc(self)

    def __str__(self):
        return f"SpecialDict -> (size: {len(self.items())}, {dict(self.items())})"

class _Iloc:
    
    def __init__(self, outer_instance) -> None:
        self.outer = outer_instance

    def __getitem__(self, key_index : int):
        keys = sorted(self.outer.keys())

        if key_index >= len(keys) or key_index < 0:
            raise SpecialDictException("Index out of range!")

        return self.outer.__getitem__(keys[key_index])

class _Ploc:
    
    def __init__(self, outer_instance) -> None:
        self.outer = outer_instance
        self.interpreter = Interpreter()

    def __getitem__(self, key_condition : str) -> SpecialDict:
        result = SpecialDict()
        keys = list(self.outer.keys())
        
        self.interpreter.init_interpreter(key_condition)

        for key in keys:
            if self.interpreter.check_condition(key):
                result[key] = self.outer[key]

        return result