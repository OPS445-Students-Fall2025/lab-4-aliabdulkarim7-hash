#!/usr/bin/env python3

dict_york = {
    'Address': '70 The Pond Rd',
    'City': 'Toronto',
    'Country': 'Canada',
    'Postal Code': 'M3J3M6',
    'Province': 'ON'
}

dict_newnham = {
    'Address': '1750 Finch Ave E',
    'City': 'Toronto',
    'Country': 'Canada',
    'Postal Code': 'M2J2X5',
    'Province': 'ON'
}

list_keys   = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # build dict using while loop
    d = {}
    i = 0
    while i < len(keys) and i < len(values):
        d[keys[i]] = values[i]
        i += 1
    return d

def shared_values(d1, d2):
    # values both dicts share
    return set(d1.values()) & set(d2.values())

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    print('Shared Values', shared_values(dict_york, dict_newnham))

