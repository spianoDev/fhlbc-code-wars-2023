# Introduction
#
# As a programmer, one must be familiar with the usage of iterative statements in coding implementations!
# Depending on the chosen programming language, iterative statements can come in the form of for, while, do-while etc.
#
# Below is an example of a nested C-style for-loop:
#
# for(int i = 0; i < A; i++){
#                           // some statements
# for(int j = 0; j < B; j++){
# // some statements
# for(int k = 0; k < C; k++){
# // some statements
# }
# }
# }
#
# Where A, B and C are natural numbers.
#
# Task
#
# Given an array of length N, where N denotes the number of iterative statements.
# Each item-pair in the array represents two elements, with the 1st value (V) indicating the upper boundary
# for the iteration to take place (can be inclusive or exclusive depending on the 2nd value) and the 2nd value
# (Boolean data type -> true / false depending on your chosen language) indicating whether the upper boundary (V)
# is inclusive or not.
#
# You must write a function that outputs an array in which each element represents the number of times each for-loop
# condition is evaluated. Below is an example for better understanding:
#
# Example
#
# arr = [[7, true], [5, false]]
#
# for(int i = 0; i <= 7; i++){
# // This statement is executed 9 times before termination -> 0, 1, 2, 3, 4, 5, 6, 7, 8 (since 8 > 7 is the breaking condition)
# for(int j = 0; j < 5; j++){
# // In one cycle of outermost loop, this statement is executed 6 times before
# termination -> 0, 1, 2, 3, 4, 5 (since 5 >= 5 is the breaking condition)
# // some statements
# }
# }
# Note
#
# The array can be empty, with a range of 0 <= N <= 20
# The starting counter of the C-style for-loop is always 0
# The iteration expression or operation to be performed is always incremental
# The range of upper boundary is as follows: 1 <= V <= 20

def count_loop_iterations(arr):
    count = 1
    new_lst = []
    for item in arr:
        if item[1]:
            num = item[0] + 2
        else:
            num = item[0] + 1
        new_lst.append(count * num)
        count *= num - 1
    print(new_lst)
    return new_lst

## I really struggled with this one because I simply didn't understand the math behind it. After looking at other
# solutions, this idea is a variation of the one that made the most sense to me.


# count_loop_iterations([(4, True), (5, False), (3, True)]) # => [6, 30, 125]
count_loop_iterations([(16, False), (11, False), (1, True)])
# count_loop_iterations([(16, False), (11, False), (1, True), (3, False), (8, True), (10, True), (9, False), (11, True), (20, True), (3, False), (7, False)])
# => [17, 192, 528, 1408, 10560, 114048, 1045440, 12231648, 248396544, 948423168, 5690539008])
# count_loop_iterations([]) # => []
# count_loop_iterations([(20, False)]) # => [21]

