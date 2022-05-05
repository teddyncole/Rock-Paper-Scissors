#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
from unittest import result
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self, move):
        return move

    def learn(self, my_move, their_move):
        pass
    

class RandomPlayer(Player):
    def randomMove(self, move):
        self.move = random.choice(moves)
        return move


Player1 = RandomPlayer
Player2 = RandomPlayer


class HumanPlayer(Player):
    def playerMove(self, move):
        self.move = input("Rock, paper, scissors?")
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = HumanPlayer
        self.p2 = Player2

    def play_round(self):
        move1 = self.p1.playerMove(self.p1, self.p1.move)
        move2 = self.p2.randomMove(self.p2, self.p2.move)
        self.result = beats(move1, move2)
#       fix below: printing "Player 1: <function Player.move at 
#       0x103b11120> Player 2: <function Player.move at 0x103b11120>"
#       instead of actual moves
        print(f"Player 1: {move1} Player 2: {move2}")
        if (move1 == move2):
            print("Tie!")
        elif (self.result):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        self.p1.learn(self.p1, move1, move2)
        self.p2.learn(self.p2, move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}: ")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), Player2())
    game.play_game()