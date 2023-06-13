#!/usr/bin/python3
"""define a function that adds a line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing a specific string

    Args:
        filename(str):name of file
        search_string: searching string
        new_string: string to insert
    """
    txt = ""
    with open(filename) as fp:
        for line in fp:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, 'w') as f:
        f.write(txt)
