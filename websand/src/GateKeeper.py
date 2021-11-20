from websand.src.User import User

class GateKeeper:
    def __init__(self):
        self.loggedInUser = None

    def setLoggedInUser(self, loggedInUser):
        self.loggedInUser = loggedInUser

    def getLoggedInUser(self):
        return self.loggedInUser