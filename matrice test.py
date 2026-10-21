#this game was finished on 3/22/2021
import pygame
import random

#sets up the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Infinite Runner")

red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
yellow = (0, 255, 255)

width = int(input("what do you want to be the grids width: "))
height = int(input("what do you want to be the grids height: "))

def create_square:
    pygame.draw_rect(
#where the main code is run
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    
    
    pygame.display.update()
pygame.quit()


