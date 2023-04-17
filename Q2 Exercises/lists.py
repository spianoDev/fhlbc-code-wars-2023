# Defining and manipulating lists
# Exercise 14: Creating Lists
# make a list called 'my_stuff' that has at least 4 items with at least 1 string and 1 float
my_stuff = ['piano', '3 cats', '2 kids', 46.7, 'HS Graduate']

print(my_stuff)
# make a list called 'nums' that has all the numbers between 1 and 99
nums = []
for num in range(1, 100):
    nums.append(num)

print(nums)

# Exercise 15: Accessing List Data
# Update spelling 'Hanna' to 'Hannah', 'Geoffrey' to 'Jeffrey', and 'aparna' to 'Aparna'

people = ['Hanna', 'Louisa', 'Claudia', 'Angela', 'Geoffrey', 'aparna']

people[0] = 'Hannah'
people[4] = 'Jeffrey'
people[5] = people[5].capitalize()

print(people)

# Exercise 16: List Iteration
# Combine all strings in list and make them uppercase

sounds = ['super', 'cali', 'fragil', 'istic', 'expi', 'ali', 'docious']
result = []
for sound in sounds:
    result.append(sound.upper())
print(''.join(result))

# Exercise 17: Lists Basics
# Create a list called 'instructors' and add 'Colt', 'Blue', 'Lisa' to the list

instructors = []
instructors.append('Colt')
instructors.append('Blue')
instructors.append('Lisa')

print(instructors)

# It would be better to just initialize this list example with these three names
instructor_lst = ['Colt', 'Blue', 'Lisa']
