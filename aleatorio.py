# Para importar la biblioteca random al completo
import random

# Para importar sólo determinadas funciones (randrange y choice)
from random import randrange, choice


char = "abcdasdfasdfasdf"
letra_aleatoria1 = random.choice(char)
letra_aleatoria2 = random.choice(char)
letra_aleatoria3 = random.choice(char)
letra_aleatoria4 = random.choice(char)
print(letra_aleatoria1,letra_aleatoria2,letra_aleatoria3,letra_aleatoria4)