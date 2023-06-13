# Exercise 30 #
# I've provided you with a start dictionary called inventory.
#
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
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
