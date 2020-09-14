#!/usr/bin/python3

import time
import sys

explanation  = []

explanation.append("The Ransomware uses Symmetric encryption to encrypt the file, because it is faster.")
explanation.append("The Ransomware uses Asymmetric encryption to encrypt key which is used in the Symmetric encryption, and sends it to the Command and Control Center.")


while True:
    for line in explanation:
        for letter in line:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.1)
        print("\r")
    break