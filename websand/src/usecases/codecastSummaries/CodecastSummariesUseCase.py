# Model or data objects contain application independent business rules
#   - Used for high level policy so it can be used independently of the application
# Use case objects application dependent business rules

from websand.src.Context import Context
from websand.src.entities.License import License
from websand.src.usecases.codecastSummaries.CodecastSummariesPresenter import CodecastSummariesPresenter
from websand.src.usecases.codecastSummaries.CodecastSummariesInputBoundary import CodecastSummariesInputBoundary
from websand.src.usecases.codecastSummaries.CodecastSummariesResponseModel import CodecastSummariesResponseModel
from websand.src.usecases.codecastSummaries.CodecastSummary import CodecastSummary


class CodecastSummariesUseCase(CodecastSummariesInputBoundary):

    def summarizeCodecast(self, codecast, user):
        summary = CodecastSummary()
        summary.title = codecast.getTitle()
        summary.publicationDate = codecast.getPublicationDate()
        summary.permalink = codecast.getPermalink()
        summary.isViewable = CodecastSummariesPresenter.isLicensedFor(License.LicenseType.VIEWING, user, codecast)
        summary.isDownloadable = CodecastSummariesPresenter.isLicensedFor(License.LicenseType.DOWNLOADING, user, codecast)

        return summary

    def summarizeCodecasts(self, user, presenter):
        responseModel = CodecastSummariesResponseModel()
        allCodecasts = Context.codecastGateway.findAllCodecastsSortedChronologically()

        for codecast in allCodecasts:
            responseModel.addCodecastSummary(self.summarizeCodecast(codecast, user))

        presenter.present(responseModel)