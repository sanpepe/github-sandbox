from threading import Semaphore

class SocketService:
    def __init__(self):
        self.sem = Semaphore()
        #super(User, self).__init__()

    def serve(self, s):
        pass

    def wait(self):
        self.sem.acquire()

    def notify(self):
        self.sem.release()