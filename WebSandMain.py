import socket
import errno
import os

from websand.src.view.ViewTemplate import ViewTemplate
from websand.src.socketserver.SocketServer import SocketServer
from websand.src.socketserver.SocketService import SocketService
from websand.src.PresentCodecastUseCase import PresentCodecastUseCase
from websand.src.Context import Context

from websand.tests.TestSetup import TestSetup

def getFrontPage():
    usecase = PresentCodecastUseCase()
    presentableCodecasts = usecase.presentCodecasts(Context.userGateway.findUserByName("Bob"))

    codecastlines = ""
    for pc in presentableCodecasts:
        codecastTemplate = ViewTemplate.create("codecast.html")
        codecastTemplate.replace("title", pc.title)
        codecastTemplate.replace("publicationDate", pc.publicationDate)

        # Staged
        codecastTemplate.replace("thumbnail", "https://via.placeholder.com/400x200.png?text=Codecast")
        codecastTemplate.replace("author", "Uncle Bob")
        codecastTemplate.replace("duration", "58 min.")
        codecastTemplate.replace("contentActions", "Buying Options go here.")

        codecastlines += codecastTemplate.getContent() + "<br>"


    frontPageView = ViewTemplate.create("frontpage.html")
    frontPageView.replace("codecasts", codecastlines)

    return frontPageView.getContent()

def makeResponse(content):
    response = "HTTP/1.1 200 OK\nContent-Length: {}\n\n".format(len(content)) + content
    return response


class MainService(SocketService):
    def __init__(self):
        super(MainService, self).__init__()

    def doService(self, s):
        #fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
        try:
            request = s.recv(2**10).decode()
            print("request msg:\n" + request)
            frontPage = getFrontPage()
            response = makeResponse(frontPage)
            print("response msg:\n" + response)
            s.sendall(response.encode())
        except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                print("no data")
                pass
        else:
            pass

    def serve(self, s):
        self.wait()
        self.doService(s)
        self.notify()
        s.close()


class Main():
    def __init__(self, *args, **kwargs):
        TestSetup.setupSampleData()

    def getServer(self):
        return self.server

    def getCodecastGateway(self):
        return self.codecastGateway

    def run(self):
        self.mainService = MainService()
        self.server = SocketServer(8080, self.mainService)
        self.server.start()

if __name__ == "__main__":
    SocketServer.TIMEOUT = None
    main_obj = Main()
    main_obj.run()
    #getFrontPage()