#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)

    is_max = my_list[0]

    for i in my_list:
        if i > is_max:
            is_max = i
    return(is_max)
