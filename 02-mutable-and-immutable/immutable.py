# Immutable behaviour in python
# * NOTE: It creates an object in memory with integer value 6 and assigns its memory reference to x
x = 6

# * NOTE: It assigns the memory reference of that same object for y as well
y = x

# * NOTE: Here both x and y has same value
print(f"x == {x}, y == {y}")
# x == 6, y == 6

# * NOTE: It creates an new object in memory with integer value 8 and assigns its memory reference to x
x = 8

# * NOTE: Here the value of y is still 6 because it is referencing to memory reference of that same old object
print(f"x == {x}, y == {y}")
# x == 8, y == 6

# ? Kind of exception I guess...!
# * NOTE: It seems like the tuple is modified but actually the list inside the tuple is modified
random = ([0, 1, 1, 2], "Ashmin")
print(f"Before: {random}")
# Before: ([0, 1, 1, 2], 'Ashmin')

random[0].append(3)
print(f"After: {random}")
# After: ([0, 1, 1, 2, 3], 'Ashmin')
