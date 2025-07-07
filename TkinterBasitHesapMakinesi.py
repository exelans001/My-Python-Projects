#Tkinter basit hesap makinesi

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

tk.Radiobutton(pencere,text="+",variable=islem,value="+").pack()
tk.Radiobutton(pencere,text="-",variable=islem,value="-").pack()
tk.Radiobutton(pencere,text="*",variable=islem,value="*").pack()
tk.Radiobutton(pencere,text="/",variable=islem,value="/").pack()
#fonksiyon
def hesap_makinesi():
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
    messagebox.showinfo("Sonuç",f"Sonuç= {sonuc}")
#Sonuç butonu    
sonuc=tk.Button(pencere,text="Hesapla",command=hesap_makinesi)
sonuc.pack()
#pencereyi açık bırakma
pencere.mainloop()
