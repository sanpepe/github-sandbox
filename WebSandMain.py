import socket
import errno

from websand.src.socketserver.SocketServer import SocketServer
from websand.src.socketserver.SocketService import SocketService
from websand.tests.TestSetup import TestSetup


def getFrontPage():
    return "<h1>Gunk</h1>"

def makeResponse(content):
    main_content = f"""<!DOCTYPE HTML>
<!-- HTML Element -->
<html lang="en-US">

    <!-- HEAD Element -->
    <head>
        <title>Test</title>
    </head>

    <!-- BODY Element -->
    <body>
        {content}
    </body>

</html>
"""
    response = "HTTP/1.1 200 OK\nContent-Length: {}\n\n".format(len(main_content)) + main_content
    return response


class MainService(SocketService):
    def __init__(self):
        super(MainService, self).__init__()

    def doService(self, s):
        #fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
        try:
            request = s.recv(1024).decode()
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