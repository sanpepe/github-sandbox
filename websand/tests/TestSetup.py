import datetime
from websand.src.Context import Context
from websand.src.GateKeeper import GateKeeper
from websand.src.entities.User import User
from websand.src.entities.Codecast import Codecast
from websand.src.entities.License import License

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

    @staticmethod
    def setupSampleData():
        TestSetup.setupContext()

        bob = User("Bob")
        micah = User("Micah")
        Context.userGateway.save(bob)
        Context.userGateway.save(micah)

        today = datetime.datetime.now()
        ep1 = Codecast()
        ep1.setTitle("Episode 1 - The Beginning")
        ep1.setPublicationDate(datetime.datetime.now().replace(day=today.day-1))
        ep2 = Codecast()
        ep2.setTitle("Episode 2 - The Continuation")
        ep2.setPublicationDate(today)
        Context.codecastGateway.save(ep1)
        Context.codecastGateway.save(ep2)

        bobE1 = License(License.LicenseType.VIEWING, bob, ep1)
        bobE2 = License(License.LicenseType.VIEWING, bob, ep2)
        Context.licenseGateway.save(bobE1)
        Context.licenseGateway.save(bobE2)