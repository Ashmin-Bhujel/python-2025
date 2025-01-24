# Function Returning Multiple Values
# TODO: Create a function that returns both the area and circumference of a circle given its radius.
import math


def circle_stats(radius):
    area = round(math.pi * math.pow(radius, 2), 2)
    circumference = round(2 * math.pi * radius, 2)
    # ? I have never returned multiple values like this before, this was new
    return area, circumference


radius = 4
# * NOTE: This will return a tuple with value of area and circumference
area, circumference = circle_stats(radius)


print(f"Radius: {radius}")
print(f"Area: {area}")
print(f"Circumference: {circumference}")
