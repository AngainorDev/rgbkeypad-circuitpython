# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

"""
* Originaly, this example displayed a rainbow animation on Keybow 2040's keys.
* This adaptation is for Pimoroni Pico RGB Keypad

* Author: Sandy Macdonald
* Author: Thierry Chantier

* Drop the rgbkeypad.py file into your `lib` folder on your `CIRCUITPY` drive.
"""

import math
import board
from rgbkeypad import RgbKeypad, number_to_xy, hsv_to_rgb

# Set up Keypad
keypad = RgbKeypad()
keys = keypad.keys

# Increment step to shift animation across keys.
step = 0

while True:
    # Always remember to call keypad.update() on every iteration of your loop!
    keypad.update()

    step += 1

    for i in range(16):
        # Convert the key number to an x/y coordinate to calculate the hue
        # in a matrix style-y.
        x, y = number_to_xy(i)

        # Calculate the hue.
        hue = (x + y + (step / 20)) / 8
        hue = hue - int(hue)
        hue = hue - math.floor(hue)

        # Convert the hue to RGB values.
        r, g, b = hsv_to_rgb(hue, 1, 1)

        # Display it on the key!
        keys[i].set_led(r, g, b)