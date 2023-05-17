#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)
    m = 0
    for x in a_dictionary:
        if m < a_dictionary[x]:
            m = a_dictionary[x]
    for x in a_dictionary.keys():
        if a_dictionary[x] == m:
            return (x)
