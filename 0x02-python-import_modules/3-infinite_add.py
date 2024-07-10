#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    summ = 0
    for i in arg:
        i = int(i)
        summ += i
    print(summ)
