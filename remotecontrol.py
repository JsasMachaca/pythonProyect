import random
from random import *
lista = []
for i in range(1, 10 + 1):
    lista.append(i)
    lista = sample(lista, i)
for j in lista:
    print(j)