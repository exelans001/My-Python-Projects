#PyGame Giriş
#ChatGPT yardımı ile yapılmıştır.
#Giriş olduğu için hatalar vardır.
#Buradaki amaç PyGame ile basit bir oyun yapmaktır.
#Retro tarzı basit bir oyun bulunmaktadır.(Snake tarzı)
#Ana amaç ise PyGame tanımak ve syntax tarzını görmektir.

#by exelans001

import pygame
import random

# PyGame başlat
pygame.init()

# Pencere boyutu
genislik, yukseklik = 600, 400
ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Basit Retro Toplama Oyunu")

# Renkler (RGB)
siyah = (0, 0, 0)
beyaz = (255, 255, 255)
kirmizi = (255, 0, 0)
yesil = (0, 255, 0)

# Oyuncu ayarları
kare_boyut = 20
x, y = genislik // 2, yukseklik // 2
hiz = 5

# Yem ayarları
def yeni_yem():
    return [random.randrange(0, genislik - kare_boyut, kare_boyut),
            random.randrange(0, yukseklik - kare_boyut, kare_boyut)]

yem_x, yem_y = yeni_yem()

# Skor
skor = 0
font = pygame.font.SysFont(None, 30)

def skor_goster():
    metin = font.render(f"Skor: {skor}", True, beyaz)
    ekran.blit(metin, (10, 10))

# Ana döngü
calisiyor = True
clock = pygame.time.Clock()

while calisiyor:
    clock.tick(30)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False

    # Tuş hareketi
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT]:
        x -= hiz
    if tuslar[pygame.K_RIGHT]:
        x += hiz
    if tuslar[pygame.K_UP]:
        y -= hiz
    if tuslar[pygame.K_DOWN]:
        y += hiz

    # Sınırlar
    if x < 0: x = 0
    if x > genislik - kare_boyut: x = genislik - kare_boyut
    if y < 0: y = 0
    if y > yukseklik - kare_boyut: y = yukseklik - kare_boyut

    # Yem yenme kontrolü (basit)
    if x == yem_x and y == yem_y:
        skor += 1
        yem_x, yem_y = yeni_yem()

    # Ekranı temizle
    ekran.fill(siyah)

    # Oyuncu çiz
    pygame.draw.rect(ekran, yesil, (x, y, kare_boyut, kare_boyut))

    # Yem çiz
    pygame.draw.rect(ekran, kirmizi, (yem_x, yem_y, kare_boyut, kare_boyut))

    # Skoru göster
    skor_goster()

    pygame.display.update()

pygame.quit()
