"""
19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo esses nomes e escrevendo o nome do
escolhido.
"""
from random import choice

al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
alunos = [al1, al2, al3, al4]
print(f'O aluno escolhido foi \033[7m{choice(alunos).title()}\033[m.')
