#!/usr/bin/python3
""" define a function that writes a string to a text"""


def write_file(filename="", text=""):
    """use with statement to write a string to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return (len(text))
