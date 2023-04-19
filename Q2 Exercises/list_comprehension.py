# Exercise
#
og_lst = ['Elie', 'Tim', 'Matt']
# Create a variable called answer that has the first letter of each name in the og_lst
answer = [x[0] for x in og_lst]
print(answer)
num_lst = [1, 2, 3, 4, 5, 6]
# Create a variable called num_answer that has all the even values of num_lst

answer2 = [x for x in num_lst if x % 2 == 0]
print(answer2)
