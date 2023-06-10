#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    retval = 0
    for i in range(x - 1):
        try:
            print("{:d}".format(my_list[i]), end="")
            retval += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print("")
    return retval
