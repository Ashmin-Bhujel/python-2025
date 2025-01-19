# Mutable behaviour in python
# * NOTE: Coming from JavaScript list is more like array and dictionary is more like object literal in Python
marks = [50, 68, 64, 52]
print(f"Before: {marks}")
# Before: [50, 68, 64, 52]

marks.append(56)
print(f"After: {marks}")
# After: [50, 68, 64, 52, 56]
