#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
player_types = ['random', 'reflect', 'cycle']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.score = 0
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):
    def move(self):
        # User have to enter 1 for move, or 2 to quit
        humanInput = input("Choose: \n1.move \n2.quit: \n").lower()
        if humanInput == "1":
            humanInput = input("Enter your move: \n")
            return humanInput
        elif humanInput == "2":
            exit()
            # loop for checking from the right input that user entered
        while humanInput not in moves:
            humanInput = input("Choose a right move! or enter 2 to quit!!\n")
            if humanInput == "2":
                exit()
        return humanInput


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            self.p1.score += 1
            print("Player 1 won")

        elif beats(move2, move1):
            self.p2.score += 1
            print("Player 2 won")
        else:
            print("TIE")

        print("Player 1: " + str(self.p1.score) +
              " Player 2: " + str(self.p2.score))

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(4):
            print(f"Round {round}:")
            self.play_round()

        # THE WINNER
        print("\n\n_____________________________________")
        print("FINAL SCORES!")
        print("Player 1: " + str(self.p1.score) +
              " Player 2: " + str(self.p2.score))
        if self.p1.score > self.p2.score:
            print("PLAYER 1 IS THE WINNER!")
        elif self.p2.score > self.p1.score:
            print("PLAYER 2 IS THE WINNER!")
        else:
            print("TIE!")
        print("GAME OVER!")


if __name__ == '__main__':
    # to let the user choose the type of the player he will play with
    playerType = input("Choose a player type: \n").lower()
    # loop for checking from the right input that user entered
    while playerType not in player_types:
        playerType = input("Enter a right type!!\n")

    if playerType == "random":
        game = Game(HumanPlayer(), RandomPlayer())
    elif playerType == "reflect":
        game = Game(HumanPlayer(), ReflectPlayer())
    elif playerType == "cycle":
        game = Game(HumanPlayer(), CyclePlayer())
    else:
        game = Game(HumanPlayer(), Player())
    game.play_game()
