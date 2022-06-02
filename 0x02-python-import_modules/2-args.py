#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    print("{} {}:".format(length, "arguments" if length > 1 else "argument"))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
