from websand.tests.doubles.GatewayUtilities import GatewayUtilities
from websand.src.gateways.UserGateway  import UserGateway

class InMemoryUserGateway(GatewayUtilities, UserGateway):
    def __init__(self):
        GatewayUtilities.__init__(self)

    def findUserByName(self, username):
        for user in self.getEntities():
            if user.getUsername() == username:
                return user
