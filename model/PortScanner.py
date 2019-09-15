import socket
from model.Scanner import Scanner

class PortScanner(Scanner):

    def __init__(self, target):
        Scanner.__init__(self)

        self.target       = target
        self.targetIP     = socket.gethostbyname(target)

    def NewInstance(self, target):
        self.target       = target
        self.targetIP     = socket.gethostbyname(target)

    def StartScan(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((self.targetIP, port))
            sock.close()

            return {'port': port, 'result' : result}
        except Exception:
            return None


