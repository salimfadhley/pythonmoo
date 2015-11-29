class Relationship:

    def __init__(self, name:str):
        self.name = name

    @classmethod
    def get(cls, name:str):
        return Relationship(name)