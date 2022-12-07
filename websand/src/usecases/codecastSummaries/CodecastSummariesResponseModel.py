from websand.src.usecases.codecastSummaries.CodecastSummary import CodecastSummary

class CodecastSummariesResponseModel:
    def __init__(self):
        self.isViewable = False
        self.isDownloadable = False
        self.title = None
        self.publicationDate = None
        self.permalink = None
        self.codecastSummaries = []
    
    def getCodecastSummaries(self):
        return self.codecastSummaries

    def addCodecastSummary(self, summary):
        return self.codecastSummaries.append(summary)