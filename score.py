import pygame
import pygame.freetype
from pygame.locals import *

pygame.init()

# Initialize variables
top_scores = [
    {"name": "json", "time": 120},
    {"name": "mi", "time": 85},
    {"name": "melody", "time": 95},
]

# Example score
top_scores = sorted(top_scores, key=lambda x: x['time'])[:3]  # Top 3 scores

# Pygame display setup
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
font = pygame.freetype.SysFont(None, 24)
font.origin = True

# Display top scores
def display_scores():
    y_offset = 10
    for score in top_scores:
        score_text = f"{score['name']}: {score['time']}s"
        text = font.render(score_text, True, (255, 255, 255))
        screen.blit(text, (screen.get_width()-200, y_offset))
        y_offset += 30

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    display_scores()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Function to display the timer
def display_timer(ticks):
    millis = ticks % 100








