#!/usr/bin/python3
def weight_average(my_list=[]):
    average = size = 0
    for item in my_list:
        average += item[0] * item[1]
        size += item[1]
    return average / size
