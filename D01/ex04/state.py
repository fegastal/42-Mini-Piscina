#!/usr/bin/python3

import sys

def my_dictionaries():

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    if verify_exists(capital_cities) == True:
        # anacrônimo (OR) vai receber o valor da chave do valor recebido
        anacronym = get_key_capital(capital_cities, sys.argv[1])
        # resultado vai receber o valor da chave do anacrônimo em states
        result = get_key_states(states, anacronym)
        print(result)
    else:
        print("Unknown capital city")

def get_key_states(states, anacronym):
    for key, value in states.items():
        if anacronym == value:
            return(key)

def get_key_capital(capital_cities, input_user):
    for key, value in capital_cities.items():
        if input_user == value:
            return(key)

def verify_exists(capital_cities):

    valid = False

    if len(sys.argv) != 2:
        sys.exit()
    for key, value in capital_cities.items():
        if(sys.argv[1]) == value:
            valid = True
    return(valid)

if __name__ == '__main__':
    my_dictionaries()