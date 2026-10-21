#this game was completed on april 13 of 2021 while listening to begin again by taylor swift
import pygame
import random
#sets up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid The Bullets")

#defines the size and coords for the player
enemy1_x = 800
enemy1_y = random.randint(20, 580)

enemy2_x = 800
enemy2_y = random.randint(20, 580)

enemy3_x = 800
enemy3_y = random.randint(20, 580)

enemy4_x = 800
enemy4_y = random.randint(20, 580)

enemy5_x = 800
enemy5_y = random.randint(20, 580)

enemy_width = 40
enemy_height = 40
x = 40
y = 300
vel = 5

width = 40
height = 60
player_vel = 10

#where the main code is run
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #movement code
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y > vel:
        y -= player_vel
    if keys[pygame.K_DOWN] and y < 600 - height - vel:
        y += player_vel
    #draws the player and the coin
    screen.fill((0,0,0))
    player = pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))

    enemy1 = pygame.draw.rect(screen, (255, 0, 0), (enemy1_x, enemy1_y, enemy_width, enemy_height))
    enemy2 = pygame.draw.rect(screen, (255, 0, 0), (enemy2_x, enemy2_y, enemy_width, enemy_height))
    enemy3 = pygame.draw.rect(screen, (255, 0, 0), (enemy3_x, enemy3_y, enemy_width, enemy_height))
    enemy4 = pygame.draw.rect(screen, (255, 0, 0), (enemy4_x, enemy4_y, enemy_width, enemy_height))
    enemy5 = pygame.draw.rect(screen, (255, 0, 0), (enemy5_x, enemy5_y, enemy_width, enemy_height))

    #moves the enemys towrads the player
    enemy1_x -= vel*vel
    enemy2_x -= vel*vel
    enemy3_x -= vel*vel
    enemy4_x -= vel*vel
    enemy5_x -= vel*vel

    #respawns the enemys when they hit the wall
    if enemy1_x <= 0:
        enemy1_x = 800
        enemy1_y = random.randint(20, 580)
    if enemy2_x <= 0:
        enemy2_x = 800
        enemy2_y = random.randint(20, 580)
    if enemy3_x <= 0:
        enemy3_x = 800
        enemy3_y = random.randint(20, 580)
    if enemy4_x <= 0:
        enemy4_x = 800
        enemy4_y = random.randint(20, 580)
    if enemy5_x <= 0:
        enemy5_x = 800
        enemy5_y = random.randint(20, 580)

    #collision code
    if player.colliderect(enemy1):
        print("you lose")
        break
    if player.colliderect(enemy2):
        print("you lose")
        break
    if player.colliderect(enemy3):
        print("you lose")
        break
    if player.colliderect(enemy4):
        print("you lose")
        break
    if player.colliderect(enemy5):
        print("you lose")
        break
    
    pygame.display.update()


pygame.quit()
