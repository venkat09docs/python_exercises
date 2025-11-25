# [ n for n in name ]
# [n for n in nums if cond]

# SET AND DICTIONARY COMPREHENSIONS

# SET COMPREHENSIONS

names = {'alice', 'BOB', 'charlie', 'DAVE'}

# Convert all names to capitalize first letter, ensuring consistent formatting
# n.capitalize() for n in name
formatted_names = { name.capitalize() for name in names }
print(formatted_names)

# DICTIONARY COMPREHENSIONS

hyperparams = {'layers': 3, 'units': 256, 'dropout': 0.2}

# Create a new dictionary where all values are doubled
new_hyperparams = { key: value * 2 for key, value in hyperparams.items() }
print(new_hyperparams)

# Create a set of keys (in uppercase) where values are greater than 0.2
new_dict = { key.upper() for key,values in hyperparams.items() if values > 0.2}
print(new_dict)

# DICTIONARY CREATION USING zip()
years = [2020, 2021, 2022]
dataset_sizes = [10000, 25000, 50000]

# Convert paired elements into dictionary mapping years to dataset sizes
data_growth = dict(zip(years, dataset_sizes))
print(data_growth)

sales = {2022: 50000, 2023: 75000, 2024: 100000}

# Calculate profit as 15% of revenue for each year
profit = { key: value * (15/100) for key,value in sales.items()}
print(profit)