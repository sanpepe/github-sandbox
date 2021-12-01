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
        self.user = Context.gateway.saveUser(user=User("User"))
        self.codecast = Context.gateway.saveCodecast(codecast=Codecast())
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
        otherUser = Context.gateway.saveUser(user=User("OtherUser"))
        viewLicense = License(user=self.user, codecast=self.codecast)
        Context.gateway.saveLicense(license=viewLicense)
        ret = self.usecase.isLicensedToViewCodecast(user=otherUser, codecast=self.codecast)
        self.assertFalse(ret)

    def test_presentNoCodecasts(self):
        Context.gateway.deleteCodecast(self.codecast)
        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        self.assertEqual(0, len(presentableCodecasts))

    def test_presentOneCodecasts(self):
        self.codecast.setTitle("Some Title")
        self.codecast.setPublicationDate("Tomorrow")
        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        self.assertEqual(1, len(presentableCodecasts))
        presentableCodecast = presentableCodecasts[0]
        self.assertEqual("Some Title", presentableCodecast.title)
        self.assertEqual("Tomorrow", presentableCodecast.publicationDate)

    def test_presentdCodecastIsNotViewableIfNoLicense(self):
        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        presentableCodecast = presentableCodecasts[0]
        self.assertFalse(presentableCodecast.isViewable)


    def test_presentdCodecastIsViewableIfLicenseExists(self):
        Context.gateway.saveLicense(license=License(user=self.user, codecast=self.codecast))
        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        presentableCodecast = presentableCodecasts[0]
        self.assertTrue(presentableCodecast.isViewable)