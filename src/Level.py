from enum import Enum, auto

class LevelType(Enum):
    DIGITS = auto()
    LOWERCASE = auto()
    UPPERCASE = auto()
    LETTERS = auto()
    PRINTABLE = auto()

class Level():
    def __init__(self, name):
        self.name = name
        self.type = self.__get_type(name)

    def __get_type(self, name):
        name = name.lower()
        if name in ['0', 'digits', 'digit']:
            return LevelType.DIGITS
        elif name in ['1', 'lowercase', 'lower', 'low']:
            return LevelType.LOWERCASE
        elif name in ['2', 'uppercase', 'upper', 'up']:
            return LevelType.UPPERCASE
        elif name in ['3', 'letter', 'let']:
            return LevelType.LETTERS
        elif name in ['4', 'printable', 'print']:
            return LevelType.PRINTABLE