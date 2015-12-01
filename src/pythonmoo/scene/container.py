from pythonmoo.scene.abstractcontainer import AbstractContainer
from pythonmoo.scene.relatable import Relatable
from pythonmoo.scene.thing import Thing


class Container(Thing, Relatable, AbstractContainer):

    def set_graph(self, graph):
        self.graph = graph

    def get_graph(self):
        return self.graph

    def get_this_node(self):
        return self