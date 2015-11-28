from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):

    def make_relationship(self, relationship, other):
        self.graph.add_node(other)
        self.graph.add_edge((self, other), attrs=[("relationship",relationship)])

    def get_related_objects(self, relationship):
        return set(self.graph.neighbors(self))
