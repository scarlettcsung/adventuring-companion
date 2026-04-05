from core.models.inventory import Inventory
from core.models.stats import Stats

class Character:
    def __init__(self,
                 name:str,classes:dict,stats:Stats = None,
                 features:list = None,spells:list = None,
                 inventory:Inventory = None,
                 index:str = None):
        """
        Initializing character attributes.
        :param name: str, Character name
        :param classes: dict of tuples {class:(level:int,IsBaseClass:bool)}, Character classes
            ex. {barbarian: (5,True)} or {barbarian:(5,True), fighter:(2,False)}
        :param stats: Stats, character statistics
        :param features: list [Feature], Character features
        :param spells: list [Spell], Character spells
        :param inventory: Inventory, Character inventory
        :param index: str, Index of character
        """

        self.name = name
        self.classes = classes
        for char_class, (lvl,is_base) in classes.items():
            if is_base:
                self.base_class = char_class
                break
        self.stats = stats
        self.features = features if features is not None else []
        self.spells = spells if spells is not None else []
        self.inventory = inventory
        self.index = index or name.lower().replace(" ", "-")

    def __repr__(self):
        return f"Character(name='{self.name}', index='{self.index}')"

    @property
    def level(self):
        return sum(lvl for lvl, _ in self.classes.values())

    def level_up(self, char_class):
        current_level, is_base = self.classes.get(char_class, (0, False))
        self.classes[char_class] = (current_level + 1, is_base)
        self.stats.classes[char_class] = (current_level + 1, is_base)
