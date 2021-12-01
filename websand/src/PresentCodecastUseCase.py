# Model or data objects contain application independent business rules
#   - Used for high level policy so it can be used independently of the application
# Use case objects application dependent business rules

from websand.src.Context import Context
from websand.src.PresentableCodecast import PresentableCodecast

class PresentCodecastUseCase:

    def presentCodecasts(self, loggedInUser):
        presentableCodecasts = []
        allCodecasts = Context.gateway.findAllCodecasts()
        for codecast in allCodecasts:
            cc = PresentableCodecast()
            cc.title = codecast.getTitle()
            cc.publicationDate = codecast.getPublicationDate()
            cc.isViewable = self.isLicensedToViewCodecast(user=loggedInUser, codecast=codecast)
            presentableCodecasts.append(cc)

        return presentableCodecasts

    def isLicensedToViewCodecast(self, user, codecast):
        licenses = Context.gateway.findLicensesForUserAndCodecast(user=user, codecast=codecast)
        return not (len(licenses) == 0)