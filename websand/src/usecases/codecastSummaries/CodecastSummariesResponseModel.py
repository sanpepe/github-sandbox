from websand.src.usecases.codecastSummaries.CodecastSummary import CodecastSummary

class CodecastSummariesResponseModel:
    def __init__(self):
        self.codecastSummaries = []
    
    def getCodecastSummaries(self):
        return self.codecastSummaries

    def addCodecastSummary(self, summary):
        return self.codecastSummaries.append(summary)