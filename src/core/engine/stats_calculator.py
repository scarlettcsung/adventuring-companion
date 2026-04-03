from math import ceil

def calc_proficiency(level: int) -> int:
    """
    Calculate proficiency bonus based on total character level
    :param level: int, character level (if multiclass, sum of all class levels)
    :return: int, proficiency bonus
    """
    return max(2,ceil(level/4)+1)

def calc_ability_modifier(score: int) -> int:
    """
    Calculates ability score modifier. NOT for skill modifiers.
    :param score: int, ability score. i.e. "big number"
    :return: int, ability score modifier i.e. "small number"
    """
    return (score-10)//2

def calc_ac(character):
    ac_value = 10
    return ac_value