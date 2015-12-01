from abc import ABCMeta, abstractmethod

from pythonmoo.scene.relationship import Relationship


class Relatable(metaclass=ABCMeta):

    @abstractmethod
    def get_graph(self):
        raise NotImplemented

    @abstractmethod
    def set_graph(self):
        raise NotImplemented

    @abstractmethod
    def get_this_node(self):
        raise NotImplemented

    def add_relationship(self, relationship_name:str, other_thing):
        relationship = Relationship.get(relationship_name)
        other_thing.set_graph(self.get_graph())
        self.get_graph().add_node(other_thing)
        self.get_graph().add_edge((self.get_this_node(), other_thing), attrs=[("relationship", relationship)])


    def get_related_objects(self, relationship_name:str):
        relationship = Relationship.get(relationship_name)
        return set(self.get_graph().neighbors(self.get_this_node()))

