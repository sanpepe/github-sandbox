from websand.src.PresentableCodecastSummary import PresentableCodecastSummary

# Presentation objects alwasy hold strings
class PresentableCodecastDetails(PresentableCodecastSummary):
    def __init__(self):
        super(PresentableCodecastDetails, self).__init__()
        self.wasFound = None
