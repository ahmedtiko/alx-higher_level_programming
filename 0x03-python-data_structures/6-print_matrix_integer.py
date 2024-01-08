#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    if not matrix:
        return

    for row in matrix:
        for i, elem in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(elem), end="")
            else:
                print("{:d} ".format(elem), end="")
        print()  # Move to the next line after printing each row
