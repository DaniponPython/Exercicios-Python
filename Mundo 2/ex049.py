"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for
"""
tabuada = int(input('Digite um número para ver sua tabuada: '))
for t in range(1, 11):
    print(f'{tabuada} x {t} = {tabuada * t}')
