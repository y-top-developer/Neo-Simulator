import string
import random

pivot = "================"
mode = "ASCII2Binary"
print("{0}\n{1:^16}\n{0}".format(pivot, mode))

sizeOfString = int(input("Enter size of ascii string: "))

printable = "".join(set(string.printable) - set(string.whitespace))
typesOfString = [string.digits, string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, printable]
print("types: 0 - digits, 1 - ascii_letters, 2 - ascii_lowercase, 3 - ascii_uppercase, 4 - printable (without whitespace)")
typeOfString = int(input("Enter type of string: "))

asciiString = "".join([random.choice(typesOfString[typeOfString]) for i in range(sizeOfString)])
correctResult = "".join(["0" * (8 - len(bin(ord(c))[2:])) + bin(ord(c))[2:] for c in asciiString])

inputResult = input(f"Enter '{asciiString}' in binary: ")

print((correctResult, "Congrats!")[inputResult == correctResult])
