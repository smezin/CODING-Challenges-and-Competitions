M1 = [[0,1],[2,3]]
M2 = [[0,1,2],[3,4,5],[6,7,8]]
m = M2

def printm (m, title=''):
    print (title)
    for row in range(len(m)):
        print(m[row])
    print ('-'*8)

def rotate_matrix (matrix):
    rotated = [[None] * len(matrix)] * len(matrix)
    print(rotated)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = matrix[i][j]
            print(f'{matrix[i][j]} to {j},{n-i-1}')
            print(rotated)
    return rotated

def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A

def rotate_counter(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def rotate_clockwise(m):
    return [[m[i][j] for j in range(len(m))] for i in range(len(m[0]))]


def zero_matrix(m):
    zeros = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0
    printm(m, 'marked')
    for i in range(len(m)):
        if m[i][0] == 0:
            for j in range(len(m[i])):
                m[i][j] = 0
    for j in range(len(m[i])):
        if m[0][j] == 0:
            for i in range(len(m)):
                m[i][j] = 0
    return m

def string_rotation(s1,s2):
    print(len(s1), len(s2))
    if len(s1) != len(s2):
        return False
    n = len(s1)
    for i in range(n):
        print(f'{s1[:i]} in {s2[n-i:n]} and {s1[i:]} in {s2[:n-i]}')
        if s1[:i] in s2[n-i:] and s1[i:] in s2[:n-i]:
            return True
    return False

print(string_rotation('waterbottle','erbottlewat'))


#printm(m, 'original')
#printm(zero_matrix(m), 'zero')

#print(rotate_matrix([[1,2],[3,4]]))
#print([[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)])
#print(list(list(x) for x in zip(*M1))[::-1])
# printm(rotate_counter(m), 'rotate_counter')
# printm(rotate90Clockwise(m), 'rotate90Clockwise')
# printm (rotate_clockwise(m),'my rotate_clockwise')
