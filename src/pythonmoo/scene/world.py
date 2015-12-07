from pygraph.classes import digraph

from pythonmoo.scene.relationship import Relationship
from pythonmoo.scene.thing import Thing


class World:

    def __init__(self, g:digraph):
        self.g = g

    def inject(self, t:Thing):
        self.g.add_node(t)

    def relate(self, a:Thing, relationship_name:str, b:Thing):
        relationship = Relationship.get(relationship_name)
        self.g.add_edge((b,a), attrs=[("relationship", relationship)])

    def get_related(self, a, relationship_name):
        relationship = Relationship.get(relationship_name)
        related = set()

        for n in self.g.neighbors(a):
            if dict(self.g.edge_attr.get((a,n), [])).get("relationship") == relationship:
                related.add(n)

        return related
