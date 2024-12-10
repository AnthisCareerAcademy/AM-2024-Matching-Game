from match_card import MatchCard
from random import shuffle

def generate_cards(screen_w, screen_h, card_set):
    """
    Generate a deck of matching cards.

    :param screen_w: Width of screen (to size cards proportionally).
    :param screen_h: Height of screen (to size cards proportionally).
    :param card_set: Which cards to use (letters [a-h, i-p, q-w], numbers).

    :return: Returns a deck of cards.
    """
    # Card generation code.
    card_w = (screen_w - 30) * 0.75
    card_h = (screen_h - 80) * 0.75
    # Keep the cards square.
    card_size = int(min(card_w // 4, card_h // 4))
    cards = []

    for i in range(4):
        for j in range(4):
            match card_set:
                case "numbers":
                    cards.append(MatchCard(
                        i + (j % 2 * 4), 30 + i*(card_size + 10),
                        80 + j*(card_size + 10), card_size, card_size,
                        f"images/memory-balls-{i+(j%2 * 4)+1}.jpg",
                        "images/card_back.png"
                    ))

                case _:
                    cards.append(MatchCard(
                        i + (j % 2 * 4), 30 + i * (card_size + 10),
                        80 + j * (card_size + 10), card_size, card_size,
                        f"images/memory-balls-{i + (j % 2 * 4) + 1}.jpg",
                        "images/card_back.png"
                    ))


    shuffle(cards)

    return cards