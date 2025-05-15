from random import randint
import pygal

class Die():
    """Uma classe que representa um único dado."""

    def __init__(self, num_sides=6):
        """Supõe que seja um dado de seis lados."""
        self.num_sides = num_sides

    def roll(self):
        """Devolve um valor aleatório entre 1 e o número de lados."""
        return randint(1, self.num_sides)
    

die = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling on D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual_D6.svg')