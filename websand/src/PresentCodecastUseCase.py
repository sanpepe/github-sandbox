# Model or data objects contain application independent business rules
#   - Used for high level policy so it can be used independently of the application
# Use case objects application dependent business rules

from websand.src.Context import Context
from websand.src.PresentableCodecast import PresentableCodecast
from websand.src.License import License

class PresentCodecastUseCase:
    dateFormat = "%m/%d/%Y"

    def presentCodecasts(self, loggedInUser):
        presentableCodecasts = []
        allCodecasts = Context.gateway.findAllCodecasts()

        for codecast in allCodecasts:
            presentableCodecasts.append(self.formatCodecast(loggedInUser, codecast))

        return presentableCodecasts

    def formatCodecast(self, loggedInUser, codecast):
            cc = PresentableCodecast()
            cc.title = codecast.getTitle()
            cc.publicationDate = codecast.getPublicationDate().strftime(PresentCodecastUseCase.dateFormat)
            cc.isViewable = self.isLicensedFor(licenseType=License.LicenseType.VIEWING, user=loggedInUser, codecast=codecast)
            cc.isDownloadable = self.isLicensedFor(licenseType=License.LicenseType.DOWNLOADING, user=loggedInUser, codecast=codecast)
            return cc

    def isLicensedToViewCodecast(self, user, codecast):
        return self.isLicensedFor(License.LicenseType.VIEWING, user, codecast)

    def isLicensedToDownloadCodecast(self, user, codecast):
        return self.isLicensedFor(License.LicenseType.DOWNLOADING, user, codecast)

    def isLicensedFor(self, licenseType, user, codecast):
        licenses = Context.gateway.findLicensesForUserAndCodecast(user=user, codecast=codecast)
        for l in licenses:
            if l.getType() == licenseType:
                return True
        return False