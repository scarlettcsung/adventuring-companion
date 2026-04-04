class Feature:
    def __init__(self,
                 name:str, desc:list = None, source:str = None, level:int = 0,
                 index: str = None, counter:bool = False):
        """
        Initializing feature attributes
        :param name: str, feature name
        :param desc: list(str), feature description. One line per item.
        :param source: str, where the feature comes from. like race, class etc.
        :param level: str, Class-level associated with feature. Defaults 0 for features not tied to levels
        :param index: str, "ID" for feature
        """
        if not (0 <= level <= 20):
            raise ValueError("Level must be between 0 and 20")

        self.name = name
        self.level = level
        self.source = source
        self.desc = desc
        self.index = index or name.lower().replace(" ","-")


    def __repr__(self):
        return f"Feature(name='{self.name}', index='{self.index}')"

