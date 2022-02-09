# PYTHONPATH=../ && python3 -m unittest websand/tests/socketserver/SocketServerTest_unittest.py
## PYTHONPATH=../ && python3 -X tracemalloc=25 -m unittest websand/tests/socketserver/SocketServerTest_unittest.py

import unittest
import socket
import time
import fcntl, os
import errno

from websand.src.socketserver.SocketServer import SocketServer
from websand.src.socketserver.SocketService import SocketService


class TestSocketService(SocketService):
    def __init__(self):
        super(TestSocketService, self).__init__()

    def doService(self, s):
        pass

    def serve(self, s):
        self.doService(s)
        s.close()
        self.notify()

class ClosingSocketService(TestSocketService):
    def __init__(self):
        super(ClosingSocketService, self).__init__()
        self.connections = 0

    def doService(self, s):
        self.connections += 1

class ReadingSocketService(TestSocketService):
    def __init__(self):
        super(ReadingSocketService, self).__init__()
        self.message = None

    def doService(self, s):
        fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
        try:
            self.message = s.recv(4096).decode()
        except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                #print("no data")
                pass
        else:
            #print(self.message)
            pass

class EchoSocketService(TestSocketService):
    def __init__(self):
        super(EchoSocketService, self).__init__()
        self.message = None

    def doService(self, s):
        fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
        try:
            self.message = s.recv(4096).decode()
            s.send(self.message.encode())
            #print("echo msg:", self.message)
        except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                #print("no data")
                pass
        else:
            #print(self.message)
            pass


class SocketServerUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SocketServerUnitTest, self).__init__(*args, **kwargs)
        self.port = None
        self.service = None
        self.server = None

    def setUp(self):
        self.port = 8042

    ## IF YOU ADD METHOD HERE IT WILL BE INHERITED IN CHILD CLASSES, ADDING 1 EXTRA TEST FOR EACH SUBCLASS!!

class SocketServerClosingServiceUnitTest(SocketServerUnitTest):
    def __init__(self, *args, **kwargs):
        super(SocketServerClosingServiceUnitTest, self).__init__(*args, **kwargs)

    def setUp(self):
        SocketServerUnitTest.setUp(self)
        self.service = ClosingSocketService()
        self.server = SocketServer(self.port, self.service)

    def tearDown(self):
        #self.server.stop()
        pass

    def test_instantiate(self):
        self.assertEqual(self.port, self.server.getPort())
        self.assertEqual(self.service, self.server.getService())
        self.server.stop()

    def test_canStartAndStopServer(self):
        self.server.setTimeout(0.01)
        self.server.start()
        self.assertTrue(self.server.isRunning())
        self.server.stop()
        self.assertFalse(self.server.isRunning())

    def test_acceptAnIncomingConnection(self):
        self.server.start()
        self.service.wait()
        ss = socket.socket() ; ss.connect(('localhost', self.port))
        self.server.stop()
        self.assertEqual(1, self.service.connections)
        ss.close()

    def test_acceptMultipleConnections(self):
        self.server.start()
        self.service.wait()
        ss1 = socket.socket() ; ss1.connect(('localhost', self.port))
        self.service.wait()
        ss2 = socket.socket() ; ss2.connect(('localhost', self.port))
        self.server.stop()
        self.assertEqual(2, self.service.connections)
        ss1.close()
        ss2.close()

class SocketServerReadingServiceUnitTest(SocketServerUnitTest):
    def __init__(self, *args, **kwargs):
        super(SocketServerReadingServiceUnitTest, self).__init__(*args, **kwargs)

    def setUp(self):
        SocketServerUnitTest.setUp(self)
        self.service = ReadingSocketService()
        self.server = SocketServer(self.port, self.service)

    def test_canSendAndReceiveData(self):
        msg = "hello"
        self.server.start()
        self.service.wait()
        ss = socket.socket() ; ss.connect(('localhost', self.port))
        ss.send(msg.encode())
        self.server.stop()
        self.assertEqual(msg, self.service.message)
        ss.close()

class SocketServerEchoServiceUnitTest(SocketServerUnitTest):
    def __init__(self, *args, **kwargs):
        super(SocketServerEchoServiceUnitTest, self).__init__(*args, **kwargs)

    def setUp(self):
        SocketServerUnitTest.setUp(self)
        self.service = EchoSocketService()
        self.server = SocketServer(self.port, self.service)

    def test_canEchoData(self):
        msg = "echo"
        self.server.start()
        self.service.wait()
        ss = socket.socket() ; ss.connect(('localhost', self.port))
        ss.send(msg.encode())

        response = ss.recv(4096).decode()
        self.server.stop()
        self.assertEqual(msg, response)
        ss.close()
