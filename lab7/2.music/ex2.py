import pygame
import os

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
songs = ['/Users/asust/Desktop/PP2-2/lab7/music/Aiga qarap.mp3', '/Users/asust/Desktop/PP2-2/lab7/music/Ne sebep.mp3']
i = 0
pygame.mixer.music.load(songs[i])
pygame.mixer.music.play()
paused = False

background_image = pygame.image.load('/Users/asust/Desktop/PP2-2/lab7/music/1.jpg')
background_rect = background_image.get_rect()

while not done:
    screen.blit(background_image, background_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

    pygame.display.flip()

pygame.quit()
