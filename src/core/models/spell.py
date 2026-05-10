import json
from dataclasses import dataclass, asdict, field
from typing import List, Optional, Dict, Any

@dataclass
class Spell:
    name: str
    classes: List[str]
    level: int
    school: str
    cast_time: str
    range: str
    duration: str
    desc: str
    components: List[str]
    is_ritual: bool = False
    is_concentration: bool = False
    damage_dice: Optional[Dict[str, str]] = None  # e.g., "4d4"
    damage_type: Optional[List[str]] = None  # e.g., "Acid"

    @classmethod
    def from_json(cls, data: Dict[str, Any]):
        dmg_info = data.get("damage", {})
        dmg_at_level = dmg_info.get("damage_at_slot_level", {})
        base_dice = dmg_at_level.get(str(data.get("level")), None)

        if not base_dice:
            char_dmg = dmg_info.get("damage_at_character_level", {})
            base_dice = char_dmg.get("1", None)

        return cls(
            name=data["name"],
            level=data["level"],
            school=data["school"]["name"],
            cast_time=data["casting_time"],
            range=data["range"],
            duration=data["duration"],
            desc="\n".join(data["desc"]),
            components=data["components"],
            is_ritual=data.get("ritual", False),
            is_concentration=data.get("concentration", False),
            damage_dice=base_dice,
            damage_type=dmg_info.get("damage_type", {}).get("name")
        )

    def to_file(self, filename: str):
        """Saves the current spell object to a clean JSON file."""
        with open(filename, 'w') as f:
            json.dump(asdict(self), f, indent=4)