import unittest

from ply.yacc import digraph

from pythonmoo.scene.scene import Scene
from pythonmoo.scene.world import World


class TestWorld(unittest.TestCase):

    def setUp(self):
        self.w = World.new()
        self.s = Scene("The First Scene")
        self.w.inject(self.s)

    def test_look_at_a_scene(self):
        self.assertEqual(self.w.look(self.s), self.s.name)