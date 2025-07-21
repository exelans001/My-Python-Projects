#Sayı Tahmin Uygulaması Tkinter Sürümü

import tkinter as tk
from tkinter import messagebox
import random

# Değişkenler
sayi = random.randint(1, 100)
skor = 100
tahminler = []

# Tahmin kontrol fonksiyonu
def tahmin_et():
    global skor
    try:
        tahmin = int(entry.get())
    except ValueError:
        messagebox.showwarning("Uyarı", "Lütfen geçerli bir sayı giriniz!")
        return

    tahminler.append(tahmin)

    if tahmin == sayi:
        skor += 50
        messagebox.showinfo("Skor", f"Tebrikler! Doğru tahmin. Skorunuz: {skor}")
        messagebox.showinfo("Tahminler", f"Denediğiniz sayılar: {tahminler}")
        frame.destroy()

    elif tahmin < sayi:
        skor -= 5
        messagebox.showinfo("Durum", "Arttır!")
    elif tahmin > sayi:
        skor -= 5
        messagebox.showinfo("Durum", "Azalt!")

    label2.config(text=f"Skorunuz: {skor}")

    if skor <= 0:
        messagebox.showinfo("Skor", f"Skorunuz {skor} olduğu için oyun bitti. Doğru sayı {sayi} idi.")
        messagebox.showinfo("Tahminler", f"Denediğiniz sayılar: {tahminler}")
        frame.destroy()

# Arayüz
frame = tk.Tk()
frame.geometry("300x400")
frame.title("Sayı Tahmin Uygulaması")

label1 = tk.Label(frame, text="1-100 arası sayı tahmin etmeye çalış! ")
label1.pack(pady=10)

label2 = tk.Label(frame, text=f"Skorunuz: {skor}")
label2.pack(pady=10)

tahmin_label = tk.Label(frame, text="Sayıyı tahmin ediniz:")
tahmin_label.pack()

entry = tk.Entry(frame)
entry.pack(pady=5)

buton = tk.Button(frame, text="Tahmin Et", command=tahmin_et)
buton.pack(pady=10)

frame.mainloop()
