#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end=" ")
                printed_integers += 1
        except IndexError:
            break  # Stop if x is greater than the length of my_list

    print()  # Add a new line after printing the integers
    return printed_integers
