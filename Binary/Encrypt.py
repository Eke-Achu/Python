from pickle import dump

def encrypt(infilename, outfilename):
    with open(infilename, "r") as infile:

        with open(outfilename, "wb") as outfile:
            for line in infile:
                numbers = line.split()

                for number in numbers:
                    dump((eval(number) + 5), outfile)



def main():
    infilename = input("Enter an input filename: ").strip()
    outfilename = input("Enter an output filename: ").strip()

    encrypt(infilename, outfilename)

main()
