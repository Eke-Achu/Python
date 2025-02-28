from pickle import load

def decrypt(infilename, outfilename):
    with open(infilename, "rb") as infile:

        with open(outfilename, "w") as outfile:
            try:
                while True:
                    outfile.write(str(load(infile) - 5) + " ")
            except EOFError:
                print("All objects have been written to the output file")



def main():
    infilename = input("Enter an input filename: ").strip()
    outfilename = input("Enter an output filename: ").strip()

    decrypt(infilename, outfilename)

main()
