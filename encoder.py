#!/usr/bin/env python3
from io import BytesIO
from PIL import Image


def CreateMessage(message):
    ascii = 7

    message_stream = message.getbuffer()
    bit_array = []
    #bit_array = [0 for x in range(len(message_stream) * 7)]
    #print(bit_array)
    for letters in range(len(message_stream)):
        for bits in range(ascii):
            bit = message_stream[letters] >> bits
            if bit % 2 == 0:
                bit_array.append(0)
            else:
                bit_array.append(1)
            print(bit_array)
    return bit_array


def Encode(picture, bit_array):
    pixel_byte = picture.tobytes()
    pixel_stream = BytesIO(pixel_byte)  # creates stream with bytes from pixel
    pixel_buffer = pixel_stream.getbuffer()  # turns stream into a memoryview that is mutable and consistent
    for rgb in range(len(bit_array)):
        if pixel_buffer[rgb] % 2 == 0 and bit_array[rgb] == 1:
            pixel_buffer[rgb] += 1
        elif pixel_buffer[rgb] % 2 == 1 and bit_array[rgb] == 0:
            pixel_buffer[rgb] -= 1
        else:
            pass
    width, height = picture.size
    encoded_bytes = pixel_buffer.tobytes()
    encoded_picture = Image.frombytes("RGB", (width, height), encoded_bytes)
    return encoded_picture


def main():
    picture = Image.open(r"C:\Users\Mushbrain\Desktop\untitled1.jpg")
    message = BytesIO(b"hello world")
    bit_array = CreateMessage(message)
    encoded_picture = Encode(picture, bit_array)
    encoded_picture.save(r"C:\Users\Mushbrain\Desktop\fromb.jpg", "JPEG")


if __name__ == "__main__":
    main()
