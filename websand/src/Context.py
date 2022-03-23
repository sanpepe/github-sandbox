#from websand.src.Gateway import Gateway
from websand.src.gateways.UserGateway import UserGateway
from websand.src.gateways.CodecastGateway import CodecastGateway
from websand.src.gateways.LicenseGateway import LicenseGateway
from websand.src.GateKeeper import GateKeeper

class Context:
    #gateway = Gateway()
    userGateway = UserGateway()
    codecastGateway = CodecastGateway()
    licenseGateway = LicenseGateway()
    gateKeeper = GateKeeper()