# g is public (prime) base.
# p is public (prime) modulus.

import random
from dh_safe_primes import dh_sp_array

import nacl.secret
import nacl.utils

import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat import backends

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

def convert_secret_key_to_derived_key(secret_key):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"00000000",
        iterations=100000,
        backend=backends.default_backend()
    )
    key = kdf.derive(str(secret_key).encode('utf-8'))
    return key

def create_secret_box(secret_key):
    # This is your safe, you can use it to encrypt or decrypt messages
    return nacl.secret.SecretBox(convert_secret_key_to_derived_key(secret_key))

def encrypt_msg(box, msg):
    binary_encoded_content = msg.encode()
    encrypted_content = box.encrypt(binary_encoded_content)
    assert len(encrypted_content) == len(binary_encoded_content) + box.NONCE_SIZE + box.MACBYTES
    return encrypted_content

def decrypt_msg(box, msg):
    return box.decrypt(msg, nonce=None).decode("ASCII")