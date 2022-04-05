from websand.src.usecases.codecastSummaries.CodecastSummaryViewModel import CodecastSummaryViewModel

# Presentation objects alwasy hold strings
class PresentableCodecastDetails(CodecastSummaryViewModel):
    def __init__(self):
        super(PresentableCodecastDetails, self).__init__()
        self.wasFound = None
