#from websand.src.Gateway import Gateway
from websand.src.UserGateway import UserGateway
from websand.src.CodecastGateway import CodecastGateway
from websand.src.LicenseGateway import LicenseGateway
from websand.src.GateKeeper import GateKeeper

class Context:
    #gateway = Gateway()
    userGateway = UserGateway()
    codecastGateway = CodecastGateway()
    licenseGateway = LicenseGateway()
    gateKeeper = GateKeeper()