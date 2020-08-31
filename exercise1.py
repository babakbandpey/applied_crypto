#!/usr/bin/python3

print("###############################")
print("# Applied Crypto Exercise 1:  #")
print("###############################")
print("# Implementing Ceasar Wheel...#")
print("###############################")

# print("Indtast key value:")
shift = int(input("Indtast key value between 0 and 25: "))

action = int(input("Type 1 for encrypting or 0 for decrypt: "))

message = input("Type your text: ")

ceasar_encryp_dict = {}

for x in range(97, 123):
    if(x + shift > 122):
        encryptyed_value = chr(x - 26 + shift)
    else:
        encryptyed_value = chr(x+shift)

    ceasar_encryp_dict[chr(x)] = encryptyed_value

ceasar_decryp_dict = {}

for k, v in ceasar_encryp_dict.items():
    ceasar_decryp_dict[v] = k

#print(ceasar_encryp_dict)
#print(ceasar_decryp_dict)

if(action):
    for char in message:
        if(char == ' '):
            print(' ')
        else:
            print(ceasar_encryp_dict[char.lower()], end='')
    print("\n")
else:
    for char in message:
        if(char == ' '):
            print(' ')
        else:
            print(ceasar_decryp_dict[char.lower()], end='')
    print("\n")