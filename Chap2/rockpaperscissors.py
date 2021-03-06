#! python3

import random
import sys
import time

print('ROCK, PAPER, SCISSORS')

# Variables to keep track of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit the program.
        if playerMove in ['r', 'p', 's']:
            break  # Break out of the player input loop.
        print('Type your move:  r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    time.sleep(1)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    # Display and record the win/loss/tie:
    time.sleep(1)
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('Wou win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You Lose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You Lose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You Lose!')
        losses += 1
