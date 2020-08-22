from pynput.mouse import Button, Controller
import time


mouse = Controller()

def flip_card(coords):
    time.sleep(2)
    mouse.position = coords
    mouse.press(Button.left)
    mouse.release(Button.left)
