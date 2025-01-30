# Internal Workings
x = 10
y = x
# * NOTE: Here x and y are referencing same object in memory
print(f"x == {x}, y == {y}")
# x == 10, y == 10

# * NOTE: Here the memory references are automatically processed before any calculations
# x = 10 + 2
x = x + 2
# * NOTE: After this the x will reference another object in memory
# * so, eventually both x and y will reference seperate objects in memory
print(f"x == {x}, y == {y}")
# x == 12, y == 10


l1 = [1, 2, 3]
l2 = l1
# * NOTE: Here l1 and l2 are referencing same object in memory
print(f"l1: {l1}, l2: {l2}")
# l1: [1, 2, 3], l2: [1, 2, 3]

# * NOTE: Changing an element of l1
l1[0] = 100
print(f"l1: {l1}, l2: {l2}")
# l1: [100, 2, 3], l2: [100, 2, 3]
# * NOTE: Again both lists are referencing same object so both have same value


# * NOTE: Changing reference but keeping value same
l1 = [100, 2, 3]
print(f"l1: {l1}, l2: {l2}")
# l1: [100, 2, 3], l2: [100, 2, 3]
l1[0] = 321
print(f"l1: {l1}, l2: {l2}")
# l1: [321, 2, 3], l2: [100, 2, 3]
# * NOTE: Here values are same because we changed reference of l1


# * NOTE: For checking equality of values we can use "==" operator
# * For checking the equality of reference we can use "is" operator
list1 = ["a", "b"]
list2 = list1
# Checking equality of value and reference
print(list1 == list2)
# True
print(list1 is list2)
# True

# Change the reference for list1 while keeping the value same
list1 = ["a", "b"]
# Checking equality of value and reference
print(list1 == list2)
# True
print(list1 is list2)
# False
