from websand.src.Context import Context
from websand.src.usecases.codecastDetails.PresentableCodecastDetails import PresentableCodecastDetails
from websand.src.usecases.codecastSummaries.CodecastSummariesUseCase import CodecastSummariesUseCase
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
            CodecastSummariesUseCase.formatSummaryFields(loggedInUser, codecast, pcd)
            return pcd