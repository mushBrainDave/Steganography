#!/usr/bin/env python3
from io import BytesIO

from PIL import Image


def DecodeMessage(picture):
    pixel_byte = picture.tobytes()
    pixel_stream = BytesIO(pixel_byte)  # creates stream with bytes from pixel
    pixel_buffer = pixel_stream.getbuffer()  # turns stream into a memoryview that is mutable and consistent
    bit_array = []
    for letters in range(len(pixel_buffer)):
        bit = pixel_buffer[letters] >> 1
        if bit % 2 == 0:
            bit_array.append(0)
        else:
            bit_array.append(1)
    return bit_array


def CompileMessage(bit_array):
    s = ["00100001"]
    print(type(s[0]))
    s1 = int(s[0], 2)
    print(s1)
    s2 = (97).to_bytes(1, byteorder="little")
    print(s2.decode("ascii"))
#    for x in range(byte_array):
#        for byt in range(7):
            


def main():
    picture = Image.open(r"C:\Users\Mushbrain\Desktop\fromb.jpg")
    DecodeMessage(picture)
    CompileMessage(1)


if __name__ == "__main__":
    main()
