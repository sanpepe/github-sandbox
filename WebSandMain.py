# PYTHONPATH=../ && python3 WebSandMain.py

import socket
import errno
import os

from websand.src.view.ViewTemplate import ViewTemplate
from websand.src.socketserver.SocketServer import SocketServer
from websand.src.socketserver.SocketService import SocketService
from websand.src.usecases.codecastSummaries.CodecastSummariesUseCase import CodecastSummariesUseCase
from websand.src.usecases.codecastSummaries.CodecastSummariesController import CodecastSummariesController
from websand.src.Context import Context
from websand.src.http.RequestParser import RequestParser

from websand.src.http.Router import Router
from websand.src.http.ParsedRequest import ParsedRequest
from websand.src.http.Controller import Controller

from websand.tests.TestSetup import TestSetup



class MainService(SocketService):
    def __init__(self):
        super(MainService, self).__init__()
        self.router = Router()
        self.router.addPath("", CodecastSummariesController(None. None))
        #self.router.addPath("episode", CodecastDetailContoller())

    def doService(self, s):
        #fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
        try:
            reader = s.recv(2**10).decode()
            lines = reader.splitlines()
            print("request msg:\n", lines)
            request = RequestParser().parse(lines[0])
            response = self.router.route(request)
            print("response msg:\n", response)
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