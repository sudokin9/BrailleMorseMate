import signal
import sys

# Dictionaries for Braille, Morse code, and their reverse mappings
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 
    'z': '⠵', ' ': ' ', 
    '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
    '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚',
    ',': '⠂', ';': '⠆', ':': '⠒', '.': '⠲', '!': '⠖', 
    '(': '⠦', ')': '⠴', '?': '⠦', '/': '⠌', '\'': '⠄',
    '-': '⠤', '@': '⠈', '*': '⠔', '+': '⠖', '=': '⠶', 
}

reverse_braille_dict = {v: k for k, v in braille_dict.items()}

morse_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 
    'z': '--..', ' ': ' / ',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '\'': '.----.', 
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', 
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '@': '.--.-', '': ' '
}

reverse_morse_dict = {v: k for k, v in morse_dict.items()}

def text_to_braille(text):
    braille_text = ''
    for char in text.lower():
        braille_char = braille_dict.get(char, '')
        if braille_char:
            braille_text += braille_char
        else:
            braille_text += '?'  # Unknown character
    return braille_text

def braille_to_text(braille_text):
    text = ''
    for char in braille_text:
        text_char = reverse_braille_dict.get(char, '?')
        text += text_char
    return text

def text_to_morse(text):
    morse_text = ''
    for char in text.lower():
        morse_char = morse_dict.get(char, '')
        if morse_char:
            morse_text += morse_char + ' '
        else:
            morse_text += '? '  # Unknown character
    return morse_text

def morse_to_text(morse_text):
    morse_words = morse_text.split(' / ')
    text = ''
    for word in morse_words:
        morse_chars = word.split()
        for char in morse_chars:
            text_char = reverse_morse_dict.get(char, '?')
            text += text_char
        text += ' '
    return text.strip()

def signal_handler(sig, frame):
    print("\nExiting the program.")
    sys.exit(0)

# Set up signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

print("Welcome to the text converter. Choose the conversion type:")
print("0: Morse Code to Text")
print("1: Braille to Text")
print("2: Text to Braille")
print("3: Text to Morse Code")

while True:
    try:
        choice = input("\nEnter choice (0, 1, 2, or 3): ")
        if choice not in ['0', '1', '2', '3']:
            print("Invalid choice. Please enter 0, 1, 2, or 3.")
            continue
        
        if choice in ['1', '2', '3']:
            print("Enter text to convert:")
            user_input = input()
        elif choice == '0':
            print("Enter Morse code (use spaces between letters and / for word separation):")
            user_input = input()
        
        if choice == '1':
            result = braille_to_text(user_input)
            print(f"Text translation: {result}")
        elif choice == '2':
            result = text_to_braille(user_input)
            print(f"Braille translation: {result}")
        elif choice == '0':
            result = morse_to_text(user_input)
            print(f"Text translation: {result}")
        elif choice == '3':
            result = text_to_morse(user_input)
            print(f"Morse code translation: {result}")

    except EOFError:
        break
