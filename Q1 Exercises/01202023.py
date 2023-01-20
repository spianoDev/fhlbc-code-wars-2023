# Set the variable called greeting  to some greeting, e.g. "hello".
#
# Set the variable called name  to some name, e.g. "Heisenberg".
#
# Then set the variable called greet_name  so that it concatenates greeting , name , and a space " " between them.

greeting = 'Hey there'
name = 'Mister Boba'
greet_name = greeting + ' ' + name
print(greet_name)

# OR, you can use a join statement
greeting_name_list = ['Hello again', 'Charlie']
another_greet_name = ' '.join(greeting_name_list)
print(another_greet_name)
