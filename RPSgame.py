#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def randomMove(self):
        return random.choice(moves)
        

class HumanPlayer(Player):
    def move(self):
        while True:
            humanMove = input("Choose Rock, Paper, or Scissors ").lower()
            if humanMove in moves:
               return humanMove
            else:
                print("Not a valid answer, choose again.")
                continue

class ReflectPlayer(Player):
    def __init__(self):
        self.beforeChoice = 'none'

    def move(self):

        if self.beforeChoice == 'none':
            return random.choice(moves)
        else:
            return self.beforeChoice

    def learn(self, my_move, their_move):
        self.beforeChoice = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.changeNumber = random.randint(0, 2)

    def move(self):
        if self.changeNumber < 2:
            self.changeNumber += 1
        else:
            self.changeNumber = 0
        return moves[self.changeNumber]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            print("Player 1 wins this round.")
            self.p1score += 1
        elif beats(move2, move1):
            print("Player 2 wins this round.")
            self.p2score += 1
        else:
            print("The Players have tied.")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1score > self.p2score:
            print("Player 1 has won Rock, Paper, Scissors!")
        elif self.p2score > self.p1score:
            print("Player 2 has won Rock, Paper, Scissors!")
        else:
            print("The Players have tied.")

        print("Game over.")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
