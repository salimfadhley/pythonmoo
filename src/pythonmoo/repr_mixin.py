class ReprMixin:

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<%s.%s %s>" % (self.__class__.__module__, self.__class__.__name__, str(self))
