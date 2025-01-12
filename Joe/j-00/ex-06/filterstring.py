from ft_filter import ft_filter
import sys

def main():
    assert len(sys.argv) == 3, "Error: wrong number of argument"
    assert int(sys.argv[2]), "Second argument should be an int"

    words = sys.argv[1].split(" ")
    isGood = lambda str : len(str) >= int(sys.argv[2])
    res = ft_filter(isGood, words)
    print(res)

main()