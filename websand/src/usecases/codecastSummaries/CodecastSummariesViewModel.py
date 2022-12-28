from websand.src.usecases.codecastSummaries.CodecastSummariesResponseModel import CodecastSummariesResponseModel

class CodecastSummariesViewModel:
    viewableCodecastSummaries = []

    class ViewableCodecastSummary:
        def __init__(self):
            self.isViewable = False
            self.isDownloadable = False
            self.title = None
            self.publicationDate = ""
            self.permalink = None
            self.duration = ""
            self.author = ""

    def addModel(self, viewableCodecastSummary):
        CodecastSummariesViewModel.viewableCodecastSummaries.append(viewableCodecastSummary)

    def getViewableCodecasts(self):
        return CodecastSummariesViewModel.viewableCodecastSummaries