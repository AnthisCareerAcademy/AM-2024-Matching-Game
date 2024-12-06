import pygame, sys
import pygame.freetype
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

# Screen setup

pygame.init()
pygame.display.set_caption('Matching Card Game')
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

fullscreen = False

#Fullscreen code
while True:
    screen.fill((200, 215, 230))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
    pygame.display.update()


# Main function for stopwatch
    def main():
        pygame.init()
        clock = pygame.time.Clock()
        font = pygame.freetype.SysFont(None, 34)
        font.origin = True
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: return
            screen.fill(pygame.Color(200, 215, 230))
            ticks = pygame.time.get_ticks()

            seconds = int(ticks / 1000 % 60)
            out = '{seconds:02d}'.format(seconds=seconds)
            font.render_to(screen, (25, 50), out, pygame.Color('DarkBlue'))
            pygame.display.flip()
            clock.tick(60)


    if __name__ == '__main__': main()

# Quit pygame safely
    pygame.quit()