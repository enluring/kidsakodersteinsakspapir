def on_gesture_shake():
    global bildenummer
    bildenummer = randint(0, 2)
    basic.show_number(bildenummer)
    if bildenummer == 0:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # # # # #
                        . # # # .
                        . . # . .
        """)
    if bildenummer == 1:
        basic.show_leds("""
            . . . # #
            # . # . .
            . # . . .
            # . # . .
            . . . # #
        """)
    if bildenummer == 2:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # # #
                        . . . . .
                        . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

bildenummer = 0
tall = 5
while tall:
    basic.show_number(tall)
    basic.pause(100)
    tall = tall - 1