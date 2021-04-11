# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

# This example demonstrates how to light keys when pressed.

# Drop the rgbkeypad.py file into your `lib` folder on your `CIRCUITPY` drive.

from rgbkeypad import RgbKeypad

# Set up keypad
keypad = RgbKeypad()
keys = keypad.keys

# Use cyan as the colour.
rgb = (0, 255, 255)

while True:
    # Always remember to call keypad.update() on every iteration of your loop!
    keypad.update()

    # Loop through the keys and set the LED to cyan if pressed, otherwise turn
    # it off (set it to black).
    for key in keys:
        if key.pressed:
            key.set_led(*rgb)
        else:
            key.set_led(0, 0, 0)
