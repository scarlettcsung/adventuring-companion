from core.models.inventory import Inventory
from core.models.stats import Stats

# TODO: add calculate logic for inputs

class Character:
    def __init__(self,
                 name:str,classes:dict,stats:Stats = None,
                 features:list = None,spells:list = None,
                 inventory:Inventory = None,
                 index:str = None):
        """
        Initializing character attributes.
        :param name: str, Character name
        :param classes: dict of tuples {class:(level:int,subclass:str,IsBaseClass:bool)}, Character classes
            ex. {barbarian: (5,"Path of the Berserker",True)}
            or {barbarian:(5,"Path of the Berserker",True), fighter:(3,"Battle Master",False)}
        :param stats: Stats, character statistics
        :param features: list [Feature], Character features
        :param spells: list [Spell], Character spells
        :param inventory: Inventory, Character inventory
        :param index: str, Index of character
        """

        self.name = name
        self.classes = classes
        self.base_class = None
        self.subclasses = {}

        for char_class, (lvl, subclass, is_base) in classes.items():
            if is_base:
                self.base_class = char_class

            if subclass:
                self.subclasses[char_class] = subclass

        self.stats = stats
        self.features = features if features is not None else []
        self.spells = spells if spells is not None else []
        self.inventory = inventory
        self.index = index or name.lower().replace(" ", "-")

    def __repr__(self):
        return f"Character(name='{self.name}', index='{self.index}')"

    @property
    def level(self):
        return sum(lvl for lvl, subclass, is_base in self.classes.values())

    def level_up(self, char_class, new_subclass: str = None):
        current_lvl, subclass, is_base = self.classes.get(char_class, (0, None, False))
        final_subclass = new_subclass or subclass
        self.classes[char_class] = (current_lvl + 1, final_subclass, is_base)
        if final_subclass:
            self.subclasses[char_class] = final_subclass
        if self.stats:
            self.stats.classes[char_class] = (current_lvl + 1, final_subclass, is_base)
