#It works better now, the object is now included in force calculations but it still wont move
import pygame
import math

width = 1000
height = 1000

pygame.init()
screen = pygame.display.set_mode((width,height))

def find_vector(x1, y1, x2, y2, f, Dh):
   #finds distance between points horizontally, vertically, and diagonally
   Dx = x2 - x1
   Dy = y2 - y1

   #finds ratio between the force and the distance between points
   r = f/Dh

   #calculates the x and y components of the force
   Fx = Dx * r
   Fy = Dy * r

   return Fx, Fy

#Calculates the force between two objects using Newtons law of univeral gravitation
def calculate_force(m1, m2, r):
   #Gravitational constant
   G = 6.67408 * (10**-11)
   #Calculates the force between the two objects
   f = (m1 * m2)/r**2
   return G*f

#Defines variables for the objects
x = [200, 400, 600]
y = [200, 400, 600]

Vx = [0.1, -0.1,  0.1]
Vy = [-0.1, 111, -0.1]

m = [999999999999, 999999999999, 999999999999]
d = [99999999999, 99999999999, 99999999999]

#Tells us how many objects we have
N = len(x)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))

    #The nested for loops are a way to find which objects we are calculating forces between
    #The algorithm is super simple, for each item in list, we find every item with a higher index than it to pair with it
    for i in range(N):
        for j in range(N-i-1):
            #The plus one is to prevent calculating forces between the same object
            Obj1 = i
            Obj2 = j+i+1

            #Finds distance between the two objects so force can be calculated
            Dh = ((x[Obj2]-x[Obj1])**2+(y[Obj2]-y[Obj1])**2)**0.5

            #Calculates the force then translates it into a force vector

            #For some reason I had to add 0.01 to the Dh variable
            #It says that I was dividing by zero but my original code worked
            f = calculate_force(m[Obj1], m[Obj2], Dh+0.01)
            Fx, Fy = find_vector(x[Obj1], y[Obj1], x[Obj2], y[Obj2], f, Dh+0.01)

            #Integrates acceleration twice to get position of objects
            Vx[Obj1] += Fx/m[Obj1]
            Vx[Obj2] += Fx/m[Obj2]

            Vy[Obj1] += Fy/m[Obj1]
            Vy[Obj2] += Fy/m[Obj2]

            x[Obj1] += Vx[Obj1]
            x[Obj2] -= Vx[Obj2]

            y[Obj1] += Vy[Obj1]
            y[Obj2] -= Vy[Obj2]

    #Draws all our circles
    for k in range(N):
        pygame.draw.circle(screen, (0,255,0), (x[k],y[k]), m[k]/d[k])
    pygame.display.update()
pygame.quit()