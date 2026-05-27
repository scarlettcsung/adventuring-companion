from core import constants
from core.engine.stats_calculator import calc_proficiency, calc_ability_modifier
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

    def get_mod(self,score_abbr:str):
        score = getattr(self, score_abbr.upper(), 10)
        return calc_ability_modifier(score)

"""
SECTION: Stats Class
"""
class Stats:
    def __init__(self,
                 classes:dict, abil_scores:AbilityScores,
                 armor_class:int = 10, saves:list = [], proficiencies:list = [],
                 initiative:int = 0, hit_die:int = 6,speed:int = 30, pb_override: int = None,
                 inventory:Inventory = None):

        self.classes = classes
        self.abil_scores = abil_scores
        self.armor_class = armor_class
        self.saves = saves
        self.proficiencies = proficiencies
        self.initiative = initiative
        self.hit_die = hit_die
        self.speed = speed
        self._pb_override = pb_override
        self.inventory = inventory if inventory is not None else Inventory()

    @property
    def level(self):
        return sum(lvl for lvl, subclass, is_base in self.classes.values())

    @property
    def pb(self):
        if self._pb_override is not None:
            return self._pb_override

        return calc_proficiency(self.level)

    @property
    def base_class(self):
        return next((
            name for name, (level, subclass, is_base) in self.classes.items() if is_base), None)

    def get_modifier(self, ability: str) -> int:
        return self.abil_scores.get_mod(ability)






