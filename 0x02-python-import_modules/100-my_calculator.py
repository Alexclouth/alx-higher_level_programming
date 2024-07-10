#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arg = sys.argv[1:]
    if len(arg) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(arg[0])
    b = int(arg[2])
    if len(arg) == 3:
        if arg[1] == '+':
            print("{} {} {} = {}".format(a, arg[1], b, add(a, b)))
        elif arg[1] == '-':
            print("{} {} {} = {}".format(a, arg[1], b, sub(a, b)))
        elif arg[1] == '*':
            print("{} {} {} = {}".format(a, arg[1], b, mul(a, b)))
        elif arg[1] == '/':
            print("{} {} {} = {}".format(a, arg[1], b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        sys.exit(0)
