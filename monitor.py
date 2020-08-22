from pynput import mouse, keyboard


def get_coord(coords):
    def on_click(x, y, button, pressed):
        if not pressed:
            coords.append((x, y))
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()


def wait_monitoring_start():
    def on_press(key):
        try:
            if(key.char == 's'):
                return False
        except AttributeError:
            print('special key {0} pressed'.format(key))

    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
