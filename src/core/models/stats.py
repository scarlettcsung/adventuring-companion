from core import constants
from core.models.inventory import Inventory
from dataclasses import dataclass

"""
SECTION: Stat Types
"""
@dataclass
class AbilityScores:
    STR:int = 10
    DEX:int = 10
    CON:int = 10
    INT:int = 10
    WIS:int = 10
    CHA:int = 10

"""
SECTION: Stats Class
"""
class Stats:
    def __init__(self,
                 classes:dict, abil_scores:AbilityScores,
                 armor_class:int, saves:list,proficiencies:list,
                 initiative:int, hit_die:int,speed:int = 30,
                 inventory:Inventory = None):

        self.classes = classes
        self.base_class = next((name for name, (level, is_base) in self.classes.items() if is_base),
                               None) # contingency, if no base class somehow
        self.abil_scores = abil_scores
        self.armor_class = armor_class
        self.saves = saves
        self.proficiencies = proficiencies
        self.initiative = initiative
        self.hit_die = hit_die
        self.speed = speed
        self.inventory = inventory if inventory is not None else Inventory()

    @property
    def level(self):
        return sum(lvl for lvl, _ in self.classes.values())


