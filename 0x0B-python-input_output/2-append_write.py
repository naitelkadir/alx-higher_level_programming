#!/usr/bin/python3
""" define a function that appends a string to a file"""

def append_write(filename="", text=""):
    """use with statement to append a string to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return (len(text))
