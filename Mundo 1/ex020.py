"""
20- O mesmo professor do desafio anterior quer sortear a ordem de apresentação
dos trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
mostre a ordem sorteada.
"""
from random import shuffle

al1 = input('Primeiro aluno: ').title()
al2 = input('Segundo aluno: ').title()
al3 = input('Terceiro aluno: ').title()
al4 = input('Quarto aluno: ').title()
lista = [al1, al2, al3, al4]
shuffle(lista)
print(f'A ordem de apresentação seŕa: \n\033[1;30;41m{lista}\033[m')
