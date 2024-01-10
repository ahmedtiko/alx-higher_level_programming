#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_set = set()

    # Iterate through the elements in the original list
    for element in my_list:
        # Add the element to the set (sets only store unique elements)
        unique_set.add(element)

    # Sum up the unique integers in the set
    result = sum(unique_set)

    return result
