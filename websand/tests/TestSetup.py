from websand.src.Context import Context
from websand.src.GateKeeper import GateKeeper
from websand.tests.doubles.InMemoryCodecastGateway import InMemoryCodecastGateway
from websand.tests.doubles.InMemoryLicenseGateway import InMemoryLicenseGateway
from websand.tests.doubles.InMemoryUserGateway import InMemoryUserGateway

class TestSetup():
    @staticmethod
    def setupContext():
        Context.userGateway = InMemoryUserGateway()
        Context.licenseGateway = InMemoryLicenseGateway()
        Context.codecastGateway  = InMemoryCodecastGateway()
        Context.gateKeeper = GateKeeper()