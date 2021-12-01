from websand.src.Entity import Entity

class Codecast(Entity):
    def __init__(self):
        super(Codecast, self).__init__()
        self.title = None
        self.publicationDate = None

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setPublicationDate(self, publicationDate):
        self.publicationDate = publicationDate

    def getPublicationDate(self):
        return self.publicationDate