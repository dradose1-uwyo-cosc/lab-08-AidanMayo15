# Aidan Mayo
# UWYO COSC 1010
# Submission Date
# Lab 08
# Lab Section:12
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert(value):
    if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
        return int(value)
    if value.count('.') == 1:
        left, right = value.split('.')
        if (left.isdigit() or (left.startswith('-') and left[1:].digit())) and right.isdigit():
            return float(value)
    return False

user_input = input("Input a number:")
result = convert(user_input)

if result is False:
    print("Input could not be converted")
else:
    print("The converted value is:", result)
        
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def function(m, x, b):
    return f"m={m}, x={x}, b={b}"
while True:
    m = input("Please enter a value for m or Type 'Exit' to exit to loop")
    if m.lower() == "Exit":
        break
    elif not m.isdigit():
        print("Please input a valid integer for m")

    x = input("Please enter a value for x or Type 'Exit' to exit to loop")
    if x.lower == "Exit":
        break
    elif not x.isdigit():
        print("Please input a valid integer for x")

    b = input("Please input a value for b or Type 'Exit' to exit to loop")
    if b.lower == "Exit":
        break
    elif not b.isdigit():
        break
m, x, b = int(m). int(x), int(b)
y = m * x + b
print(f"y = {y}")
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def function(a, b, c):
    return f"a={a}, b={b}, c={c}"
while True:
    a = input("Please enter a value for a or Type 'Exit' to exit to loop")
    if a.lower() == "Exit":
        break
    elif not a.isdigit():
        print("Please input a valid integer for a")

    b = input("Please enter a value for b or Type 'Exit' to exit to loop")
    if b.lower == "Exit":
        break
    elif not b.isdigit():
        print("Please input a valid integer for b")

    c = input("Please input a value for c or Type 'Exit' to exit to loop")
    if c.lower == "Exit":
        break
    elif not c.isdigit():
        break
a, b, c = int(a). int(b), int(c)
x1 = -{b}+**0.5 {b}**2 - 4*{a}*{c}
print(f"x = {x}")
