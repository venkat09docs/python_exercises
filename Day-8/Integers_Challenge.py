'''

Challenge #1

Declare variables of the following types: int, float, bool, string, and list.

Print each variable along with its type in the terminal.
'''

year = 2026  # int
price = 99.99  # float
is_available = True  # bool
product_name = "Laptop"  # string
features = ["Touchscreen", "Backlit Keyboard", "SSD"]  # list

print(type(year), year)
print(type(price), price)
print(type(is_available), is_available)
print(type(product_name), product_name)
print(type(features), features)

'''
Challenge #2

Refactor the below script to follow Python's naming and style conventions as described in PEP 8.

varOne=10
varTwo=20

"""
This is 
an example of a multiline
comment in Python.
"""

str='Hello'
print(str)
'''

# Refactored code following PEP 8 naming and style conventions

# snake_case notation
var_one= 10
var_two= 20


# This is
# an example of a multiline
# comment in Python.


my_str = 'Hello'
print(my_str)

'''
Challenge #3

The given script contains syntax errors. Fix them so the script runs without errors.

# This script contains some syntax errors.
# Modify the script so that it runs without any errors.

best_friend = 'Anne"
print('My best friend is ', best_friend)

my-value = 15

age = 18
print(age = 10)

a, 4b = '10', '20'
print(a + 4b)

print('To comment a line of code you # at the beginning of the line.'#)
'''

best_friend = 'Anne'
print('My best friend is ', best_friend)

my_value = 15

age = 18
print(age == 10)

a, b4 = '10', '20'
print(a + b4)

print('To comment a line of code you # at the beginning of the line.')

'''
Challenge #4

Create a Python script that uses the following operators: =, ==, >=, *, **, /, //, %, +=, and *=.
'''

# Using different Python operators

x = 10
y = 3

result1 = x == y  # Equality
result2 = x >= y  # Greater than or equal
result3 = x * y  # Multiplication
result4 = x ** y  # Exponentiation
result5 = x / y  # Division (float)
result6 = x // y  # Floor division
result7 = x % y  # Modulus

x += 5  # Increment x by 5
y *= 2  # Multiply y by 2

print(result1, result2, result3, result4, result5, result6, result7)
print(x, y)

'''
Challenge #5

Given the expression:

a = 16 / 2 + 6 / 2 ** 2

Modify it by adding parentheses to change the order of operations so that a equals 1.0.
'''

a = 16 / ((2 + 6) / 2) ** 2
print(a)

'''
Challenge #6

An IPv6 address consists of 128 bits.
Write a Python script to calculate the total number of available IPv6 addresses, including reserved ones.
'''

# Calculate total IPv6 addresses (2^128)

total_ipv6_addresses = 2 ** 128
print(total_ipv6_addresses)