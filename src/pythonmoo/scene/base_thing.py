from abc import ABCMeta, abstractmethod


class base_thing(metaclass=ABCMeta):

    @abstractmethod
    def allowed_relationships(cls):
        return {}