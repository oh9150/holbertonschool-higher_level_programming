#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    for item in my_list:
        average += item[0] * item[1]
    average /= my_list.sum()
    return average
