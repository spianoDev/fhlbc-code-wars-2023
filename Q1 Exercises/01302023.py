## Price of Mangoes ##

# There's a "3 for 2" (or "2+1" if you like) offer on mangoes.
# For a given quantity and price (per mango), calculate the total cost of the mangoes.
#
# Examples
# mango(2, 3) ==> 6    # 2 mangoes for $3 per unit = $6; no mango for free
# mango(3, 3) ==> 6    # 2 mangoes for $3 per unit = $6; +1 mango for free
# mango(5, 3) ==> 12   # 4 mangoes for $3 per unit = $12; +1 mango for free
# mango(9, 5) ==> 30   # 6 mangoes for $5 per unit = $30; +3 mangoes for free
import math

def mango(quantity, price):
    if quantity % 3 == 0 and quantity >= 6:
        total_to_buy = quantity - (quantity/3)
        print(int(total_to_buy))
        return total_to_buy * price
    elif quantity % 3 == 1 and quantity >= 5:
        total_to_buy = quantity - (quantity/3) + 1
        print(int(total_to_buy))
        return total_to_buy * price
    elif quantity % 3 == 2 and quantity >= 4:
        total_to_buy = quantity - (quantity/3) + 1
        print(int(total_to_buy))
        return total_to_buy * price
    elif quantity == 3:
        return 2 * price
    else:
        return quantity * price

## TESTS ##
# mango(2, 3) # => 6
# mango(3, 3) # => 6
# mango(9, 5) # => 30
mango(12, 5)
