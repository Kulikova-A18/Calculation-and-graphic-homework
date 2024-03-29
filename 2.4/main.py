import numpy as np
from scipy.optimize import linprog

# Платежная матрица
payoff_matrix = np.array([[8, 8, 6, 7, 8],
                            [7, 7, 6, 4, 9],
                            [10, 8, 9, 10, 8],
                            [3, 6, 9, -2, 8],
                            [7, 9, 9, 7, 10]])

# Коэффициенты целевой функции (минус т.к. ищем максимум)
c = [-1, -1, -1, -1, -1]

# Ограничения для вероятностей (сумма вероятностей равна 1)
A_eq = np.ones((1, 5))
b_eq = np.array([1])

# Ограничения для вероятностей (вероятности >= 0)
bounds = [(0, 1)] * 5

# Решение задачи линейного программирования с помощью симплекс-метода
res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Вывод результатов
print("Оптимальные смешанные стратегии для первого игрока:", res.x)

# Рассчитаем оптимальные стратегии для второго игрока
optimal_strategies_player2 = np.dot(payoff_matrix.T, res.x)
print("Оптимальные смешанные стратегии для второго игрока:", optimal_strategies_player2)
