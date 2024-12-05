A = [[1,2,5],
    [4,5,7]]

B = [[1,2,6],
    [4,5,7]]

C = [[1,2],
    [4,5],
    [7,8]]

def matrixMul(firstMatrix, secondMatrix):
    result = [[0 for _ in range(len(firstMatrix))] for _ in range(len(secondMatrix[0]))]
    try:
        if(len(firstMatrix) != len(secondMatrix[0])):
            raise TabError
        for a in range(len(firstMatrix)):
            for b in range(len(secondMatrix[0])):
                for c in range(len(secondMatrix)):
                        result[a][b] += firstMatrix[a][c] * secondMatrix[c][b]
        print(result)
    except TabError:
        print("Wrong matrix size!!!!!")


matrixMul(A,B)
matrixMul(B,C)
