from websand.tests.doubles.GatewayUtilities import GatewayUtilities
from websand.src.gateways.LicenseGateway  import LicenseGateway

class InMemoryLicenseGateway(GatewayUtilities, LicenseGateway):

    def findLicensesForUserAndCodecast(self, user, codecast):
        resultLicenses = []
        for license in self.getEntities():
            if license.getUser().isSame(user) and license.getCodecast().isSame(codecast):
                resultLicenses.append(license)

        return resultLicenses
