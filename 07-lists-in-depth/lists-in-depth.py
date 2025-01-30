# Lists in Depth
# Slicing and dicing of lists
# * NOTE: We can do slicing same as we can do with strings
fruits = ["Apple", "Mango", "Grapes", "Papaya"]

fruits[0]
# Apple

fruits[:]
# ["Apple", "Mango", "Grapes", "Papaya"]

fruits[1:3]
# ["Mango", "Grapes"]

# * NOTE: We can use slicing in weird ways also
# Inserting element at index 1
fruits[1:1] = ["Strawberry"]
# ["Apple", "Strawberry", "Mango", "Grapes", "Papaya"]

# Removing element from index 1 to 3 (two elements)
fruits[1:3] = []
# ["Apple", "Grapes", "Papaya"]


# Loop with list
fruits = ["Apple", "Mango", "Grapes", "Papaya"]
for fruit in fruits:
    print(fruit)
# ["Apple", "Mango", "Grapes", "Papaya"]


# Conditional with list
if "Mango" in fruits:
    print("The list has Mango")
else:
    print("The list does not have Mango")


# Some useful methods
# * NOTE: Since lists are mutable these methods can change the original list

# append
# * NOTE: Adds new element at the end
fruits.append("Guava")
# ['Apple', 'Mango', 'Grapes', 'Papaya', 'Guava']

# pop
# * NOTE: Removes and returns the last element
last_fruit = fruits.pop()
print(last_fruit)
# Guava
print(fruits)
# ['Apple', 'Mango', 'Grapes', 'Papaya']

# remove
# * NOTE: Remove specified element from the list
fruits.remove("Apple")
# ['Mango', 'Grapes', 'Papaya']

# insert
# * NOTE: Insert element at specified index
fruits.insert(1, "Guava")
# ['Mango', 'Guava', 'Grapes', 'Papaya']

# copy
# * NOTE: Returns a shallow copy (only upper level)
# * NOTE: To do deep copy we have to import deepcopy from copy module
fruits_copy = fruits.copy()
print(fruits_copy)
# ['Mango', 'Guava', 'Grapes', 'Papaya']


# List comprehension
# ? Kinda like loop inside list
# * NOTE: It created a list with numbers between 0 to 10
nums = [num for num in range(0, 10)]
print(nums)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
