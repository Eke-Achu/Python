def LatinSquare():
    size = int(input("Enter number n:  "))

    latinSquare = getSquare(size)

    if latinSquare != None:
        if distinctColumns(latinSquare) and distinctRows(latinSquare):
            print("The input list is a latin square")
        else:
            print("The input list is not a latin square")
    else:
        print("Program terminated")



def getSquare(n):
    square = []

    print(f"Enter {n} rows of letters separated by spaces:")
    for i in range(n):
        currentRow = input().strip().split()

        if validRow(n, currentRow):
            square.append(currentRow)
        else: 
            print(f"Wrong input. The letters must be from A to {chr(ord('A') + (n - 1))}.")
            return

    return square



def validRow(n, row):
    maxChar = chr(ord('A') + (n - 1))

    for i in row:
        if i > maxChar:
            return False
        
    return True



def distinctRows(square):
    for i in range(len(square)):
        for j in range(len(square[i])):

            for row in range(len(square)):
                if row != i and square[i][j] == square[row][j]:
                    return False
    
    return True



def distinctColumns(square):
    for i in range(len(square[0])):
        for j in range(len(square)):

            for column in range(len(square[0])):
                if column != i and square[j][i] == square[j][column]:
                    return False
    
    return True


def main():
    LatinSquare()


main()