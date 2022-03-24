import unittest
import datetime

from websand.src.http.RequestParser import RequestParser

from websand.tests.TestSetup import TestSetup

class RequestParserUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(RequestParserUnitTest, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def test_noneRequest(self):
        parser = RequestParser()
        r = parser.parse(None)
        self.assertEqual("", r.method)
        self.assertEqual("", r.path)

    def test_emptyRequest(self):
        parser = RequestParser()
        r = parser.parse("")
        self.assertEqual("", r.method)
        self.assertEqual("", r.path)

    def test_requestNonEmptyRequest(self):
        parser = RequestParser()
        r = parser.parse("GET /foo/bar HTTP/1.0")
        self.assertEqual("GET", r.method)
        self.assertEqual("/foo/bar", r.path)


    def test_partialRequest(self):
        parser = RequestParser()
        r = parser.parse("GET")
        self.assertEqual("GET", r.method)
        self.assertEqual("", r.path)