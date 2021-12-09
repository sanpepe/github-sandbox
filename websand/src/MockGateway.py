import uuid

from websand.src.Gateway import Gateway

class MockGateway(Gateway):
    def __init__(self):
        self.codecasts = []
        self.users = []
        self.licenses = []

    def establishId(self, entity):
        if entity.getID() is None:
            entity.setID(str(uuid.uuid4()))
        return entity

    def findAllCodecasts(self):
        return self.findAllCodecastsSortedChronologically()

    def findAllCodecastsSortedChronologically(self):
        sorted_codecasts = sorted(self.codecasts, key=lambda c: c.publicationDate)
        return sorted_codecasts

    def deleteCodecast(self, codecast):
        self.codecasts.remove(codecast)

    def saveCodecast(self, codecast):
        self.codecasts.append(self.establishId(entity=codecast))
        return codecast

    def saveUser(self, user):
        self.users.append(self.establishId(entity=user))
        return user

    def saveLicense(self, license):
        self.licenses.append(license)

    def findUser(self, username):
        for user in self.users:
            if user.getUsername() == username:
                return user

        return None

    def findCodecastByTitle(self, codecastTitle):
        for codecast in self.codecasts:
            if codecast.getTitle() == codecastTitle:
                return codecast

        return None

    def findLicensesForUserAndCodecast(self, user, codecast):
        resultLicenses = []
        for license in self.licenses:
            if license.getUser().isSame(user) and\
              license.getCodecast().isSame(codecast):
                resultLicenses.append(license)

        return resultLicenses
