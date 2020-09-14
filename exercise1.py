#!/usr/bin/python3

from ceasar import encrypt, decrypt, populate_decrypt_dict

print("###############################")
print("# Team Soteria                #")
print("# Applied Crypto Exercise 1:  #")
print("###############################")
print("# Implementing Ceasar Wheel...#")
print("###############################")

shift = int(input("Indtast key value between 0 and 25: "))

action = int(input("Type 1 for encrypting or 0 for decrypt: "))

message = input("Type your text: ")

populate_decrypt_dict(shift)

if(action):
    print("The encrypted text: " + encrypt(message))    
else:
    print("The decrypted text: " + decrypt(message))