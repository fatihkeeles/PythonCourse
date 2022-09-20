import os
import time

print("""

NMAP CODE BY FATİH

1- Hızlı tarama yap
2- Servis ve Versiyon biligilerini topla
3- Sadece açık portları tara


""")


opr = input("İşlem numaranızı giriniz : ")


if (opr == "1"):
	os.system("clear")
	ip = input("Hedef ip adresini giriniz : ")
	print("Hızlı tarama gerçekleştiriliyor ",ip)
	time.sleep(2)
	os.system("clear && nmap -f "+ip)
	
if (opr == "2"):
	os.system("clear")
	ip = input("Hedef ip adresini giriniz : ")
	print("Servis ve Versiyon bilgileri tespit ediliyor ",ip)
	time.sleep(2)
	os.system("clear && nmap -sS -sV "+ip)
	
if (opr == "3"):
	os.system("clear")
	ip = input("Hedef ip adresini giriniz : ")
	print("Açık portlar taranıyor ",ip)
	time.sleep(2)
	os.system("clear && nmap --open "+ip)

else:
    exit()
	

