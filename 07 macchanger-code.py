import os
import time

os.system("clear")

print("""


 _      ____  ____ 
/ \__/|/  _ \/   _\
| |\/||| / \||  /  
| |  ||| |-|||  \__
\_/  \|\_/ \|\____/
                   

1 - MAC ADRESIMI OGREN

2 - MAC ADRESIMI DEGISTIR

3 - VARSAYILAN MAC ADRESINE GERI DON


""")


işlem = input("Hedef işlem numaranız : ")


if (işlem == "1"):
	os.system("clear && ifconfig")
	
	
if (işlem == "2"):
	os.system("clear && macchanger -r eth0")

if (işlem == "3"):
	os.system("clear && macchanger -p eth0")
