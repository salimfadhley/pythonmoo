from abc import ABCMeta, abstractmethod

from pythonmoo.repr_mixin import ReprMixin


class BaseThing(ReprMixin, metaclass=ABCMeta):

    @abstractmethod
    def allowed_relationships(cls):
        return {}

    def __init__(self, name):
        self.name = name