from pygraph.classes.digraph import digraph

from pythonmoo.scene.container import Container
from pythonmoo.scene.relatable import Relatable


class Scene(digraph, Relatable, Container):

    def get_graph(self):
        return self

    def __init__(self, name):
        digraph.__init__(self)
        self.name = name

