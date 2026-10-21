#this game was completed on 5/1/2021 while listening to kiwi by harry styles
import pygame
import random
#sets up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("shooter")

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



bullet_x = 40
bullet_y = 300

enemy_width = 40
enemy_height = 40

x = 40
y = 300

vel = 5

is_shoot = True

bullet_width = 20
bullet_height = 20

bullet = pygame.draw.rect(screen, (255, 255, 0), (bullet_x, bullet_y, bullet_width, bullet_height))

width = 40
height = 60

player_vel = 30

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
    if keys[pygame.K_SPACE] and is_shoot == True:
        is_shoot = False
        bullet_x = 40
        bullet_y = y
        bullet = pygame.draw.rect(screen, (255, 255, 0), (bullet_x, bullet_y, bullet_width, bullet_height))
    #draws the player,bullet and the enemy
    screen.fill((0,0,0))
    player = pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))

    #moves enemy
    if is_shoot == False:
        bullet_x += vel*(vel*2)
        bullet = pygame.draw.rect(screen, (255, 255, 0), (bullet_x, bullet_y, bullet_width, bullet_height))
        
    enemy1 = pygame.draw.rect(screen, (255, 0, 0), (enemy1_x, enemy1_y, enemy_width, enemy_height))
    enemy2 = pygame.draw.rect(screen, (255, 0, 0), (enemy2_x, enemy2_y, enemy_width, enemy_height))
    enemy3 = pygame.draw.rect(screen, (255, 0, 0), (enemy3_x, enemy3_y, enemy_width, enemy_height))
    enemy4 = pygame.draw.rect(screen, (255, 0, 0), (enemy4_x, enemy4_y, enemy_width, enemy_height))
    enemy5 = pygame.draw.rect(screen, (255, 0, 0), (enemy5_x, enemy5_y, enemy_width, enemy_height))

    #moves the enemys towrads the player
    enemy1_x -= vel*1.5
    enemy2_x -= vel*1.5
    enemy3_x -= vel*1.5
    enemy4_x -= vel*1.5
    enemy5_x -= vel*1.5

    #collision for bullet
    if bullet_x >= 800:
        is_shoot = True
        
    if bullet.colliderect(enemy1):
        enemy1_x = 800
        enemy1_y = random.randint(20, 580)
    if bullet.colliderect(enemy2):
        enemy2_x = 800
        enemy2_y = random.randint(20, 580)
    if bullet.colliderect(enemy3):
        enemy3_x = 800
        enemy3_y = random.randint(20, 580)
    if bullet.colliderect(enemy4):
        enemy4_x = 800
        enemy4_y = random.randint(20, 580)
    if bullet.colliderect(enemy5):
        enemy5_x = 800
        enemy5_y = random.randint(20, 580)
        
    #lose code
    if enemy1_x <= 0:
        run = False
    if enemy2_x <= 0:
        run = False
    if enemy3_x <= 0:
        run = False
    if enemy4_x <= 0:
        run = False
    if enemy5_x <= 0:
        run = False

    
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
