#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    addition = 0

    for i in range(args):
        addition += int(argv[i + 1])
    print("{}".format(addition))
