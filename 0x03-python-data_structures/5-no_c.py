#!/usr/bin/python3

def no_c(my_string):
    # Initialize an empty string to store the result
    result_string = ""

    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C' and append to result_string
        if char.lower() not in {'c', 'C'}:
            result_string += char

    return result_string
