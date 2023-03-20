# When provided with a String, capitalize all vowels
#
# For example:
#
# Input : "Hello World!"
#
# Output : "HEllO WOrld!"
#
# Note: Y is not a vowel in this kata.
import re

def swap(st):
    new_st = st.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U')
    print(new_st)
    return new_st


# swap("HelloWorld!") # => "HEllOWOrld!"
# swap("Sunday") # => "SUndAy"
swap("Codewars") # => "COdEwArs"
swap("Monday") # => "MOndAy"
# swap("Friday") # => "FrIdAy"
# swap("abracadabra") # => "AbrAcAdAbrA"
