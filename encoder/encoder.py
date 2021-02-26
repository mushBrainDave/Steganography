#!/usr/bin/env python3
from io import BytesIO
from PIL import Image, PngImagePlugin
from PIL.PngImagePlugin import PngImageFile, ChunkStream, getchunks


def CreateMessage(message):
    """
    Takes a string and returns the ascii binary representation.
    :param message: string given from user
    :return: String; string
    """
    temp = bin(int.from_bytes(message.encode(), 'big'))[2:]  # removes 0b from beginning
    string = temp.zfill(len(temp)+1)  # adds 0 to beginning
    return string


def Encode(picture, string):
    """
    Takes a image (can be lossy format) creates a mutable view that maintains consistency among the objects.
    Checks and changes the least significant bit (LSB) of the image to contain ascii bits.
    :param picture: user image
    :param string: user hidden message
    :return: raw image data; user image with hidden ascii bits
    """
    pic = Image.open(picture)
    pic.save(BytesIO(), 'PNG', compression_level=100)
    #Image.open(pic.read())
    #print(type(picture))
    #picture.show()
    print(picture)
    #pixel_byte = picture.tobytes()  # this and one below uncomment and change 34 variable
    #pixel_stream = BytesIO(pixel_byte)  # creates stream with bytes from pixel
    #print(pixel_stream.read())
    pixel_buffer = picture.getbuffer()  # turns stream into a memoryview that is mutable and consistent
    for index, bit in enumerate(string, 600):
        if pixel_buffer[index] % 2 == 0 and int(bit) == 1:
            pixel_buffer[index] += 1
        elif pixel_buffer[index] % 2 == 1 and int(bit) == 0:
            pixel_buffer[index] -= 1

    #width, height = picture.size
    encoded_bytes = pixel_buffer.tobytes()
    en = BytesIO(encoded_bytes)
    #encoded_picture = Image.frombytes("RGB", (width, height), encoded_bytes)
    #print(encoded_picture)  # needs to be pngimagefile
#    encoded_picture.save(BytesIO(), format='PNG')
    #print(PngImagePlugin.getchunks(encoded_picture))
#    print(encoded_picture)
#    en = encoded_picture.tobytes()
#    en2 = BytesIO(en)
    #a = PngImageFile(encoded_picture.open())
    #print(type(en2))
    return en


def main():
    picture = Image.open(r"C:\Users\Mushbrain\Desktop\1.png")
    message = "hello world"
    string = CreateMessage(message)
    encoded_picture = Encode(picture, string)
    encoded_picture.save(r"C:\Users\Mushbrain\Desktop\fromb.png")


if __name__ == "__main__":
    main()
