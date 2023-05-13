#!/usr/bin/python3
def delete_at(my_list=None, idx=0):
    if my_list is None:
        my_list = []
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        for i in range(len(my_list)):
            if i == idx:
                my_list.remove(my_list[i])
                return (my_list)
