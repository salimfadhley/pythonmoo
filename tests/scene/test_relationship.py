import unittest

from pythonmoo.scene.relationship import Relationship


class TestRelationship(unittest.TestCase):

    def test_relationshps_are_singletons(self):
        r0 = Relationship.get("xxx")
        r1 = Relationship.get("xxx")
        self.assertTrue(r0==r1)

    def test_some_relationships_can_be_inberted(self):
        r0 = Relationship.get("above")
        r1 = Relationship.get("below")
        self.assertEqual(r0.invert(), r1)