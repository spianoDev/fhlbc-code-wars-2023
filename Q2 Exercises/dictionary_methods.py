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
