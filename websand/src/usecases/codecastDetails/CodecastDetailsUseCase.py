from websand.src.Context import Context
from websand.src.usecases.codecastDetails.CodecastDetails import CodecastDetails
from websand.src.usecases.codecastDetails.CodecastDetailsResponseModel import CodecastDetailsResponseModel
from websand.src.usecases.codecastDetails.CodecastDetailsInputBoundary import CodecastDetailsInputBoundary
from websand.src.usecases.codecastSummaries.CodecastSummariesPresenter import CodecastSummariesPresenter
from websand.src.entities.License import License



class CodecastDetailsUseCase(CodecastDetailsInputBoundary):

    def getCodecastDetails(self, user, codecast):
        details = CodecastDetails()
        details.title = codecast.getTitle()
        details.publicationDate = codecast.getPublicationDate()
        details.permalink = codecast.getPermalink()
        details.duration = codecast.getDuration()
        details.author = codecast.getAuthor()
        details.isViewable = CodecastSummariesPresenter.isLicensedFor(License.LicenseType.VIEWING, user, codecast)
        details.isDownloadable = CodecastSummariesPresenter.isLicensedFor(License.LicenseType.DOWNLOADING, user, codecast)
        return details

    def requestCodecastDetails(self, user, permalink, presenter):
        responseModel = CodecastDetailsResponseModel()

        codecast = Context.codecastGateway.findCodecastByPermalink(permalink)
        if codecast:
            responseModel.setCodecastDetails(self.getCodecastDetails(user, codecast))
        presenter.present(responseModel)
