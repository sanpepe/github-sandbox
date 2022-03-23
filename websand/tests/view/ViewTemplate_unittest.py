# PYTHONPATH=../ && python3 -m unittest websand/tests/ViewTemplate_unittest.py

import unittest

from websand.src.view.ViewTemplate import ViewTemplate

class ViewTemplateUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ViewTemplateUnitTest, self).__init__(*args, **kwargs)
        self.template = None

    def setUp(self):
        self.template = None

    def test_noReplacement(self):
        msg = "some static content"
        self.template = ViewTemplate(msg)
        self.template.getContent()
        self.assertEqual(msg, self.template.getContent())

    def test_simpleReplacement(self):
        self.template = ViewTemplate("replace ${this}.")
        self.template.replace("this", "replacement")
        self.assertEqual("replace replacement.", self.template.getContent())