#!/usr/bin/python3

import nacl.secret
import nacl.utils
from pathlib import Path
import string
from random import choice

file_to_encrypt = input("type the path to the file which shall be encrypted: " )

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(length))
    

try:
    f = open(file_to_encrypt)
    f.close()

    contents = Path(file_to_encrypt).read_text()

    binary_encoded_content = contents.encode()

    # This must be kept secret, this is the combination to your safe
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

    # This is your safe, you can use it to encrypt or decrypt messages
    box = nacl.secret.SecretBox(key)

    encrypted_content = box.encrypt(binary_encoded_content)

    assert len(encrypted_content) == len(binary_encoded_content) + box.NONCE_SIZE + box.MACBYTES

    encrypted_file_name = get_random_string(10)

    encrypted_f = open(encrypted_file_name + ".enc", "wb")
    encrypted_f.write(encrypted_content)
    encrypted_f.close()

    key_f = open(encrypted_file_name + ".enc.key", "wb")
    key_f.write(key)
    key_f.close()



except IOError:
    print("File not accessible")
    
