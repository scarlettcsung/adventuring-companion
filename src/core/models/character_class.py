from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class CharacterClass:
    name: str
    hit_die: int
    proficiencies: List[str] = field(default_factory=list)
    saving_throws: List[str] = field(default_factory=list)
    starting_equipment: Dict[str, int] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: dict):
        """Parses dictionary into character class object"""
        # Extract names from the 'proficiencies' list
        profs = [p['name'] for p in data.get('proficiencies', [])]

        # Extract names from the 'saving_throws' list
        saves = [s['name'] for s in data.get('saving_throws', [])]

        # Extract equipment and quantities
        equip = {
            item['equipment']['name']: item['quantity']
            for item in data.get('starting_equipment', [])
        }

        return cls(
            name=data['name'],
            hit_die=data['hit_die'],
            proficiencies=profs,
            saving_throws=saves,
            starting_equipment=equip
        )