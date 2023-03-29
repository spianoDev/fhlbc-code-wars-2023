# Given a mixed array of number and string representations of integers,
# add up the non-string integers and subtract the total of the string integers.
#
# Return as a number.

def div_con(x):
    answer = 0
    for item in x:
        if isinstance(item, int):
            answer += item
        else:
            answer -= int(item)
    print(answer)
    return answer

div_con([9, 3, '7', '3']) # => 2
div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]) # => 14
# div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']) # => 13
# div_con(['1', '5', '8', 8, 9, 9, 2, '3']) # => 11
# div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]) # => 61
