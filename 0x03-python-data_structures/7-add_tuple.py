#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements of each tuple (or use 0 if not present)
    a1, a2 = tuple_a[:2] + (0, 0)
    b1, b2 = tuple_b[:2] + (0, 0)

    # Perform addition and return the result as a tuple
    result_tuple = (a1 + b1, a2 + b2)
    return result_tuple
