#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':' or text[i] == '\n':
            print("\n")
            
