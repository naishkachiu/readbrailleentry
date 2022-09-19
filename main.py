buttonBinary = ""
dot5 = 0
dot4 = 0
dot3 = 0
dot2 = 0
dot1 = 0
dot6 = 0
BrailleCode = [32, 48, 36, 38, 34, 52, 54, 50, 20, 22, 40, 56, 44, 46, 42, 60, 62, 58, 28, 30, 41, 57, 23, 45, 47, 43]
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def findInArray(bNum):
    global BrailleCode, Alphabet
    for i in range(0,len(BrailleCode)):
        if BrailleCode[i] == bNum:
            return Alphabet[i]
    return ""

def on_forever():
    global dot1, dot2, dot3, dot4, dot5, dot6, buttonBinary
    dot1 = pins.digital_read_pin(DigitalPin.P1)
    dot2 = pins.digital_read_pin(DigitalPin.P2)
    dot3 = pins.digital_read_pin(DigitalPin.P13)
    dot4 = pins.digital_read_pin(DigitalPin.P14)
    dot5 = pins.digital_read_pin(DigitalPin.P15)
    dot6 = pins.digital_read_pin(DigitalPin.P16)
    brailleNum = dot6*1 + dot5*2 + dot4*4 + dot3*8 + dot2*16 + dot1*32

    basic.show_string(findInArray(brailleNum))


basic.forever(on_forever)
