import unittest
import datetime

from websand.src.usecases.codecastSummaries.CodecastSummariesController import CodecastSummariesController
from websand.src.entities.User import User
from websand.src.entities.Codecast import Codecast
from websand.src.entities.License import License
from websand.src.Context import Context

from websand.tests.TestSetup import TestSetup

class CodecastSummariesControllerUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CodecastSummariesControllerUnitTest, self).__init__(*args, **kwargs)
        pass

    def setUp(self):
        TestSetup.setupContext()
        pass

    def test_frontPage(self):
        controller = CodecastSummariesController()
        summaries = []
