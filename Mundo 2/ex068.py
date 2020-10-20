"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""
from random import randint
from time import sleep

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
v = 0
while True:
    print()
    jogador = int(input('Digite um valor: '))
    opcao = ' '
    while opcao not in 'PI':
        opcao = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total deu '
          f'{jogador + computador}... ')
    print(f'{soma} é', end=' ')
    sleep(2)
    print('PAR' if soma % 2 == 0 else 'ÍMPAR')
    print('-' * 30)
    sleep(0.5)
    if (opcao == 'P' and soma % 2 == 0) or (opcao == 'I' and soma % 2 == 1):
        print('Você VENCEU!\n'
              'Vamos jogar novamente...')
        print('-=' * 15)
        v += 1
    else:
        print('Você PERDEU!')
        print('-=' * 15)
        break
print(f'GAME OVER! Você venceu {v} vez(es)')
