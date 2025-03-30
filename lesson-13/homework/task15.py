import numpy as np

matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
col_sums = matrix_5x5.sum(axis=0)
print("Row sums:", row_sums)
print("Column sums:", col_sums)

