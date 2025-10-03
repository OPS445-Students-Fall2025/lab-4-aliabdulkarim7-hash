#!/usr/bin/env python3

def is_digits(sobj):
    # go through each character in the string
    for ch in sobj:
        if ch not in '0123456789':   # if not a digit
            return False
    return True   # all were digits

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, "is an integer.")
        else:
            print(item, "is not an integer.")

