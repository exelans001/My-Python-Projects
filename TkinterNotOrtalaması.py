#Ortalama (Kaldı-Geçti Hesaplama) Tkinter

import tkinter as tk
from tkinter import messagebox

#Ana pencere
frame=tk.Tk()
frame.geometry("300x200")
frame.title("Not Hesaplama")

#Not 1
not_1=tk.Label(frame,text="1.Notunuzu giriniz: ")
not_1.pack()

not1_giris=tk.Entry()
not1_giris.pack()

#Not 2
not_2=tk.Label(frame,text="2.Notunuzu giriniz: ")
not_2.pack()

not2_giris=tk.Entry()
not2_giris.pack()

#Not 3
not_3=tk.Label(frame,text="3.Notunuzu giriniz: ")
not_3.pack()

not3_giris=tk.Entry()
not3_giris.pack()

#Fonksiyon
def ortalama():
    #Hata önleme
    try:
        #Not verilerini alma
        not1= int(not1_giris.get())
        not2= int(not2_giris.get())
        not3= int(not3_giris.get())
        
        #Ortalama hesaplama
        ort= (not1 + not2 + not3)/ 3
        if ort>=50:
            messagebox.showinfo("Geçti!",f"Öğrenci {ort} ile geçti.")
        else:
            messagebox.showwarning("Kaldı",f"Öğrenci {ort} ile kaldı.")
    except ValueError:
        messagebox.showerror("Hata","Lütfen sayı kullanınız!")

#Hesaplama düğmesi        
sonuc=tk.Button(frame,text="Hesapla",command=ortalama)
sonuc.pack()
     
#Ana Pencere döngüsü   
frame.mainloop()
