import unittest
import datetime

from websand.src.usecases.codecastDetails.CodecastDetails import CodecastDetails
from websand.src.usecases.codecastDetails.CodecastDetailsUseCase import CodecastDetailsUseCase
from websand.src.usecases.codecastDetails.CodecastDetailsOutputBoundary import CodecastDetailsOutputBoundary

from websand.src.entities.User import User
from websand.src.entities.Codecast import Codecast
from websand.src.entities.License import License
from websand.src.Context import Context

from websand.tests.TestSetup import TestSetup

from websand.src.usecases.codecastSummaries.CodecastSummariesOutputBoundary import CodecastSummariesOutputBoundary

class CodecastDetailsOutputBoundarySpy(CodecastDetailsOutputBoundary):
    def __init__(self):
        self.viewModel = ""
        self.responseModel = None

    def getViewModel(self):
        return self.viewModel

    def present(self, responseModel):
        self.responseModel = responseModel

class CodecastDetailsUseCaseUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CodecastDetailsUseCaseUnitTest, self).__init__(*args, **kwargs)
        self.user = None
        self.codecast = None
        self.usecase = None
        self.presenterSpy = None

    def setUp(self):
        TestSetup.setupContext()
        self.user = Context.userGateway.save(User("User"))
        self.usecase = CodecastDetailsUseCase()
        self.presenterSpy = CodecastDetailsOutputBoundarySpy()


    def test_createCodecastDetailsUseCase(self):
        now_str = '01/02/2015'
        now = datetime.datetime.strptime(now_str, '%m/%d/%Y')
        codecast = Codecast()
        codecast.setTitle("Codecast")
        codecast.setPermalink("permalink-a")
        codecast.setPublicationDate(datetime.datetime.strptime(now_str, '%m/%d/%Y'))
        codecast = Context.codecastGateway.save(codecast)
        self.usecase.requestCodecastDetails(self.user, "permalink-a", self.presenterSpy)

        codecastDetails = self.presenterSpy.responseModel.getCodecastDetails()
        self.assertEqual("Codecast", codecastDetails.title)
        self.assertEqual(now, codecastDetails.publicationDate)

    def test_doesntCrashOnMissingCodecast(self):
        self.usecase.requestCodecastDetails(self.user, "missing", self.presenterSpy)

        self.assertIsInstance(self.presenterSpy.responseModel.getCodecastDetails(), CodecastDetails.CodecastDetailsNotFound)
