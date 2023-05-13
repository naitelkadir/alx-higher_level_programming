#!/usr/bin/python3
def no_c(my_string):
    table = {ord("c"): None, ord("C"): None}
    new_string = my_string.translate(table)
    return (new_string)
