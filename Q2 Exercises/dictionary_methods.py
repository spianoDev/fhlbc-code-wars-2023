# Exercise 30 #
# I've provided you with a start dictionary called inventory.
#
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}  # DON'T CHANGE THIS LINE!
#
# Follow the instructions found in the comments:
#
# 1. Make a copy of inventory  and save it to a variable called stock_list  using a dictionary method we've covered
#
# 2. Add the value 18 to stock_list  under the key "cookie"
#
# # 3. Remove 'cake' from stock_list  using a dictionary method we've learned

stock_list = inventory.copy()
print(stock_list)
stock_list.update({'cookie': 18})
print(stock_list)
stock_list.pop('cake')
print(stock_list)

# Exercise 31 #
# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"]
# create a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
# Save it to a variable called answer.

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = dict(zip(list1, list2))
print(answer)

# Exercise 32 #
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#
# Create a dictionary called person_info , that makes each first item in each list a key and the second item a
# corresponding value.
# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
person_info = {}

for info in person:
    person_info.update({info[0]: info[1]})

print(person_info)

# Exercise 33 #
# Create a dictionary with the key as a vowel in the alphabet and the value as 0.
# Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_values = dict.fromkeys(vowels, 0)
print(vowel_values)

# Exercise 34 #
# Every character has an ASCII code (basically, a number that represents it).
# Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code.
# For example:
#
# chr(65)  will return  'A'
# chr(66)  will return  'B'
# chr(90)  will return  'Z'
#
# Your task is to create dictionary that maps ASCII keys to their corresponding letters.
# Use a dictionary comprehension and chr() . Save the result to the answer variable.
# You only need to care about capital letters (65-90).
#
ascii_nums = list(range(65, 91))
ascii_dict = dict((i, chr(i)) for i in ascii_nums)
print(ascii_dict)

# Exercise 35 #
# 1 - Create a variable called numbers which is a tuple with the values 1, 2, 3 and 4 inside.
num_range = range(1, 5)
numbers = tuple(num_range)
print(numbers)
# 2 - Create a variable called value which is a tuple with the value 1 inside.
single_range = range(1, 2)
value = tuple(single_range)

# 3 - Given the following variable:
values = [10, 20, 30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 4 - Given the following variable

stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)
print(unique_stuff)
