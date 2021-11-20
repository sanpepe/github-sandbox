# PYTHONPATH=../ && python3 -m unittest websand/tests/PresentCodecastUseCase_unittest.py
import unittest
from websand.src.PresentCodecastUseCase import PresentCodecastUseCase
from websand.src.User import User
from websand.src.Codecast import Codecast
from websand.src.License import License
from websand.src.Context import Context
from websand.src.MockGateway import MockGateway

class PresentCodecastUseCaseUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PresentCodecastUseCaseUnitTest, self).__init__(*args, **kwargs)
        self.user = None
        self.codecast = None
        self.usecase = None

    def setUp(self):
        Context.gateway = MockGateway()
        self.user = User("User")
        Context.gateway.saveUser(user=self.user)
        self.codecast = Codecast()
        self.usecase = PresentCodecastUseCase()

    def test_userWithoutViewLicense_cannotViewCodecast(self):
        ret = self.usecase.isLicensedToViewCodecast(user=self.user, codecast=self.codecast)
        self.assertFalse(ret)

    def test_userWithViewLicense_canViewCodecast(self):
        viewLicense = License(user=self.user, codecast=self.codecast)
        Context.gateway.saveLicense(license=viewLicense)
        ret = self.usecase.isLicensedToViewCodecast(user=self.user, codecast=self.codecast)
        self.assertTrue(ret)

    def test_userWithoutViewLicense_cannotViewOtherUsersCodecast(self):
        otherUser = User("OtherUser")
        Context.gateway.saveUser(user=otherUser)
        viewLicense = License(user=self.user, codecast=self.codecast)
        Context.gateway.saveLicense(license=viewLicense)
        ret = self.usecase.isLicensedToViewCodecast(user=otherUser, codecast=self.codecast)
        self.assertFalse(ret)
