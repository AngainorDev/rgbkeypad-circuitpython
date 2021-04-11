# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

# This example demonstrates attaching functions to keys using decorators, and
# the ability to turn the LEDs off with led_sleep_enabled and led_sleep_time.

# Drop the rgbkeypad.py file into your `lib` folder on your `CIRCUITPY` drive.

from rgbkeypad import RgbKeypad

# Set up keypad
keypad = RgbKeypad()
keys = keypad.keys

# Enable LED sleep and set a time of 5 seconds before the LEDs turn off.
# They'll turn back on with a tap of any key!
keypad.led_sleep_enabled = True
keypad.led_sleep_time = 5

# Loop through the keys and set the RGB colour for the keys to magenta.
for key in keys:
    key.rgb = (255, 0, 255)

    # Attach a `on_hold` decorator to the key that toggles the key's LED when
    # the key is held (the default hold time is 0.75 seconds).
    @keypad.on_hold(key)
    def hold_handler(key):
        key.toggle_led()

while True:
    # Always remember to call keypad.update()!
    keypad.update()
