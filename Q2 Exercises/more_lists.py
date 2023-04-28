# Exercise 21: Another List Comp Exercise

# Create a list for all numbers between 1 and 100 (inclusive) that has all numbers divisible by 12.

divs_twelve = [num for num in range(1, 101) if num % 12 == 0]

print(divs_twelve)

# Exercise 22: List Exercise 4

# Create a list from the string 'amazing' with all the letters except vowels [a, e, i, o, u]
vowels = ['a', 'e', 'i', 'o', 'u']
no_vowels = [char for char in 'amazing' if char not in vowels]

print(no_vowels)

# Exercise 23: List Exercise 5

# Using nested lists create a list of lists that repeat the length of the original list [0,1,2]

nests_and_lengths = len(range(3)) * [list(item for item in range(3))]
print(nests_and_lengths)

# Exerise 24: One more Nested List (essentially the same as above but with a dynamic function)

def matrix(lst_length):
    return len(range(lst_length)) * [list(num for num in range(lst_length))]


print(matrix(8))
