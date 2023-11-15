import random


class Mastermind:
    def __init__(self, n_color=6, n_position=4):
        self.__color = n_color
        self.__position = n_position
        self.__hint = None
        self.__puzzle = None
        self.__round = 0

    @property
    def colors(self):
        return self.__color

    @colors.setter
    def colors(self, other):
        if other > 10:
            self.__color = self.colors
        else:
            self.__color = other

    @property
    def positions(self):
        return self.__position

    @positions.setter
    def positions(self, other):
        self.__position = other

    def check(self, user_input):
        self.__hint = ""
        dup = ""
        for i in range(len(user_input)):
            if user_input[i] == self.__puzzle[i]:
                self.__hint = "*" + self.__hint
            elif user_input[i] in self.__puzzle and dup.count(user_input[i]) <= \
                    self.__puzzle.count(user_input[i]):
                self.__hint += "o"
        return self.__hint

    def play(self):
        if self.__color < 10:
            self.__puzzle = "".join([f"{random.randrange(1, self.__color + 1)}"
                                     for i in range(self.__position)])
        elif self.__color == 10:
            self.__puzzle = "".join([f"{random.randrange(10)}" for i in range(self.__position)])
        print(f"Playing Mastermind with {self.__color} colors and {self.__position} positions")
        while self.__hint != "****":
            guess = input("What is your guess?: ")
            print(f"your guess is {guess}")
            print(self.check(guess))
            self.__round += 1
            self.__hint = self.check(guess)
        print(f"You solve it after {self.__round} rounds")
