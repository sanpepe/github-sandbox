class Entity:
    def __init__(self):
        self.ID = None

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def isSame(self, entity):
        if self.ID is None or entity.ID is None:
            return False
        return self.ID == entity.ID