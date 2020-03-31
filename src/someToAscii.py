import string
import random

def main(pivot, mode, base, sizeOfChar, func):
    print("{0}\n{1:^16}\n{0}".format(pivot, mode))

    sizeOfString = int(input("Enter size of string: "))

    printable = "".join(set(string.printable) - set(string.whitespace))
    typesOfString = [string.digits, string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, printable]
    print("types:\n\t0 - digits\n\t1 - ascii_letters\n\t2 - ascii_lowercase\n\t3 - ascii_uppercase\n\t4 - printable (without whitespace)\n")
    typeOfString = int(input("Enter type of string: "))

    asciiString = "".join(["0" * (sizeOfChar - len(func(ord(random.choice(typesOfString[typeOfString])))[2:])) + func(ord(random.choice(typesOfString[typeOfString])))[2:] for i in range(sizeOfString)])
    correctResult = [int(asciiString[i : i + sizeOfChar], base) for i in range(0, len(asciiString), sizeOfChar)]

    inputResult = list(input(f"Enter '{asciiString}': "))

    print("\n", pivot, sep = "")
    noError = True
    for correctResultElement, inputResultElement in zip(correctResult, inputResult):
        if (chr(correctResultElement) != inputResultElement):
            print(f"'{'0' * (sizeOfChar - len(func(correctResultElement)[2:])) + func(correctResultElement)[2:]}' is '{chr(correctResultElement)}' but not '{inputResultElement}'")
            noError = False
    print(pivot, "\n")
    print(("Try harder!", "Congrats!")[noError])