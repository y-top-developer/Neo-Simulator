from random import choice
from string import digits, ascii_lowercase, ascii_uppercase, ascii_letters, printable

from src.Level import Level, LevelType
from src.Value import Value, ValueType

class DataProvider():
    def __init__(self, initial, final, level):
        self.initial = Value(initial)
        self.final = Value(final)
        self.level = Level(level)

    def __get_character(self):
        if self.level.type == LevelType.DIGITS:
            return choice(digits)
        elif self.level.type == LevelType.LOWERCASE:
            return choice(ascii_lowercase)
        elif self.level.type == LevelType.UPPERCASE:
            return choice(ascii_uppercase)
        elif self.level.type == LevelType.LETTERS:
            return choice(ascii_letters)
        elif self.level.type == LevelType.PRINTABLE:
            return choice(printable)

    def __get_character_tuple(self):
        def integer_to_base(integer, base):
            if not 1 <= base <= 36:
                return chr(integer)
            letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            while integer:
                result += letters[(integer % base) % len(letters)]
                integer //= base
            return result[::-1] or "0"

        def get_character_by_type(character, result_type):
            if result_type.type == ValueType.Number:
                character = integer_to_base(ord(character), int(result_type.name))
            return character

        character = self.__get_character()
        character_initial = get_character_by_type(character, self.initial)
        character_final = get_character_by_type(character, self.final)
        
        return character, character_initial, character_final
    
    def get_data(self, size):
        data = [self.__get_character_tuple() for i in range(int(size))]
        return {
            'ASCII': [i[0] for i in data],
            'initial': [i[1] for i in data],
            'final': [i[2] for i in data]
        }
