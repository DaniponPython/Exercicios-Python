"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a
sua média
"""

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print(f'A média entre {nota1} e {nota2} é igual a {media:.1f}')
if media >= 7:
    print('\033[34mPARABÉNS\033[m! Você foi aprovado.')
else:
    print('Infelizmente você foi \033[31mREPROVADO\033[m! Estude mais.')
