# в матрице найти минимальный элемент в предпоследнем столбце
def find(matrix):
    min_element = matrix[0][-2]
    for i in range(len(matrix)):
        if matrix[i][-2] < min_element:
            min_element = matrix[i][-2]
    return min_element


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

min_element = find(matrix)
print("Минимальный элемент в предпоследнем столбце матрицы:", min_element)
