# morse_dict contains the mapping of English alphabets and digits to their respective Morse code representation
morse_dict = {
    'A': '.-',      'B': '-...', 
    'C': '-.-.',    'D': '-..', 
    'E': '.',       'F': '..-.', 
    'G': '--.',     'H': '....', 
    'I': '..',      'J': '.---', 
    'K': '-.-',     'L': '.-..', 
    'M': '--',      'N': '-.', 
    'O': '---',     'P': '.--.', 
    'Q': '--.-',    'R': '.-.', 
    'S': '...',     'T': '-', 
    'U': '..-',     'V': '...-', 
    'W': '.--',     'X': '-..-', 
    'Y': '-.--',    'Z': '--..',
    '0': '-----',   '1': '.----',
    '2': '..---',   '3': '...--',
    '4': '....-',   '5': '.....',
    '6': '-....',   '7': '--...',
    '8': '---..',   '9': '----.'
}

# to_morse_code function takes an input message as a string and returns the Morse code equivalent string of that message
def to_morse_code(message):
    morse_code = ''
    for char in message:
# if the character is not a space, it looks up the Morse code equivalent from morse_dict dictionary and appends it to the morse_code string
        if char != ' ':
            morse_code += morse_dict[char.upper()] + ' '
        else:
# if the character is a space, it appends a space to the morse_code string
            morse_code += ' '
    return morse_code

# to_text function takes a Morse code string as input and returns the equivalent English message string
def to_text(morse_code):
    message = ''
# morse_dict_reversed is the reverse mapping of morse_dict dictionary, used to get the English alphabets or digits from the Morse code equivalents
    morse_dict_reversed = {v: k for k, v in morse_dict.items()}
    for code in morse_code.split(' '):
# if the Morse code is not an empty string, it looks up the equivalent English alphabet or digit from morse_dict_reversed dictionary and appends it to the message string
        if code != '':
            message += morse_dict_reversed[code]
        else:
# if the Morse code is an empty string, it appends a space to the message string
            message += ' '
    return message

# the following code takes input from the user, converts it to Morse code or English message using the above functions and prints the output
message = input("Enter a message to translate to Morse code: ")
morse_code = to_morse_code(message)
print(morse_code)

morse_code = input("Enter Morse code to translate to text: ")
message = to_text(morse_code)
print(message)