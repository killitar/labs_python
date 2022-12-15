import pygame
import random
from pygame.locals import *
import os

WIDTH = 800
HEIGHT = 650
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NUMBER_MOVE = 30


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def move_to_right(self):
        self.rect.x += NUMBER_MOVE
        if self.rect.left > WIDTH:
            self.rect.right = 0

    def move_to_left(self):
        self.rect.x -= NUMBER_MOVE
        if self.rect.right < 0:
            self.rect.left = WIDTH

    def move_to_top(self):
        self.rect.y -= NUMBER_MOVE
        if self.rect.top < 0:
            self.rect.top = HEIGHT

    def move_to_bottom(self):
        self.rect.y += NUMBER_MOVE
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game N One")
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
player_img = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.key.get_pressed()[K_RIGHT]:
            player.move_to_right()
        elif pygame.key.get_pressed()[K_LEFT]:
            player.move_to_left()
        elif pygame.key.get_pressed()[K_UP]:
            player.move_to_top()
        elif pygame.key.get_pressed()[K_DOWN]:
            player.move_to_bottom()

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
