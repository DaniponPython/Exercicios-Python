"""
28 - Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.
O computador deverá escrever na tela se o usuário venceu ou perdeu.
"""
from time import sleep
from random import randint

print('\033[33m=*=\033[m' * 20)
print('\033[34mVou pensar em um número entre 1 e 5. Tente adivinhar...\033[m')
print('\033[33m=*=\033[m' * 20)

jogador = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(1)
computador = randint(1, 5)

if jogador == computador:
    print('\033[34mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[31mVocê perdeu! Eu pensei no número {computador} e não no '
          f'{jogador}.\033[m')
