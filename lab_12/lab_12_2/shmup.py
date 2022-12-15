import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), "img")


WIDTH = 480
HEIGHT = 600
FPS = 60
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load(path.join(img_dir, "darkPurple.png")).convert()
background = pygame.transform.scale(background, ((WIDTH, HEIGHT)))
background_rect = background.get_rect()

player_img = pygame.image.load(path.join(img_dir, "playerShip2_red.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_big1.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed01.png")).convert()


pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = meteor_img
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(meteor_img, (30, 40))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (
            self.rect.top > HEIGHT + 10
            or self.rect.left < -25
            or self.rect.right > WIDTH + 20
        ):
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(bullet_img, (10, 20))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    # Обновление
    all_sprites.update()
    # Проверка, не ударил ли моб игрока
    mob_hit_player = pygame.sprite.spritecollide(player, mobs, False)
    if mob_hit_player:
        running = False

    player_hits_mob = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for player_hit_mob in player_hits_mob:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()
