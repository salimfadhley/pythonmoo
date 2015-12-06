from pythonmoo.repr_mixin import ReprMixin

CACHE = {}

class Relationship(ReprMixin):

    def __init__(self, name:str):
        self.name = name

    @classmethod
    def get(cls, name:str):
        if not name in CACHE:
            CACHE[name] = Relationship(name)
        return CACHE[name]
