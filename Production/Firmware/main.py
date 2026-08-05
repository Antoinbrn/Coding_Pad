print("Hackpad Testing!")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

print(dir(board))

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.D11, board.D10) # Col 0, Col 1
keyboard.row_pins = (board.D9, board.D8) # Row 0, Row 1
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB imports
rgb = RGB(pixel_pin=board.GP29, num_pixels=4)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    [
        KC.LTCL(KC.C), KC.LTCL(KC.V),
        KC.VOLU,        KC.VOLD,
    ]
]


if __name__ == '__main__':
    keyboard.go()