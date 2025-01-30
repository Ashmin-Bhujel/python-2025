# Numbers in Depth
# Integer
x = 10
# * NOTE: We can convert given string integer into integer using int wrapper if possible
int("123")
# 123

# Float
pi = 3.1415
# * NOTE: We can convert given string or integer into floating point number using float wrapper if possible
float(4)
# 4.0


# Different base numbers
# binary = 2 (Decimal Value)
binary = 0b010

# octal = 8 (Decimal Value)
octal = 0o10

# hexa = 16 (Decimal Value)
hexa = 0x10


# Number conversion from different bases to decimal
# * NOTE: They returns integer value
# Binary to Decimal
int("0b111", 2)
# 7

# Octal to Decimal
int("0o123", 8)
# 83

# Hexa to Decimal
int("0xff", 16)
# 255


# Number conversion from decimal to different bases
# * NOTE: They returns value in the form of string
# To Binary
bin(5)
# "0b101"

# To Octal
oct(21)
# "0o25"

# To Hexa
hex(123)
# "0x7b"


# Some useful modules to work with numbers
# math module
import math

# floor
math.floor(3.65)
# 3
math.floor(-3.65)
# -4

# ceil
math.ceil(2.42)
# 3
math.ceil(-2.42)
# -2

# trunc
math.trunc(1.25)
# 1
math.trunc(-1.25)
# -1


# random module
import random

# Generate a random floating point number between 0 and 1
random.random()

# Generate a random integer number between 0 and 10
random.randint(0, 10)

# * NOTE: random can also be used to choose an element from list
fruits = ["Apple", "Banana", "Orange"]
random.choice(fruits)

# * NOTE: It can also be used for shuffling the list
random.shuffle(fruits)


# Working with decimals
x = (0.1 + 0.1 + 0.1) - 0.2
# ? x is assigned an unsual number the actual number should be 0.1
# 0.10000000000000003

# We need to use Decimal wrapper from decimal module
from decimal import Decimal

# Now using Decimal Wrapper
x = (Decimal("0.1") + Decimal("0.1") + Decimal("0.1")) - Decimal("0.2")
# Decimal('0.1')


# Sets
a = {1, 2, 3}
b = {3, 4, 5}

# Union
a | b
# {1, 2, 3, 4, 5}

# Intersection
a & b

# Difference
a - b
# {1, 2}
b - a
# {4, 5}

# * NOTE: The empty set is represented by set() not {}


# True and False as 1 and 0
# * NOTE: Internally True and False are represented as 1 and 0 respectively
True == 1
# True

False == 0
# True

(True + True) * 4
# (1 + 1) * 4
# 2 * 4
# 8
