import os 
import time

os.system("clear")

print("""

1 - Nmap Çalıştır
2 - Metasploit çalıştır
3 - sqlmap çalıştır
4 - wireshark çalıştır



""")


proc = input("Yapılacak işlem numarasını giriniz : ")

if (proc == "1"):
	os.system("clear")
	print("Nmap aracı çalıştırılıyor...")
	time.sleep(1)
	os.system("clear && nmap")

if (proc == "2"):
	os.system("clear")
	print("Metasploit framework çalıştırılıyor...")
	time.sleep(1)
	os.system("clear && msfconsole")
	
if (proc == "3"):
	os.system("clear")
	print("SqlMap aracı çalıştırılıyor...")
	time.sleep(1)
	os.system("clear && sqlmap")
	
if (proc == "4"):
	os.system("clear")
	print("WireShark aracı çalıştırılıyor...")
	time.sleep(1)
	os.system("clear && wireshark")
	
else:
     exit()
