from websand.src.Context import Context
from websand.src.PresentableCodecastDetails import PresentableCodecastDetails
from websand.src.CodecastSummaryUseCase import CodecastSummaryUseCase
from websand.src.License import License

class CodecastDetailsUseCase:

    def requestCodecastDetails(self, loggedInUser, permalink):
        pcd = PresentableCodecastDetails()

        codecast = Context.codecastGateway.findCodecastByPermalink(permalink)

        if codecast is None:
            pcd.wasFound = False
            return pcd
        else:
            pcd.wasFound = True
            CodecastSummaryUseCase.formatSummaryFields(loggedInUser, codecast, pcd)
            return pcd