"""
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-
vindas
"""
nome = input('Digite seu nome: ')  # perguntando ao usuário

# usando format:
print('É um prazer te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

# usando f strings:
print(f'É um prazer te conhecer, \033[4;34m{nome}\033[m!')
# o nome vai aparecer sublinhado e na cor roxa
