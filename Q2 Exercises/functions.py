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

