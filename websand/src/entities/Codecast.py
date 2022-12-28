from websand.src.entities.Entity import Entity
import datetime


class Codecast(Entity):
    def __init__(self):
        super(Codecast, self).__init__()
        self.title = None
        self.permalink = None
        self.publicationDate = datetime.datetime.now()
        self. duration = None
        self.author = None

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setPublicationDate(self, publicationDate):
        self.publicationDate = publicationDate

    def getPublicationDate(self):
        return self.publicationDate

    def setPermalink(self, permalink):
        self.permalink = permalink

    def getPermalink(self):
        return self.permalink

    def setDuration(self, duration):
        self.duration = duration

    def getDuration(self):
        return self.duration

    def setAuthor(self, author):
        self.author = author

    def getAuthor(self):
        return self.author