from abc import abstractmethod, ABCMeta

from pythonmoo.scene.thing import Thing


class Container(metaclass=ABCMeta):

    @abstractmethod
    def add_relationship(self, relationship_name, other_thing):
        raise NotImplemented

    def contains(self, t:Thing):
        self.add_relationship(relationship_name="contains", other_thing=t)
        return self