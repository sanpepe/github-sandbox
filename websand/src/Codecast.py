class Codecast:
    def __init__(self):
        self.title = None
        self.pubilicationDate = None

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setPublicationDate(self, publicationDate):
        self.pubilicationDate = publicationDate;

    def isSame(self, codecast):
        return True