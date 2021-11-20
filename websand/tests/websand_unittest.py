# PYTHONPATH=../ && python3 -m unittest websand/tests/User_unittest.py

import unittest

from websand.src.User import User

class WebSandUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(WebSandUnitTest, self).__init__(*args, **kwargs)

    def setUp(self):

        pass

    def test_nothingReallyWorks(self):
        print("test_nothingReallyWorks")
