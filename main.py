morse_codes = {
    'A': '.-',
    'B': '-..',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'

}

is_on = True
def morse_code():
    user_entry = input('What string would you like to convert?: ').upper()

    chars_of_user = []
    refactored = []

    for char in user_entry:
        chars_of_user.append(char)

    for item in chars_of_user:
        refactored.append(morse_codes[item])

    space = " "
    print(space.join(refactored))
    user_choice = input('Would you like to go again? Type Yes or No ').lower()
    if user_choice == 'no':
        is_on = False
    elif user_choice == 'yes':
        is_on = True
        morse_code()
morse_code()



