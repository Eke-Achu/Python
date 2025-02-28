from AddMatrices import getMatrices
from AddMatrices import printMatrix

def multiplyMatrices():
    matrix1, matrix2 = getMatrices()

    print("The matrices are multiplied as follows:")

    printMatrix(matrix1)
    print(" * ")
    printMatrix(matrix2)
    print(" = ")
    printMatrix(multiplyMatrix(matrix1, matrix2))



def multiplyMatrix(matrix1, matrix2):
    result = []

    #Initializes the result list with the same number of rows as the first matrix
    #And the same number of columns as the second
    for i in range(len(matrix1)): 
        result.append([0 for x in range(len(matrix2[0]))])

    for row in range(len(matrix1)): #Represents the rows in matrix1

        for column in range(len(matrix2[0])): #Represents the columns in the second matrix
            sum = 0
 
            for i in range(len(matrix2)): #Traverses each element in the current column of matrix2
                sum += matrix1[row][i] * matrix2[i][column]

            result[row][column] = sum

    return result


def main():
    multiplyMatrices()


main()