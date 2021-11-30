from websand.src.Entity import Entity

class Codecast(Entity):
    def __init__(self):
        self.title = None
        self.pubilicationDate = None
        super(Codecast, self).__init__()

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setPublicationDate(self, publicationDate):
        self.pubilicationDate = publicationDate;
