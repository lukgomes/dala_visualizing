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
    

die_1 = Die()
die_2 = Die(10)

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = [str(n) for n in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual_D6_D10.svg')