#!/usr/bin/python3

# Question 1:
# Decryption AES MODE CTR
# key = "WXvqxbAEEM08snXbYgu8bg=="
# nonce = "DevkI2Qzzfk="
# ciphertext = "aKmPJu6AbYlb/CGADkvPnpVZ6pK29SxH85kXfY58J3p9GRE5e2wr1FUMsSD812NiMVa9b0rZhtxvF0/0QEzyiSCSuATW"


from base64 import b64decode
from Crypto.Cipher import AES

key = "WXvqxbAEEM08snXbYgu8bg=="
nonce = "DevkI2Qzzfk="
ciphertext = "aKmPJu6AbYlb/CGADkvPnpVZ6pK29SxH85kXfY58J3p9GRE5e2wr1FUMsSD812NiMVa9b0rZhtxvF0/0QEzyiSCSuATW"

cipher = AES.new(b64decode(key), AES.MODE_CTR, nonce=b64decode(nonce))

print(cipher.decrypt(b64decode(ciphertext)).decode("ascii"))

# https://youtu.be/T3KFrtcupfc
# Question 2: CTR blocks contain 128 bits, or less and CTR does not use padding because it uses counter
# Question 3: The counter would start at 00