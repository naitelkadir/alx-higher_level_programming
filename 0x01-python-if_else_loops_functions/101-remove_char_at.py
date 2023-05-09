#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return (str)
    for i in range(0, len(str)):
        if i == n:
            new_str = str[:i] + str[i+1] + str[i+2:]
            return (new_str)
