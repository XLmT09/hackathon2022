import pygame, sys, button

pygame.init()
clock = pygame.time.Clock()
FPS = 60

WIDTH, HEIGHT = 1152, 648
#colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ICE_BLUE = (63, 196, 210)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hockey Game")

#get button images
START_IMG = pygame.image.load("assets\startbt.png").convert_alpha()
QUIT_IMG = pygame.image.load("assets\quitbtn.png").convert_alpha()
#create button objects
start_btn = button.Button(300, 400, START_IMG, 1)
quit_btn = button.Button(600, 400, QUIT_IMG, 1)

#text object
#create menu text object
font = pygame.font.Font('freesansbold.ttf', 50)
text = font.render('Menu Screen', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (600, 250)

def game_screen():
    run = True
    while run:
        WIN.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.quit()

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