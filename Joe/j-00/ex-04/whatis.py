import sys

sys.tracebacklimit = 0

def main():
    argv_len = len(sys.argv)
    if (argv_len > 1):
        assert not argv_len > 2, ": more than one argument is provided"
        assert sys.argv[1].isdigit(), " argument is not an integer"
        print("I'm even") if (int(sys.argv[1])%2 == 0) else print("I'm odd")

main()