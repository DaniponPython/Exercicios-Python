"""
Melhore o jogo 028 onde o computador vai 'pensar' em um número de 0 a 10. Só
que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
"""
from random import randint

print('Sou seu computador...\n'
      'Acabei de pesar em um número entre  0 e 10.\n'
      'Será que você consegue adivinhar qual foi?\n')

palpite_computador = randint(0, 10)
palpite_jogador = int(input('Qual é o seu palpite? '))
tentativas = 1
while palpite_computador != palpite_jogador:
    tentativas += 1
    if palpite_computador < palpite_jogador:
        palpite_jogador = int(input('É um número menor... Tente mais uma vez. '))
    else:
        palpite_jogador = int(input('É um número maior... Tente mais uma vez. '))
print(f'Acertou com {tentativas} tentativas. Parabéns')
