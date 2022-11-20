input.onGesture(Gesture.Shake, function () {
    bildenummer = randint(0, 2)
    basic.showNumber(bildenummer)
    if (bildenummer == 0) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
    }
    if (bildenummer == 1) {
        basic.showLeds(`
            . . . # #
            # . # . .
            . # . . .
            # . # . .
            . . . # #
            `)
    }
    if (bildenummer == 2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            `)
    }
})
let bildenummer = 0
let tall = 5
while (tall) {
    basic.showNumber(tall)
    basic.pause(100)
    tall = tall - 1
}
