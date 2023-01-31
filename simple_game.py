import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('First Game')

BACKGROUND_COLOR = (255,255,255)
BORDER_COLOR = (0,0,0)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

MIDDLE = (HEIGHT/2)-SPACESHIP_HEIGHT
MIDDLE_BORDER = pygame.Rect((WIDTH/2)-10,0,10,HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load('assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load('assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)

def draw_window(red,yellow):
    WIN.fill(BACKGROUND_COLOR)
    pygame.draw.rect(WIN,BORDER_COLOR,MIDDLE_BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x,red.y))
    pygame.display.update()
    
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < MIDDLE_BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL
        
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > MIDDLE_BORDER.x + MIDDLE_BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL

def main():
    
    red = pygame.Rect(700,MIDDLE,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(200,MIDDLE,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    
    red_bullets = [] 
    yellow_bullets = [] 
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x,red.y + red.height/2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        print(red_bullets,yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        
        # handle_bullets(red_bullets,yellow_bullets,red,yellow)
        
        draw_window(red,yellow)       
                
                
                
    pygame.quit()

if __name__ == "__main__":
    main() 