#!/usr/bin/python3

# ***********************************
# RSA Exercise Session 4
# ***********************************

from rsa_utils import decrypt

private_key = 937
n = 2537
e = 13

public_key = e

ciphertext = 2222

message = decrypt(ciphertext, private_key, n)
# message = 18
print(message)
print(chr(message))

