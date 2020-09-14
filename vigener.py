#!/usr/bin/python3

# eoqcqiwlkbnshkdcuciftsdokbjxjsymisqitsfmrvhv

cipher = input("Type the encrypted text: ")
key = input("Type the key: ")

cipher_len = len(cipher)
key_len = len(key)

key_string = ""

for x in range(0, int(cipher_len / key_len)):
    key_string += key

for index in range(0, cipher_len % key_len):
    key_string += key[index]


alpha_index = {}
i = 0
for x in range(97, 123):
    alpha_index[chr(x)] = i
    i += 1

decipher = ""
for position in range(0, cipher_len):
    decipher += chr(97 + (alpha_index[cipher[position]] - alpha_index[key_string[position]])%26 )

print(decipher)