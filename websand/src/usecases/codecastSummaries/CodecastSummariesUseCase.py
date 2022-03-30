# Model or data objects contain application independent business rules
#   - Used for high level policy so it can be used independently of the application
# Use case objects application dependent business rules

from websand.src.Context import Context
from websand.src.entities.License import License
from websand.src.usecases.codecastSummaries.CodecastSummariesPresenter import CodecastSummariesPresenter


class CodecastSummariesUseCase:

    def presentCodecasts(self, loggedInUser):
        presentableCodecasts = []
        allCodecasts = Context.codecastGateway.findAllCodecastsSortedChronologically()

        for codecast in allCodecasts:
            presentableCodecasts.append(CodecastSummariesPresenter.formatCodecast(loggedInUser, codecast))

        return presentableCodecasts
