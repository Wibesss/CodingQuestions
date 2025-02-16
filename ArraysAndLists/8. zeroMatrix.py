
def zeroMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rows = [False for x in range(n)]
    collums = [False for x in range(m)]
  
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows[i] = True
                collums[j] = True
                
    for i in range(n):
        if rows[i]: nullufyRow(matrix, i, m)
        
    for j in range(m):
        if collums[j]: nullufyCollum(matrix, j, n)
        
    return matrix


def nullufyRow(matrix, i, m):
    for j in range(m):
        matrix[i][j] = 0


def nullufyCollum(matrix, j, n):
    for i in range(n):
        matrix[i][j] = 0


print(zeroMatrix([[1,0,3],
                  [4,5,6],
                  [7,8,9]]))