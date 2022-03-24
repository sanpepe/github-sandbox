import unittest
import datetime

from websand.src.http.Router import Router
from websand.src.http.ParsedRequest import ParsedRequest
from websand.src.http.Controller import Controller


class RouterUnitTest(unittest.TestCase):
    actualRequest = None
    def __init__(self, *args, **kwargs):
        super(RouterUnitTest, self).__init__(*args, **kwargs)
        self.router = None

    def setUp(self):
        self.router = Router()

    def tearDown(self):
        RouterUnitTest.actualRequest = None

    def test_simplePath(self):
        request = ParsedRequest("GET", "/it")
        self.router.addPath("it", RouterUnitTest.TestController())
        self.router.route(request)
        self.assertEqual(self.actualRequest, request)

    def test_pathWithDynamicData(self):
        self.router.addPath("a", RouterUnitTest.TestController())
        request = ParsedRequest("GET", "/a/b/c")
        self.router.route(request)
        self.assertEqual(self.actualRequest, request)

    def test_rootPath(self):
        self.router.addPath("", RouterUnitTest.TestController())
        request = ParsedRequest("GET", "/")
        self.router.route(request)
        self.assertEqual(self.actualRequest, request)

    class TestController(Controller):
        def __init__(self):
            super(RouterUnitTest.TestController, self).__init__()

        def handle(self, parsedRequest):
            RouterUnitTest.actualRequest = parsedRequest
            return parsedRequest
