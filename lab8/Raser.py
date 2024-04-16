import pygame
import sys
import random
import time

# Инициализация Pygame
pygame.init()

# Установка FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Остальные переменные
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Установка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фоновое изображение
background = pygame.image.load("/Users/asust/Desktop/PP2-2/lab8/png/AnimatedStreet.png")

# Создание экрана
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("/Users/asust/Desktop/PP2-2/lab8/png/Coin.png")
        self.scale_factor = 0.1  
        self.image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * self.scale_factor), int(self.original_image.get_height() * self.scale_factor)))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/asust/Desktop/PP2-2/lab8/png/yellow_2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/asust/Desktop/PP2-2/lab8/png/blue.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

# Создание спрайтов
P1 = Player()
E1 = Enemy()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Добавление нового пользовательского события
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Таймер для монеты
coin_spawn_time = 0
coin_spawn_interval = 3000  # 3 секунды в миллисекундах

# Главный игровой цикл
def main_loop():
    global SPEED, SCORE, COINS, coin_spawn_time

    while True:
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.5
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.blit(background, (0, 0))
        scores = font_small.render(f'Score: {SCORE}', True, BLACK)
        coins_collected = font_small.render(f'Coins: {COINS}', True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))
        DISPLAYSURF.blit(coins_collected, (SCREEN_WIDTH - coins_collected.get_width() - 10, 10))

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        current_time = pygame.time.get_ticks()
        if current_time - coin_spawn_time > coin_spawn_interval:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
            coin_spawn_time = current_time

        for coin in pygame.sprite.spritecollide(P1, coins, True):
            COINS += 1
            SCORE += 5

        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound("/Users/asust/Desktop/PP2-2/lab8/png/CARCR222.wav").play()
            time.sleep(0.5)

            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30, 250))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    main_loop()