import pygame
from pygame.locals import *
pygame.init()

#Создание цветов для paint 
RED = (230, 0, 0)
GREEN = (0, 230, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [MAGENTA, BLUE, CYAN]
color = WHITE

#Создание окна
WIDTH = 1080
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Создание переменных
radius = 15
x = 0
y = 0
mode = 'blue'
points = []
done = False

#eraser загрузка
eraser = pygame.image.load("/Users/asust/Desktop/PP2-2/lab8/png/rubber.png")
eraser = pygame.transform.scale(eraser, (70, 70))

#Создание прямоугльников
def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*45, 0, 45, 45))

#Выбор цвета и раположение их на окне
def color_pick():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0<x<50 and 0<y<45:
            return MAGENTA
        elif 40<x<80 and 0<y<45:
            return BLUE
        elif 90<x<150 and 0<y<45:
            return CYAN
        elif 1010<=x<=1080 and 0<=y<=70:
            return BLACK 
    return color  

#Процесс рисования
def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0] and not (0<=x<=400 and 0<=y<=90):
        if mode == 'круг':
            pygame.draw.circle(screen, color, (x, y), 27)
        elif mode == 'прямоугольник':
            pygame.draw.rect(screen, color, (x, y, 40, 40), 4)
        elif mode == 'прямоугольный треугольник':
            pygame.draw.polygon(screen, color, ((x, y), (x, y+40), (x+40, y+40)), 3)
        elif mode == 'равносторонний прямоугольник':
            pygame.draw.polygon(screen, color, ((x,y), (x+20, y-40), (x+40, y)))
        elif mode == 'ромб':
            pygame.draw.polygon(screen, color, ((x, y), (x+20, y-20), (x+40, y), (x+20, y+20)))    
        elif color == BLACK:
            pygame.draw.circle(screen ,color, (x,y), 20, 27)
    
mode = 'circle'

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    for i in range(len(colors)):
        draw_rect(i)

    screen.blit(eraser, (1010, 0))
    rect = pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 3)
    circle = pygame.draw.circle(screen, WHITE, (197, 20), 23, 3)
    right = pygame.draw.polygon(screen, WHITE, ((230, 0), (230, 40), (270, 40)), 3)
    equal = pygame.draw.polygon(screen, WHITE, ((280, 40), (300, 0), (320, 40)), 3)
    rhomb = pygame.draw.polygon(screen, WHITE, ((330, 20), (350,0), (370, 20), (350, 40)), 3)

    pos = pygame.mouse.get_pos()
    print(mode)
    if rect.collidepoint(pos):
        mode = "прямоугольник"
    if circle.collidepoint(pos):
        mode = "круг"
    if right.collidepoint(pos):
        mode = 'прямоугольный треугольник'
    if equal.collidepoint(pos):
        mode = 'равностронний треугольник'
    if rhomb.collidepoint(pos):
        mode = 'ромб'


    color = color_pick()
    painting(color)


    clock.tick(370)
    pygame.display.update()