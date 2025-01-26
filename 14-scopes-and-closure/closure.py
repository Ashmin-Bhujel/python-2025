# Closure
# * NOTE: Here we are defining a child function inside the parent function and returning the child function from parent
def parent(power):
    def child(base):
        return base**power

    return child


# * NOTE: When the parent function is called a argument is passed for the power
# * That value of power will also come with the child function when the child function is returned
square = parent(2)
cube = parent(3)


# * NOTE: So, when will call the new functions square and cube with the same argument value 4 they will return
# * Different value according the value of power associated with them
print(f"Square of 4 is {square(4)}")
print(f"Cube of 4 is {cube(4)}")
