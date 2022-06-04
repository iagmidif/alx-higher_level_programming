#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_n = 0
        for n in my_list:
            if n > max_n:
                max_n = n
        return max_n
    return None
