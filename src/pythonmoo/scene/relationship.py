CACHE = {}

class Relationship:

    def __init__(self, name:str):
        self.name = name

    @classmethod
    def get(cls, name:str):
        if not name in CACHE:
            CACHE[name] = Relationship(name)
        return CACHE[name]
