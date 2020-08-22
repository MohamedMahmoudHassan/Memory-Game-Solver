from monitor import *
from cards import *

game_dim = (6, 5)

wait_monitoring_start()
coords = []
get_coord(coords)
get_coord(coords)

delta = ((coords[1][0] - coords[0][0]) / (game_dim[0] - 1),
         (coords[1][1] - coords[0][1]) / (game_dim[1] - 1))

cards = []
generate_cards(cards, coords[0], game_dim, delta)

for x in cards:
    x.flip_and_save()

diffs = []
clc_diffs(diffs, cards)
match(cards, diffs)
