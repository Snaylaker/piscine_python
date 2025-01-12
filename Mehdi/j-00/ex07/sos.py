import sys
# Make a program that takes a string as an argument and encodes it into Morse Code.
# • The program supports space and alphanumeric characters
# • An alphanumeric character is represented by dots. and dashes-
# • Complete morse characters are separated by a single space
# • A space character is represented by a slash /
# You must use a dictionary to store your morse code.
# NESTED_MORSE = { " ": "/ ",
# "A": ".- ",
# ...
# If the number of arguments is different fro

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {' ': '/ ', 'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def main(args):
    if __name__ == "__main__":
        assert len(args) == 2, "the arguments are bad"

        assert all(c.isalnum() or c.isspace()
                   for c in args[1]), "the arguments are bad"

        for letter in args[1]:
            print(MORSE_CODE_DICT.get(letter.upper()), end="")


main(sys.argv)
