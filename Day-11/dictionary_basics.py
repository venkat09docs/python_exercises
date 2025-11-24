# DICTIONARY BASICS

# Creating a dictionary with various key types
model_config = {
    'model_name': 'GPT-4', # String key
    'layers': 48,
    'parameters': '200B',
    (1,2): 0.7      # tuple key
}

print(model_config)
print(type(model_config))

# Dictionary storing hyperparameter settings
hyperparameters = {
    'learning_rate': 0.0001,
    'dropout_rate': 0.3,
    'optimizer': 'Adam'
}

print(hyperparameters)
print(hyperparameters['optimizer'])

print(hyperparameters.get('optimize', 'Key Not Available'))

# Updating the Value
hyperparameters['dropout_rate'] = 0.5
print(hyperparameters)

# ADDING A NEW KEY-VALUE PAIR

# Adding batch_size to hyperparameters
hyperparameters['batch_size'] = 64
print(hyperparameters)

hyperparameters['batch_size'] = 78

# BEST PRACTICES FOR DICTIONARIES

# 1. Stick to **immutable keys** (e.g., strings, numbers, tuples)
# 2. Avoid **duplicate keys** (last assigned value will override)
# 3. Use **.get()** for safe access to prevent errors

# NESTED DICTIONARIES

# A dictionary storing configuration settings for different models
pipeline_config = {
    'GPT-4': {'layers': 48, 'parameters': '175B', 'attention_heads': 96},
    'BERT': {'layers': 24, 'parameters': '345M', 'attention_heads': 16}
}

print(dict((pipeline_config.get('GPT-4', 'No Model'))).get('parameters', 'No Key'))
print(pipeline_config['BERT']['parameters'])













