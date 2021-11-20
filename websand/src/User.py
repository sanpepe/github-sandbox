class User:
    def __init__(self, username):
        self.username = username
        self.ID = None

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def getUsername(self):
        return self.username

    def isSame(self, user):
        return self.ID == user.ID