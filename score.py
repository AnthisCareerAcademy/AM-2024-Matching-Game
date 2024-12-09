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

# Display setup
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Top Scores")

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

# Function to update the top scores
def update_top_scores(name, time):
    top_scores.append({"name": name, "time": time}) # Add the new score
    top_scores.sort(key=lambda x:x['time']) # Sort and keep top 3 scores
    top_scores[:] = top_scores[:3] 







