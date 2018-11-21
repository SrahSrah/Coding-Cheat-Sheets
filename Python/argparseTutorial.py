# Can be run from command line with: python argparseTutorialargparseTutorial.py -strings hello 3 my test 5 -myInts 2 3 4 5 -sum


import argparse
parser = argparse.ArgumentParser(description="Add some ints")
parser.add_argument('-strings', metavar='a', type = str, nargs='+', help="string list, yo")
parser.add_argument("-myInts", metavar='b', type = int, nargs="+", help="some integers")
parser.add_argument("-sum", dest='accumulate', action="store_const", const = sum, default= max, help = "Sum the integers")


args = parser.parse_args()

for string in args.strings:
    print(string)

print("BREAK")

for anInt in args.myInts:
    print(anInt)

print("SUM THE INTS:")
print(args.accumulate(args.myInts))


# A complete reference can be found here: https://docs.python.org/3/library/argparse.html