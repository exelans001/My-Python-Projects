from colorama import init, Fore
import time

init(autoreset=True)

def oyun():
    # Bilgilendirme
    bilgi = Fore.RED + "Lütfen seçimlerde büyük-küçük harf kullanımına uyalım..."
    iyi_son = Fore.GREEN + "Her seçimin bir değeri vardır. Düşünmeden seçim yapma..."
    kotu_son = Fore.RED + "Karanlığın rehberliği bazen ışıktan daha çok aydınlıktır."
    notr_son = "Fırsatlar kaçtı diye üzülme. Geleceğe bak ve gülümse :)"

    print()
    print(bilgi)
    print()
    time.sleep(1)
    print(Fore.YELLOW + "'Survive Decides' mini oyununa hoş geldin!")
    print()
    time.sleep(2)
    print(Fore.BLACK + "Made by exelans")
    time.sleep(2)

    print(Fore.CYAN + "Sen asil bir ailenin tek çocuğusun...")
    print()

    # Cinsiyet Seçimi
    cinsiyet = input(Fore.MAGENTA + "Cinsiyet seçiniz [E/K]: ").strip().upper()
    time.sleep(0.5)

    if cinsiyet == "E":
        cinsiyet_info = "Oğul"
        print("Sen asil bir ailenin tek erkek çocuğusun...")
    else:
        cinsiyet_info = "Küçük Kız"
        print("Sen asil bir ailenin tek kız çocuğusun...")

    print()
    print(Fore.CYAN + "Bir gün bahçede oynarken bir cisim gördün...")
    print()
    time.sleep(1)
    print(bilgi)
    print()

    secim1 = input("Al/Alma: ").strip().lower()
    time.sleep(0.5)

    if secim1 == "al":
        print()
        print(Fore.CYAN + "Cismi aldın ve gözlerin kararıp bayıldın...")
        time.sleep(1)
        print(Fore.CYAN + "Uyandığında sana bakan yaşlı bir kadın gördün...")
        print()

        secim2 = input("Seçim [Kimsin/Neredeyim]: ").strip().lower()

        if secim2 == "kimsin":
            print(Fore.CYAN + "Yaşlı kadın *yavaşça*:")
            time.sleep(1)
            print(Fore.MAGENTA + "Yaşlı Kadın: Ben Cadı Nia. Bıraktığım cismi aldığını hissettim. İsmin nedir,", cinsiyet_info, "?")
            time.sleep(1.5)
            isim = input(Fore.YELLOW + "İsminizi giriniz: ").strip()
            time.sleep(1)
            print(Fore.MAGENTA + "Nia: Hm... demek",Fore.MAGENTA + isim,Fore.MAGENTA + "hah? Bu ismi daha önce duydum.")
            print()
            time.sleep(1)
            print(Fore.MAGENTA + "Nia: Sen bölgedeki Asilzade beyinin varisisin.")
            time.sleep(0.5)
            print(Fore.MAGENTA + "Nia: Seni neden ele geçirdiğimi biliyor musun?")
            print()
            time.sleep(1.5)
            print("Sen: Hayır, bilmiyorum.")
            print()
            time.sleep(1)
            print(Fore.MAGENTA + "Nia aniden kolunu tuttu.")
            time.sleep(0.5)
            print(Fore.MAGENTA + "Nia: Senin BÜYÜK MANA GÜCÜNÜ ÇALMAK İÇİN ELE GEÇİRDİM!")
            print()
            time.sleep(1)

            durum2 = input(Fore.YELLOW + "Bir şansın var! Seçim [Vur/Isır]: ").strip().lower()

            if durum2 == "vur":
                print()
                print(Fore.GREEN + "----İYİ SON----")
                print()
                time.sleep(0.5)
                print(Fore.YELLOW +  "Cadı'nın gözüne sağlam bir yumruk çaktın ve koşarak kaçtın.")
                time.sleep(1.5)
                print("Ormandaydın ve şans eseri Kraliyet Muhafızları seni buldu.")
                time.sleep(1.5)
                print("Ailene teslim edildin. Artık yabancı cisimlerden uzak duruyorsun.")
                time.sleep(1.5)
                print("Paranoyaklaştın; yemeğini önce hizmetlilere tattırıyorsun...")
                time.sleep(2)
                print()
                print(Fore.MAGENTA + "---Acaba gerçekten iyi bir son muydu?---")
                print()
                time.sleep(2)
                print(iyi_son)

            else:
                print()
                print(Fore.RED + "-----KÖTÜ SON-----")
                print()
                time.sleep(0.5)
                print(Fore.YELLOW + "Cadıyı ısırdın fakat başarısız oldun.")
                time.sleep(1.5)
                print(Fore.YELLOW + "Bütün manan Cadı tarafından çekildi.")
                time.sleep(2)
                print(Fore.YELLOW + "Cadı, elde ettiği güçle iskelet ordusu kurdu ve dünyayı ele geçirdi.")
                time.sleep(1)
                print(Fore.YELLOW + "Sen ise manasızlıktan hayatını kaybettin.")
                time.sleep(1.5)
                print()
                print(kotu_son)

        else:
            print()
            print(Fore.LIGHTMAGENTA_EX + "Yaşlı Kadın: Neredesin biliyor musun? Artık benim evimde!")
            print("TO BE CONTINUE (geliştirilecek..) ")

    else:
        print()
        print(Fore.CYAN + "Cismi almadın...")
        print()
        time.sleep(1)
        print("----NÖTR SON-----")
        time.sleep(0.5)
        print(Fore.YELLOW + "Hayatın oldukça sıradan geçti. Ailenin mirasını bitirdin.")
        time.sleep(2)
        print(Fore.YELLOW + "Sefalet içinde bir gün hayatına veda ettin... Ama çok iyi biriydin.")
        time.sleep(2)
        print(Fore.BLUE + f"Huzur içinde uyu, {cinsiyet_info}...")
        print()
        time.sleep(1)
        print(notr_son)

if __name__ == "__main__":
    while True:
        oyun()
        tekrar = input(Fore.RED + "Tekrar oynamak ister misin? [E/H]: ").strip().lower()
        if tekrar != 'e':
            print(Fore.CYAN + "Oyunu oynadığın için teşekkürler! Görüşürüz.")
            break
