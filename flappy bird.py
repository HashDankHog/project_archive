#this game was finished on 6/1/2021 while listening to peace by taylor swift
import pygame
import random

#sets up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Infinite Runner")

#defines the varibles used

score = 0

player_x = 400
player_y = 300
player_width = 40
player_height = 60
player_vel = 5

spawn_wall = True
is_jumping = False
jump_count = 0

wall1_x, wall1_y = 699, 0
wall2_x, wall2_y = 699, 450

wall1_width, wall1_height = 100, 250
wall2_width, wall2_height = 100, 250

choice = 0
wall_vel = 4
is_fall = True

#where the main code is run
clock = pygame.time.Clock()
print(score)
run = True
while run:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not is_jumping:
                is_jumping = True
                jump_count = 30
                
    if is_jumping:
        player_y -= player_vel
        jump_count -= 2
        if jump_count == 0:
            is_jumping = False
        
            
    
    #gravity
    if is_jumping:
        is_fall = False
    else:
        is_fall = True
    if is_fall and not player_y == 540:
        player_y += player_vel
    if spawn_wall:
        choice = random.randint(1,3)

    #creates the walls depending on the random number
    if choice == 1 and spawn_wall:
        wall1_y, wall1_height = -100, 250
        wall2_y, wall2_height = 400, 250
        spawn_wall = False
    elif choice == 2 and spawn_wall:
        wall1_y, wall1_height = 0, 300
        wall2_y, wall2_height = 500, 250
        spawn_wall = False
    elif choice == 3 and spawn_wall:
        wall1_y, wall1_height = -200, 250
        wall2_y, wall2_height = 300 ,300
        spawn_wall = False
        
   
    #draws the player and the walls
    screen.fill((0,0,0))

    player = pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))

    if not spawn_wall:
        wall1_x -= wall_vel
        wall2_x -= wall_vel
        wall1 = pygame.draw.rect(screen, (0, 255, 0), (wall1_x, wall1_y, wall1_width, wall1_height))
        wall2 = pygame.draw.rect(screen, (0, 255, 0), (wall2_x, wall2_y, wall2_width, wall2_height))

    if wall1_x <= 0:
        score += 1
        spawn_wall = True
        wall1_x = 699
        wall2_x = 699 
        
     #collision
    if player_y >= 770:
        run = False

    if player.colliderect(wall1):
        run = False
    elif player.colliderect(wall2):
        run = False
        
    print(score)

    
    pygame.display.update()
pygame.quit()
