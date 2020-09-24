"""
25 - Crie um programa que leia o nome de uma pessoa e diga se tem "SILVA"
"""
nome = input('Qual é o seu nome completo? ').strip().title()
print(f'Seu nome tem \033[1;35mSilva?\033[m \033[33m{"Silva" in nome}\033[m')
