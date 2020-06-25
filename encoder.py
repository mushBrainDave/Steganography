#!/usr/bin/env python3
from io import BytesIO
from PIL import Image


def CreateMessage(message):
    temp = bin(int.from_bytes(message.encode(), 'big'))[2:]  # removes 0b from beginning
    string = temp.zfill(len(temp)+1)  # adds 0 to beginning
    return string


def Encode(picture, string):
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
    encoded_picture.save(r"C:\Users\Mushbrain\Desktop\fromb.jpg", subsampling=0, quality=100)
    encoded_picture.save(r"C:\Users\Mushbrain\Desktop\fromb.png")


if __name__ == "__main__":
    main()
