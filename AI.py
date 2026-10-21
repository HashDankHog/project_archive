import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

player_x = 375
player_y = 250
player_width = 50
player_height = 75

Color_line = (255, 255, 255)

enemy_x = 0
enemy_y = 600
enemy_width = 50
enemy_height = 50

enemy_vel = 5
vel = 8

player_cx = player_x + (player_width/2)
player_cy = player_y + (player_height/2)
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= vel
    if keys[pygame.K_RIGHT]:
        player_x += vel
    if keys[pygame.K_UP]:
        player_y -= vel
    if keys[pygame.K_DOWN]:
        player_y += vel
        
    player_cx = player_x + (player_width/2)
    player_cy = player_y + (player_height/2)

    
    screen.fill((53, 53, 184))
    player = pygame.draw.rect(screen, (58, 173, 214), (player_x, player_y, player_width, player_height))
    enemy = pygame.draw.rect(screen, (240, 179, 12), (enemy_x, enemy_y , enemy_width, enemy_height))



    player_x = player_x
    player_y = player_y
    
    if enemy_x > player_x:
        enemy_x -= enemy_vel
    if enemy_y > player_y:
        enemy_y -= enemy_vel
    if enemy_x < player_x:
        enemy_x += enemy_vel
    if enemy_y < player_y:
        enemy_y += enemy_vel
        

    pygame.display.update()
pygame.quit()
    
