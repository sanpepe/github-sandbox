from websand.src.Context import Context
from websand.src.usecases.codecastDetails.PresentableCodecastDetails import PresentableCodecastDetails
from websand.src.usecases.codecastSummaries.CodecastSummariesPresenter import CodecastSummariesPresenter
from websand.src.entities.License import License

class CodecastDetailsUseCase:

    def requestCodecastDetails(self, loggedInUser, permalink):
        pcd = PresentableCodecastDetails()

        codecast = Context.codecastGateway.findCodecastByPermalink(permalink)

        if codecast is None:
            pcd.wasFound = False
            return pcd
        else:
            pcd.wasFound = True
            CodecastSummariesPresenter.formatSummaryFields(loggedInUser, codecast, pcd)
            return pcd