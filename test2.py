import pygame
from pygame.locals import *


def name():
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    name = ""
    input = ''
    font = pygame.font.Font(None, 50)
    color = ''
    dim = 13
    dimcar=int(480//13)
    colors = [pygame.Color("white"), pygame.Color("gray")]
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    input = name
                    name = ""
            elif evt.type == QUIT:
                return
        if input == "text":
            for i in range(dim):
                for x in range(dim):
                    color = colors[((i + x) % 2)]
                    text=pygame.draw.rect(screen, color, pygame.Rect(i * dimcar, x * dimcar, dimcar, dimcar))

        else:
            screen.fill((30, 30, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()


if __name__ == "__main__":
    name()
    pygame.quit()
