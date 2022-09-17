let buttonBinary = ""
let dot5 = 0
let dot4 = 0
let dot3 = 0
let dot2 = 0
let dot1 = 0
let dot6 = 0
let BrailleCode = [32, 48, 36, 38, 34, 52, 54, 50, 20, 22, 40, 56, 44, 46, 42, 60, 62, 58, 28, 30, 41, 57, 23, 45, 47, 43]
let Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
function findInArray(bNum: any): string {
    
    for (let i = 0; i < BrailleCode.length; i++) {
        if (BrailleCode[i] == bNum) {
            return Alphabet[i]
        }
        
    }
    return ""
}

basic.forever(function on_forever() {
    
    dot1 = pins.digitalReadPin(DigitalPin.P13)
    dot2 = pins.digitalReadPin(DigitalPin.P1)
    dot3 = pins.digitalReadPin(DigitalPin.P2)
    dot4 = pins.digitalReadPin(DigitalPin.P14)
    dot5 = pins.digitalReadPin(DigitalPin.P15)
    dot6 = pins.digitalReadPin(DigitalPin.P16)
    let brailleNum = dot6 * 1 + dot5 * 2 + dot4 * 4 + dot3 * 8 + dot2 * 16 + dot1 * 32
    basic.showString(findInArray(brailleNum))
})
