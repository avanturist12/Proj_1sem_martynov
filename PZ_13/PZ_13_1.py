# в матрице найти минимальный элемент в предпоследнем столбце
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if __name__ == "main":
    import numpy

    mtx = numpy.array(matrix)
    print(min(mtx[2, :]))