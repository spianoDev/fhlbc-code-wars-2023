## Rock Paper Scissors Mini-Project ##
# print("...rock...")
# print("...paper...")
# print("...scissors...")
#
# player1 = input("(enter Player 1's choice): ")
# # player2 = input("(enter Player 2's choice): ")
#
# print("SHOOT!")

## Basic Version ##
# if player1 == player2:
#     print('It\'s a DRAW!')
# elif player1.lower() == 'rock' and player2.lower() == 'scissors':
#     print(f'Player 1 WINS with {player1}!')
# elif player1.lower() == 'scissors' and player2.lower() == 'paper':
#     print(f'Player 1 WINS with {player1}!')
# elif player1.lower() == 'paper' and player2.lower() == 'rock':
#     print(f'Player 1 WINS with {player1}!')
# else:
#     print(f'Player 2 WINS with {player2}!')

## Refactor 1: wrap repeating elements inside a function ##


# def rock_paper_scissors(player1_choice, player2_choice):
#     winning_choices = {
#           'paper': 'rock',
#           'rock': 'scissors',
#           'scissors': 'paper'
#         }
#     if player1_choice.lower() == player2_choice.lower():
#         print('It\'s a DRAW!')
#     for choice in winning_choices.items():
#         if player1_choice.lower() == choice[0] and player2_choice.lower() == choice[1]:
#             print(f'Player 1 wins with {player1_choice}')
#             return player1_choice
#         elif player2_choice.lower() == choice[0] and player1_choice.lower() == choice[1]:
#             print(f'Player 2 wins with {player2_choice}')
#             return player2_choice
#
#
# rock_paper_scissors(player1, player2)

## Refactor 2: add error handling ##


# def rock_paper_scissors(player1_choice, player2_choice):
#     if player1_choice.lower() not in winning_choices:
#         sys.exit(f'Player 1 entered an incorrect response of {player1_choice}. Please try again')
#     elif player2_choice.lower() not in winning_choices:
#         sys.exit(f'Player 2 entered an incorrect response of {player2_choice}. Please try again')
#     else:
#         for choice in winning_choices.items():
#             if player1_choice.lower() == player2_choice.lower():
#                 print('It\'s a DRAW!')
#                 return
#             elif player1_choice.lower() == choice[0] and player2_choice.lower() == choice[1]:
#                 print(f'Player 1 wins with {player1_choice}')
#                 return player1_choice
#             elif player2_choice.lower() == choice[0] and player1_choice.lower() == choice[1]:
#                 print(f'Player 2 wins with {player2_choice}')
#                 return player2_choice

# rock_paper_scissors(player1, player2)
from random import randint
import sys

winning_choices = {
    'paper': 'rock',
    'rock': 'scissors',
    'scissors': 'paper'
}

player1_wins = 0
computer_wins = 0
winning_score = 3


def rock_paper_scissors(computer_choice):
    global player1_wins, computer_wins
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    player1_choice = input("(enter Player 1's choice): ")
    print("SHOOT!")
    if player1_choice.lower() not in winning_choices:
        sys.exit(f'Player 1 entered an incorrect response of {player1_choice}. Please try again')
    else:
        for choice in winning_choices.items():
            if player1_choice.lower() == computer_choice:
                print('It\'s a DRAW!')
                return
            elif player1_choice.lower() == choice[0] and computer_choice == choice[1]:
                print(f'Player 1 wins with {player1_choice} over {computer_choice}')
                player1_wins += 1
                print(player1_wins)
                return player1_choice, player1_wins
            elif computer_choice == choice[0] and player1_choice.lower() == choice[1]:
                print(f'Computer wins with {computer_choice} over {player1_choice}')
                computer_wins += 1
                print(computer_wins)
                return computer_choice, computer_wins


while player1_wins < winning_score and computer_wins < winning_score:
    random_num = randint(0, 2)
    print(random_num)
    winners = list(winning_choices)
    computer = winners[random_num]
    print(computer)
    rock_paper_scissors(computer)
    print(f"Player Score: {player1_wins} Computer Score: {computer_wins}")

