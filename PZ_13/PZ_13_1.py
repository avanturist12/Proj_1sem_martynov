# в матрице найти минимальный элемент в предпоследнем столбце
import numpy as np

def find_minimum_element(matrix):

    if matrix.ndim != 2:
        raise ValueError("Input matrix must be a 2D array.")

    # Extract the second-to-last column
    second_last_column = matrix[:, -2]

    # Find the minimum element in the column
    minimum_element = second_last_column.min()

    return minimum_element

# Example usage
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

minimum_element = find_minimum_element(matrix)
print("Minimum element in the second-to-last column:", minimum_element)