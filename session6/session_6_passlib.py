#!/usr/bin/python3

import passlib
from passlib.hash import sha512_crypt

# having_shadow = "$6$O/yIOqMzCqpyFbng$FPPwWLu/uDXtb5nVYFJrQfga2lh5rpunYTRNCwxDV6YTFq7x1OISxyTYlRzpcu5VyF1gF9tSx2fCLa.nwkNLx."
# generated_shadow = sha512_crypt.using(salt="O/yIOqMzCqpyFbng", rounds=5000).hash("passw0rd")

# if having_shadow == generated_shadow:
#    print(generated_shadow + " is equal to " + having_shadow)
#else:
#    print(generated_shadow + " is wrong")

# chars = "abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ÆæØøÅå"
chars = "1234567890"

def crack(max_depth = 3, target_depth = 3, current_depth=1, word=""):
    result = ""
    if current_depth > max_depth:
        return ""
    for c in chars:
        if(target_depth == current_depth):
            test = sha512_crypt.using(salt=salt, rounds=5000).hash(word+c)
            if test == password:
                return word+c
        else:
            result = crack(max_depth, target_depth, current_depth+1, word + c)
            if(result != ""):
                break
    return result
            
salt = "penguins"
password = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"  
print("******************************")
print("The password is: %s" % crack())
print("******************************")

# The password is 479