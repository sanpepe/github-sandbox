import socket
import errno
import os

from websand.src.view.ViewTemplate import ViewTemplate
from websand.src.socketserver.SocketServer import SocketServer
from websand.src.socketserver.SocketService import SocketService
from websand.tests.TestSetup import TestSetup


def getFrontPage():
    codecastView = ViewTemplate.create("codecast.html")
    frontPageView = ViewTemplate.create("frontpage.html")

    codecastView.replace("title", "Title Ep1 Pepe")

    frontPageView.replace("codecasts", codecastView.getContent())

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
        TestSetup.setupContext()

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