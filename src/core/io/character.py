import pathlib

from core.models.character import Character
import jsonpickle

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
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

    return character
