# https://stackoverflow.com/questions/68825905/
# import pygame
import pygame

# initialise pygame, set display and clock
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

# constant for tile size, this size is because screen is 600x600 pixels,
# there are 12 tiles per column per row so each tile gets displayed
TILE = 50

# world matrix, this is where you create the world layout of tiles,
# if you want to have thinner walls, increase the row and grid count
# and decrease the tile size
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

# tile list which will contain all the valid tiles (rectangles)
# you could append also the number and then change the number
# in the world matrix to apply some different textures
tile_list = []
for row_num, row in enumerate(world):
    for col_num, col in enumerate(row):
        # if the current tile is 1 in the matrix then calculate
        # its position and append the rectangular area to the tile_list
        if col == 1:
            x, y = col_num * TILE, row_num * TILE
            rect = pygame.Rect(x, y, TILE, TILE)
            tile_list.append(rect)

# player stuff, like player's rectangle to allow for
# easier collision detection
player_rect = pygame.Rect(60, 60, 30, 30)
vel = 3
fps = 60

while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    
    # get pressed keys
    keys = pygame.key.get_pressed()
    # delta x and delta y values that allow to move
    # player in either direction, they are like
    # a helper variable since
    # they don't directly affect player movement thus
    # allowing for additional checks like collision detection
    dx, dy = 0, 0
    # the basic key stuff, the reason to reduce instead of set the 
    # value is in case both keys are pressed so that the player stays in place
    # basically makes both keys equivalent
    if keys[pygame.K_UP]:
        dy -= vel
    if keys[pygame.K_DOWN]:
        dy += vel
    if keys[pygame.K_RIGHT]:
        dx += vel
    if keys[pygame.K_LEFT]:
        dx -= vel
    
    # this is where collision detection starts
    # first I create two projections of where the player might be
    # depending on what keys they pressed, `.move()` returns a new
    # rectangle allowing to easily apply `.colliderect()  method
    x_projection = player_rect.move(dx, 0)
    y_projection = player_rect.move(0, dy)
    # now for each placed tile check against collision
    for tile in tile_list:
        # also draw the rectangle here too
        pygame.draw.rect(screen, (255, 255, 0), tile)

        # can add the border
        # pygame.draw.rect(screen, (255, 255, 255), tile, width=1)
        
        # `pygame.Rect` has a built-in method for checking the collision
        if x_projection.colliderect(tile):
            print(tile)
            # depending on player movement calculate delta x
            # so that the player can touch the wall and there
            # wouldn't be any gaps between player and wall
            # the same logic for checking
            # y collision
            if dx > 0:
                dx = tile.left - player_rect.right
            elif dx < 0:
                dx = tile.right - player_rect.left

        elif tile.colliderect(y_projection):
            print(tile)
            if dy > 0:
                dy = tile.top - player_rect.bottom
            elif dy < 0:
                dy = tile.bottom - player_rect.top
    
    # move the player's rectangle in place meaning
    # it moves the actual rectangle instead of returning
    # an new one as `.move` would do
    player_rect.move_ip(dx, dy)
    # draw the player cube on screen
    pygame.draw.rect(screen, (255, 0, 0), player_rect)
    # can also draw border
    # pygame.draw.rect(screen, (0, 0, 255), player_rect, width=1)

    # event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # remember to update the display
    pygame.display.update()
