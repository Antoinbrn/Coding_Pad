print("Hackpad Testing!")

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

#Extensions and modules
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_rgb import RGB, AnimationModes
from kmk.modules.macros import Macros, Press, Release, Tap, Delay

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

#Direct Matrix config
keyboard.row_pins = (board.D8, board.D7)
keyboard.col_pins = (board.D10, board.D9,board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#Rotary Encoder Config
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    # pin a, pin b, button pin
    (board.D4, board.D5, None),
)

encoder_handler.map = [
    (
        (KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.AUDIO_MUTE),
    )
]


rgb = RGB(
    pixel_pin = board.D6,
    num_pixel = 2,
    animation_mode = AnimationModes.STATIC,
    colors = [(51, 0, 102)]
)
keyboard.extensions.append(rbg)

#Custom macros
#opens Gmail
OPEN_GMAIL = KC.MACRO(
    Press(KC.LWIN),
    Tap(KC.R),
    Release(KC.LWIN),
    Delay(200),
    "https://gmail.com"
    Tap(KC.ENTER)
)

#Layout
keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.AUDIO_MUTE,

        OPEN_GMAIL, KC.CALCULATOR, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()