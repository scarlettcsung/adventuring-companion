from core.models.inventory import Inventory
from core.models.stats import Stats

# TODO: add calculate logic for inputs

class Character:
    def __init__(self,
                 name:str,
                 classes:dict = None,stats:Stats = None,
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
        self.classes = classes if classes is not None else {}
        self.stats = stats
        self.features = features if features is not None else []
        self.spells = spells if spells is not None else []
        self.inventory = inventory
        self.index = index or name.lower().replace(" ", "-")

    def __repr__(self):
        return f"Character(name='{self.name}', index='{self.index}')"

    @property
    def base_class(self):
        for name, (lvl, subclass, is_base) in self.classes.items():
            if is_base:
                return name
        return None

    @property
    def subclasses(self):
        return {name: subclass for name, (lvl, subclass, is_base) in self.classes.items() if subclass}

    @property
    def level(self):
        return sum(lvl for lvl, subclass, is_base in self.classes.values())

    def level_up(self, char_class, new_subclass: str = None):
        current_lvl, subclass, is_base = self.classes.get(char_class, (0, None, False))
        final_subclass = new_subclass or subclass
        self.classes[char_class] = (current_lvl + 1, final_subclass, is_base)
        if self.stats:
            self.stats.classes[char_class] = (current_lvl + 1, final_subclass, is_base)

    def remove_feature(self, feature_name:str):
        self.features[:] = [f for f in self.features if f.name != feature_name]

