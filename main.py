import pygame, sys, button, os

pygame.init()
clock = pygame.time.Clock()
FPS = 60
VEL = 5

WIDTH, HEIGHT = 1152, 648
#colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ICE_BLUE = (63, 196, 210)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hockey Game")

#get button images

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Mappng.png")).convert(), (WIDTH, HEIGHT))
START_IMG = pygame.image.load("assets\startbt.png").convert_alpha()
QUIT_IMG = pygame.image.load("assets\quitbtn.png").convert_alpha()

#create button objects
start_btn = button.Button(350, 400, START_IMG, 1)
quit_btn = button.Button(600, 400, QUIT_IMG, 1)
redPlayer = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RedPuck.png")), (100,65))
bluePlayer = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "BluePuck.png")), (125,85))
puck = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "BlackPukc.png")), (120,70))
#text object
#create menu text object
font = pygame.font.Font('freesansbold.ttf', 50)
text = font.render('Menu Screen', True, BLACK, ICE_BLUE)
textRect = text.get_rect()
textRect.center = (550, 250)

def handle_blue_movment(keys_pressed, blue):
    if keys_pressed[pygame.K_a] and blue.x - VEL > 0:  # LEFT
        blue.x -= VEL
    if keys_pressed[pygame.K_d] and blue.x + VEL + blue.width < WIDTH / 2 - blue.width:  # RIGHT
        blue.x += VEL
    if keys_pressed[pygame.K_w] and blue.y - VEL > 0:  # UP
        blue.y -= VEL
    if keys_pressed[pygame.K_s] and blue.y + VEL + blue.height < HEIGHT - 15:  # DOWN
        blue.y += VEL

def handle_red_movment(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > WIDTH / 2 - VEL:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH - VEL:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL

def game_screen():
    #create players and pucks
    redRect = pygame.Rect(700, 300, 50, 50)
    blueRect = pygame.Rect(100, 300, 50, 50)
    run = True
    while run:
        WIN.blit(BACKGROUND, (0,0))
        WIN.blit(redPlayer, (redRect.x, redRect.y))
        WIN.blit(bluePlayer, (blueRect.x, blueRect.y))
        WIN.blit(puck, (400, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_red_movment(keys_pressed, redRect)
        handle_blue_movment(keys_pressed, blueRect)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

def main_menu():
    run = True
    while run:
        WIN.fill(ICE_BLUE)
        WIN.blit(text, textRect)

        if start_btn.draw(WIN):
            game_screen()
        if quit_btn.draw(WIN):
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()