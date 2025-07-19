#Yaş bilgisi alma sistemi
import tkinter as tk
from tkinter import messagebox

#Ana çerçeve
frame= tk.Tk()
frame.geometry("200x100")
frame.title("Yaş Sistemi")


#Giriş başlığı
label=tk.Label(frame,text="Yaşınızı giriniz: ")
label.pack()

#Giriş kutusu
entry=tk.Entry()
entry.pack()

#Fonksiyon
def yas_bilgi():
    try:
        yas = int(entry.get())
        if yas < 18:
            messagebox.showerror("Uyarı!", "Yaşınız 18'den küçük!")
        elif yas > 18:
            messagebox.showinfo("Hoşgeldiniz", f"Yaşınız: {yas}")
        else:
            messagebox.showwarning("Dikkat!", "Yaşınız: 18")
    except ValueError:
        messagebox.showerror("Hata!", "Lütfen geçerli bir sayı girin.")

#Giriş kutusu düğmesi    
button=tk.Button(frame,text="Hatırlama",command=yas_bilgi)
button.pack()

#ana döngü
frame.mainloop()
