from websand.src.usecases.codecastSummaries.CodecastSummariesOutputBoundary import CodecastSummariesOutputBoundary

class CodecastSummariesOutputBoundarySpy(CodecastSummariesOutputBoundary):
    def __init__(self):
        self.viewModel = ""
        self.responseModel = None

    def getViewModel(self):
        return self.viewModel

    def present(self, responseModel):
        self.responseModel = responseModel