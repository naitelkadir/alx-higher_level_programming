#!/usr/bin/python3
""" define a function that reads a text file and prints it to stdout"""

def read_file(filename=""):
    """use with statement to read the file.
    
    Args:
        filename(string): name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data)
