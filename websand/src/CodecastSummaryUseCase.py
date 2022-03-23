# Model or data objects contain application independent business rules
#   - Used for high level policy so it can be used independently of the application
# Use case objects application dependent business rules

from websand.src.Context import Context
from websand.src.PresentableCodecastSummary import PresentableCodecastSummary
from websand.src.License import License

class CodecastSummaryUseCase:
    dateFormat = "%m/%d/%Y"

    def presentCodecasts(self, loggedInUser):
        presentableCodecasts = []
        allCodecasts = Context.codecastGateway.findAllCodecastsSortedChronologically()

        for codecast in allCodecasts:
            presentableCodecasts.append(self.formatCodecast(loggedInUser, codecast))

        return presentableCodecasts

    @staticmethod
    def formatSummaryFields(loggedInUser, codecast, details):
        details.title = codecast.getTitle()
        details.publicationDate = codecast.getPublicationDate().strftime(CodecastSummaryUseCase.dateFormat)
        details.isViewable = CodecastSummaryUseCase.isLicensedFor(licenseType=License.LicenseType.VIEWING, user=loggedInUser, codecast=codecast)
        details.isDownloadable = CodecastSummaryUseCase.isLicensedFor(licenseType=License.LicenseType.DOWNLOADING, user=loggedInUser, codecast=codecast)

    def formatCodecast(self, loggedInUser, codecast):
        cc = PresentableCodecastSummary()
        self.formatSummaryFields(loggedInUser, codecast, cc)
        return cc

    @staticmethod
    def isLicensedFor(licenseType, user, codecast):
        licenses = Context.licenseGateway.findLicensesForUserAndCodecast(user=user, codecast=codecast)
        for l in licenses:
            if l.getType() == licenseType:
                return True
        return False