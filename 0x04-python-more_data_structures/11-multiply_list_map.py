#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    res = map((lambda i: i * number), my_list)
    return (list(res))
