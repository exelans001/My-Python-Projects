#Sayı Tahmin Uygulaması

from colorama import Fore, init
import random

init(autoreset=True)

sayi = random.randint(1, 100)
skor = 100
tahminler = []

print(Fore.MAGENTA + "1-100 arası sayı tahmin etmeye çalış! ")
print(Fore.BLUE + f"Başlangıç skorunuz: {skor}")

while True:
    try:
        tahmin = int(input("Sayıyı tahmin ediniz: "))
    except ValueError:
        print(Fore.RED + "Lütfen geçerli bir sayı giriniz!")
        continue

    tahminler.append(tahmin)

    if tahmin == sayi:
        skor += 50
        print(Fore.CYAN + f"Tebrikler! Doğru tahmin. Skorunuz: {skor}")
        print(Fore.YELLOW + f"Denediğiniz sayılar: {tahminler}")
        break
    elif tahmin < sayi:
        skor -= 5
        print(Fore.GREEN + "Arttır!")
    elif tahmin > sayi:
        skor -= 5
        print(Fore.RED + "Azalt!")

    if skor <= 0:
        print(Fore.YELLOW + f"Skorunuz {skor} olduğu için oyun bitti. Doğru sayı {sayi} idi.")
        print(Fore.YELLOW + f"Denediğiniz sayılar: {tahminler}")
        break
