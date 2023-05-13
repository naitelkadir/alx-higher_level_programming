#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    for i in range(2):
        if len(tuple_a) <= i or tuple_a[i] is None:
             new_tuple.append(tuple_b[i])
        elif len(tuple_b) <= i or tuple_b[i] is None:
             new_tuple.append(tuple_a[i])
        else:
             new_tuple.append(tuple_a[i] + tuple_b[i])
    return (new_tuple)
