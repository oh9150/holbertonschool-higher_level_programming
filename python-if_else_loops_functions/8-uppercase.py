#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = chr(ord(c) - 32)
        elif (ord(c) >= 65 and ord(c) <= 90):
            c = chr(c)
        print("{}".format(c), end="")
    print("")
