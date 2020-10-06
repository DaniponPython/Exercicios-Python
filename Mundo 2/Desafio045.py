"""
Crie um programa que faça o computador jogar Jokenpô (pedra, papel, tesoura)
com você.
"""
from random import randint
from time import sleep
print('Suas opções:\n'
      '\t[ 0 ] PEDRA\n'
      '\t[ 1 ] PAPEL\n'
      '\t[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 14)
print(f'Computador jogou {itens[computador]}')
if jogador == 0 or jogador == 1 or jogador == 2:
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 14)
    if computador == jogador:
        print('EMPATE')
    elif (computador == 0 and jogador == 2) or \
         (computador == 1 and jogador == 0) or \
         (computador == 2 and jogador == 1):
        print('COMPUTADOR VENCE')
    else:
        print('JOGADOR VENCE')
else:
    print('Jogada inválida. Tente novamente, jogador!')
    print('-=' * 14)
