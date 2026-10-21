#this game was completed on 4/15/2021
import pygame
import random

#sets up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Platformer")

#defines the varibles used

platform1_x = 100
platform1_y = 500

platform2_x = 230
platform2_y = 350

platform3_x = 40
platform3_y = 300

platform4_x = 300
platform4_y = 150

platform5_x = 650
platform5_y = 120

flag_x = 690
flag_y = 30
flag_width = 10
flag_height = 90



platform_width = 80
platform_height = 20

player_x = 400
player_y = 540
player_width = 40
player_height = 60
player_vel = 10
jump_vel = 5
gravity = 10

is_fall = True
is_jumping = False
jump_count = 0


spawn_wall = 0
move_wall = False

#where the main code is run
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not is_jumping:
                is_jumping = True
                jump_count = 30
    #gravity
    if is_jumping:
        is_fall = False
    else:
        is_fall = True
    if is_fall and not player_y == 540:
        player_y += gravity

                
    keys = pygame.key.get_pressed()

    #movement code
    if is_jumping and jump_count > 0:
        if jump_count >15:
            player_y -= player_vel
            jump_count -= 1
        elif jump_count > 0:
            player_y += player_vel  
            jump_count -= 1 
        is_jumping = jump_count > 0
    if keys[pygame.K_LEFT] and player_x > player_vel:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < 800 - player_width:
        player_x += player_vel

    #draws the player and the wall
    screen.fill((0,0,0))

    player = pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))     

    platform1 = pygame.draw.rect(screen, (255, 0, 0), (platform1_x, platform1_y, platform_width, platform_height))
    platform2 = pygame.draw.rect(screen, (255, 0, 0), (platform2_x, platform2_y, platform_width, platform_height))
    platform3 = pygame.draw.rect(screen, (255, 0, 0), (platform3_x, platform3_y, platform_width, platform_height))
    platform4 = pygame.draw.rect(screen, (255, 0, 0), (platform4_x, platform4_y, platform_width, platform_height))
    platform5 = pygame.draw.rect(screen, (255, 0, 0), (platform5_x, platform5_y, platform_width, platform_height))

    flag = pygame.draw.rect(screen, (0, 255, 0), (flag_x, flag_y, flag_width, flag_height))

    #collision code
    if player.colliderect(platform1) or player.colliderect(platform2) or player.colliderect(platform3) or player.colliderect(platform4) or player.colliderect(platform5):
        is_fall = False
        player_y -= player_vel
    else:
        is_fall = True
    #win code
    if player.colliderect(flag):
        print("You Win!")
        run = False


    
    pygame.display.update()
pygame.quit()
