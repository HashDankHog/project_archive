
#https://stackoverflow.com/questions/68825905/
#https://stackoverflow.com/questions/73514673/
import pygame
import sys
import math

# initialise pygame, set display and clock
WIDTH = 600
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



#map
world = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

TILE = WIDTH/len(world)

tile_list = []
for row_num, row in enumerate(world):
    for col_num, col in enumerate(row):
        if col == 1:
            x, y = col_num * TILE, row_num * TILE
            rect = pygame.Rect(x, y, TILE, TILE)
            tile_list.append(rect)


planeX = 0
planeY = 0.66

dirX = -1
dirY = 0

player_rect = pygame.Rect(60, 60, 30, 30)
vel = 0.5
fps = 60

#sets the origin for all vectors
startpoint = pygame.math.Vector2(player_rect[0] + player_rect[2]/2, player_rect[1] + player_rect[3]/2)

#sets the differnt endpoints for all vectors
endpoint = pygame.math.Vector2(15,0)


fov = 60
rayDistance = 5
angle = 0
angleDifference = 0

angle_rest = angle - fov//2

turnRate = 5
dis = 0

lineH = 0
lineW = WIDTH/(fov/rayDistance)
lineO = HEIGHT - lineH/2

#raycasting  
#incredibly inefficient
def castRay(rayAngle):
    angleRad = math.radians(rayAngle)
    dx, dy = math.cos(angleRad), math.sin(angleRad)
    s = max(abs(dx), abs(dy))
    dx /= s
    dy /= s

    COLLIDE = False
    x, y = startpoint
    while not COLLIDE:
        x += dx
        y += dy

        point = pygame.Rect(x,y, 1,1)
        for tile in tile_list:
            rect = pygame.Rect(tile)
            if(point.colliderect(rect)):
                COLLIDE = True

    return math.sqrt((startpoint[0] - x) ** 2 + (startpoint[1] - y) ** 2)

while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    
    # get pressed keys
    keys = pygame.key.get_pressed()
    
    # delta x and delta y values
    dx, dy = 0, 0

    startpoint = pygame.math.Vector2(player_rect[0] + player_rect[2]/2, player_rect[1] + player_rect[3]/2)
    current_endpoint = startpoint + endpoint.rotate(angle)
    


    
    #movement
    if keys[pygame.K_UP]:
        dx -= (startpoint[0] - current_endpoint[0])*vel
        dy -= (startpoint[1] - current_endpoint[1])*vel
    if keys[pygame.K_DOWN]:
        dx += (startpoint[0] - current_endpoint[0])*vel
        dy += (startpoint[1] - current_endpoint[1])*vel
    if keys[pygame.K_RIGHT]:
        angle = (angle+turnRate) % 360     
    if keys[pygame.K_LEFT]:
        angle = (angle-turnRate) % 360

    # this is where collision detection starts

    x_projection = player_rect.move(dx, 0)
    y_projection = player_rect.move(0, dy)

    for tile in tile_list:


        if x_projection.colliderect(tile):
            if dx > 0:
                dx = tile.left - player_rect.right
            elif dx < 0:
                dx = tile.right - player_rect.left

        elif y_projection.colliderect(tile):
            if dy > 0:
                dy = tile.top - player_rect.bottom
            elif dy < 0:
                dy = tile.bottom - player_rect.top
    player_rect.move_ip(dx, dy)


    



    for ray in range(int(fov//rayDistance)):
        angleDifference = math.radians((angle - (angle-fov/2+ray*rayDistance)) % 360)

        dis = castRay(angle - fov/2+ ray*rayDistance) 
        dis *= math.cos(angleDifference)
        lineH = (TILE*HEIGHT)/dis
        if lineH > HEIGHT:
            lineH = HEIGHT
        lineO = (HEIGHT - lineH)/2
        pygame.draw.rect(screen, (255,255,255), (ray * lineW, lineO, lineW, lineH))
        
        
    # remember to update the display
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
