## Vowel Remover ##

# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
#
# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata
import re

def shortcut(s):
    no_a = re.sub('a', '', s)
    no_e = re.sub('e', '', no_a)
    no_i = re.sub('i', '', no_e)
    no_o = re.sub('o', '', no_i)
    no_u = re.sub('u', '', no_o)
    print(no_u)
    return no_u

shortcut('hello') # => 'hll'
shortcut('codewars') # => 'cdwrs'
shortcut('HELLO') # => 'HELLO'
