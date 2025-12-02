# VARIABLE SCOPE AND NAMESPACES

# BUILT-IN NAMESPACE EXAMPLE

# The `max` function is part of Python's built-in namespace
scores = [85, 90, 78, 92]
print(max(scores))

# GLOBAL NAMESPACE EXAMPLE

# A global variable defined at the module level

accuracy = 0.95

def report_accuracy():
    """Prints the accuracy of the model in percentage."""
    print(f'Model accuracy is {accuracy * 100}%')

print(accuracy)
report_accuracy()

# LOCAL NAMESPACE EXAMPLE

def count_tokens(text):
    """Returns the number of words (tokens) in a given text."""
    tokens = len(text.split()) # `tokens` exists only within this function
    return tokens

print(count_tokens('Python makes AI so accessible!'))

# print(tokens)   # NameError: name 'tokens' is not defined

# GLOBAL VARIABLE
accuracy = 0.85

def update_accuracy():
    """Updates the global variable `accuracy` inside the function."""
    global accuracy # Declaring accuracy as global to modify it
    accuracy = 0.90 # Updating the global variable
    print(f'Updated accuracy inside function: {accuracy}')

# Function call modifies the global variable
update_accuracy()
print(f'Accuracy outside function: {accuracy}')

def sum(values):
    print(values)

print(sum([1, 2, 3]))



