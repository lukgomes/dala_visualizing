"""
Representando os quadrados e os cubos de uma lista numerica usando pontos
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 100))
y_values = [n**2 for n in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolors="none", s=40)

# Define o titulo do grafico e nomeia os eixos
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 110, 0, 10000])

plt.savefig('square_plot.png')
plt.savefig('square_plot2.png', bbox_inches='tight')
plt.show()

plt.scatter([1, 2, 3, 4, 5], [n**3 for n in range(1, 6)], c=([n**3 for n in range(1, 6)]), cmap=plt.cm.Reds,  edgecolors="none", s=40)
plt.show()