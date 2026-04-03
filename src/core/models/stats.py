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
                 classes:dict, abil_scores:AbilityScores, hit_die:int = None,
                 inventory:Inventory = None):

        self.classes = classes
        self.abil_scores = abil_scores
        self.hit_die = hit_die
        self.inventory = inventory if inventory is not None else Inventory()

    @property
    def level(self):
        return sum(lvl for lvl, _ in self.classes.values())


