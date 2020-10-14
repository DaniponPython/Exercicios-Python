"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos da sequencia de Fibonacci.
ex: 0 -> 1 -> 1 -> 2 -> -> 3 -> 5 -> 8
"""
print('-' * 24)
print(' SEQUENCIA DE FIBONACCI')
print('-' * 24)
termos = int(input('Quantos termos você quer mostrar? '))
termo_1 = 0
termo_2 = 1
contador = 2
print(termo_1, termo_2, sep=' -> ', end=' -> ')

while contador < termos:
    soma = termo_1 + termo_2
    print(soma, end=' -> ')
    termo_1 = termo_2
    termo_2 = soma
    contador += 1
print('FIM')
