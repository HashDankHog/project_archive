#this game was finished on 8/22/2021 while listining to satisfied
import sys
import pygame

pygame.init()


screen = pygame.display.set_mode((640, 480))
FPSCLOCK = pygame.time.Clock()
RED = pygame.Color("red")
startpoint = pygame.math.Vector2(590, 430)
endpoint = pygame.math.Vector2(10, 0)
angle = 0
done = False

#lower speed the faster it goes
speed = 0

acceleration = 0.01
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()

    
    # The current endpoint is the startpoint vector + the
    # rotated original endpoint vector.
    current_endpoint = startpoint + endpoint.rotate(angle)
    current_endpoint2 = startpoint - endpoint.rotate(angle)
    
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, RED, startpoint, current_endpoint, 2)
    pygame.draw.line(screen, RED, startpoint, current_endpoint2, 2)
    if keys[pygame.K_RIGHT]:  
        # % 360 to keep the angle between 0 and 360.
        angle = (angle+5) % 360
    if keys[pygame.K_LEFT]:
        # % 360 to keep the angle between 0 and 360.
        angle = (angle-5) % 360
    if keys[pygame.K_UP]:
        speed += acceleration
    if keys[pygame.K_DOWN]:
        speed -= acceleration
    if not keys[pygame.K_UP] and speed > 0:
        speed -= acceleration
    if not keys[pygame.K_DOWN] and speed < 0:
        speed += acceleration
    startpoint += (startpoint - current_endpoint)*speed

    pygame.display.flip()
    FPSCLOCK.tick(30)

pygame.quit()
sys.exit()

