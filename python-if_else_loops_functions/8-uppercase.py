#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if (ord(i) in range(ord('a'), ord('z') + 1)):
            res += (chr(ord(i) - 32))
        else:
            res += i
    print("{}".format(res))
