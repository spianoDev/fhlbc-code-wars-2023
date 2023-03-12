import random

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!
player_choice = input("Guess a number between 1 and 10: ")
random_number = random.randint(1, 10)  # numbers 1 - 10

def guessing_game(guess):
    while True:
        if int(guess) > random_number:
            print(f'{guess} is too high... try again')
            guess = input("Guess another, lower number between 1 and 10: ")
        elif int(guess) < random_number:
            print(f'{guess} is too low... try again')
            guess = input("Guess another, higher number between 1 and 10: ")
        else:
            print('Winner, winner chicken dinner!')
            break


guessing_game(player_choice)
