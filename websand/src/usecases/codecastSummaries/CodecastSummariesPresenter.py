from websand.src.Context import Context
from websand.src.entities.License import License

from websand.src.usecases.codecastSummaries.CodecastSummariesResponseModel import CodecastSummariesResponseModel
from websand.src.usecases.codecastSummaries.CodecastSummariesOutputBoundary import CodecastSummariesOutputBoundary
from websand.src.usecases.codecastSummaries.CodecastSummariesViewModel import CodecastSummariesViewModel


class CodecastSummariesPresenter(CodecastSummariesOutputBoundary):
    dateFormat = "%m/%d/%Y"

    def __init__(self):
        self.viewModel = None

    @staticmethod
    def isLicensedFor(licenseType, user, codecast):
        licenses = Context.licenseGateway.findLicensesForUserAndCodecast(user=user, codecast=codecast)
        for l in licenses:
            if l.getType() == licenseType:
                return True
        return False

    def makeViewable(self, codecastSummary):
        summary = CodecastSummariesViewModel.ViewableCodecastSummary()
        summary.title = codecastSummary.title
        summary.permalink = codecastSummary.permalink
        summary.publicationDate = codecastSummary.publicationDate.strftime(CodecastSummariesPresenter.dateFormat)
        summary.isDownloadable = codecastSummary.isDownloadable
        summary.isViewable = codecastSummary.isViewable
        summary.duration = str(codecastSummary.duration)
        summary.author = str(codecastSummary.author).capitalize()

        return summary

    def getViewModel(self):
        return self.viewModel

    def present(self, responseModel):
        self.viewModel = CodecastSummariesViewModel()
        for codecastSummary in responseModel.getCodecastSummaries():
            self.viewModel.addModel(self.makeViewable(codecastSummary))
