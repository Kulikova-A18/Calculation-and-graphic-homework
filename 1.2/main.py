import numpy as np

# Заданная платежная матрица 5x5
payoff_matrix = np.array([[8, 8, 6, 7, 8],
                           [7, 7, 6, 4, 9],
                           [10, 8, 9, 10, 8],
                           [3, 6, 9, -2, 8],
                           [7, 9, 9, 7, 10]])

# # Заданная платежная матрица 2x2
# payoff_matrix = np.array([[8, 6],
#                            [7, 9]])

num_strategies = payoff_matrix.shape[0]

def is_NBR_strategy(strategy_index, opponent_strategies):
    for opp_strat in opponent_strategies:
        print(f'стратегия NBR: [{strategy_index}][{opp_strat}] [{strategy_index}][{strategy_index}] {payoff_matrix[strategy_index][opp_strat]} {payoff_matrix[strategy_index][strategy_index]}')
        if payoff_matrix[strategy_index][opp_strat] < payoff_matrix[strategy_index][strategy_index]:
            return False
    return True

def find_NBR_strategies(player_index):
    NBR_strategies = []
    for i in range(num_strategies):
        if is_NBR_strategy(i, [j for j in range(num_strategies) if j != player_index]):
            NBR_strategies.append(i)
    print(f'найдена стратегия NBR: {NBR_strategies}')
    return NBR_strategies

def remove_NBR_strategies(player_index, strategies_to_remove):
    global payoff_matrix
    global num_strategies
    reduced_payoff_matrix = np.delete(payoff_matrix, strategies_to_remove, axis=0)
    reduced_payoff_matrix = np.delete(reduced_payoff_matrix, strategies_to_remove, axis=1)
    payoff_matrix = reduced_payoff_matrix
    num_strategies = payoff_matrix.shape[0]
    print(f'матрица:  \n{payoff_matrix}')

# Итеративно удаляем NBR-стратегии до достижения равновесия Нэша
iteration = 1
while iteration < 5:
    print(f"Итерация {iteration}:")
    for i in range(num_strategies):
        NBR_strategies = find_NBR_strategies(i)
        if len(NBR_strategies) < num_strategies:
            print(f"Игрок {i + 1} удаляет стратегии: {NBR_strategies}")
            remove_NBR_strategies(i, NBR_strategies)

    if payoff_matrix.shape[0] == 1 or payoff_matrix.shape[1] == 1:
        print("<Достигнуто равновесие Нэша>")
        print("Смешанные стратегии игроков:")
        for i in range(num_strategies):
            mixed_strategy = [0] * num_strategies
            mixed_strategy[i] = 1
            print(f"Игрок {i + 1}: {mixed_strategy}")
        break

    if payoff_matrix.shape[0] == num_strategies or payoff_matrix.shape[1] == num_strategies:
        print("<Невозможно найти равновесие Нэша>")
        # break

    iteration += 1
