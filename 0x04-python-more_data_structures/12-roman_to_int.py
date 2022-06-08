#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    pre = 0
    if isinstance(roman_string, str) and roman_string is not None:
        for i in range(len(roman_string) - 1, -1, -1):
            if romans[roman_string[i]] >= pre:
                num += romans[roman_string[i]]
            else:
                num -= romans[roman_string[i]]
            pre = romans[roman_string[i]]
    return num
