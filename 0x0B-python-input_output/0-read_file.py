#!/usr/bin/python3
""" define a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """use with statement to read the file."""
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
