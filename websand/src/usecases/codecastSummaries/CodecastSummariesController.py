
from websand.src.usecases.codecastSummaries.CodecastSummariesUseCase import CodecastSummariesUseCase
from websand.src.usecases.codecastSummaries.CodecastSummariesView import CodecastSummariesView

from websand.src.Context import Context

from websand.src.http.Router import Router
from websand.src.http.ParsedRequest import ParsedRequest
from websand.src.http.Controller import Controller


class CodecastSummariesController(Controller):
    def __init__(self):
        super(CodecastSummariesController, self).__init__()

    def handle(self, parsedRequest):
        usecase = CodecastSummariesUseCase()
        bob = Context.userGateway.findUserByName("Bob")
        view = CodecastSummariesView()
        html = view.toHTML(usecase.presentCodecasts(bob))
        return self.makeResponse(html)

