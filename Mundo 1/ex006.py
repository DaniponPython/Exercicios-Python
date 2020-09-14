"""
Crie um algoritmo que leia um número e mostre seu dobro, triplo e raíz quadrada
"""

# importando a função sqrt (raíz quadrada) da biblioteca math
from math import sqrt

n = int(input('Digite um número inteiro: '))
print(f'O dobro de \033[35m{n}\033[m é \033[31m{n * 2}\033[m')
print(f'O triplo de \033[35m{n}\033[m é \033[33m{n * 3}\033[m')
print(f'A raíz quadrada de \033[35m{n}\033[m é \033[34m{sqrt(n):.1f}\033[m')
