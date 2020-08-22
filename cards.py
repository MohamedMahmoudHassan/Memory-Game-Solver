from pynput.mouse import Button, Controller
import time
import pyautogui
from PIL import Image
import imagehash

mouse = Controller()


class Card:
    def __init__(self, pos, first_card_coords, delta, is_first_of_pair):
        self.img_width = self.img_height = 65
        self.pos = pos
        self.coords = (first_card_coords[0] + delta[0] * pos[0],
                       first_card_coords[1] + delta[1] * pos[1])
        self.is_first_of_pair = is_first_of_pair
        self.matched = False

    def flip(self):
        time.sleep(1.2 if self.is_first_of_pair else 0)
        mouse.position = self.coords
        mouse.press(Button.left)
        mouse.release(Button.left)

    def flip_and_save(self):
        self.flip()
        time.sleep(0.5)
        self.save_img()

    def save_img(self):
        img = pyautogui.screenshot()
        self.img = img.crop(
            (self.coords[0] - self.img_width / 2, self.coords[1] - self.img_height / 2,
             self.coords[0] + self.img_width / 2, self.coords[1] + self.img_height / 2))


def generate_cards(cards, first_card_coords, game_dim, delta):
    is_first_of_pair = True
    for x in range(game_dim[0]):
        for y in range(game_dim[1]):
            card = Card((x, y), first_card_coords, delta, is_first_of_pair)
            cards.append(card)
            is_first_of_pair = not is_first_of_pair


def images_difference(img1, img2):
    return abs(imagehash.average_hash(img1) - imagehash.average_hash(img2))


def sort_comp(x):
    return x[0]

def clc_diffs(diffs, cards):
    for x in range(len(cards)):
        for y in range(x + 1, len(cards)):
            diffs.append(
                (images_difference(cards[x].img, cards[y].img), cards[x], cards[y]))
    diffs.sort(key=sort_comp)

def match(cards, diffs):
    for x in diffs:
        if x[1].matched or x[2].matched:
            continue
        x[1].matched = x[2].matched = True
        x[1].is_first_of_pair = True
        x[2].is_first_of_pair = False
        x[1].flip()
        x[2].flip()
