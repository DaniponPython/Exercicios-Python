"""
23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
num = int(input('Informe um número: '))
print('=*='*10)
print(f'\033[33mAnalisando o número {num}\033[m')
print('=*='*10)
print(f'Unidade: \033[31m{num % 10}\033[m\n'
      f'Dezena:\t \033[31m{num // 10 % 10}\033[m\n'
      f'Centena: \033[31m{num // 100 % 10}\033[m\n'
      f'Milhar:\t \033[31m{num // 1000}\033[m')
