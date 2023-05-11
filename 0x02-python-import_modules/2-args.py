#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = len(sys.argv) - 1
    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 arguments")
    else:
        print("{} arguments".format(c))
        for i in range(1, c + 1):
            print("{}: {}".format(i, sys.argv[i]))
