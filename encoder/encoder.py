#!/usr/bin/env python3
from io import BytesIO
from PIL import Image


def CreateMessage(message):
    """
    Takes a string and returns the ascii binary representation.
    :param message: string given from user
    :return: String; string
    """
    encode = message.encode("ascii")
    bytes = int.from_bytes(encode, "big")
    binary = bin(bytes)
    cleanedBinary = binary[2:]
    preppedBinary = cleanedBinary.zfill(len(cleanedBinary) + 1)
    # temp = bin(int.from_bytes(message.encode("ascii"), 'big'))[2:]  # removes 0b from beginning
    # string = temp.zfill(len(temp)+1)  # adds 0 to beginning
    return preppedBinary


def Encode(picture, string):
    """
    Takes a image (can be lossy format) creates a mutable view that maintains consistency among the objects.
    Checks and changes the least significant bit (LSB) of the image to contain ascii bits.
    :param picture: user image
    :param string: user hidden message
    :return: raw image data; user image with hidden ascii bits
    """
    pixel_byte = picture.tobytes()
    pixel_stream = BytesIO(pixel_byte)  # creates stream with bytes from pixel
    pixel_buffer = pixel_stream.getbuffer()  # turns stream into a memoryview that is mutable and consistent
    for index, bit in enumerate(string):
        if pixel_buffer[index] % 2 == 0 and int(bit) == 1:
            pixel_buffer[index] += 1
        elif pixel_buffer[index] % 2 == 1 and int(bit) == 0:
            pixel_buffer[index] -= 1

    width, height = picture.size
    encoded_bytes = pixel_buffer.tobytes()
    encoded_picture = Image.frombytes("RGB", (width, height), encoded_bytes)
    return encoded_picture


def main():
    picture = Image.open(r"C:\Users\Mushbrain\Desktop\untitled1.jpg")
    message = "hello world"
    string = CreateMessage(message)
    encoded_picture = Encode(picture, string)
    encoded_picture.save(r"C:\Users\Mushbrain\Desktop\fromb.png")


if __name__ == "__main__":
    main()
