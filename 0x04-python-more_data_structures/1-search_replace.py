#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    for i in my_list:
        new_element = replace if i == search else i
        new_list.append(new_element)

    return new_list
