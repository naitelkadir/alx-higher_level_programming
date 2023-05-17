#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    s = 0
    res = 0
    for tup in my_list:
        res += tup[0] * tup[1]
        s += tup[1]
    return (res / s) 
