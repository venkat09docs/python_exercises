# LAMBDA EXPRESSIONS

# Regular function equivalent

def add(a, b, c):
    """Returns the sum of three numbers."""
    return a + b + c

add(3,4,5)
# Syntax:
# lambda parameters: expression

# Lambda expression equivalent
s = (lambda a,b,c: a+b+c)(3,4,5)    # Directly calling the lambda function
print(s)

# Lambda function with a default parameter
square = lambda x=10: x ** 2
print(square(5))

friends = [('Diana Y', 30), ('Ana', 25), ('Tudor', 22)]

friends.sort(key=lambda x: x[1])
print(friends)

friends.sort(key=lambda x: len(x[0]))
print(friends)











