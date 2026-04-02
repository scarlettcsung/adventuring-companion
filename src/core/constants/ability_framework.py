"""
Describes ability scores and maps saves and skills to ability scores. Contains functions calculating proficiency bonuses and ability score modifiers.
"""
# imports
import math
from typing import Dict

"""
ABILITY SCORES
Dictionary of abilities
key: 3-letter abbreviation
value: full ability name"""
ABILITIES: Dict[str, str] = {
    "STR": "Strength",
    "DEX": "Dexterity",
    "CON": "Constitution",
    "INT": "Intelligence",
    "WIS": "Wisdom",
    "CHA": "Charisma"
}

"""
SAVES
Dictionary of saves
key: 3-letter abbreviation
value: full name"""
SAVES: Dict[str, str] = {
    "STR": "Strength",
    "DEX": "Dexterity",
    "CON": "Constitution",
    "INT": "Intelligence",
    "WIS": "Wisdom",
    "CHA": "Charisma"
}

"""
SKILLS
Dictionary of skills
key: skill name
value: associated ability (3-letter abbreviation)"""
SKILL_MAP: Dict[str, str] = {
    "Acrobatics": "DEX",
    "Animal Handling": "WIS",
    "Arcana": "INT",
    "Athletics": "STR",
    "Deception": "CHA",
    "History": "INT",
    "Insight": "WIS",
    "Intimidation": "CHA",
    "Investigation": "INT",
    "Medicine": "WIS",
    "Nature": "INT",
    "Perception": "WIS",
    "Performance": "CHA",
    "Persuasion": "CHA",
    "Religion": "INT",
    "Sleight of Hand": "DEX",
    "Stealth": "DEX",
    "Survival": "WIS"
}

def get_proficiency(level: int) -> int:
    """
    Calculate proficiency bonus based on total character level
    :param level: int, character level (if multiclass, sum of all class levels)
    :return: int, proficiency bonus
    """
    return max(2,math.ceil(level/4)+1)

def get_ability_modifier(score: int) -> int:
    """
    Calculates ability score modifier. NOT for skill modifiers.
    :param score: int, ability score. i.e. "big number"
    :return: int, ability score modifier i.e. "small number"
    """
    return (score-10)//2