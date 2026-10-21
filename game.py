#this game was created on march 19 of 2021 while lisening to the song willow by taylor swift
import pygame
import random
#sets up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game")

#defines the size and coords for the coin and the player
coin_x = 50
coin_y = 50
coin_width = 20
coin_height = 20
score = 0

x = 400
y = 300
width = 40
height = 60
vel = 5

#where the main code is run
print(score)
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
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 600 - height - vel:
        y += vel
    #draws the player and the coin
    screen.fill((0,0,0))
    coin = pygame.draw.rect(screen, (244, 247, 30), (coin_x, coin_y, coin_width, coin_height))
    player = pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))

    #collision code
    if player.colliderect(coin):
        coin_x = random.randint(20, 780)
        coin_y = random.randint(20, 580)
        score += 1
        print(score)
        
    pygame.display.update()

pygame.quit()
