from websand.src.usecases.codecastSummaries.CodecastSummariesResponseModel import CodecastSummariesResponseModel

# Presentation objects alwasy hold strings
class PresentableCodecastDetails(CodecastSummariesResponseModel):
    def __init__(self):
        super(PresentableCodecastDetails, self).__init__()
        self.wasFound = None
