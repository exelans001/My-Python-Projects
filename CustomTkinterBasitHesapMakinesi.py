#Custom Tkinter Basit Hesap Makinesi
#Bu kod, CustomTkinter kullanarak basit bir hesap makinesi uygulaması oluşturur
from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from customtkinter import CTkRadioButton, CTkEntry, CTkButton, CTkLabel
#CustomTkinter'ı başlat
frantk = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

frantk.geometry("400x400")
frantk.title("Basit Hesap Makinesi")
#Giriş alanı
entry1 = ctk.CTkEntry(frantk, width=300, height=40, placeholder_text="Birinci sayıyı girin")
entry1.pack(pady=20)
#2. Giriş alanı
entry2 = ctk.CTkEntry(frantk, width=300, height=40, placeholder_text="İkinci sayıyı girin")
entry2.pack(pady=10)
# İşlem seçimi
label_islem = ctk.CTkLabel(frantk, text="İşlem Seçin:", font=("Arial", 16))
label_islem.pack(pady=10)
# İşlem seçenekleri
islem_var = StringVar(value="toplama")
radio_toplama = ctk.CTkRadioButton(frantk, text="Toplama", variable=islem_var, value="toplama")
radio_toplama.pack(anchor=W, padx=20)
radio_cikarma = ctk.CTkRadioButton(frantk, text="Çıkarma", variable=islem_var, value="cikarma")
radio_cikarma.pack(anchor=W, padx=20)
radio_carpma = ctk.CTkRadioButton(frantk, text="Çarpma", variable=islem_var, value="carpma")
radio_carpma.pack(anchor=W, padx=20)
radio_bolme = ctk.CTkRadioButton(frantk, text="Bölme", variable=islem_var, value="bolme")
radio_bolme.pack(anchor=W, padx=20)
#Sonuç etiket
label_sonuc = ctk.CTkLabel(frantk, text="Sonuç: ", font=("Arial", 16))
label_sonuc.pack(pady=10)
#Hesapla butonu
button_hesapla = ctk.CTkButton(frantk, text="Hesapla", command=lambda: hesapla())
button_hesapla.pack(pady=10)
#Hesaplama fonksiyonu
def hesapla():
    try:
        sayi1 = int(entry1.get())
        sayi2 = int(entry2.get())
        islem = str(islem_var.get())
        
        if islem == "toplama":
            sonuc = sayi1 + sayi2
        elif islem == "cikarma":
            sonuc = sayi1 - sayi2
        elif islem == "carpma":
            sonuc = sayi1 * sayi2
        elif islem == "bolme":
            if sayi2 == 0:
                raise ZeroDivisionError("Bir sayı sıfıra bölünemez.")
            sonuc = sayi1 / sayi2
        
        label_sonuc.configure(text=f"Sonuç: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")
#Uygulamayı çalıştır
frantk.mainloop()