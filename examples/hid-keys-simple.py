# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

# Original file was done for Keybow 2040
# Author: Sandy Macdonald

# Adaptation for Pimoroni RGB Keypad
# Author: Thierry Chantier

# A simple example of how to set up a keymap and HID keyboard on Pimoroni RGB Keypad.

# You'll need to connect Pimoroni RGB Keypad to a computer, as you would with a regular
# USB keyboard.

# Drop the rgbkeypad.py file into your `lib` folder on your `CIRCUITPY` drive.

# NOTE! Requires the adafruit_hid CircuitPython library also!

from rgbkeypad import RgbKeypad

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up Keypad
keypad = RgbKeypad()
keys = keypad.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# A map of keycodes that will be mapped sequentially to each of the keys, 0-15
keymap =    [Keycode.ZERO,
             Keycode.ONE,
             Keycode.TWO,
             Keycode.THREE,
             Keycode.FOUR,
             Keycode.FIVE,
             Keycode.SIX,
             Keycode.SEVEN,
             Keycode.EIGHT,
             Keycode.NINE,
             Keycode.A,
             Keycode.B,
             Keycode.C,
             Keycode.D,
             Keycode.E,
             Keycode.F]

# The colour to set the keys when pressed, yellow.
rgb = (255, 255, 0)

# Attach handler functions to all of the keys
for key in keys:
    # A press handler that sends the keycode and turns on the LED
    @keypad.on_press(key)
    def press_handler(key):
        keycode = keymap[key.number]
        print(keycode)
        keyboard.send(keycode)
        key.set_led(*rgb)

    # A release handler that turns off the LED
    @keypad.on_release(key)
    def release_handler(key):
        key.led_off()

while True:
    # Always remember to call keypad.update()
    keypad.update()