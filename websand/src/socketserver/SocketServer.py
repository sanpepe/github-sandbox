import socket
import threading

class Pepe_Thread (threading.Thread):
    def __init__(self, func, params=None, name_id=""):
        threading.Thread.__init__(self)
        self.name = name_id
        self.func = func
        self.param = params
        self.returns = ()
        self.running = False

    def isRunning(self):
        return self.running

    def run(self):
        self.running = True
        if type(self.param) is tuple:
            self.returns = self.func(*self.param)
        elif type(self.param) is dict:
            self.returns = self.func(**self.param)
        else:
            if self.param is not None:
                self.returns = self.func(self.param)
            else:
                self.returns = self.func()
        self.running = False
        #print("Pepe_Thread Exiting {} - {} with params {}".format(self.name, self.func.__name__, str(self.param)))

    def get_returns(self):
        #print("Pepe_Thread Returning {} ".format(str(self.returns)))
        return self.returns


class SocketServer:
    TIMEOUT = 3

    def __init__(self, port, service):
        self.port = port
        self.service = service
        self.running = False

        self.runThread = Pepe_Thread(self.runnable)
        self.serviceSocket = None
        self.serverSocket = socket.socket()
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.setTimeout(SocketServer.TIMEOUT)
        self.serverSocket.bind(('', self.port))
        self.serverSocket.listen()

    def setTimeout(self, timeout):
        self.serverSocket.settimeout(timeout)

    def getPort(self):
        return self.port

    def getService(self):
        return self.service

    def isRunning(self):
        return self.running

    def runnable(self):
        try:
            self.serviceSocket, addr = self.serverSocket.accept()
            self.service.serve(self.serviceSocket)
        except socket.timeout:
            pass


    def start(self):
        self.runThread.start()
        self.running = True

    def stop(self):
        self.runThread.join()
        self.serverSocket.shutdown(socket.SHUT_RDWR)
        self.serverSocket.close()
        #print("server stop", self.serverSocket)
        self.running = False