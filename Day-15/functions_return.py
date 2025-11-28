# THE return STATEMENT

# The `len()` function returns the length of a string
length = len('abc')
print(length)

# RETURNING VALUES FROM FUNCTIONS

def add(a,b):
    """Returns the sum of two numbers."""
    return a + b

# A function with no return statement
def func():
    """ Placeholder function, does nothing"""
    pass

def example_function():
    return 'This is the return value!'
    print('This line will never execute')

# Function Calls

# Storing the return value of `add()` in a variable
sum1 = add(10, 20)
print(sum1)

# Calling a function with no return value (returns None)
x = func()
print(x)    # Output: None

example_function() # This function returns a value but is not printed

def myfunc(x):
    """Returns multiple values: the input number, its square, and its cube."""
    return x, x ** 2, x ** 3, x ** 4

# Unpacking multiple returned values
a, b, c, d = myfunc(3)
print(a, b, c, d)

print(myfunc(2))