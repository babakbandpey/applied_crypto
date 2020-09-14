#!/usr/bin/python3

from ceasar import decrypt, populate_decrypt_dict

print("################################################")
print("# Team Soteria                                 #")
print("# Applied Crypto Exercise 2:                   #")
print("################################################")
print("# Implementing Ceasar Wheel Brute Force Attack #")
print("################################################")

message = input("Type your text: ")

for shift in range(0, 26):
    populate_decrypt_dict(shift)    
    print("The decrypted text: " + decrypt(message))