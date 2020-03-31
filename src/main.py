import asciiToSome
import someToAscii

pivot = "================"
welcome = "_2_"

print("{0}\n{1:^16}\n{0}".format(pivot, welcome))

while True:
    print("\ntypes:\n\t0 - ascii2hex\n\t1 - ascii2binary\n\t2 - hex2ascii\n\t3 - binary2ascii\n\t5 - exit\n")
    type = int(input("Enter type: "))

    if type == 0:
        asciiToSome.main(pivot, "ASCII2Hex", 16, 2, hex)
    elif type == 1:
        asciiToSome.main(pivot, "ASCII2Binary", 2, 8, bin)
    elif type == 2:
        someToAscii.main(pivot, "Hex2ASCII", 16, 2, hex)
    elif type == 3:
        someToAscii.main(pivot, "Binary2ASCII", 2, 8, bin)
    elif type == 5:
        exit(1)