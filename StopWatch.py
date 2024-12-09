import pygame
import pygame.freetype
import pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the screen and font
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Stopwatch")

font = pygame.freetype.SysFont(None, 24)
font.origin = True

# Function to display the timer
def display_timer(ticks):
    millis = ticks % 1000
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 60)
    timer_text = f"{minutes:02d}:{seconds:02d}:{millis}"
    text = font.render(timer_text, True, (255, 255, 255))
    screen.blit(text, (10, 10))

# Main stopwatch loop (this can be imported and run in the main game)
def run_timer():
    running = True
    start_ticks = pygame.time.get_ticks()  # Start time
    while running:
        screen.fill((200, 215, 230))  # Background color

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Timer logic
        ticks = pygame.time.get_ticks() - start_ticks  # Elapsed time in milliseconds
        display_timer(ticks)

        pygame.display.update()
        pygame.time.Clock().tick(60)  # Run at 60 FPS

    pygame.quit()
