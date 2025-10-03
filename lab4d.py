#!/usr/bin/env python3

str1 = 'Hello World!!'
str2 = 'Seneca College'
num1 = 1500
num2 = 1.50

def first_five(s):
    return s[:5]

def last_seven(s):
    return s[-7:]

def middle_number(n):
    s = str(n)
    return s[1:3]

def first_three_last_three(a, b):
    return a[:3] + b[-3:]

if __name__ == '__main__':
    print(first_five(str1))             # Hello
    print(first_five(str2))             # Senec
    print(last_seven(str1))             # World!!
    print(last_seven(str2))             # College
    print(middle_number(num1))          # 50
    print(middle_number(num2))          # .5
    print(first_three_last_three(str1, str2))  # Helege
    print(first_three_last_three(str2, str1))  # Send!!
