import re

ceasar_encryp_dict = {}
ceasar_decryp_dict = {}


def populate_encrypt_dict(shift):

    for x in range(97, 123):
        if(x + shift > 122):
            encrypted_value = chr(x - 26 + shift)
        else:
            encrypted_value = chr(x+shift)

        ceasar_encryp_dict[chr(x)] = encrypted_value

    for x in range(65, 91):
        if(x + shift > 90):
            encrypted_value = chr(x - 26 + shift)
        else:
            encrypted_value = chr(x+shift)

        ceasar_encryp_dict[chr(x)] = encrypted_value
    
def populate_decrypt_dict(shift):
    populate_encrypt_dict(shift)
    for k, v in ceasar_encryp_dict.items():
        ceasar_decryp_dict[v] = k

def encrypt(message):
    cipher = ""
    
    for char in message:
        if text_match(char) == None:
            cipher += char
        else:
            cipher += ceasar_encryp_dict[char]
    return cipher

def decrypt(message):
    decipher = ""
    for char in message:
        if text_match(char) == None:
            decipher += char
        else:
            decipher += ceasar_decryp_dict[char]
    return decipher

def text_match(char):
    return re.search('^[a-zA-Z]*$', char)