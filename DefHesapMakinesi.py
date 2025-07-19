#def fonksiyonu ile basit hesap makinesi
import time

def hesap_makinesi(a,b,secim1):
    if secim1== '+':
        print("Toplam: " ,a + b)
    elif secim1== '-':
        print("Çıkarma sonucu: " ,a - b)
    elif secim1== '*':
        print("Çarpım: " ,a * b)
    elif secim1== '/':
        print("Bölüm " ,a / b)
    else:
        print("Geçerli işlem seçiniz.")
        
x=float(input("1.Sayıyı giriniz: "))
time.sleep(0.5)
y=float(input("2.Sayıyı giriniz: "))
time.sleep(0.5)
secim0=input("İşlem Seçiniz [+,-,*,/]: ") 

hesap_makinesi(x,y,secim0)      
