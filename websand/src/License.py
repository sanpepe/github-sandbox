from websand.src.Entity import Entity

class License(Entity):
    def __init__(self, user, codecast):
        self.user = user
        self.codecast = codecast
        super(License, self).__init__()

    def getUser(self):
        return self.user

    def getCodecast(self):
        return self.codecast