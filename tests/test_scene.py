import unittest

from pythonmoo.scene import Scene


class TestScene(unittest.TestCase):

    def test_make_new_scene(self):
        Scene("The First Room")

