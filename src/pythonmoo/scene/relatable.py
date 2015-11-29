from abc import ABCMeta, abstractmethod

from pythonmoo.scene.relationship import Relationship


class Relatable(metaclass=ABCMeta):

    @abstractmethod
    def get_graph(self):
        raise NotImplemented

    def add_relationship(self, relationship_name:str, other_thing):
        relationship = Relationship.get(relationship_name)
        self.get_graph().add_node(other_thing)
        self.add_edge((self, other_thing), attrs=[("relationship", relationship)])


    def get_related_objects(self, relationship):
        return {}