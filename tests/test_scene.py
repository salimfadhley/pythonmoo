import unittest

from pythonmoo.scene.scene import Scene
from pythonmoo.scene.thing import Thing


class TestScene(unittest.TestCase):

    def test_make_new_scene(self):
        Scene.new("The First Room")

    def test_new_thing(self):
        Thing("object")

    def test_thing_in_scene(self):
        Scene.new("The First Room").make_relationship(relationship="contains", other=Thing("object"))

    def test_thing_in_scene_relationship(self):
        t = Thing("object")
        s = Scene.new("room")
        s.make_relationship("contains", t)
        self.assertEqual(s.get_related_objects(relationship="contains"), {t, })

