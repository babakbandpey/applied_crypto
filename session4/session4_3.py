#!/usr/bin/python3

#***********************
# Session 4 Exercise 3
#***********************


from rsa_utils import encrypt, decrypt

private_key = 937
n = 2537
public_key = 13

a = 5
b = 15

res1 = encrypt(a, public_key, n) * encrypt(b, public_key, n)
res2 = encrypt(a*b, public_key, n)
print( res1 )
print( res2 )

print( decrypt(res1, private_key, n) )
print( decrypt(res2, private_key, n) )

if(decrypt(res1, private_key, n) == decrypt(res2, private_key, n)):
    print(" RSA is Malleable ")