"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex: 5! = 5x4x3x2x1=120
"""
num = int(input('Digite um  número para\n'
                'calcular seu fatorial: '))
print(f'Calculando {num}!')
fatorial = 1

while num > 1:
    fatorial = fatorial * num
    print(f'{num} x', end=' ')
    num -= 1
print('1', end=' = ')
print(f'\033[31m{fatorial}\033[m')
