# Variables

# Assigning a numeric value to a variable
celsius_temp = 30
print(celsius_temp)  # Output: 30

# Assigning multiple variables in a single line
temperature, user_age, c = 1, 2, 3

# Another example of multiple assignments
age, name = 28, 'Alice'

# Printing variables to confirm assignment
print(temperature, user_age, c)  # Output: 1 2 3
print(age, name)  # Output: 28 Alice


# Comments

# Calculate the area of a circle given the radius
radius = 5
area = 3.1416 * radius ** 2

# Example of commented-out code (useful for debugging or reference)
total = sum([1, 2, 3])
print(total)
print(max([5, 6, 1, -2]))


'''
Example of a multi-line comment (docstring style),
typically used for docstrings.

temp = preprocess_data(raw_input)
model.train(temp)
'''
print(total)

# BEST PRACTICES FOR WRITING COMMENTS

# 1. Be Clear and Concise

# Bad comment: Too vague, doesn't add value
# increment
# counter += 1

# Good comment: Clearly explains the purpose
# Increment the counter to track the number of iterations
# counter += 1

# 2. Explain the "Why", Not Just the "What"

# Bad comment: States the obvious
# Set is_active to True
# is_active = True

# Good comment: Provides context on why the value is set
# Activate the user account after email verification
is_active = True

# 3. Keep Comments Up-to-Date
# (Reminder: Ensure comments reflect the latest code logic)

# 4. Avoid Obvious Comments

# Bad comment: The code itself is self-explanatory
# Assign 5 to x
x = 5

# Naming Conventions in Python (PEP 8)

# -----------------------------
# 1. Allowed Characters (a-z, A-Z, 0-9, and _)
# -----------------------------

total_count = 100 # ✅ Valid: Uses letters and underscore
_hidden_value = 42 # ✅ Valid: Leading underscore implies a "private" variable (not enforced)

# 1st_place = 'Gold' # ❌ Invalid: Cannot start with a digit

# -----------------------------
# 2. Avoid Leading Underscores (Except for Private/Internal Use in Classes)
# -----------------------------

# _variable: Often used as a convention to indicate "internal use" (not enforced)

# -----------------------------
# 3. No Special Characters or Spaces (!, %, @, ?, ., etc.)
# -----------------------------

# user-name = 'Alice' # ❌ Invalid: Hyphens are not allowed
# user name = 'Bob' # ❌ Invalid: Spaces are not allowed

# -----------------------------
# 4. Reserved Words (if, else, while, for, etc.)
# -----------------------------

# if = 10 # ❌ Invalid: Cannot use Python keywords as variable names

# -----------------------------
# 5. Case Sensitivity
# -----------------------------

Max_value = 100
max_value = 200

print(Max_value)
print(max_value)

# -----------------------------
# 6. Use Descriptive Names and snake_case (Recommended)
# -----------------------------

max_value = 99 # ✅ Descriptive and uses snake_case
maxValue = 100  # ❌ Not recommended in Python (CamelCase is for class names)

# -----------------------------
# 7. Don't Shadow Built-in Names
# -----------------------------

list = [1, 2, 3] # ❌ Not recommended: Shadows the built-in list() function

# -----------------------------
# 8. Constants (Use ALL_CAPS)
# -----------------------------

PI = 3.1416
DAYS_IN_YEAR = 365
MAX_CONNECTIONS = 10










