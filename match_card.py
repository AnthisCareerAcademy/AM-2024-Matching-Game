import pygame
import math

class MatchCard:
    """
    Class that models a memory-matching game card.

    Usage: Define a card using the constructor function. Inside the main
        game loop, draw a card with card.draw(screen), passing the pygame
        screen variable to the draw call. You will also need to update the
        card with card.update() every tick, and can even pass another card to
        it to check for matches. If there is a match, it will return True.
    """

    def __init__(self, value: int, x: int, y: int, w: int, h: int,
                 front: str, back: str):
        """
        Initialize the card with a value (so two cards can be matching) and
        a location.

        :param value: Value of the card (match it to another card).
        :param x: X-location of the top-left corner of the card.
        :param y: Y-location of the top-left corner of the card.
        :param w: Width of the card.
        :param h: Height of the card.
        :param front: Path to the image file for the front of the card.
        :param back: Path to the image file for the back of the card.
        """
        self.value = value

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.face_up = False
        self.angle = 0
        self.flipping = False
        self.matched = False

        self.image = pygame.image.load(front)
        self.draw_image = pygame.transform.scale(self.image, (self.w, self.h))
        self.image_rect = (self.x + self.w/2, self.y + self.h/2)

        self.back = pygame.image.load(back)
        self.draw_back = pygame.transform.scale(self.back, (self.w, self.h))
        self.back_rect = (self.x + self.w/2, self.y - self.h/2)

    def draw(self, screen):
        """
        Draw the card image on the screen.

        :return: Draws an image to the screen.
        """
        if self.matched or self.face_up:
            screen.blit(self.draw_image, self.image_rect)
        else:
            screen.blit(self.draw_back, self.back_rect)

    def update(self, other_card = None):
        """
        Flip the card when clicked and check for matches.

        :param other_card: The other card that has been flipped, to check for
            matches.

        :return: Flips the card with a nice animation. If the card matches the
            other card, then it remains face-up and returns True.
        """
        if not self.matched:
            size = (abs(math.cos(self.angle*math.pi/180)*self.w), self.h)

            self.image_rect = (self.x + self.w/2 - size[0]/2, self.y)
            self.back_rect = (self.x + self.w/2 - size[0]/2, self.y)

            self.draw_image = pygame.transform.scale(self.image, size)
            self.draw_back = pygame.transform.scale(self.back, size)

            if self.angle % 180 == 90:
                self.face_up = not self.face_up

            if self.flipping and self.angle <= 180:
                self.angle += 5

            if self.flipping and self.angle > 180:
                self.angle += 5

            if self.angle % 180 == 0 and self.flipping:
                self.flipping = False

            self.angle %= 180

            if other_card and other_card.value == self.value:
                self.matched = True
                return True
            else:
                self.flipping = True
                other_card.flipping = True
                return False
        else:
            self.angle = 0
            self.flipping = False