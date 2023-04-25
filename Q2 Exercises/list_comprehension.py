# Exercise 19: List Comprehension Exercises
#
og_lst = ['Elie', 'Tim', 'Matt']
# Create a variable called answer that has the first letter of each name in the og_lst
answer = [x[0] for x in og_lst]
print(answer)
num_lst = [1, 2, 3, 4, 5, 6]
# Create a variable called num_answer that has all the even values of num_lst

answer2 = [x for x in num_lst if x % 2 == 0]
print(answer2)

# Exercise 20: More List Comprehension

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
# Find all the elements that overlap between the two lists

combo_lst = []
[(combo_lst.append(num)) for num in lst1 if num in lst2 and num not in combo_lst]
print(combo_lst)

words = ['Elie', 'Tim', 'Matt']
# Reverse each word (using slice) and make all the character values lower case
reversed_words = [name[::-1].lower() for name in words]
print(reversed_words)
