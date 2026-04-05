from dataclasses import dataclass, field, replace
from enum import Enum

from typing import List, Tuple

"""
SECTION: Item Types
"""
@dataclass
class Currency:
    cp: int = 0
    sp: int = 0
    ep: int = 0
    gp: int = 0
    pp: int = 0

    @property
    def show_coins(self):
        """Shows the amount of coins."""
        return {"pp":self.pp,"gp":self.gp,"ep":self.ep,"sp":self.sp,"cp":self.cp}

    def add_coins(self, amount:'Currency'):
        """Adds to coins."""
        self.cp += amount.cp
        self.sp += amount.sp
        self.ep += amount.ep
        self.gp += amount.gp
        self.pp += amount.pp

    def spend_coins(self, amount: int, unit: str):
        """Spends coins and repackages."""

        rates = {"pp": 1000, "gp": 100, "ep": 50, "sp": 10, "cp": 1}

        # Liquidates to cp
        total_cp = (self.pp * 1000 + self.gp * 100 + self.ep * 50 +
                    self.sp * 10 + self.cp)
        cost_in_cp = amount * rates[unit]

        # Error handling, not enough money
        if cost_in_cp > total_cp:
            raise ValueError("Not enough total currency to cover the cost.")

        # Cleans up wallet
        remaining = total_cp - cost_in_cp
        self.pp = remaining // 1000
        remaining %= 1000
        self.gp = remaining // 100
        remaining %= 100
        self.ep = remaining // 50
        remaining %= 50
        self.sp = remaining // 10
        self.cp = remaining % 10


@dataclass
class Item:
    name: str # Item name
    weight: float = 0.0 # Weight of item
    quantity: int = 1 # Number of item
    description: List[str] = field(default_factory=list) # Description of item, one string per line
    cost: Currency = field(default_factory=Currency) # Cost of item
    is_arcane_focus: bool = False # If it is arcane focus

class ArmorType(Enum):
    NONE = 0
    LIGHT = 1
    MEDIUM = 2
    HEAVY = 3

@dataclass
class Armor(Item):
    is_equipped: bool = False
    base_ac: int = 10
    armor_type: ArmorType = ArmorType.NONE
    stealth_disadvantage: bool = False
    strength_requirement: int = 0

    @property
    def max_dex_bonus(self):
        if self.armor_type == ArmorType.HEAVY: return 0
        if self.armor_type == ArmorType.MEDIUM: return 2
        return 99  # Light/None has no cap

class WeaponCategory(Enum):
    SIMPLE = "Simple"
    MARTIAL = "Martial"
    UNARMED = "Unarmed"

@dataclass
class Weapon(Item):
    category: WeaponCategory = WeaponCategory.SIMPLE
    properties: List[str] = field(default_factory=list)
    is_equipped: bool = False
    dice: Tuple[int,int] = (1, 20)
    @property
    def damage_str(self):
        return f"{self.dice[0]}d{self.dice[1]}"

@dataclass
class Shield(Item):
    ac_bonus: int = 2
    is_equipped: bool = False


"""
INVENTORY CLASS
"""
class Inventory:
    def __init__(self, items:list = None):
        """
        Initializing Inventory attributes.
        :param items: list of Item objects containing all imported items of character.
        """
        self.items = items if items is not None else []

    def __repr__(self):
        if not self.items:
            return "Inventory is empty."
        return "\n".join([repr(item) for item in self.items])

    def add_item(self, item: Item, number: int = 1):
        """
        Adds item to inventory
        :param item: Item object, item that you intend to add
        :param number: int, number of items to be added
        """
        existing_item = next((i for i in self.items if i.name == item.name), None)

        if existing_item:
            existing_item.quantity += number
        else:
            new_item = replace(item)
            new_item.quantity = number
            self.items.append(new_item)

    def remove_item(self, item: Item, number: int = 1):
        """
        Removes item from inventory
        :param item: Item object of item you intend to remove
        :param number: int, number of items to be removed
        """
        target = next((i for i in self.items if i.name == item.name), None)

        if not target:
            raise ValueError(f"You don't have any '{item.name}' in your inventory.")

        if number > target.quantity:
            raise ValueError(f"Cannot remove {number} {item.name}(s). You only have {target.quantity}.")

        target.quantity -= number

        if target.quantity <= 0:
            self.items.remove(target)

    @property
    def armors(self) -> List[Armor]:
        """Returns all Armor objects in the inventory."""
        return [i for i in self.items if isinstance(i, Armor)]

    @property
    def shields(self) -> List[Shield]:
        """Returns all Shield objects in the inventory."""
        return [i for i in self.items if isinstance(i, Shield)]

    @property
    def weapons(self) -> List[Weapon]:
        """Returns all Weapon objects in the inventory."""
        return [i for i in self.items if isinstance(i, Weapon)]

    @property
    def other_items(self) -> List[Item]:
        """Returns all generic Item objects (not specialized subclasses)."""
        return [i for i in self.items if type(i) == Item]

    @property
    def equipment(self) -> List[Item]:
        """Returns 'equipment' portion of inventory."""
        return self.weapons + self.other_items

    @property
    def total_weight(self) -> float:
        """Calculates the total weight of all items in the inventory."""
        return sum(item.weight * item.quantity for item in self.items)

