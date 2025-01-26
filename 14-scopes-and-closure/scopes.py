# Scopes
# Global scope
my_num = 21


# * NOTE: the function print_my_num can access the variable declared in global scope
def print_my_num():
    print(f"My Num: {my_num}")


print_my_num()


# Function scope
another_num = 6


# * NOTE: Inside the function print_another_num we have declared seperate local variable another_num
# * So, Despite having a variable with the same name (another_num) in global scope
# * this function will print the value of variable declared inside its scope
def print_another_num():
    another_num = 8
    print(f"Another Num: {another_num}")


print_another_num()


# Climbing up the scope
bank_balance = 12345678


# * NOTE: Inside the function grand_father there are other two functions defined inside and when the function is called
# * The functions inside will climb up to the scope where it can find the variable they are referencing to
# * in this case the global scope is where they find the variable bank balance
def grand_father():
    def father():
        def son():
            print(f"Bank balance is {bank_balance}")

        son()

    father()


grand_father()
