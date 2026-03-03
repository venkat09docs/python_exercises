# List Basics

# Creating a list with different data types
sample_list = [42, 3.14, 'GPT-4', True]

# Another list with mixed data types my data
my_data = [1, 0.5, 'tokenizer', False]

# Creating empty lists
empty_list1 = []
empty_list2 = list()

# Accessing list elements
print(my_data[2])
print(my_data[1])
print(my_data[-2])

# IndexError example
# print(my_data[5])

# List - mutable
print(id(my_data))
# Modifying a list element
my_data[2] = "Language Model"
print(id(my_data))

# Adding an element to the list
my_data.append("NLP")
my_data.append("LLM")
print(my_data)

# Getting the length of the list
print(len(my_data))

# Nested lists (2D lists)
matrix = [
    [1, 2, [3, 10]],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element inside a nested list
print(matrix[0][2][1])
