# In this exercise x  and y  are two random variables.
# The code at the top of the file randomly assigns them (we'll learn how it works later on).
# For now, just leave it alone :)
#
# If both are positive numbers, print "both positive".
# If both are negative, print "both negative".
# Otherwise, tell us which one is positive and which one is negative, e.g. "x is positive and y is negative"
# The print statements are filled in for you, just add logic.

## BONUS: Create error statements if number is outside the range of 100 => -100
## (This scenario requires a change of the radint values to extend beyond the given numbers)

# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint  # |  \

x = randint(-120, 120)  # |   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-120, 120)  # |     NO TOUCHING!!!!!! (please)
y = randint(-120, 120)  # |    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-120, 120)  # |  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /


# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(x, y)

## Adding error handling for numbers beyond 100 or -100 first ##
def too_high_or_low(num1, num2):
    if num1 > 100 or num2 > 100:
        print(f'ERROR, {num1} and/or {num2} is out of bounds!')
        exit()
    elif num1 < -100 or num2 < -100:
        print(f'ERROR, {num1} and/or {num2} is out of bounds!')
        exit()
    else:
        pass

## Calling the function ##
too_high_or_low(x, y)

## If the error is not thrown, continue with the program ##
if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 > y:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
