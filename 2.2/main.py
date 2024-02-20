import numpy as np

# Заданная платежная матрица
payoff_matrix = np.array([[8, 8, 6, 7, 8],
                          [7, 7, 6, 4, 9],
                          [10, 8, 9, 10, 8],
                          [3, 6, 9, -2, 8],
                          [7, 9, 9, 7, 10]])

print("Платежная матрица:")
print(payoff_matrix)
print()

# Размерность матрицы
num_rows, num_cols = payoff_matrix.shape

# Шаг 1: Нормализация платежной матрицы
normalized_matrix = (payoff_matrix - np.min(payoff_matrix)) / (np.max(payoff_matrix) - np.min(payoff_matrix))

print("Нормализованная платежная матрица:")
print(normalized_matrix)
print()

# Шаг 2: Расчет матрицы выигрышей
win_matrix = np.zeros((num_rows, num_cols))
for i in range(num_rows):
    for j in range(num_cols):
        win_matrix[i][j] = 1 - normalized_matrix[i][j]

print("Матрица выигрышей:")
print(win_matrix)
print()

# Шаг 3: Расчет оптимальных смешанных стратегий первого игрока
optimal_strategy_row = np.linalg.solve(win_matrix.T, np.ones(num_cols))
optimal_strategy_row /= np.sum(optimal_strategy_row)

print("Оптимальная смешанная стратегия первого игрока:")
print(optimal_strategy_row)
print()

# Шаг 4: Расчет оптимальных смешанных стратегий второго игрока
transposed_payoff_matrix = payoff_matrix.T

optimal_strategy_column = np.linalg.solve(transposed_payoff_matrix, np.ones(num_rows))
optimal_strategy_column /= np.sum(optimal_strategy_column)

print("Оптимальная смешанная стратегия второго игрока:")
print(optimal_strategy_column)
