from src.core.models.character_class import CharacterClass
import json

def load_class(json_path:str):
    """
    Loads class .json file into CharacterClass object, format based on 5e-database
    :param json_path: str, filepath.json
    :return: CharacterClass object of loaded json file
    """
    with open(json_path, "r") as f:
        class_dict = json.load(f)
    return CharacterClass.from_json(class_dict)
