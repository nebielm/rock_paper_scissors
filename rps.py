import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

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
        pass


class RockPlayer(Player):
    def __init__(self):
        super().__init__()


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        while True:
            answer = input("Choose between rock, paper and scissors: ")
            if answer.lower() in moves:
                return answer
            print("Try again.")


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        next_move = self.their_move
        return next_move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        my_last_move = self.my_move
        i = moves.index(my_last_move)
        if i == 2:
            return moves[0]
        else:
            return moves[i+1]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


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
        print("---------->")
        if beats(move1, move2):
            print("Player 1 wins the round.")
            self.p1.score += 1
        elif beats(move2, move1):
            print("Player 2 wins the round.")
            self.p2.score += 1
        else:
            print("This round is a draw.")
        print(f"Score Player 1: {self.p1.score}")
        print(f"Score Player 2: {self.p2.score}")
        print("#=================#")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\n#=================#")
        while True:
            for match in range(1, 4):
                print(f"Round {match}")
                self.play_round()
            if self.p1.score > self.p2.score:
                return (f"Player 1 wins with a final "
                        f"score of {self.p1.score} Points !!!\n"
                        f"Player 2 scores {self.p2.score} Points.")
            elif self.p1.score < self.p2.score:
                return (f"Player 2 wins with a final "
                        f"score of {self.p2.score} Points !!!\n"
                        f"Player 1 scores {self.p1.score} Points.")
            print("It's a draw !! Game continues for another 3 rounds.")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    print(game.play_game())
