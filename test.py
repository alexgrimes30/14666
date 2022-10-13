def fill_matrix(N, K, matrix):
    for n in range(N):
        for k in range(K):
            matrix[n][k] = 0.5 * k * (n ** 2 + n) - n ** 2 + 2 * n
    return matrix
s = [str(i) for i in input('Введите размеры матрицы и команду(если хотите)').split()]
N = int(s[0])
K = int(s[1])
matrix=[[0] * K for i in range(N)]
matrix = fill_matrix(N, K, matrix)
for i, item in enumerate(matrix):
    print(item)