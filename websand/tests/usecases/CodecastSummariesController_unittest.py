import unittest
import datetime

from websand.src.usecases.codecastSummaries.CodecastSummariesController import CodecastSummariesController
from websand.src.usecases.codecastSummaries.CodecastSummaryResponseModel import CodecastSummaryResponseModel
from websand.src.usecases.codecastSummaries.CodecastSummaryInputBoundary import CodecastSummaryInputBoundary
from websand.src.usecases.codecastSummaries.CodecastSummaryOutputBoundary import CodecastSummaryOutputBoundary

from websand.src.http.ParsedRequest import ParsedRequest

from websand.src.Context import Context


from websand.tests.TestSetup import TestSetup

class CodecastSummaryInputBoundarySpy(CodecastSummaryInputBoundary):
    def __init__(self):
        self.summarizeCodecastWasCalled = False
        self.requestedUser = None
        self.outputBoundary = None

    def summarizeCodecasts(self, loggedInUser, presenter):
        self.summarizeCodecastWasCalled = True
        self.requestedUser = loggedInUser
        self.outputBoundary = presenter

class CodecastSummaryOutputBoundarySpy(CodecastSummaryOutputBoundary):
    def __init__(self):
        pass

    def summarizeCodecasts(self, loggedInUser, presenter):
        pass



class CodecastSummariesControllerUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CodecastSummariesControllerUnitTest, self).__init__(*args, **kwargs)
        pass

    def setUp(self):
        TestSetup.setupSampleData()

    def test_inputBoundaryInvocation(self):
        usecaseSpy = CodecastSummaryInputBoundarySpy()
        presenterSpy = CodecastSummaryOutputBoundarySpy()

        controller = CodecastSummariesController(usecaseSpy, presenterSpy)
        request = ParsedRequest("GET", "/")
        controller.handle(request)
        loggedInUser = Context.userGateway.findUserByName("Bob").getID()

        self.assertTrue(usecaseSpy.summarizeCodecastWasCalled)
        self.assertEqual(loggedInUser, usecaseSpy.requestedUser.getID())

        self.assertIsNotNone(usecaseSpy.outputBoundary)
        self.assertIs(presenterSpy, usecaseSpy.outputBoundary)

    def test_controllerSendsTheResponseModelToView(self):
        pass
        #usecaseSpy = CodecastSummaryInputBoundarySpy()
        #presenterSpy = CodecastSummaryOutputBoundarySpy()
        #viewSpy = CodecastSummaryView()
        #controller = CodecastSummariesController(usecaseSpy, presenterSpy, viewSpy)
        #request = ParsedRequest("GET", "/")
        #controller.handle(request)
        #self.assertTrue(viewSpy.generateViewWasCalled)
        #self.assertIs(presenterSpy.responseModel, viewSpy.reponseModel)