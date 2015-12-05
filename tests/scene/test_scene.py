import unittest

from pygraph.classes.digraph import digraph
from pythonmoo.scene.scene import Scene
from pythonmoo.scene.thing import Thing
from pythonmoo.scene.world import World


class TestScene(unittest.TestCase):

    def setUp(self):
        self.graph = digraph()

    def test_make_new_scene(self):
        Scene.new(graph=self.graph, name="The First Room")

    def test_scene_properties(self):
        s = Scene.new(graph=self.graph, name="The First Room")
        self.assertEqual(s.name, "The First Room")
        self.assertEqual(s.graph, self.graph)

    def test_new_thing(self):
        s = Scene.new(self.graph, "The First Room")
        t = Thing(name="object")
        s.has(t)


class TestScene2(unittest.TestCase):
    def setUp(self):
        self.g = digraph()
        self.w = World(self.g)
        self.s = Scene.new(self.g, "The First Scene")
        self.w.inject(self.s)

    def test_scene_contains_returns_the_right_object(self):
        t = Thing("object")
        self.w.inject(t)
        self.w.relate(self.s,t,"in")
        self.assertEqual(self.w.get_related(self.s, "in"), {t})

    # def test_thing_in_scene_relationship(self):
    #     t = Thing("object")
    #     s = self.s.has(t)
    #     self.assertTrue(t in s.contents())

    # def test_thing_in_scene_relationship(self):
    #     bag = Container("bag")
    #     egg = Thing("egg")
    #
    #     s = Scene.new("room")
    #
    #     s.contains(bag)
    #     bag.contains(egg)
    #
    #     self.assertEqual(s.get_related_objects(relationship="contains"), {bag, })
    #     self.assertEqual(bag.get_related_objects(relationship="contains"), {egg, })

