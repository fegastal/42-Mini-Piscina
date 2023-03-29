#!/usr/bin/python3

def my_var():

    type_int = 42

    type_str_int = "42"

    type_str = "quarante-deux"

    type_float =  42.0

    type_bool = True

    type_list = [42]

    type_dict = {42:42}

    type_tuple = (42,)

    type_set = set()

    print(type_int, "has a type", type(type_int))
    print(type_str_int, "has a type", type(type_str_int))
    print(type_str, "has a type", type(type_str))
    print(type_float, "has a type", type(type_float))
    print(type_bool, "has a type", type(type_bool))
    print(type_list, "has a type", type(type_list))
    print(type_dict, "has a type", type(type_dict))
    print(type_tuple, "has a type", type(type_tuple))
    print(type_set, "has a type", type(type_set))

if __name__ == '__main__':
    my_var()