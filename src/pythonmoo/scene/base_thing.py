from abc import ABCMeta, abstractmethod


class BaseThing(metaclass=ABCMeta):

    @abstractmethod
    def allowed_relationships(cls):
        return {}

    def __init__(self, name):
        self.name = name