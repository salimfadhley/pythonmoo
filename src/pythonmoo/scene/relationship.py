from pythonmoo.repr_mixin import ReprMixin

CACHE = {}

INVERSIONS = [
    ['above', 'below']
]

CONFIG = {}
for a,b in INVERSIONS:
    CONFIG[a] = b
    CONFIG[b] = a

class Relationship(ReprMixin):

    def __init__(self, name:str):
        self.name = name

    @classmethod
    def get(cls, name:str):
        if not name in CACHE:
            CACHE[name] = Relationship(name)
        return CACHE[name]

    def invert(self):
        inverted_relationship_name = CONFIG.get(self.name, self.name)
        return self.get(inverted_relationship_name)
