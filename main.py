from view.Console import Console
from model.PortScanner import PortScanner




mainView = Console()


portScanner = PortScanner("scanme.nmap.org")

print("\cls")

for port in range (1, 128):
    result = portScanner.StartScan(port)
    mainView.PrintBooleanRow("Port : " + str(result['port']), (result['result'] == 0), ["OPEN", "CLOSE"])
