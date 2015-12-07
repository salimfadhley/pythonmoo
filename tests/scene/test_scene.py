import unittest

from pygraph.classes.digraph import digraph

from pythonmoo.scene.container import Container
from pythonmoo.scene.scene import Scene
from pythonmoo.scene.thing import Thing
from pythonmoo.scene.world import World


class TestScene(unittest.TestCase):

    def setUp(self):
        self.graph = digraph()

    def test_make_new_scene(self):
        Scene(name="The First Room")

    def test_scene_properties(self):
        s = Scene(name="The First Room")
        self.assertEqual(s.name, "The First Room")


class TestScene2(unittest.TestCase):
    def setUp(self):
        self.g = digraph()
        self.w = World(self.g)
        self.s = Scene("The First Scene")
        self.w.inject(self.s)

    def test_scene_contains_returns_the_right_object(self):
        t = Thing("object")
        self.w.inject(t)
        self.w.relate(self.s,"in",t)
        self.assertEqual(self.w.get_related(t, "in"), {self.s})

    def test_relationships_are_specfic(self):
        t0 = Thing("A")
        t1 = Thing("B")
        self.w.inject(t0)
        self.w.inject(t1)

        self.w.relate(t0, "in" ,self.s)
        self.w.relate(t1, "on" ,self.s)

        self.assertEqual(self.w.get_related(self.s, "in"), {t0})

    def test_relationships_have_direction0(self):
        watch = Thing("watch")
        bag = Container("bag")
        self.w.inject(bag)
        self.w.relate(bag, "in", self.s)
        self.assertEqual(self.w.get_related(self.s, "in"), {bag})

    def test_relationships_have_direction1(self):
        watch = Thing("watch")
        bag = Container("bag")
        self.w.inject(bag)
        self.w.inject(watch)
        self.w.relate(bag, "in", self.s)
        self.w.relate(watch, "in", bag)
        self.assertEqual(self.w.get_related(bag, "in"), {watch})

    # def test_relationships_are_bidrectional(self):
    #     watch = Thing("watch")
    #     bag = Container("bag")
    #     self.w.inject(bag)
    #     self.w.inject(watch)
    #     self.w.relate(bag, "in", self.s)
    #     self.w.relate(watch, "in", bag)
    #     self.assertEqual(self.w.get_related(watch, "contains"), {bag})
