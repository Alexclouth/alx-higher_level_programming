#!/usr/bin/python3
def islower(c):
    c = str(c)
    char1 = ord(c)
    if char1 > 96 and char1 < 124:
        return True
    else:
        return False
