import random
import matplotlib.pyplot as plt

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class DiceSystem:
    def __init__(self, n):
        self.n = n
        self.dice = [Die(6) for _ in range(n)]

    def roll_consecutively(self, rolls):
        results = []
        for _ in range(rolls):
            total = sum([die.roll() for die in self.dice])
            results.append(total)
        return results

    def roll_simultaneously(self, rolls):
        results = []
        for _ in range(rolls):
            total = sum([random.randint(1, die.sides) for die in self.dice])
            results.append(total)
        return results
