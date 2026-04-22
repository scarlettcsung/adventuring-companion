from dataclasses import dataclass, field
from typing import List, Optional
from core.models.counter import Counter
from core.models.dice import Dice


@dataclass
class Feature:
    name: str
    desc: List[str] = field(default_factory=list)
    source: Optional[str] = None
    level: Optional[int] = 0 # Level = 0 if no level
    index: str = field(default=None)
    counter: Optional[Counter] = None
    dice: Optional[Dice] = None

    def __post_init__(self):
        if not (0 <= self.level <= 20):
            raise ValueError("Level must be between 0 and 20")

        if self.index is None:
            self.index = self.name.lower().replace(" ", "-")


