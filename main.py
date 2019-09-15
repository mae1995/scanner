from view.Console import Console
from model.PortScanner import PortScanner




mainView = Console()


portScanner = PortScanner(mainView, "scanme.nmap.org")
portScanner.StartScan(1,128)