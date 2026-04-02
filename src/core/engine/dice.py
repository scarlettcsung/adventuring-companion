import random
from typing import Literal

def roll(number:int = 1, die:int = 20, roll_type: Literal[-1,0,1] = 0):
    """
    Dice roller
    :param number: int, number of dice
    :param die: int, type of die/dice (i.e. 20 for d20)
    :param roll_type: Literal[-1,0,1], indicates whether the roll is straight, with advantage, or with disadvantage
        -1: Disadvantage
        0: Straight
        1: Advantage
    :return: tuple ([rolls],total number). Rolls list shows the number(s) on the die/dice, and the total number adds all dice.
    """

    # Initializing lists to report several rolls
    rolls_multi = []

    # Advantage/Disadvantage should not be multi-dice
    if number > 1 and roll_type != 0:
        raise ValueError("Advantage/Disadvantage only applies to single-die rolls (e.g., 1d20).")

    # Multi-dice, display all rolls and add them
    if number > 1:
        for n in range(number):
            r = random.randint(1,die)
            rolls_multi.append(r)
        return rolls_multi, sum(rolls_multi)

    # Advantage/Disadvantage, display both rolls
    if roll_type != 0:
        r1 = random.randint(1,die)
        r2 = random.randint(1,die)
        rolls_adv_disadv = [r1,r2] # Reports both rolls
        result = 0
        if roll_type == -1:
            result = min(rolls_adv_disadv)
        elif roll_type == 1:
            result = max(rolls_adv_disadv)
        return rolls_adv_disadv, result

    # Straight roll
    else:
        r = random.randint(1,die)
        return [r], r
