# Exercise 36 #
# Your First Function
# Define a function named make_noise  that prints "THE CROWD GOES WILD" (make sure you spell it exactly the same).
# Execute it once at the bottom of your file.

def make_noise():
    print('THE CROWD GOES WILD')


make_noise()


# Exercise 37 #
# Write a function called speak_pig that returns 'oink'.  Yup, that's it.
# I decided to make this a little more interesting by passing an animal through the function.
# If it is a pig, it says oink, otherwise it returns not a pig

def speak_pig(animal):
    return print('oink') if animal == 'pig' else print('No pig in sight...')


speak_pig('pig')
speak_pig('cow')


# Exercise 38 #
# Define a function called generate_evens
# It should return a list of even numbers between 1 and 50(not including 50)

def generate_evens(num1, num2):
    all_nums = range(num1, num2)
    even_nums = []
    for num in all_nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            pass
    print(even_nums)
    return even_nums


generate_evens(1, 50)


# Exercise 39 #
# Implement a function yell  which accepts a single string argument.
# It should return(not print) an uppercased version of the string with an exclamation point aded at the end.
# For example:
#
# yell("go away")   # "GO AWAY!"
#
# yell("leave me alone")   # "LEAVE ME ALONE!"

def yell(phrase):
    return phrase.upper() + '!'


print(yell('hi code warriors'))


# Exercise 40 #
# Fix This Function!
# The pre-written count_dollar_signs  function is broken.
# It's supposed to return the number of $ characters in a given string.
# For example: count_dollar_signs("$uper $ize")  should return 2 .
# But for some reason, the function always returns either 0 or 1. What's going on?

# original function #
# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == '$':
#             count += 1
#         print(count)
#         return count

# Without adding any new lines of code, make count_dollar_signs work as intended
# Need to move the return statement back to the level of the loop or after the first instance, it will return 1
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    print(count)
    return count


count_dollar_signs("$uper $ize")


# Exercise 41 #
# Write a function called speak  that accepts a single parameter, animal.
#
# If animal is "pig", it should return "oink".
# If animal is "duck", it should return "quack".
# If animal is "cat", it should return "meow"
# If animal is "dog", it should return "woof"
# If animal is anything else, it should return "?"
# If no animal is specified, it should default to "dog"
#
#
# speak()  # "woof"
# speak("pig")  # "oink"
# speak("duck")  # "quack"
# speak("cat")  # "meow"
# speak("dog")  # "woof"
# speak("banana")  # "?"

def speak(animal=None):
    if animal == 'pig':
        return 'oink'
    elif animal == 'duck':
        return 'quack'
    elif animal == 'cat':
        return 'meow'
    elif animal == 'dog':
        return 'woof'
    elif animal:
        return '?'
    else:
        return 'woof'


print(speak())
print(speak('orange'))
