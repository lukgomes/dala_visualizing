"""
Desenha um grafico linear dos quadrados dos valores definidos em uma lista
"""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Define o titulo do Gráfico e nomeia os eixos
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamnho dos rótulos dasmarcações
plt.tick_params(axis='both', labelsize=14)
plt.show()
