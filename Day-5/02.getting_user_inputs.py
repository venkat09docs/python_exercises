# GETTING USER INPUT

# BASIC USER INPUT
# Prompt the user to ask a question
# command = input('Ask your AI assistant a question: ')
# print(command)

# USER INPUT RETURNS A STRING

# training_hours = int(input('Enter hours spent training the model: '))
# print(type(training_hours))

# CONVERTING USER INPUT TO NUMERIC TYPES

iterations = int(input('Enter the number of model iterations (integer): '))
datasets = int(input('Enter the number of datasets: '))

total = iterations * datasets
print('Total processing units:', total)


