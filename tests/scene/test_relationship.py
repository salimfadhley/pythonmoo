import unittest

from pythonmoo.scene.relationship import Relationship


class TestRelationship(unittest.TestCase):

    def test_relationshps_are_singletons(self):
        r0 = Relationship.get("xxx")
        r1 = Relationship.get("xxx")
        self.assertTrue(r0==r1)