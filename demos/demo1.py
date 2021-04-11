"""
Random colors at every keypress

Save as code.py on your circuitpy drive.
"""

from rgbkeypad import RgbKeypad


def key_pressed(a_key):
    print(f"Pressed {a_key}")
    keypad.random_colors(x_range=4, y_range=4)


if __name__ == "__main__":
    # No need for params, the object will instanciate its I2C and SPI port drivers.
    keypad = RgbKeypad()
    keypad.random_colors(x_range=4, y_range=4)

    # Attach the on press handlers
    for key in keypad.keys:
        @keypad.on_press(key)
        def press_handler(a_key):
            key_pressed(a_key.number)

    # Required loop so the lib scans for touch events
    while True:
        keypad.update()
