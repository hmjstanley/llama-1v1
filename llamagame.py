import pygame
import os
import button
import time

pygame.mixer.init()

WIDTH,HEIGHT = 1240,860
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Llama game!")

NAVY_BLUE = (63,58,104)


UPPER,LOWER,LEFT,LEFT_BORDER,RIGHT,RIGHT_BORDER = -8,820,32,588,1208,652

FPS = 60
VEL = 5
SPIT_VEL = 10
MAX_BULLETS = 3
VOLUME = 0.2

BACKGROUND_SIZE = (WIDTH,HEIGHT)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Llama_Background.png')).convert(),BACKGROUND_SIZE)

LLAMA_WIDTH,LLAMA_HEIGHT = (80,116)
LLAMA_SIZE = (LLAMA_WIDTH,LLAMA_HEIGHT)
RED_LLAMA = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Red_Llama.png')),LLAMA_SIZE)
RED_LLAMA_HIT = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Red_Llama_Hit.png')),LLAMA_SIZE)

BLUE_LLAMA = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Blue_Llama.png')),LLAMA_SIZE),True,False)
BLUE_LLAMA_HIT = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Blue_Llama_Hit.png')),LLAMA_SIZE),True,False)

SPIT_SIZE = (16,8)
LLAMA_SPIT = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Llama_Spit.png')),SPIT_SIZE)

SPIT_SOUND = pygame.mixer.Sound('Llama_Spit_Sound.mp3')
SPIT_SOUND.set_volume(VOLUME)
HIT_SOUND = pygame.mixer.Sound('Llama_Hit_Sound.mp3')
HIT_SOUND.set_volume(VOLUME)
VICTORY_SOUND = pygame.mixer.Sound('Victory_Sound.wav')
VICTORY_SOUND.set_volume(VOLUME)
BUTTON_SOUND = pygame.mixer.Sound('Llama_Button_Press.mp3')
BUTTON_SOUND.set_volume(VOLUME)

RED_HIT = pygame.USEREVENT + 1
BLUE_HIT = pygame.USEREVENT + 2

HEART_SIZE = (84,72)
RED_HEART = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Red_Heart.png')),HEART_SIZE)
RED_HALF_HEART = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Red_Half_Heart.png')),HEART_SIZE)
BLUE_HEART = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Blue_Heart.png')),HEART_SIZE)
BLUE_HALF_HEART = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Blue_Half_Heart.png')),HEART_SIZE)
DEAD_HEART = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Dead_Heart.png')),HEART_SIZE)

BANNER_SIZE = (832,160)
RED_BANNER = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Red_Banner.png')),BANNER_SIZE)
BLUE_BANNER = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Blue_Banner.png')),BANNER_SIZE)

BUTTON_WIDTH,BUTTON_HEIGHT = 576,96
BUTTON_SIZE = (BUTTON_WIDTH,BUTTON_HEIGHT)
PLAY_BUTTON= pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Play_Button.png')),BUTTON_SIZE)
HOVER_PLAY_BUTTON= pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Hover_Play_Button.png')),BUTTON_SIZE)
PRESSED_PLAY_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Pressed_Play_Button.png')),BUTTON_SIZE )

EXIT_BUTTON= pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Exit_Button.png')),BUTTON_SIZE)
HOVER_EXIT_BUTTON= pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Hover_Exit_Button.png')),BUTTON_SIZE)
PRESSED_EXIT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Pressed_Exit_Button.png')),BUTTON_SIZE )

RESUME_BUTTON= pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Resume_Button.png')),BUTTON_SIZE)
HOVER_RESUME_BUTTON= pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Hover_Resume_Button.png')),BUTTON_SIZE)
PRESSED_RESUME_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Llama Assets','Pressed_Resume_Button.png')),BUTTON_SIZE )

