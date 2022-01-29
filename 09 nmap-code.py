import os
import time


os.system("clear")

print("""

 _      _      ____  ____        ____  ____  ____  _____
/ \  /|/ \__/|/  _ \/  __\      /   _\/  _ \/  _ \/  __/
| |\ ||| |\/||| / \||  \/|_____ |  /  | / \|| | \||  \  
| | \||| |  ||| |-|||  __/\____\|  \__| \_/|| |_/||  /_ 
\_/  \|\_/  \|\_/ \|\_/         \____/\____/\____/\____\
                                                        

1- Hızlı Tarama yap.

2- Servis ve versiyon bilgilerine eriş.

3- Sadece açık portlar üzerinden tarama gerçekleştir.
                                                        
""")


işlem = input("Hedef işlem numaranızı giriniz : ")


if (işlem == "1"):
	os.system("clear")
	ip = input("Tarama yapmak istediğiniz İp adresini girin : ")
	os.system("clear && nmap -f "+ip)
	
if (işlem == "2"):
	os.system("clear")
	ip2 = input("Tarama yapmak istediğiniz İp adresini girin : ")
	os.system("clear && nmap -sS -sV "+ip2)
	
if (işlem == "3"):
	os.system("clear")
	ip3 = input("Tarama yapmak istediğiniz İp adresini girin : ")
	os.system("clear && nmap --open "+ip3)
	
else:
	exit(0)


