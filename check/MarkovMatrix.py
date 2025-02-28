def markovMatrix():
    print("Enter a 3-by-3 matrix row by row:")

    matrix = []

    for i in range(3):
        print(f"Enter row {i}: ", end = ' ')
        matrix.append([eval(x) for x in input().strip().split()])

    print("It is a Markov matrix" if allPositiveElements(matrix) and isMarkovMatrix(matrix) else \
        "It is not a Markov matrix")



def allPositiveElements(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                return False
            
    return True

def isMarkovMatrix(matrix):
    for column in range(len(matrix[0])):
        sum = 0

        for row in range(len(matrix)):
            sum += matrix[row][column]

        if sum != 1:
            return False
        
    return True

def main():
    markovMatrix()

main()