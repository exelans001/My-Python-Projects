#Tkinter Askerlik Projesi

import tkinter as tk
from tkinter import messagebox

pencere = tk.Tk()
pencere.title("Askerlik Kontrolü")
pencere.geometry("300x240")

etiket = tk.Label(pencere, text="İsim-Soyisim giriniz: ")
etiket.pack()

giris = tk.Entry(pencere)
giris.pack()

cinsiyet_secimi = tk.StringVar(value="")  # Başlangıçta boş

cinsiyet_label = tk.Label(pencere, text="Cinsiyet")
cinsiyet_label.pack()

radio1 = tk.Radiobutton(pencere, text="Erkek", variable=cinsiyet_secimi, value="Erkek")
radio2 = tk.Radiobutton(pencere, text="Kadın", variable=cinsiyet_secimi, value="Kadın")
radio1.pack()
radio2.pack()

# Yaş seçimi için
yas_secimi = tk.StringVar(value="")  # Boş başlat

yas_label = tk.Label(pencere, text="Yaş")
yas_label.pack()

yas_radio1 = tk.Radiobutton(pencere, text="18 yaş ve üzeriyim", variable=yas_secimi, value="18 ve üzeri")
yas_radio2 = tk.Radiobutton(pencere, text="18 yaş ve altıyım", variable=yas_secimi, value="18 altı")
yas_radio1.pack()
yas_radio2.pack()

def yazdir():
    isim = giris.get()
    cinsiyet = cinsiyet_secimi.get()
    yas = yas_secimi.get()

    try:
        int(isim)
        messagebox.showerror("HATA", "Lütfen sayı girmeyiniz")
        return
    except ValueError:
        pass

    if isim.strip() == "":
        messagebox.showwarning("UYARI", "Lütfen bir isim giriniz")
        return

    if cinsiyet == "":
        messagebox.showwarning("UYARI", "Lütfen cinsiyet seçiniz")
        return

    if yas == "":
        messagebox.showwarning("UYARI", "Lütfen yaş seçiniz")
        return

    if cinsiyet.lower() == "kadın":
        messagebox.showwarning("DİKKAT", "Askere gidemezsiniz!")
        return
    elif cinsiyet.lower() == "erkek" and yas == "18 altı":
        messagebox.showwarning("DİKKAT", "Askere gidemezsiniz!")
        return

    messagebox.showinfo("Sonuç", f"İsim Soyisim: {isim}\nCinsiyet: {cinsiyet}\nYaş: {yas} \nAskere gideceksiniz.")

buton = tk.Button(pencere, text="Sonuç", command=yazdir)
buton.pack()

pencere.mainloop()
