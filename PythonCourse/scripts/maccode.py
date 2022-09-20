import os
import time


print("""


1 - Mac adresimi göster
2 - Mac adresimi değiştir
3 - eski ayarlara geri dön


""")


opr = input("Hedef işlem numaranızı giriniz : ")


if (opr == "1"):
	print("Mac adresi bilginiz geliyor...")
	time.sleep(1)
	os.system("clear && ifconfig")
	
if (opr == "2"):
	print("Mac adresiniz değiştirliyor...")
	time.sleep(1)
	os.system("clear && macchanger -r eth0")
	
if (opr == "3"):
	print("Mac adresiniz eski ayarlara dönüyor")
	time.sleep(1)
	os.system("clear && macchanger -p eth0")


