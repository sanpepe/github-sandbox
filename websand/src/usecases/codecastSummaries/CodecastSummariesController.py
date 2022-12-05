
from websand.src.usecases.codecastSummaries.CodecastSummariesUseCase import CodecastSummariesUseCase
from websand.src.usecases.codecastSummaries.CodecastSummariesView import CodecastSummariesView

from websand.src.Context import Context

from websand.src.http.Router import Router
from websand.src.http.ParsedRequest import ParsedRequest
from websand.src.http.Controller import Controller


class CodecastSummariesController(Controller):
    def __init__(self, usecase, presenter, view):
        super(CodecastSummariesController, self).__init__()
        self.usecase = usecase
        self.presenter = presenter
        self.view = view

    def handle(self, parsedRequest):
        loggedInUser = Context.gateKeeper.getLoggedInUser()
        self.usecase.summarizeCodecasts(loggedInUser, self.presenter)
        usecase = CodecastSummariesUseCase()
        bob = Context.userGateway.findUserByName("Bob")
        view = CodecastSummariesView()
        html = view.toHTML(usecase.presentCodecasts(bob))
        return self.makeResponse(html)

