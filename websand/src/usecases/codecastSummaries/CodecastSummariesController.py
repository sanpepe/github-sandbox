
from websand.src.usecases.codecastSummaries.CodecastSummariesUseCase import CodecastSummariesUseCase
from websand.src.usecases.codecastSummaries.CodecastSummariesViewImpl import CodecastSummariesViewImpl

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
        ret = self.view.generateView(self.presenter.getViewModel())

        html_ret = "HTTP/1.1 200 OK\nContent-Length: {}\nContent-Type: text/html\n\n".format(len(ret)) + ret

        return html_ret

