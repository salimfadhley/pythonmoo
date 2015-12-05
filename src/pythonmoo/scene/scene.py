class Scene:

    @classmethod
    def new(cls, graph, name):
        return cls(graph=graph, name=name)

    def __init__(self, graph, name, contents={}):
        self.graph = graph
        self.name = name
        self._contents = contents

    def has(self, item):
        return self

    def contents(self):
        return self._contents

