import unittest

from pythonmoo.scene.scene import Scene
from pythonmoo.scene.thing import Thing


class TestScene(unittest.TestCase):

    def test_make_new_scene(self):
        Scene("The First Room")

    def test_new_thing(self):
        s = Scene("The First Room")
        Thing("object").within(s)

    def test_scene_contains_returns_the_right_object(self):
        t = Thing("object")
        s = Scene("room").contains(t)
        self.assertIsInstance(s, Scene)

    def test_thing_in_scene_relationship(self):
        t = Thing("object")
        s = Scene("room").contains(t)
        self.assertEqual(s.get_related_objects(relationship="contains"), {t, })

    # def test_thing_in_scene_relationship(self):
    #     bag = Container("bag")
    #     egg = Thing("egg")
    #
    #     s = Scene.new("room")
    #
    #     s.insert(bag)
    #     bag.insert(egg)
    #
    #     self.assertEqual(s.get_related_objects(relationship="contains"), {bag, })
    #     self.assertEqual(bag.get_related_objects(relationship="contains"), {egg, })