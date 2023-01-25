# You will be provided with a random number in a variable called num .
#
# Use a conditional statement to check if the number is odd.
# If num  is odd, print "odd". Otherwise print "even".
#
# Hint: use modulus %  to figure out if the number is odd!

# NO TOUCHING ======================================
from random import randint
num = randint(1, 1000) #picks random number from 1-1000
# NO TOUCHING ======================================



# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

answer = True if (num % 2 == 1) else False

print(num, answer)

divided_by_five = True if (num % 5 == 0) else False
print(num, divided_by_five)

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
