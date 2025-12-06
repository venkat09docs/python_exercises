# JSON HANDLING FOR STRUCTURED DATA

import json # Importing the JSON module

# Reading and parsing a JSON file
with open('config.json', 'r') as csvfile:
    config = json.load(csvfile) # Load JSON content into a Python dictionary

# Print the raw JSON data as a dictionary
print(config)

# Formatting JSON for better readability
dict_json = json.dumps(config, indent=4)    # Convert dictionary to a formatted JSON string
print(dict_json)

print(config['api_settings']['endpoint'])
print(config['default_parameters']['temperature'])



