import uuid

from websand.src.Gateway import Gateway

class MockGateway(Gateway):
    def __init__(self):
        self.codecasts = []
        self.users = []
        self.licenses = []

    def establishId(self, user):
        if user.getID() is None:
            user.setID(str(uuid.uuid4()))

    def findAllCodecasts(self):
        return self.codecasts

    def delete(self, codecast):
        self.codecasts.remove(codecast)

    def saveCodecast(self, codecast):
        self.codecasts.append(codecast)

    def saveUser(self, user):
        self.establishId(user=user)
        self.users.append(user)

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
