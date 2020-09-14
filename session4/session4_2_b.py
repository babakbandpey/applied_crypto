#!/usr/bin/python3

#***********************
# Session 4 Exercise 2 b
#***********************

# intercepted message "247, 337, 322, 463, 15, 73, 440, 15, 342, 323, 435"

from rsa_utils import factorize, decrypt, findModInverse

n = 629
public_key = 17

factorize(n)
# N has the following factors: [17, 37.0, 37, 17.0]

p = 17
q = 37

phi = (p-1)*(q-1)

private_key = findModInverse(public_key, phi)

encrypted_message = [247, 337, 322, 463, 15, 73, 440, 15, 342, 323, 435]

for ciphertext in encrypted_message:
    print(chr(decrypt(ciphertext, private_key, n)))

# prints MATH IS FUN
