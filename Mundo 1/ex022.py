"""
22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome
"""

nome = input('Digite seu nome completo: ').strip()
tam = len(nome) - nome.count(' ')
div = nome.split()
print('\033[31mAnalisando seu nome...\033[m\n')
print(f'Seu nome em minúsculas é \033[33m{nome.lower()}\033[m.\n'
      f'Seu nome em maiúsculas é \033[31m{nome.upper()}\033[m.\n'
      f'Seu nome tem ao todo \033[36m{tam}\033[m letras.\n'
      f'Seu primeiro nomé é \033[4;34m{div[0].title()}\033[m e ele tem \033[34m{len(div[0])}\033[m letras.')

