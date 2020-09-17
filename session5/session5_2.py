#!/usr/bin/python3

# “Rudimentary” DH key exchange:
# Write a program that creates shared keys between two parties. 
# For that you can use, for instance, the parameters p=23and g=5. 
# You will need to have two instances of the program running. Each program should write their 
# public key(A=g a and B=g b)
# to disk for the other program to load. When they’re finished, 
# have them print out the shared key so that you can verify that they both come up with the same key.

from dh_utils import generate_private_key, calc_public_key, calc_secret_key

import time
import json
import os

g = 5
p = 23

firstname = input("Type your firstname: ")

counterpart_name = input("Type your counterpart name: ")

my_private_key = generate_private_key()

my_public_key_file = open(firstname + ".txt", "w")
my_public_key_file.write(str(calc_public_key(my_private_key, g, p)))
my_public_key_file.close()

while True:
    try:
        counterpart_public_key_file = open(counterpart_name + ".txt", "r")
        counterpart_public_key = int(counterpart_public_key_file.read())

        print("Secret key calculate to be: ", calc_secret_key(counterpart_public_key, my_private_key, p) )
        try :
            time.sleep(2)
            os.remove(firstname + ".txt")
            print(firstname + ".txt public key file removed")
        except :
            print("Something wrong. Public key file disappeared!!!!")
        break
    except:
        print(counterpart_name + "'s public key not ready")
        time.sleep(1)