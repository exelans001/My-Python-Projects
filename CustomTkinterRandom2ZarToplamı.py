#Rasgele 2 zar toplamı - Custom Tkinter Uygulaması
#Copilot tarafından oluşturulan kod exelans001 tarafından yazılmış.
#Konsolda çalışan rasgele 2 zar toplamı kodunun CustomTkinter ile GUI versiyonudur.
#Bu kod, CustomTkinter kütüphanesini kullanarak rastgele iki zarın toplamını gösteren basit bir uygulamadır.
import customtkinter as ctk
import random
#CustomTkinter'ı başlat
ctk.set_appearance_mode("dark")  # Koyu tema
ctk.set_default_color_theme("blue")  # Mavi tema
#Ana pencereyi oluştur
app = ctk.CTk()
app.title("Rasgele 2 Zar Toplamı")
app.geometry("300x200")
#Zar toplamını gösteren etiket
label = ctk.CTkLabel(app, text="Zar Toplamı: ",font=("Arial", 24))
label.pack(pady=20)
#Dice 1 ve Dice 2 için etiketler
dice1_label = ctk.CTkLabel(app, text="Zar 1: ", font=("Arial", 16))
dice1_label.pack(pady=5)
dice2_label = ctk.CTkLabel(app, text="Zar 2: ", font=("Arial", 16))
dice2_label.pack(pady=5)
#Zarları atma fonksiyonu
def roll_dice():
    dice1 = random.randint(1, 6)  # 1 ile 6 arasında rastgele bir sayı
    dice2 = random.randint(1, 6)  # 1 ile 6 arasında rastgele bir sayı
    total = dice1 + dice2  # Zarların toplamı
    # Etiketleri güncelle
    label.configure(text=f"Zar Toplamı: {total}")
    dice1_label.configure(text=f"Zar 1: {dice1}")
    dice2_label.configure(text=f"Zar 2: {dice2}")
#Zarları atma butonu
roll_button = ctk.CTkButton(app, text="Zarları At", command=roll_dice)
roll_button.pack(pady=10)
#Uygulamayı çalıştır
app.mainloop()
