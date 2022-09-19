import random
import time 

print("""
Fatih keleşin sayı tahmin etme oyununa hoş geldiniz

1 - 100 arasındaki sayıyı bul ve oyunu kazan 

başarılar...
""")


sayı = random.randint(1,100)
tahminhak = 5


while True:
	tahmin = int(input("Tahmininiz nedir : "))
	
	if (tahmin == sayı):
		print("Sayı sorgulanıyor...")
		time.sleep(1)
		print("Doğru cevap tebrikler")
		break
		
	elif (tahmin > sayı):
		print("Sayı sorgulanıyor")
		time.sleep(1)
		tahminhak -= 1
		print("Daha küçük bir değer girin yanlış !")
		print("Kalan tahmin hakkınız : ",tahminhak)
		
	else:
		print("Sayı sorgulanıyor...")
		time.sleep(1)
		tahminhak-=1
		print("Daha büyük bir değer girin yanlış !")
		print("Kalan tahmin hakkınız : ",tahminhak)
		
	if (tahminhak == 0):
		print("Tahmin hakkınız bitmiştir kaybettiniz ! ")
		print("Bilgisayarın tuttuğu sayı",sayı)
		break
		
	
		
		
