#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = chr(c - 32)
            strn += c
        elif (ord(c) >= 65 and ord(c) <= 90):
            c = chr(c)
            strn += chr(c)
    print("{}".format(strn))
