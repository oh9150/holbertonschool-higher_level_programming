#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if (i % 3 == 0):
            print("Fizz", end=" ")
        if (i % 5 == 0):
            print("Buzz", end=" ")
        if (i % 5 != 0 or i % 3 != 0):
            print("{}".format(i), end=" ")
