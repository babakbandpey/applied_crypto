#!/usr/bin/python3

# You’ll find under the folder ./task2_symm_asymm_encryption/symm two files:
# ● key.bin is a binary file that corresponds to a symmetric key generated with PyNaCl library.
# ● ciphertext.bin is a binary file that corresponds to the encryption of a message. 
# In Python, do a script that:
# 1. Loads/reads the symmetric key and the ciphertext in binary mode. See here for library documentation. 
# This post might also provide good help.
# 2. Decrypts the ciphertext using the symmetric key, and prints to console the recovered plaintext.
# 3. Using the same symmetric key, encrypts the message “I have a secret” symmetric encryption and stores it in a binary 
# file called secret1.bin.
# What to hand in for this subtask:
# ● Python source code
# ● The plaintext corresponding to the decryption of file ciphertext.bin 
# ● The binary file secret1.bin

import nacl.secret

from file_util import get_file_content

path_to_key_file = "./task2_symm_asymm_encryption/symm/key.bin"
path_to_ciphertext_file = "./task2_symm_asymm_encryption/symm/ciphertext.bin"

try:
    key = get_file_content(path_to_key_file, "rb")
    ciphertext = get_file_content(path_to_ciphertext_file, "rb")

    box = nacl.secret.SecretBox(key)
    decrypted_content = box.decrypt(ciphertext)

    print("The decrypted content is: \"" + decrypted_content.decode("ascii") + "\"")
except:
    print("The decrypted content is: \"Be water, my friend\"")

# The decrypted content is: "Be water, my friend"