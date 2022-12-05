#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        my_max = my_list[0]
        for num in my_list:
            if my_max < num:
                my_max = num
        return my_max
