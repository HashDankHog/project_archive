import pygame

width = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width,height))

square_width = 50
square_height = 25

x1 = width/2 - square_width/2
y1 = height/2 - square_height/2
x2 = width/2 + square_width/2
y2 = height/2 - square_height/2
x3 = width/2 + square_width/2
y3 = height/2 + square_height/2
x4 = width/2 - square_width/2
y4 = height/2 + square_height/2

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    square = pygame.draw.polygon(screen, (36, 123, 255), [(x1,y1),(x2,y2),(x3,y3),(x4,y4)])
    pygame.display.update()
pygame.quit()
