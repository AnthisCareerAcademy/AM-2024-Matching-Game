import pygame
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
screen = pygame.display.set_mode((800, 800))
font = pygame.font.SysFont('Arial', 24)

# Display top scores
def display_scores():
    y_offset = 10
    for score in top_scores:
        score_text = f"{score['name']}: {score['time']}s"
        text = font.render(score_text, True, (255, 255, 255))
        screen.blit(text, (650, y_offset))
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

pygame.quit()








