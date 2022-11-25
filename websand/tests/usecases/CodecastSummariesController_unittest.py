import unittest
import datetime

from websand.src.usecases.codecastSummaries.CodecastSummariesController import CodecastSummariesController
from websand.src.usecases.codecastSummaries.CodecastSummaryInputBoundary import CodecastSummaryInputBoundary

from websand.src.http.ParsedRequest import ParsedRequest

from websand.src.Context import Context


from websand.tests.TestSetup import TestSetup

class CodecastSummaryInputBoundarySpy(CodecastSummaryInputBoundary):
    def __init__(self):
        self.summarizeCodecastWasCalled = False
        self.requestedUser = None

    def summarizeCodecasts(self, loggedInUser):
        self.summarizeCodecastWasCalled = True
        self.requestedUser = loggedInUser


class CodecastSummariesControllerUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CodecastSummariesControllerUnitTest, self).__init__(*args, **kwargs)
        pass

    def setUp(self):
        TestSetup.setupSampleData()

    def test_inputBoundaryInvocation(self):
        codecastSummaryInputBoundary = CodecastSummaryInputBoundarySpy()
        codecastSummaryOutputBoundary = CodecastSummaryOutputBoundarySpy()

        controller = CodecastSummariesController(codecastSummaryInputBoundary)
        request = ParsedRequest("GET", "/")
        controller.handle(request)
        loggedInUser = Context.userGateway.findUserByName("Bob").getID()

        self.assertTrue(codecastSummaryInputBoundary.summarizeCodecastWasCalled)
        self.assertEqual(loggedInUser, codecastSummaryInputBoundary.requestedUser.getID())

        #outputBoundary = codecastSummaryInputBoundary.outputBoundary
        #self.assertIsNotNone(outputBoundary)