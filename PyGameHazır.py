#PyGame hazır template (frame oluşturma)
import pygame

pygame.init()

#Pencere oluşturma
frame = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Template")

# Oyun döngüsü
start = True
clock= pygame.time.Clock()

while start:
    clock.tick(60)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    # Ekranı temizleme
    frame.fill((0, 0, 0))
