import string
import random

def main(pivot, mode, base, sizeOfChar, func):
    print("{0}\n{1:^16}\n{0}\n".format(pivot, mode))

    sizeOfString = int(input("Enter size of string: "))

    printable = "".join(set(string.printable) - set(string.whitespace))
    typesOfString = [string.digits, string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, printable]
    print("types:\n\t0 - digits\n\t1 - ascii_letters\n\t2 - ascii_lowercase\n\t3 - ascii_uppercase\n\t4 - printable (without whitespace)\n")
    typeOfString = int(input("Enter type of string: "))

    asciiString = "".join([random.choice(typesOfString[typeOfString]) for i in range(sizeOfString)])
    correctResult = ["0" * (sizeOfChar - len(bin(ord(c))[2:])) + func(ord(c))[2:].upper() for c in asciiString]

    inputResult = input(f"Enter '{asciiString}': ")
    inputResult = [inputResult[i : i + sizeOfChar] for i in range(0, len(inputResult), sizeOfChar)]

    print("\n", pivot, sep = "")
    noError = True
    for correctResultElement, inputResultElement in zip(correctResult, inputResult):
        if (correctResultElement != inputResultElement):
            print(f"'{chr(int(correctResultElement, base))}' is '{correctResultElement}' but not '{inputResultElement}'")
            noError = False
    print(pivot, "\n")
    print(("Try harder!", "Congrats!")[noError])