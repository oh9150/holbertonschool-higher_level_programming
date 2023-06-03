#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    if len(argv) != 0:
        print("{} argument".format(len(argv)), end="")
        if len(argv) > 1:
            print("s", end="")
        print(":")
        for i in range(1, len(argv) + 1):
            print("{}: {}".format(i, argv[i - 1]))
    else:
        print("{} arguments.".format(len(argv)))

