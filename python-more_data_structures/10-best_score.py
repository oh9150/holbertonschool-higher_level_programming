#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    key = list(a_dictionary.keys())[0]
    val = a_dictionary[key]
    for k, v in a_dictionary.items():
        if v > val:
            val = v
            key = k
    return key
