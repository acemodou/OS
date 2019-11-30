import sys

if len(sys.argv) > 1:
    total = sum([int(args) for args in sys.argv[1:] if args.isdigit()])
    print("Total is: {}".format(total))
else:
    print("There is not enough arguments")