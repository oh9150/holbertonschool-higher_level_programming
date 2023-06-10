#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not isinstance(my_list, list):
        return None
    new_list = my_list.copy()
    for element in new_list:
        if element == search:
            element = replace
    return new_list
