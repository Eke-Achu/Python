from os.path import isfile

def displayUnique():
    filename = input("Enter a filename: ")

    if not isfile(filename):
        print(filename, "does not exist.")
        exit(9)

    infile = open(filename, "r")

    countWords = {}

    for line in infile:
        line = replacePunctuation(line)
        words = line.lower().split()
        
        for word in words:
            if word in countWords:
                countWords[word] += 1
            else:
                countWords[word] = 1

    distinctWords = []
    
    for key in countWords:
        if countWords[key] == 1:
            distinctWords.append(key)

    print(sorted(distinctWords))
    



def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, "")

    return line


def main():
    displayUnique()


main()
    