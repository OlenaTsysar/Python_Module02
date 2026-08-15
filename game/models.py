import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def check(self, score):
        self.score += score

    def cube(self):
        return random.randint(1,6)


class Computer(Player):
    def __init__(self):
        self.name = "Computer"

    # def cube(self):
    #     return random.randint(1,6)


