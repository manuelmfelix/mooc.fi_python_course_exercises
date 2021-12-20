# Write your solution here
def transpose(matrix: list):
    # for row in matrix:
    #     matrix=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # print(matrix)
    a = []
    for b in range(len(matrix)):
        d = []
        for c in range(len(matrix[0])):
            d.append(matrix[b][c])
        a.append(d)
    print(a)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[c][r] = a[r][c]

    for r in matrix:
        print(r)

if __name__ == "__main__":
    m=([[1, 2], [1, 2]])
    transpose(m)