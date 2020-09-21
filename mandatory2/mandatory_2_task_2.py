#!/usr/bin/python3

# You’ll find under the folder /asymm one single file:
# ● publickey.bin is a binary file that corresponds to my public key, generated with PyNaCl library,
# using SealedBox (not Box !).
# See here for library documentation.
# In Python, do a script that:
# 1. Loads/reads the public key from the file in binary mode.
# 2. Encrypts the text ”Encryption matters” using that public key.
# 3. Stores the ciphertext in a binary file secret2.bin

from nacl.public import SealedBox, PublicKey
from file_util import get_file_content, write_file_content

path_to_public_key_file = "./task2_symm_asymm_encryption/asymm/publickey.bin"
path_to_ciphertext_file = "./secret2.bin"
message = b"Encryption matters"

try:
    pk = get_file_content(path_to_public_key_file, "rb")
    sealed_box = SealedBox(PublicKey(pk))
    write_file_content(path_to_ciphertext_file, sealed_box.encrypt(message), "wb")
    print("The message is encrypted and saved into the: " + path_to_ciphertext_file)
except:
    print("Operation failed")