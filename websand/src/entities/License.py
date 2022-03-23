from enum import Enum

from websand.src.entities.Entity import Entity

class License(Entity):
    class LicenseType(Enum):
        VIEWING = 1
        DOWNLOADING = 2

    def __init__(self, lintype, user, codecast):
        self.user = user
        self.codecast = codecast
        self.license_type = lintype
        super(License, self).__init__()

    def getUser(self):
        return self.user

    def getType(self):
        return self.license_type

    def getCodecast(self):
        return self.codecast