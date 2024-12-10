import pygame
from pygame.locals import *
from generate_cards import *

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

choosing = True

matches = 0
seconds, minutes = 0, 0

screen.fill((200, 215, 230))
font = pygame.font.SysFont('Arial', 34)

while choosing:
    choosing = False
    # TODO: implement set choosing here
    pygame.display.update()
    

cards = generate_cards(screen.get_width(), screen.get_height(), "numbers")

cards_flipped = []

# Code to make the window fullscreen.
while running:

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
        out = font.render(f'{minutes}:{seconds:02d}', True,
            pygame.Color('DarkBlue')
        )
        screen.blit(out, (30, 30))
    else:
        if pygame.time.get_ticks() % 800 < 400:
            out = font.render(f'{minutes}:{seconds:02d}', True,
                pygame.Color('ForestGreen')
            )
        else:
            out = font.render(f'{minutes}:{seconds:02d}', True,
                pygame.Color('DarkBlue')
            )
        screen.blit(out, (30, 30))


    for card in cards:
        # Update the size of the cards.
        card_w = (screen.get_width() - 60)
        card_h = (screen.get_height() - 160)
        card_size = int(min(card_w // 4, card_h // 4))

        card.x = 30+(cards.index(card)%4)*(card_size+10)
        card.y = 80+(cards.index(card)//4)*(card_size+10)
        card.w, card.h = card_size, card_size

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if (card.x < mouse_x < card.x + card.w and
                    card.y < mouse_y < card.y + card.h and
                    not card.face_up and not card.flipping and
                    not card.matched and card not in cards_flipped):

                if len(cards_flipped) < 2:
                    card.flipping = True
                    cards_flipped.append(card)

        # Check if the cards are both flipped face up.
        if (len(cards_flipped) == 2 and cards_flipped[0].face_up and
                cards_flipped[1].face_up and cards_flipped[1].angle == 0):

            result = cards_flipped[0].check_match(cards_flipped[1])

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

        # Draw and update the card.
        card.update()
        card.draw(screen)

    main_clock.tick(60)
    pygame.display.update()

pygame.quit()
