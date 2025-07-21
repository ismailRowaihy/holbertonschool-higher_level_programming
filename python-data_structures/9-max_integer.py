#!/usr/bin/python3
def max_integer(my_list=[]):
    is_max = 0
    for i in my_list:
        if i > is_max:
            is_max = i
    return(is_max)
