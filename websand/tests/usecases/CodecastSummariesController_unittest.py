import unittest
import datetime

from websand.src.usecases.codecastSummaries.CodecastSummariesController import CodecastSummariesController
from websand.src.usecases.codecastSummaries.CodecastSummariesResponseModel import CodecastSummariesResponseModel
from websand.src.usecases.codecastSummaries.CodecastSummariesView import CodecastSummariesView
from websand.src.usecases.codecastSummaries.CodecastSummariesInputBoundary import CodecastSummariesInputBoundary
from websand.src.usecases.codecastSummaries.CodecastSummariesOutputBoundary import CodecastSummariesOutputBoundary

from websand.src.http.ParsedRequest import ParsedRequest

from websand.src.Context import Context


from websand.tests.TestSetup import TestSetup

class CodecastSummariesInputBoundarySpy(CodecastSummariesInputBoundary):
    def __init__(self):
        self.summarizeCodecastWasCalled = False
        self.requestedUser = None
        self.outputBoundary = None

    def summarizeCodecasts(self, loggedInUser, presenter):
        self.summarizeCodecastWasCalled = True
        self.requestedUser = loggedInUser
        self.outputBoundary = presenter

class CodecastSummariesOutputBoundarySpy(CodecastSummariesOutputBoundary):
    def __init__(self):
        self.responseModel = None

    def summarizeCodecasts(self, loggedInUser, presenter):
        pass

    def getResponseModel(self):
        return self.responseModel


class CodecastSummariesViewSpy(CodecastSummariesView):
    def __init__(self):
        self.generateViewWasCalled = False
        self.responseModel = None

    def generateView(self, responseModel):
        self.responseModel = responseModel
        self.generateViewWasCalled = True
        return None

class CodecastSummariesControllerUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CodecastSummariesControllerUnitTest, self).__init__(*args, **kwargs)
        pass

    def setUp(self):
        TestSetup.setupSampleData()
        self.usecaseSpy = CodecastSummariesInputBoundarySpy()
        self.presenterSpy = CodecastSummariesOutputBoundarySpy()
        self.viewSpy = CodecastSummariesViewSpy()
        self.controller = CodecastSummariesController(self.usecaseSpy, self.presenterSpy, self.viewSpy)

    def test_inputBoundaryInvocation(self):
        request = ParsedRequest("GET", "/")
        self.controller.handle(request)
        loggedInUser = Context.userGateway.findUserByName("Bob").getID()

        self.assertTrue(self.usecaseSpy.summarizeCodecastWasCalled)
        self.assertEqual(loggedInUser, self.usecaseSpy.requestedUser.getID())
        self.assertIsNotNone(self.usecaseSpy.outputBoundary)
        self.assertIs(self.presenterSpy, self.usecaseSpy.outputBoundary)

    def test_controllerSendsTheResponseModelToView(self):
        self.presenterSpy.responseModel = CodecastSummariesResponseModel()
        request = ParsedRequest("GET", "/")
        self.controller.handle(request)
        self.assertTrue(self.viewSpy.generateViewWasCalled)
        self.assertIs(self.presenterSpy.responseModel, self.viewSpy.responseModel)

    def test_githubcraze(self):
        return True