import pygame
import random
from pygame.locals import *

WIDTH = 800  # ширина игрового окна
HEIGHT = 650  # высота игрового окна
FPS = 30  # частота кадров в секунду
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update_left(self):
        self.rect.x += -5

        if self.rect.left > WIDTH:
            self.rect.x += 5

    def update_right(self):
        self.rect.x += 5

        if self.rect.right > WIDTH:
            self.rect.x += -5

    def update_up(self):
        self.rect.y += -5

        if self.rect.top > HEIGHT:
            self.rect.y += 5

    def update_down(self):
        self.rect.y += 5

        if self.rect.bottom > HEIGHT:
            self.rect.y += -5


# создаем игру и окно
pygame.init()
# pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.key.get_pressed()[K_RIGHT]:
            player.update_right()
        elif pygame.key.get_pressed()[K_LEFT]:
            player.update_left()
        elif pygame.key.get_pressed()[K_DOWN]:
            player.update_down()
        elif pygame.key.get_pressed()[K_UP]:
            player.update_up()

    # Обновление

    # Рендеринг
    screen.fill(BLACK)
    # После всего переворачиваем экран

    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
