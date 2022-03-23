# PYTHONPATH=../ && python3 -m unittest websand/tests/CodecastSummariesUseCase_unittest.py
import unittest
import datetime

from websand.src.usecases.codecastSummaries.CodecastSummariesUseCase import CodecastSummariesUseCase
from websand.src.entities.User import User
from websand.src.entities.Codecast import Codecast
from websand.src.entities.License import License
from websand.src.Context import Context

from websand.tests.TestSetup import TestSetup

class CodecastSummariesUseCaseUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CodecastSummariesUseCaseUnitTest, self).__init__(*args, **kwargs)
        self.user = None
        self.codecast = None
        self.usecase = None

    def setUp(self):
        TestSetup.setupContext()
        self.user = Context.userGateway.save(User("User"))
        self.codecast = Context.codecastGateway.save(Codecast())
        self.usecase = CodecastSummariesUseCase()

    def test_userWithoutViewLicense_cannotViewCodecast(self):
        ret = self.usecase.isLicensedFor(licenseType=License.LicenseType.VIEWING, user=self.user, codecast=self.codecast)
        self.assertFalse(ret)

    def test_userWithViewLicense_canViewCodecast(self):
        viewLicense = License(lintype=License.LicenseType.VIEWING, user=self.user, codecast=self.codecast)
        Context.licenseGateway.save(viewLicense)
        ret = self.usecase.isLicensedFor(licenseType=License.LicenseType.VIEWING, user=self.user, codecast=self.codecast)
        self.assertTrue(ret)

    def test_userWithoutViewLicense_cannotViewOtherUsersCodecast(self):
        otherUser = Context.userGateway.save(User("OtherUser"))
        viewLicense = License(lintype=License.LicenseType.VIEWING, user=self.user, codecast=self.codecast)
        Context.licenseGateway.save(viewLicense)
        ret = self.usecase.isLicensedFor(licenseType=License.LicenseType.VIEWING, user=otherUser, codecast=self.codecast)
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