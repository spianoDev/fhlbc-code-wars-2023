## More Loop Exercises ##

# Have a user imput a number.
# Use a loop to print a string the number of time inputted.

how_many = input('How many times do I have to tell you? ')

i = 0
while i < int(how_many):
    print('CLEAN UP YOUR ROOM!!')
    i += 1

# Use loops, ranges, and conditionals to find unlucky numbers 1-20 inclusive
# Numbers 4 & 13 are unlucky
# Even numbers are even, odd numbers are odd

for num in range(1, 21):
    if num == 4 or num == 13:
        print(f'{num} is UnLuCkY')
    elif num % 2 == 0:
        print(f'{num} is EVEN')
    else:
        print(f'{num} is odD')

# Emoji Art
# print emojis using both a for and while loop

emojis = ['\U0001f929', '\U0001f911', '\U0001fae3', '\U0001f914', '\U0001f60f', '\U0001f644', '\U0001f635',
          '\U0001f973', '\U0001f9d0', '\U0001f47b']
i = 1
for emoji in emojis:
    while len(emojis) >= i:
        print(emojis[i-1] * i)
        i += 1
