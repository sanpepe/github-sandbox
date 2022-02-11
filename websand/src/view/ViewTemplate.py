import os

class ViewTemplate:
    def __init__(self, rawStringTemplate):
        self.template = rawStringTemplate

    @staticmethod
    def create(resourceName):
        resourcePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "resources", "html", resourceName)
        with open(resourcePath, 'r') as f:
            rawStringTemplate = f.read()

        return ViewTemplate(rawStringTemplate)


    def replace(self, tagName, content):
        self.template = self.template.replace("${"+tagName+"}", content)

    def getContent(self):
        return self.template