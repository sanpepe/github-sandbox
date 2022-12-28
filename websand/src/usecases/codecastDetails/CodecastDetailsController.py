from websand.src.Context import Context
from websand.src.http.Controller import Controller


class CodecastDetailsController(Controller):
    def __init__(self, usecase, presenter, view):
        super(CodecastDetailsController, self).__init__()
        self.usecase = usecase
        self.presenter = presenter
        self.view = view

    def handle(self, parsedRequest):
        loggedInUser = Context.gateKeeper.getLoggedInUser()
        permalink = parsedRequest
        self.usecase.requestCodecastDetails(loggedInUser, permalink, self.presenter)
        ret = self.view.generateView(self.presenter.getViewModel())

        html_ret = "HTTP/1.1 200 OK\nContent-Length: {}\nContent-Type: text/html\n\n".format(len(ret)) + ret

        return html_ret