play_button = button.Button((WIDTH//2 - BUTTON_WIDTH//2),(HEIGHT//2 - BUTTON_HEIGHT - 16),PLAY_BUTTON,HOVER_PLAY_BUTTON)
resume_button = button.Button((WIDTH//2 - BUTTON_WIDTH//2),(HEIGHT//2 - BUTTON_HEIGHT - 16),RESUME_BUTTON,HOVER_RESUME_BUTTON)
exit_button = button.Button((WIDTH//2 - BUTTON_WIDTH//2),(HEIGHT//2 + 16),EXIT_BUTTON,HOVER_EXIT_BUTTON)

def draw_window(red,blue,red_bullets,blue_bullets,red_health,blue_health,red_llama,blue_llama):
    WIN.blit(BACKGROUND,(0,0))
    
    WIN.blit(red_llama,(red.x,red.y))
    WIN.blit(blue_llama,(blue.x,blue.y))

    for bullet in red_bullets:
        WIN.blit(LLAMA_SPIT,(bullet.x,bullet.y))
    for bullet in blue_bullets:
        WIN.blit(LLAMA_SPIT,(bullet.x,bullet.y))

    HEART_HEIGHT = HEIGHT - RED_HEART.get_height() - 12
    HEART_WIDTH = RED_HEART.get_width()

    if red_health >= 2:
        WIN.blit(RED_HEART,(12,HEART_HEIGHT))
    elif red_health == 1:
        WIN.blit(RED_HALF_HEART,(12,HEART_HEIGHT))
    else:
        WIN.blit(DEAD_HEART,(12,HEART_HEIGHT))

    if red_health >= 4:
        WIN.blit(RED_HEART,(HEART_WIDTH + 24,HEART_HEIGHT))
    elif red_health == 3:
        WIN.blit(RED_HALF_HEART,(HEART_WIDTH + 24,HEART_HEIGHT))
    else:
        WIN.blit(DEAD_HEART,(HEART_WIDTH + 24,HEART_HEIGHT))

    if red_health == 6:
        WIN.blit(RED_HEART,(HEART_WIDTH*2 + 36,HEART_HEIGHT))
    elif red_health == 5:
        WIN.blit(RED_HALF_HEART,(HEART_WIDTH*2 + 36,HEART_HEIGHT))
    else:
        WIN.blit(DEAD_HEART,(HEART_WIDTH*2 + 36,HEART_HEIGHT))

    if blue_health >= 2:
        WIN.blit(BLUE_HEART,(WIDTH - HEART_WIDTH - 12,HEART_HEIGHT))
    elif blue_health == 1:
        WIN.blit(BLUE_HALF_HEART,(WIDTH - HEART_WIDTH - 12,HEART_HEIGHT))
    else:
        WIN.blit(DEAD_HEART,(WIDTH - HEART_WIDTH - 12,HEART_HEIGHT))

    if blue_health >= 4:
        WIN.blit(BLUE_HEART,(WIDTH - HEART_WIDTH*2 - 24,HEART_HEIGHT))
    elif blue_health == 3:
        WIN.blit(BLUE_HALF_HEART,(WIDTH - HEART_WIDTH*2 - 24,HEART_HEIGHT))
    else:
        WIN.blit(DEAD_HEART,(WIDTH - HEART_WIDTH*2 - 24,HEART_HEIGHT))

    if blue_health == 6:
        WIN.blit(BLUE_HEART,(WIDTH - HEART_WIDTH*3 - 36,HEART_HEIGHT))
    elif blue_health == 5:
        WIN.blit(BLUE_HALF_HEART,(WIDTH - HEART_WIDTH*3 - 36,HEART_HEIGHT))
    else:
        WIN.blit(DEAD_HEART,(WIDTH - HEART_WIDTH*3 - 36,HEART_HEIGHT))

    pygame.display.update()

def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_a] and red.x - VEL > LEFT: # left
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x + VEL + LLAMA_WIDTH < LEFT_BORDER: # right
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > UPPER: # up
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y + VEL + LLAMA_HEIGHT < LOWER: # down
        red.y += VEL

def blue_movement(keys_pressed,blue):
    if keys_pressed[pygame.K_LEFT] and blue.x - VEL > RIGHT_BORDER: # left
        blue.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and blue.x + VEL + LLAMA_WIDTH < RIGHT: # right
        blue.x += VEL
    if keys_pressed[pygame.K_UP] and blue.y - VEL > UPPER: # up
        blue.y -= VEL
    if keys_pressed[pygame.K_DOWN] and blue.y + VEL + LLAMA_HEIGHT < LOWER: # down
        blue.y += VEL

def handle_bullets(red_bullets,blue_bullets,blue,red):
    for bullet in red_bullets:
        bullet.x += SPIT_VEL
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            pygame.mixer.Sound.play(HIT_SOUND)
            red_bullets.remove(bullet)
        if bullet.x > WIDTH:
            red_bullets.remove(bullet)
    
    for bullet in blue_bullets:
        bullet.x -= SPIT_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            pygame.mixer.Sound.play(HIT_SOUND)
            blue_bullets.remove(bullet)
        if bullet.x + bullet.width < 0:
            blue_bullets.remove(bullet)

def Pause_Menu():
    clock = pygame.time.Clock()
    run = True
    y = False
    while run:
        clock.tick(FPS)
        WIN.fill(NAVY_BLUE)

        if resume_button.draw(WIN):
            WIN.fill(NAVY_BLUE)
            WIN.blit(PRESSED_RESUME_BUTTON,(WIDTH//2 - PLAY_BUTTON.get_width()//2,HEIGHT//2 - PLAY_BUTTON.get_height() - 16))
            WIN.blit(EXIT_BUTTON,(WIDTH//2 - EXIT_BUTTON.get_width()//2,HEIGHT//2 + 16))
            run = False
            x = True
            y = True

        if exit_button.draw(WIN):
            WIN.fill(NAVY_BLUE)
            WIN.blit(RESUME_BUTTON,(WIDTH//2 - PLAY_BUTTON.get_width()//2,HEIGHT//2 - PLAY_BUTTON.get_height() - 16))
            WIN.blit(PRESSED_EXIT_BUTTON,(WIDTH//2 - EXIT_BUTTON.get_width()//2,HEIGHT//2 + 16))
            run = False
            x = False
            y = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                x = False

        pygame.display.update()

        if y:
            time.sleep(0.05)
            pygame.mixer.Sound.play(BUTTON_SOUND)

    return x


def Main_Menu():
    clock = pygame.time.Clock()
    run = True
    y = False
    while run:
        clock.tick(FPS)
        WIN.fill(NAVY_BLUE)

        if play_button.draw(WIN):
            WIN.fill(NAVY_BLUE)
            WIN.blit(PRESSED_PLAY_BUTTON,(WIDTH//2 - PLAY_BUTTON.get_width()//2,HEIGHT//2 - PLAY_BUTTON.get_height() - 16))
            WIN.blit(EXIT_BUTTON,(WIDTH//2 - EXIT_BUTTON.get_width()//2,HEIGHT//2 + 16))
            run = False
            x = True
            y = True

        if exit_button.draw(WIN):
            WIN.fill(NAVY_BLUE)
            WIN.blit(PLAY_BUTTON,(WIDTH//2 - PLAY_BUTTON.get_width()//2,HEIGHT//2 - PLAY_BUTTON.get_height() - 16))
            WIN.blit(PRESSED_EXIT_BUTTON,(WIDTH//2 - EXIT_BUTTON.get_width()//2,HEIGHT//2 + 16))
            run = False
            x = False
            y = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                x = False

        pygame.display.update()

        if y:
            pygame.mixer.Sound.play(BUTTON_SOUND)
            time.sleep(0.05)

    return x

def main():

    run = Main_Menu()

    red = pygame.Rect(100,300,LLAMA_WIDTH,LLAMA_HEIGHT)
    blue = pygame.Rect(700,300,LLAMA_WIDTH,LLAMA_HEIGHT)

    red_bullets = []
    blue_bullets = []

    red_health = 6
    blue_health = 6

    red_hit_counter = 0
    blue_hit_counter = 0

    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width-16, red.y + 32,16,8)
                    pygame.mixer.Sound.play(SPIT_SOUND)
                    red_bullets.append(bullet)

                if event.key == pygame.K_ESCAPE:
                    run = Pause_Menu()

            if event.type == pygame.MOUSEBUTTONDOWN and len(blue_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(blue.x, blue.y + 32,16,8)
                pygame.mixer.Sound.play(SPIT_SOUND)
                blue_bullets.append(bullet)
            
            if event.type == RED_HIT:
                red_health -= 1
                red_hit_counter = 10
            if event.type == BLUE_HIT:
                blue_health -= 1
                blue_hit_counter = 10

        winner = ''
        if red_health <= 0:
            winner = 'BLUE'
        if blue_health <= 0:
            winner = 'RED'
        
        if red_hit_counter > 0:
                red_llama = RED_LLAMA_HIT
                red_hit_counter -= 1
        else:
            red_llama = RED_LLAMA


        if blue_hit_counter > 0:
            blue_llama = BLUE_LLAMA_HIT
            blue_hit_counter -= 1
        else:
            blue_llama = BLUE_LLAMA

        keys_pressed = pygame.key.get_pressed()
        red_movement(keys_pressed,red)
        blue_movement(keys_pressed,blue)

        handle_bullets(red_bullets,blue_bullets,blue,red)

        if winner != '':
            if winner == 'RED':
                WIN.blit(RED_BANNER,(WIDTH//2 - RED_BANNER.get_width()/2, RED_BANNER.get_height()/2))
                WIN.blit(DEAD_HEART,(WIDTH - BLUE_HEART.get_width() - 12,HEIGHT - RED_HEART.get_height() - 12))
            elif winner == 'BLUE':
                WIN.blit(BLUE_BANNER,(WIDTH//2 - BLUE_BANNER.get_width()/2, BLUE_BANNER.get_height()/2))
                WIN.blit(DEAD_HEART,(12,HEIGHT - RED_HEART.get_height() - 12))
            pygame.display.update()
            pygame.mixer.Sound.play(VICTORY_SOUND)

            end = True
            while end:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            main()
                            end = False
                            run = False
                    if event.type == pygame.QUIT:
                        end = False
                        run = False

        if run:
            draw_window(red,blue,red_bullets,blue_bullets,red_health,blue_health,red_llama,blue_llama)
    
    pygame.quit()

if __name__ == "__main__":
    main()
