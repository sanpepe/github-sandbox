from websand.src.Context import Context
from websand.src.PresentableCodecastDetails import PresentableCodecastDetails
from websand.src.License import License

class CodecastDetailsUseCase:
    dateFormat = "%m/%d/%Y"

    def requestCodecastDetails(self, loggedInUser, permalink):
        pcd = PresentableCodecastDetails()

        codecast = Context.codecastGateway.findCodecastByPermalink(permalink)

        pcd.title = codecast.title
        pcd.publicationDate = codecast.publicationDate.strftime(CodecastDetailsUseCase.dateFormat)
        return pcd