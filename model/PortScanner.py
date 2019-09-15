import socket
from model.Scanner import Scanner

class PortScanner(Scanner):

    def __init__(self, view, target):
        Scanner.__init__(self, view)

        self.target       = target
        self.targetIP     = socket.gethostbyname(target)

    def NewInstance(self, target):
        self.target       = target
        self.targetIP     = socket.gethostbyname(target)

    def StartScan(self, fromPort, toPort):
        view = self.view

        try:
            for port in range (fromPort, toPort):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((slef.targetIP, port))

                view.PrintBooleanRow("Port :" + str(port), (result == 0), ["OPEN", "CLOSE"])

                sock.close()
        except Exception:
            view.Print("There was an error.")

            

