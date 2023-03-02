## Fix the Loop! ##
# from Code Wars https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd/train/python

# Your collegue wrote an simple loop to list his favourite animals.
# But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)
#
# If you pass the list of your favourite animals to the function,
# you should get the list of the animals with orderings and newlines added.
#
# For example, passing in:
#
#     animals = [ 'dog', 'cat', 'elephant' ]
# will result in:
#
# list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'

## Given this to correct ##
# def list_animals(animals):
#     list = ''
#     for i in range(animals):
#         list += str(i + 1) + '. ' + animals[i] + '\n'
#     return list

## Answer ##
def list_animals(animals):
    list = ''
    for i in enumerate(animals):
        print(i)
        list += str(i[0] + 1) + '. ' + i[1] + '\n'
    print(list)
    return list

animals = [ 'dog', 'cat', 'elephant' ]

list_animals(animals) # => '1. dog\n2. cat\n3. elephant\n'
