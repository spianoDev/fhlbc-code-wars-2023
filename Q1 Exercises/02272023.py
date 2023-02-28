# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

for num in range(10, 20):
    if num % 2 == 1:
        x += num

print(x)


# Use a while loop to generate a random number between 1 and 10 until you get the number 5.
# Every time the loop runs, increment the variable i .


# Generate a random number between 1 and 10 using randint(1, 10) , storing the result in the number variable
# Write a while loop to keep regenerating a new random number between 1 and 10 while the random number is not equal to 5.
# In order for my tests to work, please add 1 to i  each time through the loop.
# My tests use this variable to check how many times your loops runs.

from random import randint
# use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration


while number != 5:
    number = randint(1, 10)
    print(number)
    i += 1

print(i)
