#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                result_list.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                print("wrong type")
                result_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except IndexError:
                print("ot of range")
                result_list.append(0)
    finally:
        return result_list
