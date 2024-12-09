import pygame, sys
from pygame.locals import *
import pygame.freetype

pygame.init()

mainClock = pygame.time.Clock()

# Set up the screen size and fullscreen mode
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((800, 600), RESIZABLE)
fullscreen = False

# Card size and image loading
def create_cards(card_size):
    card = pygame.image.load("images/memory_back.png")
    card = pygame.transform.scale(card, (card_size, card_size))  # Set card size
    return card

# Function to display the stopwatch in the top-left corner
def display_stopwatch(start_time):
    font = pygame.freetype.SysFont(None, 34)
    font.origin = True
    elapsed_time = pygame.time.get_ticks() - start_time  # Elapsed time in milliseconds
    seconds = (elapsed_time // 1000) % 60
    time_str = f"{seconds:02}"
    font.render_to(screen, (25, 50), time_str, pygame.Color('DarkBlue'))

# Create a 4x4 grid of cards
def create_grid_cards():
    # Get the width and height of the screen
    screen_width, screen_height = screen.get_size()

    # Space reserved for the stopwatch (top-left corner)
    stopwatch_margin = 70  # Reserve space for the stopwatch at the top-left corner

    # Number of rows and columns in the grid
    rows = 4
    cols = 4

    # Space between cards
    margin = 10

    # Calculate the size of each square card
    available_width = screen_width - (cols + 1) * margin  # Remaining width after margins
    available_height = screen_height - stopwatch_margin - (
                rows + 1) * margin  # Remaining height after margins and stopwatch space

    # Set card size to fit the available space (adjusted to keep the cards square)
    card_size = min(available_width // cols, available_height // rows)

    # Create the cards and store their positions
    cards = []
    for row in range(rows):
        for col in range(cols):
            x = margin + col * (card_size + margin)
            y = stopwatch_margin + margin + row * (card_size + margin)
            card = create_cards(card_size)
            card_rect = card.get_rect(topleft=(x, y))
            cards.append((card, card_rect))

    return cards


# Main game loop
start_time = pygame.time.get_ticks()  # Get the starting time for the stopwatch
cards = create_grid_cards()  # Get the 16 cards in a grid

while True:
    screen.fill((200, 215, 230))

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            # Recalculate the card positions when the screen is resized
            cards = create_grid_cards()
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

    # Display the stopwatch
    display_stopwatch(start_time)

    # Draw all the cards in the grid
    for card, card_rect in cards:
        screen.blit(card, card_rect)

    pygame.display.update()  # Update the display
    mainClock.tick(60)  # Frame rate control
