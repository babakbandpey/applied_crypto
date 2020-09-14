#!/usr/bin/python3

#***********************
# Session 4 Exercise 2 a
#***********************

from rsa_utils import encrypt

n = 629
public_key = 17

message = "A"

ciphertext = encrypt(ord(message), public_key, n)

# ciphertext = 337
print(ciphertext)