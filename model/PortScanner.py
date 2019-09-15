import socket

from datetime import datetime


class PortScanner(Scanner):

    def __init__(self, view, target):
        Scanner.__init__(self, view)

        self.target       = target
        self.targetIP     = socket.gethostbyname(target)

    def NewInstance(self, target):
        self.target       = target
        self.targetIP     = socket.gethostbyname(target)

    def StartScan(self, fromPort, toPort, mode = "full_scan"):
        try:
            for port in range (fromPort, toPort):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((targetIP, p))

                if result == 0:
                    view.print("Port " + str(port) + "is open!")
                else:
                    view.print("Port " + str(port) + "is close!")
                
                sock.close()
        except Exception:
            view.print("There was an error.")
            