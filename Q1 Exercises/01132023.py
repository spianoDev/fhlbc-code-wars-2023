## Exercise 1 ##
# It's your first Python code exercise! Starting out nice and easy :)
# Use print()  to tell us your name!

print('Sarah P')

## Exercise 2 ##
# Bank Robbery Money
# I just robbed a bank with some of my friends.
# We got away with $19,867,324,678,987.99, and now we have to split it up 5 ways.
# Using the cash  variable I've already defined for you, print out the dollar amount each robber gets to keep.
# (divide cash  by 5 and print the answer out)
# p.s. I haven't actually robbed a bank.  Yet.

cash = 19867324678987.99  # DON'T CHANGE THE CASH VARIABLE

split = round(cash/5, 2)
answer = "{:.2f}".format(split)
print(answer)
