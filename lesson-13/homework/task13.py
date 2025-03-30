import numpy as np

matrix_3x3 = np.random.random((3, 3))
vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)
print(matrix_vector_product)

