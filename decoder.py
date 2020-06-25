#!/usr/bin/env python3
from io import BytesIO
from PIL import Image


def DecodeMessage(picture):
    """
    Takes user image (must be lossless format) extracts the least significant bit (LSB).
    Compiles LSB into bytes that are stored into an array.
    :param picture: user image
    :return: String; array of bytes
    """
    pixel_byte = picture.tobytes()
    pixel_stream = BytesIO(pixel_byte)  # creates stream with bytes from pixel
    pixel_buffer = pixel_stream.getbuffer()  # turns stream into a memoryview that is mutable and consistent
    string = ""
    byte_array = []
    for index, letter in enumerate(pixel_buffer):
        if index > 100:  # temporary for simplicity
            break
        elif index % 8 == 0:  # will be kept in some form
            byte_array.append(string)
            string = ""
        if letter % 2 == 0:
            string += str(0)
        elif letter % 2 == 1:
            string += str(1)
    byte_array.pop(0)
    return byte_array


def CompileMessage(byte_array):
    """
    Takes an array of strings representing ascii binary.
    :param byte_array: String; ascii bytes
    :return: String; hidden message
    """
    message = ""
    try:
        for byte in byte_array:
            message += str(int(byte, 2).to_bytes(1, byteorder="little").decode("ascii"))  # messy
    except UnicodeDecodeError:
        pass
    return message


def main():
    picture = Image.open(r"C:\Users\Mushbrain\Desktop\fromb.png")
    byte_array = DecodeMessage(picture)
    message = CompileMessage(byte_array)
    print(message)


if __name__ == "__main__":
    main()
