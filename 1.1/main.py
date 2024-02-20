import numpy as np

# Исходная матрица игры 5x5 (пример)
original_matrix = np.array([[8, 8, 6, 7, 8],
                             [7, 7, 6, 4, 9],
                             [10, 8, 9, 10, 8],
                             [3, 6, 9, -2, 8],
                             [7, 9, 9, 7, 10]])

print("Исходная матрица игры:")
print(original_matrix)

# Нормализация матрицы (приведение к неотрицательным элементам)
min_payoff = np.min(original_matrix)
if min_payoff < 0:
    original_matrix -= min_payoff

print("\nМатрица игры после нормализации:")
print(original_matrix)

# Поглощение доминируемых стратегий
row_max = np.max(original_matrix, axis=1)
col_min = np.min(original_matrix, axis=0)

dominated_rows = np.where(row_max == np.min(row_max))
dominated_cols = np.where(col_min == np.max(col_min))

if len(dominated_rows[0]) > 0 and len(dominated_cols[0]) > 0:
    new_matrix = np.delete(np.delete(original_matrix, dominated_rows, axis=0), dominated_cols, axis=1)
    print("\nМатрица игры после поглощения доминируемых стратегий:")
    print(new_matrix)
else:
    print("\nДоминируемых стратегий нет.")
