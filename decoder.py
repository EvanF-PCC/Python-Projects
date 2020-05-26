from PIL import Image
import binascii

img = Image.open("jellyfish.png")
encodeimg = Image.open("deepfried.png")
words = "Will_He_Hungers_for_the_flesh"


def BinaryToDecimal(binary):
    string = int(binary, 2)

    return string


def bintostr(bin: str):
    str_data = ""
    for i in range(0, len(bin), 7):
        temp_data = bin[i:i + 7]

        decimal_data = BinaryToDecimal(temp_data)

        str_data = str_data + chr(decimal_data)
    return str_data


def encode():
    global r1, words
    r1, g1, b1 = encodeimg.split()

    binary = str(''.join(format(i, 'b') for i in bytearray(words, encoding='utf-8')))
    print(binary)
    binary += "2"
    print(binary)

    for i in range(len(binary)):
        x = i % r1.width
        y = i // r1.width

        val = r1.getpixel((x, y))
        changed = int(str(val // 10) + str(binary[0]))
        binary = binary[1:]
        r1.putpixel((x, y), changed)

    img2 = Image.merge("RGB", (r1, g1, b1))
    img2.save("outer.png")


def decode():
    global spaces
    try:
        r, g, b, a = img.split()
    except ValueError:
        r, g, b = img.split()

    binary = dostuff(r)
    binary = bintostr(binary)

    print(binary)


def dostuff(r):
    global spaces
    currentval = "0"
    binary = ""
    spaces = []
    for y in range(r.height):

        for x in range(r.width):
            currentval = r.getpixel((x, y)) % 10
            if currentval == 2:
                return binary

            else:
                binary += str(currentval)
            pass


decode()

