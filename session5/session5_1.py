#!/usr/bin/python3

# You are the passive attacker called Eve and you have captured Alice and Bob and imprisoned them.
# You overhear the following dialog:
# Bob: Oh, let’s not bother with the prime in the Diffie-Hellman protocol, it will make things easier.
# Alice: Ok, but we still need a base g to raise things to. How about g=3?
# Bob: All right, then my result is 27.
# Alice: And mine is 243.
# As the attacker Eve, can you guess Bob’s or Alice’s private keys?
# Can you find out what their secret combined key is?

from math import log

g = 3
bob_public_key = 27
alice_public_key = 243

def calc_public_key(private_key, g):
    return g ** private_key

def calc_private_key(public_key, g):
    return round( log(public_key, g) )

def calc_secret_key(others_public_key, my_private_key):
    return others_public_key ** my_private_key

bob_private_key = calc_private_key(bob_public_key, g)
alice_private_key = calc_private_key(alice_public_key, g)

print("Base number is: ", g)
print("Bob's public key is: ", bob_public_key)
print("Alice's public key is: ", alice_public_key)
print("Bob's private key is: ", bob_private_key)
print("Alice's private key is: ", alice_private_key)

print("Bob calculates the secret key to be: ", calc_secret_key(alice_public_key, bob_private_key))
print("Alice calculates the secret key to be: ", calc_secret_key(bob_public_key, alice_private_key))
