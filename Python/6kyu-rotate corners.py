"""
In this kata, you must write a function that expects a two-dimensional list matrix (minimum size: 2 x 2) as the only argument. The return value will be a two-dimensional list (size: 2 x 2) showing only the corners after n clockwise rotations.

Examples of corner values, rotation and corners-only return value: invalid as a kata test case, demonstration only!

# corners = 1, 2, 3, 4
# non-corners = 0
[[1, 0, 2],
 [0, 0, 0],
 [4, 0, 3]]

# above 2D list after a single clockwise rotation
[[4, 0, 1],
 [0, 0, 0],
 [3, 0, 2]]

# return value of above 2D list showing only the corners
[[4, 1],
 [3, 2]]

    The total number of clockwise rotations, n, is equal to the sum of all corner values multiplied by the sum of all non-corner values.
    Values in matrix are ASCII characters, booleans or integers. Use the integer values when determining the corner/non-corner sums.
        In the case of ASCII characters, use the corresponding ASCII value. A == 65, Z == 90, etc
        In the case of booleans, use the corresponding integer value. True/true == 1, False/false == 0

    matrix will always be a two-dimensional list (minimum size: 2 x 2)
    If the initial size of matrix is 2 x 2, no rotation is needed.

"""


def rotate_corners(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix
    m = []
    for i in matrix:
        m += [i[:]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) == int:
                continue
            elif matrix[i][j] == True:
                matrix[i][j] = 1
            elif matrix[i][j] == False:
                matrix[i][j] = 0
            else:
                matrix[i][j] = ord(matrix[i][j])
    corner = matrix[0][0] + matrix[len(matrix)-1][0] + matrix[0][len(matrix[0])-1] + matrix[len(matrix)-1][len(matrix[0])-1]
    noncorner = 0
    for i in range(len(matrix)):
        noncorner += sum(matrix[i])
    noncorner -= corner
    n = (corner * noncorner) % 4
    for i in range(n):
        m = rotate(m)[:]
    matrix = m[:]
    return [[matrix[0][0], matrix[0][len(matrix[0])-1]],[matrix[len(matrix)-1][0], matrix[len(matrix)-1][len(matrix[0])-1]]]
    
def rotate(matrix):
    matrix = matrix[::-1]
    m = []
    for j in range(len(matrix[0])):
        temp = []
        for i in range(len(matrix)):
            temp += [matrix[i][j]]
        m += [temp]
    return m
