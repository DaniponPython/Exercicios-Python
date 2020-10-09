"""
Crie um programa que leia um a frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
ex:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
"""
frase = input('Digite uma frase (sem acentos): ').replace(' ', '').upper()
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso += frase[c]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um Palíndromo')
