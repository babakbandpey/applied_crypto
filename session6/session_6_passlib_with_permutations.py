#!/usr/bin/python3

import passlib
from passlib.hash import sha512_crypt
import itertools


# having_shadow = "$6$O/yIOqMzCqpyFbng$FPPwWLu/uDXtb5nVYFJrQfga2lh5rpunYTRNCwxDV6YTFq7x1OISxyTYlRzpcu5VyF1gF9tSx2fCLa.nwkNLx."
# generated_shadow = sha512_crypt.using(salt="O/yIOqMzCqpyFbng", rounds=5000).hash("passw0rd")

# if having_shadow == generated_shadow:
#    print(generated_shadow + " is equal to " + having_shadow)
#else:
#    print(generated_shadow + " is wrong")



# chars = "abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ÆæØøÅå"
# the above chars can be used for a larger search
chars = "1234567890"

salt = "penguins"
password = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"

for arr in itertools.permutations(list(chars),r=3):
    perm = ''.join(arr)
    test = sha512_crypt.using(salt=salt, rounds=5000).hash(perm)
    if test == password:
        print("******************************")
        print("The password is %s" % perm)
        print("******************************")
        break

# The password is 479