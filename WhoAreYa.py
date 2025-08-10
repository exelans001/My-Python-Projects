#Who AreYa? - Kaotik Sistem İzleyici
# Bu Python uygulaması, kullanıcıları eğlenceli ve kaotik bir şekilde izleyen
# bir sistem izleyici simülasyonudur. Kullanıcı bilgilerini ve sahte uyarıları
# gösterir, temalar arasında geçiş yapar ve sahte terminal çıktıları üretir
# Kullanıcı bilgileri ve sahte terminal çıktıları içerir.
# Fikir: exelans001
# Geliştirici: exelans001 (Kütüphane entegreleri,ana yerleştirme,renk seçimleri,fikir verme,konsept sahibi) ve ChatGPT (kodları yazan)

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import time
import threading
import getpass
import platform
import socket

class WhoAreYaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WhoAreYa? - Sistem İzleniyor...")
        self.geometry("800x600+200+100")
        self.running = False

        self.themes = [
            {"bg": "black", "fg": "lime", "font": ("Courier", 16)},
            {"bg": "#1e1e2f", "fg": "cyan", "font": ("Arial", 18, "bold")},
            {"bg": "#222222", "fg": "orange", "font": ("Consolas", 14)},
            {"bg": "#003300", "fg": "#ccffcc", "font": ("Courier New", 16)},
            {"bg": "#330000", "fg": "#ff6666", "font": ("Comic Sans MS", 16, "italic")},
        ]

        self.configure(bg="black")
        self.current_theme = 0

        # Ana label
        self.label = ctk.CTkLabel(self, text="Sistem Başlatılıyor...", text_color="lime", font=("Courier", 16))
        self.label.pack(pady=20)

        # Butonlar
        self.start_button = ctk.CTkButton(self, text="💀 SİSTEMİ BOZ 💀", command=self.start_chaos)
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(self, text="🧯 DURDUR", command=self.stop_chaos)
        self.stop_button.pack(pady=5)

        # Terminal benzeri loglar
        self.terminal_logs = [
            "[ACCESS GRANTED] Connected to system core...",
            "[INFO] Injecting script into memory...",
            "[TRACE] Searching for user data...",
            "[WARNING] Unauthorized access detected.",
            "[UPLOAD] Sending local logs to remote server...",
            "[SYS] Bypassing firewall...",
            "[ERROR] BIOS integrity check failed!",
            "[CRITICAL] Remote shell activated.",
            "[INFO] Decrypting hard drive...",
            "[OVERRIDE] User control disabled."
        ]

        # Kullanıcı ve sistem bilgileri (fake+gerçek karışık)
        self.user_info_fakes = [
            f"Kullanıcı Adı: {getpass.getuser()}",
            f"IP Adresi: {self.get_ip()}",
            f"İşletim Sistemi: {platform.system()} {platform.release()}",
            f"Makine Adı: {socket.gethostname()}",
            "Kullanıcı Yetkisi: SÜPERADMIN",
            "Ağ Durumu: Bağlı",
            "Gizlilik Durumu: İhlal Edildi",
            "Disk Sağlığı: %47 - Kritik!",
            "RAM Kullanımı: %99 (Tehlikeli)",
            "Arka Plan Uygulamaları: 42 Adet Algılandı",
        ]

        self.who_are_you_questions = [
            "Who are you?",
            "Identify yourself...",
            "Seni tanımıyorum.",
            "Kendini açıklayabilir misin?",
            "Kim olduğunu kanıtla!",
            "Sistem seni sorguluyor...",
            "Kimlik doğrulaması gerekiyor!",
            "WhoAreYa? 🤖",
            "Gizli mod aktif, kim olduğunu söyle!",
            "Sen kimsin, neden buradasın?"
        ]

    def get_ip(self):
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            return ip
        except:
            return "0.0.0.0"

    def start_chaos(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.chaos_loop, daemon=True).start()

    def stop_chaos(self):
        self.running = False
        self.label.configure(text="İzleme durduruldu...", text_color="gray")

    def spawn_terminal_line(self):
        text = random.choice(self.terminal_logs + self.user_info_fakes + self.who_are_you_questions)
        lbl = ctk.CTkLabel(self, text=text,
                           text_color=self.themes[self.current_theme]["fg"],
                           font=self.themes[self.current_theme]["font"])
        lbl.place(x=10, y=random.randint(50, 550))

    def change_theme(self):
        self.current_theme = (self.current_theme + 1) % len(self.themes)
        theme = self.themes[self.current_theme]
        self.configure(bg=theme["bg"])
        self.label.configure(text_color=theme["fg"], font=theme["font"])

    def chaos_loop(self):
        counter = 0
        while self.running:
            time.sleep(random.uniform(0.2, 1))

            # Tema değişimi her 10 adımda bir
            if counter % 10 == 0:
                self.change_theme()

            self.spawn_terminal_line()

            # Sahte uyarılar
            if random.random() < 0.25:
                messagebox.showwarning("Güvenlik Uyarısı", "Sistemde anormal işlem tespit edildi.")
            if random.random() < 0.12:
                messagebox.showerror("Kritik Hata", "Sistem belleği şüpheli şekilde değiştirildi!")
            if random.random() < 0.06:
                messagebox.showinfo("Bilgi", "Gizli verileriniz dışa aktarılıyor...")

            # Ekran konumu değişikliği
            xpos = random.randint(100, 800)
            ypos = random.randint(100, 500)
            self.geometry(f"800x600+{xpos}+{ypos}")

            # Ana label’ın anlık mesajları
            if random.random() < 0.15:
                self.label.configure(text=random.choice([
                    "🛑 KONTROL SİZDE DEĞİL",
                    "👁‍🗨 VERİLERİNİZ GÖNDERİLİYOR",
                    "💀 SİSTEME SIZILDI",
                    "🧬 DNA TARANIYOR...",
                    "🚫 ERİŞİM ENGELLENDİ",
                    random.choice(self.who_are_you_questions)
                ]), text_color="red")
            else:
                self.label.configure(text="Sistem analiz ediliyor...", text_color=self.themes[self.current_theme]["fg"])

            counter += 1

if __name__ == "__main__":
    app = WhoAreYaApp()
    app.mainloop()
