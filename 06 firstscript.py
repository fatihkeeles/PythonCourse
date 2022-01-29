import os
import time


os.system("clear")

print("""

1- NMAP CALISTIR

2- METASPLOIT CALISTIR

3- SQLMAP CALISTIR


""")


işlem = input("Hedef İşlem Numarası  : ")


if (işlem == "1"):
	os.system("clear")
	print("Nmap aracı başlatılıyor...")
	time.sleep(3)
	os.system("clear && nmap")

if (işlem == "2"):
	os.system("clear")
 	print("Metasploit aracı başlatılıyor")
        os.system("clear && msfconsole")

if (işlem == "3"):
	os.system("clear")
 	print("Sqlmap aracı başlatılıyor...")
        os.system("clear && sqlmap")

else:
	exit(0)

    
    
