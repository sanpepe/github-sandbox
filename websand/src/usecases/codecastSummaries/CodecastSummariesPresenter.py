from websand.src.Context import Context
from websand.src.entities.License import License

from websand.src.usecases.codecastSummaries.PresentableCodecastSummary import PresentableCodecastSummary

class CodecastSummariesPresenter:
    dateFormat = "%m/%d/%Y"

    @staticmethod
    def formatCodecast(loggedInUser, codecast):
        cc = PresentableCodecastSummary()
        CodecastSummariesPresenter.formatSummaryFields(loggedInUser, codecast, cc)
        return cc

    @staticmethod
    def formatSummaryFields(loggedInUser, codecast, details):
        details.title = codecast.getTitle()
        details.publicationDate = codecast.getPublicationDate().strftime(CodecastSummariesPresenter.dateFormat)
        details.isViewable = CodecastSummariesPresenter.isLicensedFor(licenseType=License.LicenseType.VIEWING, user=loggedInUser, codecast=codecast)
        details.isDownloadable = CodecastSummariesPresenter.isLicensedFor(licenseType=License.LicenseType.DOWNLOADING, user=loggedInUser, codecast=codecast)
        details.permalink = codecast.getPermalink()

    @staticmethod
    def isLicensedFor(licenseType, user, codecast):
        licenses = Context.licenseGateway.findLicensesForUserAndCodecast(user=user, codecast=codecast)
        for l in licenses:
            if l.getType() == licenseType:
                return True
        return False