from view.Console import Console
from model.PortScanner import PortScanner


class Controller:

    def __init__(self):
        self.isRunnig = True

    def Init(self):
        mainView = Console()
        portScanner = PortScanner("scanme.nmap.org")

        print("PortScanner is Running now...")

        for port in range (1, 128):
            result = portScanner.StartScan(port)
            mainView.PrintBooleanRow("Port : " + str(result['port']), (result['result'] == 0), ["OPEN", "CLOSE"])

