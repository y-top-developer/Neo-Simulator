import asciiToSome
import someToAscii

pivot = "================"
welcome = "_2_"

print("{0}\n{1:^16}\n{0}".format(pivot, welcome))

while True:
    print("types: ascii2hex - 0, ascii2binary - 1, hex2ascii - 2, binary2ascii - 3, exit - -1")
    type = int(input("Enter type: "))

    if type == 0:
        asciiToSome.main(pivot, "ASCII2Hex", 16, 2, hex)
    elif type == 1:
        asciiToSome.main(pivot, "ASCII2Binary", 2, 8, bin)
    elif type == 2:
        someToAscii.main(pivot, "Hex2ASCII", 16, 2, hex)
    elif type == 3:
        someToAscii.main(pivot, "Binary2ASCII", 2, 8, bin)
    elif type == -1:
        exit(1)