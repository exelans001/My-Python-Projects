#Tkinter basit hesap makinesi
#Güncelleme tarihi: 28.07.2025
#by exelans001

import tkinter as tk
from tkinter import messagebox
#pencere
pencere=tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("300x300")
#metin1
etiket1=tk.Label(pencere,text="1. Sayıyı giriniz: ")
etiket1.pack()
#giriş penceresi 1
sayi1=tk.Entry(pencere)
sayi1.pack()
#metin2
etiket2=tk.Label(pencere,text="2.Sayıyı giriniz: ")
etiket2.pack()
#giriş penceresi 2
sayi2=tk.Entry(pencere)
sayi2.pack()
#Seçme butonları kısmı
islem= tk.StringVar(value="+")

#combobox
tk.OptionMenu(pencere,islem,"+","-","*","/").pack()

#sonuç labeli
label_sonuc=tk.Label(pencere,text="Sonucu görmek için Hesapla butonuna basınız.")
label_sonuc.pack()
#fonksiyon
def hesap_makinesi():
    try:
       a=float(sayi1.get())
       b=float(sayi2.get())
    
       op=islem.get()
       if op=="+":
        sonuc= a+b
       elif op=="-":
        sonuc= a-b
       elif op=="*":
        sonuc= a*b
       elif op=="/":
        sonuc= a/b
       label_sonuc.configure(text=f"Sonuç= {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen her iki sayıyı da giriniz.")
        return    
    
#Sonuç butonu    
sonuc=tk.Button(pencere,text="Hesapla",command=hesap_makinesi)
sonuc.pack()
#pencereyi açık bırakma
pencere.mainloop()
