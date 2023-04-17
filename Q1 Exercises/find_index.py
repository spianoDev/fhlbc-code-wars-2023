# This was the last one from Q1 but not getting to it until mid April

# In this kata, you need to write a function that takes a string and a letter as input
# and then returns the index of the second occurrence of that letter in the string.
# If there is no such letter in the string, then the function should return -1.
# If the letter occurs only once in the string, then -1 should also be returned.
#
# Examples:
#
# second_symbol('Hello world!!!','l') --> 3
# second_symbol('Hello world!!!', 'A') --> -1

def second_symbol(s, symbol):
    try:
        print(s.index(symbol, s.index(symbol)+1))
        return s.index(symbol, s.index(symbol)+1)
    except:
        print(-1)
        return -1

# second_symbol('Hello world!!!','l') # => 3, 'Find the index of the second symbol "l" in the string'
# second_symbol('Hello world!!!', 'o') # => 7, 'Find the index of the second symbol "o" in the string'
second_symbol('Hello world!!!', 'A') # => -1, 'The symbol "A" is not in the string'
second_symbol('', 'q') # => -1, 'The symbol "q" is not in the string'
second_symbol('Hello', '!') # => -1, 'The symbol "!" is not in the string'
