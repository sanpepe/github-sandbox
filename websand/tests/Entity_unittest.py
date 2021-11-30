# PYTHONPATH=../ && python3 -m unittest websand/tests/Entity_unittest.py

import unittest

from websand.src.Entity import Entity

class EntityUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(EntityUnitTest, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def test_twoDifferentEntitiesAreNotTheSame(self):
        e1 = Entity()
        e2 = Entity()
        e1.setID("e1ID")
        e2.setID("e2ID")
        self.assertFalse(e1.isSame(e2))

    def test_oneEntityIsTheSameAsItself(self):
        e1 = Entity()
        e1.setID("e1ID")
        self.assertTrue(e1.isSame(e1))

    def test_entitiesWithTheSameIdAreTheSame(self):
        e1 = Entity()
        e2 = Entity()
        e1.setID("e1ID")
        e2.setID("e1ID")
        self.assertTrue(e1.isSame(e2))

    def test_entitiesWithNoneIdsAreNeverSame(self):
        e1 = Entity()
        e2 = Entity()
        self.assertFalse(e1.isSame(e2))