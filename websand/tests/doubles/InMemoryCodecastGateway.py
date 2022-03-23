from websand.tests.doubles.GatewayUtilities import GatewayUtilities
from websand.src.gateways.CodecastGateway import CodecastGateway

class InMemoryCodecastGateway(GatewayUtilities, CodecastGateway):

    def findAllCodecastsSortedChronologically(self):
        sorted_codecasts = sorted(self.getEntities(), key=lambda c: c.publicationDate)
        return sorted_codecasts

    def findCodecastByTitle(self, codecastTitle):
        for codecast in self.getEntities():
            if codecast.getTitle() == codecastTitle:
                return codecast

    def findCodecastByPermalink(self, permalink):
        for codecast in self.getEntities():
            if codecast.getPermalink() == permalink:
                return codecast