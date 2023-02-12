## Basic Version ##
print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
player2 = input("(enter Player 2's choice): ")

print("SHOOT!")

if player1 == player2:
    print('It\'s a DRAW!')
elif player1.lower() == 'rock' and player2.lower() == 'scissors':
    print(f'Player 1 WINS with {player1}!')
elif player1.lower() == 'scissors' and player2.lower() == 'paper':
    print(f'Player 1 WINS with {player1}!')
elif player1.lower() == 'paper' and player2.lower() == 'rock':
    print(f'Player 1 WINS with {player1}!')
else:
    print(f'Player 2 WINS with {player2}!')
