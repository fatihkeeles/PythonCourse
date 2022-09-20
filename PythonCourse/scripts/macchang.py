import subprocess
import optparse
from termcolor import colored

def main():
	
	parser = optparse.OptionParser("Usage of the program : " + " -i <interface>" + " -m <macaddress>")
	parser.add_option("-i", dest="interface", type="string", help="interfaces")
	parser.add_option("-m", dest="mac_address", type="string", help="new mac address")
	(options, args) = parser.parse_args()
	interface = options.interface
	mac_address = options.mac_address
	if (interface == None) and (mac_address == None):
	    print(parser.usage)
	    exit(0)
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
	subprocess.call(["ifconfig",interface,"up"])
	print(colored("Your new mac address : %s " %(mac_address),"green"))

main()
