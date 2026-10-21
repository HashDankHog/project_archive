#this game was finished on 3/22/2021
import pygame
import random

#sets up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Infinite Runner")

#defines the varibles used
wall_x = 800
wall_y = 330
wall_width = 30
wall_height = 30

score = 0

player_x = 400
player_y = 300
player_width = 40
player_height = 60
player_vel = 5

is_jumping = False
jump_count = 0

spawn_wall = 0
move_wall = False

#where the main code is run
clock = pygame.time.Clock()
print(score)
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

    #movement code
    if is_jumping and jump_count > 0:
        if jump_count > 15:
            player_y -= player_vel
            jump_count -= 1
        elif jump_count > 0:
            player_y += player_vel  
            jump_count -= 1 
        is_jumping = jump_count > 0

    #draws the player and the wall
    screen.fill((0,0,0))
    wall = pygame.draw.rect(screen, (255, 0, 0), (wall_x, wall_y, wall_width, wall_height))
    player = pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))     



    #moves the wall
    spawn_wall = random.randint(0, 200)
    if spawn_wall == 1 and move_wall == False:
        move_wall = True
    if move_wall == True:
        wall_x -= player_vel
    if wall_x == 0:
        wall_x = 800
        move_wall = False
        score += 1
        print(score)
    #sees if the player has hit a wall therefore losing the game
    if player.colliderect(wall):
        print("You lose :(")
        run = False
    
    pygame.display.update()
pygame.quit()
