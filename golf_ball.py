 #finished on 2021/8/9 while listening to cherry by harry styles
import pygame

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width,height))

ball_x = 400
ball_y = 300
ball_r = 12.5

mouse_pos = pygame.mouse.get_pos()
mouse_s = False
initial_mouse_pos = pygame.mouse.get_pos()
end_mouse_pos = pygame.mouse.get_pos()

dx = initial_mouse_pos[0] - end_mouse_pos[0]
dy = initial_mouse_pos[1] - end_mouse_pos[1]

#the higher the number the lower the friction
friction = 15

friction_x = dx/friction
friction_y = dy/friction

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    mouse_pos = pygame.mouse.get_pos()
    mouse_state = pygame.mouse.get_pressed()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        initial_mouse_pos = pygame.mouse.get_pos()
        mouse_s = True
        
    elif event.type == pygame.MOUSEBUTTONUP and mouse_s:
        mouse_s = False
        end_mouse_pos = pygame.mouse.get_pos()
        
        dx = initial_mouse_pos[0] - end_mouse_pos[0]
        dy = initial_mouse_pos[1] - end_mouse_pos[1]

    
    
    friction_x = dx/friction
    friction_x = -friction_x
    
    friction_y = dy/friction
    friction_y = -friction_y

    dx += friction_x
    dy += friction_y
    if ball_x < width - ball_r and ball_x > 0 + ball_r:
        ball_x += dx
    if ball_y < height - ball_r and ball_y > 0 + ball_r:
        ball_y += dy

    if ball_x > width - ball_r:
        ball_x = width - ball_r - 1
        dx = -dx
    if ball_x < 0 + ball_r:
        ball_x = 0 + ball_r + 1
        dx = -dx

    if ball_y > height - ball_r:
        ball_y = height - ball_r - 1
        dy = -dy
    if ball_y < 0 + ball_r:
        ball_y = 0 + ball_r + 1
        dy = -dy
        
         
    screen.fill((50, 168, 82))
    
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_r)
    pygame.display.update()
pygame.quit()
