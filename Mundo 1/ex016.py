""" Crie um programa que leia um número real qualquer pelo teclado e mostre na
tela a sua porção inteira.

Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""

# importando flor da biblioteca math
from math import floor

# floor arredonda o número para baixo
num = float(input('Digite um número real: '))
print(f'O número digitado foi \033[7m{num}\033[m e sua porção inteira é '
      f'\033[2;31;43m{floor(num)}\033[m.')
