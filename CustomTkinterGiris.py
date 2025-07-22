# CustomTkinterGiris.py
# Bu kod, CustomTkinter kütüphanesini kullanarak basit bir GUI uygulaması oluşturur.
# Kullanıcıdan metin girişi alır ve bir düğmeye tıklandığında bu metni gösterir.

from tkinter import *
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("system")  # Sistem görünümünü kullan
ctk.set_default_color_theme("dark-blue")  # Mavi tema ayarla

root=ctk.CTk()
root.geometry("300x400")

label= ctk.CTkLabel(root, text="Merhaba, CustomTkinter!", font=("Arial", 20))
label.pack(pady=20)

button = ctk.CTkButton(root, text="Tıkla", command=lambda: label.configure(text="Düğmeye Tıklandı!"))
button.pack(pady=20)

entry = ctk.CTkEntry(root, placeholder_text="Buraya yazın")
entry.pack(pady=20)


def show_message():
    giris = entry.get()
    if giris:
        messagebox.showinfo("Giriş", f"Giriş yaptığınız metin: {giris}")

button2 = ctk.CTkButton(root, text="Giriş Yap", command=show_message)
button2.pack(pady=20)



root.mainloop()
