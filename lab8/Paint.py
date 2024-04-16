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
        elif 180<x<200 and 0<y<60:
            return "прямоугольник"
        elif 180<x<200 and 0<y<45:
            return "круг"
        elif 1010<=x<=1080 and 0<=y<=70:
            return BLACK 
    return color  

#Процесс рисования
def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if color != "прямоугольник" and color != "круг" and color != BLACK:
            pygame.draw.circle(screen, color, (x,y), radius)
        elif color == "прямоугольник":
            pygame.draw.rect(screen, WHITE, (x,y, 40, 60), 4) 
        elif color == "круг":
            pygame.draw.circle(screen, WHITE, (x,y), 20, 4)
        elif color == BLACK:
            pygame.draw.circle(screen ,color, (x,y), 20, 27)
        
    
while not done:
    for event in pygame.event.get():
        
        #Условия выхода
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
        
        #Отрисковка квадратов на экране
        for i in range(len(colors)):
            draw_rect(i)
        pygame.draw.circle(screen, WHITE, (180,20), 20, 4)
        screen.blit(eraser, (1010, 0))
        pygame.draw.rect(screen, WHITE, (120, 0, 40, 60), 4)
        
        #выбор цевети рисование
        color = color_pick()
        painting(color)
        
        clock.tick(370)
        pygame.display.update()