# Exercise 25
# Create a dictionary with three key pairs
user_info = {
    'Name': 'Sarah',
    'Title': 'Lead IT Engineer',
    'ERG': ['WERG', 'Culture & Community', 'Women in IT']
}

print(user_info)

# Exercise 26
# Create a variable called 'full_name' that uses the dictionary values to create the name
artist = {
    'first': 'Neil',
    'last': 'Young'
}
full_name = ''
for key, value in artist.items():
    full_name += value + ' '
print(full_name)

# Exercise 27
# Save the total donations in a variable

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# print(donations)

total_donations = 0
for value in donations.items():
    # print(value[1])
    total_donations += value[1]
print(total_donations)

# Exercise 28 Dictionary Access
# This code picks a random food item:
from random import choice
food = choice(['cheese pizza', 'quiche', 'morning bun', 'gummy bear', 'tea cake'])

bakery_stock = {
    'almond croissant': 12,
    'toffee cookie': 3,
    'morning bun': 1,
    'chocolate chunk cookie': 9,
    'tea cake': 25
}

# Exercise is to print out the inventory if it exists in the bakery stock

print(food)
if food in bakery_stock.keys():
    if bakery_stock[food] > 1:
        print(f'There are {bakery_stock[food]} {food}s left!')
    else:
        print(f'There is {bakery_stock[food]} {food} left!')
else:
    print('We don\'t make that!')
