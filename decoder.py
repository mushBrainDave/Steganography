#!/usr/bin/env python3
from io import BytesIO
from PIL import Image


def DecodeMessage(picture):
    pixel_byte = picture.tobytes()
    pixel_stream = BytesIO(pixel_byte)  # creates stream with bytes from pixel
    pixel_buffer = pixel_stream.getbuffer()  # turns stream into a memoryview that is mutable and consistent
    bit_array = []
    string = ""
    print(pixel_byte[3])
    for letters in range(len(pixel_buffer)):
        bit = pixel_buffer[letters] >> 1
        #print(pixel_buffer[letters])
        if bit % 2 == 0:
            string += str(0)
            bit_array.append(0)
        else:
            string += str(1)
            bit_array.append(1)
    #print(bit_array)

    return bit_array, string


def CompileMessage(bit_array, string):
    print("")
#    s = ["00100001"]
#    print(type(s[0]))
#    s1 = int(s[0], 2)
#    print(s1)
#    s2 = (97).to_bytes(1, byteorder="little")
#    print(s2.decode("ascii"))
#    for x in range(byte_array):
#        for byt in range(7):
            


def main():
    picture = Image.open(r"C:\Users\Mushbrain\Desktop\fromb.jpg")
    print(picture.getpixel((0, 0)))

    byte_array, string = DecodeMessage(picture)
    CompileMessage(byte_array, string)


if __name__ == "__main__":
    main()
