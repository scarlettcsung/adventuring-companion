import pathlib

from core.models.character import Character
import jsonpickle
import json

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent.parent
SAVE_DIR = PROJECT_ROOT / 'saves' / 'character'

def save_character(character:Character):
    """
    Saves Character object to json file
    :param character: Character object of character of interest
    """
    SAVE_DIR.mkdir(parents=True, exist_ok=True)

    file_path = SAVE_DIR / f"{character.index}.json"

    encoded_data = jsonpickle.encode(character, indent=4)
    file_path.write_text(encoded_data)

    print(f"Saved to: {file_path}")

def load_character(character_index: str) -> Character:
    """
    Loads Character object from json file
    :param character_index: str, character index of character
    :return: Character object of selected character
    """
    file_path = SAVE_DIR / f"{character_index}.json"

    if not file_path.exists():
        raise FileNotFoundError(f"No save file at: {file_path}")

    encoded_data = file_path.read_text()
    character = jsonpickle.decode(encoded_data)

    if hasattr(character, 'spellcasting') and hasattr(character.spellcasting, 'spellslots'):
        character.spellcasting.spellslots = {
            int(k): v for k, v in character.spellcasting.spellslots.items()
        }

    return character


def loadable_characters():
    characters_map = {}

    if not SAVE_DIR.exists():
        return {}

    for file_path in SAVE_DIR.glob('*.json'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)

                char_name = raw_data.get('name', 'Unknown Hero')
                characters_map[char_name] = file_path.stem

        except (json.JSONDecodeError, IOError):
            continue

    return characters_map

def delete_character(index : str):
    """
        Deletes a character's json save file.
        :param index: The filename stem (index) of the character.
        """
    file_path = SAVE_DIR / f"{index}.json"

    if file_path.exists():
        try:
            file_path.unlink()
            print(f"Deleted character file: {file_path}")
        except Exception as e:
            raise IOError(f"Could not delete {index}: {e}")
    else:
        raise FileNotFoundError(f"No save file found for index: {index}")
