# PYTHONPATH=../ && python3 -m unittest websand/tests/websand_unittest.py

import unittest

from websand.src.User import User

class UserUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(UserUnitTest, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def test_twoDifferentUsersAreNotTheSame(self):
        u1 = User("u1")
        u2 = User("u2")
        u1.setID("u1ID")
        u2.setID("u2ID")
        self.assertFalse(u1.isSame(u2))

    def test_oneUserIsTheSameAsItself(self):
        u1 = User("u1")
        u1.setID("u1ID")
        self.assertTrue(u1.isSame(u1))

    def test_usersWithTheSameIdAreTheSame(self):
        u1 = User("u1")
        u2 = User("u2")
        u1.setID("u1ID")
        u2.setID("u1ID")
        self.assertTrue(u1.isSame(u2))
