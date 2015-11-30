from pygraph.classes.digraph import digraph

from pythonmoo.scene.container import Container
from pythonmoo.scene.id_generator import get_next_id
from pythonmoo.scene.relatable import Relatable


class Scene(Relatable, Container):

    def get_this_node(self):
        return self.scene_id

    @classmethod
    def new(cls, name):
        graph = digraph()
        scene_id = "scene_%i" % get_next_id()
        graph.add_node(scene_id)
        return cls(name, graph, scene_id)

    def get_graph(self):
        return self.graph

    def __init__(self, name:str, graph:digraph, scene_id:str):
        self.graph = graph
        self.name = name
        self.scene_id = scene_id

