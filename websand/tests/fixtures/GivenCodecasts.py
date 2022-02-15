from websand.src.Context import Context
from websand.src.Codecast import Codecast

class GivenCodecasts:
    def __init__(self):
        self.title = None
        self.permalink = None
        self.publicationDate = None

    def setTitle(self, title):
        self.title = title

    def setPublished(self, pubDate):
        self.publicationDate = pubDate

    def setPermalink(self, permalink):
        self.permalink = permalink

    def execute(self):
        codecast = Codecast()
        codecast.setTitle(self.title)
        codecast.setPublicationDate(self.publicationDate)
        codecast.setPermalink(self.permalink)
        Context.codecastGateway.save(codecast)