# Tuples in Depth
# Slicing and dicing of tuples
nums = (0, 1, 2, 3)
print(nums[2])
# 2

print(nums[1:3])
# (1, 2)

print(nums[:])
# (0, 1, 2, 3)


# Loop with tuple
for num in nums:
    print(num)
# 0
# 1
# 2
# 3


# Conditional with tuple
if 4 in nums:
    print("There is number 4")
else:
    print("There is no number 4")
# There is no number 4


# Combining to tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)
# OR
# * NOTE: "*" can be used to spread the iterable objects
print((*t1, *t2))
# (1, 2, 3, 4, 5, 6)


# Unwrapping of tuple
ages = (21, 23, 22)
# * NOTE: Here at the left hand side the given elements will be treated as new variables
# * And the value are assigned from the right hand side tuple
# * Also, we can use the "*" to capture the remaining values
(john_age, *remaining) = ages
print(john_age, remaining)
# 21 23 22
