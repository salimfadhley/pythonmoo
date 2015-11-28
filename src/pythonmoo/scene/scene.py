from pygraph.classes.digraph import digraph

from pythonmoo.scene.base import Base


class Scene(Base):

    @classmethod
    def new(cls, name, graph=None):
        scene = cls(name)
        graph = graph or digraph()
        graph.add_node(scene)
        return scene.add_graph(graph)

    def __init__(self, name):
        self.name = name

    def add_graph(self, graph):
        self.graph = graph
        return self
