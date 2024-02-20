import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
# Заданная платежная матрица
payoff_matrix = np.array([[8, 8, 6, 7, 8],
                          [7, 7, 6, 4, 9],
                          [10, 8, 9, 10, 8],
                          [3, 6, 9, -2, 8],
                          [7, 9, 9, 7, 10]])

# Размерность матрицы
num_rows, num_cols = payoff_matrix.shape

# Шаг 1: Построение графика платежной матрицы
plt.imshow(payoff_matrix, cmap='viridis', origin='upper')
plt.colorbar()
plt.title('Платежная матрица')
plt.xlabel('Столбцы')
plt.ylabel('Строки')
plt.xticks(range(num_cols))
plt.yticks(range(num_rows))
plt.show()

# Шаг 2: Поиск оптимальной смешанной стратегии первого игрока
c = [-1] * num_rows
A = payoff_matrix.T
b = [1] * num_cols
bounds = [(0, 1)] * num_rows

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

optimal_strategy_row = res.x

print("Оптимальная смешанная стратегия первого игрока:")
print(optimal_strategy_row)
print()

# Шаг 3: Поиск оптимальной смешанной стратегии второго игрока
c = [1] * num_cols
A = -payoff_matrix
b = [-1] * num_rows
bounds = [(0, 1)] * num_cols

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

optimal_strategy_column = res.x

print("Оптимальная смешанная стратегия второго игрока:")
print(optimal_strategy_column)
