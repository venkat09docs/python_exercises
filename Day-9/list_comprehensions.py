# LIST COMPREHENSIONS

# Doubling values using a traditional for loop
clicks = [10, 5, 15, 20, 5]
double_clicks = []

for item in clicks:
    double_clicks.append(item * 2)

print(double_clicks)

# [expression for item in list if condition]
double_clicks1 = [ item * 2 for item in clicks]
print(double_clicks1)

contributors = ['alice', 'Bob', 'CHARLIE']  # Output: ['Alice', 'Bob', 'Charlie']
con_cap = [item.capitalize() for item in contributors]
print(con_cap)

nums = [1, 7, 8, 14, 21, 30, 50] # Output: [7, 14, 21]
nums_divide_by_7 = [ n for n in nums if n % 7 == 0 ]
print(nums_divide_by_7)

# Finding shared skills between two teams # Output: ['Alice', 'Charlie']
ai_team = ['Alice', 'Bob', 'Charlie']
data_team = ['Alice', 'David', 'Charlie']

shared_skills = [team_member for team_member in ai_team if team_member in data_team]
print(shared_skills)



