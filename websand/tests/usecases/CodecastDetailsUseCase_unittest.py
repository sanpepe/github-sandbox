# PYTHONPATH=../ && python3 -m unittest websand/tests/CodecastDetailsUseCase_unittest.py
import unittest
import datetime

from websand.src.usecases.codecastDetails.CodecastDetailsUseCase import CodecastDetailsUseCase
from websand.src.entities.User import User
from websand.src.entities.Codecast import Codecast
from websand.src.entities.License import License
from websand.src.Context import Context

from websand.tests.TestSetup import TestSetup

class CodecastDetailsUseCaseUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CodecastDetailsUseCaseUnitTest, self).__init__(*args, **kwargs)
        self.user = None
        self.codecast = None
        self.usecase = None

    def setUp(self):
        TestSetup.setupContext()

        self.user = Context.userGateway.save(User("User"))
        self.usecase = CodecastDetailsUseCase()

    def test_createCodecastDetailsUseCase(self):
        now_str = '01/02/2015'

        codecast = Codecast()
        codecast.setTitle("Codecast")
        codecast.setPermalink("permalink-a")
        codecast.setPublicationDate(datetime.datetime.strptime(now_str, '%m/%d/%Y'))
        codecast = Context.codecastGateway.save(codecast)

        details = self.usecase.requestCodecastDetails(loggedInUser=self.user, permalink="permalink-a")

        self.assertEqual("Codecast", details.title)
        self.assertEqual(now_str, details.publicationDate)

    def test_doesntCrashOnMissingCodecast(self):

        details = self.usecase.requestCodecastDetails(loggedInUser=self.user, permalink="missing")

        self.assertFalse(details.wasFound)
