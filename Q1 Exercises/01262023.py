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
from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /



# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(x, y)
if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
