import sys

def main():
    sys.tracebacklimit = 0
    if __name__ == "__main__":
        if (len(sys.argv) < 2):
            arg = input("What is the text to count? ")
        else:
            arg = sys.argv[1]
        assert not len(sys.argv) > 2, ": more than one argument is provided"
        counter = {
            "upper" : 0,
            "lower": 0,
            "space": 0,
            "digit": 0,
            "punctuation": 0
        }
        punctuation ="!.?,"
        for i in arg:
            if not i.isdigit() and not i.isalpha() and not i.isspace():
                counter["punctuation"] +=1
            elif i.isdigit():
                counter["digit"] += 1
            elif (i.isupper()):
                counter["upper"] += 1
            elif (i.islower()):
                counter["lower"] += 1
            elif (i.isspace()):
                counter["space"] += 1


            
        print("The text contains ", len(arg), " characters: ")
        print(counter["upper"], " upper letter",add_plural(counter["upper"]), sep="")
        print(counter["lower"], " lower letter",add_plural(counter["lower"]), sep="")
        print(counter["space"], " space",add_plural(counter["space"]), sep="")
        print(counter["digit"], " digit",add_plural(counter["digit"]), sep="")
        print(counter["punctuation"], " punctuation mark",add_plural(counter["punctuation"]), sep="")

  





def add_plural(count):
    if count > 1:
        return "s"
    return ""

main()