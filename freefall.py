import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("")




x = 400
y = 300
width = 40
height = 60
vel = 5
option = 0

option1_x, option1_y = 600, 500


run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #movement code
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800 - width:
        x += vel
    
    screen.fill((0,0,0))
    player = pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    
    
        
    pygame.display.update()

pygame.quit()
