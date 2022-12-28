from websand.src.usecases.codecastDetails.CodecastDetails import CodecastDetails

class CodecastDetailsResponseModel:
    def __init__(self):
        self.codecastDetails = CodecastDetails.CodecastDetailsNotFound()
    
    def getCodecastDetails(self):
        return self.codecastDetails

    def setCodecastDetails(self, details):
        self.codecastDetails = details