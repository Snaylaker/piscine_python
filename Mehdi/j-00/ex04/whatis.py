import sys

sys.tracebacklimit = 0

if len(sys.argv) == 1:
    sys.exit(1)
else:
    assert not len(sys.argv) > 2, "more than one argument is provided"
    assert not type(sys.argv[1]) is int, "argument is not an integer"

print("I'm Even.") if int(sys.argv[1]) % 2 else print("I'm Odd")
