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


# class where player always plays rock
class RockPlayer(Player):
    def __init__(self) -> None:
        super().__init__()


# class where player will play a random move
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# class to allow actual player to input choices
class HumanPlayer(Player):
    def move(self):
        for round in iter(int, 1):
            humanMove = input("Choose Rock, Paper, or Scissors ").lower()
            if humanMove in moves:
                return humanMove
            else:
                print("Not a valid answer, choose again.")


# class where the player will play whatever previous choice of other
# players move was
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


# class where player always plays the next move in the list of options
class CyclePlayer(Player):
    def __init__(self):
        self.changeNumber = random.randint(0, 2)

    def move(self):
        if self.changeNumber < 2:
            self.changeNumber += 1
        else:
            self.changeNumber = 0
        return moves[self.changeNumber]


# defining what choices beat other choices
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

# function that stores what the players have entered
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
        print(f"Player 1 score: {self.p1score} Player 2 score: {self.p2score}")

# function to play multiple rounds
    def play_3round(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        if self.p1score > self.p2score:
            print("Player 1 has won Rock, Paper, Scissors!")
        elif self.p2score > self.p1score:
            print("Player 2 has won Rock, Paper, Scissors!")
        else:
            print("The Players have tied.")

        print("Game over.")

# function to play 1 round
    def play_1round(self):
        print("Game start!")
        self.play_round()
        if self.p1score > self.p2score:
            print("Player 1 has won Rock, Paper, Scissors!")
        elif self.p2score > self.p1score:
            print("Player 2 has won Rock, Paper, Scissors!")
        else:
            print("The Players have tied.")

        print("Game over.")


if __name__ == '__main__':
    game = Game(RockPlayer(), HumanPlayer())
    game.play_1round()
