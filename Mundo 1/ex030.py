"""
30 - Crie um programa que leia um número inteiro qualquer e mostre na tela se
ele é par ou ímpar
"""
num = int(input('\033[35mDigite um número qualquer: \033[m'))
if num % 2 == 0:
    print(f'O número {num} é \033[34mPAR\033[m')
else:
    print(f'O número {num} é \033[34mÍMPAR\033[m.')
