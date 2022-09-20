import socket
import subprocess
import optparse
from termcolor import colored

def banner():
	print("""
 ____  ____  ____  _____  ____  ____  ____  _      _      _____ ____   
/  __\/  _ \/  __\/__ __\/ ___\/   _\/  _ \/ \  /|/ \  /|/  __//  __\  
|  \/|| / \||  \/|  / \  |    \|  /  | / \|| |\ ||| |\ |||  \  |  \/|  
|  __/| \_/||    /  | |  \___ ||  \__| |-||| | \||| | \|||  /_ |    /  
\_/   \____/\_/\_\  \_/  \____/\____/\_/ \|\_/  \|\_/  \|\____\\_/\_\  
                                                                                                                          	
	""")
banner()


socket.setdefaulttimeout(2)
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

parser = optparse.OptionParser("Usage of the program : " + "-H <target host>" + "-p <target port>")
parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
parser.add_option("-p", dest="tgtPort", type="int", help="specify target port")
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort


if con.connect_ex((tgtHost,tgtPort)):
    print(colored("Scan Result for : %s " %(tgtHost),"blue"))
    print(colored("port is %d closed" %(tgtPort),"red"))

else:
    print(colored("Scan Result for : %s " %(tgtHost),"blue"))
    print(colored("port is %d opened" %(tgtPort),"green"))

