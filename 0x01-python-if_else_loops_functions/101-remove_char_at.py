#!/usr/bin/python3
def remove_char_at(str, n):
    char = ''
    for i in range(len(str)):
        if i == n:
            char += ''
        else:
            char += str[i]
    return char
