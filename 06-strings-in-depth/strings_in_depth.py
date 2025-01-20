# Strings in Depth
# Slicing and dicing of strings
nums = "0123456789"

# Get first character
nums[0]

# Get characters between 0 to 5
nums[0:5]
# OR
nums[:5]
# 01234

# Get all characters
nums[:]
# 0123456789

# Hoping
# * Note: Below example skips every two in between characters while hoping
nums[::3]
# 0369

# Use of negative value
# * NOTE: Negative number starts counting from end
nums[-1]


# Some useful methods
# * NOTE: These methods do not change the actual string rather they create a copy
username = "Ashmin"

# lower
# * Note: Converts all letters to lowercase
username.lower()
# ashmin

# upper
# * Note: Converts all letters to uppercase
username.upper()
# ASHMIN

# strip
username = "    Ashmin    "
# * NOTE: strip method removes extra whitespace around the string
username.strip()
# Ashmin

# replace
# * NOTE: It replaces the specified substring with the given new string
username = "Ashim Bhujel"
username.replace("Ashim", "Ashmin")
# Ashmin Bhujel

# split
# * NOTE: split method returns a list, It uses the space as separator by default or we can specify another seperator
fruits = "Apple, Banana, Orange"
fruits.split(", ")
# ["Apple", "Banana", "Orange"]

# find
# * NOTE: find method returns the index of first occurence of the specified string
random_str = "Hi, Hello, Namaste"
random_str.find("e")
# 5

# join
# * NOTE: join method converts the given list into a string using specified seperator
date = ["2025", "01", "20"]
"-".join(date)
# 2025-01-20

# format
# * NOTE: format method replaces placeholders "{}" with the specified value in order
username = "Ashmin"
age = 21
info = "Your name is {} and you are {} years old."
info.format(username, age)
# Your name is Ashmin and you are 21 years old.


# Formatted string
# * NOTE: With formatted string we can write a valid python expression inside the palceholders {}
x = 2
y = 5
f"{x} + {y} = {x + y}"
# 2 + 5 = 7


# "in" operator
# * NOTE: We can check if the string includes the specified substring or not
"Apple" in "Apple, Ball, Cat"
# True
"Dog" in "Apple, Ball, Cat"
# False
