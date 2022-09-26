import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Pygame Practice Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/atari-font-full-version/atari_full.ttf', 25) #(font type, font size)
game_active = True

sky_surface = pygame.image.load('graphics/cloudbackground.webp').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface = test_font.render('My game', False, (64,64,64)).convert() #(text, AA, color) AA means anti-aliasing, or smoothing the edges of the text: must be TRUE or FALSE
score_rect = score_surface.get_rect(center = (250, 150))

enemy_surface = pygame.image.load('graphics/tile026.png').convert_alpha()
enemy_rect = enemy_surface.get_rect(midbottom = (210, 415))

player_surface = pygame.image.load('graphics/charactertest2.gif').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,435)) #get_rect just takes the surface you inputted and draws a rectangle around it
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 430:
                player_gravity = -20
                #allows me to jump when i click on player
       
        #if event.type == pygame.MOUSEBUTTONDOWN:
         #   print('mouse down')
            #whenever i click, it will print mousedown, if i use MOUSEBUTTONUP, then it will react when the mouse is released
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 430:
                player_gravity = -20
                #allows me to jump when i click space
         


    screen.blit(sky_surface, (0,0)) #blit stabds for block image transfer, putting one surface on another surface, THESE COORDINATES ARE THE ORIGIN POINT OF THE SURFACE (top left corner)
    screen.blit(ground_surface, (-10,400))
    pygame.draw.rect(screen,(66,191,245),score_rect,12) #(surface we want to draw on, color, the rectangle we want to draw, *width*, *border radius*) '*' is optional
    pygame.draw.rect(screen,(66,191,245),score_rect) #this line fills in the empty space as the previous line only makes the border
    #pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100)) 
    #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10) #surface, color, start_pos, end_pos, width)
    if game_active:
        screen.blit(score_surface, score_rect)

    
        if enemy_rect.right <= 0:
            enemy_rect.left = 600
        enemy_rect.x -= 4
    screen.blit(enemy_surface, enemy_rect)

    #player_rect.left += 1 
    # #moves the player by grabbing the left of the rectangle and moving it one pixel, you can also print player_rect.left to get the actual positon of the rectangle
    
    #Player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 430:
        player_rect.bottom = 430
    screen.blit(player_surface, player_rect)


    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
     #   print('jump')

    #if player_rect.colliderect(enemy_rect) == True: #returns false or true, if there is no collision then false, if there is collision then true
    #    print('collision')
    #else:
    #    print('False')
    
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse_pos)):
       # print(pygame.mouse.get_pressed())
        #(false, false, false) = first false is left click, second false is 'middle click', third false is right click

    # collision
    

    pygame.display.update()
    clock.tick(60) #tells pygame that this while loop should not run faster than 60 fps (max framerate)
