"""
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while
"""
print('Gerador de PA')
print('=-' * 10)
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(inicio, end=' -> ')
    inicio += razao
    c += 1
print('FIM')