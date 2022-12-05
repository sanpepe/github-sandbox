from websand.src.usecases.codecastSummaries.CodecastSummariesViewModel import CodecastSummariesViewModel

# Presentation objects alwasy hold strings
class PresentableCodecastDetails(CodecastSummariesViewModel):
    def __init__(self):
        super(PresentableCodecastDetails, self).__init__()
        self.wasFound = None
