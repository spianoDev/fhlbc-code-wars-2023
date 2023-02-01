# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.
#
# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return string * repeat

repeat_str(4, 'a') # => 'aaaa'
repeat_str(3, 'hello ') # => 'hello hello hello '
repeat_str(2, 'abc') # => 'abcabc'
