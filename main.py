from match_card import MatchCard
import pygame
from pygame.locals import *
from random import shuffle

pygame.font.init()
pygame.init()
main_clock = pygame.time.Clock()


# Screen setup
pygame.init()
pygame.display.set_caption('Matching Card Game')
monitor_size = [
    pygame.display.Info().current_w,
    pygame.display.Info().current_h,
]
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

fullscreen = False
running = True

matches = 0
out = ""

# Card generation code.
card_w = (screen.get_width() - 30) * 0.75
card_h = (screen.get_height() - 80) * 0.75

# Keep the cards square.
card_size = int(min(card_w // 4, card_h // 4))

cards = []

cards_flipped = []

for i in range(4):
    for j in range(4):
        cards.append(MatchCard(
            i + (j % 2 * 4), 30 + i*(card_size + 10), 80 + j*(card_size + 10),
            card_size, card_size, f"images/memory-balls-{i+(j%2 * 4)+1}.jpg",
            "images/card_back.png"
        ))


shuffle(cards)

# End card generation code.

# Code to make the window fullscreen.
while running:
    screen.fill((200, 215, 230))
    font = pygame.font.SysFont('Arial', 34)

    # Event cases.
    for event in pygame.event.get():
        if (event.type == QUIT or
                (event.type == KEYDOWN and event.key == K_ESCAPE)):
            running = False

        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode(
                    (event.w, event.h), pygame.RESIZABLE)

        if event.type == KEYDOWN:
            if event.key == K_f:
                fullscreen = not fullscreen

                if fullscreen:
                    screen = pygame.display.set_mode(
                        monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(
                        (screen.get_width(), screen.get_height()),
                        pygame.RESIZABLE)

    # Run the timer.
    if matches < 8:
        ticks = pygame.time.get_ticks()

        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 1000 // 60)
        out = font.render(f'{minutes:02d}:{seconds:02d}', True,
            pygame.Color('DarkBlue')
        )
        screen.blit(out, (30, 30))
    else:
        screen.blit(out, (30, 30))


    for card in cards:
        # Update the size of the cards.
        card_w = (screen.get_width() - 30) * 0.75
        card_h = (screen.get_height() - 80) * 0.75
        card_size = int(min(card_w // 4, card_h // 4))

        card.x = 30 + (cards.index(card)%4)*(card_size + 10)
        card.y = 80 + (cards.index(card)//4)*(card_size + 10)
        card.w, card.h = card_size, card_size

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if len(cards_flipped) == 2:
            result = cards_flipped[0].check_match(cards_flipped[1])
            print(f"[{cards_flipped[0]}, {cards_flipped[1]}")
            print(result)

            if result:
                cards_flipped[0].matched = True
                cards_flipped[1].matched = True
                matches += 1
            else:
                cards_flipped[0].angle = 180
                cards_flipped[1].angle = 180
                cards_flipped[0].flipping = True
                cards_flipped[1].flipping = True
            cards_flipped.clear()

        if pygame.mouse.get_pressed()[0]:
            if (card.x < mouse_x < card.x + card.w and
                    card.y < mouse_y < card.y + card.h and
                    not card.matched and card not in cards_flipped):

                if len(cards_flipped) < 2:
                    card.flipping = True
                    cards_flipped.append(card)

        # Draw and update the card.
        card.update()
        card.draw(screen)

    main_clock.tick(60)
    pygame.display.update()

pygame.quit()
