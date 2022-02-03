# PYTHONPATH=../ && python3 -m unittest websand/tests/socketserver/SocketServerTest_unittest.py

import unittest
import socket
import time
from websand.src.socketserver.SocketServer import SocketServer
from websand.src.socketserver.SocketService import SocketService

class FakeSocketService(SocketService):
    def __init__(self):
        self.connections = 0
        super(FakeSocketService, self).__init__()

    def serve(self, s):
        self.connections += 1
        s.close()


class SocketServerUnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SocketServerUnitTest, self).__init__(*args, **kwargs)
        self.port = None
        self.service = None
        self.server = None

    def setUp(self):
        self.port = 8042
        self.service = FakeSocketService()
        self.server = SocketServer(self.port, self.service)

    def tearDown(self):
        #self.server.stop()
        pass

    def test_instantiate(self):
        self.assertEqual(self.port, self.server.getPort())
        self.assertEqual(self.service, self.server.getService())

    #@unittest.skip("demonstrating skipping")
    def test_canStartAndStopServer(self):
        self.server.setTimeout(0.01)
        self.server.start()
        self.assertTrue(self.server.isRunning())
        self.server.stop()
        self.assertFalse(self.server.isRunning())

    def test_acceptAnIncomingConnection(self):
        self.server.start()
        ss = socket.socket()
        ss.connect(('localhost', self.port))
        self.server.stop()

        self.assertEqual(1, self.service.connections)
        ss.close()
