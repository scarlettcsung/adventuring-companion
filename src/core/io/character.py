from core.models.character import Character
import jsonpickle
import os

def save_character(character:Character, outfile_path:str):
    """
    Saves Character object to json file
    :param character: Character object of character of interest
    :param outfile_path: str, file path to save .json file
    """
    file_name = f"{character.index}.json"
    file_path = os.path.join(outfile_path, file_name)

    if not os.path.isdir(outfile_path):
        raise NotADirectoryError(f"Directory not found: {outfile_path}")

    encoded_data = jsonpickle.encode(character,indent=4)
    with open(file_path,"w") as f:
        f.write(encoded_data)

def load_character(character_index: str, folder_path: str) -> Character:
    """
    Loads Character object from json file
    :param character_index: str, character index of character
    :param folder_path: str, loaded folder path
    :return: Character object of selected character
    """
    file_name = f"{character_index}.json"
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No save file at: {file_path}")

    # 3. Read and Thaw
    with open(file_path, "r") as f:
        encoded_data = f.read()
        character = jsonpickle.decode(encoded_data)

    return character
