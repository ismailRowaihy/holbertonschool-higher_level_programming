#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list.copy()
    for i in range(len(my_list)):
        if search in my_new_list:
            my_new_list[my_new_list.index(search)] = replace
        else:
            break
    return my_new_list
