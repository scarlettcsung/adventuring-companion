class Feature:
    def __init__(self, name:str, source:str, desc, level:int = 0, index: str = None):
        """
        Initializing attributes
        :param name: str, feature name
        :param source: str, where the feature comes from. like race, class etc.
        :param desc: str/list, feature description. str if inputted by UI, list if imported json.
        :param level: str, class-level associated with feature. defaults 0 for features not tied to classes
        :param index: str, "ID" for feature
        """
        self.name = name
        self.level = level
        self.source = source

        if isinstance(desc,list):
            self.desc = "\n\n".join(desc)
        else:
            self.desc = desc

        self.index = index or name.lower().replace(" ","-")