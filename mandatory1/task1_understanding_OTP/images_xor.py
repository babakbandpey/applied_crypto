#!/usr/bin/python3
from PIL import Image, ImageChops
import sys


try:
    # 3 parameters are expected when running the script.
    # In order: the name of the file containing the plaintext,
    # the name of the file containing the key, and the name of the file where
    # the result of the XOR will be stored.
    # Both the plaintext and the key should be bitmap images of the same size (number of pixels).
    plaintextFilename = sys.argv[1]
    keyFilename = sys.argv[2]
    encryptionFilename = sys.argv[3]

    # load images
    plaintext = Image.open(plaintextFilename).convert("1")
    key = Image.open(keyFilename).convert("1")

    # If either the plaintext or the key are not B/W images,
    # they will be converted to one.
    # If you want to see the converted image, uncomment the following two lines
    #plaintext.show()
    #key.show()

    # compute the XOR
    ciphertext = ImageChops.logical_xor(plaintext, key)
    ciphertext.save(encryptionFilename)
    print("Script finished successfully")

except Exception as exc:
    print("Error:", exc)

