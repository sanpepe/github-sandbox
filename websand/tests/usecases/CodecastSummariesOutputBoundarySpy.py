from websand.src.usecases.codecastSummaries.CodecastSummariesOutputBoundary import CodecastSummariesOutputBoundary

class CodecastSummariesOutputBoundarySpy(CodecastSummariesOutputBoundary):
    def __init__(self):
        self.viewModel = None

    def summarizeCodecasts(self, loggedInUser, presenter):
        pass

    def getViewModel(self):
        return self.viewModel
