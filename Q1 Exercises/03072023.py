# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).
#
# For example,
#
# [True,  True,  True,  False,
#  True,  True,  True,  True ,
#  True,  False, True,  False,
#  True,  False, False, True ,
#  True,  True,  True,  True ,
#  False, False, True,  True]
# The correct answer would be 17.
#
# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    count = 0
    for yes in sheep:
        if yes:
            count += 1
        else:
            print('not a sheep')
    print(count)
    return count

array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True];

count_sheeps(array1)  # => 17
