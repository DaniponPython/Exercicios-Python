"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número
primo
"""
num = int(input('Digite um número inteiro: '))
contador = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[1;32m{c}\033[m', end=' ')
        contador += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {num} foi divisível {contador} vezes.')
if contador == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
