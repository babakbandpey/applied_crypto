# g is public (prime) base.
# p is public (prime) modulus.

import random
from dh_safe_primes import dh_sp_array

import nacl.secret
import nacl.utils

def get_random_safe_prime():
    return random.choice(dh_sp_array)

def generate_private_key():
    return random.randrange(50, 100)

def get_random_base(p = 10, q = 100):
    primes = [i for i in range(p,q) if isPrime(i)]
    return random.choice(primes)

def calc_public_key(private_key, g, p):
    return (g ** private_key) % p

def calc_secret_key(others_public_key, my_private_key, p):
    return (others_public_key ** my_private_key) % p

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

"""
Not related to DH
"""

def encrypt_msg(key, msg):

    binary_encoded_content = msg.encode()

    # This must be kept secret, this is the combination to your safe
    key = bin(key)

    # This is your safe, you can use it to encrypt or decrypt messages
    box = nacl.secret.SecretBox(key)

    encrypted_content = box.encrypt(binary_encoded_content)

    assert len(encrypted_content) == len(binary_encoded_content) + box.NONCE_SIZE + box.MACBYTES

    return encrypted_content

def decrypt_msg(key, msg):

    binary_encoded_content = msg.encode()

    # This must be kept secret, this is the combination to your safe
    key = bin(key)

    # This is your safe, you can use it to encrypt or decrypt messages
    box = nacl.secret.SecretBox(key)

    return box.decrypt(binary_encoded_content)