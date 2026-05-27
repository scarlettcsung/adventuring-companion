# Include stats as param (optional), and all spellcasting related stats go here
from core.models.stats import Stats

from enum import Enum

class SpellPrepType(Enum):
    INNATE = 0
    PREPARED = 1
    KNOWN = 2


class SpellSource:
    """A small container for different sources of magic."""
    def __init__(self, name: str, ability: str, prep_type:SpellPrepType = SpellPrepType.KNOWN):
        self.name = name          # "Fairy", "Wizard", "Magic Initiate"
        self.ability = ability     # e.g., "INT", "WIS", "CHA"
        self.prep_type = prep_type # e.g., "innate", "prepared", "known"
        self.spells = []          # The actual list of Spell objects

class SpellCasting:
    def __init__(self,classes:dict,stats:Stats= None):
        self.stats = stats
        self.classes = classes
        self.subclasses = {}
        for char_class, (lvl, subclass, is_base) in classes.items():
            if is_base:
                self.base_class = char_class
            if subclass:
                self.subclasses[char_class] = subclass

        self.sources = {}
        self.spellslots = {}

    def set_spellslot(self, spell_level:int, spellslots: int, remaining:int):
        self.spellslots[spell_level] = (spellslots,remaining)

    def add_source(self, name: str, ability: str, prep_type: SpellPrepType = SpellPrepType.KNOWN):
        name_key = name.lower().replace(" ", "-")

        if name_key in self.sources:
            source_obj = self.sources[name_key]
            source_obj.ability = ability.upper()
            source_obj.prep_type = prep_type
        else:
            self.sources[name_key] = SpellSource(name, ability.upper(), prep_type)

    def learn_spell(self, source_name: str, spell_obj):
        name_key = source_name.lower().replace(" ", "-")

        if name_key in self.sources:
            self.sources[name_key].spells.append(spell_obj)
        else:
            raise ValueError(f"Source '{source_name}' must be added before learning spells.")

    def get_source_stats(self, source_name: str):
        name_key = source_name.lower().replace(" ", "-")
        source = self.sources.get(name_key)

        if not source or not self.stats:
            return 0, 8

        ability_mod = self.stats.get_modifier(source.ability)

        pb = self.stats.pb

        attack_bonus = ability_mod + pb
        save_dc = 8 + ability_mod + pb

        return attack_bonus, save_dc