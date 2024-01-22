#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        printed_elements = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            printed_elements += 1
    except IndexError:
        pass  # Handle the case where x is greater than the length of my_list

    print()  # Add a new line after printing the elements
    return printed_elements
