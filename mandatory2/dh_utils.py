# g is public (prime) base.
# p is public (prime) modulus.

from random import randrange

def generate_private_key():
    return randrange(1, 100)

def calc_public_key(private_key, g, p):
    return (g ** private_key) % p

def calc_secret_key(others_public_key, my_private_key, p):
    return (others_public_key ** my_private_key) % p