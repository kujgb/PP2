import pygame 
import time
import random

# Скорость змейки
snake_speed = 15

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
X, Y = 800, 600
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = X // CELL_SIZE, Y // CELL_SIZE
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Snake Game")

# Цвета
PINK = (255, 0, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Класс Змейки
class Snake:
    def __init__(self):
        # Инициализация тела змейки и начального направления
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        # Движение змейки в заданном направлении
        head = self.body[0]
        x, y = self.direction
        new_head = ((head[0] + x) % GRID_WIDTH, (head[1] + y) % GRID_HEIGHT)
        if new_head in self.body[:-1]:
            return False  # Змейка столкнулась сама с собой
        self.body.insert(0, new_head)
        self.body.pop()  # Убрать последний сегмент
        return True

    def change_direction(self, direction):
        # Изменение направления движения змейки
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def grow(self):
        # Увеличение длины змейки при поедании еды
        self.body.append(self.body[-1])

    def draw(self, surface):
        # Отрисовка змейки на экране
        for segment in self.body:
            pygame.draw.rect(surface, BLUE, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Класс Еды
class Food:
    def __init__(self):
        # Инициализация положения еды и таймера ее исчезновения
        self.position = self.randomize_position()
        self.timer = 5000  # Время в миллисекундах до исчезновения еды
        self.spawn_time = pygame.time.get_ticks()

    def randomize_position(self):
        # Генерация случайного положения для еды
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake.body:
                return (x, y)

    def draw(self, surface):
        # Отрисовка еды на экране
        pygame.draw.rect(surface, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def update(self):
        # Обновление состояния еды
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > self.timer:
            self.position = self.randomize_position()
            self.spawn_time = current_time

# Установка игровых параметров
snake = Snake()
food = Food()
clock = pygame.time.Clock()

# Игровые переменные
score = 0
level = 1
foods_eaten = 0
speed = 8  # Начальная скорость

# Главный игровой цикл
running = True
while running:
    screen.fill(PINK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    # Проверка столкновения с едой
    if snake.body[0] == food.position:
        score += 1
        foods_eaten += 1
        if foods_eaten >= 3:  # Увеличение уровня каждые 3 съеденные еды
            level += 1
            speed += 1  # Увеличение скорости с уровнем
            foods_eaten = 0
        food.position = food.randomize_position()
        snake.grow()  # Увеличение змейки при съедании еды

    # Движение змейки
    if not snake.move():
        running = False  # Игра окончена при столкновении змейки с собой или стеной

    # Обновление состояния еды
    food.update()

    # Отрисовка объектов на экране
    snake.draw(screen)
    food.draw(screen)
    
    # Отображение счета и уровня
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Счет: {score}", True, BLUE)
    level_text = font.render(f"Уровень: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    pygame.display.flip()
    clock.tick(speed)  # Управление скоростью игры

pygame.quit()
