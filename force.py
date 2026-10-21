#this was completed on 5/20/23 at 2:11 pm while listening to mahler 5 III scherzo
import pygame
import math

width = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width,height))


def find_vector(x1, y1, x2, y2, f):
    #finds distance between points horizontally, vertically, and diagnolly
    Dx = x2 - x1
    Dy = y2 - y1

    Dh = ((x2-x1)**2+(y2-y1)**2)**0.5
    
    #finds ratio between the force and the distance between points
    r = f/Dh

    #calculates the x and y components of the force
    Fx = Dx * r
    Fy = Dy * r

    return Fx, Fy

def calculate_force(m1, m2, r):
    #gravitational constant
    G = 6.67408 * (10**-11)
    #calculates the force between the two objects
    f = (m1 * m2)/r**2
    return G*f


#defines varibles for first object
x1 = 200
y1 = 200
Vx1 = -0.1
Vy1 =  0.1

m1 = 999999999999
d1 = 99999999999
r1 = m1/d1

#defines varibles for second object
x2 = 400
y2 = 400
Vx2 = -0.1
Vy2 =  0.1
m2 = 999999999999
d2 = 99999999999
r2 = m2/d2

r12 = 0
f = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))

    #finds distance between the two objects so force can be calculated
    r12 = ((x2-x1)**2+(y2-y1)**2)**0.5

    f = calculate_force(m1, m2, r12)
    
    Fx, Fy = find_vector(x1, y1, x2, y2, f)

    
    Vx1 += Fx/m1
    Vx2 += Fx/m2

    Vy1 += Fy/m1
    Vy2 += Fy/m2

    x1 += Vx1
    x2 -= Vx2

    y1 += Vy1
    y2 -= Vy2
    
    pygame.draw.circle(screen, (255,0,0), (x1,y1), r1)
    pygame.draw.circle(screen, (0,255,0), (x2,y2), r2)

    pygame.display.update()
pygame.quit()