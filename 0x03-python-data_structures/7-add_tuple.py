#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    new_list = list(new_tuple)
    for i in range(2):
        if len(tuple_a) <= i or tuple_a[i] is None:
             new_list.append(tuple_b[i])
        elif len(tuple_b) <= i or tuple_b[i] is None:
             new_list.append(tuple_a[i])
        else:
             new_list.append(tuple_a[i] + tuple_b[i])
    new_tuple = tuple(new_list)
    return (new_tuple)
