import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render('Score: ' + str(current_time),False,(64,64,64))
    score_rect = score_surface.get_rect(center = (250, 150))
    screen.blit(score_surface, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 415:
                screen.blit(enemy_surface,obstacle_rect)
            else:
                screen.blit(enemyfly_surface,obstacle_rect)


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 415:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]
    #play walking animation when player is on floor
    #play jump animation when player is not on floor

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Pygame Practice Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/atari-font-full-version/atari_full.ttf', 25) #(font type, font size)
game_active = True
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/cloudbackground.webp').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface = test_font.render('My game', False, (64,64,64)).convert() 
#(text, AA, color) AA means anti-aliasing, or smoothing the edges of the text: must be TRUE or FALSE
#score_rect = score_surface.get_rect(center = (250, 150))

#obstacles
enemy_frame_1 = pygame.image.load('graphics/enemy.png').convert_alpha()
enemy_frame_2 = pygame.image.load('graphics/enemy_2.png').convert_alpha()
enemy_frames = [enemy_frame_1,enemy_frame_2]
enemy_frame_index = 0
enemy_surface = enemy_frames[enemy_frame_index]

enemyfly_frame1 = pygame.image.load('graphics/fly_1.png').convert_alpha()
enemyfly_frame2 = pygame.image.load('graphics/fly_2.png').convert_alpha()
enemyfly_frames = [enemyfly_frame1,enemyfly_frame2]
enemyfly_frame_index = 0
enemyfly_surface = enemyfly_frames[enemyfly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('graphics/charactertest3.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player_jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (100, 415)) #get_rect just takes the surface you inputted and draws a rectangle around it
player_gravity = 0

#intro screen
player_stand = pygame.image.load('graphics/charactertest3.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,3)
player_stand_rect = player_stand.get_rect(center = (400, 250))

game_name = test_font.render('Trashy Game', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,100))

game_message = test_font.render('Press space to start',False,'Black')
game_message_rect = game_message.get_rect(center = (400, 400))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400) #(event you want to trigger, how often to trigger it in milliseconds)

enemy_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_animation_timer,500)

enemyfly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(enemyfly_animation_timer,200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 415:
                    player_gravity = -20
                    #allows me to jump when i click on player
        
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #   print('mouse down')
                #whenever i click, it will print mousedown, if i use MOUSEBUTTONUP, then it will react when the mouse is released
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 413:
                    player_gravity = -20
                    #allows me to jump when i click space
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(enemy_surface.get_rect(midbottom = (randint(900, 1100), 415)))
                else:
                    obstacle_rect_list.append(enemyfly_surface.get_rect(midbottom = (randint(900, 1100), 300)))

            if event.type == enemy_animation_timer:
                if enemy_frame_index == 0:
                    enemy_frame_index == 1
                else:
                    enemy_frame_index == 0
                enemy_surface = enemy_frames[enemy_frame_index]

            if event.type == enemyfly_animation_timer:
                if enemyfly_frame_index == 0:
                    enemyfly_frame_index == 1
                else:
                    enemyfly_frame_index == 0
                enemyfly_surface = enemyfly_frames[enemyfly_frame_index]


    if game_active:
        screen.blit(sky_surface, (0,0)) #blit stabds for block image transfer, putting one surface on another surface, THESE COORDINATES ARE THE ORIGIN POINT OF THE SURFACE (top left corner)
        screen.blit(ground_surface, (-10,400))
        
        #pygame.draw.rect(screen,(66,191,245),score_rect,12) #(surface we want to draw on, color, the rectangle we want to draw, *width*, *border radius*) '*' is optional
        #pygame.draw.rect(screen,(66,191,245),score_rect) #this line fills in the empty space as the previous line only makes the border
        #pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100)) 
        #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10) #surface, color, start_pos, end_pos, width)
        #screen.blit(score_surface, score_rect)
        score = display_score()
        
        
        
            

        
            #if enemy_rect.right <= 0:
             #   enemy_rect.left = 800
            #enemy_rect.x -= 4
        #screen.blit(enemy_surface, enemy_rect)

        #player_rect.left += 1 
        # #moves the player by grabbing the left of the rectangle and moving it one pixel, you can also print player_rect.left to get the actual positon of the rectangle
        
        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 415:
            player_rect.bottom = 415
        player_animation()
        screen.blit(player_surface, player_rect)

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        game_active = collisions(player_rect,obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (100,415)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,400))
        screen.blit(game_name,game_name_rect)

        if score ==  0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)
            
        


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

    
    pygame.display.update()
    clock.tick(60) #tells pygame that this while loop should not run faster than 60 fps (max framerate)
