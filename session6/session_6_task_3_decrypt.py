#!/usr/bin/python3

from nacl import pwhash, secret
from binascii import unhexlify


cipher_text = unhexlify("939e3de3b219e4207139d660e410ca9e6c7a6645f2a4f75861d7842984d77c018011b13228bbedf6445cb6ef5a8ae24a156882d52cee765ff59ff515f36e67ff960ea4c57c03d5ef494a66f4fa049bbe9ab47291")
password = "My secret password"
salt = unhexlify("9de8dedb65bb103e55ed203305968f43")


key = pwhash.argon2i.kdf(
    size=secret.SecretBox.KEY_SIZE,
    password=password.encode("UTF-8"),
    salt=salt
)

box = secret.SecretBox(key)

print(box.decrypt(cipher_text).decode("UTF-8"))

# Prints: Some people think technology has the answers