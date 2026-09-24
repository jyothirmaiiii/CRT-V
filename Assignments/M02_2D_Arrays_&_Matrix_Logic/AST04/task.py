def diagonalSort(mat):
    m = len(mat)
    n = len(mat[0])

    for start_col in range(n):
        diagonal = []
        r, c = 0, start_col

        while r < m and c < n:
            diagonal.append(mat[r][c])
            r += 1
            c += 1

        diagonal.sort()

        r, c = 0, start_col
        i = 0

        while r < m and c < n:
            mat[r][c] = diagonal[i]
            r += 1
            c += 1
            i += 1

    for start_row in range(1, m):
        diagonal = []
        r, c = start_row, 0

        while r < m and c < n:
            diagonal.append(mat[r][c])
            r += 1
            c += 1

        diagonal.sort()

        r, c = start_row, 0
        i = 0

        while r < m and c < n:
            mat[r][c] = diagonal[i]
            r += 1
            c += 1
            i += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []

    for i in range(m):
        mat.append(list(map(int, input().split())))

    result = diagonalSort(mat)

    for row in result:
        print(*row)