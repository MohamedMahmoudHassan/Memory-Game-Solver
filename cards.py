from pynput.mouse import Button, Controller
import time

mouse = Controller()


class Card:
    def __init__(self, pos, first_card_coords, delta, is_first_of_pair):
        self.pos = pos
        self.coords = (first_card_coords[0] + delta[0] * pos[0],
                       first_card_coords[1] + delta[1] * pos[1])
        self.sleep_time = 1.5 if is_first_of_pair else 0.1

    def flip(self):
        time.sleep(self.sleep_time)
        mouse.position = self.coords
        mouse.press(Button.left)
        mouse.release(Button.left)


def generate_cards(cards, first_card_coords, game_dim, delta):
    is_first_of_pair = True
    for x in range(game_dim[0]):
        for y in range(game_dim[1]):
            card = Card((x, y), first_card_coords, delta, is_first_of_pair)
            cards.append(card)
            is_first_of_pair = not is_first_of_pair
