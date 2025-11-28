import sys, pygame
import colours
pygame.init()
size = width, height = 1000, 800
flags = pygame.FULLSCREEN | pygame.SCALED
screen = pygame.display.set_mode(size, flags)
pygame.display.set_caption("hello world.")


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
    screen.fill(colours.black)
    pygame.draw.circle(screen, colours.white, (0,0), 30)
    pygame.draw.circle(screen, colours.white, (1000,0), 30)
    pygame.draw.circle(screen, colours.white, (0,800), 30)
    pygame.draw.circle(screen, colours.white, (1000,800), 30)
    pygame.display.flip()
