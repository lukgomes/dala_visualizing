from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """Uma classe para gerar passeios aleatórios."""

    def __init__(self, num_points=5000):
        """Inicializa os atributos de um passeio."""
        self.num_points = num_points

        # Todos os passeios começam em (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos os pontos do passeio."""

        # Continua dando passos até que o passeio alence o tamanho desejado
        while len(self.x_values) < self.num_points:
            # Decide direção a ser seguida e distância a ser percorrida nessa direção
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejeita movimentos que não vão a lugar nenhum
            if x_step == 0 and y_step == 0:
                continue

            # Calcula os próximos valores de x e de y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


# Continua criando varios passeios aleatórios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove os eixos
    # A versão do livro deve funionar em versões antigas da lib
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    
    ax = plt.gca()
    ax.axis('off') # Retira bordas e eixos

    #ax.get_xaxis().set_visible(False) # Retira os eixos, porem deixa as bordas
    #ax.get_yaxis().set_visible(False)


    plt.show()

    keep_running = input("Make another walk: (y/n): ")
    if keep_running.lower() == 'n':
        break