#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = len(sys.argv) - 1
    s = 0
    for i in range(c):
        s = s + int(sys.argv[i + 1])
    print("{}".format(s))
