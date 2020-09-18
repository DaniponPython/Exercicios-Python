"""
17 - Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo, calcule e mostre o comprimento da
hipotenusa.
"""
from math import hypot

print('\033[1;34mCalculando a hipotenusa de um triângulo retângulo\033[m\n')

co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
print(f'A hipotenusa vai medir \033[1;31m{hypot(co,ca):.2f}\033[m')
