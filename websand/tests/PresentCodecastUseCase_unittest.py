# PYTHONPATH=../ && python3 -m unittest websand/tests/PresentCodecastUseCase_unittest.py
import unittest
import datetime

from websand.src.PresentCodecastUseCase import PresentCodecastUseCase
from websand.src.User import User
from websand.src.Codecast import Codecast
from websand.src.License import License
from websand.src.Context import Context

from websand.tests.TestSetup import TestSetup

class PresentCodecastUseCaseUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PresentCodecastUseCaseUnitTest, self).__init__(*args, **kwargs)
        self.user = None
        self.codecast = None
        self.usecase = None

    def setUp(self):
        TestSetup.setupContext()
        self.user = Context.userGateway.save(User("User"))
        self.codecast = Context.codecastGateway.save(Codecast())
        self.usecase = PresentCodecastUseCase()

    def test_userWithoutViewLicense_cannotViewCodecast(self):
        ret = self.usecase.isLicensedToViewCodecast(user=self.user, codecast=self.codecast)
        self.assertFalse(ret)

    def test_userWithViewLicense_canViewCodecast(self):
        viewLicense = License(lintype=License.LicenseType.VIEWING, user=self.user, codecast=self.codecast)
        Context.licenseGateway.save(viewLicense)
        ret = self.usecase.isLicensedToViewCodecast(user=self.user, codecast=self.codecast)
        self.assertTrue(ret)

    def test_userWithoutViewLicense_cannotViewOtherUsersCodecast(self):
        otherUser = Context.userGateway.save(User("OtherUser"))
        viewLicense = License(lintype=License.LicenseType.VIEWING, user=self.user, codecast=self.codecast)
        Context.licenseGateway.save(viewLicense)
        ret = self.usecase.isLicensedToViewCodecast(user=otherUser, codecast=self.codecast)
        self.assertFalse(ret)

    def test_presentNoCodecasts(self):
        Context.codecastGateway.delete(self.codecast)
        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        self.assertEqual(0, len(presentableCodecasts))

    def test_presentOneCodecasts(self):
        self.codecast.setTitle("Some Title")
        now_str = '05/19/2014'
        now = datetime.datetime.strptime(now_str, '%m/%d/%Y')
        self.codecast.setPublicationDate(now)
        Context.codecastGateway.save(self.codecast);

        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        self.assertEqual(1, len(presentableCodecasts))
        presentableCodecast = presentableCodecasts[0]
        self.assertEqual("Some Title", presentableCodecast.title)
        self.assertEqual(now_str, presentableCodecast.publicationDate)

    def test_presentdCodecastIsNotViewableIfNoLicense(self):
        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        presentableCodecast = presentableCodecasts[0]
        self.assertFalse(presentableCodecast.isViewable)

    def test_presentedCodecastIsViewableIfLicenseExists(self):
        viewableLicense = License(lintype=License.LicenseType.VIEWING, user=self.user, codecast=self.codecast)
        Context.licenseGateway.save(viewableLicense)
        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        presentableCodecast = presentableCodecasts[0]
        self.assertTrue(presentableCodecast.isViewable)

    def test_presentedCodecastIsDownloadableIfDownloadLicenseExists(self):
        downloadLicense = License(lintype=License.LicenseType.DOWNLOADING, user=self.user, codecast=self.codecast)
        Context.licenseGateway.save(downloadLicense)
        presentableCodecasts = self.usecase.presentCodecasts(loggedInUser=self.user)
        presentableCodecast = presentableCodecasts[0]
        self.assertTrue(presentableCodecast.isDownloadable)
        self.assertFalse(presentableCodecast.isViewable)