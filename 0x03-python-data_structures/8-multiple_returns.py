#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = ""
    if len(sentence) == 0:
        b = "None"
    else:
        b = sentence[0]
    Rtuple = (a, b)
    return Rtuple
