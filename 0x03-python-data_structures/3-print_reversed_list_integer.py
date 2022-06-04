#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list
    new_list.reverse()
    for i in new_list:
        print("{:d}".format(i))
    if len(new_list) == 0:
        print()
