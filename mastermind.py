import random


class Mastermind:
    def __init__(self, n_color=6, n_position=4):
        if not isinstance(n_color, int):
            raise TypeError("Number of colors must be an integer")
        if not isinstance(n_position, int):
            raise TypeError("Number of positions must be an integer")
        if not(1 <= n_position <= 10):
            raise ValueError("Number of positions must be an integer between 1~10")
        if not(1 <= n_color <= 10):
            raise ValueError("Number of color must be an integer between 1~10")
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
            elif user_input[i] in self.__puzzle and dup.count(user_input[i]) < \
                    self.__puzzle.count(user_input[i]):
                self.__hint += "o"
            dup += user_input[i]
        return self.__hint

    def play(self):
        if self.__color < 10:
            self.__puzzle = "".join([f"{random.randrange(1, self.__color + 1)}"
                                     for i in range(self.__position)])
        elif self.__color == 10:
            self.__puzzle = "".join([f"{random.randrange(10)}" for i in range(self.__position)])
        print(f"Playing Mastermind with {self.__color} colors and {self.__position} positions")
        while self.__hint != "".join(["*" for i in range(self.__position)]):
            guess = input("What is your guess?: ")
            while len(guess) != self.__position:
                print("Number of digits you guess must equal to positions")
                print()
                guess = input("What is your guess?: ")
            print(f"your guess is {guess}")
            print(self.check(guess))
            print(self.__puzzle)
            print()
            self.__round += 1
            self.__hint = self.check(guess)

        print(f"You solve it after {self.__round} rounds")


print("Welcome to mastermind game, Let's start!")
q = ""
while q != "No":
    colors = input("How many colors? (1~10): ")
    while colors != "1" and colors != "2" and colors != "3" and colors != "4" and colors != "5" and\
            colors != "6" and colors != "7" and colors != "8" and colors != "9" and colors != "10":
        print("Number of colors must be an integer between 1~10")
        colors = input("How many colors? (1~10): ")
    colors = int(colors)
    positions = input("How many positions? (1~10): ")
    while positions != "1" and positions != "2" and positions != "3" and positions != "4" and\
            positions != "5" and positions != "6" and positions != "7" and positions != "8" and\
            positions != "9" and positions != "10":
        print("Number of colors must be an integer between 1~10")
        positions = input("How many colors? (1~10): ")
    positions = int(positions)
    new_game = Mastermind(colors, positions)
    print()
    new_game.play()
    print()
    q = input("Wanna continue? (Yes/No): ")
    while q != "Yes" and q != "No":
        print('Type only "Yes" or "No"')
        q = input("Wanna continue? (Yes/No): ")
print("Thanks for playing!!")
