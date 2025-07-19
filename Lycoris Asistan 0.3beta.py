#Lycoris Asistan 0.3beta
from colorama import init, Fore, Style

init(autoreset=True)


def selamla():
    print(Fore.CYAN + "Lycoris version 0.3beta'a hoş geldin!")
    print(Fore.CYAN + "Ben Lycoris, senin dijital asistanın.")
    print(Fore.CYAN + "Herhangi bir şey sorabilir, sohbet edebilirsin.")
    print(Fore.YELLOW + "Sohbeti sonlandırmak için 'çık' yazman yeterli.\n")

def ismini_ogren():
    isim = input(Fore.MAGENTA + "Önce tanışalım. Adın nedir?: " + Style.RESET_ALL).strip()
    print(Fore.GREEN + f"Memnun oldum, {isim}!\n")
    return isim

def nasilsin_diyalogu(isim):
    print(Fore.BLUE + f"İyiyim {isim}, teşekkür ederim. Sen nasılsın?")
    cevap = input(Fore.MAGENTA + ">> " + Style.RESET_ALL).strip().lower()
    if "iyi" in cevap or "fena" in cevap:
        print(Fore.GREEN + "Harika! Sana nasıl yardımcı olabilirim?")
    else:
        print(Fore.RED + "Üzgünüm bunu duyduğuma... Elimden geleni yapmak isterim.")

def komut_isle(girdi, isim):
    girdi = girdi.strip().lower()

    if girdi in ["merhaba", "selam", "hey"]:
        print(Fore.GREEN + f"Selam {isim}! Yardım edebileceğim bir şey var mı?")

    elif girdi == "nasılsın":
        nasilsin_diyalogu(isim)

    elif girdi in ["beni seviyor musun", "beni seviyor musun?"]:
        print(Fore.YELLOW + "Ben duygularla değil, verilerle çalışıyorum 😄 Ama sen fena değilsin!")

    elif girdi in ["ne yapıyorsun", "napıyorsun"]:
        print(Fore.BLUE + "Seninle sohbet ediyorum. Ayrıca CPU sıcaklığımı kontrol ediyordum biraz önce 😅")

    elif girdi in ["yardım", "komutlar", "ne yapabilirsin"]:
        print(Fore.CYAN + "Şu komutları deneyebilirsin:\n" +
              Fore.LIGHTMAGENTA_EX + "- merhaba\n- nasılsın\n- beni seviyor musun\n- ne yapıyorsun\n- çık")

    else:
        print(Fore.RED + "Bunu anlayamadım 🤔 Daha farklı bir şekilde sorabilir misin?")

def sohbet():
    selamla()
    isim = ismini_ogren()

    while True:
        girdi = input(Fore.LIGHTWHITE_EX + "\nBir şey yaz: " + Style.RESET_ALL)
        if girdi.strip().lower() == "çık":
            print(Fore.YELLOW + f"Görüşmek üzere {isim}, kendine iyi bak!")
            break
        else:
            komut_isle(girdi, isim)

sohbet()
