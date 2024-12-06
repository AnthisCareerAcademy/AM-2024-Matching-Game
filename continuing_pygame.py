import pygame
from pygame.locals import *

pygame.init()
running = True

size = width, height = (800, 800)

# Create an 800 by 800 display.
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Matching Game")
screen.fill((200, 215, 230))
pygame.display.update()

# This is the main game loop.
while running:

    # This code gets the different events from PyGame and loops through them.
    for event in pygame.event.get():
        # If the event is the QUIT event (X button or Alt+F4), then exit the
        # loop.
        if event.type == QUIT:
            running = False

pygame.quit()