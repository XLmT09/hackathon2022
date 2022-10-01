import pygame, sys

pygame.init()
clock = pygame.time.Clock()
FPS = 60

WIDTH, HEIGHT = 1152, 648

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hockey Game")

#text object
#create menu text object
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
        WIN.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.quit()

if __name__ == "__main__":
    main_menu()