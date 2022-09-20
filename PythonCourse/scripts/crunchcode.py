import os
import time


min = input("Min karakter : ")
max = input("Max karakter : ")
options = input("Karakterler giriniz : ")
output = input("İsim ver  : ")


os.system("clear")
print("Worlist oluşturuluyor....")
time.sleep(2)
os.system("clear && crunch "+min+" "+max+" -o "+output)
