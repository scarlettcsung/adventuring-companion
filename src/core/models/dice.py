import random

class Dice:
    def __init__(self, n:int = 1, die_type:int = 20):
        self.n = n
        self.die_type = die_type

    def to_tuple(self):
        return self.n, self.die_type

    def roll(self):
        rolls = [random.randint(1, self.die_type) for _ in range(self.n)]
        return rolls, sum(rolls)

    def roll_highest(self,times:int = 2):
        if self.n > 1:
            raise ValueError("Advantage only applies to single-die rolls (e.g., 1d20).")
        rolls = [random.randint(1,self.die_type) for _ in range(times)]
        return max(rolls), rolls

    def roll_lowest(self, times: int = 2):
        if self.n > 1:
            raise ValueError("Disadvantage only applies to single-die rolls (e.g., 1d20).")
        rolls = [random.randint(1,self.die_type) for _ in range(times)]
        return min(rolls), rolls


