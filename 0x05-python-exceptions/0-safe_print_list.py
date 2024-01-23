#!/usr/bin/python3
# A Function that prints x elements of a list.

def safe_print_list(my_list=[], x=0):
    i = 0
    for elem in my_list:
        i += 1
    try:
        for elem in range(x):
            print(f"{my_list[elem]}", end="")
        print()
        return(x)
    except IndexError:
        print()
        return(i)
