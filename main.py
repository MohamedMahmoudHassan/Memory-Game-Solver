from monitor import *
from cards import *

wait_monitoring_start()
coords = []
get_coord(coords)
get_coord(coords)

first_pos = (min(coords[0][0], coords[1][0]), min(coords[0][1], coords[1][1]))
flip_card(first_pos)
