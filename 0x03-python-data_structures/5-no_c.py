#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    i = 0
    while i < len(new_string):
        if new_string[i] in "cC":
            new_string = new_string[:i] + new_string[(i+1):]
            continue
        i += 1
    return new_string
