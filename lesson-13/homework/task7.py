import numpy as np

matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())
print(normalized_matrix)

