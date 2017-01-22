ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
UALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphabet_position(letter):
    '''takes parameter letter and returns the index of that letter in the alphabet'''
    lowLetter = letter.lower()
    index = ALPHABET.index(lowLetter)
    return index


def rotate_character(char, rot):
    '''take a char and rot as parameter and returns index of the rotated letter in the amphabet'''
    return ALPHABET[(char + rot) % 26]


def encrypt(text, rot):
    '''takes text and rot as parameters and return encrypted text'''
    cipher = ''
    for char in text:
        if char.isalpha():
            newCharIndex = alphabet_position(char)
            newChar = rotate_character(newCharIndex, rot)
            if char in UALPHABET:
                cipher = cipher + newChar.upper()
            else:
                cipher = cipher + newChar
        else:
            cipher = cipher + char
    return cipher