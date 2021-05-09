from enum import Enum, auto

class ValueType(Enum):
    ASCII = auto()
    Number = auto()

class Value:
    def __init__(self, name):
        self.name = name
        self.type = self.__get_type(name)

    def __get_type(self, name):
        if name.lower() in ['a', 'ascii', 'asci']:
            return ValueType.ASCII
        elif name.isdigit():
            return ValueType.Number