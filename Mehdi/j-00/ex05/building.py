import sys


def main(args):
    if __name__ == "__main__":
        # • If more than one argument is provided to the program, print an AssertionError
        assert not len(args) > 2

        # • If None or nothing is provided, the user is prompted to provide a string.
        if (len(args) == 1):
            sentence = str(input("What is the text to count ? \n"))
        else:
            sentence = args[1]

        spaceCounter = 0
        upperCasedCounter = 0
        lowerCasedCounter = 0
        punctuationCounter = 0
        digitsCounter = 0
        print(sentence)
        for char in sentence:
            if char.isspace():
                spaceCounter += 1
            if char.isupper():
                upperCasedCounter += 1
            if char.islower():
                lowerCasedCounter += 1
            if not char.isalpha() and not char.isdigit() and not char.isspace():
                punctuationCounter += 1
            if char.isdigit():
                digitsCounter += 1

    print("the text contains:", (upperCasedCounter + lowerCasedCounter + punctuationCounter + spaceCounter + digitsCounter), "\n", upperCasedCounter, "upper letters \n",
          lowerCasedCounter, "lower letters\n",
          punctuationCounter, "punctuation marks \n",
          spaceCounter, "space\n",
          digitsCounter, "digits\n")


main(sys.argv)
