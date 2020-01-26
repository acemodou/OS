import sys


def _addCommandLineDigit():

    if len(sys.argv) > 1:
        total = sum([int(args) for args in sys.argv[1:] if args.isdigit()])
        print("Total is: {}".format(total))
    else:
        print("There is not enough arguments")


def _printCommandargs():

    if len(sys.argv) > 1:
        number = int(sys.argv[1])

        for i in range(number):
            print("Hello there")


if __name__=="__main__":
    _printCommandargs()
