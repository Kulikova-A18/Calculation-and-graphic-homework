import matplotlib.pyplot as plt

payoff_matrix = [[8, 8, 6, 7, 8],
                 [7, 7, 6, 4, 9],
                 [10, 8, 9, 10, 8],
                 [3, 6, 9, -2, 8],
                 [7, 9, 9, 7, 10]]

plt.imshow(payoff_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.show()
