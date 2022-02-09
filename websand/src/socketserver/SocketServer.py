import socket
import threading

class GenericThread (threading.Thread):
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
        #print("GenericThread Exiting {} - {} with params {}".format(self.name, self.func.__name__, str(self.param)))

    def get_returns(self):
        #print("GenericThread Returning {} ".format(str(self.returns)))
        return self.returns


class SocketServer:
    TIMEOUT = 10

    def __init__(self, port, service):
        self.port = port
        self.service = service
        self.running = False

        self.mainThread = GenericThread(self.runnable)
        self.serviceSocket = None
        self.serverSocket = socket.socket() # socket.AF_INET, socket.SOCK_STREAM
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.setTimeout(SocketServer.TIMEOUT)
        self.serverSocket.bind(('', self.port))
        self.serverSocket.listen(1)

    def setTimeout(self, timeout):
        self.TIMEOUT = timeout
        self.serverSocket.settimeout(timeout)

    def getPort(self):
        return self.port

    def getService(self):
        return self.service

    def setService(self, s):
        self.service = s

    def isRunning(self):
        return self.running

    def runnable(self):
        while self.running:
            try:
                self.serviceSocket, addr = self.serverSocket.accept()
                self.service.serve(self.serviceSocket)
            except socket.timeout:
                #print("Timeout after {}s".format(SocketServer.TIMEOUT))
                break
            except socket.error as e:
                err = e.args[0]
                if err == errno.EWOULDBLOCK:
                    #print("no data")
                    continue

    def start(self):
        self.running = True
        self.mainThread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.mainThread.join()
        self.serverSocket.shutdown(socket.SHUT_RDWR)
        self.serverSocket.close()
        #print("server stop", self.serverSocket)