from websand.src.entities.Entity import Entity

class User(Entity):
    def __init__(self, username):
        self.username = username
        super(User, self).__init__()

    def getUsername(self):
        return self.username