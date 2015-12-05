from pygraph.classes import digraph

from pythonmoo.scene.relationship import Relationship
from pythonmoo.scene.thing import Thing


class World:

    def __init__(self, g:digraph):
        self.g = g

    def inject(self, t:Thing):
        self.g.add_node(t)

    def relate(self, a:Thing,b:Thing,relationship_name:str):
        relationship = Relationship.get(relationship_name)
        self.g.add_edge((a,b), attrs=[("relationship", relationship)])

    def get_related(self, a, relationship_name):
        return set(self.g.neighbors(a))