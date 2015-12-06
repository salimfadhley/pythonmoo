from abc import ABCMeta, abstractmethod


class BaseThing(metaclass=ABCMeta):

    @abstractmethod
    def allowed_relationships(cls):
        return {}

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<%s.%s %s>" % (self.__class__.__module__, self.__class__.__name__, str(self))

    def __init__(self, name):
        self.name = name