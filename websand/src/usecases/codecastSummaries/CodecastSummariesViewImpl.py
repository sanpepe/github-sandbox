from websand.src.view.ViewTemplate import ViewTemplate
from websand.src.usecases.codecastSummaries.CodecastSummariesView import CodecastSummariesView

class CodecastSummariesViewImpl(CodecastSummariesView):
    def __init__(self):
        super(CodecastSummariesViewImpl, self).__init__()

    def generateView(self, viewModel):
        return self.toHTML(viewModel.getViewableCodecasts())

    def toHTML(self, presentableCodecasts):
        codecastlines = ""
        for pc in presentableCodecasts:
            codecastTemplate = ViewTemplate.create("codecast.html")
            codecastTemplate.replace("title", pc.title)
            codecastTemplate.replace("publicationDate", pc.publicationDate)
            codecastTemplate.replace("permalink", pc.permalink)

            # Staged
            codecastTemplate.replace("thumbnail", "https://via.placeholder.com/400x200.png?text=Codecast")
            codecastTemplate.replace("author", "Uncle Bob")
            codecastTemplate.replace("duration", "58 min.")
            codecastTemplate.replace("contentActions", "Buying Options go here.")

            codecastlines += codecastTemplate.getContent() + "<br>"


        frontPageView = ViewTemplate.create("frontpage.html")
        frontPageView.replace("codecasts", codecastlines)

        return frontPageView.getContent()