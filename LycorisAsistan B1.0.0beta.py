# Lycoris Assistant B1.0.0beta
# Bu kod, Lycoris Asistan adlı bir uygulamayı oluşturur.
# Kullanıcı adını alır, mesajları balon şeklinde gösterir ve çeşitli komutları işler.
# Kullanıcı not alabilir, tarih ve saat bilgisi alabilir ve uygulamadan çıkabilir.
# Geliştirilmiştir: 2025-07-23
# ChatGPT tarafından oluşturulmuştur.Ana fikir ve tasarım exelans001 tarafından yapılmıştır.
# Bu sürüm beta aşamasındadır ve bazı özellikler eksik olabilir.
# İlk temeller exelans001 tarafından atılmıştır.
# Bu kod, CustomTkinter kütüphanesini kullanarak modern bir arayüz sağlar.
# Geliştirici: exelans001

import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

ctk.set_appearance_mode("system")  # Light veya Dark mod otomatik
ctk.set_default_color_theme("dark-blue")

class LycorisApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Lycoris Asistan B1.0.0beta")
        self.geometry("500x700")

        self.username = None

        self.label = ctk.CTkLabel(self, text="Lycoris Asistan", font=("Arial", 24, "bold"))
        self.label.pack(pady=10)

        self.entry_name = ctk.CTkEntry(self, placeholder_text="Adını gir", font=("Arial", 14))
        self.entry_name.pack(pady=10)

        self.name_button = ctk.CTkButton(self, text="Başla", command=self.set_username, font=("Arial", 14))
        self.name_button.pack(pady=10)

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=460, height=350)
        self.scroll_frame.pack(pady=10)

        self.entry_input = ctk.CTkEntry(self, placeholder_text="Bir şey yaz...", font=("Arial", 14))
        self.entry_input.pack(pady=10, fill="x", padx=20)

        self.send_button = ctk.CTkButton(self, text="Gönder", command=self.process_input)
        self.send_button.pack(pady=10)

    def set_username(self):
        name = self.entry_name.get().strip()
        if name:
            self.username = name
            self.entry_name.configure(state="disabled")
            self.name_button.configure(state="disabled")
            self.create_bubble(f"Merhaba {self.username}, nasılsın?", sender="lycoris")
        else:
            messagebox.showwarning("Uyarı", "Lütfen adını gir!")

    def process_input(self):
        if not self.username:
            messagebox.showinfo("Bilgi", "Lütfen önce adını gir.")
            return

        girdi = self.entry_input.get().strip()
        if not girdi:
            return

        self.create_bubble(girdi, sender="user")
        yanit = self.komut_isle(girdi)
        self.create_bubble(yanit, sender="lycoris")

        self.entry_input.delete(0, "end")

        if girdi.lower() == "çık":
            self.after(1000, self.destroy)

    def create_bubble(self, text, sender="user"):
        bubble_frame = ctk.CTkFrame(self.scroll_frame, corner_radius=10)

        if sender == "user":
            if ctk.get_appearance_mode() == "Dark":
                color = "#2a2a2a"
                text_color = "#eee"
            else:
                color = "#ddd"
                text_color = "#222"
            anchor = "e"
        else:
            if ctk.get_appearance_mode() == "Dark":
                color = "#1c1c1c"
                text_color = "#eee"
            else:
                color = "#bbb"
                text_color = "#222"
            anchor = "w"

        bubble_frame.configure(fg_color=color)
        label = ctk.CTkLabel(
            bubble_frame,
            text=f"{self.username if sender == 'user' else 'Lycoris'}:\n{text}",
            justify="left",
            font=("Arial", 12),
            text_color=text_color,
            wraplength=400,
        )
        label.pack(padx=5, pady=2)
        bubble_frame.pack(anchor=anchor, padx=5, pady=2, fill=None)

    def komut_isle(self, girdi):
        girdi = girdi.lower()

        if girdi == "nasılsın":
            return f"İyiyim {self.username}, teşekkür ederim. Sen nasılsın?"

        elif girdi == "yardım":
            return ("Şu komutları deneyebilirsin:\n"
                    "- nasılsın\n"
                    "- tarih ve saat\n"
                    "- not al\n"
                    "- not göster\n"
                    "- çık")

        elif girdi == "tarih ve saat":
            now = datetime.now()
            return now.strftime("Bugün %d.%m.%Y - Saat %H:%M")

        elif girdi == "not al":
            return self.not_al()

        elif girdi == "not göster":
            self.notlari_goster()
            return "Notları gösteriyorum..."

        elif girdi == "çık":
            return f"Görüşmek üzere {self.username}, kendine iyi bak!"

        else:
            return "Bunu anlayamadım 🤔 Daha farklı bir şekilde sorabilir misin?"

    def not_al(self):
        def kaydet():
            not_metni = not_text.get("1.0", "end").strip()
            if not_metni:
                with open("lycoris_notlar.txt", "a", encoding="utf-8") as f:
                    f.write(f"{self.username}: {not_metni}\n")
                not_pencere.destroy()
                self.create_bubble("Notunu kaydettim ✅", sender="lycoris")
            else:
                messagebox.showwarning("Uyarı", "Boş not kaydedilemez!")

        not_pencere = ctk.CTkToplevel(self)
        not_pencere.title("Not Al")
        not_pencere.geometry("400x300")

        not_label = ctk.CTkLabel(not_pencere, text="Notunu yaz:")
        not_label.pack(pady=10)

        not_text = ctk.CTkTextbox(not_pencere, width=360, height=180)
        not_text.pack(pady=10)

        kaydet_buton = ctk.CTkButton(not_pencere, text="Kaydet", command=kaydet)
        kaydet_buton.pack(pady=10)

        return "Not alma penceresini açtım 📝"

    def notlari_goster(self):
        try:
            with open("lycoris_notlar.txt", "r", encoding="utf-8") as f:
                notlar = f.readlines()
        except FileNotFoundError:
            notlar = []

        def sil():
            secim = listbox.curselection()
            if not secim:
                messagebox.showwarning("Uyarı", "Silmek için not seçmelisin!")
                return
            idx = secim[0]
            del notlar[idx]
            with open("lycoris_notlar.txt", "w", encoding="utf-8") as f:
                f.writelines(notlar)
            listbox.delete(idx)

        not_pencere = ctk.CTkToplevel(self)
        not_pencere.title("Notlar")
        not_pencere.geometry("400x300")

        # tkinter Listbox kullanıyoruz çünkü CustomTkinter'da Listbox yok
        import tkinter as tk
        listbox = tk.Listbox(not_pencere, width=60, height=15)
        listbox.pack(pady=10)

        for satir in notlar:
            listbox.insert("end", satir.strip())

        sil_buton = ctk.CTkButton(not_pencere, text="Seçili Notu Sil", command=sil)
        sil_buton.pack(pady=5)

if __name__ == "__main__":
    app = LycorisApp()
    app.mainloop()
