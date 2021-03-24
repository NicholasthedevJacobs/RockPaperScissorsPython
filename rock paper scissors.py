from random import random


def play():
    user = input("Press 'r'  for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

def is_win(player, opponent):