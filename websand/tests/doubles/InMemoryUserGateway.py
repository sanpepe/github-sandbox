from websand.tests.doubles.GatewayUtilities import GatewayUtilities
from websand.src.UserGateway  import UserGateway

class InMemoryUserGateway(GatewayUtilities, UserGateway):

    def findUserByName(self, username):
        for user in self.users:
            if user.getUsername() == username:
                return user
