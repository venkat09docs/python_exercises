# FUNCTION ARGUMENTS

# 5 TYPES OF FUNCTION ARGUMENTS:

# 1. **Positional Arguments** - Arguments that must be passed in the correct order.

def display_weather(temp, humidity, wind_speed):
    print(f'Temparature => {temp}C, Humidity => {humidity}%, wind Speed => {wind_speed}km/h')

# temp = 22 and humidity = 70
display_weather(22, 70, 30)

# 2. **Keyword (Named) Arguments** - Arguments that are explicitly named when passed.

# Using keyword arguments (order does not matter)
display_weather(humidity=70, temp=22, wind_speed=15)

display_weather(70, wind_speed=15, humidity=22)

# Mixing positional and keyword arguments (order still matters for positional)
display_weather(70, 15, wind_speed=22)

# ❌ This will cause a **SyntaxError**
# display_weather(humidity=70, 15, temp=22)  # Positional argument after keyword argument is not allowed

# 3. **Default Arguments** - Arguments that take a default value if not provided.

def adjust_lighting(room, brightness=75, color_temp=4000):
    """Adjusts lighting settings for a given room."""
    print(f'Adjusting lighting in {room} to {brightness}% brightness and {color_temp}K color temp.')

# Function calls with default values
adjust_lighting('Living Room')

adjust_lighting('Bedroom', 50)

adjust_lighting('Kitchen', 50, 3500)