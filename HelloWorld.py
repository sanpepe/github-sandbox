
import socket
import time
import fcntl, os
import errno

from websand.src.socketserver.SocketServer import SocketServer
from websand.src.socketserver.SocketService import SocketService

class HelloWorldService(SocketService):
    def __init__(self):
        super(HelloWorldService, self).__init__()
        self.counter = 0
        self.response = """HTTP/1.1 200 OK

<!DOCTYPE HTML>
<!-- HTML Element -->
<html lang="en-US">

    <!-- HEAD Element -->
    <head>
        <title>Test</title>
    </head>

    <!-- BODY Element -->
    <body>
        <h1>Hello World {}</h1>
    </body>

</html>
"""

    def doService(self, s):
        #fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
        try:
            self.counter += 1
            request = s.recv(1024).decode()
            print("request msg:\n", request)

            msg = self.response.format(self.counter)
            print("response msg:\n", msg)
            s.sendall(msg.encode())
        except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                print("no data")
                pass
        else:
            print("Done", self.counter)
            pass

    def serve(self, s):
        self.wait()
        self.doService(s)
        self.notify()
        s.close()

if __name__ == "__main__":
    SocketServer.TIMEOUT = None
    port = 8080
    print("http:\\\\127.0.0.1:{}".format(port))
    service = HelloWorldService()
    server = SocketServer(port, service)
    server.start()

    #server.stop()