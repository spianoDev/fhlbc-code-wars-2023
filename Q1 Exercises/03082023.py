# Complete the solution so that it reverses the string passed into it.
#
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    reversed_string = ''
    for char in string[::-1]:
        reversed_string = reversed_string + char
    print(reversed_string)
    return reversed_string

solution('world') # => 'dlrow'
solution('hello') # => 'olleh'
solution('') # => ''
solution('h') # => 'h'
