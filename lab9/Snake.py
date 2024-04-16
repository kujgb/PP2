import pygame 
import time
import random

snake_speed = 15

# Initialize
pygame.init()

# Set up the screen
X, Y = 800, 600
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = X // CELL_SIZE, Y // CELL_SIZE
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (0, 255, 255)
blue = (255, 0, 255)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        head = self.body[0]
        x, y = self.direction
        new_head = ((head[0] + x) % GRID_WIDTH, (head[1] + y) % GRID_HEIGHT)
        if new_head in self.body[:-1]:
            return False  # Snake collided with itself
        self.body.insert(0, new_head)
        self.body.pop()  # Remove the last segment
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:  # Prevents reversing into itself
            self.direction = direction

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, blue, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake.body:
                return (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Game setup
snake = Snake()
food = Food()
clock = pygame.time.Clock()

# Game variables
score = 0
level = 1
foods_eaten = 0
speed = 8  # Initial speed

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
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

    # Check for food collision
    if snake.body[0][0] < 0 or snake.body[0][0] >= GRID_WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= GRID_HEIGHT:
        running = False  # Game over if snake hits the wall
    if snake.body[0] == food.position:
        score += 1
        foods_eaten += 1
        if foods_eaten >= 3:  # Increase level every 3 foods eaten
            level += 1
            speed += 1  # Increase speed with level
            foods_eaten = 0
        food.position = food.randomize_position()
        snake.grow()  # Grow the snake only when it eats food
    else:
        # Move the snake only if it doesn't eat food
        if not snake.move():
            running = False  # Game over if snake collides with itself or the wall

    # Check for border collision
    if snake.body[0][0] < 0 or snake.body[0][0] >= GRID_WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= GRID_HEIGHT:
        running = False  # Game over if snake hits the wall

    # Draw objects
    snake.draw(screen)
    food.draw(screen)
    
    # Display score and level
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, blue)
    level_text = font.render(f"Level: {level}", True, blue)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    pygame.display.flip()
    clock.tick(speed)  # Control game speed

pygame.quit()
