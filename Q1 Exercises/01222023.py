# Set the variable called first  to your first name.
#
# Set the variable called last  to your last name.
#
# Then set the variable called formatted  that interpolates both using the .format() method.
# Make sure you follow this pattern:
#
# "First Name: Colt, Last Name: Steele"

first = 'Sarah'
last = 'Panaligan'

formatted = 'First Name: {}, Last Name: {}'.format(first, last)
print(formatted)

## F-string is much more readable since you can see the placement of the variable in the sentence location ##

f_string_format = f'First Name: {first}, Last Name: {last}'
print(f_string_format)
