import pygame, sys, button, os

pygame.init()
clock = pygame.time.Clock()
FPS = 60
VEL = 5
puck_x_vel = 4
puck_y_vel = 4
red_score = 0
blue_score = 0

WIDTH, HEIGHT = 1152, 648
#colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ICE_BLUE = (63, 196, 210)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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

#create score text
gamefont = pygame.font.Font('freesansbold.ttf', 25)


def draw_text(text):
    draw_text = font.render(text, 1, BLACK)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    pygame.quit()
    sys.exit()
    

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
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH - red.width:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL

def handle_puck_movment(puckRect, pmask, red, rmask, blue, bmask):
    global puck_x_vel, puck_y_vel

    puckRect.x += puck_x_vel
    puckRect.y += puck_y_vel

    if(puckRect.right >= WIDTH + 100 or puckRect.left <= 0):
        puck_x_vel *= -1
    if(puckRect.bottom >= HEIGHT or puckRect.top <= 0):
        puck_y_vel *= -1

    offsetr_x = red.x - puckRect.x
    offsetr_y = red.y - puckRect.y

    if rmask.overlap(pmask, (int(offsetr_x), int(offsetr_y))):
        if abs(red.top - puckRect.bottom) < 50 and puck_y_vel > 0:
            print("bottom")
            puck_y_vel *= -1
        if abs(red.bottom - puckRect.top) < 50 and puck_y_vel < 0:
            print("top")
            puck_y_vel *= -1
        if abs(red.right - puckRect.left) < 50 and puck_x_vel < 0:
            print("right")
            puck_x_vel *= -1
        if abs(red.left - puckRect.right) < 400 and puck_x_vel > 0:
            print("left")
            puck_x_vel *= -1

    offsetb_x = blue.x - puckRect.x
    offsetb_y = blue.y - puckRect.y

    if bmask.overlap(pmask, (int(offsetb_x), int(offsetb_y))):
        if abs(blue.top - puckRect.bottom) < 50 and puck_y_vel > 0:
            print("bottom")
            puck_y_vel *= -1
        if abs(blue.bottom - puckRect.top) < 50 and puck_y_vel < 0:
            print("top")
            puck_y_vel *= -1
        if abs(blue.right - puckRect.left) < 50 and puck_x_vel < 0:
            print("right")
            puck_x_vel *= -1
        if abs(blue.left - puckRect.right) < 50 and puck_x_vel > 0:
            print("left")
            puck_x_vel *= -1

def game_screen():
    #create players and pucks
    redRect = pygame.Rect(700, 300, 50, 50)
    blueRect = pygame.Rect(100, 300, 50, 50)
    puckRect = pygame.Rect(WIDTH / 2 - 60, HEIGHT / 2 - 35, 200, 70)
    puckmask = pygame.mask.from_surface(puck)
    redmask = pygame.mask.from_surface(redPlayer)
    bluemask = pygame.mask.from_surface(bluePlayer)

    bluetext = gamefont.render(f'Blue Score: {blue_score}', True, BLUE)
    redtext = gamefont.render(f'Red Score: {red_score}', True, RED)

    run = True
    while run:
        WIN.blit(BACKGROUND, (0,0))
        WIN.blit(redPlayer, (redRect.x, redRect.y))
        WIN.blit(bluePlayer, (blueRect.x, blueRect.y))
        WIN.blit(puck, (puckRect.x, puckRect.y))
        WIN.blit(bluetext, (30, 10))
        WIN.blit(redtext, (WIDTH - 200, 10))

        if red_score == 3:
            draw_text("Red wins!!")
        if blue_score == 3:
            draw_text("Blue wins!!")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_red_movment(keys_pressed, redRect)
        handle_blue_movment(keys_pressed, blueRect)
        handle_puck_movment(puckRect, puckmask, redRect, redmask, blueRect, bluemask)

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