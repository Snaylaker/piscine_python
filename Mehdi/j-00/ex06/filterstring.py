import ft_filter
import sys
# Create a program that accepts two arguments: a string(S), and an integer(N). The
# program should output a list of words from S that have a length greater than N.
# • Strings do not contain any special characters. (Punctuation or invisible)


def main(args):
    if __name__ == "__main__":
        # • If the number of argument is different from 2, or if the type of any argument is wrong,
        # the program prints an AssertionError.
        assert len(args) == 3, "arguments are bad"
        # Create a program that accepts two arguments: a string(S), and an integer(N).
        assert int(args[2]), "argument is not an integer"

        S = str(args[1])
        N = int(args[2])

        # The program should output a list of words from S that have a length greater than N.
        words = S.split()

        # • The program must contain at least one list comprehension expression

        # and one lambda.
        filtered_words = ft_filter.ft_filter(lambda word: len(word) > N, words)

        for filtered_word in filtered_words:
            # • Words are separated from each other by space characters.
            print(filtered_word, end=" ")


main(sys.argv)
